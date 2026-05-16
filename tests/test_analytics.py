"""Тестове за analytics: weekly windows, z-scores, divergence engine."""
from __future__ import annotations

from datetime import date

import pandas as pd

from macro_satellite.analytics.weekly_window import (
    current_week,
    iso_week_for,
    previous_week,
    trailing_weeks,
)


def test_iso_week_for_known_date():
    # Понеделник 11 май 2026 → W20 (но проверяваме endpoints)
    w = iso_week_for(date(2026, 5, 14))   # Thursday
    assert w.iso_week == 20
    assert w.week_start == date(2026, 5, 11)
    assert w.week_end == date(2026, 5, 17)
    assert w.label == "2026-W20"


def test_previous_week():
    w = iso_week_for(date(2026, 5, 14))
    p = previous_week(w)
    assert p.iso_week == 19
    assert p.week_end == date(2026, 5, 10)


def test_trailing_weeks_count():
    w = iso_week_for(date(2026, 5, 14))
    ws = trailing_weeks(w, 4)
    assert len(ws) == 4
    # Most recent (last in list) трябва да е previous_week(w)
    assert ws[-1].iso_week == 19
    assert ws[0].iso_week == 16


def test_iso_week_boundary_sunday():
    # Sunday 17 May 2026 → все още W20 по ISO
    w = iso_week_for(date(2026, 5, 17))
    assert w.iso_week == 20
    assert w.week_start == date(2026, 5, 11)


def test_iso_week_boundary_monday_next():
    # Monday 18 May 2026 → W21
    w = iso_week_for(date(2026, 5, 18))
    assert w.iso_week == 21
    assert w.week_start == date(2026, 5, 18)


def test_divergence_rules_load():
    from macro_satellite.analytics.divergence_engine import _load_rules
    rules = _load_rules()
    names = {p.name for p in rules.patterns}
    assert "stagflation_hint" in names
    assert "liquidity_stress" in names
    # Every pattern has at least 1 condition
    for p in rules.patterns:
        assert len(p.conditions) >= 1
        assert p.min_conditions_met <= len(p.conditions)
