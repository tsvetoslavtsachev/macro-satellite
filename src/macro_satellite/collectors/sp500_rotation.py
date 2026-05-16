"""Парсер за SP500 Rotation Radar.

Top-level keys: metadata, stable_winners_1m, stable_winners_3m, quality_dip_1m,
quality_dip_3m, faded_bounces_1m, current_strength, rank_all_stocks,
sector_rotation, sub_industry_rotation, ...

Източник на истината за per-ticker записи: `rank_all_stocks` (~500 items, цял универсум,
включва quadrant_1m, quadrant_3m). Полето `trajectory` се игнорира — history-та се
изгражда от daily snapshots, не от вградени trajectory списъци.

Нормализиране на quadrant: source използва смесени стойности
('Stable Winner', 'stable_winner', 'Neutral', '—', 'decayer'...). Нормализираме към
snake_case + lowercase, '—' → 'other'.
"""
from __future__ import annotations

import json
from datetime import date

import pandas as pd

from ..utils.dates import parse_iso_date, utc_now


def _normalize_quadrant(v: str | None) -> str | None:
    if v is None or v == "—" or v == "":
        return "other"
    s = str(v).strip().lower().replace(" ", "_")
    return s


def parse(raw: bytes, snapshot_date: date | None = None, source: str = "sp500_rotation") -> pd.DataFrame:
    doc = json.loads(raw)
    md = doc.get("metadata", {})

    if snapshot_date is None:
        as_of = md.get("as_of")
        if not as_of:
            raise ValueError("SP500 rotation: missing metadata.as_of")
        snapshot_date = parse_iso_date(as_of)

    items = doc.get("rank_all_stocks", [])
    if not items:
        raise ValueError("SP500 rotation: 'rank_all_stocks' is missing or empty")

    now = utc_now()
    rows = []
    for it in items:
        rows.append({
            "date": snapshot_date,
            "ticker": it.get("ticker"),
            "name": it.get("name"),
            "sector": it.get("sector"),
            "sub_industry": it.get("sub_industry"),
            "current_rank": it.get("current_rank"),
            "abs_strength": it.get("abs_strength"),
            "mom_12_1_pct": it.get("mom_12_1_pct"),
            "base_rank_6m": it.get("base_rank_6m"),
            "delta_1m": it.get("delta_1m"),
            "delta_3m": it.get("delta_3m"),
            "quadrant_1m": _normalize_quadrant(it.get("quadrant_1m")),
            "quadrant_3m": _normalize_quadrant(it.get("quadrant_3m")),
            "source": source,
            "ingested_at": now,
        })

    df = pd.DataFrame(rows)
    if not df.empty:
        for c in ("current_rank", "base_rank_6m", "abs_strength", "mom_12_1_pct",
                  "delta_1m", "delta_3m"):
            if c in df.columns:
                df[c] = pd.to_numeric(df[c], errors="coerce")
    return df
