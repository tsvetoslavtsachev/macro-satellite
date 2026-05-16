"""Парсер за COT Monitor derived/watchlist.json.

Един файл, един snapshot, всички tracked markets с асет клас, percentile, position,
delta. По-просто от manifest + per-market fetches.

Структура: list[ {market, title, subtitle, date, score, regime,
                  primary_percentile (0-1), primary_zscore, primary_net,
                  primary_delta_4w, secondary_net, ..., streak_*, takeaway, rank} ]
"""
from __future__ import annotations

import json
from datetime import date, datetime

import pandas as pd

from ..utils.dates import utc_now


def _parse_report_date(s: str | None) -> date | None:
    if not s:
        return None
    # '2026-05-12T00:00:00.000' или '2026-05-12'
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).date()
    except ValueError:
        return None


def parse(raw: bytes, snapshot_date: date | None = None, source: str = "cot_monitor") -> pd.DataFrame:
    items = json.loads(raw)
    if not isinstance(items, list):
        raise ValueError("watchlist.json: expected a list")

    if snapshot_date is None:
        # вади най-късната date от items
        rds = [_parse_report_date(it.get("date")) for it in items if it.get("date")]
        rds = [d for d in rds if d is not None]
        if not rds:
            raise ValueError("watchlist.json: no parsable 'date' field in items and no snapshot_date provided")
        snapshot_date = max(rds)

    now = utc_now()
    rows = []
    for it in items:
        # primary_percentile in source is already 0-100 (verified: nasdaq=0.19 with
        # z=-2.08 matches percentile≈0.2%, soyoil=99.43 with z=+2.42 matches 99%).
        pct = it.get("primary_percentile")
        pct_val = float(pct) if isinstance(pct, (int, float)) else None
        rows.append({
            "date": snapshot_date,
            "market": it.get("market"),
            "asset_class": it.get("subtitle"),
            "report_date": _parse_report_date(it.get("date")),
            "net_position": it.get("primary_net"),
            "net_position_pct": pct_val,
            "percentile_3y": None,
            "percentile_5y": pct_val,
            "weekly_change": it.get("primary_delta_4w"),
            "on_watchlist": True,
            "source": source,
            "ingested_at": now,
        })

    df = pd.DataFrame(rows)
    if not df.empty:
        for c in ("net_position", "weekly_change"):
            if c in df.columns:
                df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int64")
    return df
