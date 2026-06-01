"""China macro_state интеграция (Фаза 5) — parser + схема + region taxonomy.

Offline; малък fixture. US/EU parser-ите нямат тестове (наследено) — тук покриваме
новия CN път + region→lens конфигурацията, която всички consumer-и ползват.
"""
from __future__ import annotations

from datetime import date

import pyarrow as pa

from macro_satellite.collectors.macro_state import parse_cn, parse_eu
from macro_satellite.config import MACRO_LENSES, MACRO_REGIONS, macro_lenses
from macro_satellite.storage.parquet_writer import _conform
from macro_satellite.storage.schema import get_schema, schema_columns


def test_macro_regions_includes_cn():
    assert "CN" in MACRO_REGIONS
    assert macro_lenses("CN") == ("growth", "inflation", "labor", "credit", "property")
    assert MACRO_LENSES["US"] == ("labor", "growth", "inflation", "liquidity")
    # EU credit-bug fix: реалната EU таксономия е credit (НЕ liquidity)
    assert MACRO_LENSES["EU"] == ("labor", "growth", "inflation", "credit")


# ── EU credit-lens taxonomy (bug fix) ────────────────────────────────────────

def test_parse_eu_credit_taxonomy(fixtures_dir):
    raw = (fixtures_dir / "eu_macro_state_mini.json").read_bytes()
    df = parse_eu(raw)
    assert len(df) == 1
    r = df.iloc[0]
    assert r["region"] == "EA"
    assert r["date"] == date(2026, 5, 30)
    # credit лещата се чете (НЕ се изпуска)
    assert r["credit_score"] == 62.0
    assert r["credit_direction"] == "expanding"
    assert r["credit_breadth_pct"] == 62.0
    # споделените лещи остават
    assert r["labor_score"] == 55.0 and r["inflation_score"] == 30.0
    # liquidity таксономията е премахната
    assert not any("liquidity" in c for c in df.columns)
    assert r["top_anomalies_count"] == 1
    assert r["cross_lens_divergences_count"] == 1


def test_eu_schema_credit_not_liquidity():
    cols = schema_columns("eu_macro_state")
    for lens in ("labor", "growth", "inflation", "credit"):
        assert f"{lens}_score" in cols
    assert not any("liquidity" in c for c in cols)


def test_parse_eu_conforms_to_eu_schema(fixtures_dir):
    raw = (fixtures_dir / "eu_macro_state_mini.json").read_bytes()
    df = parse_eu(raw)
    schema = get_schema("eu_macro_state")
    conformed = _conform(df, schema)
    assert set(df.columns) <= set(schema_columns("eu_macro_state"))
    tbl = pa.Table.from_pandas(conformed, schema=schema, preserve_index=False)
    assert tbl.num_rows == 1
    assert tbl.num_columns == len(schema)


def test_parse_us_still_liquidity():
    """US параметризацията остава непроменена (liquidity, не credit)."""
    from macro_satellite.collectors.macro_state import parse_us
    assert "liquidity_score" in schema_columns("us_macro_state")
    assert MACRO_LENSES["US"][-1] == "liquidity"


def test_parse_cn_basic(fixtures_dir):
    raw = (fixtures_dir / "cn_macro_state_mini.json").read_bytes()
    df = parse_cn(raw)
    assert len(df) == 1
    r = df.iloc[0]
    assert r["region"] == "CN"
    assert r["date"] == date(2026, 6, 1)
    assert r["composite_score"] == 30.4
    assert r["regime_key"] == "recessionary"
    # per-lens score/direction/regime
    assert r["credit_score"] == 71.5
    assert r["credit_direction"] == "expanding"
    assert r["property_score"] == 26.6
    assert r["growth_regime"] == "РЕЦЕСИЯ"
    # JSON expansions + counts
    assert r["top_anomalies_count"] == 2
    assert r["cross_lens_divergences_count"] == 1


def test_parse_cn_snapshot_override(fixtures_dir):
    raw = (fixtures_dir / "cn_macro_state_mini.json").read_bytes()
    df = parse_cn(raw, snapshot_date=date(2026, 1, 1))
    assert (df["date"] == date(2026, 1, 1)).all()


def test_parse_cn_conforms_to_schema(fixtures_dir):
    """Parser output трябва да пасва точно на CN_MACRO_STATE_SCHEMA (pyarrow cast)."""
    raw = (fixtures_dir / "cn_macro_state_mini.json").read_bytes()
    df = parse_cn(raw)
    schema = get_schema("cn_macro_state")
    conformed = _conform(df, schema)
    # никаква parser колона не остава извън схемата
    assert set(df.columns) <= set(schema_columns("cn_macro_state"))
    tbl = pa.Table.from_pandas(conformed, schema=schema, preserve_index=False)
    assert tbl.num_rows == 1
    assert tbl.num_columns == len(schema)


def test_cn_schema_has_composite_and_5_lenses():
    cols = schema_columns("cn_macro_state")
    assert "composite_score" in cols
    for lens in ("growth", "inflation", "labor", "credit", "property"):
        assert f"{lens}_score" in cols
        assert f"{lens}_regime" in cols


def test_expand_region_cn_empty_is_safe(isolated_storage):
    """Без CN данни — expand_region('CN') връща 0 rows, без crash (empty view)."""
    from macro_satellite.analytics.macro_anomalies_expander import expand_region
    from macro_satellite.storage.duckdb_conn import get_duck

    res = expand_region("CN", duck=get_duck())
    assert res.region == "CN"
    assert res.anomaly_rows == 0
    assert res.divergence_rows == 0
