"""Comprehensive data export за downstream analysis (parallel-thinking, deep research, custom workflows).

Различава се от briefing.py / narrative.py:
- briefing: structured TLDR + 8 sections, ~10KB
- narrative: prose with thesis, ~5KB
- full_export: RAW data, no truncation, ~30-50KB, optimized за други AI агенти да го парсват

Всяка секция е self-contained с пълни tables, dates, IDs, contexts.
"""
from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

from ..config import MACRO_REGIONS, macro_lenses
from ..logging_setup import get_logger
from ..paths import REPO_ROOT
from ..storage.duckdb_conn import get_duck
from .backtest import (
    QuerySpec,
    format_report as backtest_format,
    load_canonical_queries,
    run_backtest,
)
from .divergence_engine import evaluate_all
from .macro_anomalies_expander import persistent_anomalies
from .parallels import find_parallels
from .rotation_events import rotation_diff
from .weekly_window import WeekWindow, current_week, last_close_on_or_before, previous_week
from .z_scores import scan_universe

log = get_logger(__name__)

# Broader universe than briefing.CORE_ETFS — include all macro proxies.
EXPORT_ETF_UNIVERSE = [
    # Energy
    "USO", "XLE", "DBC",
    # Defense / Industrial
    "DFEN", "XLI",
    # Metals
    "GLD", "SLV", "GDX",
    # Other commodities
    "DBA", "URA",
    # Rates / Bonds
    "TLT", "IEF", "SHY", "TIP", "LQD", "HYG",
    # USD
    "UUP",
    # US Equity
    "SPY", "QQQ", "IWM", "DIA",
    # International
    "EFA", "EEM", "VEA", "VWO",
    # US Sectors
    "XLF", "XLK", "XLV", "XLP", "XLY", "XLB", "XLU", "XLRE", "XLC",
    # Real estate
    "VNQ",
    # Crypto / Semis
    "IBIT", "SOXX",
]


def _fmt_pct(x, decimals: int = 2) -> str:
    if x is None or pd.isna(x):
        return "-"
    return f"{x*100:+.{decimals}f}%"


def _fmt_num(x, decimals: int = 2) -> str:
    if x is None or pd.isna(x):
        return "-"
    try:
        return f"{float(x):.{decimals}f}"
    except (ValueError, TypeError):
        return str(x)


# ──────────────────────────────────────────────────────────────────────────
#  Section generators — each returns markdown string
# ──────────────────────────────────────────────────────────────────────────

def _header(week: WeekWindow) -> str:
    return (
        f"# Сателит — пълен data export за {week.label}\n\n"
        f"_Период: {week.week_start} → {week.week_end}_  \n"
        f"_Генериран: {pd.Timestamp.utcnow().strftime('%Y-%m-%d %H:%M UTC')}_  \n"
        f"_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, "
        f"deep research, custom workflows)_  \n"
        f"_Различава се от: `{week.label}.md` (structured briefing) и "
        f"`narrative_{week.label}.md` (prose narrative)._\n\n"
        f"_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._\n"
    )


def _section_etf_anomalies(duck, week: WeekWindow) -> str:
    lines = ["## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)\n"]
    lines.append("_Седмично изменение vs trailing 13-week distribution на същия symbol. "
                 "z-score = брой стандартни отклонения от mean._\n")
    results = scan_universe(duck, EXPORT_ETF_UNIVERSE, week, trailing_n=13, z_threshold=1.0)
    if not results:
        lines.append("_Никой ETF не премина 1.0σ._\n")
        return "\n".join(lines)

    lines.append(f"**{len(results)} ETF в universe-а от {len(EXPORT_ETF_UNIVERSE)} с |z| >= 1.0σ:**\n")
    lines.append("| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |")
    lines.append("|---|---:|---:|---:|---:|---|---|---:|---:|---:|")
    for r in results:
        lines.append(
            f"| **{r.symbol}** | {_fmt_pct(r.weekly_change)} | "
            f"{r.z_score:+.2f}σ | {r.price_a:.2f} | {r.price_b:.2f} | "
            f"{r.date_a} | {r.date_b} | "
            f"{_fmt_pct(r.trailing_mean)} | {_fmt_pct(r.trailing_std)} | "
            f"{r.n_baseline_weeks} |"
        )
    return "\n".join(lines) + "\n"


