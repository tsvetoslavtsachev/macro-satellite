"""Детекция на gap-епизоди (Тухла 2a).

Gap-епизод = контигуозен run от седмици, в който |gap| ≥ τ_open. Отваряне = пресичане
нагоре през τ_open; затваряне = първата седмица, в която |gap| < τ_close (хистерезис,
τ_close < τ_open срещу chattering) ИЛИ смяна на знака спрямо отварянето.

Прагът е VOL-BASED ГЛОБАЛЕН (решение Q4): τ_open = k_open·σ_gap, τ_close = k_close·σ_gap,
σ_gap = стандартното отклонение на gap-а върху ЦЯЛАТА реконструирана история.
⚠ σ_gap е глобален → лек look-ahead САМО за прага (не за изхода). Документиран; приет
заради вече наличния revision-bias look-ahead и защото адаптира прага към естествения
мащаб на метриката (по-защитимо от ръчно избрана абсолютна стойност).

Броим ЕПИЗОДИ, не записи (Възел 4): клъстерираните седмици на един режим = 1 епизод.
Незатворен на края на серията → censored (брои се честно, не се класифицира като затворен).

`config_key` (Възел 4, грубо): знак на gap-а при отваряне → 'gap_pos' | 'gap_neg'.
"""
from __future__ import annotations

import statistics
from dataclasses import dataclass
from datetime import date

# Прагове в единици σ_gap. Хистерезис: отваря над 1σ, затваря под 0.5σ.
K_OPEN = 1.0
K_CLOSE = 0.5


@dataclass
class GapEpisode:
    """Един gap-епизод. Машинно-извлечени полета (нула човешка преценка в 2a)."""
    episode_id: str
    open_index: int             # индекс в подравнената седмична серия
    open_week: str
    open_date: date             # week_end на отварящата седмица
    close_index: int | None     # None ако censored
    close_week: str | None
    close_date: date | None
    open_gap: float
    close_gap: float | None
    peak_gap: float             # gap при max |gap| в епизода (signed)
    n_weeks: int                # брой седмици open..close включително (или до края ако censored)
    censored: bool              # все още отворен на края на серията
    config_key: str             # 'gap_pos' | 'gap_neg' (знак при отваряне)


def gap_sigma(gaps: list[float]) -> float:
    """Глобална σ на gap-а (population std). Базата за vol-based прага."""
    clean = [g for g in gaps if g is not None]
    if len(clean) < 2:
        return 0.0
    return statistics.pstdev(clean)


def detect_episodes(weeks: list, gaps: list[float | None],
                    sigma: float | None = None,
                    k_open: float = K_OPEN,
                    k_close: float = K_CLOSE) -> tuple[list[GapEpisode], dict]:
    """Открива gap-епизоди в подравнена седмична серия.

    Args:
        weeks: list[WeekWindow] (подравнен с gaps; само седмици с изчислим gap).
        gaps:  list[float] gap стойности (без None — подразбира се вече филтрирано).
        sigma: σ_gap; ако None → смята се глобално от gaps.
        k_open/k_close: множители на прага в единици σ.

    Returns:
        (episodes, meta) — meta носи sigma, τ_open, τ_close, n_weeks_total за прозрачност.
    """
    clean_gaps = [g for g in gaps if g is not None]
    sig = sigma if sigma is not None else gap_sigma(clean_gaps)
    tau_open = k_open * sig
    tau_close = k_close * sig
    meta = {
        "sigma_gap": sig,
        "tau_open": tau_open,
        "tau_close": tau_close,
        "k_open": k_open,
        "k_close": k_close,
        "n_weeks_total": len(clean_gaps),
    }

    episodes: list[GapEpisode] = []
    n = len(gaps)
    i = 0
    ep_counter = 0
    while i < n:
        g = gaps[i]
        if g is None or abs(g) < tau_open:
            i += 1
            continue
        # ── Отваряне ──────────────────────────────────────────────────────────
        # Епизодът заема on-side седмиците [open, close-1]: |gap|≥τ_close И същ знак.
        # close_idx = първата седмица ИЗВЪН (под прага ИЛИ обратен знак) = резолюция.
        open_idx = i
        open_gap = g
        open_sign = 1 if open_gap > 0 else -1
        peak_gap = open_gap
        close_idx = None
        j = i + 1
        while j < n:
            gj = gaps[j]
            if gj is None:
                # пропуск в серията — третираме като продължение (без да чупим епизода)
                j += 1
                continue
            same_side = (1 if gj > 0 else -1) == open_sign
            if (not same_side) or abs(gj) < tau_close:
                close_idx = j
                break
            if abs(gj) > abs(peak_gap):   # peak само над on-side седмиците (без резолюцията)
                peak_gap = gj
            j += 1
        ep_counter += 1
        if close_idx is None:
            # Censored — стигнахме края на серията, още отворен.
            episodes.append(GapEpisode(
                episode_id=_episode_id(weeks[open_idx], ep_counter),
                open_index=open_idx, open_week=weeks[open_idx].label,
                open_date=weeks[open_idx].week_end,
                close_index=None, close_week=None, close_date=None,
                open_gap=open_gap, close_gap=None, peak_gap=peak_gap,
                n_weeks=n - open_idx, censored=True,
                config_key=_config_key(open_gap),
            ))
            break  # нищо след censored епизод
        else:
            episodes.append(GapEpisode(
                episode_id=_episode_id(weeks[open_idx], ep_counter),
                open_index=open_idx, open_week=weeks[open_idx].label,
                open_date=weeks[open_idx].week_end,
                close_index=close_idx, close_week=weeks[close_idx].label,
                close_date=weeks[close_idx].week_end,
                open_gap=open_gap, close_gap=gaps[close_idx], peak_gap=peak_gap,
                n_weeks=close_idx - open_idx, censored=False,
                config_key=_config_key(open_gap),
            ))
            # Резолюционната седмица може САМА да открие обратен епизод (твърд flip →
            # две дислокации, не една). Под прага → outer loop я прескача. i=close_idx,
            # НЕ +1 → клъстериране пази (on-side седмиците не се препокриват).
            i = close_idx
    return episodes, meta


def _config_key(open_gap: float) -> str:
    """Възел 4, грубо: посока на gap-а при отваряне."""
    return "gap_pos" if open_gap > 0 else "gap_neg"


def _episode_id(open_week, counter: int) -> str:
    return f"ep{counter:03d}_{open_week.label}"
