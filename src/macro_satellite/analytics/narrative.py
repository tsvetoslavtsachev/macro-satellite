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
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

from ..config import MACRO_REGIONS, macro_lenses
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
#  Thesis derivation (П2в / D2)
#  Заглавната теза следва МАКРО-РЕЖИМА, не седмичния ETF-шум:
#    1) VRM режимна/KS промяна → 2) макро режимна ПРОМЯНА (US/EU) →
#    3) стабилният макро режим (default заглавие; седмичната динамика = подточка)
#    → fallback (без режимни данни): старият седмичен ред.
#  Седмичният ред (divergence → extreme |z| → lens shift → moderate → calm)
#  вече произвежда САМО подточката „седмична динамика", не заглавието.
# ────────────────────────────────────────────────────────────────────────────

def _derive_weekly_note(triggered: list[PatternHit],
                        z_results: list[WeeklyZScore],
                        macro_us_shift: dict | None,
                        macro_eu_shift: dict | None) -> dict:
    """Седмичната динамика (старият приоритетен ред, без VRM клона).

    П2в: това вече НЕ е заглавната теза — връща се като подточка към
    режимното заглавие. Заглавие става само във fallback (без режимни данни).
    """

    # triggered divergence pattern (highest match count first)
    if triggered:
        p = sorted(triggered, key=lambda h: -h.n_matched)[0]
        return {
            "priority": "divergence",
            "summary_bg": p.label_bg,
            "description": p.description,
            "raw": p,
        }

    # extreme |z| move (>=2.5σ) — single most-extreme
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

    # Macro lens score shift (>=5 points week-over-week)
    for region, shift in [("US", macro_us_shift), ("EU", macro_eu_shift)]:
        if shift and shift.get("max_abs_delta", 0) >= 5.0:
            return {
                "priority": "macro_lens_shift",
                "summary_bg": (f"{region} macro: значителна промяна в "
                               f"{shift['top_lens']} lens ({shift['top_delta']:+.1f} pts)"),
                "raw": shift,
            }

    # Lower-grade |z| signal
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


def _derive_thesis(triggered: list[PatternHit],
                   z_results: list[WeeklyZScore],
                   vrm_changed: bool,
                   vrm_summary: dict | None,
                   macro_us_shift: dict | None,
                   macro_eu_shift: dict | None,
                   regime_us: dict | None = None,
                   regime_eu: dict | None = None,
                   regime_cn: dict | None = None) -> dict:
    """Връща dict с {priority, summary_bg, raw, weekly}.

    П2в / D2: макро-режимът НАД седмичния divergence. При стабилен режим
    заглавната теза е режимът (не алтернира от седмичния шум); divergence /
    extreme z / lens shift слизат в `weekly` подточката.

    X-пакет: CN влиза в режимния ВХОД — режимна ПРОМЯНА в Китай става заглавие
    само при ИСТИНСКА смяна (`changed`), и то СЛЕД US/EU (US пред EU пред CN) →
    US/EU поведението остава непроменено (те се проверяват първи). Стабилен CN
    режим НЕ титулува (US стабилен остава default-ът); показва се като контекст.
    """
    weekly = _derive_weekly_note(triggered, z_results, macro_us_shift, macro_eu_shift)

    # Priority 1: VRM режимна/KS промяна (режимно събитие, най-рядко)
    if vrm_changed and vrm_summary:
        return {
            "priority": "vrm_shift",
            "summary_bg": f"VRM режимна промяна — {vrm_summary.get('summary', 'виж раздела')}",
            "raw": vrm_summary,
            "weekly": weekly,
        }

    # Priority 2: макро режимна ПРОМЯНА през тази седмица (US пред EU пред CN).
    # CN е последен → US/EU precedence непроменена; CN титулува само ако US/EU НЕ
    # са се сменили И CN има истинска смяна (`changed`).
    for reg in (regime_us, regime_eu, regime_cn):
        if reg and reg.get("changed"):
            return {
                "priority": "macro_regime_shift",
                "summary_bg": (
                    f"{reg['region']} макро режимът се смени: "
                    f"{reg.get('prev_regime_label_bg') or reg.get('prev_regime_key')} → "
                    f"{reg['regime_label_bg']} ({reg['regime_key']})"
                ),
                "raw": reg,
                "weekly": weekly,
            }

    # Priority 3 (default заглавие): стабилният макро режим
    if regime_us:
        since = regime_us.get("stable_since")
        since_str = f" (стабилен от {since})" if since else ""
        return {
            "priority": "macro_regime",
            "summary_bg": (
                f"US макро режим: {regime_us['regime_label_bg']} "
                f"({regime_us['regime_key']}){since_str} — режимът е тезата; "
                f"седмичната динамика е подточка"
            ),
            "raw": regime_us,
            "regime_eu": regime_eu,
            "regime_cn": regime_cn,
            "weekly": weekly,
        }

    # Fallback: без режимни данни → седмичната бележка става заглавие (старото поведение)
    weekly["weekly"] = None
    return weekly


