"""Реконструкция на историческия икономика-крак за gap-журнала (Тухла 2a).

Колекторът държи само ~4 реда `us_macro_state` (Phase 5 тръгна май 2026). За machine
base rate икономика-кракът се РЕКОНСТРУИРА назад: чете пълните FRED серии от
us-macro-dashboard (`fred_cache`), trim-ва ги до всяка седмична дата X (`.loc[:X]`),
и пуска СЪЩИЯ `build_macro_state(trimmed, X)` pipeline → исторически lens scores →
СЪЩАТА композит-логика (`gap_engine.economy_axis_from_scores`).

⚠ REVISION / VINTAGE BIAS (caveat #1): `fred_cache` днес = РЕВИЗИРАНИ данни, а trim-ът
   е по дата-на-наблюдение — включва точки, които реално НЕ са били публикувани към X
   (publication lag) + бъдещи ревизии на стойностите. → реконструкцията „знае бъдещето"
   → machine base rate е BEST-CASE (perfect-hindsight), НЕ real-time постижим. Емпирично
   потвърдено: на overlap-а (15–30 май 2026) реконструкцията се разминава с колекторския
   snapshot, и разминаването СВИВА към най-скорошната дата (по-старите дати „виждат"
   по-късно публикувани принтове). Никога не представяй това като real-time edge.

⚠ МЕТОДОЛОГИЧНА КОНСИСТЕНТНОСТ (caveat #2): прилага ДНЕШНАТА `build_macro_state`
   методология + ДНЕШНИТЕ `gap_weights` ориентации (вкл. stagflation-scoped
   inflation=-1) назад. За консистентна base-rate метрика е feature, но се документира —
   2021 reflation носи семантично обърнат inflation orient (виж backfill двойния доклад).

Колекторът е чист — този модул НЕ пише в `us_macro_state`. Реконструкцията отива в
ОТДЕЛЕН store (`journal/economy_reconstructed.parquet`), маркиран revision-biased.
"""
from __future__ import annotations

import contextlib
import io
import os
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import pandas as pd

from ...paths import REPO_ROOT
from ..gap_engine import GapWeights, LegReading, economy_axis_from_scores, load_gap_weights
from ..weekly_window import WeekWindow

# us-macro-dashboard репо (sibling по подразбиране; override с env за CI/различни машини).
US_DASHBOARD_ROOT = Path(
    os.environ.get("MACRO_US_DASHBOARD_ROOT", str(REPO_ROOT.parent / "us-macro-dashboard"))
)

# Lens-и, които gap-икономика-кракът ползва (= US таксономия в build_macro_state).
_US_LENSES = ("labor", "growth", "inflation", "liquidity")


@dataclass
class _Bridge:
    """Заредени us-macro-dashboard обекти + пълният FRED snapshot (зарежда се веднъж)."""
    snapshot: dict          # {series_id: pd.Series} с DatetimeIndex
    build_macro_state: callable
    lenses: tuple[str, ...]


_BRIDGE: _Bridge | None = None


def _load_bridge() -> _Bridge:
    """Инжектира us-macro-dashboard в sys.path, зарежда FRED snapshot от cache (без мрежа).

    Кешира се на ниво модул — пълният snapshot е скъп да се чете повторно.
    """
    global _BRIDGE
    if _BRIDGE is not None:
        return _BRIDGE
    root = str(US_DASHBOARD_ROOT)
    if not Path(root).exists():
        raise FileNotFoundError(
            f"us-macro-dashboard не е намерен: {root}. "
            f"Сетни MACRO_US_DASHBOARD_ROOT към репото."
        )
    if root not in sys.path:
        sys.path.insert(0, root)
    # Импортите са top-level в us-macro-dashboard (config/catalog/sources/...).
    from catalog.series import SERIES_CATALOG          # noqa: E402
    from config import FRED_API_KEY                     # noqa: E402
    from export_api import LENSES, build_macro_state    # noqa: E402
    from sources.fred_adapter import FredAdapter        # noqa: E402

    adapter = FredAdapter(api_key=FRED_API_KEY, base_dir=root)
    snapshot = adapter.get_snapshot(SERIES_CATALOG.keys())  # cache-only, без fetch
    if len(snapshot) < 10:
        raise RuntimeError(
            f"fred_cache почти празен ({len(snapshot)} серии). "
            f"Стартирай `python export_api.py --refresh` в us-macro-dashboard."
        )
    _BRIDGE = _Bridge(snapshot=snapshot, build_macro_state=build_macro_state,
                      lenses=tuple(LENSES))
    return _BRIDGE


def reconstruct_scores_as_of(d: date, bridge: _Bridge | None = None) -> dict | None:
    """Реконструирани lens scores as-of дата d (trim → build_macro_state).

    Връща {'labor':..,'growth':..,'inflation':..,'liquidity':.., 'as_of_date': date}
    или None ако snapshot-ът няма достатъчно данни преди d.
    """
    b = bridge or _load_bridge()
    cutoff = pd.Timestamp(d)
    trimmed = {k: s.loc[:cutoff] for k, s in b.snapshot.items()}
    # Колко серии реално имат точка ≤ d? Под праг → твърде рано в историята.
    if sum(1 for s in trimmed.values() if not s.empty) < 10:
        return None
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):   # build_macro_state принтира emoji → cp1252 краш
        ms = b.build_macro_state(trimmed, d)
    lenses = ms.get("lenses") or {}
    out: dict = {}
    for lens in _US_LENSES:
        ld = lenses.get(lens) or {}
        out[lens] = ld.get("score")
    out["as_of_date"] = _parse_as_of(ms.get("as_of_date"))
    return out


def _parse_as_of(value) -> date | None:
    if not value:
        return None
    if isinstance(value, date):
        return value
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


def reconstruct_economy_axis(week: WeekWindow, weights: GapWeights | None = None,
                             bridge: _Bridge | None = None) -> LegReading | None:
    """Реконструиран икономика-крак за една седмица (as-of week_end).

    Минава през СЪЩАТА композит-логика като табличния `economy_axis` (Тухла 1) →
    числата са директно съизмерими с пазари-крака.
    """
    w = weights or load_gap_weights()
    scores = reconstruct_scores_as_of(week.week_end, bridge)
    if scores is None:
        return None
    as_of = scores.pop("as_of_date", None)
    return economy_axis_from_scores(scores, w, as_of_date=as_of, week_end=week.week_end)
