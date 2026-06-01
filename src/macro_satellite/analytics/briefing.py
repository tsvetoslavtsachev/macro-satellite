"""Седмичен briefing markdown generator.

Комбинира findings от:
- weekly_window: interval changes за core universe
- z_scores: |z|>=1.5 ETF moves vs trailing 13 weeks
- rotation_events: entered/exited stable_winners за US + EU
- vrm_state: regime/KS/alignment shift
- macro_state: lens shifts + top anomalies от US/EU
- divergence_engine: triggered cross-asset patterns
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pandas as pd

from ..config import macro_lenses
from ..logging_setup import get_logger
from ..paths import REPO_ROOT
from ..storage.duckdb_conn import get_duck
from .divergence_engine import evaluate_all
from .macro_anomalies_expander import persistent_anomalies
from .parallels import find_parallels
from .rotation_events import rotation_diff
from .weekly_window import (
    WeekWindow,
    current_week,
    last_close_on_or_before,
    previous_week,
    weekly_interval_change,
)
from .z_scores import scan_universe

log = get_logger(__name__)

# Core ETF universe за briefing — типични macro/sector proxies.
CORE_ETFS = ["USO", "XLE", "DFEN", "URA", "GLD", "TLT", "UUP",
             "SPY", "QQQ", "IWM", "DIA",
             "XLF", "XLK", "XLV", "XLP", "XLY", "XLI", "XLB", "XLU", "XLRE", "XLC",
             "HYG", "LQD", "TIP", "IEF", "SHY",
             "DBC", "DBA", "GDX", "SLV", "VNQ",
             "EFA", "EEM", "VEA", "VWO",
             "IBIT", "SOXX"]


def _fmt_pct(x: float, decimals: int = 1) -> str:
    return f"{x*100:+.{decimals}f}%"


def _safe_float(x):
    try:
        return float(x) if x is not None and not pd.isna(x) else None
    except (ValueError, TypeError):
        return None


def _vrm_section(duck) -> str:
    sql = """SELECT date, regime, ks_status, alignment_score, alignment_total,
             gms_value, last_updated_md, is_change_day
             FROM vrm_state ORDER BY date DESC LIMIT 2"""
    df = duck.execute(sql).df()
    if df.empty:
        return "## VRM\n_Няма данни._\n"
    latest = df.iloc[0]
    prev = df.iloc[1] if len(df) > 1 else None

    lines = ["## VRM"]
    lines.append(f"- **Режим:** {latest['regime']}")
    lines.append(f"- **KS:** {latest['ks_status']}")
    al = _safe_float(latest["alignment_score"])
    al_max = latest["alignment_total"]
    if al is not None:
        lines.append(f"- **Alignment:** {al:.1f}/{al_max}")
    gms = _safe_float(latest["gms_value"])
    if gms is not None:
        lines.append(f"- **GMS:** {gms:.1f}")
    lines.append(f"- **Последна актуализация в MD:** {latest['last_updated_md']}")

    if prev is not None:
        changes = []
        if latest["regime"] != prev["regime"]:
            changes.append(f"режим {prev['regime']} → {latest['regime']}")
        if latest["ks_status"] != prev["ks_status"]:
            changes.append(f"KS {prev['ks_status']} → {latest['ks_status']}")
        prev_al = _safe_float(prev["alignment_score"])
        if al is not None and prev_al is not None and abs(al - prev_al) > 0.01:
            changes.append(f"alignment {prev_al:.1f} → {al:.1f}")
        if changes:
            lines.append("- **Промени:** " + "; ".join(changes))
        else:
            lines.append("- _Без структурни промени от последния snapshot._")
    return "\n".join(lines) + "\n"


def _macro_section(duck, region: str) -> str:
    table = f"{region.lower()}_macro_state"
    lenses = macro_lenses(region)
    lens_sel = ", ".join(f"{l}_score" for l in lenses)
    sql = (f"SELECT date, regime_key, regime_label_bg, narrative, primary_driver, "
           f"{lens_sel}, "
           f"top_anomalies_json, cross_lens_divergences_count "
           f"FROM {table} ORDER BY date DESC LIMIT 2")
    df = duck.execute(sql).df()
    if df.empty:
        return f"## Macro {region}\n_Няма данни._\n"
    latest = df.iloc[0]
    prev = df.iloc[1] if len(df) > 1 else None

    lines = [f"## Macro {region}"]
    lines.append(f"- **Режим:** {latest['regime_key']} ({latest['regime_label_bg']})")
    lines.append(f"- **Primary driver:** {latest['primary_driver']}")
    lens_strs = []
    for lens in lenses:
        v = _safe_float(latest[f"{lens}_score"])
        if v is None:
            continue
        delta = ""
        if prev is not None:
            pv = _safe_float(prev[f"{lens}_score"])
            if pv is not None and abs(v - pv) > 0.05:
                delta = f" ({v - pv:+.1f} vs prev)"
        lens_strs.append(f"{lens}={v:.1f}{delta}")
    if lens_strs:
        lines.append("- **Lens scores:** " + " · ".join(lens_strs))
    lines.append(f"- **Cross-lens divergences:** {latest['cross_lens_divergences_count']}")

    # Top anomalies от latest snapshot
    try:
        anomalies = json.loads(latest["top_anomalies_json"] or "[]")
    except Exception:
        anomalies = []
    if anomalies:
        lines.append("- **Top anomalies:**")
        for a in anomalies[:5]:
            sid = a.get("series_id", "?")
            name = a.get("name_bg", sid)
            z = a.get("z_score", 0)
            direction = a.get("direction", "")
            ext = " · NEW-MAX" if a.get("is_new_extreme") and a.get("new_extreme_direction") == "max" else ""
            ext = " · NEW-MIN" if a.get("is_new_extreme") and a.get("new_extreme_direction") == "min" else ext
            lines.append(f"  - {sid} ({name}) z={z:+.2f} {direction}{ext}")
    if latest.get("narrative"):
        lines.append(f"\n> {str(latest['narrative']).strip()[:500]}")
    return "\n".join(lines) + "\n"


def _etf_moves_section(duck, week: WeekWindow) -> tuple[str, list]:
    z_results = scan_universe(duck, CORE_ETFS, week, trailing_n=13, z_threshold=1.5)
    lines = ["## ETF движения (|z| ≥ 1.5σ vs предишните 13 седмици)"]
    if not z_results:
        lines.append("_Нищо забележимо тази седмица._\n")
        return "\n".join(lines) + "\n", []
    for r in z_results[:15]:
        lines.append(
            f"- **{r.symbol}** {_fmt_pct(r.weekly_change)} ({r.z_score:+.2f}σ) · "
            f"price {r.price_a:.2f} → {r.price_b:.2f} · "
            f"{r.date_a} → {r.date_b}"
        )
    return "\n".join(lines) + "\n", z_results


def _rotation_section(duck, week: WeekWindow) -> str:
    lines = ["## Ротация (US + EU)"]
    any_data = False
    for universe in ("us", "eu"):
        deltas = rotation_diff(duck, universe, week)
        if not deltas:
            continue
        any_data = True
        lines.append(f"\n### {universe.upper()}")
        for d in deltas:
            if not d.entered and not d.exited:
                continue
            header = f"**{d.quadrant}** ({d.horizon}, {d.a_date} → {d.b_date}):"
            parts = []
            if d.entered:
                first_marker = ""
                if d.first_time_ever:
                    first_marker = f" · {len(d.first_time_ever)} for first time ever"
                parts.append(f"+{len(d.entered)} entered{first_marker} → "
                             f"{', '.join(d.entered[:8])}"
                             f"{'...' if len(d.entered) > 8 else ''}")
            if d.exited:
                parts.append(f"-{len(d.exited)} exited → "
                             f"{', '.join(d.exited[:8])}"
                             f"{'...' if len(d.exited) > 8 else ''}")
            if parts:
                lines.append(f"- {header} " + "; ".join(parts))
    if not any_data:
        lines.append("_Няма rotation snapshot за тази седмица или предишната._")
    return "\n".join(lines) + "\n"


def _persistent_anomalies_section(duck, region: str,
                                   lookback_weeks: int = 4,
                                   min_occurrences: int = 2) -> str:
    """Серии, появили се в top_anomalies поне `min_occurrences` пъти в lookback window."""
    try:
        df = persistent_anomalies(region, lookback_weeks=lookback_weeks,
                                  min_occurrences=min_occurrences,
                                  min_abs_z=2.0, duck=duck)
    except Exception:
        df = None
    label = f"Persistent аномалии {region} (≥{min_occurrences} появявания в последните {lookback_weeks} седмици)"
    lines = [f"### {label}"]
    if df is None or df.empty:
        lines.append("_Никои серии не покриват праговете._")
        return "\n".join(lines) + "\n"
    for _, r in df.head(10).iterrows():
        ext = " · NEW-EXTREME" if r["any_new_extreme"] else ""
        lines.append(
            f"- **{r['series_id']}** ({r['name_bg']}) · "
            f"lens={r['lens']} · "
            f"{int(r['occurrences'])} appearances · "
            f"mean |z|={r['mean_abs_z']:.2f} · max |z|={r['max_abs_z']:.2f}{ext}"
        )
    return "\n".join(lines) + "\n"


def _parallels_section(duck, week: WeekWindow, top_k: int = 5) -> str:
    """Historical parallels section — top K similar weeks + forward returns."""
    parallels = find_parallels(duck, week, top_k=top_k)
    lines = ["## Исторически паралели (top {} най-similar weeks по macro signature)".format(top_k)]
    if not parallels:
        lines.append("_Недостатъчно история за similarity search._")
        return "\n".join(lines) + "\n"
    lines.append("_Cosine similarity vs 10-ETF macro vector (SPY/IWM/TLT/GLD/USO/UUP/HYG/XLE/XLK/XLF). "
                 "Forward returns показват какво е последвало след всеки паралел._\n")
    for p in parallels:
        lines.append(f"### {p.match_week} (week ending {p.match_week_end}) · cosine={p.cosine_similarity:.3f}")
        if not p.forward_returns:
            lines.append("_Без forward returns (близо до края на история-та)._")
            continue
        lines.append("| Symbol | +1m | +3m | +6m |")
        lines.append("|---|---:|---:|---:|")
        for sym in ("SPY", "USO", "GLD", "TLT", "XLE", "IWM"):
            if sym not in p.forward_returns:
                continue
            row = p.forward_returns[sym]
            def cell(h):
                v = row.get(h)
                return f"{v*100:+.1f}%" if v is not None else "-"
            lines.append(f"| **{sym}** | {cell('1m')} | {cell('3m')} | {cell('6m')} |")
        lines.append("")
    return "\n".join(lines) + "\n"


def _divergence_section(duck, end_date: date) -> tuple[str, list]:
    hits = evaluate_all(end_date, duck)
    triggered = [h for h in hits if h.triggered]
    lines = ["## Cross-asset divergence patterns"]
    if not triggered:
        not_triggered = [f"{h.name}: {h.n_matched}/{len(h.matches)}" for h in hits]
        lines.append("_Никой канонична pattern не се триггерира тази седмица._")
        lines.append(f"\nЧасtично съвпадение: {' · '.join(not_triggered)}")
        return "\n".join(lines) + "\n", []
    for h in triggered:
        lines.append(f"\n### 🔔 {h.label_bg} (`{h.name}`)")
        lines.append(f"_{h.description}_")
        lines.append(f"- Window: {h.window_days}d ending {h.end_date}")
        lines.append(f"- Conditions matched: **{h.n_matched}/{len(h.matches)}**")
        for m in h.matches:
            mark = "✓" if m.matched else "✗"
            if pd.isna(m.actual_change_pct):
                lines.append(f"  - {mark} {m.symbol}: no data for window")
            else:
                lines.append(
                    f"  - {mark} {m.symbol}: {m.actual_change_pct:+.2f}% "
                    f"(target {m.target_direction} ≥ {m.target_min_pct}%)"
                )
    return "\n".join(lines) + "\n", triggered


def _tldr_section(z_results: list, triggered_patterns: list,
                  vrm_changed: bool, regime_us: str | None,
                  regime_eu: str | None) -> str:
    bullets = []
    if triggered_patterns:
        names = [h.label_bg for h in triggered_patterns[:3]]
        bullets.append(f"🔔 Триггерирани patterns: {', '.join(names)}")
    if z_results:
        top = z_results[0]
        bullets.append(
            f"📈 Топ седмично движение: {top.symbol} {_fmt_pct(top.weekly_change)} "
            f"({top.z_score:+.2f}σ)"
        )
    if vrm_changed:
        bullets.append("⚙️ VRM regime/KS shift тази седмица — виж раздела")
    if regime_us:
        bullets.append(f"🇺🇸 US macro: {regime_us}")
    if regime_eu:
        bullets.append(f"🇪🇺 EU macro: {regime_eu}")
    if not bullets:
        bullets.append("Спокойна седмица — никой канонична pattern, никой ETF |z|≥1.5σ.")
    return "## TL;DR\n" + "\n".join(f"- {b}" for b in bullets) + "\n"


def generate_briefing(target_week: WeekWindow | None = None) -> tuple[str, Path]:
    duck = get_duck()
    week = target_week or current_week()
    log.info("briefing start", extra={"week": week.label,
                                      "range": f"{week.week_start}..{week.week_end}"})

    # collect findings
    vrm_md = _vrm_section(duck)
    us_macro_md = _macro_section(duck, "US")
    eu_macro_md = _macro_section(duck, "EU")
    cn_macro_md = _macro_section(duck, "CN")
    persist_us = _persistent_anomalies_section(duck, "US")
    persist_eu = _persistent_anomalies_section(duck, "EU")
    persist_cn = _persistent_anomalies_section(duck, "CN")
    persistent_md = ("## Macro серии с persistence\n"
                     "_Серии, появили се в top_anomalies на macro_state в "
                     "няколко поредни snapshots — текущи макро напрежения._\n\n"
                     + persist_us + "\n" + persist_eu + "\n" + persist_cn)
    etf_md, z_results = _etf_moves_section(duck, week)
    rotation_md = _rotation_section(duck, week)
    div_md, triggered = _divergence_section(duck, week.week_end)
    parallels_md = _parallels_section(duck, week, top_k=5)

    # extract regime labels for TL;DR
    us_regime = None
    eu_regime = None
    try:
        us_regime = duck.execute(
            "SELECT regime_label_bg FROM us_macro_state ORDER BY date DESC LIMIT 1"
        ).df().iloc[0]["regime_label_bg"]
    except Exception:
        pass
    try:
        eu_regime = duck.execute(
            "SELECT regime_label_bg FROM eu_macro_state ORDER BY date DESC LIMIT 1"
        ).df().iloc[0]["regime_label_bg"]
    except Exception:
        pass

    # VRM change indicator
    vrm_changed = False
    try:
        vrm_df = duck.execute(
            "SELECT regime, ks_status FROM vrm_state ORDER BY date DESC LIMIT 2"
        ).df()
        if len(vrm_df) == 2:
            vrm_changed = (vrm_df.iloc[0]["regime"] != vrm_df.iloc[1]["regime"]
                          or vrm_df.iloc[0]["ks_status"] != vrm_df.iloc[1]["ks_status"])
    except Exception:
        pass

    tldr = _tldr_section(z_results, triggered, vrm_changed, us_regime, eu_regime)

    header = (
        f"# Сателитен Обзор — Седмица {week.label}\n"
        f"\n_Период: {week.week_start} → {week.week_end}_  \n"
        f"_Генериран: {pd.Timestamp.utcnow().strftime('%Y-%m-%d %H:%M UTC')}_\n\n"
    )
    open_questions = (
        "## Open questions за ръчна проверка\n"
        "- _Placeholder. Phase 3 ще автоматизира извличането на въпроси от narrative-а._\n"
    )

    body = "\n---\n\n".join([
        tldr, etf_md, div_md, parallels_md, persistent_md, rotation_md, vrm_md,
        us_macro_md, eu_macro_md, cn_macro_md, open_questions,
    ])
    md = header + body

    out_dir = REPO_ROOT / "briefings"
    out_dir.mkdir(exist_ok=True)
    path = out_dir / f"{week.label}.md"
    path.write_text(md, encoding="utf-8")
    log.info("briefing written", extra={"path": str(path), "n_z_signals": len(z_results),
                                        "n_triggered_patterns": len(triggered)})
    return md, path
