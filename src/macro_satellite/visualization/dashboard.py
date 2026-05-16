"""Generate self-contained HTML dashboard.

Output: docs/index.html — single HTML file с inline Plotly данни. Готов за
GitHub Pages hosting.

Секции:
1. Текущо състояние — VRM + US + EU regime badges, дата на последния brief
2. Macro signature price chart — SPY/USO/GLD/TLT/UUP/XLE/IWM нормирани към 100
3. Weekly z-scores heatmap — symbols × weeks, color -3σ..+3σ
4. Macro lens scores timeline — US + EU 4 lenses
5. VRM timeline — regime + alignment + KS
6. Divergence pattern history — кои patterns са триггерирани кога
"""
from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

from ..analytics.divergence_engine import evaluate_all
from ..analytics.weekly_window import current_week, iso_week_for, trailing_weeks
from ..analytics.z_scores import scan_universe
from ..logging_setup import get_logger
from ..paths import REPO_ROOT
from ..storage.duckdb_conn import get_duck

log = get_logger(__name__)

# Signature за price chart — 7 core macro proxies
PRICE_CHART_SYMBOLS = ["SPY", "USO", "GLD", "TLT", "UUP", "XLE", "IWM"]
# Universe за weekly z-score heatmap
HEATMAP_SYMBOLS = ["USO", "XLE", "DFEN", "URA", "GLD", "TLT", "UUP", "SPY", "QQQ",
                   "IWM", "HYG", "LQD", "TIP", "DBC", "GDX", "SLV", "XLF", "XLK",
                   "XLV", "XLP", "XLE", "XLU"]
# Unique версия
HEATMAP_SYMBOLS = list(dict.fromkeys(HEATMAP_SYMBOLS))


def _load_etf_prices_long(duck, symbols: list[str], since: date) -> pd.DataFrame:
    placeholders = ",".join(["?"] * len(symbols))
    sql = (f"SELECT date, symbol, price FROM etf_prices "
           f"WHERE symbol IN ({placeholders}) AND price IS NOT NULL "
           f"AND date >= ? ORDER BY symbol, date")
    df = duck.execute(sql, list(symbols) + [since]).df()
    if df.empty:
        return df
    df["date"] = pd.to_datetime(df["date"])
    return df


def _section_current_state(duck) -> str:
    """Top section — regime badges + last update info."""
    parts = ['<section class="card current-state">',
             '<h2>📡 Текущо състояние</h2>',
             '<div class="badges">']

    # VRM
    try:
        vrm = duck.execute(
            "SELECT date, regime, ks_status, alignment_score, alignment_total "
            "FROM vrm_state ORDER BY date DESC LIMIT 1"
        ).df()
        if not vrm.empty:
            r = vrm.iloc[0]
            ks_cls = "active" if str(r["ks_status"]).lower() == "active" else "inactive"
            al = f"{float(r['alignment_score']):.1f}/{int(r['alignment_total'])}" if pd.notna(r["alignment_score"]) else "?"
            parts.append(
                f'<div class="badge vrm"><div class="badge-label">VRM</div>'
                f'<div class="badge-value">{r["regime"]}</div>'
                f'<div class="badge-sub">KS: <span class="ks-{ks_cls}">{r["ks_status"]}</span> · Alignment {al}</div></div>'
            )
    except Exception:
        pass

    # US macro
    try:
        us = duck.execute(
            "SELECT regime_key, regime_label_bg, primary_driver FROM us_macro_state "
            "ORDER BY date DESC LIMIT 1"
        ).df()
        if not us.empty:
            r = us.iloc[0]
            parts.append(
                f'<div class="badge us"><div class="badge-label">🇺🇸 US Macro</div>'
                f'<div class="badge-value">{r["regime_label_bg"]}</div>'
                f'<div class="badge-sub">{r["regime_key"]} · driver: {r["primary_driver"]}</div></div>'
            )
    except Exception:
        pass

    # EU macro
    try:
        eu = duck.execute(
            "SELECT regime_key, regime_label_bg, primary_driver FROM eu_macro_state "
            "ORDER BY date DESC LIMIT 1"
        ).df()
        if not eu.empty:
            r = eu.iloc[0]
            parts.append(
                f'<div class="badge eu"><div class="badge-label">🇪🇺 EU Macro</div>'
                f'<div class="badge-value">{r["regime_label_bg"]}</div>'
                f'<div class="badge-sub">{r["regime_key"]} · driver: {r["primary_driver"]}</div></div>'
            )
    except Exception:
        pass

    parts.append('</div></section>')
    return "\n".join(parts)


