"""Generate self-contained HTML dashboard.

Output: docs/index.html — single HTML file с inline Plotly данни. Готов за
GitHub Pages hosting. Pairs с docs/state.json за AI consumption.

Layout:
1. Hero — VRM/US/EU режими + TL;DR от briefing + триггерирани patterns
2. 4w focus — price signature normalized (4 седмици), top movements таблица,
   pattern conditions detail
3. 13w context — z-score heatmap, macro lens scores, divergence patterns history
4. VRM timeline — alignment score с KS shaded bands (поправено)
5. Top 3 исторически паралели
6. Линкове + state.json

Този модул преизползва state_export.build_state_bundle() — без двойно дърпане.
"""
from __future__ import annotations

import math
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

from ..analytics.weekly_window import current_week, trailing_weeks
from ..logging_setup import get_logger
from ..paths import REPO_ROOT
from ..storage.duckdb_conn import get_duck
from .md_renderer import render_briefing_full_link_block, render_briefing_hero
from .state_export import (
    HEATMAP_SYMBOLS,
    StateBundle,
    build_state_bundle,
    write_state_json,
)

log = get_logger(__name__)

# Signature за price chart — 7 core macro proxies.
PRICE_CHART_SYMBOLS = ["SPY", "USO", "GLD", "TLT", "UUP", "XLE", "IWM"]

# Lookback windows (in calendar days).
SHORT_WINDOW_DAYS = 28           # ~4 weeks
MEDIUM_WINDOW_DAYS = 91          # ~13 weeks

PLOTLY_CDN = "https://cdn.plot.ly/plotly-2.32.0.min.js"


# ────────────────────────────────────────────────────────────────────────────
#  Data helpers
# ────────────────────────────────────────────────────────────────────────────

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


def _fmt_signed_pct(x: float | None, decimals: int = 1) -> str:
    if x is None or (isinstance(x, float) and not math.isfinite(x)):
        return "—"
    return f"{x:+.{decimals}f}%"


def _fmt_z(z: float | None) -> str:
    if z is None or (isinstance(z, float) and not math.isfinite(z)):
        return "—"
    return f"{z:+.2f}σ"


# ────────────────────────────────────────────────────────────────────────────
#  Hero section — current state + briefing TL;DR + triggered patterns
# ────────────────────────────────────────────────────────────────────────────

def _section_hero(bundle: StateBundle) -> str:
    parts: list[str] = []

    # ──── Regime badges ────
    badge_html = ['<div class="badges">']
    vrm = bundle.regimes.get("vrm")
    if vrm:
        ks_status = str(vrm.get("ks_status") or "").lower()
        ks_cls = "active" if ks_status == "active" else "inactive"
        al_score = vrm.get("alignment_score")
        al_total = vrm.get("alignment_total")
        if al_score is not None and al_total is not None:
            al_str = f"{float(al_score):.1f}/{int(al_total)}"
        else:
            al_str = "?"
        badge_html.append(
            f'<div class="badge vrm">'
            f'<div class="badge-label">VRM</div>'
            f'<div class="badge-value">{vrm.get("regime", "?")}</div>'
            f'<div class="badge-sub">KS: <span class="ks-{ks_cls}">{vrm.get("ks_status", "?")}</span>'
            f' · Alignment {al_str}</div></div>'
        )
    us = bundle.regimes.get("us_macro")
    if us:
        badge_html.append(
            f'<div class="badge us">'
            f'<div class="badge-label">🇺🇸 US Macro</div>'
            f'<div class="badge-value">{us.get("regime_label_bg") or us.get("regime_key") or "?"}</div>'
            f'<div class="badge-sub">{us.get("regime_key") or "?"} · driver: {us.get("primary_driver") or "—"}</div></div>'
        )
    eu = bundle.regimes.get("eu_macro")
    if eu:
        badge_html.append(
            f'<div class="badge eu">'
            f'<div class="badge-label">🇪🇺 EU Macro</div>'
            f'<div class="badge-value">{eu.get("regime_label_bg") or eu.get("regime_key") or "?"}</div>'
            f'<div class="badge-sub">{eu.get("regime_key") or "?"} · driver: {eu.get("primary_driver") or "—"}</div></div>'
        )
    badge_html.append('</div>')

    # ──── Triggered patterns chips ────
    triggered = bundle.triggered_patterns
    if triggered:
        chips = ['<div class="triggered-chips">']
        for p in triggered:
            chips.append(
                f'<a href="#patterns-detail" class="chip chip-alert">'
                f'🔔 {p["label_bg"]} <span class="chip-count">{p["n_matched"]}/{p["n_total"]}</span>'
                f'</a>'
            )
        chips.append('</div>')
        triggered_html = "\n".join(chips)
    else:
        triggered_html = '<p class="hint">Никой канонична pattern не се триггерира тази седмица.</p>'

    # ──── Briefing hero (rendered markdown, not <pre>) ────
    narrative_path = REPO_ROOT / "briefings" / f"narrative_{bundle.week.label}.md"
    structured_path = REPO_ROOT / "briefings" / f"{bundle.week.label}.md"
    briefing_html = render_briefing_hero(narrative_path, structured_path)
    link_block = render_briefing_full_link_block(narrative_path, structured_path,
                                                  bundle.week.label)

    parts.append('<section class="card hero">')
    parts.append(f'<h2>📡 Тази седмица — {bundle.week.label} '
                 f'<span class="date-range">({bundle.week.week_start} → {bundle.week.week_end})</span></h2>')
    parts.append("\n".join(badge_html))
    parts.append('<h3 style="margin-top: 20px;">🔔 Триггерирани patterns</h3>')
    parts.append(triggered_html)
    parts.append('<h3 style="margin-top: 24px;">📋 Теза + TL;DR</h3>')
    parts.append('<div class="briefing-hero">')
    parts.append(briefing_html)
    parts.append('</div>')
    if link_block:
        parts.append(link_block)
    parts.append('</section>')

    return "\n".join(parts)


