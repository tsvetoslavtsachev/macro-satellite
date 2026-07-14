# -*- coding: utf-8 -*-
"""INIT-22 P6 part 2 -- base-first ETF price ingest (macro-satellite cut-over).

Hermetic unit tests inject a FAKE consumer (no live archive / no network) to prove:
  * base-served symbols write source="data-core" rows with price == value_tr;
  * SKIP-EXISTING freezes already-stored bars (no RIV-2 re-adjustment drift);
  * symbols not served by the archive route through the UNCHANGED yfinance fallback;
  * an unreachable archive degrades the WHOLE universe to the fallback (strangler);
  * data/price_source.json provenance matches (feeds assert_base_sourced.py).
A final live test reads SPY from a real local price-archive if one is wired (else skips).
"""
from __future__ import annotations

import importlib
import json
from datetime import date

import pandas as pd
import pytest

from macro_satellite.backfill import base_first as _bf
from macro_satellite.backfill.yfinance_backfill import YfBackfillResult
from macro_satellite.config import EtfUniverseConfig
from macro_satellite.storage import parquet_writer


class _FakeConsumer:
    """Stand-in for collectors.price.consumer with a canned base read."""
    SRC_BASE = "base"
    SRC_UNMAPPED = "unmapped"

    def __init__(self, close_map, vol_map=None, unmapped=()):
        self.close_map = close_map          # {sym: {iso_date: value_tr}}
        self.vol_map = vol_map or {}        # {sym: {iso_date: volume}}
        self.unmapped = set(unmapped)

    def read_base_ohlcv(self, tickers, *, root=None, period="2y", start=None, end=None,
                        as_of_vintage=None):
        cols_close, cols_vol, source_map = {}, {}, {}
        for t in tickers:
            if t in self.close_map:
                s = pd.Series(self.close_map[t]); s.index = pd.to_datetime(s.index)
                cols_close[t] = s
                v = self.vol_map.get(t, {})
                if v:
                    vs = pd.Series(v); vs.index = pd.to_datetime(vs.index)
                else:
                    vs = pd.Series(dtype="float64")
                cols_vol[t] = vs
                source_map[t] = self.SRC_BASE
            elif t in self.unmapped:
                source_map[t] = self.SRC_UNMAPPED
            # else: mapped-but-empty -> omitted (a fallback candidate), mirrors the real reader
        ohlcv = {
            "Open": pd.DataFrame(), "High": pd.DataFrame(), "Low": pd.DataFrame(),
            "Close": pd.DataFrame(cols_close).sort_index() if cols_close else pd.DataFrame(),
            "Volume": pd.DataFrame(cols_vol).sort_index() if cols_vol else pd.DataFrame(),
        }
        return ohlcv, source_map


def _reload():
    """Rebind base_first onto the isolated-storage reloaded parquet_writer/paths."""
    importlib.reload(_bf)
    return _bf


def _read_price_source(tmp_root):
    return json.loads((tmp_root / "data" / "price_source.json").read_text(encoding="utf-8"))