def _chart_price_signature(duck, since: date) -> str:
    """Normalized price chart (всеки symbol → 100 at start)."""
    df = _load_etf_prices_long(duck, PRICE_CHART_SYMBOLS, since)
    if df.empty:
        return '<section class="card"><h2>Macro signature</h2><p>Няма данни.</p></section>'

    fig = go.Figure()
    for sym in PRICE_CHART_SYMBOLS:
        sub = df[df["symbol"] == sym].sort_values("date")
        if sub.empty:
            continue
        base = sub.iloc[0]["price"]
        if base <= 0:
            continue
        normalized = (sub["price"] / base) * 100
        fig.add_trace(go.Scatter(
            x=sub["date"], y=normalized, mode="lines", name=sym,
            hovertemplate=f"<b>{sym}</b><br>%{{x|%Y-%m-%d}}: %{{y:.1f}}<extra></extra>",
        ))
    fig.update_layout(
        height=480, margin=dict(l=40, r=20, t=10, b=40),
        xaxis_title="Дата", yaxis_title="Normalized (start = 100)",
        legend=dict(orientation="h", y=-0.15),
        template="plotly_white",
        hovermode="x unified",
    )
    chart_html = pio.to_html(fig, include_plotlyjs=False, full_html=False,
                              div_id="price-chart")
    return (
        '<section class="card">'
        '<h2>📈 Macro signature (нормирано към 100)</h2>'
        '<p class="hint">Топ 7 ETF в satellite signature: '
        + ", ".join(PRICE_CHART_SYMBOLS) + '. Hover за конкретни стойности.</p>'
        + chart_html + '</section>'
    )


def _chart_zscore_heatmap(duck, n_weeks: int = 13) -> str:
    """Heatmap: symbols × weeks, color -3σ..+3σ.

    Batch approach: 1 SQL за всички цени → pandas weekly resample → rolling z-score.
    """
    target = current_week()
    weeks = trailing_weeks(target, n_weeks)[::-1] + [target]
    week_labels = [w.label for w in weeks]
    week_end_ts = [pd.Timestamp(w.week_end) for w in weeks]

    # Batch load всички prices за heatmap symbols
    placeholders = ",".join(["?"] * len(HEATMAP_SYMBOLS))
    earliest = min(w.week_start for w in weeks) - timedelta(weeks=20)
    sql = (f"SELECT date, symbol, price FROM etf_prices "
           f"WHERE symbol IN ({placeholders}) AND price IS NOT NULL "
           f"AND date >= ? ORDER BY date")
    df = duck.execute(sql, list(HEATMAP_SYMBOLS) + [earliest]).df()
    if df.empty:
        return '<section class="card"><h2>Z-scores</h2><p>Няма данни.</p></section>'
    df["date"] = pd.to_datetime(df["date"])

    # Pivot → wide, resample weekly (W-SUN), pct_change
    wide = df.pivot_table(index="date", columns="symbol", values="price", aggfunc="last")
    weekly = wide.resample("W-SUN").last().ffill(limit=1)
    returns = weekly.pct_change()

    # За всеки таргет week → z-score = (return - rolling 13w mean) / rolling 13w std
    rolling_mean = returns.shift(1).rolling(window=13, min_periods=4).mean()
    rolling_std = returns.shift(1).rolling(window=13, min_periods=4).std()
    z_matrix = (returns - rolling_mean) / rolling_std

    # Subset target weeks
    target_z = z_matrix.reindex(week_end_ts, method="ffill")  # most-recent index <= each target

    # Build matrix in HEATMAP_SYMBOLS order
    z = np.full((len(HEATMAP_SYMBOLS), len(week_labels)), np.nan)
    for i, sym in enumerate(HEATMAP_SYMBOLS):
        if sym not in target_z.columns:
            continue
        for j, _ in enumerate(week_end_ts):
            v = target_z.iloc[j].get(sym)
            if pd.notna(v) and np.isfinite(v):
                z[i, j] = float(v)

    fig = go.Figure(data=go.Heatmap(
        z=z, x=week_labels, y=HEATMAP_SYMBOLS,
        colorscale="RdBu_r", zmin=-3, zmax=3, zmid=0,
        colorbar=dict(title="z-score"),
        hovertemplate="<b>%{y}</b><br>%{x}: z=%{z:.2f}<extra></extra>",
    ))
    fig.update_layout(
        height=560, margin=dict(l=60, r=20, t=10, b=60),
        xaxis_title="Седмица", yaxis_title="Symbol",
        template="plotly_white",
    )
    chart_html = pio.to_html(fig, include_plotlyjs=False, full_html=False,
                              div_id="zscore-heatmap")
    return (
        '<section class="card">'
        '<h2>🌡️ Weekly z-scores heatmap</h2>'
        f'<p class="hint">Последните {n_weeks + 1} седмици vs trailing 13w distribution. '
        'Тъмно червено = силно нагоре, тъмно синьо = силно надолу.</p>'
        + chart_html + '</section>'
    )


