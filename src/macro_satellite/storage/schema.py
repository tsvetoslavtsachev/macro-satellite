"""Single source-of-truth за pyarrow schemas.

Колоните в parser-ите трябва да съответстват. Парсерите винаги извеждат
DataFrame с ВСИЧКИ колони (липсващите → None). pyarrow ги cast-ва nullable.
"""
from __future__ import annotations

import pyarrow as pa

from ..config import macro_lenses

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

# COT positioning (сателитен препубликатор на cot-monitor watchlist.json).
# Вълна-1 B1 [2026-07-10]: полето `percentile_5y` е ПРЕИМЕНУВАНО → `percentile_hist`
#   + добавено `hist_weeks`. Причина: старото `percentile_5y` носеше FULL-HISTORY
#   percentile (229-1046 седм per пазар), т.е. името лъжеше за съдържанието
#   (Г7 колизия #2). `percentile_hist` е честното име; `hist_weeks` носи дължината
#   на историята (от watchlist.json `history_weeks`) — тя е несравнима между пазари.
#   DATA-SAFE (X-пакет образец): duckdb чете с union_by_name=true (duckdb_conn.py),
#   тъй че стар parquet с колона `percentile_5y` НЕ чупи прочита (сурви като null-нат
#   допълнителен стълб); в репото няма персистиран cot_positioning parquet за миграция.
#   DEPRECATION: `percentile_5y` вече не се пише. `percentile_3y` остава (винаги None =
#   „не се смята"; не лъже за съдържание) — кандидат за махане в отделна писта.
COT_POSITIONING_SCHEMA = pa.schema([
    ("date", pa.date32()),
    ("market", pa.string()),
    ("asset_class", pa.string()),
    ("report_date", pa.date32()),
    ("net_position", pa.int64()),
    ("net_position_pct", pa.float64()),
    ("percentile_3y", pa.float64()),
    ("percentile_hist", pa.float64()),   # full-history percentile (беше подвеждащо „percentile_5y")
    ("hist_weeks", pa.int32()),          # дължина на историята в седмици; несравнима между пазари
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

MOMENTUM_SCHEMA = pa.schema([
    ("date", pa.date32()),
    ("symbol", pa.string()),
    ("name", pa.string()),
    ("sector", pa.string()),
    ("country", pa.string()),          # null за SP500
    ("exchange", pa.string()),         # null за SP500
    ("currency", pa.string()),         # null за SP500
    ("price", pa.float64()),
    ("market_cap", pa.float64()),
    ("return_1m", pa.float64()),
    ("return_3m", pa.float64()),
    ("return_6m", pa.float64()),
    ("return_12m", pa.float64()),
    ("volatility", pa.float64()),
    ("avg_volume", pa.int64()),
    ("day_change", pa.float64()),
    ("sharpe", pa.float64()),
    ("drawdown", pa.float64()),
    ("high_52w", pa.float64()),
    ("low_52w", pa.float64()),
    ("drawdown_52w", pa.float64()),
    ("momentum_score", pa.float64()),
    ("weight", pa.float64()),
    ("stale", pa.bool_()),
    ("rank", pa.int32()),
    ("source", pa.string()),
    ("ingested_at", pa.timestamp("us", tz="UTC")),
])

STOCK_SELECTION_SCHEMA = pa.schema([
    ("date", pa.date32()),
    ("ticker", pa.string()),
    ("name", pa.string()),
    ("sector", pa.string()),
    ("rank", pa.int32()),
    ("composite_score", pa.float64()),
    ("trend_score", pa.float64()),
    ("quality_score", pa.float64()),
    ("value_score", pa.float64()),
    ("risk_score", pa.float64()),
    ("ret_13w", pa.float64()),
    ("ret_26w", pa.float64()),
    ("ret_52w", pa.float64()),
    ("volatility_26w", pa.float64()),
    ("pe_ratio", pa.float64()),
    ("pb_ratio", pa.float64()),
    ("ev_ebitda", pa.float64()),
    ("ev_ebit", pa.float64()),
    ("roe", pa.float64()),
    ("roic", pa.float64()),
    ("debt_equity", pa.float64()),
    ("eps_ttm", pa.float64()),
    ("dividend_yield", pa.float64()),
    ("revenue_growth_ttm", pa.float64()),
    ("oper_margin_ttm", pa.float64()),
    ("gross_margin_ttm", pa.float64()),
    ("fcf_margin", pa.float64()),
    ("source", pa.string()),
    ("ingested_at", pa.timestamp("us", tz="UTC")),
])

# Жив VRM мозък (data-core weekly overlay). Пълни се от datacore-state колектора
# (collectors/vrm_overlay.py), който чете vrm_overlay.json[-1] READ-ONLY от data-core.
# Това е публичната VRM health-лампа (S14 мери max(date) = свежестта на мозъка).
# Cardinal rule: само полета, които мозъкът реално emit-ва (regime/alignment/gms/KS).
VRM_OVERLAY_SCHEMA = pa.schema([
    ("date", pa.date32()),                  # = as_of (W-FRI) — S14 freshness anchor
    ("as_of", pa.date32()),
    ("regime", pa.string()),
    ("alignment_score", pa.float64()),
    ("gms_score", pa.float64()),
    ("gms_max", pa.int32()),
    ("gms_tier", pa.string()),
    ("ks_active", pa.bool_()),              # nullable — мозъкът emit-ва None при неизвестно
    ("source", pa.string()),
    ("ingested_at", pa.timestamp("us", tz="UTC")),
])

VRM_WEEK_SCHEMA = pa.schema([
    ("date", pa.date32()),                  # = week_start_date
    ("week_start", pa.date32()),
    ("week_end", pa.date32()),
    ("last_updated_md", pa.date32()),
    ("approved", pa.bool_()),
    ("regime", pa.string()),
    ("regime_bg", pa.string()),
    ("signal", pa.string()),
    ("alignment", pa.float64()),
    ("alignment_max", pa.int32()),
    ("alignment_label", pa.string()),
    ("gms_score", pa.float64()),
    ("gms_max", pa.int32()),
    ("gms_label", pa.string()),
    ("ks_active", pa.bool_()),
    ("ks_variant", pa.string()),
    ("ks_weeks_active", pa.float64()),
    ("ks_portfolio", pa.string()),
    ("ks_eu_portfolio", pa.string()),
    ("spy_4w", pa.float64()),
    ("qqq_4w", pa.float64()),
    ("xle_4w", pa.float64()),
    ("gld_4w", pa.float64()),
    ("tlt_4w", pa.float64()),
    ("tip_4w", pa.float64()),
    ("iwm_4w", pa.float64()),
    ("source", pa.string()),
    ("ingested_at", pa.timestamp("us", tz="UTC")),
])

def _macro_state_schema(
    lenses: tuple[str, ...] = ("labor", "growth", "inflation", "liquidity"),
) -> pa.Schema:
    """Wide row per snapshot. len(lenses) × 5 metrics + executive summary.

    `lenses` параметризира таксономията: US ползва liquidity, EU ползва credit
    (extension). China има собствена схема (CN_MACRO_STATE_SCHEMA)."""
    fields = [
        ("date", pa.date32()),
        ("region", pa.string()),
        ("generated_at", pa.timestamp("us", tz="UTC")),
        ("regime_key", pa.string()),
        ("regime_label_bg", pa.string()),
        ("narrative", pa.string()),
        ("primary_driver", pa.string()),
        ("supporting_signals_json", pa.string()),
        ("top_anomalies_count", pa.int32()),
        ("top_anomalies_json", pa.string()),
        ("cross_lens_divergences_count", pa.int32()),
        ("cross_lens_divergences_json", pa.string()),
    ]
    for lens in lenses:
        fields += [
            (f"{lens}_score", pa.float64()),
            (f"{lens}_direction", pa.string()),
            (f"{lens}_breadth_pct", pa.float64()),
            (f"{lens}_anomalies_count", pa.int32()),
            (f"{lens}_new_extreme_count", pa.int32()),
        ]
    fields += [
        ("source", pa.string()),
        ("ingested_at", pa.timestamp("us", tz="UTC")),
    ]
    return pa.schema(fields)


MACRO_STATE_SCHEMA = _macro_state_schema()  # US (core 4 + liquidity)
# EU: labor/growth/inflation/credit/external (5 лещи) — таксономията се деривира
# от config.MACRO_LENSES (single-source), НЕ от литерал тук. external влезе в
# X-пакет (Сесия-7 одит): преди се изпускаше → икон-осът biased нагоре.
EU_MACRO_STATE_SCHEMA = _macro_state_schema(macro_lenses("EU"))


def _cn_macro_state_schema() -> pa.Schema:
    """China wide row. 5 lenses (growth/inflation/labor/credit/property) с
    score+direction+regime (China-native), + претеглен composite_score.
    Отделна схема от US/EU — China има различна таксономия + composite.
    """
    fields = [
        ("date", pa.date32()),
        ("region", pa.string()),
        ("generated_at", pa.timestamp("us", tz="UTC")),
        ("composite_score", pa.float64()),       # претеглен (MODULE_WEIGHTS)
        ("regime_key", pa.string()),
        ("regime_label_bg", pa.string()),
        ("narrative", pa.string()),
        ("primary_driver", pa.string()),
        ("supporting_signals_json", pa.string()),
        ("top_anomalies_count", pa.int32()),
        ("top_anomalies_json", pa.string()),
        ("cross_lens_divergences_count", pa.int32()),
        ("cross_lens_divergences_json", pa.string()),
    ]
    for lens in ("growth", "inflation", "labor", "credit", "property"):
        fields += [
            (f"{lens}_score", pa.float64()),
            (f"{lens}_direction", pa.string()),
            (f"{lens}_regime", pa.string()),
        ]
    fields += [
        ("source", pa.string()),
        ("ingested_at", pa.timestamp("us", tz="UTC")),
    ]
    return pa.schema(fields)


CN_MACRO_STATE_SCHEMA = _cn_macro_state_schema()


MACRO_ANOMALIES_SCHEMA = pa.schema([
    ("date", pa.date32()),                # snapshot date (from macro_state)
    ("region", pa.string()),              # 'US' | 'EU'
    ("series_id", pa.string()),
    ("name_bg", pa.string()),
    ("lens", pa.string()),                # first lens (string, not list — denorm-ирано)
    ("lenses_json", pa.string()),         # пълен list от lenses (рядко >1)
    ("peer_group", pa.string()),
    ("z_score", pa.float64()),
    ("direction", pa.string()),           # 'up' | 'down'
    ("current_value", pa.float64()),
    ("last_observation_date", pa.date32()),
    ("is_new_extreme", pa.bool_()),
    ("new_extreme_direction", pa.string()),
    ("narrative_hint", pa.string()),
    ("source", pa.string()),
    ("ingested_at", pa.timestamp("us", tz="UTC")),
])

MACRO_DIVERGENCES_SCHEMA = pa.schema([
    ("date", pa.date32()),
    ("region", pa.string()),
    ("name", pa.string()),                # divergence rule name
    ("label_bg", pa.string()),
    ("triggered", pa.bool_()),
    ("payload_json", pa.string()),        # пълен row от source
    ("source", pa.string()),
    ("ingested_at", pa.timestamp("us", tz="UTC")),
])

SCHEMA_REGISTRY: dict[str, pa.Schema] = {
    "etf_prices": ETF_PRICES_SCHEMA,
    "rotation_us": ROTATION_SCHEMA,
    "rotation_eu": ROTATION_SCHEMA,
    "cot_positioning": COT_POSITIONING_SCHEMA,
    "vrm_state": VRM_STATE_SCHEMA,
    "vrm_week": VRM_WEEK_SCHEMA,
    "vrm": VRM_OVERLAY_SCHEMA,
    "sp500_momentum": MOMENTUM_SCHEMA,
    "stoxx600_momentum": MOMENTUM_SCHEMA,
    "stock_selection": STOCK_SELECTION_SCHEMA,
    "us_macro_state": MACRO_STATE_SCHEMA,
    "eu_macro_state": EU_MACRO_STATE_SCHEMA,
    "cn_macro_state": CN_MACRO_STATE_SCHEMA,
    "macro_anomalies": MACRO_ANOMALIES_SCHEMA,
    "macro_divergences": MACRO_DIVERGENCES_SCHEMA,
}


def get_schema(table: str) -> pa.Schema:
    if table not in SCHEMA_REGISTRY:
        raise KeyError(f"Unknown table: {table}")
    return SCHEMA_REGISTRY[table]


def schema_columns(table: str) -> list[str]:
    return [f.name for f in get_schema(table)]
