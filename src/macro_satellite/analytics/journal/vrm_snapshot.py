"""VRM снимка за журнала — ХИБРИД C6 четец (решение 2026-06-03 с Цветослав).

VRM е дистилирана присъда за това как двете оси се съчетават. В журнала влиза като
LOOSE conditioning хипотеза (по-късно калибрацията пита „при VRM=REFLATION как се
разреши залогът"), НЕ в gap-триангулацията (тавтология модел↔flow — STRESSTEST §1).

Хибрид C6 (разрешава дилемата „твърд adapter vs мек loose"):
  • FRESHNESS винаги — `age_days` от last_updated → as_of; `stale` флаг при > STALE_DAYS.
    Стар VRM, закачен за днешна присъда, е подвеждащ (C4 — възраст на входа).
  • RAISE ШУМНО САМО при CORRUPTION — VRM ред съществува, но липсва задължителното
    `regime` → silent schema drift (точно failure mode #11 / C6). Гръмва, не записва гнило.
  • NON-BLOCKING при ОТСЪСТВИЕ — няма VRM ред ≤ as_of → `available=False`, присъдата за
    gap-а стои сама. VRM е loose, не твърд gate.

Източник: НАЙ-СВЕЖИЯТ ред (по last_updated) ≤ as_of измежду `vrm_week` И `vrm_state` —
НЕ „vrm_week на всяка цена". vrm_state често носи по-скорошен KS/режим touch от седмичния
vrm_week (напр. 2026-05-31 vrm_state > 2026-05-24 vrm_week). Tie → vrm_week (authoritative
за текущите числа по VRM конвенция). ⚠ vrm_state НЕ носи `signal` поле → когато то е
по-свежото, `signal=None`. C6 валидира РЕЗУЛТАТА от колектора — хваща тихия regex провал,
без да дублира parsing-а.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

# VRM_WEEK е седмичен (събота). < 7 дни = свеж; > 14 (пропуснати 2 цикъла) = stale флаг.
STALE_DAYS = 14

# Познати режими — за corruption детекция (regime извън това при наличен ред → drift).
KNOWN_REGIMES = {"REFLATION", "GROWTH", "STAGFLATION", "DEFLATION", "GOLDILOCKS", "RECESSION"}


class VrmCorruptionError(ValueError):
    """C6 — VRM ред съществува, но е повреден (липсва/невалиден regime). Raise ШУМНО."""


@dataclass
class VrmSnapshot:
    """Loose VRM conditioning снимка, закачена към присъда. НЕ е gap-вход."""
    available: bool
    regime: str | None
    signal: str | None
    ks_active: bool | None
    alignment: float | None
    last_updated: date | None
    age_days: int | None
    stale: bool | None
    source: str | None        # 'vrm_week' | 'vrm_state' | None


def _none_if_nan(v):
    if v is None:
        return None
    try:
        if v != v:   # NaN
            return None
    except Exception:
        pass
    return v


def _coerce_date(v) -> date | None:
    if v is None:
        return None
    if hasattr(v, "date") and callable(v.date):
        return v.date()
    if isinstance(v, date):
        return v
    try:
        return date.fromisoformat(str(v)[:10])
    except ValueError:
        return None


def read_vrm_snapshot(as_of: date, duck=None) -> VrmSnapshot:
    """Най-скорошната VRM снимка ≤ `as_of`, валидирана + freshness-печатана.

    Args:
        as_of: дата, спрямо която мерим свежест (= judgment_date в ритуала).
        duck:  опционална DuckDB връзка (за тестове); иначе get_duck().

    Raises:
        VrmCorruptionError: наличен VRM ред с липсващ/невалиден regime (C6).
    """
    if duck is None:
        from ...storage.duckdb_conn import get_duck
        duck = get_duck()

    # Кандидати от ДВАТА източника → избираме НАЙ-СВЕЖИЯ по last_updated (vrm_state често
    # носи по-скорошен touch от седмичния vrm_week). Tie → vrm_week (authoritative).
    cands: list[tuple[str, dict]] = []
    rw, _ = _latest_row(duck, "vrm_week", as_of)
    if rw is not None:
        cands.append(("vrm_week", rw))
    rs, _ = _latest_row(duck, "vrm_state", as_of)
    if rs is not None:
        cands.append(("vrm_state", rs))

    if not cands:
        # Отсъствие → non-blocking (loose).
        return VrmSnapshot(available=False, regime=None, signal=None, ks_active=None,
                           alignment=None, last_updated=None, age_days=None,
                           stale=None, source=None)

    def _fresh_key(item: tuple[str, dict]):
        src, r = item
        lu = _coerce_date(r.get("last_updated_md")) or _coerce_date(r.get("date")) or date.min
        return (lu, 1 if src == "vrm_week" else 0)   # tie → vrm_week

    source, row = max(cands, key=_fresh_key)

    regime = _none_if_nan(row.get("regime"))
    if regime is None or not str(regime).strip():
        # Наличен ред, но без regime → тих schema drift → гръмва (C6).
        raise VrmCorruptionError(
            f"VRM ред в '{source}' (date={row.get('date')}) съществува, но regime липсва — "
            f"тих schema drift? Отказвам да закача повреден VRM към присъда (C6). "
            f"Провери {source} колектора/markdown формата."
        )
    regime = str(regime).strip().upper()
    if regime not in KNOWN_REGIMES:
        raise VrmCorruptionError(
            f"VRM regime='{regime}' (source={source}, date={row.get('date')}) извън "
            f"познатите {sorted(KNOWN_REGIMES)} — непознат режим или drift (C6). "
            f"Ако е легитимен нов режим → добави го към KNOWN_REGIMES изрично."
        )

    last_updated = _coerce_date(row.get("last_updated_md")) or _coerce_date(row.get("date"))
    age_days = (as_of - last_updated).days if last_updated else None
    stale = (age_days is not None and age_days > STALE_DAYS)

    return VrmSnapshot(
        available=True,
        regime=regime,
        signal=_none_if_nan(row.get("signal")),
        ks_active=_coerce_ks(row),
        alignment=_coerce_float(row.get("alignment") if source == "vrm_week"
                                else row.get("alignment_score")),
        last_updated=last_updated,
        age_days=age_days,
        stale=stale,
        source=source,
    )


def _latest_row(duck, table: str, as_of: date):
    """Най-скорошният ред с date ≤ as_of от `table` → (dict|None, table|None)."""
    try:
        df = duck.execute(
            f"SELECT * FROM {table} WHERE date <= ? ORDER BY date DESC LIMIT 1",
            [as_of],
        ).df()
    except Exception:
        return None, None
    if df.empty:
        return None, None
    return df.iloc[0].to_dict(), table


def _coerce_ks(row) -> bool | None:
    if "ks_active" in row:
        v = _none_if_nan(row.get("ks_active"))
        if v is None:
            return None
        return bool(v)
    if "ks_status" in row:
        v = _none_if_nan(row.get("ks_status"))
        if v is None:
            return None
        return str(v).lower() == "active"
    return None


def _coerce_float(v) -> float | None:
    v = _none_if_nan(v)
    if v is None:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None
