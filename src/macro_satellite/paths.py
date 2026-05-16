"""Централизирани пътеки. Всички абсолютни пътища се изграждат тук."""
from __future__ import annotations

import os
from pathlib import Path

# Repo root = parent на src/. Override с MACRO_SATELLITE_ROOT за тестове.
_default_root = Path(__file__).resolve().parents[2]
REPO_ROOT = Path(os.environ.get("MACRO_SATELLITE_ROOT", _default_root))

STORAGE_DIR = REPO_ROOT / "storage"
PARQUET_DIR = STORAGE_DIR / "parquet"
RAW_DIR = STORAGE_DIR / "raw"
DELTAS_DIR = REPO_ROOT / "deltas"
LOGS_DIR = REPO_ROOT / "logs"
CONFIG_DIR = REPO_ROOT / "config"


def parquet_table_dir(table: str) -> Path:
    return PARQUET_DIR / table


def parquet_partition_path(table: str, year: int, month: int) -> Path:
    return PARQUET_DIR / table / f"year={year}" / f"month={month:02d}" / "data.parquet"


def parquet_glob(table: str) -> str:
    return str(PARQUET_DIR / table / "**" / "*.parquet")


def raw_archive_path(date_iso: str, dashboard: str, filename: str) -> Path:
    return RAW_DIR / date_iso / dashboard / filename


def delta_output_path(date_a: str, date_b: str) -> Path:
    return DELTAS_DIR / "daily" / f"{date_a}_vs_{date_b}.json"


def ensure_dirs() -> None:
    for d in (STORAGE_DIR, PARQUET_DIR, RAW_DIR, DELTAS_DIR / "daily", LOGS_DIR):
        d.mkdir(parents=True, exist_ok=True)
