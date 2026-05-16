"""Тестове за backtest engine."""
from __future__ import annotations

from datetime import date, timedelta

import pandas as pd

from macro_satellite.analytics.backtest import (
    ConditionSpec,
    Episode,
    QuerySpec,
    _cluster_to_episodes,
    _compute_metric,
    _compute_summary_stats,
    _condition_matches,
    _required_symbols,
    load_canonical_queries,
)


def test_condition_matches_basic():
    c = ConditionSpec(symbol="SPY", metric="price", op=">=", value=500.0)
    assert _condition_matches(550.0, c) is True
    assert _condition_matches(499.0, c) is False
    assert _condition_matches(float("nan"), c) is False


def test_condition_matches_between():
    c = ConditionSpec(symbol="SPY", metric="price", op="between",
                      value_low=400.0, value_high=500.0)
    assert _condition_matches(450.0, c) is True
    assert _condition_matches(350.0, c) is False
    assert _condition_matches(550.0, c) is False


def test_cluster_to_episodes_basic():
    dates = [
        date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3),  # cluster 1
        date(2023, 2, 1),                                        # cluster 2 (gap > 14d)
        date(2023, 2, 5), date(2023, 2, 10),                     # joined to cluster 2
    ]
    eps = _cluster_to_episodes(dates, gap_days=14)
    assert len(eps) == 2
    assert eps[0].start_date == date(2023, 1, 1)
    assert eps[0].end_date == date(2023, 1, 3)
    assert eps[0].n_days == 3
    assert eps[1].start_date == date(2023, 2, 1)
    assert eps[1].end_date == date(2023, 2, 10)
    assert eps[1].n_days == 3


def test_cluster_to_episodes_empty():
    assert _cluster_to_episodes([], 14) == []


def test_required_symbols_resolves_ratio():
    q = QuerySpec(
        name="t",
        conditions=[
            ConditionSpec(symbol="USO", metric="price", op=">=", value=100),
            ConditionSpec(symbol="XLE", metric="ratio:SPY", op=">=", value=0.1),
        ],
        forward_symbols=["GLD"],
    )
    syms = _required_symbols(q)
    assert "USO" in syms
    assert "XLE" in syms
    assert "SPY" in syms       # from ratio
    assert "GLD" in syms       # from forward


def test_compute_metric_price():
    prices = pd.DataFrame(
        {"SPY": [100, 110, 105]},
        index=pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-03"]),
    )
    s = _compute_metric(prices, "SPY", "price")
    assert s.iloc[0] == 100
    assert s.iloc[-1] == 105


def test_compute_metric_ratio():
    prices = pd.DataFrame(
        {"XLE": [50, 60, 55], "SPY": [400, 400, 500]},
        index=pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-03"]),
    )
    ratio = _compute_metric(prices, "XLE", "ratio:SPY")
    assert abs(ratio.iloc[0] - 0.125) < 1e-9
    assert abs(ratio.iloc[1] - 0.15) < 1e-9


def test_summary_stats_basic():
    episodes = [
        Episode(start_date=date(2023, 1, 1), end_date=date(2023, 1, 1), n_days=1,
                forward_returns={"SPY": {"1m": 0.05, "3m": 0.10}}),
        Episode(start_date=date(2023, 2, 1), end_date=date(2023, 2, 1), n_days=1,
                forward_returns={"SPY": {"1m": -0.02, "3m": 0.05}}),
        Episode(start_date=date(2023, 3, 1), end_date=date(2023, 3, 1), n_days=1,
                forward_returns={"SPY": {"1m": 0.03}}),  # no 3m
    ]
    stats = _compute_summary_stats(episodes, ["SPY"], ["1m", "3m"])
    assert stats["SPY"]["1m"]["n"] == 3
    assert stats["SPY"]["1m"]["win_rate"] == 2/3
    assert stats["SPY"]["3m"]["n"] == 2
    assert abs(stats["SPY"]["3m"]["mean"] - 0.075) < 1e-9


def test_canonical_queries_load():
    queries = load_canonical_queries()
    names = {q.name for q in queries}
    assert "stagflation_signature" in names
    assert "oil_supply_shock" in names
    # Each query has well-formed conditions
    for q in queries:
        assert len(q.conditions) >= 1
        for c in q.conditions:
            assert c.op in {">=", "<=", ">", "<", "==", "between"}