# ────────────────────────────────────────────────────────────────────────────
#  Section 2: 4-week focus
# ────────────────────────────────────────────────────────────────────────────

def _chart_price_signature(duck, since: date, label: str,
                            div_id: str) -> str:
    df = _load_etf_prices_long(duck, PRICE_CHART_SYMBOLS, since)
    if df.empty:
        return f'<div class="hint">Няма данни за {label}.</div>'

    fig = go.Figure()
    for sym in PRICE_CHART_SYMBOLS:
        sub = df[df["symbol"] == sym].sort_values("date")
        if sub.empty:
            continue
        base = sub.iloc[0]["price"]
        if base <= 0:
            continue
        normalized = (sub["price"] / base) * 100.0
        fig.add_trace(go.Scatter(
            x=sub["date"], y=normalized, mode="lines", name=sym,
            hovertemplate=f"<b>{sym}</b><br>%{{x|%Y-%m-%d}}: %{{y:.1f}}<extra></extra>",
        ))
    fig.update_layout(
        height=420, margin=dict(l=40, r=20, t=10, b=40),
        xaxis_title="Дата", yaxis_title="Normalized (start = 100)",
        legend=dict(orientation="h", y=-0.18),
        template="plotly_white",
        hovermode="x unified",
    )
    return pio.to_html(fig, include_plotlyjs=False, full_html=False,
                       div_id=div_id)


def _table_week_movements(bundle: StateBundle) -> str:
    movs = bundle.week_movements_etf
    if not movs:
        return ('<p class="hint">Нищо забележимо: никой ETF не премина '
                '|z|≥1.5σ спрямо последните 13 седмици.</p>')

    rows: list[str] = []
    rows.append(
        '<table class="tbl moves"><thead><tr>'
        '<th>Symbol</th><th class="num">% седмично</th><th class="num">z-score</th>'
        '<th class="num">Цена</th><th>Период</th>'
        '</tr></thead><tbody>'
    )
    for m in movs:
        pct = m.get("weekly_change_pct")
        z = m.get("z_score")
        pa, pb = m.get("price_a"), m.get("price_b")
        da, db = m.get("date_a"), m.get("date_b")
        direction_cls = ("up" if (pct or 0) > 0 else "down" if (pct or 0) < 0 else "")
        price_str = f"{pa:.2f} → {pb:.2f}" if (pa is not None and pb is not None) else "—"
        period_str = f"{da or '?'} → {db or '?'}"
        rows.append(
            f'<tr>'
            f'<td class="sym">{m["symbol"]}</td>'
            f'<td class="num {direction_cls}">{_fmt_signed_pct(pct)}</td>'
            f'<td class="num {direction_cls}">{_fmt_z(z)}</td>'
            f'<td class="num">{price_str}</td>'
            f'<td class="muted">{period_str}</td>'
            f'</tr>'
        )
    rows.append('</tbody></table>')
    return "\n".join(rows)


