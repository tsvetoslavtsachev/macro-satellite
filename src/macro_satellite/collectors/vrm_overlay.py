"""Collector за живия data-core VRM weekly overlay (source_kind: datacore-state).

Чете `vrm_overlay.json[-1]` (свежия W-FRI запис) от DATACORE_STATE_DIR — READ-ONLY
към data-core — и го мапва към `vrm` таблицата. Това е живата VRM health-лампа:
S14 мери свежестта от max(date) на таблицата, точно както при github сензорите.
Единственият VRM канал: ръчните vrm_state/vrm_week са пенсионирани изцяло
(мандат №36, 07.2026) — всички читатели (briefing/narrative/full_export/
journal/state_export/dashboard/delta) четат таблица `vrm`.

Cardinal rule: извличаме само това, което мозъкът реално emit-ва (regime/alignment/
gms/kill_switch). Липсва ли overlay (без env/checkout/файл) или липсва ядрото →
връща None → run_collect пропуска записа (degrade-safe; S14 показва сензора
'missing' честно, не фалшиво-свежо). Не гадаем формат.

KS изворът (25.07.2026, стъпка 3 на VRM прегледа): живата KS истина е S6e
state-machine серията `vrm_ks_state.json` — overlay блокът `kill_switch` е legacy
остатък с active=null по конструкция на ВСИЧКИ редове. Колекторът чете ks_active
от state серията при съвпадащ as_of с overlay върха; разминаване/липса → fallback
към overlay блока (старото поведение), т.е. None → state_export казва 'unknown'.
"""
from __future__ import annotations

import json
import os
from datetime import date
from pathlib import Path
from typing import Any

import pandas as pd

from ..logging_setup import get_logger
from ..utils.dates import utc_now

log = get_logger(__name__)


def _overlay_path() -> Path | None:
    """DATACORE_STATE_DIR/vrm_overlay.json, ако env е сложен И файлът съществува."""
    state_dir = os.environ.get("DATACORE_STATE_DIR")
    if not state_dir:
        return None
    p = Path(state_dir) / "vrm_overlay.json"
    return p if p.exists() else None


def _ks_active_from_state(state_dir: Path, as_of: date) -> bool | None:
    """Живата KS истина: vrm_ks_state.json[-1].active (S6e state-machine).

    Приема се САМО при съвпадащ as_of с overlay върха — разминаване значи, че
    мозъкът е писал частично, и тогава не гадаем (None). Липсващ/нечетим файл
    или не-булев active → None (degrade-safe, fallback пътят поема)."""
    p = state_dir / "vrm_ks_state.json"
    if not p.exists():
        return None
    try:
        tip = json.loads(p.read_text(encoding="utf-8"))[-1]
        tip_as_of = date.fromisoformat(str(tip.get("as_of"))[:10])
    except (json.JSONDecodeError, IndexError, OSError, TypeError, ValueError) as e:  # noqa: BLE001
        log.warning("vrm ks_state read failed — ks_active stays None",
                    extra={"path": str(p), "error": str(e)})
        return None
    if tip_as_of != as_of:
        log.warning("vrm ks_state as_of mismatch — ks_active stays None",
                    extra={"ks_as_of": str(tip_as_of), "overlay_as_of": str(as_of)})
        return None
    active = tip.get("active")
    return active if isinstance(active, bool) else None


def _num(v: Any) -> float | None:
    try:
        return float(v) if v is not None else None
    except (TypeError, ValueError):
        return None


def _int(v: Any) -> int | None:
    try:
        return int(v) if v is not None else None
    except (TypeError, ValueError):
        return None


def collect_overlay(source: str = "vrm_live") -> pd.DataFrame | None:
    """Жив VRM tip → 1-ред DataFrame за `vrm` таблицата.

    Връща None ако overlay липсва/нечетим или ядрото (as_of/regime) липсва — тогава
    run_collect пропуска и S14 показва сензора честно като 'missing'/'stale'.
    """
    path = _overlay_path()
    if path is None:
        log.warning("vrm overlay unavailable (no DATACORE_STATE_DIR or file missing)")
        return None
    try:
        records = json.loads(path.read_text(encoding="utf-8"))
        ov = records[-1]
    except (json.JSONDecodeError, IndexError, OSError, TypeError) as e:  # noqa: BLE001
        log.warning("vrm overlay read failed",
                    extra={"path": str(path), "error": str(e)})
        return None

    as_of_raw = ov.get("as_of")
    regime = ov.get("regime")
    if not as_of_raw or not regime:  # липсва ядро → не гадаем (cardinal rule)
        log.warning("vrm overlay tip missing as_of/regime — skip",
                    extra={"as_of": as_of_raw})
        return None
    try:
        as_of = date.fromisoformat(str(as_of_raw)[:10])
    except ValueError:
        log.warning("vrm overlay as_of unparseable", extra={"as_of": as_of_raw})
        return None

    gms = ov.get("gms") or {}
    # KS: първо живата S6e state серия (vrm_ks_state.json, as_of-matched); чак после
    # overlay блокът kill_switch (legacy, active=null по конструкция) като fallback.
    ks_active = _ks_active_from_state(path.parent, as_of)
    if ks_active is None:
        ks = ov.get("kill_switch") or {}
        ks_active = ks.get("active")
    return pd.DataFrame([{
        "date": as_of,
        "as_of": as_of,
        "regime": regime,
        "alignment_score": _num(ov.get("alignment_score")),
        "gms_score": _num(gms.get("score")),
        "gms_max": _int(gms.get("max")),
        "gms_tier": gms.get("tier"),
        "ks_active": ks_active if isinstance(ks_active, bool) else None,
        "source": source,
        "ingested_at": utc_now(),
    }])
