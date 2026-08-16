"""INIT-22 E1b (organism vertical, mandate organism/MANDATE-E1B-external-citizens.md,
2026-07-04) -- the SECOND repackager, living at macro-satellite (the AGGREGATOR;
"data-core COMPUTES, macro-satellite AGGREGATES" -- consilium canon Д-К2).

The data-core repackager (migrations/e1_organism_cards/export_organism_cards.py)
reads ONLY data-core's own state/ + canonical/, so it structurally CANNOT card the
12 organs that live OUTSIDE data-core (audit AUDIT-GROUP-B-2026-07-04 §Е1b). This
module cards those 12 -- the external citizens -- into the SAME locked E1 schema v1,
in an INTERNAL satellite file (docs/organism_cards_external.json). The public
showcase (docs/organism.json) is NOT touched (mandate §Контекст.3, gate Г4).

CARDINAL RULE (E1 contract, opening + s6; E1b mandate "Кардинални правила"): this is
a REPACKAGER. Every field traces to an ALREADY-generated artifact. ZERO new numbers,
ZERO new analytical logic. It only READS structured outputs and copies values
verbatim; it never computes a threshold, an aggregate, or a classification. The only
derived values are STRUCTURAL bookkeeping (a row/constituent count, a max-of-dates
frontier, a stale flag = a date comparison) -- never analytical.

reading = null on EVERY external card (E1 s3 + E1b mandate item 1): none of these
organs carries a pre-existing confirm/diverge logic the way S10/S11 do, so a reading
here would be a NEW classification through the back door. null means "requires
E4/separate decision". (The macro US/EU/CN card -- the blind spot, mandate item 2 --
is exactly where E4 will later compare the macro floor against the VRM regime; but
E1b only makes the card exist, it does NOT compute the divergence.)

PRIORITY #1 (mandate item 2): the macro regime from the three regional dashboards
(US/EU/CN) -- the organism's most important blind spot (the VRM-regime <-> macro-
table divergence is invisible to the card layer today). ⚠️ The China composite is a
DIFFERENT methodology (percentile-based composite_score vs the US/EU tanh-z lens
scores) -- the card SAYS this in `measures`, it does not hide it (Г7 is a separate
open decision; this module does NOT resolve it).

Source strategy (deterministic, CI-reachable, degrade-safe -- mirrors the proven
organism_export.py pattern of disk + URL-fetch):
  * macro US/EU/CN  <- satellite DuckDB {us,eu,cn}_macro_state (one substrate for all
                       three; PIT; fresh from each collect)
  * momentum twins  <- DuckDB sp500_momentum / stoxx600_momentum
  * rotation twins  <- DuckDB rotation_us / rotation_eu
  * stock-selection <- DuckDB stock_selection
  * satellite synth <- own docs/state.json on disk (satellite is the producer)
  * funding/barometer/etf-rr/hype <- public GitHub Pages JSON (URL fetch, degrade-safe)
  * oil             <- data-core canonical oil_*.json via DATACORE_STATE_DIR sibling
                       (degrade-safe: absent checkout -> card unavailable, not silent)

Determinism (E1b gates Г3/Г4): all I/O is isolated in load_sources(); build(sources)
is a PURE function over already-extracted primitives, so a replay over the SAME
sources is byte-identical. A missing/unreachable source degrades LOUDLY -- the card
carries available:false or a stale flag, never a silent old value.

stale (mandate item 3): a source older than its cadence tolerance carries stale=True
in `state` (fail-loud, not a quiet old card).

Run (write, also what run_daily invokes):  python -m macro_satellite external-cards
Check (verify determinism, no write):       python -m macro_satellite external-cards --check
"""
from __future__ import annotations

import json
import math
import os
from collections import OrderedDict
from datetime import date, datetime
from pathlib import Path
from typing import Any

from ..logging_setup import get_logger
from ..paths import REPO_ROOT
from ..utils.http import fetch_json

log = get_logger(__name__)

GENERATOR_VERSION = "1.0.0"     # bump on ANY change to what/how cards are emitted
CARD_SCHEMA = "v1"              # E1 s2 locked schema version (shared with data-core)
OUT_NAME = "organism_cards_external.json"

