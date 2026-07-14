# -*- coding: utf-8 -*-
"""US equity-market (NYSE) trading-day calendar — the phantom-bar guard.

WHY (mandate #32-B, 2026-07-14). The RETIRED ``etf_dashboard`` live collector stamped an
etf_prices row with ``updatedAt.date()`` — the ETF-Dashboard's own daily REGENERATION
timestamp — WITHOUT checking that a real market session occurred that day. The ETF-Dashboard
regenerated on US market holidays too, carrying the prior session's STALE close, so the
satellite wrote a bar on a NON-TRADING day (a "phantom bar"). Confirmed residue in
``etf_prices``: 2026-06-19 (Juneteenth, 88 symbols) and 2026-05-25 (Memorial Day, 85 symbols),
both sourced ``etf_dashboard_live`` — including SPY/QQQ, which cannot trade on those days.

A legitimate daily CLOSE can only exist on a real trading session. So the fix is a hard
guard at the etf_prices write boundary: any row dated on a non-trading day (weekend or NYSE
holiday) is DROPPED, never carried forward with a stale price. ``drop_non_trading_days`` is
applied by BOTH current writers (``run_price_ingest_base_first``, ``run_yf_backfill``). Today's
upstreams (yfinance ``history`` and the canonical archive) only ever emit real sessions, so in
normal operation this filter drops nothing — it is defence-in-depth that makes the phantom-bar
class impossible regardless of which upstream feeds etf_prices in the future.

Zero external dependency: NYSE holidays are computed from rules (Easter via the Anonymous
Gregorian algorithm for Good Friday), so no ``pandas_market_calendars`` / network / data file.
Scope = US equity market (the etf_prices universe is US-listed ETFs).
"""
from __future__ import annotations

from datetime import date, timedelta

__all__ = ["easter_sunday", "is_us_market_holiday", "is_us_trading_day",
           "drop_non_trading_days"]


def easter_sunday(year: int) -> date:
    """Western (Gregorian) Easter Sunday — Anonymous Gregorian algorithm. Good Friday = -2 days."""
    a = year % 19
    b, c = divmod(year, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    wk = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * wk) // 451
    month = (h + wk - 7 * m + 114) // 31
    day = ((h + wk - 7 * m + 114) % 31) + 1
    return date(year, month, day)


def _nth_weekday(year: int, month: int, weekday: int, n: int) -> date:
    """The ``n``-th ``weekday`` (Mon=0..Sun=6) of ``month`` in ``year`` (n>=1)."""
    d = date(year, month, 1)
    offset = (weekday - d.weekday()) % 7
    return d + timedelta(days=offset + 7 * (n - 1))


def _last_weekday(year: int, month: int, weekday: int) -> date:
    """The LAST ``weekday`` of ``month`` in ``year`` (e.g. Memorial Day = last Monday of May)."""
    if month == 12:
        nxt = date(year + 1, 1, 1)
    else:
        nxt = date(year, month + 1, 1)
    last = nxt - timedelta(days=1)
    return last - timedelta(days=(last.weekday() - weekday) % 7)


def _observed(d: date) -> date:
    """NYSE fixed-date holiday observance: Saturday -> Friday, Sunday -> Monday."""
    if d.weekday() == 5:            # Saturday
        return d - timedelta(days=1)
    if d.weekday() == 6:            # Sunday
        return d + timedelta(days=1)
    return d


def is_us_market_holiday(d: date) -> bool:
    """True if ``d`` is a full-day NYSE holiday closure (not counting weekends).

    Covers the 9 standard NYSE holidays + Good Friday + Juneteenth (NYSE observance began 2022).
    Half-days (e.g. the day after Thanksgiving) are NOT closures and stay trading days."""
    y = d.year

    # Fixed-date, weekend-observed
    if d == _observed(date(y, 1, 1)):        # New Year's Day
        return True
    if d == _observed(date(y, 7, 4)):        # Independence Day
        return True
    if d == _observed(date(y, 12, 25)):      # Christmas Day
        return True
    # Juneteenth — NYSE first observed it in 2022
    if y >= 2022 and d == _observed(date(y, 6, 19)):
        return True

    # Floating Monday/Thursday holidays
    if d == _nth_weekday(y, 1, 0, 3):        # MLK Jr. Day — 3rd Monday of January
        return True
    if d == _nth_weekday(y, 2, 0, 3):        # Washington's Birthday — 3rd Monday of February
        return True
    if d == _last_weekday(y, 5, 0):          # Memorial Day — last Monday of May
        return True
    if d == _nth_weekday(y, 9, 0, 1):        # Labor Day — 1st Monday of September
        return True
    if d == _nth_weekday(y, 11, 3, 4):       # Thanksgiving — 4th Thursday of November
        return True

    # Good Friday — 2 days before Easter Sunday
    if d == easter_sunday(y) - timedelta(days=2):
        return True

    return False


def is_us_trading_day(d: date) -> bool:
    """True if ``d`` is a real NYSE trading session: a weekday that is not a holiday closure."""
    if d.weekday() >= 5:            # Saturday / Sunday
        return False
    return not is_us_market_holiday(d)


def drop_non_trading_days(df, date_col: str = "date"):
    """Return ``df`` with every row whose ``date_col`` falls on a NON-trading day removed.

    The phantom-bar guard (mandate #32-B): a daily CLOSE can exist only on a real session, so a
    weekend/holiday-stamped bar is a fabricated (stale-carried) bar and is dropped rather than
    written. ``(kept_df, dropped_dates)`` where ``dropped_dates`` is the sorted unique list of
    dropped dates (for logging). Empty / missing-column input is returned untouched."""
    if df is None or len(df) == 0 or date_col not in getattr(df, "columns", []):
        return df, []

    def _as_date(v):
        if hasattr(v, "date") and callable(v.date):   # datetime / pandas Timestamp
            return v.date()
        if isinstance(v, str):
            return date.fromisoformat(v[:10])
        return v

    mask = df[date_col].map(lambda v: is_us_trading_day(_as_date(v)))
    dropped = sorted({_as_date(v) for v in df.loc[~mask, date_col]})
    return df.loc[mask].copy(), dropped
