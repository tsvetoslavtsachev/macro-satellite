# -*- coding: utf-8 -*-
"""yfinance backfill: RAW-close convention + phantom-bar guard (mandate #32-B).

Proves the yfinance path stores the RAW ``close`` (not ``adj_close``) so etf_prices is one
convention across sources, and that a holiday-dated bar is dropped at the write boundary."""
from __future__ import annotations

import importlib
from datetime import date

import pandas as pd
import pytest

from macro_satellite.config import EtfUniverseConfig


def _reload_yb():
    from macro_satellite.backfill import yfinance_backfill as yb
    importlib.reload(yb)
    return yb


def test_yf_stores_raw_close_and_drops_holiday(isolated_storage, monkeypatch):
    yb = _reload_yb()
    from macro_satellite.storage import parquet_writer

    def _fake_history(symbol, period="5y", interval="1d"):
        # auto_adjust=False shape: raw ``close`` AND a dividend-adjusted ``adj_close`` both present.
        return pd.DataFrame([
            {"date": date(2026, 6, 18), "open": 745, "high": 748, "low": 744,
             "close": 746.0, "adj_close": 740.0, "volume": 10},
            {"date": date(2026, 6, 19), "open": 746, "high": 747, "low": 745,   # Juneteenth
             "close": 746.74, "adj_close": 740.5, "volume": 11},
            {"date": date(2026, 6, 22), "open": 747, "high": 749, "low": 746,
             "close": 747.0, "adj_close": 741.0, "volume": 12},
        ])
    monkeypatch.setattr(yb, "fetch_history", _fake_history)

    cfg = EtfUniverseConfig(period="1mo", interval="1d", symbols=["SPY"])
    yb.run_yf_backfill(cfg=cfg, period="1mo")

    df = parquet_writer.read_table("etf_prices")
    spy = df[df.symbol == "SPY"].set_index("date")
    assert date(2026, 6, 19) not in spy.index                       # Juneteenth phantom dropped
    assert spy.loc[date(2026, 6, 18), "price"] == pytest.approx(746.0)   # RAW close, not 740.0 adj
    assert spy.loc[date(2026, 6, 22), "price"] == pytest.approx(747.0)
    # close_yf keeps the raw close too -> price == close_yf (one convention).
    assert spy.loc[date(2026, 6, 18), "close_yf"] == pytest.approx(746.0)


def test_yf_row_schema_ignores_adj_close():
    """Unit: _yf_row_to_etf_schema picks ``close`` even when ``adj_close`` is present."""
    yb = _reload_yb()
    row = pd.Series({"date": date(2026, 6, 18), "open": 1.0, "high": 1.0, "low": 1.0,
                     "close": 746.0, "adj_close": 740.0, "volume": 10})
    out = yb._yf_row_to_etf_schema("SPY", row)
    assert out["price"] == pytest.approx(746.0)      # raw close
    assert out["close_yf"] == pytest.approx(746.0)
