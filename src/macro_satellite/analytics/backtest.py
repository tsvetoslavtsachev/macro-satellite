"""Backtest engine — conditional historical queries.

За дадена hypothesis (list от conditions върху ETF metrics), скенира 5y history
и връща episode list: всеки episode = consecutive период когато всички conditions
са истина. За всеки episode → forward returns 1m/3m/6m.

Различава се от parallels.py:
- parallels: similarity search (cosine similarity на returns vector)
- backtest: declarative conditional query ("USO >= 130 AND TLT <= 87 AND SPY pct_from_high >= -2")

Поддържани metrics:
- price: spot price
- return_Nw: rolling N-week return (price/price_N_weeks_ago - 1)
- pct_from_high_Nw: distance from N-week trailing max
- pct_from_low_Nw: distance from N-week trailing min
- ratio:OTHER: this_symbol_price / OTHER_symbol_price

Operators: ">=", "<=", ">", "<", "==", "between"
"""
from __future__ import annotations

import statistics
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import yaml
from pydantic import BaseModel, Field

from ..logging_setup import get_logger
from ..paths import CONFIG_DIR

log = get_logger(__name__)

# Forward return horizons (calendar days).
FORWARD_DAYS = {"1m": 30, "3m": 91, "6m": 182, "12m": 365}

# Episode clustering: dates within this gap → same episode.
DEFAULT_EPISODE_GAP_DAYS = 14


class ConditionSpec(BaseModel):
    symbol: str
    metric: str                              # 'price' | 'return_Nw' | 'pct_from_high_Nw' | 'pct_from_low_Nw' | 'ratio:OTHER'
    op: str                                  # '>=', '<=', '>', '<', '==', 'between'
    value: float | None = None
    value_low: float | None = None           # for 'between'
    value_high: float | None = None


class QuerySpec(BaseModel):
    name: str
    label_bg: str = ""
    description: str = ""
    conditions: list[ConditionSpec]
    forward_horizons: list[str] = Field(default_factory=lambda: ["1m", "3m", "6m"])
    forward_symbols: list[str] = Field(default_factory=lambda: ["SPY", "USO", "GLD", "TLT"])
    episode_gap_days: int = DEFAULT_EPISODE_GAP_DAYS


class _QueriesConfig(BaseModel):
    queries: list[QuerySpec]


@dataclass
class Episode:
    start_date: date
    end_date: date
    n_days: int                              # дни с матч в episode-а
    forward_returns: dict[str, dict[str, float]] = field(default_factory=dict)


@dataclass
class BacktestResult:
    query_name: str
    label_bg: str
    description: str
    n_episodes: int
    n_total_matching_days: int
    history_start: date | None
    history_end: date | None
    episodes: list[Episode] = field(default_factory=list)
    summary_stats: dict[str, dict[str, float]] = field(default_factory=dict)
    # {symbol: {horizon: {"mean": x, "median": y, "win_rate": z, "min": a, "max": b, "n": k}}}


# ────────────────────────────────────────────────────────────────────────────
#  Metric extraction
# ────────────────────────────────────────────────────────────────────────────

def _load_price_series(duck, symbols: list[str]) -> pd.DataFrame:
    """Чете daily prices за symbols → wide DataFrame indexed by date."""
    if not symbols:
        return pd.DataFrame()
    placeholders = ",".join(["?"] * len(symbols))
    sql = (f"SELECT date, symbol, price FROM etf_prices "
           f"WHERE symbol IN ({placeholders}) AND price IS NOT NULL "
           f"ORDER BY date")
    df = duck.execute(sql, list(symbols)).df()
    if df.empty:
        return pd.DataFrame()
    df["date"] = pd.to_datetime(df["date"])
    wide = df.pivot_table(index="date", columns="symbol", values="price", aggfunc="last")
    wide = wide.sort_index().ffill(limit=3)
    return wide