def _section_pattern_details(bundle: StateBundle) -> str:
    triggered = bundle.triggered_patterns
    if not triggered:
        return ""

    parts: list[str] = []
    parts.append('<section class="card" id="patterns-detail">')
    parts.append('<h2>🔔 Conditions detail за триггерираните patterns</h2>')
    for p in triggered:
        parts.append(f'<div class="pattern-block">')
        parts.append(f'<h3>{p["label_bg"]} <span class="muted">({p["n_matched"]}/{p["n_total"]} условия)</span></h3>')
        if p.get("description"):
            parts.append(f'<p class="muted small">{p["description"]}</p>')
        parts.append(f'<p class="hint">Window: {p["window_days"]} дни, end {p["end_date"]}</p>')
        parts.append('<ul class="conditions">')
        for c in p["conditions"]:
            mark = "✓" if c["matched"] else "✗"
            mark_cls = "match" if c["matched"] else "miss"
            actual = c.get("actual_change_pct")
            actual_str = (f"{actual:+.2f}%" if actual is not None else "no data")
            parts.append(
                f'<li class="cond {mark_cls}">'
                f'<span class="mark">{mark}</span> '
                f'<b>{c["symbol"]}</b>: {actual_str} '
                f'<span class="muted">(target {c["target_direction"]} ≥ {c["target_min_pct"]}%)</span>'
                f'</li>'
            )
        parts.append('</ul>')
        parts.append('</div>')
    parts.append('</section>')
    return "\n".join(parts)


def _section_4w_focus(duck, bundle: StateBundle) -> str:
    since = bundle.week.week_end - timedelta(days=SHORT_WINDOW_DAYS)
    price_html = _chart_price_signature(duck, since,
                                         "4-седмичен изглед", "price-chart-4w")
    moves_html = _table_week_movements(bundle)

    return (
        '<section class="card">'
        '<h2>📈 4 седмици — какво се случи последно</h2>'
        '<p class="hint">7 macro ETF, normalized към 100 в началото на прозореца. '
        'Таблицата отдолу е официалният списък ETF движения с |z|≥1.5σ спрямо предишните 13 седмици.</p>'
        '<h3>Macro signature</h3>'
        + price_html +
        '<h3 style="margin-top: 24px;">Топ ETF движения тази седмица</h3>'
        + moves_html +
        '</section>'
    )


# ────────────────────────────────────────────────────────────────────────────
#  Section 3: 13-week context — heatmap + macro lenses + divergence history
# ────────────────────────────────────────────────────────────────────────────

def _chart_zscore_heatmap_from_bundle(bundle: StateBundle) -> str:
    """Heatmap от вече-извлечените z-scores в bundle. БЕЗ ffill — None клетки
    се визуализират като сиво."""
    hm = bundle.z_heatmap
    symbols = hm.get("symbols", [])
    weeks = hm.get("weeks", [])
    matrix = hm.get("matrix", [])
    if not symbols or not weeks or not matrix:
        return '<p class="hint">Няма данни за z-score heatmap.</p>'

    # Convert None → np.nan за plotly
    z = np.array([
        [(v if v is not None else np.nan) for v in row]
        for row in matrix
    ], dtype=float)

    fig = go.Figure(data=go.Heatmap(
        z=z, x=weeks, y=symbols,
        colorscale="RdBu_r", zmin=-3, zmax=3, zmid=0,
        colorbar=dict(title="z-score"),
        hovertemplate="<b>%{y}</b><br>%{x}: z=%{z:.2f}<extra></extra>",
        hoverongaps=False,                # сиво за NaN, no hover
    ))
    fig.update_layout(
        height=560, margin=dict(l=60, r=20, t=10, b=60),
        xaxis_title="Седмица", yaxis_title="Symbol",
        template="plotly_white",
    )
    return pio.to_html(fig, include_plotlyjs=False, full_html=False,
                       div_id="zscore-heatmap")