def _chart_macro_lenses(duck) -> str:
    """4 lens scores за US + EU в 2 subplots."""
    fig = make_subplots(rows=1, cols=2, subplot_titles=("🇺🇸 US lenses", "🇪🇺 EU lenses"),
                         shared_yaxes=True)
    lens_colors = {"labor": "#1f77b4", "growth": "#2ca02c",
                   "inflation": "#d62728", "liquidity": "#9467bd"}
    for col_idx, region in enumerate(["US", "EU"], start=1):
        table = f"{region.lower()}_macro_state"
        try:
            df = duck.execute(
                f"SELECT date, labor_score, growth_score, inflation_score, liquidity_score "
                f"FROM {table} ORDER BY date"
            ).df()
            if df.empty:
                continue
            df["date"] = pd.to_datetime(df["date"])
            for lens in ("labor", "growth", "inflation", "liquidity"):
                col = f"{lens}_score"
                if col not in df.columns or df[col].isna().all():
                    continue
                fig.add_trace(go.Scatter(
                    x=df["date"], y=df[col], mode="lines+markers",
                    name=f"{region} {lens}", legendgroup=region,
                    line=dict(color=lens_colors[lens]),
                    showlegend=(col_idx == 1),
                    hovertemplate=f"<b>{region} {lens}</b><br>%{{x|%Y-%m-%d}}: %{{y:.1f}}<extra></extra>",
                ), row=1, col=col_idx)
        except Exception as e:
            log.warning("macro lens plot failed", extra={"region": region, "error": str(e)})
    fig.update_layout(
        height=420, margin=dict(l=40, r=20, t=40, b=40),
        template="plotly_white",
        legend=dict(orientation="h", y=-0.2),
    )
    chart_html = pio.to_html(fig, include_plotlyjs=False, full_html=False,
                              div_id="macro-lenses")
    return (
        '<section class="card">'
        '<h2>🔬 Macro lens scores (US + EU)</h2>'
        '<p class="hint">4 лещи (labor / growth / inflation / liquidity) per regio. '
        'Score 0-100, по-високо = по-силно положителен сигнал.</p>'
        + chart_html + '</section>'
    )


def _chart_vrm_timeline(duck) -> str:
    try:
        df = duck.execute(
            "SELECT date, regime, ks_status, alignment_score FROM vrm_state ORDER BY date"
        ).df()
    except Exception:
        return ""
    if df.empty:
        return ""
    df["date"] = pd.to_datetime(df["date"])
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                         row_heights=[0.6, 0.4],
                         subplot_titles=("Alignment score", "KS статус / Режим"))
    fig.add_trace(go.Scatter(
        x=df["date"], y=df["alignment_score"], mode="lines+markers",
        name="Alignment", line=dict(color="#1f77b4", width=3),
    ), row=1, col=1)
    # KS as colored bar background — simplified as scatter markers
    ks_colors = df["ks_status"].apply(lambda x: "red" if str(x).lower() == "active" else "green")
    fig.add_trace(go.Scatter(
        x=df["date"], y=[1]*len(df), mode="markers",
        marker=dict(color=ks_colors, size=12),
        text=df["regime"], hovertemplate="<b>%{x|%Y-%m-%d}</b><br>Регим: %{text}<br>KS: %{customdata}<extra></extra>",
        customdata=df["ks_status"],
        name="KS / Режим", showlegend=False,
    ), row=2, col=1)
    fig.update_layout(
        height=420, margin=dict(l=40, r=20, t=40, b=40),
        template="plotly_white", showlegend=False,
    )
    fig.update_yaxes(title_text="Score", row=1, col=1)
    fig.update_yaxes(visible=False, row=2, col=1)
    chart_html = pio.to_html(fig, include_plotlyjs=False, full_html=False,
                              div_id="vrm-timeline")
    return (
        '<section class="card">'
        '<h2>⚙️ VRM timeline</h2>'
        '<p class="hint">Alignment score над времето. Зелени точки = KS inactive, '
        'червени = KS active. Hover за regime.</p>'
        + chart_html + '</section>'
    )


