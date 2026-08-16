"""Tests for visualization.organism_export — data-core-live VRM + organism merge.

Детерминистични, без мрежа. Фикстурите имитират реалните формати (verified
2026-06-27). Доказват: (1) живия overlay reader извлича авторитетните VRM полета;
(2) мъртъв източник свети `available:false` (S14 честност), не нула; (3) cardinal
rule — липсва ядро → не гадаем формат; (4) A3 strangler — липсва overlay → vrm
блокът е `available:false, source:"data-core-live"` (НЕ excel-frozen, НЕ фабрикуваме).
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

from macro_satellite.visualization.organism_export import (
    ORGANISM_SCHEMA_VERSION,
    build_organism_payload,
    read_vrm_from_datacore,
)

# ── Фикстури (имитират verified формите 2026-06-27) ───────────────────────────

# Жив data-core weekly overlay — списък седмични записи; reader-ът чете tip ([-1]).
VRM_OVERLAY_FIXTURE = [
    {"as_of": "2026-06-12", "regime": "GROWTH", "alignment_score": 5,
     "gms": {"score": 4, "max": 8, "tier": "LOW"},
     "kill_switch": {"active": False}},
    {"as_of": "2026-06-19", "regime": "REFLATION", "alignment_score": 6,
     "gms": {"score": 5, "max": 8, "tier": "MEDIUM"},
     "kill_switch": {"active": False}},
]

# Готовия data-core-live VRM блок (каквото read_vrm_from_datacore връща за tip-а горе).
VRM_BLOCK_FIXTURE = {
    "available": True,
    "source": "data-core-live",
    "regime": "REFLATION",
    "regime_bg": "РЕФЛАЦИЯ",
    "signal": None,
    "gms": "5/8 MEDIUM",
    "ks_active": False,
    "ks_status": "неактивен",
    "ks_as_of": "2026-06-19",
    "ks_stale": False,
    "as_of": "2026-06-19",
}

STATE_FIXTURE = {
    "week": {"label": "2026-W26", "start": "2026-06-22", "end": "2026-06-28"},
    "data_health": {
        "checked_at": "2026-06-27",
        "n_live": 8, "n_stale": 4, "n_missing": 0, "any_dead": True,
        "sources": {
            "etf_prices": {"table": "etf_prices", "status": "live",
                           "as_of": "2026-06-26", "days_stale": 1},
            "vrm": {"table": "vrm", "status": "live",
                    "as_of": "2026-06-19", "days_stale": 8},
        },
    },
    "regimes": {
        "vrm": {"as_of": "2026-05-31T00:00:00", "regime": "REFLATION",
                "gms_value": 0.0},
        "us_macro": {"as_of": "2026-06-20T00:00:00", "regime_key": "stagflation_confirmed",
                     "regime_label_bg": "Стагфлация (потвърдена)",
                     "cross_lens_divergences_count": 6},
        "eu_macro": {"as_of": "2026-06-20T00:00:00", "regime_key": "stagflation_confirmed",
                     "regime_label_bg": "Стагфлация (потвърдена)",
                     "cross_lens_divergences_count": 6},
        "cn_macro": {"as_of": "2026-06-22T00:00:00", "regime_key": "recessionary",
                     "regime_label_bg": "РЕЦЕСИОНЕН",
                     "cross_lens_divergences_count": 3},
    },
}

FUNDING_FIXTURE = {
    "schema_version": 1, "as_of": "2026-06-23T15:29:41+00:00",
    "composite_score": 0.0, "verdict": "Спокойно финансиране",
    "lamp_status": {"1": "green", "2": "green", "3": "green", "4": "green", "5": "green"},
    "any_dead_source": False,
}

BAROMETER_FIXTURE = {
    "as_of": "2026-06-22",
    "confluence": {"alarm_count": 0, "base_count": 10, "net": -10,
                   "has_confluence": True, "direction": "base"},
}

NOW = datetime(2026, 6, 27, 7, 0, tzinfo=timezone.utc)


# ── data-core-live VRM reader ─────────────────────────────────────────────────

def test_read_vrm_from_datacore_tip(tmp_path):
    """Чете tip-а ([-1]) на overlay-а → авторитетните VRM полета, source live."""
    (tmp_path / "vrm_overlay.json").write_text(
        json.dumps(VRM_OVERLAY_FIXTURE), encoding="utf-8")
    (tmp_path / "vrm_ks_state.json").write_text(
        json.dumps([{"as_of": "2026-06-19", "active": False}]), encoding="utf-8")
    vrm = read_vrm_from_datacore(tmp_path)
    assert vrm is not None
    assert vrm["available"] is True
    assert vrm["source"] == "data-core-live"
    assert vrm["regime"] == "REFLATION"        # tip, не GROWTH от по-старата седмица
    assert vrm["regime_bg"] == "РЕФЛАЦИЯ"
    assert "alignment" not in vrm              # С3 Д3.1: свален от клиентския канал
    assert vrm["gms"] == "5/8 MEDIUM"
    assert vrm["ks_active"] is False
    assert vrm["ks_as_of"] == "2026-06-19"     # Д5.4: KS датата пътува с обсерваторията
    assert vrm["ks_stale"] is False            # равни дати => не е stale
    assert vrm["as_of"] == "2026-06-19"
    assert vrm["signal"] is None               # мозъкът не emit-ва еднословен сигнал


def test_read_vrm_from_datacore_stale_ks(tmp_path):
    """Д5.4: изоставащ (или липсващ) vrm_ks_state → ks_stale=True."""
    (tmp_path / "vrm_overlay.json").write_text(
        json.dumps(VRM_OVERLAY_FIXTURE), encoding="utf-8")
    (tmp_path / "vrm_ks_state.json").write_text(
        json.dumps([{"as_of": "2026-06-12", "active": False}]), encoding="utf-8")
    vrm = read_vrm_from_datacore(tmp_path)
    assert vrm["ks_stale"] is True
    assert vrm["ks_as_of"] == "2026-06-12"
    # липсващ KS state файл → също stale (честен канал)
    (tmp_path / "vrm_ks_state.json").unlink()
    vrm2 = read_vrm_from_datacore(tmp_path)
    assert vrm2["ks_stale"] is True and vrm2["ks_as_of"] is None


def test_read_vrm_from_datacore_missing_file(tmp_path):
    """Липсва overlay файл → None (caller ще светне available:false)."""
    assert read_vrm_from_datacore(tmp_path) is None


def test_read_vrm_from_datacore_no_regime(tmp_path):
    """Cardinal rule — tip без РЕЖИМ ядро → None, не гадаем формат."""
    (tmp_path / "vrm_overlay.json").write_text(
        json.dumps([{"as_of": "2026-06-19", "alignment_score": 6}]), encoding="utf-8")
    assert read_vrm_from_datacore(tmp_path) is None


# ── Organism merge ────────────────────────────────────────────────────────────

def test_build_organism_all_live():
    p = build_organism_payload(STATE_FIXTURE, FUNDING_FIXTURE, BAROMETER_FIXTURE,
                               VRM_BLOCK_FIXTURE, now=NOW)
    assert p["schema_version"] == ORGANISM_SCHEMA_VERSION
    assert p["week"] == "2026-W26"
    assert p["generated_at"] == "2026-06-27T07:00:00+00:00"

    # organism_health lift
    oh = p["organism_health"]
    assert (oh["n_live"], oh["n_stale"], oh["n_missing"]) == (8, 4, 0)
    assert oh["any_dead"] is True
    assert oh["sources"]["vrm"]["status"] == "live"

    # vrm = живия data-core-live блок
    assert p["vrm"]["source"] == "data-core-live"
    assert p["vrm"]["gms"] == "5/8 MEDIUM"
    assert p["vrm"]["as_of"] == "2026-06-19"

    # funding
    assert p["funding"]["available"] is True
    assert p["funding"]["composite"] == 0.0
    assert p["funding"]["lamps"]["3"] == "green"

    # barometer
    assert p["barometer"]["available"] is True
    assert p["barometer"]["net"] == -10
    assert p["barometer"]["direction"] == "base"

    # macro (от state, вече агрегирано)
    assert p["macro"]["us"]["regime"] == "stagflation_confirmed"
    assert p["macro"]["us"]["label"] == "Стагфлация (потвърдена)"
    assert p["macro"]["cn"]["regime"] == "recessionary"
    assert p["macro"]["cn"]["as_of"] == "2026-06-22"

    # links блок присъства, БЕЗ vrm (VRM_WEEK.md вече не е card източник — A3)
    assert p["links"]["funding"].endswith("funding_state.json")
    assert "vrm" not in p["links"]

    # round-trips през JSON (UTF-8 чисто)
    json.loads(json.dumps(p, ensure_ascii=False))


def test_build_organism_dead_sources_honest():
    """Падне ли източник (None) → блокът свети available:false, не фалшива нула."""
    p = build_organism_payload(STATE_FIXTURE, None, None, None, now=NOW)
    assert p["funding"]["available"] is False
    assert "error" in p["funding"]
    assert p["barometer"]["available"] is False
    assert p["vrm"]["available"] is False
    # state-derived блокове остават живи (macro/health не зависят от външните фетчове)
    assert p["macro"]["us"]["regime"] == "stagflation_confirmed"
    assert p["organism_health"]["n_live"] == 8


def test_build_organism_missing_vrm_overlay_not_excel():
    """A3 strangler — липсва overlay (vrm_block=None) → available:false със
    source=data-core-live (НЕ excel-frozen, НЕ фабрикуваме). Excel мрежата е махната."""
    p = build_organism_payload(STATE_FIXTURE, FUNDING_FIXTURE, BAROMETER_FIXTURE,
                               None, now=NOW)
    vrm = p["vrm"]
    assert vrm["available"] is False
    assert vrm["source"] == "data-core-live"
    assert "excel" not in vrm["source"]       # старата опашка я няма
    assert "error" in vrm
    # съседните живи блокове не са засегнати
    assert p["funding"]["available"] is True
    assert p["barometer"]["available"] is True


def test_build_organism_missing_macro_region_is_none():
    state = {"week": {"label": "2026-W26"}, "data_health": {}, "regimes": {}}
    p = build_organism_payload(state, FUNDING_FIXTURE, BAROMETER_FIXTURE,
                               VRM_BLOCK_FIXTURE, now=NOW)
    assert p["macro"]["us"] is None
    assert p["macro"]["eu"] is None
    assert p["macro"]["cn"] is None
