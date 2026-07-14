"""Парсер тестове върху малки offline fixtures."""
from __future__ import annotations

from datetime import date

from macro_satellite.collectors import (
    cot_monitor,
    sp500_rotation,
    stoxx600_rotation,
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
    # B1: full-history percentile носи честното име `percentile_hist` (не лъжливото „_5y").
    pct = df["percentile_hist"].dropna()
    assert bool((pct >= 0).all()) and bool((pct <= 100).all())
    assert "percentile_5y" not in df.columns, "лъжливото поле '_5y' е премахнато (док. №2)"
    # hist_weeks идва от watchlist.json `history_weeks` (несравним между пазари)
    hw = df["hist_weeks"].dropna()
    assert len(hw) == len(df) and bool((hw > 0).all())


# vrm_state parser тестовете са пенсионирани заедно с колектора (мандат №36,
# 07.2026) — живият VRM канал е collectors/vrm_overlay.py (test_vrm_overlay_collector).
