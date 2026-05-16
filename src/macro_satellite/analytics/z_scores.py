"""Z-score computations vs trailing windows."""
from __future__ import annotations

import math
import statistics
from dataclasses import dataclass
from datetime import date

from .weekly_window import WeekWindow, trailing_weeks, weekly_interval_change


@dataclass
class WeeklyZScore:
    symbol: str
    week: str
    weekly_change: float
    trailing_mean: float
    trailing_std: float
    z_score: float
    n_baseline_weeks: int
    price_a: float
    price_b: float
    date_a: date
    date_b: date


def weekly_z(duck, symbol: str, week: WeekWindow,
             trailing_n: int = 13) -> WeeklyZScore | None:
    """Z-score на седмичното движение спрямо предишните `trailing_n` седмици."""
    current = weekly_interval_change(duck, symbol, week)
    if current is None:
        return None
    baseline: list[float] = []
    for w in trailing_weeks(week, trailing_n):
        x = weekly_interval_change(duck, symbol, w)
        if x is not None:
            baseline.append(x["weekly_change"])
    if len(baseline) < 4:           # too few data points to trust std
        return None
    mean = statistics.fmean(baseline)
    std = statistics.pstdev(baseline)
    if std == 0 or math.isnan(std):
        return None
    z = (current["weekly_change"] - mean) / std
    return WeeklyZScore(
        symbol=symbol,
        week=week.label,
        weekly_change=current["weekly_change"],
        trailing_mean=mean,
        trailing_std=std,
        z_score=z,
        n_baseline_weeks=len(baseline),
        price_a=current["price_a"],
        price_b=current["price_b"],
        date_a=current["date_a"],
        date_b=current["date_b"],
    )


def scan_universe(duck, symbols: list[str], week: WeekWindow,
                  trailing_n: int = 13,
                  z_threshold: float = 1.5) -> list[WeeklyZScore]:
    """За всеки symbol → weekly_z. Връща списък сортиран по |z| descending,
    филтриран на |z| >= threshold."""
    out: list[WeeklyZScore] = []
    for s in symbols:
        wz = weekly_z(duck, s, week, trailing_n=trailing_n)
        if wz is None:
            continue
        if abs(wz.z_score) >= z_threshold:
            out.append(wz)
    out.sort(key=lambda x: abs(x.z_score), reverse=True)
    return out
