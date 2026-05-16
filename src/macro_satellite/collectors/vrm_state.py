"""Парсер за VRM_STATE.md.

Извлича:
- last_updated_md: от '**Последна актуализация:** YYYY-MM-DD' или 'DD.MM.YYYY'
- regime: от 'РЕЖИМ:' line — REFLATION / GROWTH / STAGFLATION / ...
- ks_status: от 'KILL SWITCH:' line — ДЕАКТИВИРАН → 'inactive', АКТИВИРАН → 'active'
- alignment_score / alignment_total: от 'Alignment X/Y' (или 'Alignment X.X/Y')
- gms_value: от 'GMS X/Y' ако присъства (нерегулярно)
"""
from __future__ import annotations

import re
from datetime import date, datetime

import pandas as pd

from ..utils.dates import utc_now


_RE_LAST_UPDATED_ISO = re.compile(r"Последна актуализация:?\*?\*?\s*(\d{4}-\d{2}-\d{2})")
_RE_LAST_UPDATED_DOT = re.compile(r"Последна актуализация:?\*?\*?\s*(\d{2}\.\d{2}\.\d{4})")
_RE_REGIME = re.compile(r"РЕЖИМ:?\s*([A-ZА-Я_/]+)")
_RE_KS = re.compile(r"KILL SWITCH:?\s*[^\w]*(ДЕАКТИВИРАН|АКТИВИРАН|STANDBY|АКТИВЕН)", re.IGNORECASE)
_RE_ALIGNMENT = re.compile(r"Alignment[:\s]+(\d+(?:\.\d+)?)/(\d+)", re.IGNORECASE)
_RE_GMS = re.compile(r"GMS[:\s]+(\d+(?:\.\d+)?)/(\d+)", re.IGNORECASE)


def _parse_date_iso_or_dot(s: str) -> date | None:
    try:
        if "-" in s:
            return date.fromisoformat(s)
        if "." in s:
            return datetime.strptime(s, "%d.%m.%Y").date()
    except ValueError:
        return None
    return None


def _normalize_ks(raw: str) -> str:
    raw = raw.upper()
    if "ДЕАКТИВИРАН" in raw:
        return "inactive"
    if "АКТИВЕН" in raw or "АКТИВИРАН" in raw:
        return "active"
    if "STANDBY" in raw:
        return "standby"
    return raw.lower()


def parse(raw: bytes, snapshot_date: date | None = None, source: str = "vrm_state") -> pd.DataFrame:
    text = raw.decode("utf-8", errors="replace")

    last_updated: date | None = None
    m = _RE_LAST_UPDATED_ISO.search(text)
    if m:
        last_updated = _parse_date_iso_or_dot(m.group(1))
    else:
        m = _RE_LAST_UPDATED_DOT.search(text)
        if m:
            last_updated = _parse_date_iso_or_dot(m.group(1))

    regime = None
    m = _RE_REGIME.search(text)
    if m:
        regime = m.group(1).strip()

    ks_status = None
    m = _RE_KS.search(text)
    if m:
        ks_status = _normalize_ks(m.group(1))

    alignment_score: float | None = None
    alignment_total: int | None = None
    m = _RE_ALIGNMENT.search(text)
    if m:
        alignment_score = float(m.group(1))
        alignment_total = int(m.group(2))

    gms_value: float | None = None
    m = _RE_GMS.search(text)
    if m:
        gms_value = float(m.group(1))

    if snapshot_date is None:
        snapshot_date = last_updated
    if snapshot_date is None:
        raise ValueError("VRM_STATE.md: cannot determine snapshot_date (no last_updated, no override)")

    is_change_day = last_updated == snapshot_date

    return pd.DataFrame([{
        "date": snapshot_date,
        "regime": regime,
        "ks_status": ks_status,
        "alignment_score": alignment_score,
        "alignment_total": alignment_total,
        "gms_value": gms_value,
        "last_updated_md": last_updated,
        "is_change_day": is_change_day,
        "source": source,
        "source_path": "vrm-state/VRM_STATE.md",
        "ingested_at": utc_now(),
    }])