def _chart_divergence_history(duck, n_weeks: int = 13) -> str:
    """За всяка от последните N седмици → колко patterns са триггерирали."""
    target = current_week()
    weeks = trailing_weeks(target, n_weeks)[::-1] + [target]
    rows = []
    for w in weeks:
        hits = evaluate_all(w.week_end, duck)
        triggered = [h for h in hits if h.triggered]
        for h in triggered:
            rows.append({"week": w.label, "pattern": h.label_bg, "n_matched": h.n_matched})
    if not rows:
        return ('<section class="card"><h2>🔔 Divergence patterns history</h2>'
                '<p>Никой канонична pattern не се триггерира в последните седмици.</p></section>')
    df = pd.DataFrame(rows)
    # Pivot to wide for stacked bar
    pivot = df.pivot_table(index="week", columns="pattern", values="n_matched",
                           aggfunc="max", fill_value=0)
    fig = go.Figure()
    for col in pivot.columns:
        fig.add_trace(go.Bar(x=pivot.index, y=pivot[col], name=col))
    fig.update_layout(
        height=380, margin=dict(l=40, r=20, t=10, b=40),
        barmode="stack", template="plotly_white",
        xaxis_title="Седмица", yaxis_title="Conditions matched",
        legend=dict(orientation="h", y=-0.2),
    )
    chart_html = pio.to_html(fig, include_plotlyjs=False, full_html=False,
                              div_id="divergence-history")
    return (
        '<section class="card">'
        '<h2>🔔 Divergence patterns history (последни {} седмици)</h2>'.format(n_weeks + 1)
        + '<p class="hint">Триггерирани patterns per седмица, color-coded.</p>'
        + chart_html + '</section>'
    )


def _section_latest_briefing(duck) -> str:
    """Чете последния narrative briefing и embed-ва TLDR + thesis."""
    target = current_week()
    path = REPO_ROOT / "briefings" / f"narrative_{target.label}.md"
    if not path.exists():
        # fallback: structured briefing
        path = REPO_ROOT / "briefings" / f"{target.label}.md"
    if not path.exists():
        return ""
    content = path.read_text(encoding="utf-8")
    # Take first ~2000 chars (header + thesis + evidence start)
    excerpt = content[:2500]
    if len(content) > 2500:
        excerpt += "\n\n_... (виж пълния briefing в repo-то)_"
    # Convert markdown to HTML (minimal: just preserve as preformatted with basic escapes)
    import html
    body = html.escape(excerpt)
    return (
        '<section class="card briefing-excerpt">'
        f'<h2>📋 Последен briefing — {target.label}</h2>'
        f'<a href="https://github.com/tsvetoslavtsachev/macro-satellite/blob/main/briefings/narrative_{target.label}.md" '
        'class="link-external">Целият narrative briefing →</a>'
        '<pre>' + body + '</pre>'
        '</section>'
    )