# Public GitHub Pages endpoints (verified 200, 2026-07-04). Same channel style
# organism_export.py already fetches; degrade-safe on failure.
FUNDING_URL = "https://tsvetoslavtsachev.github.io/treasury-funding-radar/data/funding_state.json"
BAROMETER_URL = "https://tsvetoslavtsachev.github.io/ETF-rotationradar/barometer_feed.json"
ETF_RR_URL = "https://tsvetoslavtsachev.github.io/ETF-rotationradar/data.json"
HYPE_URL = "https://tsvetoslavtsachev.github.io/ai-hype-monitor/data/hype_index.json"

# Cadence -> stale tolerance in days (mandate item 3). Weekly channels get a week +
# buffer; daily channels a few days; the macro tables inherit the dashboards.yaml
# 7d convention. These mirror the satellite's own stale_tolerable_days philosophy
# (a source lag is the SOURCE's fault -> flag, don't crash).
STALE_TOL_DAYS = {
    "daily": 4,
    "weekly": 10,
    "monthly": 40,
}


def _p(text: str) -> None:
    """cp1252-safe console print (the file itself stays UTF-8)."""
    print(str(text).encode("ascii", "replace").decode("ascii"))


def _clean(v: Any) -> Any:
    """pandas/numpy/date -> plain JSON-serializable python. Pure copy; a value is
    only type-normalized (float NaN/Inf -> None, numpy scalar -> python), NEVER
    transformed analytically."""
    if v is None:
        return None
    if isinstance(v, float):
        return None if (math.isnan(v) or math.isinf(v)) else v
    if isinstance(v, bool):
        return v
    if isinstance(v, (datetime,)):
        return v.isoformat()
    if isinstance(v, date):
        return v.isoformat()
    if hasattr(v, "item"):
        try:
            return v.item()
        except Exception:
            pass
    return v


def _iso_date(v: Any) -> str | None:
    """Coerce a value to an ISO 'YYYY-MM-DD' string (the card as_of convention)."""
    if v is None:
        return None
    if isinstance(v, datetime):
        return v.date().isoformat()
    if isinstance(v, date):
        return v.isoformat()
    s = str(v)
    return s[:10] if len(s) >= 10 else s


def _stale(as_of_iso: str | None, cadence: str, ref: date) -> bool:
    """Structural staleness = a date comparison (NOT an analytical judgement).
    Missing as_of -> True (a card with no vintage is by definition not fresh)."""
    if not as_of_iso:
        return True
    try:
        d = date.fromisoformat(as_of_iso[:10])
    except (ValueError, TypeError):
        return True
    tol = STALE_TOL_DAYS.get(cadence, 10)
    return (ref - d).days > tol


def _card(organ_id, floor, taxonomy_layer, measures, cadence, horizon,
          state, reading, epistemic_label, as_of, source):
    """Assemble one card in the LOCKED E1 s2 field order (identical to the data-core
    _card). No field is added or dropped -- schema v1 is fixed; extension is a
    Д-decision, not code."""
    return OrderedDict([
        ("organ_id", organ_id),
        ("floor", floor),
        ("taxonomy_layer", taxonomy_layer),
        ("measures", measures),
        ("cadence", cadence),
        ("horizon", horizon),
        ("state", state),
        ("reading", reading),           # ALWAYS None here (E1 s3 / E1b item 1)
        ("epistemic_label", epistemic_label),
        ("as_of", as_of),
        ("source", source),
        ("schema_version", CARD_SCHEMA),
    ])


# ── I/O layer (all impurity lives here) ──────────────────────────────────────

def _macro_from_duck(duck, region: str) -> dict[str, Any] | None:
    """Latest macro_state row for a region as plain primitives, or None if empty.
    READ-ONLY; verbatim copy of the source columns the dashboards already computed."""
    table = f"{region}_macro_state"
    cols = ["date", "regime_key", "regime_label_bg", "primary_driver",
            "cross_lens_divergences_count"]
    try:
        df = duck.execute(
            f"SELECT {', '.join(cols)} FROM {table} ORDER BY date DESC LIMIT 1"
        ).df()
    except Exception as e:  # noqa: BLE001
        log.warning("macro extract failed", extra={"region": region, "error": str(e)})
        return None
    if df.empty:
        return None
    r = df.iloc[0]
    out = {c: _clean(r[c]) for c in cols}
    # composite_score exists ONLY on China (percentile methodology) -- carry it iff
    # the column exists, and record which methodology so the card is honest (Г7).
    has_comp = "composite_score" in {d[0] for d in duck.execute(f"DESCRIBE {table}").fetchall()}
    if has_comp:
        c = duck.execute(
            f"SELECT composite_score FROM {table} ORDER BY date DESC LIMIT 1"
        ).fetchone()
        out["composite_score"] = _clean(c[0]) if c else None
    out["as_of"] = _iso_date(out.pop("date"))
    out["methodology"] = "percentile-composite" if has_comp else "tanh-z-lens"
    return out


