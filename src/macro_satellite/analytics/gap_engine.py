"""gap_us — едно число през времето: разстоянието икономика-крак ↔ пазари-крак за US.

Тухла 1 на синтез-слоя (Phase 6). НИВО 1: само числа + история. Нула флагове,
нула интерпретация, нула тези. divergence patterns НЕ са оста (контекст по-късно).

Два ориентирани, нормализирани крака (и двата: + = risk-friendly):
- Икономика-крак (вариант B): претеглен ориентиран композит от `us_macro_state`
  lens scores → Σ wᵢ·orientᵢ·(scoreᵢ−midpoint)/scale ∈ ~[-1,+1].
- Пазари-крак (вариант A): risk-on/off от ETF ratio z-scores (cyclical/defensive,
  credit quality, breadth/size, energy) → tanh(Σ wⱼ·orientⱼ·zⱼ) ∈ (-1,+1).

gap = markets_axis − economy_axis. Положителен gap = пазарите са по-risk-on,
отколкото състоянието на икономиката оправдава; отрицателен = по-защитни.

Тегла/ориентации идват от config/gap_weights.yaml (нула hardcode). Всеки крак носи
дата + „възраст" (age_days спрямо week_end) → сравнението е aware за закъснение (C4).
"""
from __future__ import annotations

import math
import statistics
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import pandas as pd
import yaml
from pydantic import BaseModel

from ..config import macro_lenses
from ..paths import CONFIG_DIR
from .weekly_window import (
    WeekWindow,
    last_close_on_or_before,
    trailing_weeks,
)

# ── Config модели ─────────────────────────────────────────────────────────────


class _LensWeight(BaseModel):
    weight: float
    orient: int


class _EconomyWeights(BaseModel):
    midpoint: float = 50.0
    scale: float = 50.0
    lenses: dict[str, _LensWeight]


class _PairWeight(BaseModel):
    name: str
    num: str
    den: str
    weight: float
    orient: int


class _MarketsWeights(BaseModel):
    trailing_weeks: int = 13
    squash: str = "tanh"
    pairs: list[_PairWeight]


class _GapFormula(BaseModel):
    formula: str = "markets_axis - economy_axis"


class GapWeights(BaseModel):
    economy: _EconomyWeights
    markets: _MarketsWeights
    gap: _GapFormula


def load_gap_weights(path: Path | None = None) -> GapWeights:
    p = path or (CONFIG_DIR / "gap_weights.yaml")
    with open(p, encoding="utf-8") as f:
        return GapWeights.model_validate(yaml.safe_load(f))


# ── Изходни dataclasses (Ниво 1 — числа + дати + възраст) ─────────────────────


@dataclass
class LegReading:
    """Един крак за дадена седмица: нормализирана ос + произход + възраст (C4)."""
    axis: float                       # ∈ ~[-1,+1], + = risk-friendly
    components: dict = field(default_factory=dict)   # per-компонент числа (прозрачност)
    as_of_date: date | None = None    # дата на данните, които стоят зад оста
    age_days: int | None = None       # week_end − as_of_date (закъснение на крака)


@dataclass
class GapPoint:
    """gap_us за една седмица. Нула флагове/интерпретация."""
    week: str                         # ISO label, напр. '2026-W20'
    week_end: date
    economy: LegReading | None
    markets: LegReading | None
    gap: float | None                 # markets.axis − economy.axis (None ако крак липсва)


# ── Helpers ───────────────────────────────────────────────────────────────────


def _to_date(value) -> date | None:
    if value is None:
        return None
    if isinstance(value, date) and not isinstance(value, pd.Timestamp):
        return value
    if hasattr(value, "date") and callable(value.date):
        return value.date()
    return value


def _ratio_on_or_before(duck, num: str, den: str,
                        cutoff: date) -> tuple[date, float] | None:
    """num/den ratio level от последните котировки ≤ cutoff за двата символа.

    Възрастта на ratio-то = по-старата от двете котировки (консервативно).
    """
    a = last_close_on_or_before(duck, "etf_prices", "symbol", num, "price", cutoff)
    b = last_close_on_or_before(duck, "etf_prices", "symbol", den, "price", cutoff)
    if a is None or b is None or b[1] == 0:
        return None
    ratio_date = min(a[0], b[0])      # ratio-то е свежо колкото по-стария крак
    return ratio_date, a[1] / b[1]


def _pair_ratio_z(duck, num: str, den: str, week: WeekWindow,
                  trailing_n: int) -> tuple[float, date] | None:
    """z-score на текущото ratio level спрямо trailing_n седмични ratio levels.

    Връща (z, ratio_date) или None при недостатъчен baseline (<4 точки).
    """
    cur = _ratio_on_or_before(duck, num, den, week.week_end)
    if cur is None:
        return None
    cur_date, cur_ratio = cur
    baseline: list[float] = []
    for w in trailing_weeks(week, trailing_n):
        r = _ratio_on_or_before(duck, num, den, w.week_end)
        if r is not None:
            baseline.append(r[1])
    if len(baseline) < 4:             # твърде малко за надеждно std
        return None
    mean = statistics.fmean(baseline)
    std = statistics.pstdev(baseline)
    if std == 0 or math.isnan(std):
        return None
    return (cur_ratio - mean) / std, cur_date


# ── Двата крака ───────────────────────────────────────────────────────────────


def _us_economy_lens_names(econ: _EconomyWeights) -> list[str]:
    """Lens-и от config-а, които реално съществуват за US (защита срещу drift)."""
    known = set(macro_lenses("US"))
    return [ln for ln in econ.lenses.keys() if ln in known]


