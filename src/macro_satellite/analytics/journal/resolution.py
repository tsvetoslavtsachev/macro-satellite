"""Resolution loop (Тухла 2b, стъпка 6) — разрешава човешка присъда на хоризонт Y.

КОТВА = judgment_date (НЕ episode open_date). Защо: човекът пише присъда седмици след
като епизодът е отворил; ако хоризонтът броеше от open_date, човекът вече е видял част от
еволюцията → look-ahead изтичане → счупва точно real-time теста, заради който 2b съществува
(caveat #1). Котвата на judgment_date прави залога истински forward — нула look-ahead.

Преизползва attribution.classify (СЪЩАТА vol-норм. математика като машинния base rate) —
само прозорецът е друг (T → T+Y, не open → open+Y). Следователно НЕ apples-to-apples с
machine base rate: калибрацията е prior-vs-realtime, не глава-в-глава (етикетирано в стъпка 7).

⚠ resolved-week gap-ът идва от backfill серията (revision-biased на тази седмица — caveat #1).
   No-look-ahead на ЧОВЕКА е запазен независимо (заложил е на T без да види T+Y); revision
   bias на самата стойност е ортогонален и наследен от машинната серия. Строгият тест би
   снимал live gap при T и T+Y — refinement за по-късно.
"""
from __future__ import annotations

import pandas as pd

from ...paths import JOURNAL_DIR
from ..weekly_window import iso_week_for
from .attribution import axis_sigma, classify
from .human_store import HumanJudgment, HumanResolution
from .store import _gap_series_file


def load_gap_series(region: str = "US") -> pd.DataFrame:
    """gap_series[_<region>].parquet → подреден по week_end DataFrame (resolution източник)."""
    path = JOURNAL_DIR / _gap_series_file(region)
    if not path.exists():
        return pd.DataFrame()
    df = pd.read_parquet(path)
    df = df.sort_values("week_end").reset_index(drop=True)
    return df


def series_sigmas(gap_series: pd.DataFrame) -> tuple[float, float]:
    """Глобална σ на седмичните Δ на двете оси — СЪЩАТА axis_sigma като backfill."""
    sigma_e = axis_sigma(gap_series["economy_axis"].tolist())
    sigma_m = axis_sigma(gap_series["markets_axis"].tolist())
    return sigma_e, sigma_m


def _row_for_week_label(gap_series: pd.DataFrame, label: str):
    hit = gap_series[gap_series["week"] == label]
    return hit.iloc[0] if not hit.empty else None


def _row_for_week_end(gap_series: pd.DataFrame, week_end) -> pd.Series | None:
    we = pd.Timestamp(week_end).date() if hasattr(pd.Timestamp(week_end), "date") else week_end
    for _, r in gap_series.iterrows():
        rwe = r["week_end"]
        rwe = rwe.date() if hasattr(rwe, "date") else rwe
        if rwe == we:
            return r
    return None


def resolve_judgment(j: HumanJudgment,
                     gap_series: pd.DataFrame,
                     sigma_e: float,
                     sigma_m: float) -> HumanResolution | None:
    """Разрешава една присъда на нейния хоризонт Y. Връща None ако още PENDING (T+Y няма данни).

    T = седмицата на judgment_date; T+Y = седмицата след Y седмици. classify(gap_T, gap_T+Y,
    ΔM, ΔE, σ) → machine_outcome; сравнява се със залога (direction_hit / axis_hit).
    """
    t_week = iso_week_for(j.judgment_date)
    t_row = _row_for_week_label(gap_series, t_week.label)
    if t_row is None:
        # judgment_date седмицата няма изчислим gap → не можем да котвираме (рядко).
        return None

    from datetime import timedelta
    y_week = iso_week_for(t_week.week_start + timedelta(days=7 * j.horizon_y_human))
    y_row = _row_for_week_end(gap_series, y_week.week_end)
    if y_row is None:
        return None  # PENDING — хоризонтът още не е настъпил (нула look-ahead)

    gap_open = float(t_row["gap"])
    gap_y = float(y_row["gap"])
    d_e = float(y_row["economy_axis"]) - float(t_row["economy_axis"])
    d_m = float(y_row["markets_axis"]) - float(t_row["markets_axis"])

    outcome, m_share, e_share = classify(gap_open, gap_y, d_m, d_e, sigma_m, sigma_e)

    direction_hit = _direction_hit(j.claim_direction, outcome)
    axis_hit = _axis_hit(j.claim_direction, j.claim_axis, outcome)

    resolved_we = y_row["week_end"]
    resolved_we = resolved_we.date() if hasattr(resolved_we, "date") else resolved_we

    return HumanResolution(
        resolution_id=f"hr_{j.judgment_id}",
        judgment_id=j.judgment_id,
        gap_episode_id=j.gap_episode_id,
        region=j.region,
        horizon_y=j.horizon_y_human,
        judgment_date=j.judgment_date,
        resolved_week=str(y_row["week"]),
        resolved_date=resolved_we,
        as_of_gap=gap_open,
        y_gap=gap_y,
        d_economy=d_e,
        d_markets=d_m,
        machine_outcome=outcome,
        machine_m_share=m_share,
        machine_e_share=e_share,
        human_claim_direction=j.claim_direction,
        human_claim_axis=j.claim_axis,
        direction_hit=direction_hit,
        axis_hit=axis_hit,
        resolved_at=None,
    )


def _direction_hit(claim_direction: str, outcome: str) -> bool:
    """close = всеки от 3-те затварящи изхода; widen = widen. (ПЪРВИЧНАТА информативна ос.)"""
    if claim_direction == "widen":
        return outcome == "widen"
    # close
    return outcome in ("market_leads", "economy_leads", "meet")


def _axis_hit(claim_direction: str, claim_axis: str | None, outcome: str) -> bool | None:
    """Само ако човекът каза close И машината затвори (≠ widen): позна ли затварящата ос?

    None ако: човекът каза widen (няма ос), ИЛИ машината се разшири (затваряща ос неприложима).
    """
    if claim_direction != "close" or outcome == "widen":
        return None
    return claim_axis == outcome


def resolve_pending(region: str = "US") -> list[HumanResolution]:
    """Намира всички присъди БЕЗ резолюция, чийто хоризонт е настъпил → разрешава ги.

    Idempotent: вече-разрешените (по resolution_id) се пропускат при append. Връща САМО
    новоразрешените този run (за доклада на ритуала).
    """
    from .human_store import append_resolution, read_judgments, resolved_judgment_ids

    gap_series = load_gap_series(region)
    if gap_series.empty:
        return []
    sigma_e, sigma_m = series_sigmas(gap_series)
    already = resolved_judgment_ids()
    newly: list[HumanResolution] = []
    for j in read_judgments():
        if j.region.upper() != region.upper():
            continue
        if j.judgment_id in already:
            continue
        res = resolve_judgment(j, gap_series, sigma_e, sigma_m)
        if res is None:
            continue  # still pending
        if append_resolution(res):
            newly.append(res)
    return newly