def _chart_macro_lenses(duck) -> str:
    """4 lens scores за US + EU в 2 subplots, 13w window."""
    fig = make_subplots(rows=1, cols=2, subplot_titles=("🇺🇸 US lenses", "🇪🇺 EU lenses"),
                         shared_yaxes=True)
    lens_colors = {"labor": "#1f77b4", "growth": "#2ca02c",
                   "inflation": "#d62728", "liquidity": "#9467bd"}
    cutoff = date.today() - timedelta(days=MEDIUM_WINDOW_DAYS)
    any_data = False
    for col_idx, region in enumerate(["US", "EU"], start=1):
        table = f"{region.lower()}_macro_state"
        try:
            df = duck.execute(
                f"SELECT date, labor_score, growth_score, inflation_score, liquidity_score "
                f"FROM {table} WHERE date >= ? ORDER BY date",
                [cutoff],
            ).df()
        except Exception as e:
            log.warning("macro lens load failed", extra={"region": region, "error": str(e)})
            continue
        if df.empty:
            continue
        any_data = True
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
    if not any_data:
        return '<p class="hint">Няма данни за macro lens scores.</p>'
    fig.update_layout(
        height=420, margin=dict(l=40, r=20, t=40, b=40),
        template="plotly_white",
        legend=dict(orientation="h", y=-0.2),
    )
    fig.update_yaxes(range=[0, 100])
    return pio.to_html(fig, include_plotlyjs=False, full_html=False,
                       div_id="macro-lenses")


def _chart_divergence_history(duck, target_week, n_weeks: int = 13) -> str:
    """За всяка от последните N+1 седмици → колко conditions matched за всеки pattern.

    Stacked bar. Преизползва divergence_engine.evaluate_all (N+1 заявки).
    """
    from ..analytics.divergence_engine import evaluate_all
    weeks = trailing_weeks(target_week, n_weeks) + [target_week]

    rows = []
    for w in weeks:
        hits = evaluate_all(w.week_end, duck)
        for h in hits:
            if h.n_matched > 0:
                rows.append({
                    "week": w.label,
                    "pattern": h.label_bg,
                    "n_matched": h.n_matched,
                    "triggered": h.triggered,
                })
    if not rows:
        return ('<p class="hint">Никой канонична pattern не получи дори частично '
                f'съвпадение в последните {n_weeks + 1} седмици.</p>')
    df = pd.DataFrame(rows)
    pivot = df.pivot_table(index="week", columns="pattern", values="n_matched",
                           aggfunc="max", fill_value=0)
    pivot = pivot.reindex([w.label for w in weeks])

    fig = go.Figure()
    for col in pivot.columns:
        fig.add_trace(go.Bar(x=pivot.index, y=pivot[col], name=col))
    fig.update_layout(
        height=380, margin=dict(l=40, r=20, t=10, b=40),
        barmode="stack", template="plotly_white",
        xaxis_title="Седмица", yaxis_title="Conditions matched (max)",
        legend=dict(orientation="h", y=-0.25),
    )
    return pio.to_html(fig, include_plotlyjs=False, full_html=False,
                       div_id="divergence-history")


def _section_13w_context(duck, bundle: StateBundle) -> str:
    heatmap_html = _chart_zscore_heatmap_from_bundle(bundle)
    lenses_html = _chart_macro_lenses(duck)
    div_history_html = _chart_divergence_history(duck, bundle.week, n_weeks=13)

    return (
        '<section class="card">'
        '<h2>🌡️ 13 седмици — контекст</h2>'
        '<p class="hint">Среден хоризонт: z-scores срещу 13-седмично разпределение, '
        'macro lens scores, история на pattern triggerings.</p>'
        '<h3>Weekly z-scores (последните 14 седмици)</h3>'
        '<p class="hint">Сиво = недостатъчно baseline за z-score. Тъмно червено = силно нагоре, '
        'тъмно синьо = силно надолу.</p>'
        + heatmap_html +
        '<h3 style="margin-top: 24px;">Macro lens scores (US + EU)</h3>'
        '<p class="hint">4 лещи per regio. Score 0-100; по-високо = по-силно положителен сигнал.</p>'
        + lenses_html +
        '<h3 style="margin-top: 24px;">Divergence pattern history</h3>'
        '<p class="hint">Stacked bar: conditions matched per pattern, per седмица. '
        '5/5 = pattern триггериран.</p>'
        + div_history_html +
        '</section>'
    )