def _economy_composite(scores: dict, econ: _EconomyWeights,
                       lens_names: list[str]) -> tuple[float, dict] | None:
    """Ориентираният претеглен композит: Σ wᵢ·orientᵢ·(scoreᵢ−mid)/scale ∈ ~[-1,+1].

    `scores` = {lens: score}. Един източник на истина за двата пътя
    (табличния `economy_axis` и backfill `economy_axis_from_scores`).
    """
    num = 0.0
    den = 0.0
    comps: dict = {}
    for lens in lens_names:
        lw = econ.lenses[lens]
        if lw.weight == 0:
            continue
        raw = scores.get(lens)
        if raw is None or (isinstance(raw, float) and pd.isna(raw)):
            continue
        score = float(raw)
        contrib = lw.orient * (score - econ.midpoint) / econ.scale
        comps[lens] = {
            "score": round(score, 2),
            "orient": lw.orient,
            "weight": lw.weight,
            "contribution": round(contrib, 4),
        }
        num += lw.weight * contrib
        den += lw.weight
    if den == 0:
        return None
    return num / den, comps


def economy_axis(duck, week: WeekWindow,
                 weights: GapWeights | None = None) -> LegReading | None:
    """Икономика-крак: последен us_macro_state snapshot ≤ week_end → ориентиран композит.

    Σ wᵢ·orientᵢ·(scoreᵢ−midpoint)/scale, претеглено средно ∈ ~[-1,+1].
    """
    w = weights or load_gap_weights()
    econ = w.economy
    lens_names = _us_economy_lens_names(econ)
    if not lens_names:
        return None

    sel = ", ".join(f"{ln}_score" for ln in lens_names)
    sql = (f"SELECT date, {sel} FROM us_macro_state "
           f"WHERE date <= ? ORDER BY date DESC LIMIT 1")
    df = duck.execute(sql, [week.week_end]).df()
    if df.empty:
        return None
    row = df.iloc[0]
    snap_date = _to_date(row["date"])

    scores = {ln: row.get(f"{ln}_score") for ln in lens_names}
    res = _economy_composite(scores, econ, lens_names)
    if res is None:
        return None
    axis, comps = res
    age = (week.week_end - snap_date).days if snap_date else None
    return LegReading(axis=axis, components=comps,
                      as_of_date=snap_date, age_days=age)


def economy_axis_from_scores(scores: dict, weights: GapWeights | None = None,
                             *, as_of_date: date | None = None,
                             week_end: date | None = None) -> LegReading | None:
    """Икономика-крак от ВЕЧЕ ИЗВЛЕЧЕНИ lens scores (не от таблицата).

    Backfill пътят: реконструираните lens scores (build_macro_state над trimmed
    fred snapshot) минават през СЪЩАТА композит-логика като табличния `economy_axis`.
    `as_of_date`/`week_end` → age_days (C4). Нула докосване на колектора.
    """
    w = weights or load_gap_weights()
    econ = w.economy
    lens_names = _us_economy_lens_names(econ)
    if not lens_names:
        return None
    res = _economy_composite(scores, econ, lens_names)
    if res is None:
        return None
    axis, comps = res
    age = ((week_end - as_of_date).days
           if (week_end is not None and as_of_date is not None) else None)
    return LegReading(axis=axis, components=comps,
                      as_of_date=as_of_date, age_days=age)


def markets_axis(duck, week: WeekWindow,
                 weights: GapWeights | None = None) -> LegReading | None:
    """Пазари-крак: ETF ratio z-scores → претеглена ориентирана средна → tanh.

    tanh(Σ wⱼ·orientⱼ·zⱼ / Σ wⱼ) ∈ (-1,+1). Тегла само върху изчислимите двойки.
    """
    w = weights or load_gap_weights()
    mk = w.markets
    num = 0.0
    den = 0.0
    comps: dict = {}
    as_of_dates: list[date] = []
    for pair in mk.pairs:
        if pair.weight == 0:
            continue
        z = _pair_ratio_z(duck, pair.num, pair.den, week, mk.trailing_weeks)
        if z is None:
            continue
        zval, ratio_date = z
        contrib = pair.orient * zval
        comps[pair.name] = {
            "num": pair.num,
            "den": pair.den,
            "orient": pair.orient,
            "weight": pair.weight,
            "z": round(zval, 4),
            "ratio_date": ratio_date,
            "contribution": round(contrib, 4),
        }
        num += pair.weight * contrib
        den += pair.weight
        as_of_dates.append(ratio_date)
    if den == 0:
        return None

    mean_z = num / den
    axis = math.tanh(mean_z) if mk.squash == "tanh" else mean_z
    as_of = max(as_of_dates) if as_of_dates else None
    age = (week.week_end - as_of).days if as_of else None
    return LegReading(axis=axis, components=comps,
                      as_of_date=as_of, age_days=age)


# ── gap ───────────────────────────────────────────────────────────────────────


def gap_for_week(duck, week: WeekWindow,
                 weights: GapWeights | None = None) -> GapPoint:
    """gap_us за една седмица. gap = markets.axis − economy.axis (None ако крак липсва)."""
    w = weights or load_gap_weights()
    econ = economy_axis(duck, week, w)
    mkt = markets_axis(duck, week, w)
    gap = (mkt.axis - econ.axis) if (econ is not None and mkt is not None) else None
    return GapPoint(week=week.label, week_end=week.week_end,
                    economy=econ, markets=mkt, gap=gap)


def gap_series(duck, weeks: list[WeekWindow],
               weights: GapWeights | None = None) -> list[GapPoint]:
    """gap_us longitudinal за списък седмици."""
    w = weights or load_gap_weights()
    return [gap_for_week(duck, wk, w) for wk in weeks]
