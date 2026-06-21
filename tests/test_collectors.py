"""Парсер тестове върху малки offline fixtures."""
from __future__ import annotations

from datetime import date

from macro_satellite.collectors import (
    cot_monitor,
    sp500_rotation,
    stoxx600_rotation,
    vrm_state,
)

# ETF парсерът е премахнат в S17 Build D2 (etf_prices = yfinance, не etf_dashboard).
# Неговите две parser-теста са пенсионирани заедно с модула; storage/delta тестовете
# вече ползват tests/_etf_fixture.py като data-generator.


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
