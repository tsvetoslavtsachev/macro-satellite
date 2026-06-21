"""Тестов helper: ETF fixture JSON → etf_prices schema DataFrame.

Портната логика от премахнатия `collectors/etf_dashboard.py` (S17 Build D2,
2026-06-22). Парсерът вече НЕ е в живия collect път — etf_prices се пълни от
yfinance (backfill-yf). Но storage/delta/idempotency тестовете още имат нужда от
детерминистичен data-generator върху малките offline ETF fixtures, затова
логиката се пази тук, в тестовете, а не в продукцията.

Top-level fixture форма: {"updatedAt": "<ISO>", "etfs": [{...}, ...], ...}
"""
from __future__ import annotations

import json
from datetime import date

import pandas as pd

from macro_satellite.utils.dates import parse_iso_datetime, utc_now

# Map camelCase JSON → snake_case колони (както старият парсер)
_FIELD_MAP = {
    "symbol": "symbol",
    "name": "name",
    "category": "category",
    "region": "region",
    "price": "price",
    "volume": "volume",
    "return1m": "return_1m",
    "return3m": "return_3m",
    "return6m": "return_6m",
    "return12m": "return_12m",
    "returnYTD": "return_ytd",
    "volatility": "volatility",
    "sharpe": "sharpe",
    "maxDrawdown": "max_drawdown",
    "high52w": "high_52w",
    "low52w": "low_52w",
    "pctFromHigh": "pct_from_high",
    "rsScore": "rs_score",
    "aum": "aum",
    "flow1m": "flow_1m",
    "flow3m": "flow_3m",
    "flow6m": "flow_6m",
    "flowYTD": "flow_ytd",
}


def parse_etf_fixture(raw: bytes, snapshot_date: date | None = None,
                      source: str = "etf_fixture") -> pd.DataFrame:
    """ETF fixture bytes → DataFrame със etf_prices schema колони."""
    doc = json.loads(raw)
    etfs = doc.get("etfs", [])
    if not isinstance(etfs, list):
        raise ValueError("etfs.json: 'etfs' must be a list")

    # snapshot_date override → use it; иначе вади от updatedAt.date() в UTC
    if snapshot_date is None:
        updated_at = doc.get("updatedAt")
        if updated_at:
            snapshot_date = parse_iso_datetime(updated_at).date()
        else:
            raise ValueError("etfs.json: missing 'updatedAt' and no snapshot_date provided")

    rows = []
    now = utc_now()
    for etf in etfs:
        row = {dst: etf.get(src) for src, dst in _FIELD_MAP.items()}
        row["date"] = snapshot_date
        row["source"] = source
        row["ingested_at"] = now
        rows.append(row)

    return pd.DataFrame(rows)