def _vrm_from_duck(duck) -> dict[str, Any] | None:
    """Latest live VRM regime (data-core overlay) -- carried alongside the macro card
    for context so the blind-spot divergence is READABLE side by side (still no
    reading computed; E4 territory)."""
    try:
        df = duck.execute(
            "SELECT date, regime FROM vrm ORDER BY date DESC LIMIT 1"
        ).df()
    except Exception as e:  # noqa: BLE001
        log.warning("vrm extract failed", extra={"error": str(e)})
        return None
    if df.empty or df.iloc[0]["regime"] is None:
        return None
    r = df.iloc[0]
    return {"regime": _clean(r["regime"]), "as_of": _iso_date(r["date"])}


def _twin_from_duck(duck, table: str, score_col: str) -> dict[str, Any] | None:
    """Summarized card body over a per-name ranking table (momentum/rotation/stock-
    selection): the latest snapshot's row count + its date. NO cross-name aggregate
    (an average score would be a new number) -- only structural counts + the frontier.
    """
    try:
        df = duck.execute(
            f"SELECT max(date) AS d, count(*) FILTER (WHERE date = "
            f"(SELECT max(date) FROM {table})) AS n_latest, "
            f"count(DISTINCT date) AS n_dates FROM {table}"
        ).df()
    except Exception as e:  # noqa: BLE001
        log.warning("twin extract failed", extra={"table": table, "error": str(e)})
        return None
    if df.empty or df.iloc[0]["d"] is None:
        return None
    r = df.iloc[0]
    return {
        "as_of": _iso_date(r["d"]),
        "n_names_latest": int(r["n_latest"]) if r["n_latest"] is not None else None,
        "n_snapshots": int(r["n_dates"]) if r["n_dates"] is not None else None,
        "score_field": score_col,
    }


def _try_fetch(url: str) -> dict[str, Any] | None:
    try:
        return fetch_json(url)
    except Exception as e:  # noqa: BLE001 -- honest degrade, never hidden
        log.warning("external source fetch failed", extra={"url": url, "error": str(e)})
        return None


def _oil_from_canonical(state_dir: Path | None) -> dict[str, Any] | None:
    """The 6 oil_* canonical series from data-core (each verbatim: latest value +
    as_of). state_dir is DATACORE_STATE_DIR/../canonical (the sibling of the state
    dir the organism_export already resolves). Absent checkout -> None -> card
    unavailable (degrade-safe, not silent)."""
    if state_dir is None:
        return None
    canon = state_dir.parent / "canonical"
    if not canon.exists():
        return None
    series = {}
    for p in sorted(canon.glob("oil_*.json")):
        try:
            recs = json.loads(p.read_text(encoding="utf-8"))
            rec = recs[-1] if isinstance(recs, list) else recs
            series[rec.get("series_id", p.stem)] = {
                "value": _clean(rec.get("value")),
                "as_of": _iso_date(rec.get("as_of")),
            }
        except Exception as e:  # noqa: BLE001
            log.warning("oil series read failed", extra={"path": str(p), "error": str(e)})
    if not series:
        return None
    return series


def _load_state_json(docs: Path) -> dict[str, Any] | None:
    p = docs / "state.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        log.warning("state.json read failed", extra={"path": str(p), "error": str(e)})
        return None


