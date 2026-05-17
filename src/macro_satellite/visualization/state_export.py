"""AI-readable state.json sidecar generator.

Output: docs/state.json — структуриран snapshot на текущата седмица за direct AI
consumption. WebFetch на този файл дава цялата картина в един JSON, без да се
налага парсване на markdown.

Всички полета произлизат от вече съществуващите analytics модули — никакви
нови изчисления. Това е тънък serialization слой над:
- vrm_state / us_macro_state / eu_macro_state (DuckDB)
- analytics.z_scores.scan_universe + weekly_z
- analytics.divergence_engine.evaluate_all
- analytics.parallels.find_parallels
- analytics.macro_anomalies_expander.persistent_anomalies
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from ..analytics.briefing import CORE_ETFS
from ..analytics.divergence_engine import evaluate_all
from ..analytics.macro_anomalies_expander import persistent_anomalies
from ..analytics.parallels import find_parallels
from ..analytics.weekly_window import (
    WeekWindow,
    current_week,
    trailing_weeks,
)
from ..analytics.z_scores import scan_universe, weekly_z
from ..logging_setup import get_logger
from ..paths import REPO_ROOT
from ..storage.duckdb_conn import get_duck

log = get_logger(__name__)

SCHEMA_VERSION = "1.0"

# Universe за z-score heatmap (без дубликати).
HEATMAP_SYMBOLS: list[str] = [
    "USO", "XLE", "DFEN", "URA", "GLD", "SLV", "GDX",
    "TLT", "IEF", "TIP", "HYG", "LQD",
    "UUP", "DBC",
    "SPY", "QQQ", "IWM",
    "XLF", "XLK", "XLV", "XLP", "XLU",
]


@dataclass(frozen=True)
class StateBundle:
    """In-memory state snapshot. Used by dashboard.py to render without
    recomputing everything that state_export already extracted."""
    week: WeekWindow
    regimes: dict[str, Any]
    week_movements_etf: list[dict[str, Any]]
    triggered_patterns: list[dict[str, Any]]
    all_patterns: list[dict[str, Any]]
    z_heatmap: dict[str, Any]
    parallels: list[dict[str, Any]]
    persistent_us: list[dict[str, Any]]
    persistent_eu: list[dict[str, Any]]


def _clean_value(v: Any) -> Any:
    """Convert pandas/numpy types to plain Python for JSON serialization."""
    if v is None:
        return None
    if isinstance(v, float):
        if math.isnan(v) or math.isinf(v):
            return None
        return v
    if isinstance(v, (pd.Timestamp, datetime)):
        return v.isoformat()
    if isinstance(v, date):
        return v.isoformat()
    if hasattr(v, "item"):
        try:
            return v.item()
        except Exception:
            pass
    return v


def _extract_regimes(duck) -> dict[str, Any]:
    out: dict[str, Any] = {"vrm": None, "us_macro": None, "eu_macro": None}

    try:
        vrm = duck.execute(
            "SELECT date, regime, ks_status, alignment_score, alignment_total, gms_value "
            "FROM vrm_state ORDER BY date DESC LIMIT 1"
        ).df()
        if not vrm.empty:
            r = vrm.iloc[0]
            out["vrm"] = {
                "as_of": _clean_value(r["date"]),
                "regime": _clean_value(r["regime"]),
                "ks_status": _clean_value(r["ks_status"]),
                "alignment_score": _clean_value(r["alignment_score"]),
                "alignment_total": _clean_value(r["alignment_total"]),
                "gms_value": _clean_value(r["gms_value"]),
            }
    except Exception as e:
        log.warning("vrm regime extract failed", extra={"error": str(e)})

    for region in ("us", "eu"):
        table = f"{region}_macro_state"
        try:
            df = duck.execute(
                f"SELECT date, regime_key, regime_label_bg, primary_driver, "
                f"labor_score, growth_score, inflation_score, liquidity_score, "
                f"cross_lens_divergences_count "
                f"FROM {table} ORDER BY date DESC LIMIT 1"
            ).df()
            if df.empty:
                continue
            r = df.iloc[0]
            lens_scores = {}
            for lens in ("labor", "growth", "inflation", "liquidity"):
                v = _clean_value(r[f"{lens}_score"])
                if v is not None:
                    lens_scores[lens] = v
            out[f"{region}_macro"] = {
                "as_of": _clean_value(r["date"]),
                "regime_key": _clean_value(r["regime_key"]),
                "regime_label_bg": _clean_value(r["regime_label_bg"]),
                "primary_driver": _clean_value(r["primary_driver"]),
                "lens_scores": lens_scores,
                "cross_lens_divergences_count": _clean_value(r["cross_lens_divergences_count"]),
            }
        except Exception as e:
            log.warning("macro regime extract failed",
                        extra={"region": region, "error": str(e)})

    return out


def _extract_week_movements(duck, week: WeekWindow,
                             z_threshold: float = 1.5) -> list[dict[str, Any]]:
    """|z| >= threshold ETF movements за target седмицата."""
    results = scan_universe(duck, CORE_ETFS, week, trailing_n=13,
                            z_threshold=z_threshold)
    return [
        {
            "symbol": r.symbol,
            "week": r.week,
            "weekly_change_pct": r.weekly_change * 100.0,
            "z_score": r.z_score,
            "trailing_mean_pct": r.trailing_mean * 100.0,
            "trailing_std_pct": r.trailing_std * 100.0,
            "n_baseline_weeks": r.n_baseline_weeks,
            "price_a": r.price_a,
            "price_b": r.price_b,
            "date_a": r.date_a.isoformat() if r.date_a else None,
            "date_b": r.date_b.isoformat() if r.date_b else None,
        }
        for r in results
    ]


def _extract_patterns(duck, end_date: date) -> tuple[list[dict], list[dict]]:
    """Returns (triggered_only, all_with_status)."""
    hits = evaluate_all(end_date, duck)
    all_p: list[dict] = []
    for h in hits:
        conditions = []
        for m in h.matches:
            actual = (None if pd.isna(m.actual_change_pct)
                      else _clean_value(m.actual_change_pct))
            conditions.append({
                "symbol": m.symbol,
                "target_direction": m.target_direction,
                "target_min_pct": m.target_min_pct,
                "actual_change_pct": actual,
                "matched": bool(m.matched),
                "price_a": _clean_value(m.price_a),
                "price_b": _clean_value(m.price_b),
                "date_a": m.date_a.isoformat() if m.date_a else None,
                "date_b": m.date_b.isoformat() if m.date_b else None,
            })
        all_p.append({
            "pattern_key": h.name,
            "label_bg": h.label_bg,
            "description": h.description,
            "end_date": h.end_date.isoformat(),
            "window_days": h.window_days,
            "n_matched": h.n_matched,
            "n_total": len(h.matches),
            "triggered": bool(h.triggered),
            "conditions": conditions,
        })
    triggered = [p for p in all_p if p["triggered"]]
    return triggered, all_p


def _extract_z_heatmap(duck, target: WeekWindow,
                       n_history_weeks: int = 13,
                       symbols: list[str] | None = None) -> dict[str, Any]:
    """Z-score matrix: symbols × (last n_history_weeks + target).

    БЕЗ ffill — ако (symbol, week) няма достатъчно baseline за z-score, клетката
    е None. Не фалшифицираме свежест.
    """
    syms = symbols or HEATMAP_SYMBOLS
    weeks = trailing_weeks(target, n_history_weeks) + [target]
    week_labels = [w.label for w in weeks]
    week_ends = [w.week_end.isoformat() for w in weeks]

    matrix: list[list[float | None]] = []
    for sym in syms:
        row: list[float | None] = []
        for w in weeks:
            wz = weekly_z(duck, sym, w, trailing_n=13)
            if wz is None or not math.isfinite(wz.z_score):
                row.append(None)
            else:
                row.append(round(wz.z_score, 3))
        matrix.append(row)

    return {
        "symbols": syms,
        "weeks": week_labels,
        "week_ends": week_ends,
        "matrix": matrix,
    }


def _extract_parallels(duck, week: WeekWindow,
                        top_k: int = 3) -> list[dict[str, Any]]:
    parallels = find_parallels(duck, week, top_k=top_k)
    out: list[dict[str, Any]] = []
    for p in parallels:
        forwards: dict[str, dict[str, float]] = {}
        for sym, h_dict in p.forward_returns.items():
            forwards[sym] = {
                h: round(v * 100.0, 2) for h, v in h_dict.items()
                if v is not None
            }
        out.append({
            "target_week": p.target_week,
            "match_week": p.match_week,
            "match_week_end": p.match_week_end.isoformat(),
            "cosine_similarity": round(p.cosine_similarity, 4),
            "n_common_symbols": p.n_common_symbols,
            "forward_returns_pct": forwards,
        })
    return out


def _extract_persistent_anomalies(duck, region: str,
                                    lookback_weeks: int = 4,
                                    min_occurrences: int = 2) -> list[dict[str, Any]]:
    try:
        df = persistent_anomalies(region, lookback_weeks=lookback_weeks,
                                   min_occurrences=min_occurrences,
                                   min_abs_z=2.0, duck=duck)
    except Exception as e:
        log.warning("persistent_anomalies failed",
                    extra={"region": region, "error": str(e)})
        return []
    if df is None or df.empty:
        return []
    out: list[dict[str, Any]] = []
    for _, r in df.head(10).iterrows():
        out.append({
            "code": _clean_value(r["series_id"]),
            "label_bg": _clean_value(r["name_bg"]),
            "lens": _clean_value(r["lens"]),
            "peer_group": _clean_value(r["peer_group"]),
            "occurrences": int(r["occurrences"]),
            "mean_abs_z": round(float(r["mean_abs_z"]), 3),
            "max_abs_z": round(float(r["max_abs_z"]), 3),
            "first_date": _clean_value(r["first_date"]),
            "last_date": _clean_value(r["last_date"]),
            "new_extreme": bool(r["any_new_extreme"]),
        })
    return out


def build_state_bundle(week: WeekWindow | None = None,
                        duck=None) -> StateBundle:
    """Извлича всичко веднъж и връща StateBundle, който dashboard.py консумира
    директно (без повторни DB заявки)."""
    duck = duck or get_duck()
    w = week or current_week()
    log.info("state_export build start", extra={"week": w.label})

    regimes = _extract_regimes(duck)
    movements = _extract_week_movements(duck, w)
    triggered, all_patterns = _extract_patterns(duck, w.week_end)
    z_heatmap = _extract_z_heatmap(duck, w)
    parallels = _extract_parallels(duck, w, top_k=3)
    persist_us = _extract_persistent_anomalies(duck, "US")
    persist_eu = _extract_persistent_anomalies(duck, "EU")

    return StateBundle(
        week=w,
        regimes=regimes,
        week_movements_etf=movements,
        triggered_patterns=triggered,
        all_patterns=all_patterns,
        z_heatmap=z_heatmap,
        parallels=parallels,
        persistent_us=persist_us,
        persistent_eu=persist_eu,
    )


def bundle_to_dict(bundle: StateBundle) -> dict[str, Any]:
    """Serialize StateBundle → JSON-ready dict."""
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "week": {
            "label": bundle.week.label,
            "start": bundle.week.week_start.isoformat(),
            "end": bundle.week.week_end.isoformat(),
        },
        "regimes": bundle.regimes,
        "week_movements_etf": bundle.week_movements_etf,
        "triggered_patterns": bundle.triggered_patterns,
        "all_patterns": bundle.all_patterns,
        "z_heatmap": bundle.z_heatmap,
        "parallels_top3": bundle.parallels,
        "persistent_anomalies": {
            "us": bundle.persistent_us,
            "eu": bundle.persistent_eu,
        },
        "briefing_links": {
            "narrative_md": (
                f"https://raw.githubusercontent.com/tsvetoslavtsachev/macro-satellite/"
                f"main/briefings/narrative_{bundle.week.label}.md"
            ),
            "structured_md": (
                f"https://raw.githubusercontent.com/tsvetoslavtsachev/macro-satellite/"
                f"main/briefings/{bundle.week.label}.md"
            ),
        },
    }


def write_state_json(week: WeekWindow | None = None,
                      output_dir: Path | None = None,
                      duck=None) -> tuple[Path, StateBundle]:
    """Извлича state и пише docs/state.json. Връща (path, bundle) така че
    dashboard.py да може директно да преизползва същия bundle."""
    bundle = build_state_bundle(week=week, duck=duck)
    payload = bundle_to_dict(bundle)
    out_dir = output_dir or (REPO_ROOT / "docs")
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "state.json"
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    log.info("state.json written",
             extra={"path": str(path),
                    "size_kb": path.stat().st_size // 1024,
                    "n_movements": len(bundle.week_movements_etf),
                    "n_triggered": len(bundle.triggered_patterns)})
    return path, bundle