def test_base_served_writes_value_tr_and_skips_existing(isolated_storage, monkeypatch):
    bf = _reload()
    # Seed an EXISTING bar for SPY at the old date with a sentinel price.
    seeded = pd.DataFrame([{
        "date": date(2026, 6, 1), "symbol": "SPY", "price": 111.0, "source": "yfinance",
    }])
    parquet_writer.upsert("etf_prices", seeded, key_cols=["symbol"])

    fake = _FakeConsumer(
        close_map={"SPY": {"2026-06-01": 999.0, "2026-06-02": 123.45},   # old (skipped) + new
                   "TLT": {"2026-06-02": 88.20}},
        vol_map={"SPY": {"2026-06-02": 1000}, "TLT": {"2026-06-02": 2000}},
    )
    monkeypatch.setattr(bf, "_import_consumer", lambda: fake)

    cfg = EtfUniverseConfig(period="1mo", interval="1d", symbols=["SPY", "TLT"])
    res = bf.run_price_ingest_base_first(period="1mo", cfg=cfg)

    assert res.base_symbols == 2 and res.fetch_symbols == 0
    df = parquet_writer.read_table("etf_prices")
    spy_old = df[(df.symbol == "SPY") & (df.date == date(2026, 6, 1))].iloc[0]
    spy_new = df[(df.symbol == "SPY") & (df.date == date(2026, 6, 2))].iloc[0]
    assert spy_old["price"] == pytest.approx(111.0)          # SKIP-EXISTING: frozen, not 999.0
    assert spy_old["source"] == "yfinance"
    assert spy_new["price"] == pytest.approx(123.45)         # base value_tr written
    assert spy_new["source"] == "data-core"
    assert int(spy_new["volume"]) == 1000
    src = _read_price_source(isolated_storage)
    assert src["by_symbol"] == {"SPY": "base", "TLT": "base"}
    assert src["summary"] == {"expected": 2, "covered": 2, "base": 2, "fetch": 0}


def test_unmapped_symbol_routes_to_fetch(isolated_storage, monkeypatch):
    bf = _reload()
    fake = _FakeConsumer(close_map={"SPY": {"2026-06-02": 123.45}}, unmapped={"IBIT"})
    monkeypatch.setattr(bf, "_import_consumer", lambda: fake)

    called = {}

    def _stub_yf(cfg=None, period=None):
        called["symbols"] = list(cfg.symbols)
        return YfBackfillResult(symbols_requested=len(cfg.symbols),
                                symbols_with_data=len(cfg.symbols), rows_written=1)
    monkeypatch.setattr(bf, "run_yf_backfill", _stub_yf)

    cfg = EtfUniverseConfig(period="1mo", interval="1d", symbols=["SPY", "IBIT"])
    res = bf.run_price_ingest_base_first(period="1mo", cfg=cfg)

    assert called["symbols"] == ["IBIT"]                 # only the gap goes to the fallback
    assert res.base_symbols == 1 and res.fetch_symbols == 1
    src = _read_price_source(isolated_storage)
    assert src["by_symbol"] == {"IBIT": "fetch", "SPY": "base"}


def test_degrade_whole_universe_when_base_unimportable(isolated_storage, monkeypatch):
    bf = _reload()

    def _raise():
        raise ImportError("no collectors checkout")
    monkeypatch.setattr(bf, "_import_consumer", _raise)

    seen = {}

    def _stub_yf(cfg=None, period=None):
        seen["symbols"] = list(cfg.symbols)
        return YfBackfillResult(symbols_requested=len(cfg.symbols), rows_written=3)
    monkeypatch.setattr(bf, "run_yf_backfill", _stub_yf)

    cfg = EtfUniverseConfig(period="1mo", interval="1d", symbols=["SPY", "TLT", "IBIT"])
    res = bf.run_price_ingest_base_first(period="1mo", cfg=cfg)

    assert seen["symbols"] == ["SPY", "TLT", "IBIT"]     # production never stops
    assert res.base_symbols == 0 and res.fetch_symbols == 3
    src = _read_price_source(isolated_storage)
    assert set(src["by_symbol"].values()) == {"fetch"}
    assert src["summary"]["base"] == 0


def test_base_read_exception_falls_back_for_everything(isolated_storage, monkeypatch):
    bf = _reload()

    class _Boom:
        SRC_BASE = "base"
        def read_base_ohlcv(self, *a, **k):
            raise RuntimeError("archive corrupt")
    monkeypatch.setattr(bf, "_import_consumer", lambda: _Boom())
    monkeypatch.setattr(bf, "run_yf_backfill",
                        lambda cfg=None, period=None: YfBackfillResult(rows_written=2))

    cfg = EtfUniverseConfig(period="1mo", interval="1d", symbols=["SPY", "TLT"])
    res = bf.run_price_ingest_base_first(period="1mo", cfg=cfg)

    assert res.base_symbols == 0 and res.fetch_symbols == 2
    assert any("base read" in e for e in res.errors)


