"""Storage upsert е idempotent: двукратен collect → същият resultat."""
from __future__ import annotations

from datetime import date

import pandas as pd

from macro_satellite.storage import parquet_writer

from _etf_fixture import parse_etf_fixture


def _read_count(table: str) -> int:
    df = parquet_writer.read_table(table)
    return len(df)


def test_idempotent_upsert_same_data(isolated_storage, fixtures_dir):
    raw = (fixtures_dir / "etfs_mini_2026-05-15.json").read_bytes()
    df = parse_etf_fixture(raw)
    n1 = parquet_writer.upsert("etf_prices", df, key_cols=["symbol"])
    n2 = parquet_writer.upsert("etf_prices", df, key_cols=["symbol"])
    assert n1 == n2 == len(df)
    assert _read_count("etf_prices") == len(df)


def test_upsert_overwrites_changed_row(isolated_storage, fixtures_dir):
    raw = (fixtures_dir / "etfs_mini_2026-05-15.json").read_bytes()
    df1 = parse_etf_fixture(raw)
    parquet_writer.upsert("etf_prices", df1, key_cols=["symbol"])

    df2 = df1.copy()
    df2.loc[df2["symbol"] == "USO", "price"] = 999.99
    parquet_writer.upsert("etf_prices", df2, key_cols=["symbol"])

    out = parquet_writer.read_table("etf_prices")
    uso = out[out["symbol"] == "USO"].iloc[0]
    assert uso["price"] == 999.99
    # NO duplicate rows for USO
    assert len(out[out["symbol"] == "USO"]) == 1


def test_upsert_different_dates_coexist(isolated_storage, fixtures_dir):
    raw = (fixtures_dir / "etfs_mini_2026-05-15.json").read_bytes()
    df1 = parse_etf_fixture(raw, snapshot_date=date(2026, 5, 7))
    df2 = parse_etf_fixture(raw, snapshot_date=date(2026, 5, 15))
    parquet_writer.upsert("etf_prices", df1, key_cols=["symbol"])
    parquet_writer.upsert("etf_prices", df2, key_cols=["symbol"])

    out = parquet_writer.read_table("etf_prices")
    # 5 ETFs × 2 dates = 10 rows
    assert len(out) == 10
    assert set(out["date"].tolist()) == {date(2026, 5, 7), date(2026, 5, 15)}