# ────────────────────────────────────────────────────────────────────────────
#  Section 4: VRM timeline — поправен (KS as shaded bands, no phantom subplot)
# ────────────────────────────────────────────────────────────────────────────

def _chart_vrm_timeline(duck) -> str:
    try:
        df = duck.execute(
            "SELECT date, regime, ks_status, alignment_score, alignment_total "
            "FROM vrm_state ORDER BY date"
        ).df()
    except Exception as e:
        log.warning("vrm timeline load failed", extra={"error": str(e)})
        return ""
    if df.empty:
        return ""
    df["date"] = pd.to_datetime(df["date"])

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["date"], y=df["alignment_score"],
        mode="lines+markers",
        name="Alignment score",
        line=dict(color="#1f77b4", width=3),
        customdata=np.stack([df["regime"].fillna("?"),
                             df["ks_status"].fillna("?")], axis=-1),
        hovertemplate=("<b>%{x|%Y-%m-%d}</b><br>"
                       "Alignment: %{y:.1f}<br>"
                       "Регим: %{customdata[0]}<br>"
                       "KS: %{customdata[1]}<extra></extra>"),
    ))

    # KS active интервали → shaded vrect bands
    df["_ks_active"] = df["ks_status"].fillna("").str.lower().eq("active")
    if df["_ks_active"].any():
        # Find consecutive active runs
        in_active = False
        run_start = None
        for _, row in df.iterrows():
            if row["_ks_active"] and not in_active:
                in_active = True
                run_start = row["date"]
            elif not row["_ks_active"] and in_active:
                in_active = False
                fig.add_vrect(x0=run_start, x1=row["date"],
                              fillcolor="rgba(220,38,38,0.12)",
                              line_width=0, annotation_text="KS active",
                              annotation_position="top left",
                              annotation_font_size=10)
        if in_active and run_start is not None:
            fig.add_vrect(x0=run_start, x1=df.iloc[-1]["date"],
                          fillcolor="rgba(220,38,38,0.12)",
                          line_width=0, annotation_text="KS active",
                          annotation_position="top left",
                          annotation_font_size=10)

    fig.update_layout(
        height=380, margin=dict(l=40, r=20, t=20, b=40),
        template="plotly_white",
        xaxis_title="Дата", yaxis_title="Alignment score",
        showlegend=False,
    )
    return pio.to_html(fig, include_plotlyjs=False, full_html=False,
                       div_id="vrm-timeline")


def _section_vrm(duck) -> str:
    chart_html = _chart_vrm_timeline(duck)
    if not chart_html:
        return ""
    return (
        '<section class="card">'
        '<h2>⚙️ VRM timeline</h2>'
        '<p class="hint">Alignment score над времето. Червени shaded bands = KS активен. '
        'Hover за regime + KS статус.</p>'
        + chart_html +
        '</section>'
    )


# ────────────────────────────────────────────────────────────────────────────
#  Section 5: Top 3 parallels table
# ────────────────────────────────────────────────────────────────────────────