def load_sources(duck=None, docs: Path | None = None,
                 fetch: bool = True) -> dict[str, Any]:
    """Extract every source ONCE into plain primitives (the ONLY impure step).

    Returns a dict build() consumes. `fetch=False` skips the URL calls (verify uses
    this for a network-free, deterministic replay over an in-memory snapshot). The
    returned dict is JSON-plain, so build() over it is a pure, byte-stable function.
    """
    from ..storage.duckdb_conn import get_duck
    duck = duck or get_duck()
    docs = docs or (REPO_ROOT / "docs")

    state_dir = os.environ.get("DATACORE_STATE_DIR")
    oil = _oil_from_canonical(Path(state_dir)) if state_dir else None

    src: dict[str, Any] = {
        "macro": {r: _macro_from_duck(duck, r) for r in ("us", "eu", "cn")},
        "vrm": _vrm_from_duck(duck),
        "momentum_us": _twin_from_duck(duck, "sp500_momentum", "momentum_score"),
        "momentum_eu": _twin_from_duck(duck, "stoxx600_momentum", "momentum_score"),
        "rotation_us": _twin_from_duck(duck, "rotation_us", "current_rank/quadrant"),
        "rotation_eu": _twin_from_duck(duck, "rotation_eu", "current_rank/quadrant"),
        "stock_selection": _twin_from_duck(duck, "stock_selection", "composite_score"),
        "satellite_state": _load_state_json(docs),
        "oil": oil,
        # URL-fetched (degrade-safe). None on failure -> available:false card.
        "funding": _try_fetch(FUNDING_URL) if fetch else None,
        "barometer": _try_fetch(BAROMETER_URL) if fetch else None,
        "etf_rr": _try_fetch(ETF_RR_URL) if fetch else None,
        "hype": _try_fetch(HYPE_URL) if fetch else None,
        "_fetch_used": fetch,
    }
    return src


# ── Pure build (deterministic over `sources`) ────────────────────────────────

def _unavail(organ_id, floor, layer, measures, cadence, horizon, label, note):
    """A card for a source that failed to load: available:false in state, as_of=None.
    Fail-loud (S14 honest dead channel), never a silent omission or stale value."""
    return _card(organ_id, floor, layer, measures, cadence, horizon,
                 OrderedDict([("available", False), ("note", note)]),
                 None, label, None, note)