def _compute_metric(prices: pd.DataFrame, symbol: str, metric: str) -> pd.Series:
    """Връща pandas Series indexed by date с стойностите на metric за symbol."""
    if symbol not in prices.columns:
        return pd.Series(dtype=float)
    s = prices[symbol]
    if metric == "price":
        return s
    if metric.startswith("return_"):
        n_weeks = int(metric.split("_")[1].rstrip("w"))
        shift_days = n_weeks * 5  # trading-day approximation
        return (s / s.shift(shift_days)) - 1.0
    if metric.startswith("pct_from_high_"):
        n_weeks = int(metric.split("_")[3].rstrip("w"))
        window = n_weeks * 5
        rolling_max = s.rolling(window=window, min_periods=window // 2).max()
        return (s / rolling_max) - 1.0
    if metric.startswith("pct_from_low_"):
        n_weeks = int(metric.split("_")[3].rstrip("w"))
        window = n_weeks * 5
        rolling_min = s.rolling(window=window, min_periods=window // 2).min()
        return (s / rolling_min) - 1.0
    if metric.startswith("ratio:"):
        other = metric.split(":")[1]
        if other not in prices.columns:
            return pd.Series(dtype=float)
        return s / prices[other]
    raise ValueError(f"Unknown metric: {metric}")


def _required_symbols(query: QuerySpec) -> list[str]:
    out: set[str] = set()
    for c in query.conditions:
        out.add(c.symbol)
        if c.metric.startswith("ratio:"):
            out.add(c.metric.split(":")[1])
    for s in query.forward_symbols:
        out.add(s)
    return sorted(out)


def _condition_matches(series_val: float, c: ConditionSpec) -> bool:
    if pd.isna(series_val):
        return False
    if c.op == ">=":
        return series_val >= c.value
    if c.op == "<=":
        return series_val <= c.value
    if c.op == ">":
        return series_val > c.value
    if c.op == "<":
        return series_val < c.value
    if c.op == "==":
        return abs(series_val - c.value) < 1e-9
    if c.op == "between":
        return c.value_low <= series_val <= c.value_high
    raise ValueError(f"Unknown op: {c.op}")


# ────────────────────────────────────────────────────────────────────────────
#  Forward returns + episode clustering
# ────────────────────────────────────────────────────────────────────────────

def _forward_for_date(prices: pd.DataFrame, base_date: date,
                      symbols: list[str], horizons: list[str]) -> dict:
    """За base_date → forward returns per symbol per horizon."""
    out: dict[str, dict[str, float]] = {}
    base_ts = pd.Timestamp(base_date)
    if base_ts not in prices.index:
        before = prices.index[prices.index <= base_ts]
        if before.empty:
            return {}
        base_ts = before[-1]
    base_row = prices.loc[base_ts]
    for sym in symbols:
        if sym not in prices.columns:
            continue
        base_p = base_row.get(sym)
        if pd.isna(base_p) or base_p <= 0:
            continue
        per: dict[str, float] = {}
        for h in horizons:
            days = FORWARD_DAYS.get(h)
            if days is None:
                continue
            target_ts = base_ts + pd.Timedelta(days=days)
            in_window = prices.index[(prices.index <= target_ts) & (prices.index > base_ts)]
            if in_window.empty:
                continue
            fwd_p = prices.loc[in_window[-1], sym]
            if pd.isna(fwd_p):
                continue
            per[h] = (float(fwd_p) / float(base_p)) - 1.0
        if per:
            out[sym] = per
    return out


def _cluster_to_episodes(matching_dates: list[date], gap_days: int) -> list[Episode]:
    if not matching_dates:
        return []
    matching_dates = sorted(matching_dates)
    episodes: list[Episode] = []
    cur_start = matching_dates[0]
    cur_end = matching_dates[0]
    cur_count = 1
    for d in matching_dates[1:]:
        if (d - cur_end).days <= gap_days:
            cur_end = d
            cur_count += 1
        else:
            episodes.append(Episode(start_date=cur_start, end_date=cur_end, n_days=cur_count))
            cur_start = d
            cur_end = d
            cur_count = 1
    episodes.append(Episode(start_date=cur_start, end_date=cur_end, n_days=cur_count))
    return episodes


def _compute_summary_stats(episodes: list[Episode], symbols: list[str],
                           horizons: list[str]) -> dict:
    out: dict[str, dict[str, dict[str, float]]] = {}
    for sym in symbols:
        out[sym] = {}
        for h in horizons:
            vals = []
            for ep in episodes:
                v = ep.forward_returns.get(sym, {}).get(h)
                if v is not None:
                    vals.append(v)
            if not vals:
                continue
            n_pos = sum(1 for v in vals if v > 0)
            out[sym][h] = {
                "n": len(vals),
                "mean": statistics.fmean(vals),
                "median": statistics.median(vals),
                "min": min(vals),
                "max": max(vals),
                "win_rate": n_pos / len(vals),
            }
    return out


# ────────────────────────────────────────────────────────────────────────────
#  Main entry point
# ────────────────────────────────────────────────────────────────────────────

def run_backtest(query: QuerySpec, duck) -> BacktestResult:
    symbols = _required_symbols(query)
    prices = _load_price_series(duck, symbols)
    if prices.empty:
        return BacktestResult(
            query_name=query.name, label_bg=query.label_bg,
            description=query.description, n_episodes=0,
            n_total_matching_days=0, history_start=None, history_end=None,
        )

    # Compute each condition metric series
    series_per_cond: list[pd.Series] = []
    for c in query.conditions:
        s = _compute_metric(prices, c.symbol, c.metric)
        series_per_cond.append(s)

    # Per-date AND of all conditions
    combined_idx = prices.index
    matches_mask = pd.Series(True, index=combined_idx)
    for s, c in zip(series_per_cond, query.conditions):
        if s.empty:
            matches_mask = pd.Series(False, index=combined_idx)
            break
        aligned = s.reindex(combined_idx)
        cond_mask = aligned.apply(lambda v: _condition_matches(v, c))
        matches_mask = matches_mask & cond_mask

    matching_dates = [ts.date() for ts in combined_idx[matches_mask]]

    # Cluster to episodes
    episodes = _cluster_to_episodes(matching_dates, query.episode_gap_days)

    # Forward returns per episode (from episode start_date)
    for ep in episodes:
        ep.forward_returns = _forward_for_date(
            prices, ep.start_date, query.forward_symbols, query.forward_horizons)

    # Summary stats
    summary = _compute_summary_stats(episodes, query.forward_symbols, query.forward_horizons)

    return BacktestResult(
        query_name=query.name,
        label_bg=query.label_bg,
        description=query.description,
        n_episodes=len(episodes),
        n_total_matching_days=len(matching_dates),
        history_start=combined_idx[0].date() if len(combined_idx) else None,
        history_end=combined_idx[-1].date() if len(combined_idx) else None,
        episodes=episodes,
        summary_stats=summary,
    )


def load_canonical_queries(path: Path | None = None) -> list[QuerySpec]:
    p = path or (CONFIG_DIR / "backtest_queries.yaml")
    with open(p, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    cfg = _QueriesConfig.model_validate(data)
    return cfg.queries


def find_query(name: str, path: Path | None = None) -> QuerySpec:
    for q in load_canonical_queries(path):
        if q.name == name:
            return q
    raise KeyError(f"Query '{name}' not found in backtest_queries.yaml")


# ────────────────────────────────────────────────────────────────────────────
#  Markdown report formatter
# ────────────────────────────────────────────────────────────────────────────

def format_report(result: BacktestResult) -> str:
    lines = []
    lines.append(f"# Backtest: {result.label_bg or result.query_name}")
    lines.append(f"\n_Query: `{result.query_name}`_")
    if result.description:
        lines.append(f"\n_{result.description}_")
    lines.append("")
    lines.append(f"- **Episode count:** {result.n_episodes}")
    lines.append(f"- **Total matching days:** {result.n_total_matching_days}")
    lines.append(f"- **History range:** {result.history_start} → {result.history_end}")
    lines.append("")

    if not result.episodes:
        lines.append("_Не намерени историчски епизоди._")
        return "\n".join(lines)

    # Summary stats
    lines.append("## Forward returns статистика\n")
    horizons_seen: list[str] = []
    for sym, h_dict in result.summary_stats.items():
        for h in h_dict:
            if h not in horizons_seen:
                horizons_seen.append(h)

    if horizons_seen:
        lines.append("| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |")
        lines.append("|---|---|---:|---:|---:|---:|---:|---:|")
        for sym, h_dict in result.summary_stats.items():
            for h in horizons_seen:
                if h not in h_dict:
                    continue
                stats = h_dict[h]
                lines.append(
                    f"| **{sym}** | {h} | {int(stats['n'])} | "
                    f"{stats['mean']*100:+.1f}% | {stats['median']*100:+.1f}% | "
                    f"{stats['min']*100:+.1f}% | {stats['max']*100:+.1f}% | "
                    f"{stats['win_rate']*100:.0f}% |"
                )
        lines.append("")

    # Episode details
    lines.append("## Episodes\n")
    for ep in result.episodes[:20]:
        lines.append(f"### {ep.start_date} → {ep.end_date} ({ep.n_days} matching days)")
        if not ep.forward_returns:
            lines.append("_Без forward returns (близо до края на история-та)._")
            continue
        lines.append("| Symbol | +1m | +3m | +6m | +12m |")
        lines.append("|---|---:|---:|---:|---:|")
        for sym, h_dict in ep.forward_returns.items():
            cells = []
            for h in ("1m", "3m", "6m", "12m"):
                v = h_dict.get(h)
                cells.append(f"{v*100:+.1f}%" if v is not None else "-")
            lines.append(f"| **{sym}** | " + " | ".join(cells) + " |")
        lines.append("")
    if len(result.episodes) > 20:
        lines.append(f"\n_... и още {len(result.episodes) - 20} епизода._")

    return "\n".join(lines)
