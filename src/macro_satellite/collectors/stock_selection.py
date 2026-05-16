"""Парсер за stock-selection-dashboard/app/data/ranked_stocks.json.

503 акции, всяка с composite_score + 4 factor scores + ~20 fundamental метрики.
snapshot_date се вади от market_summary.json (отделен файл).

Текущата имплементация: чете снъпшот датата от env var ако подадена при backfill,
иначе used today_utc при live. За backfill снъпшот датата ще дойде от git commit.
"""
from __future__ import annotations

import json
from datetime import date

import pandas as pd

from ..utils.dates import utc_now

_FIELD_MAP = {
    "rank": "rank", "ticker": "ticker", "name": "name", "sector": "sector",
    "composite_score": "composite_score",
    "trend_score": "trend_score", "quality_score": "quality_score",
    "value_score": "value_score", "risk_score": "risk_score",
    "ret_13w": "ret_13w", "ret_26w": "ret_26w", "ret_52w": "ret_52w",
    "volatility_26w": "volatility_26w",
    "pe_ratio": "pe_ratio", "pb_ratio": "pb_ratio",
    "ev_ebitda": "ev_ebitda", "ev_ebit": "ev_ebit",
    "roe": "roe", "roic": "roic", "debt_equity": "debt_equity",
    "eps_ttm": "eps_ttm", "dividend_yield": "dividend_yield",
    "revenue_growth_ttm": "revenue_growth_ttm",
    "oper_margin_ttm": "oper_margin_ttm",
    "gross_margin_ttm": "gross_margin_ttm",
    "fcf_margin": "fcf_margin",
}


def parse(raw: bytes, snapshot_date: date | None = None,
          source: str = "stock_selection") -> pd.DataFrame:
    items = json.loads(raw)
    if not isinstance(items, list):
        raise ValueError("stock_selection: expected JSON array")
    if snapshot_date is None:
        from ..utils.dates import today_utc
        snapshot_date = today_utc()

    now = utc_now()
    rows = []
    for it in items:
        row = {dst: it.get(src) for src, dst in _FIELD_MAP.items()}
        row["date"] = snapshot_date
        row["source"] = source
        row["ingested_at"] = now
        rows.append(row)
    df = pd.DataFrame(rows)
    if not df.empty:
        for c in ("rank",):
            df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int32")
    return df
