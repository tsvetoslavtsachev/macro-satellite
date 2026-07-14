"""VRM снимка за журнала — ХИБРИД C6 четец (решение 2026-06-03 с Цветослав).

VRM е дистилирана присъда за това как двете оси се съчетават. В журнала влиза като
LOOSE conditioning хипотеза (по-късно калибрацията пита „при VRM=REFLATION как се
разреши залогът"), НЕ в gap-триангулацията (тавтология модел↔flow — STRESSTEST §1).

Хибрид C6 (разрешава дилемата „твърд adapter vs мек loose"):
  • FRESHNESS винаги — `age_days` от as_of на живия ред; `stale` флаг при > STALE_DAYS.
    Стар VRM, закачен за днешна присъда, е подвеждащ (C4 — възраст на входа).
  • RAISE ШУМНО САМО при CORRUPTION — VRM ред съществува, но липсва задължителното
    `regime` → silent schema drift (точно failure mode #11 / C6). Гръмва, не записва гнило.
  • NON-BLOCKING при ОТСЪСТВИЕ — няма VRM ред ≤ as_of → `available=False`, присъдата за
    gap-а стои сама. VRM е loose, не твърд gate.

Източник (мандат №36, 07.2026): таблица `vrm` — живият data-core weekly overlay
(collectors/vrm_overlay.py). Ръчните vrm_state/vrm_week са пенсионирани. Живата
серия НЕ носи `signal` поле (мозъкът не emit-ва еднословен сигнал) → signal=None
честно. C6 валидира РЕЗУЛТАТА от колектора — хваща тихия drift, без да дублира
parsing-а.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from ...utils.vrm import KNOWN_REGIMES

# Живият overlay е седмичен (W-FRI). < 7 дни = свеж; > 14 (пропуснати 2 цикъла) = stale флаг.
STALE_DAYS = 14


class VrmCorruptionError(ValueError):
    """C6 — VRM ред съществува, но е повреден (липсва/невалиден regime). Raise ШУМНО."""


@dataclass
class VrmSnapshot:
    """Loose VRM conditioning снимка, закачена към присъда. НЕ е gap-вход."""
    available: bool
    regime: str | None
    signal: str | None        # живата серия не носи signal → None (честно)
    ks_active: bool | None
    alignment: float | None
    last_updated: date | None
    age_days: int | None
    stale: bool | None
    source: str | None        # 'vrm' | None


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
    """Най-скорошната VRM снимка ≤ `as_of` от живата таблица `vrm`, валидирана +
    freshness-печатана.

    Args:
        as_of: дата, спрямо която мерим свежест (= judgment_date в ритуала).
        duck:  опционална DuckDB връзка (за тестове); иначе get_duck().

    Raises:
        VrmCorruptionError: наличен VRM ред с липсващ/невалиден regime (C6).
    """
    if duck is None:
        from ...storage.duckdb_conn import get_duck
        duck = get_duck()

    row, source = _latest_row(duck, "vrm", as_of)
    if row is None:
        # Отсъствие → non-blocking (loose).
        return VrmSnapshot(available=False, regime=None, signal=None, ks_active=None,
                           alignment=None, last_updated=None, age_days=None,
                           stale=None, source=None)

    regime = _none_if_nan(row.get("regime"))
    if regime is None or not str(regime).strip():
        # Наличен ред, но без regime → тих schema drift → гръмва (C6).
        raise VrmCorruptionError(
            f"VRM ред в '{source}' (date={row.get('date')}) съществува, но regime липсва — "
            f"тих schema drift? Отказвам да закача повреден VRM към присъда (C6). "
            f"Провери vrm_overlay колектора/data-core overlay формата."
        )
    regime = str(regime).strip().upper()
    if regime not in KNOWN_REGIMES:
        raise VrmCorruptionError(
            f"VRM regime='{regime}' (source={source}, date={row.get('date')}) извън "
            f"познатите {sorted(KNOWN_REGIMES)} — непознат режим или drift (C6). "
            f"Ако е легитимен нов режим → добави го в utils/vrm.py REGIME_BG изрично."
        )

    # Живата серия: date = as_of (W-FRI печатът на мозъка) е freshness котвата.
    last_updated = _coerce_date(row.get("as_of")) or _coerce_date(row.get("date"))
    age_days = (as_of - last_updated).days if last_updated else None
    stale = (age_days is not None and age_days > STALE_DAYS)

    return VrmSnapshot(
        available=True,
        regime=regime,
        signal=None,   # мозъкът не emit-ва еднословен сигнал — не фабрикуваме
        ks_active=_coerce_ks(row),
        alignment=_coerce_float(row.get("alignment_score")),
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
    v = _none_if_nan(row.get("ks_active"))
    if v is None:
        return None
    return bool(v)


def _coerce_float(v) -> float | None:
    v = _none_if_nan(v)
    if v is None:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None