def _section_divergence_patterns(duck, week: WeekWindow) -> str:
    lines = ["## 2. Cross-asset divergence patterns — пълно evaluation\n"]
    lines.append("_5 канонични patterns от `config/divergence_rules.yaml`, "
                 "evaluated за края на седмицата._\n")
    hits = evaluate_all(week.week_end, duck)
    for hit in hits:
        status = "🔔 ТРИГГЕРИРАН" if hit.triggered else "не активен"
        lines.append(f"### {hit.label_bg} (`{hit.name}`) — {status}")
        lines.append(f"_{hit.description}_  ")
        lines.append(f"**Window:** {hit.window_days}d ending {hit.end_date} · "
                     f"**Conditions matched:** {hit.n_matched}/{len(hit.matches)}\n")
        lines.append("| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |")
        lines.append("|---|---|---:|:---:|---:|---:|---|---|")
        for m in hit.matches:
            mark = "✅" if m.matched else "❌"
            target = f"{m.target_direction} ≥ {m.target_min_pct}%"
            actual = f"{m.actual_change_pct:+.2f}%" if pd.notna(m.actual_change_pct) else "no data"
            lines.append(
                f"| {m.symbol} | {target} | {actual} | {mark} | "
                f"{_fmt_num(m.price_a)} | {_fmt_num(m.price_b)} | "
                f"{m.date_a or '-'} | {m.date_b or '-'} |"
            )
        lines.append("")
    return "\n".join(lines) + "\n"


def _section_parallels(duck, week: WeekWindow) -> str:
    lines = ["## 3. Исторически паралели — top 10 най-similar weeks\n"]
    lines.append("_Cosine similarity vs 10-ETF macro signature vector "
                 "(SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). "
                 "Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._\n")
    parallels = find_parallels(duck, week, top_k=10)
    if not parallels:
        lines.append("_Недостатъчно история за similarity search._\n")
        return "\n".join(lines)
    for i, p in enumerate(parallels, 1):
        lines.append(f"### Паралел #{i}: {p.match_week} (week ending {p.match_week_end})")
        lines.append(f"**Cosine similarity:** {p.cosine_similarity:.4f} · "
                     f"**Common symbols:** {p.n_common_symbols}/10\n")
        if not p.forward_returns:
            lines.append("_Forward returns липсват._\n")
            continue
        lines.append("| Symbol | +1m | +3m | +6m |")
        lines.append("|---|---:|---:|---:|")
        for sym in ("SPY", "USO", "GLD", "TLT", "XLE", "IWM"):
            if sym not in p.forward_returns:
                continue
            fwd = p.forward_returns[sym]
            lines.append(
                f"| **{sym}** | {_fmt_pct(fwd.get('1m'))} | "
                f"{_fmt_pct(fwd.get('3m'))} | {_fmt_pct(fwd.get('6m'))} |"
            )
        lines.append("")
    return "\n".join(lines) + "\n"


def _section_backtests(duck, week: WeekWindow) -> str:
    lines = ["## 4. Backtest на canonical queries\n"]
    lines.append("_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + "
                 "forward returns статистика (mean/median/win_rate)._\n")
    queries = load_canonical_queries()
    for q in queries:
        result = run_backtest(q, duck)
        lines.append(f"### `{q.name}` — {q.label_bg}")
        lines.append(f"_{q.description}_  ")
        lines.append(f"**Episodes:** {result.n_episodes} · "
                     f"**Total matching days:** {result.n_total_matching_days} · "
                     f"**History:** {result.history_start} → {result.history_end}\n")
        if not result.summary_stats:
            lines.append("_Без data за forward returns._\n")
            continue
        # Stats table
        lines.append("| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |")
        lines.append("|---|---|---:|---:|---:|---:|---:|---:|")
        for sym, h_dict in result.summary_stats.items():
            for h, stats in h_dict.items():
                lines.append(
                    f"| **{sym}** | {h} | {int(stats['n'])} | "
                    f"{stats['mean']*100:+.1f}% | {stats['median']*100:+.1f}% | "
                    f"{stats['min']*100:+.1f}% | {stats['max']*100:+.1f}% | "
                    f"{stats['win_rate']*100:.0f}% |"
                )
        # Recent episodes (last 5)
        if result.episodes:
            lines.append("\n**Episodes (последни 5 от " + str(len(result.episodes)) + "):**")
            for ep in result.episodes[-5:]:
                lines.append(f"- `{ep.start_date} → {ep.end_date}` ({ep.n_days}d)")
        lines.append("")
    return "\n".join(lines) + "\n"


