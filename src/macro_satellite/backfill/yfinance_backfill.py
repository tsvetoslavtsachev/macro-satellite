"""yfinance bootstrap за raw ETF prices.

Дава дълъг price history (5y default), независимо от ETF Dashboard git history.
Източник 'yfinance'.

Merge правило: yfinance НЕ overwrite-ва съществуващи rows. Ако вече има row за
(date, symbol) — от git или предишен yfinance run — пропускаме. Това гарантира,
че git rich data винаги печели за overlap dates.
"""
from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
import pyarrow.parquet as pq

from ..config import EtfUniverseConfig, load_etf_universe
from ..logging_setup import get_logger
from ..paths import parquet_partition_path
from ..storage import parquet_writer
from ..utils.dates import utc_now
from ..utils.market_calendar import drop_non_trading_days

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
    # RAW-close convention (mandate #32-B, 2026-07-14). The etf_prices ``price`` column is the
    # RAW close (split-adjusted, NOT dividend-adjusted) for EVERY source, so weekly %-change /
    # CHECK-Z compare like with like. Previously this used ``adj_close`` when present, mixing a
    # dividend-adjusted level into a series that is raw close elsewhere (biasing ex-dividend
    # weeks). ``fetch_history`` pulls with ``auto_adjust=False``, so ``close`` IS the raw close;
    # ``adj_close`` is deliberately ignored (its dividend-adjustment is the contamination).
    price = row.get("close")
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


def _existing_keys_for_symbol(symbol: str) -> set:
    """Връща set от съществуващи (date) keys за даден symbol в etf_prices."""
    import glob as g
    from ..paths import parquet_glob
    out: set = set()
    for f in g.glob(parquet_glob("etf_prices"), recursive=True):
        try:
            t = pq.read_table(f, columns=["date", "symbol"]).to_pandas()
            out |= set(t.loc[t["symbol"] == symbol, "date"].tolist())
        except Exception:
            pass
    return out


def run_yf_backfill(cfg: EtfUniverseConfig | None = None,
                    period: str | None = None) -> YfBackfillResult:
    """Backfill за всички symbols от etf_universe.yaml.

    period: override на прозореца (напр. '1mo' за дневния CI run). None → cfg.period
    (5y bootstrap). Skip-existing работи и в двата случая: четем кои dates вече имат
    row и НЕ ги препокриваме, така че кратък дневен прозорец пише само новите барове.
    """
    cfg = cfg or load_etf_universe()
    window = period or cfg.period
    result = YfBackfillResult(symbols_requested=len(cfg.symbols))

    for sym in cfg.symbols:
        try:
            h = fetch_history(sym, period=window, interval=cfg.interval)
            if h.empty:
                log.warning("yfinance: empty history", extra={"symbol": sym})
                continue
            existing = _existing_keys_for_symbol(sym)
            if existing:
                h = h[~h["date"].isin(existing)]
            if h.empty:
                log.info("yfinance: all dates already present, skipping",
                         extra={"symbol": sym})
                continue
            rows = [_yf_row_to_etf_schema(sym, r) for _, r in h.iterrows()]
            df = pd.DataFrame(rows)
            # Phantom-bar guard (mandate #32-B): never write a bar dated on a non-trading day.
            # yfinance ``history`` returns only real sessions, so this normally drops nothing —
            # defence-in-depth so no upstream can reintroduce holiday phantom bars into etf_prices.
            df, dropped = drop_non_trading_days(df, date_col="date")
            if dropped:
                log.warning("yfinance: dropped non-trading-day bars",
                            extra={"symbol": sym, "dates": [str(x) for x in dropped]})
            if df.empty:
                continue
            n = parquet_writer.upsert("etf_prices", df, key_cols=["symbol"])
            result.symbols_with_data += 1
            result.rows_written += n
            log.info("yfinance backfill ok",
                     extra={"symbol": sym, "rows": n, "skipped_existing": len(existing)})
        except Exception as e:
            result.errors.append(f"{sym}: {e}")
            log.error("yfinance backfill failed", extra={"symbol": sym, "error": str(e)})

    return result