def _build_html(sections: list[str]) -> str:
    generated_at = pd.Timestamp.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    return f"""<!DOCTYPE html>
<html lang="bg">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>macro-satellite · Сателитен Dashboard</title>
<script src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>
<style>
:root {{
  --bg: #f7f7f8;
  --card-bg: #ffffff;
  --border: #e5e7eb;
  --text: #1f2937;
  --muted: #6b7280;
  --accent: #2563eb;
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background: var(--bg); color: var(--text); line-height: 1.5;
}}
header {{
  background: white; border-bottom: 1px solid var(--border); padding: 16px 32px;
}}
header h1 {{ margin: 0; font-size: 22px; }}
header .meta {{ color: var(--muted); font-size: 13px; margin-top: 4px; }}
header .links a {{ color: var(--accent); text-decoration: none; margin-right: 16px; font-size: 13px; }}
main {{ max-width: 1280px; margin: 0 auto; padding: 24px; }}
.card {{
  background: var(--card-bg); border: 1px solid var(--border); border-radius: 8px;
  padding: 20px; margin-bottom: 20px;
}}
.card h2 {{ margin-top: 0; margin-bottom: 12px; font-size: 18px; }}
.hint {{ color: var(--muted); font-size: 13px; margin-bottom: 12px; }}
.badges {{ display: flex; flex-wrap: wrap; gap: 16px; }}
.badge {{
  flex: 1 1 200px; background: #f9fafb; border-left: 4px solid var(--accent);
  padding: 12px 16px; border-radius: 4px;
}}
.badge-label {{ color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em; }}
.badge-value {{ font-size: 18px; font-weight: 600; margin-top: 4px; }}
.badge-sub {{ color: var(--muted); font-size: 12px; margin-top: 4px; }}
.badge.vrm {{ border-left-color: #2563eb; }}
.badge.us {{ border-left-color: #dc2626; }}
.badge.eu {{ border-left-color: #2563eb; }}
.ks-active {{ color: #dc2626; font-weight: 600; }}
.ks-inactive {{ color: #16a34a; }}
.link-external {{ color: var(--accent); text-decoration: none; font-size: 13px; display: inline-block; margin-bottom: 10px; }}
.briefing-excerpt pre {{
  background: #f9fafb; border: 1px solid var(--border); border-radius: 4px;
  padding: 16px; font-size: 13px; line-height: 1.5; overflow-x: auto;
  white-space: pre-wrap; word-wrap: break-word;
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
}}
footer {{
  text-align: center; padding: 24px; color: var(--muted); font-size: 12px;
  border-top: 1px solid var(--border); margin-top: 24px;
}}
footer a {{ color: var(--accent); text-decoration: none; }}
</style>
</head>
<body>
<header>
  <h1>📡 macro-satellite · Сателитен Dashboard</h1>
  <div class="meta">Автоматично генериран {generated_at} · 12 dashboards · daily collect 07:00 София</div>
  <div class="links" style="margin-top: 8px;">
    <a href="https://github.com/tsvetoslavtsachev/macro-satellite">GitHub repo</a>
    <a href="https://github.com/tsvetoslavtsachev/macro-satellite/tree/main/briefings">Briefings</a>
    <a href="https://github.com/tsvetoslavtsachev/macro-satellite/actions">Workflow runs</a>
  </div>
</header>
<main>
{chr(10).join(sections)}
</main>
<footer>
  Generated by <a href="https://github.com/tsvetoslavtsachev/macro-satellite">macro-satellite</a>.
  Daily collect + weekly briefing + interactive viz. Data via Parquet + DuckDB.
</footer>
</body>
</html>
"""


def generate_dashboard(output_dir: Path | None = None,
                       price_history_days: int = 365 * 3,
                       heatmap_weeks: int = 13) -> Path:
    """Генерира docs/index.html."""
    duck = get_duck()
    out_dir = output_dir or (REPO_ROOT / "docs")
    out_dir.mkdir(parents=True, exist_ok=True)
    since = date.today() - timedelta(days=price_history_days)

    log.info("dashboard generate start")
    sections = [
        _section_current_state(duck),
        _section_latest_briefing(duck),
        _chart_price_signature(duck, since),
        _chart_zscore_heatmap(duck, n_weeks=heatmap_weeks),
        _chart_macro_lenses(duck),
        _chart_vrm_timeline(duck),
        _chart_divergence_history(duck, n_weeks=heatmap_weeks),
    ]
    html = _build_html(sections)
    path = out_dir / "index.html"
    path.write_text(html, encoding="utf-8")
    log.info("dashboard written", extra={"path": str(path), "size_kb": len(html) // 1024})
    return path
