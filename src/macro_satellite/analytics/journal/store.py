"""Store за gap-журнала (Тухла 2a) — ОТДЕЛЕН git-tracked namespace.

`journal/` е в корена на репото, НЕ под `storage/parquet` → нула замърсяване на
колектора (C3), извън LFS price данните, извън `get_duck()` auto-registration.

Два артефакта:
  • economy_reconstructed.parquet — реконструираният икономика-крак (revision-biased).
  • machine_episodes.parquet       — машинните записи, по 1 ред на (епизод × хоризонт Y).

Машинните записи се РЕГЕНЕРИРАТ от backfill (idempotent overwrite). Човешките присъди
(Тухла 2b) ще са append-only в ОТДЕЛЕН файл — тук не се пишат (NULL колоните са резерв).
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from ...paths import JOURNAL_DIR

ECONOMY_RECON_FILE = "economy_reconstructed.parquet"
MACHINE_EPISODES_FILE = "machine_episodes.parquet"


def _econ_file(region: str) -> str:
    """US → unsuffixed (байт-идентичен с Тухла 2a); EU/CN → region-суфикс."""
    return (ECONOMY_RECON_FILE if region.upper() == "US"
            else f"economy_reconstructed_{region.lower()}.parquet")


def _episodes_file(region: str) -> str:
    return (MACHINE_EPISODES_FILE if region.upper() == "US"
            else f"machine_episodes_{region.lower()}.parquet")

# ── Schemas ───────────────────────────────────────────────────────────────────

ECONOMY_RECON_SCHEMA = pa.schema([
    ("week", pa.string()),
    ("week_end", pa.date32()),
    ("economy_axis", pa.float64()),
    ("labor_score", pa.float64()),
    ("growth_score", pa.float64()),
    ("inflation_score", pa.float64()),
    ("liquidity_score", pa.float64()),
    ("as_of_date", pa.date32()),
    ("age_days", pa.int32()),
    ("revision_biased", pa.bool_()),     # винаги True — backfill чете ревизиран cache
    ("ingested_at", pa.timestamp("us", tz="UTC")),
])

MACHINE_EPISODES_SCHEMA = pa.schema([
    # ── machine-derived (винаги попълнени) ──────────────────────────────────
    ("gap_episode_id", pa.string()),
    ("config_key", pa.string()),               # 'gap_pos' | 'gap_neg' (Възел 4, грубо)
    ("open_week", pa.string()),
    ("open_date", pa.date32()),
    ("close_date", pa.date32()),               # NULL ако censored
    ("n_weeks", pa.int32()),
    ("censored", pa.bool_()),                  # епизодът все още отворен на края на серията
    ("open_economy_axis", pa.float64()),
    ("open_markets_axis", pa.float64()),
    ("open_gap", pa.float64()),
    ("peak_gap", pa.float64()),
    ("horizon_y", pa.int32()),                 # седмици (4 | 8 | 13)
    ("y_date", pa.date32()),                   # open_date + Y (NULL ако unresolved)
    ("y_economy_axis", pa.float64()),
    ("y_markets_axis", pa.float64()),
    ("y_gap", pa.float64()),
    ("sigma_economy", pa.float64()),           # глобална σ на седмичните Δ (vol-норм.)
    ("sigma_markets", pa.float64()),
    ("d_economy", pa.float64()),               # ΔE между open и Y
    ("d_markets", pa.float64()),               # ΔM
    ("attribution_economy_share", pa.float64()),
    ("attribution_markets_share", pa.float64()),
    ("outcome", pa.string()),                  # market_leads|economy_leads|meet|widen|unresolved
    ("censored_at_y", pa.bool_()),
    # ── caveat-маркери (заковани в данните, не само в доклада) ───────────────
    ("revision_biased", pa.bool_()),                  # caveat #1 — best-case, не real-time
    ("methodology_consistent_backfill", pa.bool_()),  # caveat #2 — днешна методология назад
    # ── human-judgment (NULL в 2a; резерв за Тухла 2b) ──────────────────────
    ("claim", pa.string()),
    ("horizon_y_human", pa.int32()),
    ("falsification_criterion", pa.string()),
    ("author", pa.string()),
    ("judgment_date", pa.date32()),
    ("ingested_at", pa.timestamp("us", tz="UTC")),
])


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _ensure_dir() -> Path:
    JOURNAL_DIR.mkdir(parents=True, exist_ok=True)
    return JOURNAL_DIR


def write_economy_reconstructed(df: pd.DataFrame, region: str = "US") -> Path:
    """Презаписва economy_reconstructed[_<region>].parquet (idempotent — регенерируем)."""
    _ensure_dir()
    df = df.copy()
    df["revision_biased"] = True
    df["ingested_at"] = _utc_now()
    table = pa.Table.from_pandas(df, schema=ECONOMY_RECON_SCHEMA, preserve_index=False)
    path = JOURNAL_DIR / _econ_file(region)
    pq.write_table(table, path)
    return path


def write_machine_episodes(df: pd.DataFrame, region: str = "US") -> Path:
    """Презаписва machine_episodes[_<region>].parquet (idempotent — от backfill)."""
    _ensure_dir()
    df = df.copy()
    df["revision_biased"] = True
    df["methodology_consistent_backfill"] = True
    # human-judgment колони → NULL (резерв за 2b)
    for col, default in (
        ("claim", None), ("horizon_y_human", None),
        ("falsification_criterion", None), ("author", None), ("judgment_date", None),
    ):
        if col not in df.columns:
            df[col] = default
    df["ingested_at"] = _utc_now()
    table = pa.Table.from_pandas(df, schema=MACHINE_EPISODES_SCHEMA, preserve_index=False)
    path = JOURNAL_DIR / _episodes_file(region)
    pq.write_table(table, path)
    return path


def read_machine_episodes(region: str = "US") -> pd.DataFrame:
    path = JOURNAL_DIR / _episodes_file(region)
    if not path.exists():
        return pd.DataFrame()
    return pq.read_table(path).to_pandas()
