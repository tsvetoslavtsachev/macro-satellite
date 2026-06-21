"""S14 — staleness audit в cmd_collect: мъртъв/застоял канал не минава тихо зелено.

Чист gate върху `_stale_sources` (без I/O/мрежа). Доказва, че „успешен" collect
върху застоял source (HTTP 200, 1 ред, стара дата) се хваща над толеранса.
"""
from __future__ import annotations

from datetime import date

from macro_satellite.cli import _stale_sources
from macro_satellite.runner import DashboardResult


def test_stale_sources_flags_over_tolerance():
    today = date(2026, 6, 18)
    tol = {"vrm_state": 14, "etf_prices": 3, "us_macro_state": 7}
    successes = [
        # 18д > 14 → stale (точната VRM жертва: VRM_STATE.md от 31 май)
        DashboardResult(name="vrm_state", ok=True, rows_written=1, snapshot_date="2026-05-31"),
        # 2д ≤ 3 → fresh
        DashboardResult(name="etf_prices", ok=True, rows_written=47, snapshot_date="2026-06-16"),
        # 5д ≤ 7 → fresh
        DashboardResult(name="us_macro_state", ok=True, rows_written=1, snapshot_date="2026-06-13"),
    ]
    stale = _stale_sources(successes, tol, today)
    assert {s[0] for s in stale} == {"vrm_state"}
    name, snap, age, td = stale[0]
    assert snap == date(2026, 5, 31) and age == 18 and td == 14


def test_stale_sources_boundary_is_live():
    today = date(2026, 6, 18)
    tol = {"x": 14}
    # age == tolerable → НЕ stale (границата = live, консистентно с data_health)
    res = [DashboardResult(name="x", ok=True, rows_written=1, snapshot_date="2026-06-04")]  # 14д
    assert _stale_sources(res, tol, today) == []


def test_stale_sources_skips_missing_date_or_unconfigured():
    today = date(2026, 6, 18)
    tol = {"known": 7}
    res = [
        DashboardResult(name="known", ok=True, rows_written=0, snapshot_date=None),       # няма дата → skip
        DashboardResult(name="unknown", ok=True, rows_written=1, snapshot_date="2026-01-01"),  # няма толеранс → skip
    ]
    assert _stale_sources(res, tol, today) == []