def test_live_archive_reads_spy_from_canon(isolated_storage, monkeypatch):
    """Live smoke: read SPY from a real local price-archive if DATACORE_ROOT wires one.

    Skips cleanly when collectors/data-core are not importable or no archive root is set --
    exactly the strangler degrade path the other tests cover hermetically."""
    bf = _reload()
    try:
        consumer = bf._import_consumer()
    except ImportError:
        pytest.skip("collectors.price.consumer not importable (no archive wiring)")
    import os
    if not (os.environ.get("DATACORE_ROOT") or os.environ.get("PRICE_ARCHIVE_ROOT")):
        pytest.skip("no DATACORE_ROOT -> archive not wired for a live read")
    root = os.environ.get("DATACORE_ROOT") or os.environ.get("PRICE_ARCHIVE_ROOT")

    cfg = EtfUniverseConfig(period="6mo", interval="1d", symbols=["SPY"])
    res = bf.run_price_ingest_base_first(period="6mo", root=root, cfg=cfg)
    if res.base_symbols == 0:
        pytest.skip("SPY not present in the wired archive root")
    df = parquet_writer.read_table("etf_prices")
    spy = df[df.symbol == "SPY"]
    assert not spy.empty
    assert (spy["price"] > 0).all()
    assert (spy["source"] == "data-core").all()


class _ConsumerWithArchive(_FakeConsumer):
    """FakeConsumer that also exposes the public helpers _raw_close_map needs."""
    def __init__(self, close_map, series_map, vol_map=None, unmapped=()):
        super().__init__(close_map, vol_map=vol_map, unmapped=unmapped)
        self._series_map = series_map

    def resolve_root(self, root=None):
        return root or "FAKE_ROOT"

    def symbol_to_series(self):
        return dict(self._series_map)


def test_base_price_uses_raw_close_not_total_return(isolated_storage, monkeypatch):
    """Mandate #32-B: the stored data-core price is the archive's RAW ``close``, NOT the
    total-return Close read_base_ohlcv returns (which folds in a dividend adjustment).

    Models the measured LQD case: read_base_ohlcv Close = 109.116 (total-return / value_tr on a
    pre-ex-dividend bar), while the archive's raw close = 109.50. The row must store 109.50."""
    bf = _reload()
    fake = _ConsumerWithArchive(
        close_map={"LQD": {"2026-06-26": 109.116494}},         # total-return (value_tr)
        series_map={"LQD": "px_lqd_daily"},
        vol_map={"LQD": {"2026-06-26": 500}},
    )
    monkeypatch.setattr(bf, "_import_consumer", lambda: fake)

    class _Archive:
        def read(self, sid, root=None, as_of_vintage=None):
            assert sid == "px_lqd_daily" and root == "FAKE_ROOT"
            return [{"as_of": "2026-06-26", "close": 109.50, "value_tr": 109.116494}]  # RAW close
    monkeypatch.setattr(bf, "_import_archive", lambda: _Archive())

    cfg = EtfUniverseConfig(period="1mo", interval="1d", symbols=["LQD"])
    res = bf.run_price_ingest_base_first(period="1mo", cfg=cfg)

    assert res.base_symbols == 1
    df = parquet_writer.read_table("etf_prices")
    lqd = df[(df.symbol == "LQD") & (df.date == date(2026, 6, 26))].iloc[0]
    assert lqd["price"] == pytest.approx(109.50)          # RAW close (not 109.116 total-return)
    assert lqd["source"] == "data-core"


