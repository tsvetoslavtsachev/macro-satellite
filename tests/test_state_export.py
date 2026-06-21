"""Tests for visualization.state_export — JSON sidecar schema + bug fixes."""
from __future__ import annotations

import json

import pytest

from macro_satellite.visualization import state_export
from macro_satellite.visualization.state_export import (
    HEATMAP_SYMBOLS,
    SCHEMA_VERSION,
    bundle_to_dict,
    write_state_json,
)


def test_heatmap_symbols_no_duplicates():
    """Bug #5 от plan — HEATMAP_SYMBOLS не съдържа дубликати."""
    assert len(HEATMAP_SYMBOLS) == len(set(HEATMAP_SYMBOLS)), (
        f"Duplicates in HEATMAP_SYMBOLS: {HEATMAP_SYMBOLS}")


def test_schema_version_present():
    assert SCHEMA_VERSION == "1.0"


def test_state_export_integration_writes_valid_json(tmp_path):
    """End-to-end: build_state_bundle reads from prod DuckDB, write_state_json
    produces a valid JSON file with all required top-level keys.

    Този тест зависи от live storage — skip-ва ако DB е празна (CI clean state).
    """
    from macro_satellite.storage.duckdb_conn import get_duck
    duck = get_duck()

    # Skip ако няма данни
    try:
        n_rows = duck.execute("SELECT count(*) FROM etf_prices").fetchone()[0]
    except Exception:
        pytest.skip("etf_prices table missing — clean test environment")
    if n_rows == 0:
        pytest.skip("etf_prices table empty — no data to export")

    path, bundle = write_state_json(output_dir=tmp_path, duck=duck)
    assert path.exists()
    assert path.name == "state.json"

    data = json.loads(path.read_text(encoding="utf-8"))

    # Top-level schema
    required_keys = {
        "schema_version", "generated_at", "week", "regimes", "data_health",
        "week_movements_etf", "triggered_patterns", "all_patterns",
        "z_heatmap", "parallels_top3", "persistent_anomalies", "briefing_links",
    }
    missing = required_keys - set(data.keys())
    assert not missing, f"Missing top-level keys: {missing}"

    # S14 — data_health контракт присъства и е структуриран
    dh = data["data_health"]
    assert {"checked_at", "n_live", "n_stale", "n_missing",
            "any_dead", "sources"} <= set(dh.keys())
    assert isinstance(dh["sources"], dict) and dh["sources"]
    for name, e in dh["sources"].items():
        assert e["status"] in {"live", "stale", "missing"}, (name, e)

    # Schema version
    assert data["schema_version"] == "1.0"

    # Week structure
    assert "label" in data["week"]
    assert "start" in data["week"]
    assert "end" in data["week"]

    # z_heatmap не съдържа дубликати в symbols
    syms = data["z_heatmap"]["symbols"]
    assert len(syms) == len(set(syms))

    # Regimes — поне един от трите трябва да е populated ако имаме данни
    regimes = data["regimes"]
    assert set(regimes.keys()) >= {"vrm", "us_macro", "eu_macro"}


def test_bundle_to_dict_serialization():
    """Verify bundle_to_dict produces valid JSON-serializable dict."""
    from datetime import date as _date

    from macro_satellite.analytics.weekly_window import iso_week_for
    from macro_satellite.visualization.state_export import StateBundle

    fake_week = iso_week_for(_date(2026, 5, 14))
    bundle = StateBundle(
        week=fake_week,
        regimes={"vrm": None, "us_macro": None, "eu_macro": None, "cn_macro": None},
        week_movements_etf=[],
        triggered_patterns=[],
        all_patterns=[],
        z_heatmap={"symbols": [], "weeks": [], "week_ends": [], "matrix": []},
        parallels=[],
        persistent_us=[],
        persistent_eu=[],
        persistent_cn=[],
    )
    payload = bundle_to_dict(bundle)
    # Must round-trip through JSON
    serialized = json.dumps(payload, ensure_ascii=False)
    reloaded = json.loads(serialized)
    assert reloaded["week"]["label"] == "2026-W20"
    assert reloaded["schema_version"] == "1.0"
    # CN присъства в persistent_anomalies изхода (Фаза 5)
    assert "cn" in reloaded["persistent_anomalies"]


def test_classify_freshness_boundaries():
    """S14 — чистият статус-център: live/stale/missing граници."""
    from datetime import date as _date

    ref = _date(2026, 6, 18)
    # missing → as_of None
    assert state_export._classify_freshness(None, ref, 14) == ("missing", None)
    # days == tolerable → още live (границата принадлежи на live)
    assert state_export._classify_freshness(_date(2026, 6, 4), ref, 14) == ("live", 14)
    # days == tolerable + 1 → stale
    assert state_export._classify_freshness(_date(2026, 6, 3), ref, 14) == ("stale", 15)
    # пресен → live
    assert state_export._classify_freshness(ref, ref, 3) == ("live", 0)


def test_extract_data_health_synthetic():
    """S14 gate — forced-stale → stale, fresh → live, липсваща таблица → missing.

    Детерминистичен; не зависи от prod DB. Точно това доказва, че мъртвият
    канал ще свети червено (status != live), а не тихо зелено.
    """
    import duckdb
    from datetime import date as _date, timedelta

    from macro_satellite.config import load_dashboards_config

    cfg = load_dashboards_config()
    ref = _date(2026, 6, 18)
    con = duckdb.connect()  # in-memory

    # etf_prices = пресен (tolerable 3 → 0 дни → live)
    con.execute("CREATE TABLE etf_prices (date DATE)")
    con.execute("INSERT INTO etf_prices VALUES (?)", [ref])
    # vrm_state = 20 дни стар (tolerable 14 → stale) — жалбата на S14
    stale_day = ref - timedelta(days=20)
    con.execute("CREATE TABLE vrm_state (date DATE)")
    con.execute("INSERT INTO vrm_state VALUES (?)", [stale_day])
    # cot_monitor таблица НЕ съществува → missing

    dh = state_export._extract_data_health(con, ref, cfg=cfg)
    src = dh["sources"]

    assert src["etf_prices"]["status"] == "live"
    assert src["etf_prices"]["days_stale"] == 0

    assert src["vrm_state"]["status"] == "stale"
    assert src["vrm_state"]["days_stale"] == 20
    assert src["vrm_state"]["stale_tolerable_days"] == 14

    assert src["cot_monitor"]["status"] == "missing"
    assert src["cot_monitor"]["as_of"] is None

    assert dh["n_live"] >= 1 and dh["n_stale"] >= 1 and dh["n_missing"] >= 1
    assert dh["any_dead"] is True
    assert dh["checked_at"] == ref.isoformat()


def test_clean_value_handles_nan():
    """_clean_value трябва да конвертира NaN → None."""
    import math
    assert state_export._clean_value(math.nan) is None
    assert state_export._clean_value(math.inf) is None
    assert state_export._clean_value(-math.inf) is None
    assert state_export._clean_value(3.14) == 3.14
    assert state_export._clean_value(None) is None
    assert state_export._clean_value("hello") == "hello"
