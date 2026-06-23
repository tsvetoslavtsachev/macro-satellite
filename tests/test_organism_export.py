"""Tests for visualization.organism_export — VRM_WEEK parse + organism merge.

Детерминистични, без мрежа. Фикстурите имитират реалните формати (verified
2026-06-23). Доказват: (1) parse-ът извлича авторитетните VRM полета; (2) мъртъв
източник свети `available:false` (S14 честност), не нула; (3) cardinal rule —
парс провал → не гадаем формат.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

from macro_satellite.visualization.organism_export import (
    ORGANISM_SCHEMA_VERSION,
    build_organism_payload,
    parse_vrm_week,
)

# ── Фикстури (имитират verified формите 2026-06-23) ───────────────────────────

VRM_WEEK_FIXTURE = """# VRM_WEEK — Текуща Седмица

**Последна актуализация:** 2026-06-14
**Седмица:** 2026-06-08 → 2026-06-12

## 🔢 VRM ЯДРО

```
РЕЖИМ:            REFLATION
РЕЖИМ_БГ:         РЕФЛАЦИЯ
СИГНАЛ:           ЗАДРЪЖ (REFLATION 100%, 4-ти месец, Regime_Duration 4.0)
ALIGNMENT:        6.0
ALIGNMENT_MAX:    8
ALIGNMENT_LABEL:  ЧИСТ (макро) / оспорено пазарно поведение
GMS_SCORE:        5
GMS_MAX:          8
GMS_LABEL:        MEDIUM
```

## 🟢 KILL SWITCH

```
KS_АКТИВЕН:                  НЕ
KS_СТАТУС:                   ДЕАКТИВИРАН — CLEAR (Еп.8 архивиран)
```
"""

STATE_FIXTURE = {
    "week": {"label": "2026-W26", "start": "2026-06-22", "end": "2026-06-28"},
    "data_health": {
        "checked_at": "2026-06-23",
        "n_live": 8, "n_stale": 4, "n_missing": 0, "any_dead": True,
        "sources": {
            "etf_prices": {"table": "etf_prices", "status": "live",
                           "as_of": "2026-06-22", "days_stale": 1},
            "vrm_week": {"table": "vrm_week", "status": "stale",
                         "as_of": "2026-06-08", "days_stale": 15},
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

NOW = datetime(2026, 6, 23, 7, 0, tzinfo=timezone.utc)


# ── VRM_WEEK parse ────────────────────────────────────────────────────────────

def test_parse_vrm_week_core_fields():
    vrm = parse_vrm_week(VRM_WEEK_FIXTURE)
    assert vrm["available"] is True
    assert vrm["regime"] == "REFLATION"
    assert vrm["regime_bg"] == "РЕФЛАЦИЯ"
    assert vrm["signal"] == "ЗАДРЪЖ"          # token преди " ("
    assert vrm["alignment"] == "6/8"          # 6.0 → 6
    assert vrm["gms"] == "5/8 MEDIUM"
    assert vrm["ks_active"] is False          # "НЕ" → False
    assert vrm["as_of"] == "2026-06-14"
    assert vrm["source"] == "excel-frozen"    # strangler
    assert "ЧИСТ" in vrm["alignment_label"]


def test_parse_vrm_week_ks_active_true():
    md = VRM_WEEK_FIXTURE.replace("KS_АКТИВЕН:                  НЕ",
                                  "KS_АКТИВЕН:                  ДА")
    assert parse_vrm_week(md)["ks_active"] is True


def test_parse_vrm_week_bad_format_not_available():
    """Cardinal rule — липсва РЕЖИМ ядро → available:false, не гадаем."""
    vrm = parse_vrm_week("# случаен markdown без VRM ядро")
    assert vrm["available"] is False
    assert vrm["source"] == "excel-frozen"
    assert "error" in vrm


# ── Organism merge ────────────────────────────────────────────────────────────

def test_build_organism_all_live():
    p = build_organism_payload(STATE_FIXTURE, FUNDING_FIXTURE, BAROMETER_FIXTURE,
                               VRM_WEEK_FIXTURE, now=NOW)
    assert p["schema_version"] == ORGANISM_SCHEMA_VERSION
    assert p["week"] == "2026-W26"
    assert p["generated_at"] == "2026-06-23T07:00:00+00:00"

    # organism_health lift
    oh = p["organism_health"]
    assert (oh["n_live"], oh["n_stale"], oh["n_missing"]) == (8, 4, 0)
    assert oh["any_dead"] is True
    assert oh["sources"]["vrm_week"]["status"] == "stale"

    # vrm от VRM_WEEK (не от застоялия satellite vrm)
    assert p["vrm"]["gms"] == "5/8 MEDIUM"    # VRM_WEEK 5/8, не satellite 0.0
    assert p["vrm"]["as_of"] == "2026-06-14"

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

    # links блок присъства
    assert p["links"]["funding"].endswith("funding_state.json")

    # round-trips през JSON (UTF-8 чисто)
    json.loads(json.dumps(p, ensure_ascii=False))


def test_build_organism_dead_sources_honest():
    """Падне ли източник (None) → блокът свети available:false, не фалшива нула."""
    p = build_organism_payload(STATE_FIXTURE, None, None, None, now=NOW)
    assert p["funding"]["available"] is False
    assert "error" in p["funding"]
    assert p["barometer"]["available"] is False
    assert p["vrm"]["available"] is False
    assert p["vrm"]["source"] == "excel-frozen"
    # state-derived блокове остават живи (macro/health не зависят от външните фетчове)
    assert p["macro"]["us"]["regime"] == "stagflation_confirmed"
    assert p["organism_health"]["n_live"] == 8


def test_build_organism_missing_macro_region_is_none():
    state = {"week": {"label": "2026-W26"}, "data_health": {}, "regimes": {}}
    p = build_organism_payload(state, FUNDING_FIXTURE, BAROMETER_FIXTURE,
                               VRM_WEEK_FIXTURE, now=NOW)
    assert p["macro"]["us"] is None
    assert p["macro"]["eu"] is None
    assert p["macro"]["cn"] is None
