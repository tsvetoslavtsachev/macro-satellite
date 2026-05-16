"""Single source-of-truth за pyarrow schemas.

Колоните в parser-ите трябва да съответстват. Парсерите винаги извеждат
DataFrame с ВСИЧКИ колони (липсващите → None). pyarrow ги cast-ва nullable.
"""
from __future__ import annotations

import pyarrow as pa

ETF_PRICES_SCHEMA = pa.schema([
    ("date", pa.date32()),
    ("symbol", pa.string()),
    ("name", pa.string()),
    ("category", pa.string()),
    ("region", pa.string()),
    ("price", pa.float64()),
    ("volume", pa.int64()),
    ("return_1m", pa.float64()),
    ("return_3m", pa.float64()),
    ("return_6m", pa.float64()),
    ("return_12m", pa.float64()),
    ("return_ytd", pa.float64()),
    ("volatility", pa.float64()),
    ("sharpe", pa.float64()),
    ("max_drawdown", pa.float64()),
    ("high_52w", pa.float64()),
    ("low_52w", pa.float64()),
    ("pct_from_high", pa.float64()),
    ("rs_score", pa.float64()),
    ("aum", pa.float64()),
    ("flow_1m", pa.float64()),
    ("flow_3m", pa.float64()),
    ("flow_6m", pa.float64()),
    ("flow_ytd", pa.float64()),
    # Optional yfinance OHLCV fields
    ("open_yf", pa.float64()),
    ("high_yf", pa.float64()),
    ("low_yf", pa.float64()),
    ("close_yf", pa.float64()),
    ("source", pa.string()),
    ("ingested_at", pa.timestamp("us", tz="UTC")),
])

ROTATION_SCHEMA = pa.schema([
    ("date", pa.date32()),
    ("ticker", pa.string()),
    ("name", pa.string()),
    ("sector", pa.string()),
    ("sub_industry", pa.string()),
    ("current_rank", pa.float64()),
    ("abs_strength", pa.float64()),
    ("mom_12_1_pct", pa.float64()),
    ("base_rank_6m", pa.float64()),
    ("delta_1m", pa.float64()),
    ("delta_3m", pa.float64()),
    ("quadrant_1m", pa.string()),
    ("quadrant_3m", pa.string()),
    ("source", pa.string()),
    ("ingested_at", pa.timestamp("us", tz="UTC")),
])

COT_POSITIONING_SCHEMA = pa.schema([
    ("date", pa.date32()),
    ("market", pa.string()),
    ("asset_class", pa.string()),
    ("report_date", pa.date32()),
    ("net_position", pa.int64()),
    ("net_position_pct", pa.float64()),
    ("percentile_3y", pa.float64()),
    ("percentile_5y", pa.float64()),
    ("weekly_change", pa.int64()),
    ("on_watchlist", pa.bool_()),
    ("source", pa.string()),
    ("ingested_at", pa.timestamp("us", tz="UTC")),
])

VRM_STATE_SCHEMA = pa.schema([
    ("date", pa.date32()),
    ("regime", pa.string()),
    ("ks_status", pa.string()),
    ("alignment_score", pa.float64()),
    ("alignment_total", pa.int32()),
    ("gms_value", pa.float64()),
    ("last_updated_md", pa.date32()),
    ("is_change_day", pa.bool_()),
    ("source", pa.string()),
    ("source_path", pa.string()),
    ("ingested_at", pa.timestamp("us", tz="UTC")),
])

SCHEMA_REGISTRY: dict[str, pa.Schema] = {
    "etf_prices": ETF_PRICES_SCHEMA,
    "rotation_us": ROTATION_SCHEMA,
    "rotation_eu": ROTATION_SCHEMA,
    "cot_positioning": COT_POSITIONING_SCHEMA,
    "vrm_state": VRM_STATE_SCHEMA,
}


def get_schema(table: str) -> pa.Schema:
    if table not in SCHEMA_REGISTRY:
        raise KeyError(f"Unknown table: {table}")
    return SCHEMA_REGISTRY[table]


def schema_columns(table: str) -> list[str]:
    return [f.name for f in get_schema(table)]