def _section_persistent_macro(duck) -> str:
    lines = ["## 5. Persistent макро аномалии (US + EU + CN)\n"]
    lines.append("_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. "
                 "Сегашната history е малка (~2 weeks); pers signal става информативен с time._\n")
    for region in MACRO_REGIONS:
        try:
            df = persistent_anomalies(region, lookback_weeks=4,
                                      min_occurrences=1, min_abs_z=1.5, duck=duck)
        except Exception as e:
            lines.append(f"### {region} — error: {e}\n")
            continue
        if df.empty:
            lines.append(f"### {region}\n_Няма серии с persistence._\n")
            continue
        lines.append(f"### {region} ({len(df)} серии)\n")
        lines.append("| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \\|z\\| | Max \\|z\\| | First date | Last date | NEW-EXTREME |")
        lines.append("|---|---|---|---|---:|---:|---:|---|---|:---:|")
        for _, r in df.iterrows():
            ext = "✓" if r["any_new_extreme"] else "-"
            lines.append(
                f"| **{r['series_id']}** | {r['name_bg']} | {r['lens']} | "
                f"{r['peer_group']} | {int(r['occurrences'])} | "
                f"{r['mean_abs_z']:.2f} | {r['max_abs_z']:.2f} | "
                f"{r['first_date']} | {r['last_date']} | {ext} |"
            )
        lines.append("")
    return "\n".join(lines) + "\n"


def _section_macro_state(duck, region: str) -> str:
    table = f"{region.lower()}_macro_state"
    sec_num = 6 + list(MACRO_REGIONS).index(region.upper())
    lines = [f"## {sec_num}. {region} Macro State — пълен snapshot\n"]
    try:
        df = duck.execute(
            f"SELECT * FROM {table} ORDER BY date DESC LIMIT 1"
        ).df()
    except Exception as e:
        lines.append(f"_Error: {e}_\n")
        return "\n".join(lines)
    if df.empty:
        lines.append(f"_Няма {region} macro state._\n")
        return "\n".join(lines)
    r = df.iloc[0]
    lines.append(f"**Дата:** {r['date']} · **Generated:** {r['generated_at']}")
    lines.append(f"\n**Режим:** `{r['regime_key']}` ({r['regime_label_bg']})  ")
    lines.append(f"**Primary driver:** `{r['primary_driver']}`\n")

    # Lens scores
    lines.append("### Lens scores")
    lines.append("| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |")
    lines.append("|---|---:|---|---:|---:|---:|")
    for lens in macro_lenses(region):
        score = r.get(f"{lens}_score")
        direction = r.get(f"{lens}_direction")
        breadth = r.get(f"{lens}_breadth_pct")
        n_anom = r.get(f"{lens}_anomalies_count")
        n_ext = r.get(f"{lens}_new_extreme_count")
        if pd.isna(score):
            continue
        lines.append(
            f"| **{lens}** | {_fmt_num(score, 1)} | {direction or '-'} | "
            f"{_fmt_num(breadth, 1)}% | "
            f"{int(n_anom) if pd.notna(n_anom) else '-'} | "
            f"{int(n_ext) if pd.notna(n_ext) else '-'} |"
        )
    lines.append("")

    # Top anomalies (full)
    try:
        anomalies = json.loads(r.get("top_anomalies_json") or "[]")
    except Exception:
        anomalies = []
    if anomalies:
        lines.append(f"### Top anomalies ({len(anomalies)} серии)")
        lines.append("| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |")
        lines.append("|---|---|---|---|---:|---|---:|---|:---:|")
        for a in anomalies:
            lenses = a.get("lens") or []
            if isinstance(lenses, str):
                lenses = [lenses]
            ext_marker = ""
            if a.get("is_new_extreme"):
                ext_marker = f"✓ {a.get('new_extreme_direction', '')}"
            lines.append(
                f"| **{a.get('series_id', '?')}** | {a.get('name_bg', '?')} | "
                f"{', '.join(lenses)} | {a.get('peer_group', '-')} | "
                f"{a.get('z_score', 0):+.2f} | {a.get('direction', '-')} | "
                f"{_fmt_num(a.get('current_value'))} | "
                f"{a.get('last_date', '-')} | {ext_marker or '-'} |"
            )
        lines.append("")

        # Narrative hints (separate section, full text)
        hints = [a for a in anomalies if a.get("narrative_hint")]
        if hints:
            lines.append("### Narrative hints от макро лещите")
            for h in hints:
                lines.append(f"- **{h['series_id']}**: {h['narrative_hint']}")
            lines.append("")

    # Cross-lens divergences (full JSON unpacked)
    try:
        divs = json.loads(r.get("cross_lens_divergences_json") or "[]")
    except Exception:
        divs = []
    if divs:
        lines.append(f"### Cross-lens divergences ({len(divs)} entries)")
        for d in divs:
            label = d.get("label_bg") or d.get("label") or d.get("name") or d.get("key") or "?"
            triggered = "🔔" if d.get("triggered", d.get("active", True)) else "💤"
            lines.append(f"- {triggered} **{label}**")
            # All remaining fields as bullet
            extras = {k: v for k, v in d.items()
                      if k not in {"label", "label_bg", "name", "key", "triggered", "active"}}
            for k, v in extras.items():
                if isinstance(v, (dict, list)):
                    v = json.dumps(v, ensure_ascii=False)[:200]
                lines.append(f"  - `{k}`: {v}")
        lines.append("")

    # Executive summary narrative
    if r.get("narrative"):
        lines.append("### Executive narrative")
        lines.append(f"> {str(r['narrative']).strip()}\n")

    # Supporting signals
    try:
        signals = json.loads(r.get("supporting_signals_json") or "[]")
        if signals:
            lines.append("### Supporting signals")
            for s in signals:
                lines.append(f"- {s}")
            lines.append("")
    except Exception:
        pass

    return "\n".join(lines) + "\n"


