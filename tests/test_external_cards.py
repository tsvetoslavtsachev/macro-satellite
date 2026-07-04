"""Tests for visualization.external_organism_cards — INIT-22 E1b external repackager.

Детерминистични, без мрежа/DuckDB: тестват ЧИСТАТА build(sources) над фикстури от
вече-извлечени примитиви (точно това, което load_sources връща). Доказват:
(1) 12/12 карти в заключената E1 schema v1 (gate Г1);
(2) reading=null на ВСЯКА карта (E1 s3 — външните органи нямат готова присъда);
(3) макро картата (приоритет №1) показва VRM<->табла side by side, China методология
    обявена, не скрита (сляпата точка става видима, но БЕЗ да се смята присъда — Г2);
(4) детерминизъм — build над същите sources е byte-identical (Г3);
(5) падне ли източник → картата свети available:false, честно (не тиха липса);
(6) stale флаг — as_of по-стар от каданса → stale=True (fail-loud).
"""
from __future__ import annotations

import json

from macro_satellite.visualization.external_organism_cards import (
    CARD_SCHEMA,
    build,
)

FIELDS = ["organ_id", "floor", "taxonomy_layer", "measures", "cadence", "horizon",
          "state", "reading", "epistemic_label", "as_of", "source", "schema_version"]
EXPECT_IDS = [
    "macro-regime", "barometer", "funding-radar", "etf-rotation", "oil", "ai-hype",
    "momentum-sp500", "momentum-stoxx", "rotation-sp500", "rotation-stoxx",
    "stock-selection", "satellite-synth",
]


def _sources_all_live() -> dict:
    """Пълен fixture — всичките 12 източника живи (примитивите, каквито load_sources
    произвежда). Датите ~2026-07-03 → близки до reference, за да НЕ са stale."""
    return {
        "macro": {
            "us": {"regime_key": "stagflation_confirmed",
                   "regime_label_bg": "Стагфлация (потвърдена)",
                   "primary_driver": "stagflation_test",
                   "cross_lens_divergences_count": 6, "composite_score": None,
                   "methodology": "tanh-z-lens", "as_of": "2026-06-27"},
            "eu": {"regime_key": "stagflation_confirmed",
                   "regime_label_bg": "Стагфлация (потвърдена)",
                   "primary_driver": "stagflation_test",
                   "cross_lens_divergences_count": 6, "composite_score": None,
                   "methodology": "tanh-z-lens", "as_of": "2026-06-27"},
            "cn": {"regime_key": "recessionary", "regime_label_bg": "РЕЦЕСИОНЕН",
                   "primary_driver": None, "cross_lens_divergences_count": 3,
                   "composite_score": 33.3, "methodology": "percentile-composite",
                   "as_of": "2026-06-29"},
        },
        "vrm": {"regime": "REFLATION", "as_of": "2026-06-26"},
        "momentum_us": {"as_of": "2026-07-03", "n_names_latest": 503,
                        "n_snapshots": 60, "score_field": "momentum_score"},
        "momentum_eu": {"as_of": "2026-07-03", "n_names_latest": 609,
                        "n_snapshots": 60, "score_field": "momentum_score"},
        "rotation_us": {"as_of": "2026-07-01", "n_names_latest": 131,
                        "n_snapshots": 40, "score_field": "current_rank/quadrant"},
        "rotation_eu": {"as_of": "2026-07-01", "n_names_latest": 200,
                        "n_snapshots": 40, "score_field": "current_rank/quadrant"},
        "stock_selection": {"as_of": "2026-07-03", "n_names_latest": 400,
                            "n_snapshots": 30, "score_field": "composite_score"},
        "satellite_state": {
            "week": {"label": "2026-W27", "end": "2026-07-05"},
            "triggered_patterns": [{"pattern_key": "x"}],
            "z_heatmap": {"symbols": ["SPY", "GLD", "TLT"]},
            "parallels_top3": [{"match_week": "2019-W10"}],
            "persistent_anomalies": {"us": [1, 2], "eu": [], "cn": [3]},
        },
        "oil": {
            "oil_wti_close": {"value": 68.78, "as_of": "2026-07-03"},
            "oil_brent_wti_spread": {"value": 3.1, "as_of": "2026-07-03"},
        },
        "funding": {"as_of": "2026-07-03T14:00:00+00:00", "verdict": "Спокойно",
                    "composite_score": 0.0,
                    "lamp_status": {"1": "green", "5": "green"},
                    "any_dead_source": False},
        "barometer": {"as_of": "2026-07-02",
                      "confluence": {"alarm_count": 0, "base_count": 10, "net": -10,
                                     "has_confluence": True, "direction": "base"},
                      "snapshot": [{"indicator": "HY-spread", "value": 2.76,
                                    "zone": "base", "trend": "down"},
                                   {"indicator": "VIX", "value": 15.0,
                                    "zone": "base", "trend": "flat"}]},
        "etf_rr": {"as_of": "2026-07-02", "etfs": [{"ticker": "XLE"}, {"ticker": "XLK"}]},
        "hype": {"hype_score": 68.1, "zone": {"label": "Повишен Hype"},
                 "quarter": "Q2 2026", "prev_score": 55.2, "change": 12.9,
                 "updated_at": "03.07.2026 16:37",
                 "components": {"market_momentum": {"score": 69.5},
                                "rhetoric": {"score": 60.0},
                                "valuation": {"score": 74.0}}},
        "_fetch_used": True,
    }


