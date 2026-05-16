"""Idempotent upsert на Parquet таблици.

Партициониране: year=/month=. За upsert на (date, ...key_cols):
1. Маршрутираме по month на date.
2. Чете month-файла (ако съществува).
3. Изтриваме старите редове за същите (date, ...key_cols) tuples.
4. Append на новите.
5. Презаписваме month-файла.
"""
from __future__ import annotations

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from ..paths import parquet_partition_path
from .schema import get_schema


def _conform(df: pd.DataFrame, schema: pa.Schema) -> pd.DataFrame:
    """Гарантира, че df има всички колони от schema-та, с правилни типове."""
    out = df.copy()
    for field in schema:
        if field.name not in out.columns:
            out[field.name] = None
    # Каст за date columns — поддържаме date32; pandas го дава като object с date
    return out[[f.name for f in schema]]


def upsert(table: str, df: pd.DataFrame, key_cols: list[str]) -> int:
    """Upsert редовете в df в правилните month-партиции.

    Връща: брой реални нови/обновени редове.
    """
    if df.empty:
        return 0

    schema = get_schema(table)
    conformed = _conform(df, schema)

    # Group by (year, month) of date
    conformed = conformed.copy()
    date_series = pd.to_datetime(conformed["date"])
    conformed["_year"] = date_series.dt.year.astype(int)
    conformed["_month"] = date_series.dt.month.astype(int)

    written = 0
    full_keys = ["date"] + list(key_cols)

    for (year, month), grp in conformed.groupby(["_year", "_month"]):
        path = parquet_partition_path(table, int(year), int(month))
        path.parent.mkdir(parents=True, exist_ok=True)

        grp_clean = grp.drop(columns=["_year", "_month"])

        if path.exists():
            existing = pq.read_table(path, schema=schema).to_pandas()
            # Build delete mask: rows in existing whose full_keys are in grp
            grp_keys = grp_clean[full_keys].drop_duplicates()
            merged = existing.merge(grp_keys, on=full_keys, how="left", indicator=True)
            remaining = existing[merged["_merge"].values == "left_only"]
            combined = pd.concat([remaining, grp_clean], ignore_index=True)
        else:
            combined = grp_clean

        # Sort for deterministic file content
        combined = combined.sort_values(by=full_keys).reset_index(drop=True)

        # Convert to pyarrow table with strict schema
        tbl = pa.Table.from_pandas(combined, schema=schema, preserve_index=False)
        pq.write_table(tbl, path, compression="zstd")
        written += len(grp_clean)

    return written


def read_table(table: str) -> pd.DataFrame:
    """Read всички партиции на дадена таблица. За малки таблици / тестове."""
    import glob as g
    from ..paths import parquet_glob
    files = sorted(g.glob(parquet_glob(table), recursive=True))
    if not files:
        return pd.DataFrame()
    parts = [pq.read_table(f, schema=get_schema(table)).to_pandas() for f in files]
    return pd.concat(parts, ignore_index=True)
