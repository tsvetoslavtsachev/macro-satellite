"""Narrative briefing generator.

Структуриран briefing → БГ prose, готов вход за `weekly-story-teller` skill.
Никакви invented numbers — всички твърдения произлизат от Parquet данните.

Структура на output-а:
1. 🎯 Тезата на седмицата (1-2 параграфа)
2. 📊 Какво се случи (evidence — ETF + divergence + rotation)
3. ⏳ Исторически паралели (prose за топ 2-3 match-а)
4. ⚠️ Какво може да обърне тезата (open questions + contradicting signals)
5. 🔭 Какво да наблюдаваме (watchlist от persistent anomalies + macro hints)
6. 📋 Линк към структурирания briefing
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pandas as pd

from ..logging_setup import get_logger
from ..paths import REPO_ROOT
from ..storage.duckdb_conn import get_duck
from .briefing import CORE_ETFS
from .divergence_engine import PatternHit, evaluate_all
from .macro_anomalies_expander import persistent_anomalies
from .parallels import find_parallels
from .weekly_window import WeekWindow, current_week
from .z_scores import WeeklyZScore, scan_universe

log = get_logger(__name__)


# ────────────────────────────────────────────────────────────────────────────
#  Helpers
# ────────────────────────────────────────────────────────────────────────────

def _fmt_pct(x: float, decimals: int = 1) -> str:
    return f"{x*100:+.{decimals}f}%"


def _safe(val):
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return None
    return val


# ────────────────────────────────────────────────────────────────────────────
#  Thesis derivation
#  Приоритет: 1) triggered divergence pattern → 2) Extreme |z| ETF move →
#             3) VRM regime/KS shift → 4) Macro lens shift → 5) Calm week
# ────────────────────────────────────────────────────────────────────────────

def _derive_thesis(triggered: list[PatternHit],
                   z_results: list[WeeklyZScore],
                   vrm_changed: bool,
                   vrm_summary: dict | None,
                   macro_us_shift: dict | None,
                   macro_eu_shift: dict | None) -> dict:
    """Връща dict с {priority, summary_bg, supporting_label, raw_source}."""

    # Priority 1: triggered divergence pattern (highest match count first)
    if triggered:
        p = sorted(triggered, key=lambda h: -h.n_matched)[0]
        return {
            "priority": "divergence",
            "summary_bg": p.label_bg,
            "description": p.description,
            "raw": p,
        }

    # Priority 2: extreme |z| move (>=2.5σ) — single most-extreme
    if z_results:
        extreme = [r for r in z_results if abs(r.z_score) >= 2.5]
        if extreme:
            top = extreme[0]
            direction_word = "взрив" if top.z_score > 0 else "срив"
            return {
                "priority": "extreme_etf",
                "summary_bg": f"{top.symbol} {direction_word} от {top.z_score:+.2f}σ — {_fmt_pct(top.weekly_change)} за седмицата",
                "raw": top,
            }

    # Priority 3: VRM regime/KS shift
    if vrm_changed and vrm_summary:
        return {
            "priority": "vrm_shift",
            "summary_bg": f"VRM режимна промяна — {vrm_summary.get('summary', 'виж раздела')}",
            "raw": vrm_summary,
        }

    # Priority 4: Macro lens score shift (>=5 points week-over-week)
    for region, shift in [("US", macro_us_shift), ("EU", macro_eu_shift)]:
        if shift and shift.get("max_abs_delta", 0) >= 5.0:
            return {
                "priority": "macro_lens_shift",
                "summary_bg": (f"{region} macro: значителна промяна в "
                               f"{shift['top_lens']} lens ({shift['top_delta']:+.1f} pts)"),
                "raw": shift,
            }

    # Priority 5: Lower-grade |z| signal
    if z_results:
        top = z_results[0]
        return {
            "priority": "moderate_etf",
            "summary_bg": (f"Без екстремни сигнали. Най-силно движение: "
                           f"{top.symbol} {_fmt_pct(top.weekly_change)} ({top.z_score:+.2f}σ)"),
            "raw": top,
        }

    # Calm week
    return {
        "priority": "calm",
        "summary_bg": "Спокойна седмица — никой ETF не премина 1.5σ, никой канонична pattern не се триггерира.",
        "raw": None,
    }


# ────────────────────────────────────────────────────────────────────────────
#  Section generators (return markdown strings)
# ────────────────────────────────────────────────────────────────────────────

def _thesis_section(thesis: dict, triggered: list[PatternHit],
                    z_results: list[WeeklyZScore]) -> str:
    lines = ["## 🎯 Тезата на седмицата\n"]
    lines.append(f"**{thesis['summary_bg']}**\n")

    p = thesis["priority"]
    if p == "divergence":
        hit: PatternHit = thesis["raw"]
        match_lines = []
        for m in hit.matches:
            if m.matched:
                match_lines.append(
                    f"{m.symbol} {m.actual_change_pct:+.1f}% (target {m.target_direction} ≥ {m.target_min_pct}%)")
        lines.append(
            f"Триггерирана е канонична **{hit.label_bg}** — съвпадат "
            f"**{hit.n_matched}/{len(hit.matches)}** условия:"
        )
        lines.append("")
        for ml in match_lines:
            lines.append(f"- {ml}")
        lines.append(f"\n_{hit.description}_\n")
    elif p == "extreme_etf":
        r: WeeklyZScore = thesis["raw"]
        lines.append(
            f"Движението {r.symbol} {_fmt_pct(r.weekly_change)} е "
            f"**{abs(r.z_score):.2f}σ** разстояние от средната седмична промяна "
            f"({_fmt_pct(r.trailing_mean)} ± {_fmt_pct(r.trailing_std)}) "
            f"над последните {r.n_baseline_weeks} седмици. "
        )
        lines.append(
            f"Цената премина от {r.price_a:.2f} ({r.date_a}) до "
            f"{r.price_b:.2f} ({r.date_b}).\n"
        )
        # Related signals
        other_strong = [x for x in z_results if x.symbol != r.symbol][:3]
        if other_strong:
            lines.append("Контекст от други движения същата седмица:")
            for o in other_strong:
                lines.append(f"- {o.symbol} {_fmt_pct(o.weekly_change)} ({o.z_score:+.2f}σ)")
            lines.append("")
    elif p == "calm":
        lines.append("_Това е период за наблюдение, не за теза._\n")
    return "\n".join(lines) + "\n"


def _evidence_section(z_results: list[WeeklyZScore],
                      triggered: list[PatternHit],
                      rotation_summary: str) -> str:
    lines = ["## 📊 Какво се случи (евиденция)\n"]

    if z_results:
        lines.append("### ETF движения с \|z\| ≥ 1.5σ\n")
        up = [r for r in z_results if r.z_score > 0]
        down = [r for r in z_results if r.z_score < 0]
        if up:
            lines.append("**Нагоре:** " +
                         ", ".join(f"{r.symbol} {_fmt_pct(r.weekly_change)} ({r.z_score:+.2f}σ)"
                                   for r in up))
        if down:
            lines.append("\n**Надолу:** " +
                         ", ".join(f"{r.symbol} {_fmt_pct(r.weekly_change)} ({r.z_score:+.2f}σ)"
                                   for r in down))
        lines.append("")
    else:
        lines.append("_Никой ETF в core universe не премина 1.5σ._\n")

    # Triggered patterns
    if triggered:
        lines.append("### Triggered divergence patterns\n")
        for hit in triggered:
            lines.append(f"- **{hit.label_bg}**: {hit.n_matched}/{len(hit.matches)} conditions matched")
        lines.append("")
    else:
        lines.append("### Cross-asset patterns\n_Никой канонична pattern не се триггерира._\n")

    # Rotation
    if rotation_summary:
        lines.append("### Rotation\n")
        lines.append(rotation_summary)
        lines.append("")

    return "\n".join(lines) + "\n"


def _parallels_section(duck, week: WeekWindow, top_k: int = 3) -> str:
    parallels = find_parallels(duck, week, top_k=top_k)
    lines = ["## ⏳ Исторически паралели — какво е следвало\n"]
    if not parallels:
        lines.append("_Недостатъчно история за similarity search._\n")
        return "\n".join(lines)

    # First parallel (closest) — prose
    top = parallels[0]
    lines.append(
        f"Най-близкият паралел на текущата седмица е **{top.match_week}** "
        f"(week ending {top.match_week_end}, cosine similarity {top.cosine_similarity:.2f}). "
    )
    spy_returns = top.forward_returns.get("SPY", {})
    uso_returns = top.forward_returns.get("USO", {})
    gld_returns = top.forward_returns.get("GLD", {})

    summary_parts = []
    if spy_returns.get("6m") is not None:
        summary_parts.append(f"SPY {_fmt_pct(spy_returns['6m'])} за 6m")
    if uso_returns.get("6m") is not None:
        summary_parts.append(f"USO {_fmt_pct(uso_returns['6m'])}")
    if gld_returns.get("6m") is not None:
        summary_parts.append(f"GLD {_fmt_pct(gld_returns['6m'])}")
    if summary_parts:
        lines.append(f"Тогава за следващите 6 месеца: {', '.join(summary_parts)}.")
    lines.append("")

    # Aggregate signal: consistent или mixed forward outcomes?
    if len(parallels) >= 3:
        spy_6m_vals = [p.forward_returns.get("SPY", {}).get("6m") for p in parallels]
        spy_6m_vals = [v for v in spy_6m_vals if v is not None]
        if spy_6m_vals:
            n_pos = sum(1 for v in spy_6m_vals if v > 0)
            n_neg = sum(1 for v in spy_6m_vals if v < 0)
            n_total = len(spy_6m_vals)
            if n_pos == n_total:
                tone = f"**consistent bullish forward** ({n_pos}/{n_total} паралела с положителен SPY 6m return)"
            elif n_neg == n_total:
                tone = f"**consistent bearish forward** ({n_neg}/{n_total} паралела с отрицателен SPY 6m return)"
            else:
                tone = f"**mixed forward** ({n_pos} положителни, {n_neg} отрицателни, общо {n_total} паралела)"
            lines.append(
                f"През всичките топ {n_total} паралела forward-ите са {tone}. "
                f"Това означава, че текущата signature **не дава ясен directional signal** — "
                f"режимната конфигурация е нестабилна, посоката зависи от макроекономическите "
                f"релизи през следващите 4-6 седмици.\n"
            )

    # Table за справка — всички топ паралели
    lines.append("Детайли за всички паралели:\n")
    lines.append("| Седмица | Cosine | SPY 1m/3m/6m | USO 1m/3m/6m | GLD 1m/3m/6m |")
    lines.append("|---|---:|---:|---:|---:|")
    def cell(returns: dict, key: str) -> str:
        v = returns.get(key)
        return f"{v*100:+.1f}%" if v is not None else "-"
    for p in parallels:
        spy = p.forward_returns.get("SPY", {})
        uso = p.forward_returns.get("USO", {})
        gld = p.forward_returns.get("GLD", {})
        lines.append(
            f"| {p.match_week} | {p.cosine_similarity:.2f} | "
            f"{cell(spy,'1m')}/{cell(spy,'3m')}/{cell(spy,'6m')} | "
            f"{cell(uso,'1m')}/{cell(uso,'3m')}/{cell(uso,'6m')} | "
            f"{cell(gld,'1m')}/{cell(gld,'3m')}/{cell(gld,'6m')} |"
        )
    return "\n".join(lines) + "\n"


def _falsifiers_section(z_results: list[WeeklyZScore],
                        triggered: list[PatternHit],
                        thesis: dict) -> str:
    lines = ["## ⚠️ Какво може да обърне тезата\n"]
    fail_conditions = []

    if thesis["priority"] == "divergence":
        hit: PatternHit = thesis["raw"]
        fail_conditions.append(
            f"Ако следващата седмица {hit.matches[0].symbol} обърне посоката (от "
            f"{hit.matches[0].target_direction} → обратното), pattern-а ще се разпадне."
        )
        # Identify which conditions are weakest (closest to threshold)
        weakest = [m for m in hit.matches if m.matched and
                   abs(m.actual_change_pct) < m.target_min_pct * 1.5]
        if weakest:
            for m in weakest:
                fail_conditions.append(
                    f"{m.symbol} ({m.actual_change_pct:+.1f}%) е близо до прага "
                    f"({m.target_min_pct}%) — лесно може да отпадне следващата седмица."
                )
    elif thesis["priority"] == "extreme_etf":
        r: WeeklyZScore = thesis["raw"]
        fail_conditions.append(
            f"Ако {r.symbol} се върне към trailing mean ({_fmt_pct(r.trailing_mean)}) "
            f"следващата седмица, тезата става епизод не trend."
        )

    # General falsifiers from contradicting signals
    if z_results and triggered:
        # Look for ETF moves that go AGAINST the triggered pattern direction
        pattern_directions = {m.symbol: m.target_direction for hit in triggered for m in hit.matches}
        contradicting = []
        for r in z_results:
            expected = pattern_directions.get(r.symbol)
            if expected is None:
                continue
            actual = "up" if r.weekly_change > 0 else "down"
            if expected != actual:
                contradicting.append(r)
        if contradicting:
            fail_conditions.append(
                "Противоречи на текущата теза: " +
                ", ".join(f"{r.symbol} {_fmt_pct(r.weekly_change)}" for r in contradicting[:3])
            )

    if not fail_conditions:
        fail_conditions.append(
            "_Не са идентифицирани механични falsifiers. Преглеждай макро лещите за "
            "сигнал на режимна смяна (виж раздела за персистни аномалии)._"
        )

    for f in fail_conditions:
        lines.append(f"- {f}")
    return "\n".join(lines) + "\n"


def _watchlist_section(duck) -> str:
    lines = ["## 🔭 Какво да наблюдаваме следващата седмица\n"]

    # Persistent macro anomalies — these are series with structural pressure
    for region in ("US", "EU"):
        try:
            df = persistent_anomalies(region, lookback_weeks=4,
                                      min_occurrences=2, min_abs_z=2.0, duck=duck)
        except Exception:
            continue
        if df.empty:
            continue
        lines.append(f"### {region} макро серии под натиск")
        top = df.head(5)
        for _, r in top.iterrows():
            ext = " · NEW-EXTREME" if r["any_new_extreme"] else ""
            lines.append(
                f"- **{r['series_id']}** ({r['name_bg']}) · "
                f"lens={r['lens']} · |z|={r['mean_abs_z']:.2f}{ext}"
            )
        lines.append("")

    # Pull narrative hints от latest US macro state
    try:
        df = duck.execute(
            "SELECT top_anomalies_json FROM us_macro_state ORDER BY date DESC LIMIT 1"
        ).df()
        if not df.empty:
            anomalies = json.loads(df.iloc[0]["top_anomalies_json"] or "[]")
            hints = [a for a in anomalies if a.get("narrative_hint")]
            if hints:
                lines.append("### US narrative hints от макро лещите")
                for h in hints[:3]:
                    lines.append(f"- **{h['series_id']}**: {h['narrative_hint']}")
                lines.append("")
    except Exception:
        pass

    if len(lines) == 1:
        lines.append("_Няма очевидни watchlist кандидати._")
    return "\n".join(lines) + "\n"


# ────────────────────────────────────────────────────────────────────────────
#  Top-level
# ────────────────────────────────────────────────────────────────────────────

def _rotation_summary(duck, week: WeekWindow) -> str:
    """Кратко prose резюме на rotation events."""
    from .rotation_events import rotation_diff
    parts = []
    for universe in ("us", "eu"):
        deltas = rotation_diff(duck, universe, week)
        if not deltas:
            continue
        # Само stable_winner 1m като headline
        sw = [d for d in deltas if d.quadrant == "stable_winner" and d.horizon == "1m"]
        if sw and (sw[0].entered or sw[0].exited):
            d = sw[0]
            ft_marker = ""
            if d.first_time_ever:
                ft_marker = f" ({len(d.first_time_ever)} за първи път в историята)"
            parts.append(
                f"**{universe.upper()} stable_winners 1m:** {len(d.entered)} entered{ft_marker}, "
                f"{len(d.exited)} exited"
            )
    return ". ".join(parts) if parts else ""


def _vrm_summary(duck) -> tuple[bool, dict | None]:
    """Returns (changed, summary_dict)."""
    try:
        df = duck.execute(
            "SELECT date, regime, ks_status, alignment_score FROM vrm_state ORDER BY date DESC LIMIT 2"
        ).df()
        if len(df) < 2:
            return False, None
        latest, prev = df.iloc[0], df.iloc[1]
        changed = (latest["regime"] != prev["regime"]
                   or latest["ks_status"] != prev["ks_status"])
        summary = (f"режим {prev['regime']} → {latest['regime']}, "
                   f"KS {prev['ks_status']} → {latest['ks_status']}") if changed else ""
        return changed, {"summary": summary, "latest": latest.to_dict(), "prev": prev.to_dict()}
    except Exception:
        return False, None


def _macro_shift_summary(duck, region: str) -> dict | None:
    """Returns dict с {top_lens, top_delta, max_abs_delta} или None."""
    table = f"{region.lower()}_macro_state"
    try:
        df = duck.execute(
            f"SELECT date, labor_score, growth_score, inflation_score, liquidity_score "
            f"FROM {table} ORDER BY date DESC LIMIT 2"
        ).df()
        if len(df) < 2:
            return None
        latest, prev = df.iloc[0], df.iloc[1]
        deltas = {}
        for lens in ("labor", "growth", "inflation", "liquidity"):
            l_val = _safe(latest[f"{lens}_score"])
            p_val = _safe(prev[f"{lens}_score"])
            if l_val is not None and p_val is not None:
                deltas[lens] = l_val - p_val
        if not deltas:
            return None
        top_lens = max(deltas, key=lambda k: abs(deltas[k]))
        return {
            "top_lens": top_lens,
            "top_delta": deltas[top_lens],
            "max_abs_delta": abs(deltas[top_lens]),
            "deltas": deltas,
        }
    except Exception:
        return None


def generate_narrative(target_week: WeekWindow | None = None) -> tuple[str, Path]:
    """Главен entry point — генерира narrative briefing markdown."""
    duck = get_duck()
    week = target_week or current_week()
    log.info("narrative start", extra={"week": week.label})

    # Gather signals
    z_results = scan_universe(duck, CORE_ETFS, week, trailing_n=13, z_threshold=1.5)
    pattern_hits = evaluate_all(week.week_end, duck)
    triggered = [h for h in pattern_hits if h.triggered]
    vrm_changed, vrm_summary = _vrm_summary(duck)
    us_shift = _macro_shift_summary(duck, "US")
    eu_shift = _macro_shift_summary(duck, "EU")
    rotation_text = _rotation_summary(duck, week)

    thesis = _derive_thesis(triggered, z_results, vrm_changed, vrm_summary,
                            us_shift, eu_shift)

    # Build sections
    thesis_md = _thesis_section(thesis, triggered, z_results)
    evidence_md = _evidence_section(z_results, triggered, rotation_text)
    parallels_md = _parallels_section(duck, week, top_k=3)
    falsifiers_md = _falsifiers_section(z_results, triggered, thesis)
    watch_md = _watchlist_section(duck)

    header = (
        f"# Сателитен Разказ — Седмица {week.label}\n"
        f"\n_Период: {week.week_start} → {week.week_end}_  \n"
        f"_Генериран: {pd.Timestamp.utcnow().strftime('%Y-%m-%d %H:%M UTC')}_  \n"
        f"_Тип: narrative (за weekly-story-teller skill). "
        f"За структурирани данни виж [{week.label}.md]({week.label}.md)._\n\n"
    )

    footer = (
        "\n---\n\n## 📋 Линкове\n"
        f"- [Структуриран briefing — {week.label}.md]({week.label}.md)\n"
        "- [Сателит repo](https://github.com/tsvetoslavtsachev/macro-satellite)\n"
        "\n_Този файл е автоматично генериран. weekly-story-teller skill го "
        "консумира директно като source за bullet sheet-а на седмичното видео._\n"
    )

    body = "\n---\n\n".join([
        thesis_md, evidence_md, parallels_md, falsifiers_md, watch_md,
    ])
    md = header + body + footer

    out_dir = REPO_ROOT / "briefings"
    out_dir.mkdir(exist_ok=True)
    path = out_dir / f"narrative_{week.label}.md"
    path.write_text(md, encoding="utf-8")
    log.info("narrative written", extra={"path": str(path),
                                          "thesis_priority": thesis["priority"]})
    return md, path
