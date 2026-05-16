"""Тестове за Phase 2 collectors: momentum rank x2, cot_cta, stock_selection, vrm_week."""
from __future__ import annotations

from datetime import date

import pytest

from macro_satellite.collectors import (
    cot_cta,
    sp500_momentum,
    stock_selection,
    stoxx600_momentum,
    vrm_week,
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


def test_cot_cta_parser(fixtures_dir):
    raw = (fixtures_dir / "cot_cta_mini.json").read_bytes()
    df = cot_cta.parse(raw)
    assert len(df) == 5
    assert bool(df["on_watchlist"].all())


def test_stock_selection_parser(fixtures_dir):
    raw = (fixtures_dir / "stock_selection_mini.json").read_bytes()
    df = stock_selection.parse(raw, snapshot_date=date(2026, 5, 16))
    assert len(df) == 5
    for col in ("composite_score", "trend_score", "quality_score",
                "value_score", "risk_score"):
        assert col in df.columns
        assert df[col].notna().any()


def test_vrm_week_parser(fixtures_dir):
    raw = (fixtures_dir / "vrm_week_mini.md").read_bytes()
    df = vrm_week.parse(raw)
    assert len(df) == 1
    row = df.iloc[0]
    assert row["regime"] == "REFLATION"
    assert row["alignment"] == pytest.approx(6.0)
    assert row["alignment_max"] == 8
    assert row["gms_score"] == pytest.approx(3.0)
    assert row["ks_active"] is True or bool(row["ks_active"]) is True
    assert row["ks_variant"] == "A"
    # 4W metrics
    assert row["spy_4w"] == pytest.approx(0.1209)
    assert row["xle_4w"] == pytest.approx(-0.0920)
    assert row["gld_4w"] == pytest.approx(0.0452)
    assert row["week_start"] == date(2026, 4, 25)
    assert row["week_end"] == date(2026, 5, 1)
