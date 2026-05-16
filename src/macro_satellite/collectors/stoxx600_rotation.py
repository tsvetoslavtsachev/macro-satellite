"""Парсер за STOXX600 Rotation Radar. Същата схема като SP500 — reuse."""
from __future__ import annotations

from datetime import date

import pandas as pd

from .sp500_rotation import parse as _parse_sp500


def parse(raw: bytes, snapshot_date: date | None = None, source: str = "stoxx600_rotation") -> pd.DataFrame:
    return _parse_sp500(raw, snapshot_date=snapshot_date, source=source)