# ────────────────────────────────────────────────────────────────────────────
#  Section generators (return markdown strings)
# ────────────────────────────────────────────────────────────────────────────

def _weekly_detail_lines(weekly: dict, z_results: list[WeeklyZScore]) -> list[str]:
    """Детайлните редове за седмичната динамика (по неин priority).

    Използва се и когато динамиката е подточка (П2в), и във fallback
    когато е заглавие.
    """
    lines: list[str] = []
    p = weekly["priority"]
    if p == "divergence":
        hit: PatternHit = weekly["raw"]
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
        r: WeeklyZScore = weekly["raw"]
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
    return lines


def _thesis_section(thesis: dict, triggered: list[PatternHit],
                    z_results: list[WeeklyZScore]) -> str:
    lines = ["## 🎯 Тезата на седмицата\n"]
    lines.append(f"**{thesis['summary_bg']}**\n")

    p = thesis["priority"]
    weekly = thesis.get("weekly")

    if p == "macro_regime":
        # П2в: режимът е заглавието; EU/CN режими като контекст; динамиката = подточка
        regime_eu = thesis.get("regime_eu")
        if regime_eu:
            lines.append(
                f"EU макро режим: {regime_eu['regime_label_bg']} "
                f"({regime_eu['regime_key']}).\n"
            )
        # X-пакет: CN режим като контекст (стабилен CN не титулува — само истинска
        # смяна прави CN заглавие, priority 2 по-горе).
        regime_cn = thesis.get("regime_cn")
        if regime_cn:
            lines.append(
                f"CN макро режим: {regime_cn['regime_label_bg']} "
                f"({regime_cn['regime_key']}).\n"
            )
    elif p == "macro_regime_shift":
        reg = thesis["raw"]
        since = reg.get("as_of")
        if since:
            lines.append(f"_Режимна снимка към {since}._\n")
    elif p == "vrm_shift":
        pass  # VRM детайлът е в собствения раздел на briefing-а
    else:
        # Fallback (без режимни данни): седмичната бележка е заглавие
        lines.extend(_weekly_detail_lines(thesis, z_results))

    # Седмичната динамика като ПОДТОЧКА към режимното заглавие (П2в)
    if weekly is not None and p in ("macro_regime", "macro_regime_shift", "vrm_shift"):
        lines.append(
            f"**Седмична динамика (подточка — не мени режимната теза):** "
            f"{weekly['summary_bg']}\n"
        )
        lines.extend(_weekly_detail_lines(weekly, z_results))

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

    # П3г-lite / D10: честен етикет — метриката е конструктивно щедра.
    lines.append(
        "> ⚠ **Честен етикет:** cosine върху сурови седмични доходности почти "
        "никога не пада под ~0.78 по конструкция (доминиран от най-волатилните "
        "крака) — винаги „намира близък паралел“. Чети го като **отправна точка "
        "за разглеждане, НЕ доказана режимна близост**. (Демийн + permutation-null "
        "или пенсия = паркирано решение Q3.)\n"
    )

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
    """П3б / D9: механични falsifiers за ВСЯКА теза (не само divergence).

    Две нива: (1) режимен falsifier за заглавната теза (macro_regime /
    macro_regime_shift / vrm_shift), (2) седмичен falsifier по weekly
    приоритета (divergence / extreme_etf / macro_lens_shift / moderate_etf /
    calm). Всяка теза излиза с поне 1 falsifier.
    """
    lines = ["## ⚠️ Какво може да обърне тезата\n"]
    fail_conditions = []

    # П2в: седмичните falsifiers идват от weekly подточката (когато режимът
    # е заглавие); във fallback thesis самата Е седмичната бележка.
    weekly = thesis.get("weekly") or thesis

    # ─── Режимно ниво (заглавната теза) ───
    p = thesis["priority"]
    if p == "macro_regime":
        reg = thesis["raw"]
        fail_conditions.append(
            f"Режимен: следващият {reg['region']} macro snapshot с regime_key ≠ "
            f"`{reg['regime_key']}` сваля заглавната теза (режимът е стабилен от "
            f"{reg.get('stable_since', '—')})."
        )
    elif p == "macro_regime_shift":
        reg = thesis["raw"]
        prev_lbl = reg.get("prev_regime_label_bg") or reg.get("prev_regime_key") or "предишния режим"
        fail_conditions.append(
            f"Режимен: връщане към {prev_lbl} в следващия snapshot = шум на прага "
            f"между режими, не смяна — искай 2 поредни седмици в новия режим "
            f"преди да я разказваш като режимна."
        )
    elif p == "vrm_shift":
        fail_conditions.append(
            "Режимен: VRM връщане към предишния режим/KS статус следващата "
            "седмица = единичен flip, не режимна смяна."
        )

    # ─── Седмично ниво (по weekly приоритета) ───
    if weekly["priority"] == "divergence":
        hit: PatternHit = weekly["raw"]
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
    elif weekly["priority"] == "extreme_etf":
        r: WeeklyZScore = weekly["raw"]
        fail_conditions.append(
            f"Ако {r.symbol} се върне към trailing mean ({_fmt_pct(r.trailing_mean)}) "
            f"следващата седмица, тезата става епизод не trend."
        )
    elif weekly["priority"] == "macro_lens_shift":
        shift = weekly["raw"]
        fail_conditions.append(
            f"Ако {shift['top_lens']} score върне поне половината от делтата "
            f"({shift['top_delta']:+.1f} pts) в следващия седмичен snapshot, "
            f"промяната е snapshot-шум, не тренд — изчакай второ потвърждение."
        )
    elif weekly["priority"] == "moderate_etf":
        r: WeeklyZScore = weekly["raw"]
        fail_conditions.append(
            f"Ако {r.symbol} се върне под 1σ следващата седмица, и това "
            f"„най-силно движение“ е шум — седмицата остава без пазарен сигнал."
        )
    elif weekly["priority"] == "calm":
        fail_conditions.append(
            "Едно |z| ≥ 1.5σ движение, триггериран pattern или режимна смяна "
            "следващата седмица прекратява „спокойния“ прочит."
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
        # П3б: не бива да се стига дотук (всяка комбинация има поне 1 ред по-горе)
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
    for region in MACRO_REGIONS:
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
#  Base rates (X-пакет / Тухла 3б) — gap-журналът wire-нат в наратива
#  Дисциплина (виж machine_base_rate.md образеца): N (n_episodes) експлицитен,
#  count/N вместо голи проценти, уговорките (revision bias + velocity asymmetry),
#  n < MIN_EPISODES → „недостатъчно" не процент.
# ────────────────────────────────────────────────────────────────────────────

_OUTCOME_ORDER = ("market_leads", "economy_leads", "meet", "widen")
_OUTCOME_BG = {
    "market_leads": "пазарът води",
    "economy_leads": "икономиката води",
    "meet": "срещат се",
    "widen": "разширяване",
}


def _base_rate_section() -> str:
    """Историческите base rates за ТЕКУЩАТА gap-конфигурация per регион.

    Чете gap-журнала (US/EU/CN `machine_episodes[_<region>].parquet` +
    `gap_series[_<region>].parquet`). За всеки регион с журнал: дистрибуцията на
    изходите (пазар/икономика/срещат/разширяване) за конфигурацията на последния
    gap, с N епизоди експлицитен и уговорките. Гола проценти НЕ се пише — винаги
    count/N + N. n < MIN_EPISODES → „недостатъчно".
    """
    from .journal.calibration import MIN_EPISODES, machine_base_rate
    from .journal.resolution import load_gap_series

    lines = ["## 📐 Базови нива (gap-журнал — исторически прецедент)\n"]
    lines.append(
        "_Икон-крак ↔ пазари-крак „gap\" журнал. Базите са look-ahead-biased prior "
        "(виж уговорките), НЕ real-time edge. Дистрибуцията е за конфигурацията на "
        "последния изчислен gap, с N епизоди експлицитен._\n"
    )

    any_region = False
    for region in MACRO_REGIONS:
        try:
            gs = load_gap_series(region)
        except Exception:
            continue
        if gs is None or gs.empty:
            continue
        last = gs.iloc[-1]
        gap = _safe(last.get("gap"))
        if gap is None:
            continue
        config_key = "gap_pos" if float(gap) >= 0 else "gap_neg"
        week_label = str(last.get("week"))
        try:
            mbr = machine_base_rate(region, post_reflation=False)
        except Exception:
            mbr = {}
        buckets = mbr.get(config_key)
        if not buckets:
            continue
        any_region = True
        lines.append(
            f"### {region} · конфигурация `{config_key}` "
            f"(gap {float(gap):+.2f}, към {week_label})\n"
        )
        for y in sorted(buckets):
            b = buckets[y]
            n_eps = b["n_episodes"]
            nr = b["n_resolved"]
            if n_eps < MIN_EPISODES:
                lines.append(
                    f"- {y} седм. напред: n_eps={n_eps} → недостатъчно "
                    f"(не процент — n-дисциплина)"
                )
                continue
            parts = []
            for oc in _OUTCOME_ORDER:
                c = b["counts"].get(oc, 0)
                if not c:
                    continue
                pct = (100.0 * c / nr) if nr else 0.0
                parts.append(f"{_OUTCOME_BG[oc]} {c}/{nr} ({pct:.0f}%)")
            dist = " · ".join(parts) if parts else "—"
            lines.append(f"- {y} седм. напред (**N={n_eps} еп.**, {nr} resolved): {dist}")
        lines.append("")

    if not any_region:
        lines.append("_Няма наличен gap-журнал за база (пусни journal-backfill)._")
        return "\n".join(lines) + "\n"

    lines.append("**Уговорки (важат за всички бази — НЕ ги чети като real-time edge):**")
    lines.append(
        "- ⚠ Revision/vintage bias: базите се реконструират от ревизиран cache → "
        "best-case (perfect-hindsight), НЕ real-time постижими (виж machine_base_rate.md)."
    )
    lines.append(
        "- ⚠ Velocity asymmetry: икон-осът е структурно бавен (месечни данни) → "
        "„пазарът води\" е ДО ГОЛЯМА СТЕПЕН механичен. Информативни са "
        "„разширяване\"-ставките + pos/neg асиметрията, не „пазарът води %\"."
    )
    lines.append(
        f"- n < {MIN_EPISODES} епизода → „недостатъчно\", не процент (n-дисциплина)."
    )
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


def _macro_regime_summary(duck, region: str, week: WeekWindow) -> dict | None:
    """As-of режимна снимка за седмицата (П2в / D2).

    Чете последния ред ≤ week_end (НЕ глобалния latest — иначе исторически
    re-run чете бъдещето). Връща и:
      - stable_since: началото на непрекъснатия завършващ run от същия режим;
      - changed: дали режимът се е сменил ПРЕЗ тази седмица (спрямо последния
        ред преди week_start) — календарно, не snapshot-подредба.
    """
    table = f"{region.lower()}_macro_state"
    try:
        df = duck.execute(
            f"SELECT date, regime_key, regime_label_bg FROM {table} "
            f"WHERE date <= ? ORDER BY date DESC LIMIT 60",
            [week.week_end],
        ).df()
        if df.empty:
            return None
        latest = df.iloc[0]
        current_key = latest["regime_key"]

        stable_since = latest["date"]
        for _, row in df.iterrows():
            if row["regime_key"] != current_key:
                break
            stable_since = row["date"]

        prev = df[df["date"] < pd.Timestamp(week.week_start)]
        changed = bool(len(prev)) and prev.iloc[0]["regime_key"] != current_key

        def _d(x):
            return str(pd.Timestamp(x).date())

        return {
            "region": region,
            "regime_key": current_key,
            "regime_label_bg": latest["regime_label_bg"],
            "as_of": _d(latest["date"]),
            "stable_since": _d(stable_since),
            "changed": changed,
            "prev_regime_key": prev.iloc[0]["regime_key"] if len(prev) else None,
            "prev_regime_label_bg": prev.iloc[0]["regime_label_bg"] if len(prev) else None,
        }
    except Exception:
        return None


def _macro_shift_summary(duck, region: str, week: WeekWindow) -> dict | None:
    """WoW lens-score промяна върху КАЛЕНДАРНИ седмици (П3в / D8).

    Сравнява последния snapshot В текущата седмица срещу последния snapshot
    В предходната календарна седмица. Старият `ORDER BY date DESC LIMIT 2`
    вземаше последните 2 РАЗЛИЧНИ snapshot-а независимо от седмицата →
    двойно броене при замразен prev (W20≡W21 идентични делти) и
    многоседмичен телескоп, представен като WoW (W23 „−42.1 pts").
    Липсва snapshot в някоя от двете седмици → None (няма честно WoW).

    Returns dict с {top_lens, top_delta, max_abs_delta} или None.
    """
    table = f"{region.lower()}_macro_state"
    lenses = macro_lenses(region)
    lens_sel = ", ".join(f"{l}_score" for l in lenses)
    prev_week_start = week.week_start - timedelta(days=7)
    try:
        cur_df = duck.execute(
            f"SELECT date, {lens_sel} FROM {table} "
            f"WHERE date >= ? AND date <= ? ORDER BY date DESC LIMIT 1",
            [week.week_start, week.week_end],
        ).df()
        prev_df = duck.execute(
            f"SELECT date, {lens_sel} FROM {table} "
            f"WHERE date >= ? AND date < ? ORDER BY date DESC LIMIT 1",
            [prev_week_start, week.week_start],
        ).df()
        if cur_df.empty or prev_df.empty:
            return None
        latest, prev = cur_df.iloc[0], prev_df.iloc[0]
        deltas = {}
        for lens in lenses:
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
    us_shift = _macro_shift_summary(duck, "US", week)
    eu_shift = _macro_shift_summary(duck, "EU", week)
    regime_us = _macro_regime_summary(duck, "US", week)
    regime_eu = _macro_regime_summary(duck, "EU", week)
    regime_cn = _macro_regime_summary(duck, "CN", week)
    rotation_text = _rotation_summary(duck, week)

    thesis = _derive_thesis(triggered, z_results, vrm_changed, vrm_summary,
                            us_shift, eu_shift, regime_us, regime_eu, regime_cn)

    # Build sections
    thesis_md = _thesis_section(thesis, triggered, z_results)
    evidence_md = _evidence_section(z_results, triggered, rotation_text)
    parallels_md = _parallels_section(duck, week, top_k=3)
    falsifiers_md = _falsifiers_section(z_results, triggered, thesis)
    base_rate_md = _base_rate_section()
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
        thesis_md, evidence_md, parallels_md, falsifiers_md, base_rate_md, watch_md,
    ])
    md = header + body + footer

    out_dir = REPO_ROOT / "briefings"
    out_dir.mkdir(exist_ok=True)
    path = out_dir / f"narrative_{week.label}.md"
    path.write_text(md, encoding="utf-8")
    log.info("narrative written", extra={"path": str(path),
                                          "thesis_priority": thesis["priority"]})
    return md, path
