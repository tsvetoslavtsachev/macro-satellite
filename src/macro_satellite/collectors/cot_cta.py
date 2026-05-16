"""Парсер за cot-cta-positioning-dashboard/data/derived/watchlist.json.

Same schema като cot_monitor — reuse logiq.
"""
from __future__ import annotations

from datetime import date

import pandas as pd

from .cot_monitor import parse as _parse_cot


def parse(raw: bytes, snapshot_date: date | None = None,
          source: str = "cot_cta_positioning") -> pd.DataFrame:
    return _parse_cot(raw, snapshot_date=snapshot_date, source=source)
