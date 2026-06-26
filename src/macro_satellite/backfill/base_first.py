# -*- coding: utf-8 -*-
"""Base-first canonical ETF price ingest (INIT-22 P6 part 2 -- macro-satellite cut-over).

The strangler READ side for the satellite. Instead of pulling yfinance for the whole ETF universe
and keeping it in the satellite's OWN etf_prices store, the daily price refresh now reads the
canonical daily bars FROM the price-archive (P2) through the ONE shared reader
``collectors/price/consumer.py`` (P6) -- no per-repo reader copy. The OLD yfinance backfill
(``run_yf_backfill``) stays intact as the CLOSED fallback: the 5 satellite-only symbols outside the
archive universe (DFEN/EFA/VEA/IBIT/ASHR) and any transient base miss route through it, so
production never stops; with NO archive checkout the WHOLE universe degrades to the old fetch.

BASIS = ``value_tr`` (Tsvetoslav, 2026-06-26). The etf_prices ``price`` column today is yfinance
Adj Close (``yfinance_backfill._yf_row_to_etf_schema`` line 63), which is bar-for-bar ``value_tr``.
``price_delta`` is a ratio ``(price_B/price_A) - 1``, so reading ``value_tr`` reproduces every delta
exactly. SKIP-EXISTING is preserved (mirrors ``run_yf_backfill``): only dates ABSENT from the store
are written, so historical bars stay frozen at their first-write Adj Close (no RIV-2 re-adjustment
drift is introduced) and only the new tip comes from canon -- the production delta (last two
snapshots, days apart) is identical to today's yfinance pull.

PROVENANCE: ``data/price_source.json`` ({by_symbol: base|fetch, summary}) feeds
``scripts/assert_base_sourced.py`` -- RED if any archive-covered symbol silently fell back to
yfinance while base sourcing was intended (the read PAT is set in CI). Mirror of A1 cot_source /
P6 ETF-rr. INIT-22 P6 part 2 strangler discipline.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field

import pandas as pd

from ..config import EtfUniverseConfig, load_etf_universe
from ..logging_setup import get_logger
from ..storage import parquet_writer
from ..utils.dates import utc_now
from .yfinance_backfill import _existing_keys_for_symbol, run_yf_backfill

log = get_logger(__name__)


@dataclass
class BaseFirstResult:
    symbols_requested: int = 0
    base_symbols: int = 0
    fetch_symbols: int = 0
    rows_written_base: int = 0
    rows_written_fetch: int = 0
    errors: list[str] = field(default_factory=list)


def _import_consumer():
    """Import the ONE canonical reader (collectors/price/consumer.py).

    Isolated so the ImportError degrade-path (no collectors/data-core checkout -> the whole
    universe falls back to yfinance, production never stops) is handled in ONE place and the
    base read is monkeypatchable in tests without a live archive."""
    from collectors.price import consumer
    return consumer


def _price_source_path():
    """data/price_source.json under the (possibly test-overridden) repo root. Resolved lazily so
    the conftest ``isolated_storage`` MACRO_SATELLITE_ROOT override is honoured."""
    from .. import paths
    return paths.REPO_ROOT / "data" / "price_source.json"


def _base_row(symbol: str, d, price, volume) -> dict:
    """One base-sourced etf_prices row. ``price`` = value_tr (== today's Adj Close). The raw OHLC
    columns (``*_yf``) are left NULL: the archive carries split-adjusted OHLC, not the raw bars the
    old yfinance path stored there, and NOTHING downstream reads ``*_yf`` -- only ``price``/``volume``
    (verified: grep over src). ``source`` marks the canonical provenance for price_source.json."""
    return {
        "date": d, "symbol": symbol, "name": None, "category": None, "region": None,
        "price": float(price) if pd.notna(price) else None,
        "volume": int(volume) if pd.notna(volume) else None,
        "return_1m": None, "return_3m": None, "return_6m": None,
        "return_12m": None, "return_ytd": None,
        "volatility": None, "sharpe": None, "max_drawdown": None,
        "high_52w": None, "low_52w": None, "pct_from_high": None,
        "rs_score": None, "aum": None,
        "flow_1m": None, "flow_3m": None, "flow_6m": None, "flow_ytd": None,
        "open_yf": None, "high_yf": None, "low_yf": None, "close_yf": None,
        "source": "data-core",
        "ingested_at": utc_now(),
    }


def run_price_ingest_base_first(period: str | None = None, root=None,
                                cfg: EtfUniverseConfig | None = None) -> BaseFirstResult:
    """Read the ETF universe base-first from the canonical archive; yfinance CLOSED fallback.

    period: read window (the daily CI passes '1mo'; None -> cfg.period, the 5y bootstrap).
    root:   archive root override; None -> the consumer resolves DATACORE_ROOT (-> price-archive).
    """
    cfg = cfg or load_etf_universe()
    window = period or cfg.period
    symbols = list(cfg.symbols)
    result = BaseFirstResult(symbols_requested=len(symbols))

    source_map: dict[str, str] = {}
    base_served: list[str] = []

    try:
        consumer = _import_consumer()
    except ImportError:
        consumer = None
        log.warning("base reader unavailable (collectors/data-core not importable) -- whole "
                    "universe falls back to yfinance (strangler degrade)")

    if consumer is not None:
        try:
            ohlcv, smap = consumer.read_base_ohlcv(symbols, root=root, period=window)
            close_df = ohlcv.get("Close", pd.DataFrame())
            vol_df = ohlcv.get("Volume", pd.DataFrame())
            base_served = [s for s in symbols if smap.get(s) == consumer.SRC_BASE]
            for s in base_served:
                col = close_df[s].dropna() if s in close_df.columns else pd.Series(dtype="float64")
                vcol = vol_df[s] if (not vol_df.empty and s in vol_df.columns) else None
                existing = _existing_keys_for_symbol(s)
                rows = []
                for ts, price in col.items():
                    d = ts.date()
                    if d in existing:            # SKIP-EXISTING: never re-touch a frozen bar
                        continue
                    vol = vcol.get(ts) if vcol is not None else None
                    rows.append(_base_row(s, d, price, vol))
                if rows:
                    result.rows_written_base += parquet_writer.upsert(
                        "etf_prices", pd.DataFrame(rows), key_cols=["symbol"])
                source_map[s] = "base"
            result.base_symbols = len(base_served)
        except Exception as e:  # base read failed -> fall back for EVERYTHING, never crash
            result.errors.append(f"base read: {e}")
            base_served = []
            source_map = {}
            log.error("base read failed -- whole universe falls back to yfinance",
                      extra={"error": str(e)})

    # CLOSED fallback: every symbol not base-served -> the UNCHANGED yfinance backfill.
    served = set(base_served)
    missing = [s for s in symbols if s not in served]
    if missing:
        fb_cfg = EtfUniverseConfig(period=cfg.period, interval=cfg.interval, symbols=missing)
        yf = run_yf_backfill(cfg=fb_cfg, period=window)
        result.rows_written_fetch = yf.rows_written
        result.errors.extend(yf.errors)
        for s in missing:
            source_map[s] = "fetch"
    result.fetch_symbols = len(missing)

    _write_price_source(source_map, expected=len(symbols))
    log.info("base-first ingest done", extra={
        "base": result.base_symbols, "fetch": result.fetch_symbols,
        "rows_base": result.rows_written_base, "rows_fetch": result.rows_written_fetch,
        "errors": len(result.errors)})
    return result


def _write_price_source(source_map: dict[str, str], expected: int) -> None:
    n_base = sum(1 for v in source_map.values() if v == "base")
    payload = {
        "by_symbol": dict(sorted(source_map.items())),
        "summary": {"expected": expected, "covered": len(source_map),
                    "base": n_base, "fetch": len(source_map) - n_base},
        "generated_at": utc_now().isoformat(),
    }
    path = _price_source_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
