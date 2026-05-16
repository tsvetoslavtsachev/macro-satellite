"""Парсер за vrm-state/VRM_WEEK.md.

Извлича weekly ядрото от структурираните code блокове в Markdown файла:
- VRM ЯДРО: regime, signal, alignment, GMS scores
- KILL SWITCH: ks_active, variant, weeks_active, portfolio
- GAP АНАЛИЗ 4W: SPY/QQQ/XLE/GLD/TLT/TIP/IWM 4W returns
"""
from __future__ import annotations

import re
from datetime import date, datetime, timedelta

import pandas as pd

from ..utils.dates import utc_now


def _kv_block(text: str, key: str) -> str | None:
    """Извлича value за KEY: VALUE pattern, толерира whitespace и trailing comments."""
    pat = re.compile(rf"^{re.escape(key)}\s*:\s*(.+?)$", re.MULTILINE)
    m = pat.search(text)
    if not m:
        return None
    return m.group(1).strip()


def _parse_pct(s: str | None) -> float | None:
    """+12.09% → 0.1209, -3.0% → -0.030."""
    if not s:
        return None
    m = re.search(r"([+-]?\d+(?:\.\d+)?)\s*%", s)
    if not m:
        return None
    return float(m.group(1)) / 100.0


def _parse_score_pair(s: str | None) -> tuple[float | None, int | None]:
    """'6.0' → (6.0, None); '6.0/8' → (6.0, 8); '7/8 MEDIUM' → (7.0, 8)."""
    if not s:
        return None, None
    m = re.search(r"(\d+(?:\.\d+)?)\s*/\s*(\d+)", s)
    if m:
        return float(m.group(1)), int(m.group(2))
    m = re.search(r"(\d+(?:\.\d+)?)", s)
    if m:
        return float(m.group(1)), None
    return None, None


def _parse_date_label(s: str | None) -> date | None:
    if not s:
        return None
    # try ISO
    m = re.search(r"(\d{4}-\d{2}-\d{2})", s)
    if m:
        try:
            return date.fromisoformat(m.group(1))
        except ValueError:
            return None
    m = re.search(r"(\d{2})\.(\d{2})\.(\d{4})", s)
    if m:
        try:
            return date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
        except ValueError:
            return None
    return None


def parse(raw: bytes, snapshot_date: date | None = None,
          source: str = "vrm_week") -> pd.DataFrame:
    text = raw.decode("utf-8", errors="replace")

    # Header
    last_updated = None
    m = re.search(r"Последна актуализация:?\*?\*?\s*(\d{4}-\d{2}-\d{2})", text)
    if m:
        last_updated = date.fromisoformat(m.group(1))

    week_start = week_end = None
    m = re.search(r"Седмица:?\*?\*?\s*(\d{4}-\d{2}-\d{2})\s*→\s*(\d{4}-\d{2}-\d{2})", text)
    if m:
        week_start = date.fromisoformat(m.group(1))
        week_end = date.fromisoformat(m.group(2))

    approved = None
    m = re.search(r"Одобрено от Цветослав:?\*?\*?\s*(ДА|НЕ)", text, re.IGNORECASE)
    if m:
        approved = m.group(1).upper() == "ДА"

    def _parse_int(s: str | None) -> int | None:
        if not s:
            return None
        m = re.search(r"(\d+)", s)
        return int(m.group(1)) if m else None

    # VRM ЯДРО block
    regime = _kv_block(text, "РЕЖИМ")
    regime_bg = _kv_block(text, "РЕЖИМ_БГ")
    signal = _kv_block(text, "СИГНАЛ")
    align_score, align_max = _parse_score_pair(_kv_block(text, "ALIGNMENT"))
    align_max = align_max or _parse_int(_kv_block(text, "ALIGNMENT_MAX"))
    alignment_label = _kv_block(text, "ALIGNMENT_LABEL")
    gms_score, gms_max = _parse_score_pair(_kv_block(text, "GMS_SCORE"))
    gms_max = gms_max or _parse_int(_kv_block(text, "GMS_MAX"))
    gms_label = _kv_block(text, "GMS_LABEL")

    # KILL SWITCH block
    ks_active_str = _kv_block(text, "KS_АКТИВЕН")
    ks_active = ks_active_str.upper() == "ДА" if ks_active_str else None
    ks_variant = _kv_block(text, "KS_ВАРИАНТ")
    ks_weeks = _kv_block(text, "KS_СЕДМИЦИ_АКТИВЕН")
    ks_weeks_f = float(ks_weeks) if ks_weeks and re.match(r"^\d+(\.\d+)?$", ks_weeks) else None
    ks_portfolio = _kv_block(text, "KS_ПОРТФЕЙЛ")
    ks_eu_portfolio = _kv_block(text, "KS_EU_ПОРТФЕЙЛ")

    # GAP АНАЛИЗ 4W
    metrics = {}
    for key in ("SPY_4W", "QQQ_4W", "XLE_4W", "GLD_4W", "TLT_4W", "TIP_4W", "IWM_4W"):
        metrics[key.lower()] = _parse_pct(_kv_block(text, key))

    # snapshot_date defaults to week_start, иначе last_updated
    if snapshot_date is None:
        snapshot_date = week_start or last_updated
    if snapshot_date is None:
        raise ValueError("VRM_WEEK.md: cannot determine snapshot_date")

    row = {
        "date": snapshot_date,
        "week_start": week_start,
        "week_end": week_end,
        "last_updated_md": last_updated,
        "approved": approved,
        "regime": regime,
        "regime_bg": regime_bg,
        "signal": signal,
        "alignment": align_score,
        "alignment_max": align_max,
        "alignment_label": alignment_label,
        "gms_score": gms_score,
        "gms_max": gms_max,
        "gms_label": gms_label,
        "ks_active": ks_active,
        "ks_variant": ks_variant,
        "ks_weeks_active": ks_weeks_f,
        "ks_portfolio": ks_portfolio,
        "ks_eu_portfolio": ks_eu_portfolio,
        **metrics,
        "source": source,
        "ingested_at": utc_now(),
    }
    return pd.DataFrame([row])
