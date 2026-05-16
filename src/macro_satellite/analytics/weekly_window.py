"""Weekly aggregation helpers.

ISO weeks (Monday start). За дадена референтна дата → endpoints на седмицата.
Седмичен interval change за всеки symbol = (price на края на седмицата / price на края на предишната седмица) - 1.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta

import pandas as pd


@dataclass(frozen=True)
class WeekWindow:
    week_start: date           # Monday
    week_end: date             # Sunday
    iso_year: int
    iso_week: int

    @property
    def label(self) -> str:
        return f"{self.iso_year}-W{self.iso_week:02d}"


def iso_week_for(d: date) -> WeekWindow:
    iso_year, iso_week, iso_dow = d.isocalendar()
    week_start = d - timedelta(days=iso_dow - 1)
    week_end = week_start + timedelta(days=6)
    return WeekWindow(week_start, week_end, iso_year, iso_week)


def current_week(today: date | None = None) -> WeekWindow:
    from ..utils.dates import today_utc
    return iso_week_for(today or today_utc())


def previous_week(w: WeekWindow) -> WeekWindow:
    return iso_week_for(w.week_start - timedelta(days=1))


def trailing_weeks(w: WeekWindow, n: int) -> list[WeekWindow]:
    """Връща list[WeekWindow] с n седмици преди w (без w)."""
    out: list[WeekWindow] = []
    cur = previous_week(w)
    for _ in range(n):
        out.append(cur)
        cur = previous_week(cur)
    return list(reversed(out))


def last_close_in_window(duck, table: str, symbol_col: str, symbol: str,
                         price_col: str, window: WeekWindow) -> tuple[date, float] | None:
    """Последното (date, price) в week window-а за даден symbol."""
    sql = f"""
    SELECT date, {price_col} AS price
    FROM {table}
    WHERE {symbol_col} = ? AND date >= ? AND date <= ?
    ORDER BY date DESC LIMIT 1
    """
    df = duck.execute(sql, [symbol, window.week_start, window.week_end]).df()
    if df.empty or pd.isna(df.iloc[0]["price"]):
        return None
    d_val = df.iloc[0]["date"]
    if hasattr(d_val, "date") and callable(d_val.date):
        d_val = d_val.date()
    return d_val, float(df.iloc[0]["price"])


def last_close_on_or_before(duck, table: str, symbol_col: str, symbol: str,
                             price_col: str, cutoff: date) -> tuple[date, float] | None:
    """Последното (date, price) ≤ cutoff."""
    sql = f"""
    SELECT date, {price_col} AS price
    FROM {table}
    WHERE {symbol_col} = ? AND date <= ?
    ORDER BY date DESC LIMIT 1
    """
    df = duck.execute(sql, [symbol, cutoff]).df()
    if df.empty or pd.isna(df.iloc[0]["price"]):
        return None
    d_val = df.iloc[0]["date"]
    if hasattr(d_val, "date") and callable(d_val.date):
        d_val = d_val.date()
    return d_val, float(df.iloc[0]["price"])


def weekly_interval_change(duck, symbol: str, week: WeekWindow) -> dict | None:
    """interval change = (price_at_week_end / price_at_prev_week_end) - 1.

    Използва last close ≤ week_end и last close ≤ prev_week_end.
    """
    end = last_close_on_or_before(duck, "etf_prices", "symbol", symbol, "price", week.week_end)
    if end is None:
        return None
    prev = previous_week(week)
    start = last_close_on_or_before(duck, "etf_prices", "symbol", symbol, "price", prev.week_end)
    if start is None:
        return None
    p_a, p_b = start[1], end[1]
    if p_a <= 0:
        return None
    return {
        "symbol": symbol,
        "week": week.label,
        "date_a": start[0],
        "date_b": end[0],
        "price_a": p_a,
        "price_b": p_b,
        "weekly_change": (p_b / p_a) - 1.0,
    }