def _section_vrm(duck) -> str:
    lines = ["## 9. VRM — пълен текущ snapshot\n"]
    try:
        state = duck.execute(
            "SELECT * FROM vrm_state ORDER BY date DESC LIMIT 1"
        ).df()
        week = duck.execute(
            "SELECT * FROM vrm_week ORDER BY date DESC LIMIT 1"
        ).df()
    except Exception as e:
        lines.append(f"_Error: {e}_\n")
        return "\n".join(lines)

    if not state.empty:
        r = state.iloc[0]
        lines.append("### VRM_STATE (current)")
        lines.append("| Field | Value |")
        lines.append("|---|---|")
        for col in ("date", "regime", "ks_status", "alignment_score", "alignment_total",
                     "gms_value", "last_updated_md", "is_change_day"):
            val = r.get(col)
            if pd.notna(val):
                lines.append(f"| `{col}` | {val} |")
        lines.append("")

    if not week.empty:
        r = week.iloc[0]
        lines.append("### VRM_WEEK (current)")
        lines.append("| Field | Value |")
        lines.append("|---|---|")
        for col in ("date", "week_start", "week_end", "approved", "regime", "regime_bg",
                     "signal", "alignment", "alignment_max", "alignment_label",
                     "gms_score", "gms_max", "gms_label",
                     "ks_active", "ks_variant", "ks_weeks_active",
                     "ks_portfolio", "ks_eu_portfolio",
                     "spy_4w", "qqq_4w", "xle_4w", "gld_4w", "tlt_4w", "tip_4w", "iwm_4w"):
            val = r.get(col)
            if pd.notna(val):
                # Format pct fields
                if col.endswith("_4w") and isinstance(val, (int, float)):
                    lines.append(f"| `{col}` | {_fmt_pct(val)} |")
                else:
                    lines.append(f"| `{col}` | {val} |")
        lines.append("")
    return "\n".join(lines) + "\n"