def _section_parallels(bundle: StateBundle) -> str:
    parallels = bundle.parallels
    if not parallels:
        return ""

    rows: list[str] = []
    rows.append(
        '<table class="tbl parallels"><thead><tr>'
        '<th>Седмица</th><th class="num">Cosine</th>'
        '<th class="num">SPY 1m/3m/6m</th>'
        '<th class="num">USO 1m/3m/6m</th>'
        '<th class="num">GLD 1m/3m/6m</th>'
        '<th class="num">TLT 1m/3m/6m</th>'
        '</tr></thead><tbody>'
    )

    def trio(fwd: dict, sym: str) -> str:
        d = fwd.get(sym, {})
        def cell(h):
            v = d.get(h)
            return f"{v:+.1f}%" if v is not None else "—"
        return f"{cell('1m')} / {cell('3m')} / {cell('6m')}"

    for p in parallels:
        fwd = p.get("forward_returns_pct", {})
        rows.append(
            f'<tr>'
            f'<td class="sym">{p["match_week"]} <span class="muted small">(end {p["match_week_end"]})</span></td>'
            f'<td class="num">{p["cosine_similarity"]:.3f}</td>'
            f'<td class="num">{trio(fwd, "SPY")}</td>'
            f'<td class="num">{trio(fwd, "USO")}</td>'
            f'<td class="num">{trio(fwd, "GLD")}</td>'
            f'<td class="num">{trio(fwd, "TLT")}</td>'
            f'</tr>'
        )
    rows.append('</tbody></table>')

    return (
        '<section class="card">'
        '<h2>⏳ Топ 3 исторически паралели</h2>'
        '<p class="hint">Cosine similarity на текущата седмица vs 10-ETF macro signature '
        '(SPY/IWM/TLT/GLD/USO/UUP/HYG/XLE/XLK/XLF). Forward returns = какво е последвало '
        'след всеки паралел.</p>'
        + "\n".join(rows) +
        f'<p class="hint" style="margin-top: 12px;">Виж пълни 5 паралела + всички '
        f'symbols в <a href="https://github.com/tsvetoslavtsachev/macro-satellite/blob/main/'
        f'briefings/{bundle.week.label}.md" class="link-external">{bundle.week.label}.md</a>.</p>'
        '</section>'
    )


# ────────────────────────────────────────────────────────────────────────────
#  Section 6: Persistent macro anomalies + links footer
# ────────────────────────────────────────────────────────────────────────────

def _section_persistent_anomalies(bundle: StateBundle) -> str:
    us = bundle.persistent_us
    eu = bundle.persistent_eu
    if not us and not eu:
        return ""

    def render_block(region: str, items: list[dict]) -> str:
        if not items:
            return ""
        rows = [f'<h3>{region} макро серии под натиск</h3>',
                '<ul class="anomalies">']
        for it in items[:5]:
            ext = ' <span class="badge-inline new-extreme">NEW-EXTREME</span>' if it.get("new_extreme") else ""
            rows.append(
                f'<li><b>{it["code"]}</b> '
                f'<span class="muted">({it.get("label_bg", "")})</span> · '
                f'lens={it.get("lens", "?")} · '
                f'|z|={it.get("mean_abs_z", 0):.2f}'
                f'{ext}</li>'
            )
        rows.append('</ul>')
        return "\n".join(rows)

    parts = ['<section class="card">',
             '<h2>🔭 Macro серии с persistence</h2>',
             '<p class="hint">Серии в top_anomalies на macro_state поне 2 пъти '
             'в последните 4 седмици с |z|≥2.0 — текущи структурни напрежения.</p>']
    parts.append(render_block("🇺🇸 US", us))
    parts.append(render_block("🇪🇺 EU", eu))
    parts.append('</section>')
    return "\n".join(parts)


# ────────────────────────────────────────────────────────────────────────────
#  HTML scaffold
# ────────────────────────────────────────────────────────────────────────────