def build(sources: dict[str, Any], ref_date: str | None = None) -> OrderedDict:
    """Pure, deterministic. Emits the 12 external-citizen cards from already-extracted
    `sources`. ref_date (ISO) pins the staleness reference; defaults to the newest
    as_of seen across sources so the output stays byte-stable for unchanged inputs
    (no wallclock -> a replay over the same sources is byte-identical, gate Г3)."""
    cards: list[OrderedDict] = []

    # Determine a data-driven reference date (max as_of across all sources) so
    # staleness is computed WITHOUT a wallclock (keeps the file byte-stable).
    if ref_date is None:
        seen: list[str] = []
        for m in (sources.get("macro") or {}).values():
            if m and m.get("as_of"):
                seen.append(m["as_of"])
        for k in ("momentum_us", "momentum_eu", "rotation_us", "rotation_eu",
                  "stock_selection"):
            s = sources.get(k)
            if s and s.get("as_of"):
                seen.append(s["as_of"])
        for k in ("funding", "barometer", "etf_rr"):
            s = sources.get(k)
            if s and s.get("as_of"):
                seen.append(_iso_date(s["as_of"]))
        ref = max((date.fromisoformat(x[:10]) for x in seen if x), default=date(1970, 1, 1))
    else:
        ref = date.fromisoformat(ref_date[:10])

    def mk_state(od: OrderedDict, as_of: str | None, cadence: str) -> OrderedDict:
        """Attach a structural stale flag (a date comparison) to a state body."""
        od["stale"] = _stale(as_of, cadence, ref)
        return od

    # 1) MACRO US/EU/CN -- PRIORITY #1, the blind spot (mandate item 2) ----------#
    macro = sources.get("macro") or {}
    vrm = sources.get("vrm")
    regions_state = OrderedDict()
    macro_asof: list[str] = []
    for geo in ("us", "eu", "cn"):
        m = macro.get(geo)
        if not m:
            regions_state[geo] = OrderedDict([("available", False)])
            continue
        regions_state[geo] = OrderedDict([
            ("regime_key", m.get("regime_key")),
            ("regime_label_bg", m.get("regime_label_bg")),
            ("primary_driver", m.get("primary_driver")),
            ("cross_lens_divergences", m.get("cross_lens_divergences_count")),
            ("composite_score", m.get("composite_score")),   # None for US/EU
            ("methodology", m.get("methodology")),
            ("as_of", m.get("as_of")),
        ])
        if m.get("as_of"):
            macro_asof.append(m["as_of"])
    macro_state = OrderedDict([
        ("regions", regions_state),
        # Carry the live VRM regime verbatim so the divergence is READABLE side by
        # side. NO reading/verdict is computed -- that is E4 (mandate item 2).
        ("vrm_regime", (vrm or {}).get("regime")),
        ("vrm_as_of", (vrm or {}).get("as_of")),
        ("note", "China composite_score = percentile methodology; US/EU = tanh-z "
                 "lens scores (Г7 open). reading=null: VRM<->macro divergence is E4."),
    ])
    macro_frontier = max(macro_asof) if macro_asof else None
    cards.append(_card(
        "macro-regime", "macro", "belt",
        "Макро режим US/EU/CN от трите regional табла (растеж x инфлация) + жив VRM "
        "режим за сравнение. Разминаването VRM<->табла е сляпата точка на обсерваторията.",
        "weekly", "1-3м",
        mk_state(macro_state, macro_frontier, "weekly"),
        None, "context", macro_frontier,
        "satellite DuckDB {us,eu,cn}_macro_state + vrm (data-core-live overlay)"))

    # 2) Barometer (10 behavioral dislocations) -- EASY --------------------------#
    baro = sources.get("barometer")
    if baro:
        conf = baro.get("confluence") or {}
        b_asof = _iso_date(baro.get("as_of"))
        snap = baro.get("snapshot") or []
        indicators = OrderedDict()
        for it in snap:
            if isinstance(it, dict) and it.get("indicator"):
                indicators[it["indicator"]] = OrderedDict([
                    ("value", _clean(it.get("value"))),
                    ("zone", it.get("zone")),
                    ("trend", it.get("trend")),
                ])
        b_state = OrderedDict([
            ("alarm_count", conf.get("alarm_count")),
            ("base_count", conf.get("base_count")),
            ("net", conf.get("net")),
            ("has_confluence", conf.get("has_confluence")),
            ("direction", conf.get("direction")),
            ("n_indicators", len(indicators)),
            ("indicators", indicators),
        ])
        cards.append(_card(
            "barometer", "indicator", "belt",
            "Барометър на поведенческите дислокации -- 10 индикатора (HY-spread, "
            "XLE/SPY, GLD/TLT, VIX, breakeven, MOVE, HYG/LQD, XLY/XLP, IWM/SPY, VUG/VTV).",
            "weekly", "седмица",
            mk_state(b_state, b_asof, "weekly"),
            None, "validated", b_asof,
            "ETF-rotationradar/barometer_feed.json (snapshot[] + confluence{})"))
    else:
        cards.append(_unavail(
            "barometer", "indicator", "belt",
            "Барометър на поведенческите дислокации (10 индикатора).",
            "weekly", "седмица", "validated",
            "barometer_feed.json недостъпен"))

    # 3) Treasury Funding Radar (5 lamps) -- EASY --------------------------------#
    funding = sources.get("funding")
    if funding:
        f_asof = _iso_date(funding.get("as_of"))
        f_state = OrderedDict([
            ("verdict", funding.get("verdict")),
            ("composite_score", _clean(funding.get("composite_score"))),
            ("lamp_status", funding.get("lamp_status") or {}),
            ("any_dead_source", funding.get("any_dead_source")),
        ])
        cards.append(_card(
            "funding-radar", "indicator", "belt",
            "Treasury Funding Radar -- 5 лампи за стрес във финансирането на щатския "
            "дълг (verdict + composite + lamp_status 1..5). Постоянен същодневен сензор.",
            "weekly", "седмица",
            mk_state(f_state, f_asof, "weekly"),
            None, "context", f_asof,
            "treasury-funding-radar/funding_state.json"))
    else:
        cards.append(_unavail(
            "funding-radar", "indicator", "belt",
            "Treasury Funding Radar -- 5 лампи за funding стрес.",
            "weekly", "седмица", "context",
            "funding_state.json недостъпен"))

    # 4) ETF Rotation Radar -- EASY (summarized over etfs[]) ---------------------#
    etf = sources.get("etf_rr")
    if etf:
        e_asof = _iso_date(etf.get("as_of"))
        etfs = etf.get("etfs") or []
        e_state = OrderedDict([
            ("n_etfs", len(etfs)),
            ("categories_field", "per-ETF rank/quadrant/delta_1m/delta_3m в etfs[]"),
        ])
        cards.append(_card(
            "etf-rotation", "sectors", "belt",
            f"ETF Rotation Radar -- ранг/квадрант/delta за {len(etfs)} ETF-а (относителна сила "
            "спрямо бенчмарк).",
            "weekly", "1-3м",
            mk_state(e_state, e_asof, "weekly"),
            None, "context", e_asof,
            "ETF-rotationradar/data.json (etfs[])"))
    else:
        cards.append(_unavail(
            "etf-rotation", "sectors", "belt",
            "ETF Rotation Radar -- ранг/квадрант за ETF вселена.",
            "weekly", "1-3м", "context",
            "data.json недостъпен"))

    # 5) Oil (6 canonical series) -- EASY (data-core canonical) ------------------#
    oil = sources.get("oil")
    if oil:
        o_asof = max((v.get("as_of") for v in oil.values() if v.get("as_of")),
                     default=None)
        o_state = OrderedDict([
            ("n_series", len(oil)),
            ("series", OrderedDict(sorted(oil.items()))),
        ])
        cards.append(_card(
            "oil", "indicator", "belt",
            f"Петролен сензор -- {len(oil)} канонични серии (WTI close, Brent-WTI спред, "
            "M1-M2, EIA девиация, COT персентил, Hormuz transit).",
            "weekly", "седмица",
            mk_state(o_state, o_asof, "weekly"),
            None, "context", o_asof,
            "data-core canonical oil_*.json (6 series)"))
    else:
        cards.append(_unavail(
            "oil", "indicator", "belt",
            "Петролен сензор -- 6 канонични серии.",
            "weekly", "седмица", "context",
            "data-core canonical oil_*.json недостъпен (без DATACORE_STATE_DIR checkout)"))

    # 6) AI Hype Monitor -- EASY -------------------------------------------------#
    hype = sources.get("hype")
    if hype:
        h_asof = _iso_date(hype.get("updated_at")) if hype.get("updated_at") else None
        # updated_at is 'DD.MM.YYYY HH:MM' (non-ISO) -> parse the date part only.
        if h_asof and "." in str(hype.get("updated_at", "")):
            try:
                dd, mm, yy = str(hype["updated_at"]).split()[0].split(".")
                h_asof = f"{yy}-{mm}-{dd}"
            except (ValueError, IndexError):
                h_asof = None
        comps = hype.get("components") or {}
        comp_scores = OrderedDict(
            (k, _clean(v.get("score")) if isinstance(v, dict) else None)
            for k, v in comps.items())
        h_state = OrderedDict([
            ("hype_score", _clean(hype.get("hype_score"))),
            ("zone_label", (hype.get("zone") or {}).get("label")
                if isinstance(hype.get("zone"), dict) else hype.get("zone")),
            ("quarter", hype.get("quarter")),
            ("prev_score", _clean(hype.get("prev_score"))),
            ("change", _clean(hype.get("change"))),
            ("components", comp_scores),
        ])
        cards.append(_card(
            "ai-hype", "indicator", "conditional",
            "AI Hype Monitor -- индекс 0-100 (momentum + реторика + оценки). Продукт "
            "в разработка (чертожна дъска, не клиентски сигнал).",
            "daily", "1-3м",
            mk_state(h_state, h_asof, "daily"),
            None, "narrative", h_asof,
            "ai-hype-monitor/hype_index.json"))
    else:
        cards.append(_unavail(
            "ai-hype", "indicator", "conditional",
            "AI Hype Monitor -- индекс 0-100 (в разработка).",
            "daily", "1-3м", "narrative",
            "hype_index.json недостъпен"))

    # 7-8) Momentum twins (SP500 + STOXX600) -- MEDIUM ---------------------------#
    for organ_id, key, label_geo in (
            ("momentum-sp500", "momentum_us", "SP500"),
            ("momentum-stoxx", "momentum_eu", "STOXX600")):
        t = sources.get(key)
        if t:
            cards.append(_card(
                organ_id, "stocks", "belt",
                "Моментум ранг ({}) -- per-акция momentum_score; {} имена в последната "
                "снимка.".format(label_geo, t.get("n_names_latest")),
                "daily", "1-3м",
                mk_state(OrderedDict([
                    ("n_names_latest", t.get("n_names_latest")),
                    ("n_snapshots", t.get("n_snapshots")),
                    ("score_field", t.get("score_field")),
                ]), t.get("as_of"), "daily"),
                None, "context", t.get("as_of"),
                "satellite DuckDB {}".format(
                    "sp500_momentum" if key == "momentum_us" else "stoxx600_momentum")))
        else:
            cards.append(_unavail(
                organ_id, "stocks", "belt",
                f"Моментум ранг ({label_geo}) -- per-акция momentum_score.",
                "daily", "1-3м", "context", "momentum таблица празна"))

    # 9-10) Rotation twins (SP500 + STOXX600) -- MEDIUM --------------------------#
    for organ_id, key, label_geo in (
            ("rotation-sp500", "rotation_us", "SP500"),
            ("rotation-stoxx", "rotation_eu", "STOXX600")):
        t = sources.get(key)
        if t:
            cards.append(_card(
                organ_id, "sectors", "belt",
                "Ротационен радар ({}) -- per-акция квадрант/ранг; {} имена в последната "
                "снимка.".format(label_geo, t.get("n_names_latest")),
                "daily", "1-3м",
                mk_state(OrderedDict([
                    ("n_names_latest", t.get("n_names_latest")),
                    ("n_snapshots", t.get("n_snapshots")),
                    ("score_field", t.get("score_field")),
                ]), t.get("as_of"), "daily"),
                None, "context", t.get("as_of"),
                "satellite DuckDB {}".format(
                    "rotation_us" if key == "rotation_us" else "rotation_eu")))
        else:
            cards.append(_unavail(
                organ_id, "sectors", "belt",
                f"Ротационен радар ({label_geo}) -- per-акция квадрант/ранг.",
                "daily", "1-3м", "context", "rotation таблица празна"))

    # 11) Stock-selection -- MEDIUM ----------------------------------------------#
    ss = sources.get("stock_selection")
    if ss:
        cards.append(_card(
            "stock-selection", "stocks", "belt",
            "Селекция на акции -- per-акция composite_score (trend/quality/value/risk); "
            "{} имена в последната снимка.".format(ss.get("n_names_latest")),
            "daily", "1-3м",
            mk_state(OrderedDict([
                ("n_names_latest", ss.get("n_names_latest")),
                ("n_snapshots", ss.get("n_snapshots")),
                ("score_field", ss.get("score_field")),
            ]), ss.get("as_of"), "daily"),
            None, "context", ss.get("as_of"),
            "satellite DuckDB stock_selection"))
    else:
        cards.append(_unavail(
            "stock-selection", "stocks", "belt",
            "Селекция на акции -- per-акция composite_score.",
            "daily", "1-3м", "context", "stock_selection таблица празна"))

    # 12) Satellite synthesis (self-reflective) -- MEDIUM ------------------------#
    st = sources.get("satellite_state")
    if st:
        # as_of is a data VINTAGE, not a calendar boundary: state.json labels its week
        # by the ISO window (Mon..Sun), so mid-week week.end lies in the future and a
        # Saturday snapshot downstream (data-core make_snapshot, №41 gate) rightly
        # refuses future-dated content. Clamp to generated_at — the day the state was
        # actually produced — so the card never claims data from tomorrow.
        s_asof = _iso_date((st.get("week") or {}).get("end"))
        s_gen = _iso_date(st.get("generated_at"))
        if s_asof and s_gen and s_asof > s_gen:
            s_asof = s_gen
        z = st.get("z_heatmap") or {}
        pa = st.get("persistent_anomalies") or {}
        s_state = OrderedDict([
            ("week", (st.get("week") or {}).get("label")),
            ("n_triggered_patterns", len(st.get("triggered_patterns") or [])),
            ("n_z_symbols", len(z.get("symbols") or [])),
            ("n_parallels", len(st.get("parallels_top3") or [])),
            ("persistent_anomalies", OrderedDict([
                ("us", len(pa.get("us") or [])),
                ("eu", len(pa.get("eu") or [])),
                ("cn", len(pa.get("cn") or [])),
            ])),
        ])
        cards.append(_card(
            "satellite-synth", "bridge", "blackbox",
            "Сателитен синтез -- z-heatmap, триггернати pattern-и, исторически "
            "паралели, устойчиви аномалии US/EU/CN (саморефлексивна карта).",
            "weekly", "седмица",
            mk_state(s_state, s_asof, "weekly"),
            None, "context", s_asof,
            "macro-satellite docs/state.json (self)"))
    else:
        cards.append(_unavail(
            "satellite-synth", "bridge", "blackbox",
            "Сателитен синтез -- z-heatmap, pattern-и, паралели, аномалии.",
            "weekly", "седмица", "context", "state.json липсва"))

    # ---- file wrapper (metadata + audit frontier; cards are the payload) ------ #
    dead = [c["organ_id"] for c in cards
            if isinstance(c["state"], dict) and c["state"].get("available") is False]
    stale_ids = [c["organ_id"] for c in cards
                 if isinstance(c["state"], dict) and c["state"].get("stale") is True]
    return OrderedDict([
        ("generator", "external_organism_cards.py v" + GENERATOR_VERSION),
        ("schema", "organism_cards " + CARD_SCHEMA),
        ("mandate", "INIT-22 E1b external citizens (organism/MANDATE-E1B-external-citizens.md)"),
        ("scope", "12 external-citizen organs carded into E1 schema v1. INTERNAL "
                  "satellite file; the public organism.json is NOT touched."),
        ("reading_convention",
         "reading=null on EVERY external card (E1 s3): none carries a pre-existing "
         "confirm/diverge logic, so a reading would be a new classification. The "
         "macro-regime card exposes the VRM<->macro-table values side by side but "
         "computes NO verdict -- that divergence is E4 territory (mandate item 2)."),
        ("reference_date", ref.isoformat()),
        ("n_cards", len(cards)),
        ("n_unavailable", len(dead)),
        ("unavailable", dead),
        ("n_stale", len(stale_ids)),
        ("stale", stale_ids),
        ("cards", cards),
    ])