def _section_rotation(duck, week: WeekWindow) -> str:
    lines = ["## 10. Rotation events — US + EU, пълни списъци\n"]
    for universe in ("us", "eu"):
        deltas = rotation_diff(duck, universe, week)
        if not deltas:
            continue
        lines.append(f"### {universe.upper()} (period: {deltas[0].a_date} → {deltas[0].b_date})\n")
        for d in deltas:
            if not d.entered and not d.exited:
                continue
            lines.append(f"**{d.quadrant} ({d.horizon}):** "
                         f"+{len(d.entered)} entered, -{len(d.exited)} exited")
            if d.entered:
                ft_marker = ""
                if d.first_time_ever:
                    ft_marker = f" _(включително {len(d.first_time_ever)} за първи път в историята: {', '.join(d.first_time_ever)})_"
                lines.append(f"  - **Entered:** {', '.join(d.entered)}{ft_marker}")
            if d.exited:
                lines.append(f"  - **Exited:** {', '.join(d.exited)}")
            lines.append("")
    return "\n".join(lines) + "\n"


def _section_cot(duck) -> str:
    lines = ["## 11. COT positioning — текуща картина (cot_monitor + cot_cta)\n"]
    for table_name, label in [("cot_positioning", "COT Monitor (38 markets)"),
                               ("cot_cta_positioning", "COT/CTA Positioning (11 markets)")]:
        try:
            df = duck.execute(
                f"SELECT * FROM {table_name} WHERE date = (SELECT max(date) FROM {table_name}) "
                f"ORDER BY percentile_5y DESC NULLS LAST"
            ).df()
        except Exception as e:
            lines.append(f"### {label}\n_Error: {e}_\n")
            continue
        if df.empty:
            lines.append(f"### {label}\n_Няма данни._\n")
            continue
        snapshot_date = df.iloc[0]["date"]
        lines.append(f"### {label} (snapshot: {snapshot_date})")
        lines.append("| Market | Asset class | Net position | Net % | Percentile 5y | Weekly change |")
        lines.append("|---|---|---:|---:|---:|---:|")
        for _, r in df.iterrows():
            lines.append(
                f"| **{r['market']}** | {r['asset_class']} | "
                f"{_fmt_num(r['net_position'], 0)} | "
                f"{_fmt_num(r['net_position_pct'], 1)} | "
                f"{_fmt_num(r['percentile_5y'], 1)} | "
                f"{_fmt_num(r['weekly_change'], 0)} |"
            )
        lines.append("")
    return "\n".join(lines) + "\n"


def _section_momentum_top(duck) -> str:
    lines = ["## 12. Momentum leaders (SP500 + STOXX600)\n"]
    for table_name, label in [("sp500_momentum", "SP500 momentum top 20"),
                               ("stoxx600_momentum", "STOXX600 momentum top 20")]:
        try:
            df = duck.execute(
                f"SELECT symbol, name, sector, momentum_score, return_1m, return_3m, "
                f"return_6m, return_12m, sharpe, drawdown, rank "
                f"FROM {table_name} WHERE date = (SELECT max(date) FROM {table_name}) "
                f"ORDER BY rank LIMIT 20"
            ).df()
        except Exception as e:
            lines.append(f"### {label}\n_Error: {e}_\n")
            continue
        if df.empty:
            continue
        lines.append(f"### {label}")
        lines.append("| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |")
        lines.append("|---:|---|---|---:|---:|---:|---:|---:|---:|---:|")
        for _, r in df.iterrows():
            lines.append(
                f"| {int(r['rank']) if pd.notna(r['rank']) else '-'} | "
                f"**{r['symbol']}** | {r['sector']} | "
                f"{_fmt_num(r['momentum_score'], 1)} | "
                f"{_fmt_num(r['return_1m'], 1)}% | {_fmt_num(r['return_3m'], 1)}% | "
                f"{_fmt_num(r['return_6m'], 1)}% | {_fmt_num(r['return_12m'], 1)}% | "
                f"{_fmt_num(r['sharpe'], 2)} | {_fmt_num(r['drawdown'], 1)}% |"
            )
        lines.append("")
    return "\n".join(lines) + "\n"


