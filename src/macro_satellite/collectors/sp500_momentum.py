"""Парсер за SP500-momentumrank/data.json (~503 stocks)."""
from __future__ import annotations

import json
from datetime import date

import pandas as pd

from ..utils.dates import utc_now

_FIELD_MAP = {
    "symbol": "symbol", "name": "name", "sector": "sector",
    "price": "price", "marketCap": "market_cap",
    "return1m": "return_1m", "return3m": "return_3m",
    "return6m": "return_6m", "return12m": "return_12m",
    "volatility": "volatility", "avgVolume": "avg_volume",
    "dayChange": "day_change", "sharpe": "sharpe", "drawdown": "drawdown",
    "high52w": "high_52w", "low52w": "low_52w", "drawdown52w": "drawdown_52w",
    "momentumScore": "momentum_score", "weight": "weight",
    "stale": "stale", "rank": "rank",
}


def parse(raw: bytes, snapshot_date: date | None = None,
          source: str = "sp500_momentum") -> pd.DataFrame:
    items = json.loads(raw)
    if not isinstance(items, list):
        raise ValueError("sp500_momentum: expected JSON array")
    if snapshot_date is None:
        # No embedded date; commit timestamp ще се сетне при backfill, иначе today UTC
        from ..utils.dates import today_utc
        snapshot_date = today_utc()

    now = utc_now()
    rows = []
    for it in items:
        row = {dst: it.get(src) for src, dst in _FIELD_MAP.items()}
        row["country"] = None
        row["exchange"] = None
        row["currency"] = None
        row["date"] = snapshot_date
        row["source"] = source
        row["ingested_at"] = now
        rows.append(row)
    df = pd.DataFrame(rows)
    if not df.empty:
        for c in ("avg_volume",):
            df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int64")
        for c in ("rank",):
            df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int32")
    return df