# ── Orchestration (I/O) ──────────────────────────────────────────────────────

def write_external_cards(output_dir: Path | None = None,
                         fetch: bool = True) -> Path:
    """Load sources once, build, write docs/organism_cards_external.json. Returns path."""
    docs = output_dir or (REPO_ROOT / "docs")
    sources = load_sources(docs=docs, fetch=fetch)
    reg = build(sources)
    docs.mkdir(parents=True, exist_ok=True)
    out = docs / OUT_NAME
    out.write_text(json.dumps(reg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    log.info("organism_cards_external.json written",
             extra={"path": str(out), "n_cards": reg["n_cards"],
                    "n_unavailable": reg["n_unavailable"], "n_stale": reg["n_stale"]})
    return out


def main(argv: list[str] | None = None) -> int:
    import sys
    argv = argv if argv is not None else sys.argv[1:]
    docs = REPO_ROOT / "docs"

    if "--check" in argv:
        # Verify determinism WITHOUT network: replay over a single in-memory snapshot
        # must be byte-identical. (The full verify gate lives in verify_external_cards;
        # this is the standalone quick check.)
        sources = load_sources(docs=docs, fetch=False)
        a = json.dumps(build(sources), ensure_ascii=False, indent=2) + "\n"
        b = json.dumps(build(sources), ensure_ascii=False, indent=2) + "\n"
        if a != b:
            _p("FAIL: build is non-deterministic over identical sources")
            return 1
        _p("OK (deterministic replay): {} cards".format(build(sources)["n_cards"]))
        return 0

    path = write_external_cards()
    reg = json.loads(path.read_text(encoding="utf-8"))
    _p("wrote {} ({} cards, {} unavailable, {} stale)".format(
        path, reg["n_cards"], reg["n_unavailable"], reg["n_stale"]))
    for c in reg["cards"]:
        st = c["state"]
        flag = "UNAVAIL" if (isinstance(st, dict) and st.get("available") is False) else \
               ("STALE" if (isinstance(st, dict) and st.get("stale")) else "ok")
        _p("  {:<16} {:<10} {:<11} as_of={} [{}]".format(
            c["organ_id"], c["floor"], c["taxonomy_layer"], c["as_of"], flag))
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
