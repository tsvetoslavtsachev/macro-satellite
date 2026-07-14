# -*- coding: utf-8 -*-
"""Phantom-bar guard: the US (NYSE) trading-day calendar (mandate #32-B).

The retired ``etf_dashboard_live`` collector wrote etf_prices bars on US market holidays with a
stale carried close (residue: 2026-06-19 Juneteenth, 2026-05-25 Memorial Day). These tests pin
the calendar that now DROPS any non-trading-day bar at the write boundary, and reproduce the
Juneteenth case end-to-end (06-19 -> row NOT written)."""
from __future__ import annotations

from datetime import date

import pandas as pd

from macro_satellite.utils.market_calendar import (
    drop_non_trading_days,
    easter_sunday,
    is_us_market_holiday,
    is_us_trading_day,
)


def test_the_two_phantom_holidays_are_non_trading():
    # The exact dates that produced phantom bars in etf_prices.
    assert is_us_market_holiday(date(2026, 6, 19))    # Juneteenth (observed)
    assert not is_us_trading_day(date(2026, 6, 19))
    assert is_us_market_holiday(date(2026, 5, 25))    # Memorial Day (last Mon of May 2026)
    assert not is_us_trading_day(date(2026, 5, 25))


def test_standard_nyse_holidays_2026():
    holidays = {
        date(2026, 1, 1):   "New Year's Day",
        date(2026, 1, 19):  "MLK Jr. Day (3rd Mon Jan)",
        date(2026, 2, 16):  "Washington's Birthday (3rd Mon Feb)",
        date(2026, 4, 3):   "Good Friday",
        date(2026, 5, 25):  "Memorial Day",
        date(2026, 6, 19):  "Juneteenth",
        date(2026, 7, 3):   "Independence Day (observed, Jul 4 = Sat)",
        date(2026, 9, 7):   "Labor Day (1st Mon Sep)",
        date(2026, 11, 26): "Thanksgiving (4th Thu Nov)",
        date(2026, 12, 25): "Christmas Day",
    }
    for d, name in holidays.items():
        assert is_us_market_holiday(d), f"{d} ({name}) should be a holiday"
        assert not is_us_trading_day(d), f"{d} ({name}) should not be a trading day"


def test_good_friday_via_easter():
    # 2026 Easter Sunday = 2026-04-05 -> Good Friday = 2026-04-03.
    assert easter_sunday(2026) == date(2026, 4, 5)
    assert is_us_market_holiday(date(2026, 4, 3))


def test_juneteenth_only_from_2022():
    # NYSE first observed Juneteenth in 2022; 2021-06-18/21 were normal sessions.
    assert not is_us_market_holiday(date(2021, 6, 18))   # Fri before (real session)
    assert is_us_market_holiday(date(2022, 6, 20))       # 2022 observed (Jun 19 = Sun)


def test_weekends_and_normal_days():
    assert not is_us_trading_day(date(2026, 6, 20))   # Saturday
    assert not is_us_trading_day(date(2026, 6, 21))   # Sunday
    # Normal weekday sessions (around the two phantom holidays)
    for d in [date(2026, 6, 18), date(2026, 6, 22), date(2026, 5, 22), date(2026, 5, 26)]:
        assert is_us_trading_day(d), f"{d} should be a trading session"


def test_drop_non_trading_days_filters_and_reports():
    df = pd.DataFrame([
        {"date": date(2026, 6, 18), "symbol": "SPY", "price": 746.0},   # Thu, session
        {"date": date(2026, 6, 19), "symbol": "SPY", "price": 746.74},  # Juneteenth -> DROP
        {"date": date(2026, 6, 22), "symbol": "SPY", "price": 747.0},   # Mon, session
        {"date": date(2026, 6, 20), "symbol": "SPY", "price": 999.0},   # Sat -> DROP
    ])
    kept, dropped = drop_non_trading_days(df, date_col="date")
    assert list(kept["date"]) == [date(2026, 6, 18), date(2026, 6, 22)]
    assert dropped == [date(2026, 6, 19), date(2026, 6, 20)]


def test_drop_accepts_timestamp_and_string_dates():
    df = pd.DataFrame([
        {"date": pd.Timestamp("2026-06-19"), "symbol": "LQD", "price": 108.77},  # DROP
        {"date": pd.Timestamp("2026-06-22"), "symbol": "LQD", "price": 108.78},  # keep
    ])
    kept, dropped = drop_non_trading_days(df)
    assert len(kept) == 1 and dropped == [date(2026, 6, 19)]

    df2 = pd.DataFrame([{"date": "2026-05-25", "symbol": "DBA", "price": 27.56}])  # Memorial Day
    kept2, dropped2 = drop_non_trading_days(df2)
    assert kept2.empty and dropped2 == [date(2026, 5, 25)]


def test_drop_empty_or_missing_column_is_noop():
    empty = pd.DataFrame(columns=["date", "symbol", "price"])
    kept, dropped = drop_non_trading_days(empty)
    assert kept.empty and dropped == []
    nocol = pd.DataFrame([{"symbol": "SPY", "price": 1.0}])
    kept2, dropped2 = drop_non_trading_days(nocol, date_col="date")
    assert len(kept2) == 1 and dropped2 == []
