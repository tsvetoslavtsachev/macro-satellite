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

# Региона → dashboard репо (sibling по подразбиране; override с env per регион).
_DASHBOARD_REPO = {
    "US": "us-macro-dashboard",
    "EU": "eu-macro-dashboard",
    "CN": "china-macro-dashboard",
}
_ROOT_ENV = {
    "US": "MACRO_US_DASHBOARD_ROOT",
    "EU": "MACRO_EU_DASHBOARD_ROOT",
    "CN": "MACRO_CN_DASHBOARD_ROOT",
}


def _dashboard_root(region: str) -> Path:
    return Path(os.environ.get(_ROOT_ENV[region], str(REPO_ROOT.parent / _DASHBOARD_REPO[region])))


# Назад-съвместимост (Тухла 2a изнасяше това публично).
US_DASHBOARD_ROOT = _dashboard_root("US")


@dataclass
class _Bridge:
    """Заредени dashboard обекти + пълният snapshot (зарежда се веднъж per регион)."""
    region: str
    snapshot: dict          # {series_id: pd.Series} с DatetimeIndex
    build_macro_state: callable
    lenses: tuple[str, ...]


# Кеш per регион. ⚠ САМО ЕДИН регион dashboard на процес — us/eu/cn dashboard-ите имат
# СЪЩИТЕ top-level имена (catalog/config/export_api/sources) → втори регион в същия процес
# би взел кешираните модули на първия (sys.modules) и ТИХО върнал грешни данни. Затова
# guard-ваме: различен регион → raise. journal-backfill е per регион (отделна инвокация).
_BRIDGES: dict[str, _Bridge] = {}
_LOADED_REGION: str | None = None


def _load_bridge(region: str = "US") -> _Bridge:
    """Инжектира dashboard-а на региона в sys.path, зарежда snapshot от cache (без мрежа).

    US: FredAdapter.get_snapshot(SERIES_CATALOG). EU: _build_snapshot({ecb,eurostat}).
    Кешира per регион. Lens наборът идва от dashboard-овия LENSES (authoritative).
    """
    global _LOADED_REGION
    region = region.upper()
    if region in _BRIDGES:
        return _BRIDGES[region]
    if _LOADED_REGION is not None and _LOADED_REGION != region:
        raise RuntimeError(
            f"cross-repo bridge: {_LOADED_REGION} dashboard вече е зареден в този процес; "
            f"'{region}' ще колизира top-level модули (catalog/config/export_api/sources). "
            f"Пусни отделна инвокация per регион (journal-backfill --region {region})."
        )
    root = str(_dashboard_root(region))
    if not Path(root).exists():
        raise FileNotFoundError(
            f"{_DASHBOARD_REPO.get(region, region)} не е намерен: {root}. Сетни {_ROOT_ENV[region]}."
        )
    if root not in sys.path:
        sys.path.insert(0, root)

    if region == "US":
        from catalog.series import SERIES_CATALOG          # noqa: E402
        from config import FRED_API_KEY                     # noqa: E402
        from export_api import LENSES, build_macro_state    # noqa: E402
        from sources.fred_adapter import FredAdapter        # noqa: E402
        adapter = FredAdapter(api_key=FRED_API_KEY, base_dir=root)
        snapshot = adapter.get_snapshot(SERIES_CATALOG.keys())  # cache-only, без fetch
    elif region == "EU":
        from export_api import (                            # noqa: E402
            LENSES,
            _build_snapshot,
            build_macro_state,
        )
        from sources.ecb_adapter import EcbAdapter          # noqa: E402
        from sources.eurostat_adapter import EurostatAdapter  # noqa: E402
        _buf = io.StringIO()
        with contextlib.redirect_stdout(_buf):              # build print-ове → cp1252 краш иначе
            snapshot = _build_snapshot(
                {"ecb": EcbAdapter(), "eurostat": EurostatAdapter()}, force=False
            )
    elif region == "CN":
        # China е native-composite + multi-adapter (WorldBank/IMF/AkShare/DBnomics).
        # Няма константа LENSES — lens наборът идва от export_api.MODULES_ORDER (5 модула,
        # core 4 + property). build_macro_state връща ms["lenses"] keyed по module name
        # (growth/inflation/labor/credit/property) с per-lens "score" = модулния composite
        # (0–100 healthiness, higher = по-здрав) → СЪЩИЯТ интерфейс като US/EU.
        from export_api import (                            # noqa: E402
            MODULES_ORDER,
            build_macro_state,
        )
        from run import _build_adapters, _build_snapshot    # noqa: E402
        LENSES = tuple(name for name, _ in MODULES_ORDER)   # 5 lens имена
        _buf = io.StringIO()
        with contextlib.redirect_stdout(_buf):              # adapter/snapshot print-ове → cp1252 краш иначе
            snapshot = _build_snapshot(_build_adapters(), force=False)  # cache-only
    else:
        raise NotImplementedError(
            f"bridge за регион '{region}' още не е имплементиран "
            f"(познати: US/EU/CN). Германия/Япония/Корея = config-врати после."
        )

    if len(snapshot) < 10:
        raise RuntimeError(
            f"{region} cache почти празен ({len(snapshot)} серии). "
            f"Стартирай `python export_api.py --refresh` в {_DASHBOARD_REPO[region]}."
        )
    bridge = _Bridge(region=region, snapshot=snapshot,
                     build_macro_state=build_macro_state, lenses=tuple(LENSES))
    _BRIDGES[region] = bridge
    _LOADED_REGION = region
    return bridge


def reconstruct_scores_as_of(d: date, region: str = "US",
                             bridge: _Bridge | None = None) -> dict | None:
    """Реконструирани lens scores as-of дата d (trim → build_macro_state).

    Връща {lens: score за всеки lens в региона, 'as_of_date': date} или None ако
    snapshot-ът няма достатъчно данни преди d. Lens наборът = dashboard LENSES
    (US: labor/growth/inflation/liquidity · EU: labor/growth/inflation/credit).
    """
    b = bridge or _load_bridge(region)
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
    for lens in b.lenses:
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
    scores = reconstruct_scores_as_of(week.week_end, w.region, bridge)
    if scores is None:
        return None
    as_of = scores.pop("as_of_date", None)
    return economy_axis_from_scores(scores, w, as_of_date=as_of, week_end=week.week_end)
