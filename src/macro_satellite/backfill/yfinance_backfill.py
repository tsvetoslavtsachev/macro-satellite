"""yfinance bootstrap за raw ETF prices.

Дава дълъг price history (5y default), независимо от ETF Dashboard git history.
Източник 'yfinance'. Merge правило (delegated to merge.py): git печели за overlap dates.
"""
from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from ..config import EtfUniverseConfig, load_etf_universe
from ..logging_setup import get_logger
from ..storage import parquet_writer
from ..utils.dates import utc_now

log = get_logger(__name__)


@dataclass
class YfBackfillResult:
    symbols_requested: int = 0
    symbols_with_data: int = 0
    rows_written: int = 0
    errors: list[str] = None  # type: ignore

    def __post_init__(self):
        if self.errors is None:
            self.errors = []


def fetch_history(symbol: str, period: str = "5y", interval: str = "1d") -> pd.DataFrame:
    """yfinance daily OHLCV. Връща df с колони open/high/low/close/volume + date."""
    import yfinance as yf
    t = yf.Ticker(symbol)
    h = t.history(period=period, interval=interval, auto_adjust=False)
    if h.empty:
        return pd.DataFrame()
    h = h.reset_index()
    # Колоните: Date, Open, High, Low, Close, Adj Close (sometimes), Volume
    # Normalize:
    rename = {c: c.lower().replace(" ", "_") for c in h.columns}
    h = h.rename(columns=rename)
    if "date" not in h.columns:
        # 'datetime' от intraday — не би трябвало за interval='1d'
        for cand in ("datetime", "index"):
            if cand in h.columns:
                h = h.rename(columns={cand: "date"})
                break
    # Make date a python date (drop time)
    h["date"] = pd.to_datetime(h["date"]).dt.date
    return h


def _yf_row_to_etf_schema(symbol: str, row: pd.Series) -> dict:
    """yfinance row → etf_prices schema-compatible dict."""
    price = row.get("adj_close") if "adj_close" in row else row.get("close")
    return {
        "date": row["date"],
        "symbol": symbol,
        "name": None,
        "category": None,
        "region": None,
        "price": float(price) if pd.notna(price) else None,
        "volume": int(row["volume"]) if pd.notna(row.get("volume")) else None,
        "return_1m": None, "return_3m": None, "return_6m": None,
        "return_12m": None, "return_ytd": None,
        "volatility": None, "sharpe": None, "max_drawdown": None,
        "high_52w": None, "low_52w": None, "pct_from_high": None,
        "rs_score": None, "aum": None,
        "flow_1m": None, "flow_3m": None, "flow_6m": None, "flow_ytd": None,
        "open_yf": float(row["open"]) if pd.notna(row.get("open")) else None,
        "high_yf": float(row["high"]) if pd.notna(row.get("high")) else None,
        "low_yf": float(row["low"]) if pd.notna(row.get("low")) else None,
        "close_yf": float(row["close"]) if pd.notna(row.get("close")) else None,
        "source": "yfinance",
        "ingested_at": utc_now(),
    }


def run_yf_backfill(cfg: EtfUniverseConfig | None = None) -> YfBackfillResult:
    """Backfill за всички symbols от etf_universe.yaml. yfinance НЕ overwrite-ва git
    snapshots — upsert по (date, symbol). За dates, които вече имат git source с
    напълно populated полета, yfinance row ще overwrite-не само поле `source`
    към 'yfinance', което е НЕ желателно.
    Затова merge.py отделно прави git-wins логика. Тук просто пишем yfinance rows.
    """
    cfg = cfg or load_etf_universe()
    result = YfBackfillResult(symbols_requested=len(cfg.symbols))

    for sym in cfg.symbols:
        try:
            h = fetch_history(sym, period=cfg.period, interval=cfg.interval)
            if h.empty:
                log.warning("yfinance: empty history", extra={"symbol": sym})
                continue
            rows = [_yf_row_to_etf_schema(sym, r) for _, r in h.iterrows()]
            df = pd.DataFrame(rows)
            n = parquet_writer.upsert("etf_prices", df, key_cols=["symbol"])
            result.symbols_with_data += 1
            result.rows_written += n
            log.info("yfinance backfill ok", extra={"symbol": sym, "rows": n})
        except Exception as e:
            result.errors.append(f"{sym}: {e}")
            log.error("yfinance backfill failed", extra={"symbol": sym, "error": str(e)})

    return result
