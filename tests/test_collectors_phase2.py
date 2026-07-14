"""Тестове за Phase 2 collectors: momentum rank x2, stock_selection.

(vrm_week parser тестът е пенсиониран заедно с колектора — мандат №36, 07.2026;
живият VRM канал е collectors/vrm_overlay.py → test_vrm_overlay_collector.)
"""
from __future__ import annotations

from datetime import date

from macro_satellite.collectors import (
    sp500_momentum,
    stock_selection,
    stoxx600_momentum,
)


def test_sp500_momentum_parser(fixtures_dir):
    raw = (fixtures_dir / "sp500_momentum_mini.json").read_bytes()
    df = sp500_momentum.parse(raw, snapshot_date=date(2026, 5, 16))
    assert len(df) == 5
    assert "momentum_score" in df.columns
    assert (df["date"] == date(2026, 5, 16)).all()
    assert df["country"].isna().all()  # SP500 has no country field


def test_stoxx600_momentum_parser(fixtures_dir):
    raw = (fixtures_dir / "stoxx600_momentum_mini.json").read_bytes()
    df = stoxx600_momentum.parse(raw, snapshot_date=date(2026, 5, 16))
    assert len(df) == 5
    assert df["country"].notna().all()  # EU has country
    assert df["currency"].notna().all()
    assert df["market_cap"].isna().all()  # STOXX600 doesn't have market_cap


def test_stock_selection_parser(fixtures_dir):
    raw = (fixtures_dir / "stock_selection_mini.json").read_bytes()
    df = stock_selection.parse(raw, snapshot_date=date(2026, 5, 16))
    assert len(df) == 5
    for col in ("composite_score", "trend_score", "quality_score",
                "value_score", "risk_score"):
        assert col in df.columns
        assert df[col].notna().any()
