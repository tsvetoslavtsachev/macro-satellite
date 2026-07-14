"""VRM канон — живият режимен речник + KS статус деривация (мандат №36).

ЕДИНСТВЕНОТО място, което знае речника на живия мозък (data-core
`vrm_overlay.json`). Всички консуматори (organism_export, journal/vrm_snapshot,
briefing/narrative/full_export/state_export/dashboard/delta) внасят оттук —
не дублират. Старият речник на ръчната серия (STAGFLATION/GOLDILOCKS/RECESSION)
е пенсиониран заедно с vrm_state/vrm_week (07.2026).

Бележка за alignment знаменателя: живият колектор (collectors/vrm_overlay.py)
НЕ ingest-ва alignment max (осемте alignment_flags на overlay-а не влизат в
таблица `vrm`) → display пътищата показват голото число (напр. „6.0", не
„6.0/8") — не фабрикуваме знаменател. Кандидат-разширение на колектора:
вж. мандат №36 receipt.
"""
from __future__ import annotations

from typing import Any

# Режимите, които живият мозък реално emit-ва (огледало на data-core
# vrm_overlay.json). BG етикетите ползва организмовата витрина.
REGIME_BG: dict[str, str] = {
    "REFLATION": "РЕФЛАЦИЯ", "GROWTH": "РАСТЕЖ", "STAGNATION": "СТАГНАЦИЯ",
    "CRISIS": "КРИЗА", "DEFLATION": "ДЕФЛАЦИЯ",
}

# За corruption детекция (journal C6): наличен ред с regime извън това = drift.
KNOWN_REGIMES: frozenset[str] = frozenset(REGIME_BG)


def ks_status_from_active(active: Any) -> str:
    """bool|None → display статус. None ≠ inactive: мозъкът emit-ва None при
    неизвестно → „unknown" (не фабрикуваме сигурност). NaN (pandas) = None."""
    if active is None:
        return "unknown"
    try:
        if active != active:  # NaN
            return "unknown"
    except Exception:  # noqa: BLE001 — екзотичен тип → не гадаем
        return "unknown"
    return "active" if bool(active) else "inactive"