def _section_stock_selection(duck) -> str:
    lines = ["## 13. Stock Selection — top 15 + bottom 5 (composite score)\n"]
    try:
        top = duck.execute(
            "SELECT rank, ticker, name, sector, composite_score, trend_score, "
            "quality_score, value_score, risk_score, ret_52w, pe_ratio, roe "
            "FROM stock_selection WHERE date = (SELECT max(date) FROM stock_selection) "
            "ORDER BY rank LIMIT 15"
        ).df()
        bot = duck.execute(
            "SELECT rank, ticker, name, sector, composite_score, trend_score, "
            "quality_score, value_score, risk_score "
            "FROM stock_selection WHERE date = (SELECT max(date) FROM stock_selection) "
            "ORDER BY rank DESC LIMIT 5"
        ).df()
    except Exception as e:
        lines.append(f"_Error: {e}_\n")
        return "\n".join(lines)

    if not top.empty:
        lines.append("### Top 15 (composite score)")
        lines.append("| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |")
        lines.append("|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|")
        for _, r in top.iterrows():
            lines.append(
                f"| {int(r['rank'])} | **{r['ticker']}** | {r['sector']} | "
                f"{_fmt_num(r['composite_score'], 3)} | "
                f"{_fmt_num(r['trend_score'], 3)} | {_fmt_num(r['quality_score'], 3)} | "
                f"{_fmt_num(r['value_score'], 3)} | {_fmt_num(r['risk_score'], 3)} | "
                f"{_fmt_pct(r['ret_52w'], 1)} | "
                f"{_fmt_num(r['pe_ratio'], 1)} | {_fmt_pct(r['roe'], 1)} |"
            )
        lines.append("")
    if not bot.empty:
        lines.append("### Bottom 5 (worst composite score)")
        lines.append("| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |")
        lines.append("|---:|---|---|---:|---:|---:|---:|---:|")
        for _, r in bot.iterrows():
            lines.append(
                f"| {int(r['rank'])} | **{r['ticker']}** | {r['sector']} | "
                f"{_fmt_num(r['composite_score'], 3)} | "
                f"{_fmt_num(r['trend_score'], 3)} | {_fmt_num(r['quality_score'], 3)} | "
                f"{_fmt_num(r['value_score'], 3)} | {_fmt_num(r['risk_score'], 3)} |"
            )
        lines.append("")
    return "\n".join(lines) + "\n"


def _section_footer(week: WeekWindow) -> str:
    return (
        "## Mета — навигация и употреба\n\n"
        "**Този файл е comprehensive raw data dump за downstream AI агенти "
        "(parallel-thinking, deep research, custom workflows).** Не е narrative, "
        "не е bullet sheet. Структуриран за machine + human парсване.\n\n"
        "### Свързани сателитни артефакти\n\n"
        f"- **Structured briefing:** `briefings/{week.label}.md` — TLDR + 8 sections, ~10KB\n"
        f"- **Narrative briefing:** `briefings/narrative_{week.label}.md` — БГ prose за weekly-story-teller, ~5KB\n"
        "- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query\n"
        "- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/\n"
        "- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards\n\n"
        "### Регенериране\n\n"
        "```\n"
        "cd C:\\Projects\\dashboards\\macro-satellite\n"
        f"python -m macro_satellite export-week                      # current week\n"
        f"python -m macro_satellite export-week --week {week.week_start.isoformat()}  # anchor date\n"
        "```\n\n"
        "Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.\n"
    )


# ──────────────────────────────────────────────────────────────────────────
#  Top-level entry
# ──────────────────────────────────────────────────────────────────────────

def generate_full_export(target_week: WeekWindow | None = None,
                         output_dir: Path | None = None) -> tuple[str, Path]:
    duck = get_duck()
    week = target_week or current_week()
    log.info("full export start", extra={"week": week.label})

    sections = [
        _header(week),
        _section_etf_anomalies(duck, week),
        _section_divergence_patterns(duck, week),
        _section_parallels(duck, week),
        _section_backtests(duck, week),
        _section_persistent_macro(duck),
        _section_macro_state(duck, "US"),
        _section_macro_state(duck, "EU"),
        _section_macro_state(duck, "CN"),
        _section_vrm(duck),
        _section_rotation(duck, week),
        _section_cot(duck),
        _section_momentum_top(duck),
        _section_stock_selection(duck),
        _section_footer(week),
    ]
    md = "\n\n---\n\n".join(sections)

    out_dir = output_dir or (REPO_ROOT / "briefings")
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"data_export_{week.label}.md"
    path.write_text(md, encoding="utf-8")
    log.info("full export written", extra={"path": str(path),
                                            "size_kb": len(md) // 1024})
    return md, path
