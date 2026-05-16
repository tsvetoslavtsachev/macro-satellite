"""Парсер тестове върху малки offline fixtures."""
from __future__ import annotations

from datetime import date

import pytest

from macro_satellite.collectors import (
    cot_monitor,
    etf_dashboard,
    sp500_rotation,
    stoxx600_rotation,
    vrm_state,
)


def test_etf_dashboard_parser(fixtures_dir):
    raw = (fixtures_dir / "etfs_mini_2026-05-15.json").read_bytes()
    df = etf_dashboard.parse(raw)
    assert len(df) == 5
    assert set(df["symbol"]) == {"USO", "XLE", "GLD", "SPY", "TLT"}
    assert (df["date"] == date(2026, 5, 15)).all()
    uso = df[df["symbol"] == "USO"].iloc[0]
    assert uso["price"] == pytest.approx(148.23, rel=1e-3)


def test_etf_parser_snapshot_override(fixtures_dir):
    raw = (fixtures_dir / "etfs_mini_2026-05-15.json").read_bytes()
    df = etf_dashboard.parse(raw, snapshot_date=date(2026, 1, 1))
    assert (df["date"] == date(2026, 1, 1)).all()


def test_sp500_rotation_parser(fixtures_dir):
    raw = (fixtures_dir / "sp500_rotation_mini_2026-05-14.json").read_bytes()
    df = sp500_rotation.parse(raw)
    assert len(df) == 20
    assert (df["date"] == date(2026, 5, 14)).all()
    # Quadrant normalized към snake_case lowercase
    quads = set(df["quadrant_1m"].dropna().unique())
    assert all(q == q.lower() for q in quads)
    assert "—" not in quads  # normalized към 'other'


def test_stoxx600_rotation_parser_reuses_sp500(fixtures_dir):
    raw = (fixtures_dir / "sp500_rotation_mini_2026-05-14.json").read_bytes()
    df = stoxx600_rotation.parse(raw)
    assert len(df) == 20


def test_cot_monitor_parser(fixtures_dir):
    raw = (fixtures_dir / "cot_watchlist_mini_2026-05-12.json").read_bytes()
    df = cot_monitor.parse(raw)
    assert len(df) == 10
    assert bool(df["on_watchlist"].all())
    pct = df["percentile_5y"].dropna()
    assert bool((pct >= 0).all()) and bool((pct <= 100).all())


def test_vrm_state_parser(fixtures_dir):
    raw = (fixtures_dir / "vrm_state_mini.md").read_bytes()
    df = vrm_state.parse(raw)
    assert len(df) == 1
    row = df.iloc[0]
    assert row["regime"] == "REFLATION"
    assert row["ks_status"] == "inactive"
    assert row["alignment_score"] == 7.0
    assert row["alignment_total"] == 8
    assert row["last_updated_md"] == date(2026, 5, 10)


def test_vrm_state_parser_snapshot_override(fixtures_dir):
    raw = (fixtures_dir / "vrm_state_mini.md").read_bytes()
    df = vrm_state.parse(raw, snapshot_date=date(2026, 5, 16))
    row = df.iloc[0]
    assert row["date"] == date(2026, 5, 16)
    assert row["last_updated_md"] == date(2026, 5, 10)
    assert bool(row["is_change_day"]) is False
