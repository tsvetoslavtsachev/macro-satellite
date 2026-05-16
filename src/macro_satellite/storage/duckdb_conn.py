"""DuckDB connection helper. Чете директно върху Parquet glob-ове.

Ако таблица няма още partition-и → създава празен view със schema-та, така че
queries не падат. Толерира bootstrap state, където само 1-2 collectors са успели.
"""
from __future__ import annotations

import glob as _glob

import duckdb
import pyarrow as pa

from ..paths import parquet_glob, parquet_table_dir


def _table_has_files(table: str) -> bool:
    return bool(_glob.glob(parquet_glob(table), recursive=True))


def _empty_view_sql(table: str) -> str:
    """Build SELECT с правилните колони и типове, но 0 rows. За празни tables."""
    from .schema import get_schema
    sch = get_schema(table)
    # CAST(NULL AS <type>) per колона; WHERE FALSE → 0 rows
    cols = []
    for f in sch:
        sql_type = _arrow_to_sql(f.type)
        cols.append(f"CAST(NULL AS {sql_type}) AS {f.name}")
    return f"SELECT {', '.join(cols)} WHERE FALSE"


def _arrow_to_sql(t: pa.DataType) -> str:
    if pa.types.is_date32(t) or pa.types.is_date64(t):
        return "DATE"
    if pa.types.is_timestamp(t):
        return "TIMESTAMP WITH TIME ZONE"
    if pa.types.is_string(t):
        return "VARCHAR"
    if pa.types.is_boolean(t):
        return "BOOLEAN"
    if pa.types.is_int32(t):
        return "INTEGER"
    if pa.types.is_int64(t):
        return "BIGINT"
    if pa.types.is_floating(t):
        return "DOUBLE"
    return "VARCHAR"


def get_duck() -> duckdb.DuckDBPyConnection:
    """In-memory DuckDB. Регистрира views за всяка известна таблица."""
    from .schema import SCHEMA_REGISTRY
    con = duckdb.connect(":memory:")
    for table in SCHEMA_REGISTRY:
        if _table_has_files(table):
            glob = parquet_glob(table).replace("\\", "/")
            con.execute(
                f"CREATE OR REPLACE VIEW {table} AS "
                f"SELECT * FROM read_parquet('{glob}', union_by_name=true)"
            )
        else:
            con.execute(f"CREATE OR REPLACE VIEW {table} AS {_empty_view_sql(table)}")
    # Suppress unused-import warning at runtime
    _ = parquet_table_dir
    return con