_CSS = """
:root {
  --bg: #f7f7f8;
  --card-bg: #ffffff;
  --border: #e5e7eb;
  --text: #1f2937;
  --muted: #6b7280;
  --accent: #2563eb;
  --up: #16a34a;
  --down: #dc2626;
}
* { box-sizing: border-box; }
body {
  margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Inter", sans-serif;
  background: var(--bg); color: var(--text); line-height: 1.5;
}
header {
  background: white; border-bottom: 1px solid var(--border); padding: 16px 32px;
}
header h1 { margin: 0; font-size: 22px; }
header .meta { color: var(--muted); font-size: 13px; margin-top: 4px; }
header .links a { color: var(--accent); text-decoration: none; margin-right: 16px; font-size: 13px; }
main { max-width: 1280px; margin: 0 auto; padding: 24px; }
.card {
  background: var(--card-bg); border: 1px solid var(--border); border-radius: 10px;
  padding: 24px; margin-bottom: 20px;
}
.card.hero {
  background: linear-gradient(180deg, #fafbff 0%, #ffffff 100%);
  border-color: #c7d2fe;
}
.card h2 { margin-top: 0; margin-bottom: 12px; font-size: 20px; }
.card h2 .date-range { font-size: 14px; color: var(--muted); font-weight: 400; }
.card h3 { margin-top: 16px; margin-bottom: 8px; font-size: 15px; color: var(--text); }
.hint { color: var(--muted); font-size: 13px; margin-bottom: 12px; }
.muted { color: var(--muted); }
.small { font-size: 12px; }
.badges { display: flex; flex-wrap: wrap; gap: 16px; }
.badge {
  flex: 1 1 230px; background: #f9fafb; border-left: 4px solid var(--accent);
  padding: 14px 18px; border-radius: 6px;
}
.badge-label { color: var(--muted); font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em; }
.badge-value { font-size: 18px; font-weight: 600; margin-top: 4px; }
.badge-sub { color: var(--muted); font-size: 12px; margin-top: 4px; }
.badge.vrm { border-left-color: #2563eb; }
.badge.us { border-left-color: #dc2626; }
.badge.eu { border-left-color: #2563eb; }
.ks-active { color: var(--down); font-weight: 700; }
.ks-inactive { color: var(--up); }
.triggered-chips { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 8px; }
.chip {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 6px 12px; border-radius: 16px; font-size: 13px;
  text-decoration: none; transition: background 0.15s;
}
.chip-alert {
  background: #fef2f2; color: #991b1b; border: 1px solid #fecaca;
}
.chip-alert:hover { background: #fee2e2; }
.chip-count {
  background: white; color: #991b1b; padding: 2px 8px;
  border-radius: 10px; font-weight: 600; font-size: 11px;
}
.briefing-hero { padding: 16px 20px; background: #f9fafb; border-radius: 6px; margin-top: 8px; }
.briefing-hero h2 { font-size: 17px; margin-top: 0; }
.briefing-hero h3 { font-size: 15px; }
.briefing-hero ul { margin: 8px 0; padding-left: 22px; }
.briefing-hero li { margin: 4px 0; }
.briefing-hero p { margin: 8px 0; }
.briefing-hero strong { color: var(--text); }
.briefing-hero code {
  background: white; padding: 1px 6px; border-radius: 3px; font-size: 0.9em;
}
.briefing-tldr {
  border-left: 3px solid #94a3b8;
  padding-left: 14px; margin-bottom: 14px;
}
.briefing-tldr h2 { font-size: 14px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; }
.briefing-thesis h2 { font-size: 17px; }
.briefing-links {
  margin-top: 14px; font-size: 13px;
}
.link-external { color: var(--accent); text-decoration: none; }
.link-external:hover { text-decoration: underline; }
.pattern-block {
  margin-bottom: 18px; padding: 14px 16px;
  background: #fefce8; border-left: 3px solid #ca8a04; border-radius: 4px;
}
.pattern-block h3 { margin-top: 0; }
ul.conditions { list-style: none; padding-left: 0; margin: 8px 0; }
li.cond { padding: 4px 0; font-size: 14px; }
li.cond .mark {
  display: inline-block; width: 18px; text-align: center;
  font-weight: 700;
}
li.cond.match .mark { color: var(--up); }
li.cond.miss .mark { color: var(--down); }
table.tbl {
  width: 100%; border-collapse: collapse; font-size: 13px;
}
table.tbl th, table.tbl td {
  padding: 8px 12px; text-align: left; border-bottom: 1px solid var(--border);
}
table.tbl th {
  background: #f9fafb; font-weight: 600; color: var(--muted);
  text-transform: uppercase; font-size: 11px; letter-spacing: 0.05em;
}
table.tbl td.sym { font-weight: 600; }
table.tbl td.num, table.tbl th.num { text-align: right; font-variant-numeric: tabular-nums; }
table.tbl td.up { color: var(--up); }
table.tbl td.down { color: var(--down); }
ul.anomalies { padding-left: 22px; margin: 8px 0 16px; }
ul.anomalies li { padding: 3px 0; font-size: 13px; }
.badge-inline {
  display: inline-block; padding: 1px 7px; border-radius: 10px;
  font-size: 10px; font-weight: 600; margin-left: 4px;
}
.badge-inline.new-extreme {
  background: #fef2f2; color: #991b1b; border: 1px solid #fecaca;
}
footer {
  text-align: center; padding: 24px; color: var(--muted); font-size: 12px;
  border-top: 1px solid var(--border); margin-top: 24px;
}
footer a { color: var(--accent); text-decoration: none; }
footer .ai-link {
  display: inline-block; margin-top: 8px; padding: 6px 14px;
  background: #eef2ff; color: #4338ca; border-radius: 16px;
  font-weight: 600; border: 1px solid #c7d2fe;
}
@media (max-width: 640px) {
  main { padding: 16px; }
  .card { padding: 18px 16px; }
  .badge { flex: 1 1 100%; }
  table.tbl { font-size: 12px; }
  table.tbl th, table.tbl td { padding: 6px 8px; }
}
"""