# ── Gate Г1: 12/12 карти в заключената схема ──────────────────────────────────

def test_all_twelve_cards_locked_schema():
    reg = build(_sources_all_live(), ref_date="2026-07-05")
    assert reg["n_cards"] == 12
    assert [c["organ_id"] for c in reg["cards"]] == EXPECT_IDS
    for c in reg["cards"]:
        assert list(c.keys()) == FIELDS, f"{c['organ_id']} schema drift"
        assert c["schema_version"] == CARD_SCHEMA
    # round-trips clean UTF-8
    json.loads(json.dumps(reg, ensure_ascii=False))


# ── E1 s3: reading=null на ВСЯКА външна карта ─────────────────────────────────

def test_reading_null_on_every_card():
    reg = build(_sources_all_live(), ref_date="2026-07-05")
    for c in reg["cards"]:
        assert c["reading"] is None, f"{c['organ_id']} carries a reading (must be E4)"


# ── Приоритет №1: макро картата прави сляпата точка видима (без присъда) ───────

def test_macro_regime_blind_spot_visible():
    reg = build(_sources_all_live(), ref_date="2026-07-05")
    mc = next(c for c in reg["cards"] if c["organ_id"] == "macro-regime")
    st = mc["state"]
    # трите региона + живия VRM режим седят side by side
    assert st["regions"]["us"]["regime_key"] == "stagflation_confirmed"
    assert st["regions"]["eu"]["regime_key"] == "stagflation_confirmed"
    assert st["regions"]["cn"]["regime_key"] == "recessionary"
    assert st["vrm_regime"] == "REFLATION"          # разминаването е ВИДИМО
    # China другата методология е ОБЯВЕНА, не скрита (Г7)
    assert st["regions"]["cn"]["methodology"] == "percentile-composite"
    assert st["regions"]["cn"]["composite_score"] == 33.3
    assert st["regions"]["us"]["methodology"] == "tanh-z-lens"
    assert st["regions"]["us"]["composite_score"] is None
    # но НИКАКВА присъда не се смята — reading=null (E4 територия)
    assert mc["reading"] is None
    assert mc["floor"] == "macro"


# ── Gate Г3: детерминизъм ─────────────────────────────────────────────────────

def test_deterministic_build():
    src = _sources_all_live()
    a = json.dumps(build(src, ref_date="2026-07-05"), ensure_ascii=False, indent=2)
    b = json.dumps(build(src, ref_date="2026-07-05"), ensure_ascii=False, indent=2)
    assert a == b


def test_reference_date_from_sources_when_unpinned():
    """Без ref_date → reference = max as_of от източниците (без wallclock → byte-stable)."""
    reg = build(_sources_all_live())
    # най-новата as_of е satellite week end 2026-07-05 (или momentum/stock 07-03)
    assert reg["reference_date"] >= "2026-07-03"


# ── Честен degrade: падне ли източник → available:false ───────────────────────

def test_dead_sources_are_honest():
    src = _sources_all_live()
    src["funding"] = None
    src["oil"] = None
    src["hype"] = None
    reg = build(src, ref_date="2026-07-05")
    by = {c["organ_id"]: c for c in reg["cards"]}
    for cid in ("funding-radar", "oil", "ai-hype"):
        assert by[cid]["state"]["available"] is False
        assert by[cid]["as_of"] is None
        assert by[cid]["reading"] is None
    assert set(reg["unavailable"]) == {"funding-radar", "oil", "ai-hype"}
    assert reg["n_unavailable"] == 3
    # живите съседи не са засегнати (жива карта НЕ носи поле available)
    assert by["macro-regime"]["state"]["regions"]["us"]["regime_key"] == "stagflation_confirmed"
    assert by["barometer"]["state"].get("available") is not False
    assert "barometer" not in reg["unavailable"]


def test_macro_region_missing_is_honest():
    src = _sources_all_live()
    src["macro"]["cn"] = None
    reg = build(src, ref_date="2026-07-05")
    mc = next(c for c in reg["cards"] if c["organ_id"] == "macro-regime")
    assert mc["state"]["regions"]["cn"] == {"available": False}
    # US/EU остават живи
    assert mc["state"]["regions"]["us"]["regime_key"] == "stagflation_confirmed"


# ── Stale флаг (fail-loud) ────────────────────────────────────────────────────

def test_stale_flag_on_old_source():
    src = _sources_all_live()
    # старим момента далеч назад спрямо reference 2026-07-05 (daily толеранс 4д)
    src["momentum_us"]["as_of"] = "2026-06-01"
    reg = build(src, ref_date="2026-07-05")
    by = {c["organ_id"]: c for c in reg["cards"]}
    assert by["momentum-sp500"]["state"]["stale"] is True
    assert "momentum-sp500" in reg["stale"]
    # свежите не са stale
    assert by["momentum-stoxx"]["state"]["stale"] is False


def test_fresh_sources_not_stale():
    reg = build(_sources_all_live(), ref_date="2026-07-05")
    # weekly органи (макро/funding/barometer) at 06-27..07-03, reference 07-05,
    # weekly толеранс 10д → не stale
    by = {c["organ_id"]: c for c in reg["cards"]}
    assert by["macro-regime"]["state"]["stale"] is False
    assert by["funding-radar"]["state"]["stale"] is False
    assert by["barometer"]["state"]["stale"] is False
