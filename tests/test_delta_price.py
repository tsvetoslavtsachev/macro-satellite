"""price_delta: задължително (price_B / price_A) - 1, никога разлика на returns."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from macro_satellite.collectors import etf_dashboard
from macro_satellite.delta.price_delta import MissingDataError, interval_change
from macro_satellite.storage import parquet_writer
from macro_satellite.storage.duckdb_conn import get_duck


def _seed_two_dates(fixtures_dir):
    raw = (fixtures_dir / "etfs_mini_2026-05-15.json").read_bytes()
    df1 = etf_dashboard.parse(raw, snapshot_date=date(2026, 5, 7))
    # mutate USO price for date_a → 134.97 (real 7 May)
    df1.loc[df1["symbol"] == "USO", "price"] = 134.97
    df2 = etf_dashboard.parse(raw, snapshot_date=date(2026, 5, 15))
    parquet_writer.upsert("etf_prices", df1, key_cols=["symbol"])
    parquet_writer.upsert("etf_prices", df2, key_cols=["symbol"])


def test_interval_change_uses_real_prices(isolated_storage, fixtures_dir):
    _seed_two_dates(fixtures_dir)
    duck = get_duck()
    r = interval_change("USO", date(2026, 5, 7), date(2026, 5, 15), duck)
    assert r.price_a == pytest.approx(134.97)
    assert r.price_b == pytest.approx(148.23, rel=1e-3)
    expected = (148.23 / 134.97) - 1
    assert r.interval_change == pytest.approx(expected, rel=1e-3)


def test_interval_change_missing_date_raises(isolated_storage, fixtures_dir):
    _seed_two_dates(fixtures_dir)
    duck = get_duck()
    with pytest.raises(MissingDataError):
        interval_change("USO", date(2020, 1, 1), date(2020, 1, 2), duck)


def test_interval_change_unknown_symbol_raises(isolated_storage, fixtures_dir):
    _seed_two_dates(fixtures_dir)
    duck = get_duck()
    with pytest.raises(MissingDataError):
        interval_change("ZZZZ", date(2026, 5, 7), date(2026, 5, 15), duck)