def test_base_price_degrades_to_total_return_when_archive_absent(isolated_storage, monkeypatch):
    """Safe degrade: if the raw archive read is unavailable, the row keeps the consumer's
    (total-return) value -- production never stops (only the convention is temporarily off)."""
    bf = _reload()
    fake = _FakeConsumer(close_map={"SPY": {"2026-06-26": 123.45}},
                         vol_map={"SPY": {"2026-06-26": 10}})
    monkeypatch.setattr(bf, "_import_consumer", lambda: fake)

    def _no_archive():
        raise ImportError("no datacore checkout")
    monkeypatch.setattr(bf, "_import_archive", _no_archive)

    cfg = EtfUniverseConfig(period="1mo", interval="1d", symbols=["SPY"])
    bf.run_price_ingest_base_first(period="1mo", cfg=cfg)
    df = parquet_writer.read_table("etf_prices")
    spy = df[(df.symbol == "SPY") & (df.date == date(2026, 6, 26))].iloc[0]
    assert spy["price"] == pytest.approx(123.45)          # degraded to the consumer value
    assert spy["source"] == "data-core"


def test_base_drops_juneteenth_phantom_bar(isolated_storage, monkeypatch):
    """Mandate #32-B phantom-bar guard end-to-end: a base read that includes a Juneteenth
    (2026-06-19) bar must NOT write a 06-19 row; the real sessions around it are written."""
    bf = _reload()
    fake = _FakeConsumer(
        close_map={"SPY": {"2026-06-18": 746.0, "2026-06-19": 746.74, "2026-06-22": 747.0}},
        vol_map={"SPY": {"2026-06-18": 1, "2026-06-19": 1, "2026-06-22": 1}},
    )
    monkeypatch.setattr(bf, "_import_consumer", lambda: fake)

    def _no_archive():
        raise ImportError("no datacore checkout")
    monkeypatch.setattr(bf, "_import_archive", _no_archive)

    cfg = EtfUniverseConfig(period="1mo", interval="1d", symbols=["SPY"])
    bf.run_price_ingest_base_first(period="1mo", cfg=cfg)

    df = parquet_writer.read_table("etf_prices")
    spy_dates = set(df[df.symbol == "SPY"]["date"])
    assert date(2026, 6, 19) not in spy_dates             # Juneteenth phantom dropped
    assert {date(2026, 6, 18), date(2026, 6, 22)} <= spy_dates


def test_cmd_backfill_base_exit_code_policy(monkeypatch):
    """Strangler at the CLI: a partial fallback miss must NOT exit 1 (would take the satellite dark);
    only a true dead channel (nothing ingested + errors) fails loud. Mirrors cmd_collect."""
    import argparse
    from macro_satellite import cli
    from macro_satellite.backfill import base_first as bfmod
    from macro_satellite.backfill.base_first import BaseFirstResult

    args = argparse.Namespace(period="1mo")

    def _patch(res):
        monkeypatch.setattr(bfmod, "run_price_ingest_base_first", lambda period=None: res)

    # 42 base healthy + a transient yfinance miss on one gap -> stay alive (exit 0)
    _patch(BaseFirstResult(symbols_requested=47, base_symbols=42, fetch_symbols=5,
                           rows_written_base=924, rows_written_fetch=88, errors=["IBIT: 404"]))
    assert cli.cmd_backfill_base(args) == 0

    # dormant (PATs absent): whole universe via yfinance, rows written -> exit 0
    _patch(BaseFirstResult(symbols_requested=47, base_symbols=0, fetch_symbols=47,
                           rows_written_base=0, rows_written_fetch=900, errors=[]))
    assert cli.cmd_backfill_base(args) == 0

    # same-day re-run, nothing new but no errors -> exit 0 (not a dead channel)
    _patch(BaseFirstResult(symbols_requested=47, base_symbols=42, fetch_symbols=5,
                           rows_written_base=0, rows_written_fetch=0, errors=[]))
    assert cli.cmd_backfill_base(args) == 0

    # dead channel: base served nothing, fallback wrote nothing, errors present -> exit 1 (loud)
    _patch(BaseFirstResult(symbols_requested=47, base_symbols=0, fetch_symbols=47,
                           rows_written_base=0, rows_written_fetch=0,
                           errors=["SPY: net down", "base read: archive unreachable"]))
    assert cli.cmd_backfill_base(args) == 1
