"""Седмичен diff на rotation quadrants — кои tickers са влезли/излезли.

Сравнява latest snapshot в текущата седмица vs latest snapshot в предишната.
Маркира 'first_time_ever' за tickers, които никога преди не са били в quadrant-а.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

import pandas as pd

from .weekly_window import WeekWindow, previous_week


@dataclass
class RotationDelta:
    universe: str  # 'us' | 'eu'
    quadrant: str  # 'stable_winner' | 'quality_dip' | 'faded_bounce'
    horizon: str   # '1m' | '3m'
    entered: list[str]
    exited: list[str]
    first_time_ever: list[str]  # subset of entered
    a_date: date
    b_date: date


def _latest_snapshot_date_in_window(duck, table: str, week: WeekWindow) -> date | None:
    sql = f"SELECT max(date) AS d FROM {table} WHERE date >= ? AND date <= ?"
    df = duck.execute(sql, [week.week_start, week.week_end]).df()
    if df.empty or pd.isna(df.iloc[0]["d"]):
        return None
    val = df.iloc[0]["d"]
    if hasattr(val, "date") and callable(val.date):
        val = val.date()
    return val


def _tickers_in_quadrant(duck, table: str, snapshot_date: date,
                         quadrant: str, horizon: str) -> set[str]:
    col = f"quadrant_{horizon}"
    sql = f"SELECT ticker FROM {table} WHERE date = ? AND {col} = ?"
    df = duck.execute(sql, [snapshot_date, quadrant]).df()
    return set(df["ticker"].dropna().tolist())


def _ever_in_quadrant_before(duck, table: str, cutoff: date,
                              tickers: set[str], quadrant: str, horizon: str) -> set[str]:
    """Връща tickers, които поне веднъж преди cutoff са били в quadrant."""
    if not tickers:
        return set()
    col = f"quadrant_{horizon}"
    placeholders = ",".join(["?"] * len(tickers))
    sql = (f"SELECT DISTINCT ticker FROM {table} "
           f"WHERE date < ? AND {col} = ? AND ticker IN ({placeholders})")
    params = [cutoff, quadrant] + list(tickers)
    df = duck.execute(sql, params).df()
    return set(df["ticker"].tolist())


def rotation_diff(duck, universe: str, week: WeekWindow,
                  quadrants: tuple[str, ...] = ("stable_winner", "quality_dip", "faded_bounce"),
                  horizons: tuple[str, ...] = ("1m", "3m")) -> list[RotationDelta]:
    table = f"rotation_{universe}"
    prev = previous_week(week)
    b_date = _latest_snapshot_date_in_window(duck, table, week)
    a_date = _latest_snapshot_date_in_window(duck, table, prev)
    if a_date is None or b_date is None or a_date == b_date:
        return []
    results: list[RotationDelta] = []
    for q in quadrants:
        for h in horizons:
            set_a = _tickers_in_quadrant(duck, table, a_date, q, h)
            set_b = _tickers_in_quadrant(duck, table, b_date, q, h)
            entered = sorted(set_b - set_a)
            exited = sorted(set_a - set_b)
            ever_before = _ever_in_quadrant_before(
                duck, table, a_date, set(entered), q, h)
            first_time = sorted(set(entered) - ever_before)
            results.append(RotationDelta(
                universe=universe, quadrant=q, horizon=h,
                entered=entered, exited=exited,
                first_time_ever=first_time,
                a_date=a_date, b_date=b_date,
            ))
    return results
