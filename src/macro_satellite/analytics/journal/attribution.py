"""Attribution на затварянето на gap-епизод → 4 изхода (Тухла 2a).

За епизод, отворен при index `open` с gap_open = M_open − E_open, и хоризонт Y седмици:

    s     = sign(gap_open)
    ΔM    = M(open+Y) − M(open)              ΔE = E(open+Y) − E(open)
    C_M   = −s·ΔM   (принос на пазари-крака към затварянето)
    C_E   = +s·ΔE   (принос на икономика-крака към затварянето)
    ĉ_M   = C_M / σ_M    ĉ_E = C_E / σ_E     ← VOL-НОРМАЛИЗАЦИЯ

σ_M, σ_E = глобална σ на седмичните Δ на всяка ос (цялата реконструирана история).
Защо vol-норм: икономика-кракът е КРЕХЪК (4–5 показателя, без излишество) → може да
скочи от един ревизиран индикатор. Делене на σ_E дисконтира генерично-скокливия крак —
иначе по-голямата сурова амплитуда фалшиво „печели" приноса. (STRESSTEST §2.)

Четирите изхода (по доминиращия vol-норм. дял; миноритарен дял > 1/3 → meet):
  • market_leads  — пазари-оста се движи към икономиката → ИКОНОМИКАТА беше водещ сигнал
                    (пазарът капитулира). Action: FADE (връщане към икон. гравитация).
  • economy_leads — икономика-оста към пазара → ПАЗАРЪТ позна как ще се промени светът.
                    Action: СЛЕДВАЙ пазара.
  • meet          — двата крака съизмеримо → споделена корекция. Action: стой настрана.
  • widen         — |gap| се разшири на хоризонта → присъдата (за затваряне) сгреши.

⚠ Конвенцията `X_leads` = „оста X се движи за да затвори"; vindicated е ДРУГАТА страна
   (потвърдено от Цветослав). Mapping-ът горе е каноничен — не го инвертирай.

`unresolved` (НЕ е сред 4-те) = епизодът няма още Y седмици данни (censored at Y) → не
се класифицира, брои се отделно. Само longitudinal (M от N) разграничава оракул от монета —
калибрацията се чете на КУПЧИНАТА (base rate), никога на единичен запис (= Тухла 2b).
"""
from __future__ import annotations

import statistics
from dataclasses import dataclass
from datetime import date

# Хоризонти Y (седмици) — решение Q2: набор, headline = 8w.
HORIZONS = (4, 8, 13)

# Дял за „воден" изход: победителят трябва ≥ 2/3 (миноритарен ≤ 1/3); иначе meet.
MEET_MINORITY = 1.0 / 3.0

_EPS = 1e-9


@dataclass
class HorizonOutcome:
    """Машинен изход на епизод на конкретен хоризонт Y."""
    horizon_y: int
    y_index: int | None
    y_date: date | None
    y_economy_axis: float | None
    y_markets_axis: float | None
    y_gap: float | None
    d_economy: float | None       # ΔE
    d_markets: float | None       # ΔM
    economy_share: float | None   # vol-норм. дял ∈ [0,1] (None ако unresolved/widen)
    markets_share: float | None
    outcome: str                  # market_leads | economy_leads | meet | widen | unresolved
    censored_at_y: bool


def axis_sigma(values: list) -> float:
    """Глобална σ на седмичните първи разлики на дадена ос (за vol-нормализация)."""
    diffs = []
    prev = None
    for v in values:
        if v is None:
            prev = None
            continue
        if prev is not None:
            diffs.append(v - prev)
        prev = v
    if len(diffs) < 2:
        return 0.0
    return statistics.pstdev(diffs)


def classify(gap_open: float, gap_y: float,
             d_markets: float, d_economy: float,
             sigma_m: float, sigma_e: float) -> tuple[str, float | None, float | None]:
    """Класифицира един (open → Y) преход в изход + vol-норм. дялове.

    Returns (outcome, markets_share, economy_share). За widen дяловете са None.
    """
    if abs(gap_y) >= abs(gap_open):          # не се сви (разшири се или флат) → присъдата сгреши
        return "widen", None, None

    s = 1.0 if gap_open > 0 else -1.0
    c_m = -s * d_markets                       # принос на пазари към затварянето
    c_e = +s * d_economy                       # принос на икономика към затварянето
    cn_m = c_m / max(sigma_m, _EPS)            # vol-нормализиран
    cn_e = c_e / max(sigma_e, _EPS)
    pos_m = max(cn_m, 0.0)                      # крак, движещ се ПРОТИВ затварянето → 0 кредит
    pos_e = max(cn_e, 0.0)
    tot = pos_m + pos_e
    if tot <= _EPS:
        # Сви се, но нито един крак не „затваря" в vol-норм. термини (числов ръб) → meet.
        return "meet", 0.5, 0.5
    m_share = pos_m / tot
    e_share = pos_e / tot
    minority = min(m_share, e_share)
    if minority > MEET_MINORITY:
        return "meet", m_share, e_share
    if m_share > e_share:
        return "market_leads", m_share, e_share
    return "economy_leads", m_share, e_share


def attribute_episode(ep, economy: list, markets: list, weeks: list,
                      sigma_e: float, sigma_m: float,
                      horizons: tuple[int, ...] = HORIZONS) -> list[HorizonOutcome]:
    """Класифицира епизод на всеки хоризонт Y (Δ open → open+Y, capped при края на серията).

    Args:
        ep: GapEpisode.
        economy/markets: подравнени списъци с осите (същия index като weeks).
        weeks: list[WeekWindow].
        sigma_e/sigma_m: глобална σ на седмичните Δ на всяка ос.
    """
    o = ep.open_index
    e_open = economy[o]
    m_open = markets[o]
    gap_open = m_open - e_open
    n = len(weeks)
    out: list[HorizonOutcome] = []
    for y in horizons:
        ty = o + y
        if ty >= n:
            # Няма Y седмици данни след отварянето → не може да се съди на този хоризонт.
            out.append(HorizonOutcome(
                horizon_y=y, y_index=None, y_date=None,
                y_economy_axis=None, y_markets_axis=None, y_gap=None,
                d_economy=None, d_markets=None,
                economy_share=None, markets_share=None,
                outcome="unresolved", censored_at_y=True,
            ))
            continue
        e_y = economy[ty]
        m_y = markets[ty]
        if e_y is None or m_y is None:
            out.append(HorizonOutcome(
                horizon_y=y, y_index=ty, y_date=weeks[ty].week_end,
                y_economy_axis=e_y, y_markets_axis=m_y, y_gap=None,
                d_economy=None, d_markets=None,
                economy_share=None, markets_share=None,
                outcome="unresolved", censored_at_y=True,
            ))
            continue
        gap_y = m_y - e_y
        d_m = m_y - m_open
        d_e = e_y - e_open
        outcome, m_share, e_share = classify(gap_open, gap_y, d_m, d_e, sigma_m, sigma_e)
        out.append(HorizonOutcome(
            horizon_y=y, y_index=ty, y_date=weeks[ty].week_end,
            y_economy_axis=e_y, y_markets_axis=m_y, y_gap=gap_y,
            d_economy=d_e, d_markets=d_m,
            economy_share=e_share,
            markets_share=m_share,
            outcome=outcome, censored_at_y=False,
        ))
    return out