def _build_html(sections: list[str], week_label: str) -> str:
    from datetime import datetime, timezone
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    sections_html = "\n".join(s for s in sections if s)
    return f"""<!DOCTYPE html>
<html lang="bg">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>macro-satellite · Сателитен Dashboard · {week_label}</title>
<script src="{PLOTLY_CDN}"></script>
<style>{_CSS}</style>
</head>
<body>
<header>
  <h1>📡 macro-satellite · Сателитен Dashboard</h1>
  <div class="meta">Автоматично генериран {generated_at} · daily collect 04:00 София · седмица {week_label}</div>
  <div class="links" style="margin-top: 8px;">
    <a href="https://github.com/tsvetoslavtsachev/macro-satellite">GitHub repo</a>
    <a href="https://github.com/tsvetoslavtsachev/macro-satellite/tree/main/briefings">Briefings</a>
    <a href="https://github.com/tsvetoslavtsachev/macro-satellite/actions">Workflow runs</a>
    <a href="state.json">📡 state.json (за AI)</a>
  </div>
</header>
<main>
{sections_html}
</main>
<footer>
  Generated by <a href="https://github.com/tsvetoslavtsachev/macro-satellite">macro-satellite</a>.
  <br/>
  <a class="ai-link" href="state.json">📡 AI-readable JSON snapshot</a>
</footer>
</body>
</html>
"""


# ────────────────────────────────────────────────────────────────────────────
#  Public entry point
# ────────────────────────────────────────────────────────────────────────────

def generate_dashboard(output_dir: Path | None = None,
                       heatmap_weeks: int = 13,
                       skip_state_export: bool = False,
                       price_history_days: int | None = None,
                       ) -> Path:
    """Генерира docs/index.html + (по подразбиране) docs/state.json.

    Args:
        output_dir: target dir, default REPO_ROOT/docs.
        heatmap_weeks: брой исторически седмици в z-score heatmap (default 13).
        skip_state_export: ако True, не пише state.json (използва се само от
            външни callers, които вече са го изпратили).
        price_history_days: ignored (запазен за CLI compatibility) — dashboard-ът
            ползва фиксиран 4w и 13w window.

    Returns:
        Path към index.html.
    """
    duck = get_duck()
    out_dir = output_dir or (REPO_ROOT / "docs")
    out_dir.mkdir(parents=True, exist_ok=True)
    week = current_week()

    log.info("dashboard generate start", extra={"week": week.label})

    # Build state bundle веднъж — споделя се между state.json и HTML рендеринга.
    if skip_state_export:
        bundle = build_state_bundle(week=week, duck=duck)
    else:
        _state_path, bundle = write_state_json(week=week, output_dir=out_dir,
                                                duck=duck)

    sections = [
        _section_hero(bundle),
        _section_4w_focus(duck, bundle),
        _section_pattern_details(bundle),
        _section_13w_context(duck, bundle),
        _section_vrm(duck),
        _section_parallels(bundle),
        _section_persistent_anomalies(bundle),
    ]
    html = _build_html(sections, bundle.week.label)
    path = out_dir / "index.html"
    path.write_text(html, encoding="utf-8")
    log.info("dashboard written",
             extra={"path": str(path), "size_kb": len(html) // 1024,
                    "n_sections": sum(1 for s in sections if s),
                    "n_triggered_patterns": len(bundle.triggered_patterns),
                    "n_movements": len(bundle.week_movements_etf)})
    return path
