"""Машинен backfill на gap-журнала → machine base rate (Тухла 2a, стъпка 4).

Пайплайн:
  1. Подравнена седмична gap-серия: markets_axis (gap_engine, etf_prices) +
     reconstruct_economy_axis (build_macro_state над trimmed fred_cache).
  2. detect_episodes (vol-based глобален праг; броим ЕПИЗОДИ, не записи).
  3. Глобална σ на двете оси → attribute_episode на всеки хоризонт Y ∈ {4,8,13}.
  4. Persist (economy_reconstructed + machine_episodes) + base rate per (config_key, Y).

ДВОЕН ДОКЛАД (решение Q3): base rate се смята за ПЪЛНИЯ прозорец (2021→) И за
post-reflation подмножеството (open_date ≥ 2022-01-01). 2021 reflation носи семантично
обърнат inflation orient (gap_weights inflation=-1 е stagflation-scoped) → двойният
доклад показва чувствителността директно.

⚠ Двата caveat-а (в данните И в доклада): revision bias (best-case, не real-time) +
методологична консистентност (днешна методология назад). Виж CAVEATS.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta

import pandas as pd

from ...storage.duckdb_conn import get_duck
from ..gap_engine import GapWeights, economy_axis, load_gap_weights, markets_axis
from ..weekly_window import WeekWindow, current_week, iso_week_for
from . import store
from .attribution import HORIZONS, attribute_episode, axis_sigma
from .economy_reconstruct import _load_bridge, reconstruct_economy_axis
from .episodes import detect_episodes

# Пазари-кракът е binding constraint: etf_prices от 2021-05-17 + 13w trailing baseline.
DEFAULT_START = date(2021, 5, 17)
# Post-reflation отрязък за двойния доклад (inflation orient -1 семантично валиден).
POST_REFLATION_CUTOFF = date(2022, 1, 1)

CAVEATS = (
    "⚠ REVISION/VINTAGE BIAS: backfill чете РЕВИЗИРАН fred_cache + trim по дата-на-"
    "наблюдение (вкл. непубликувани-към-X данни) → machine base rate е BEST-CASE "
    "(perfect-hindsight), НЕ real-time постижим. Human forward track record (2b) ще е "
    "по-реалистичен. Никога не го представяй като real-time edge.",
    "⚠ МЕТОДОЛОГИЧНА КОНСИСТЕНТНОСТ: днешната методология (робастен z спрямо 10-г. "
    "прозорец + полярност на ниво серия + U-форма за инфлация; orient +1 навсякъде) "
    "приложена назад. U-формата прави inflation orient режим-инвариантен (близост до "
    "целта = здраве), затова двойният доклад (full vs post-2022) е по-малко чувствителен "
    "към 2021 reflation, отколкото при стария stagflation-scoped orient. Виж "
    "LENS_SCORING_METHODOLOGY.md.",
    "⚠ VELOCITY ASYMMETRY (за честно четене): икономика-оста е структурно БАВНА (месечни "
    "макро данни) → движи се много по-малко от пазари-оста за същия хоризонт (виж "
    "диагностиката долу). Затова market_leads е ДО ГОЛЯМА СТЕПЕН МЕХАНИЧЕН — бавният "
    "икон-крак физически не може да затвори голям gap за седмици. Vol-нормализацията "
    "изравнява amplitude-per-σ, НЕ structural velocity. → НЕ чети 'market_leads %' като "
    "tradeable edge; информативни са widen-ставките + pos/neg асиметрията. economy_leads "
    "(по-рядко) е по-значимо когато се случи.",
)


@dataclass
class BackfillResult:
    week_start: date
    week_end: date
    n_weeks_computed: int
    n_weeks_total_generated: int
    sigma_gap: float
    tau_open: float
    tau_close: float
    sigma_economy: float
    sigma_markets: float
    episodes: list = field(default_factory=list)         # GapEpisode
    episode_rows: list = field(default_factory=list)      # dict per (episode × horizon)
    base_rates: dict = field(default_factory=dict)        # {window: {config_key: {Y: {...}}}}
    reconciliation: list = field(default_factory=list)    # caveat #1 quantified
    velocity: dict = field(default_factory=dict)          # caveat #3: {Y: (|ΔE|, |ΔM|, ratio)}
    economy_path: str = ""
    episodes_path: str = ""
    gap_series_path: str = ""
    gap_rows: list = field(default_factory=list)   # per-week {week,week_end,econ,mkt,gap}
    region: str = "US"


def _materialize_etf(duck) -> None:
    """etf_prices view (parquet glob) → in-memory TABLE + index.

    markets_axis прави ~112 as-of queries на седмица; над view-а върху 62 parquet
    файла това е ~16 мин за пълния backfill. Материализирано в паметта → ~1 мин (14×).
    Чете СЪЩИТЕ данни — нула промяна в логиката/числата.
    """
    df = duck.execute("SELECT * FROM etf_prices").df()
    duck.execute("DROP VIEW IF EXISTS etf_prices")
    duck.register("_etf_df", df)
    duck.execute("CREATE TABLE etf_prices AS SELECT * FROM _etf_df")
    duck.unregister("_etf_df")
    duck.execute("CREATE INDEX idx_etf_prices ON etf_prices(symbol, date)")


def _enumerate_weeks(start: date, end_week: WeekWindow) -> list[WeekWindow]:
    """Седмици от седмицата на `start` до `end_week` включително (forward)."""
    weeks: list[WeekWindow] = []
    cur = iso_week_for(start)
    while cur.week_start <= end_week.week_start:
        weeks.append(cur)
        cur = iso_week_for(cur.week_start + timedelta(days=7))
    return weeks


def _build_gap_series(duck, weeks: list[WeekWindow], weights: GapWeights, bridge):
    """За всяка седмица: (economy_axis, markets_axis, gap, econ_leg, mkt_leg).

    Икономика-кракът е РЕКОНСТРУИРАН (не от таблицата). Връща подравнени списъци +
    списък само на седмиците с двата крака изчислими (за епизоди/attribution).
    """
    econ_axis: list = []
    mkt_axis: list = []
    gaps: list = []
    econ_legs: list = []
    for wk in weeks:
        e_leg = reconstruct_economy_axis(wk, weights, bridge)
        m_leg = markets_axis(duck, wk, weights)
        e = e_leg.axis if e_leg is not None else None
        m = m_leg.axis if m_leg is not None else None
        econ_axis.append(e)
        mkt_axis.append(m)
        gaps.append((m - e) if (e is not None and m is not None) else None)
        econ_legs.append(e_leg)
    return econ_axis, mkt_axis, gaps, econ_legs


def _compact(weeks, econ_axis, mkt_axis, gaps, econ_legs):
    """Запазва само седмиците с изчислим gap (двата крака) — подравнена серия за епизоди."""
    cw, ce, cm, cg, cl = [], [], [], [], []
    for i, g in enumerate(gaps):
        if g is None:
            continue
        cw.append(weeks[i]); ce.append(econ_axis[i]); cm.append(mkt_axis[i])
        cg.append(g); cl.append(econ_legs[i])
    return cw, ce, cm, cg, cl


def run_backfill(start: date = DEFAULT_START,
                 region: str = "US",
                 weights: GapWeights | None = None,
                 horizons: tuple[int, ...] = HORIZONS) -> BackfillResult:
    w = weights or load_gap_weights(region)
    duck = get_duck()
    _materialize_etf(duck)          # 14× speedup за повтарящите се as-of queries
    bridge = _load_bridge(w.region)
    end_week = current_week()
    weeks_all = _enumerate_weeks(start, end_week)

    econ_axis, mkt_axis, gaps, econ_legs = _build_gap_series(duck, weeks_all, w, bridge)
    weeks, ce, cm, cg, cl = _compact(weeks_all, econ_axis, mkt_axis, gaps, econ_legs)

    episodes, meta = detect_episodes(weeks, cg)
    sigma_e = axis_sigma(ce)
    sigma_m = axis_sigma(cm)

    # ── Attribution per епизод × хоризонт → редове за store ──────────────────
    rows: list[dict] = []
    for ep in episodes:
        outs = attribute_episode(ep, ce, cm, weeks, sigma_e, sigma_m, horizons)
        for ho in outs:
            rows.append({
                "gap_episode_id": ep.episode_id,
                "config_key": ep.config_key,
                "open_week": ep.open_week,
                "open_date": ep.open_date,
                "close_date": ep.close_date,
                "n_weeks": ep.n_weeks,
                "censored": ep.censored,
                "open_economy_axis": ce[ep.open_index],
                "open_markets_axis": cm[ep.open_index],
                "open_gap": ep.open_gap,
                "peak_gap": ep.peak_gap,
                "horizon_y": ho.horizon_y,
                "y_date": ho.y_date,
                "y_economy_axis": ho.y_economy_axis,
                "y_markets_axis": ho.y_markets_axis,
                "y_gap": ho.y_gap,
                "sigma_economy": sigma_e,
                "sigma_markets": sigma_m,
                "d_economy": ho.d_economy,
                "d_markets": ho.d_markets,
                "attribution_economy_share": ho.economy_share,
                "attribution_markets_share": ho.markets_share,
                "outcome": ho.outcome,
                "censored_at_y": ho.censored_at_y,
            })

    # ── Persist ──────────────────────────────────────────────────────────────
    econ_df = pd.DataFrame([{
        "week": weeks[i].label,
        "week_end": weeks[i].week_end,
        "economy_axis": ce[i],
        "labor_score": (cl[i].components.get("labor") or {}).get("score"),
        "growth_score": (cl[i].components.get("growth") or {}).get("score"),
        "inflation_score": (cl[i].components.get("inflation") or {}).get("score"),
        "liquidity_score": (cl[i].components.get("liquidity") or {}).get("score"),
        "credit_score": (cl[i].components.get("credit") or {}).get("score"),
        "as_of_date": cl[i].as_of_date,
        "age_days": cl[i].age_days,
    } for i in range(len(weeks))])
    economy_path = store.write_economy_reconstructed(econ_df, w.region)
    episodes_df = pd.DataFrame(rows)
    episodes_path = store.write_machine_episodes(episodes_df, w.region)

    # ── Per-week gap серия ("gap в историята", Тухла 3(б)) ────────────────────
    gap_rows = [{
        "week": weeks[i].label,
        "week_end": weeks[i].week_end,
        "economy_axis": ce[i],
        "markets_axis": cm[i],
        "gap": cg[i],
    } for i in range(len(weeks))]
    gap_series_path = store.write_gap_series(pd.DataFrame(gap_rows), w.region)

    # ── Base rates (двоен доклад) ─────────────────────────────────────────────
    base_rates = {
        "full": _base_rates(rows, min_open_date=None),
        "post_2022": _base_rates(rows, min_open_date=POST_REFLATION_CUTOFF),
    }

    # ── Reconciliation (caveat #1 quantified): recon vs табличния икон-axis ───
    reconciliation = _reconcile(duck, w, bridge)

    # ── Velocity asymmetry (caveat #3): средно |ΔE| vs |ΔM| per хоризонт ─────
    velocity = _velocity_asymmetry(rows, horizons)

    return BackfillResult(
        week_start=weeks[0].week_end if weeks else start,
        week_end=weeks[-1].week_end if weeks else end_week.week_end,
        n_weeks_computed=len(weeks),
        n_weeks_total_generated=len(weeks_all),
        sigma_gap=meta["sigma_gap"], tau_open=meta["tau_open"], tau_close=meta["tau_close"],
        sigma_economy=sigma_e, sigma_markets=sigma_m,
        episodes=episodes, episode_rows=rows, base_rates=base_rates,
        reconciliation=reconciliation, velocity=velocity,
        economy_path=str(economy_path), episodes_path=str(episodes_path),
        gap_series_path=str(gap_series_path), gap_rows=gap_rows,
        region=w.region,
    )


def _velocity_asymmetry(rows: list[dict], horizons: tuple[int, ...]) -> dict:
    """Средно |ΔE| vs |ΔM| per хоризонт (само resolved редове) + съотношение.

    Документира caveat #3: бавната икон-ос → market_leads е ларгели механичен.
    """
    out: dict = {}
    for y in horizons:
        de = [abs(r["d_economy"]) for r in rows
              if r["horizon_y"] == y and r["d_economy"] is not None]
        dm = [abs(r["d_markets"]) for r in rows
              if r["horizon_y"] == y and r["d_markets"] is not None]
        if not de or not dm:
            continue
        mean_e = sum(de) / len(de)
        mean_m = sum(dm) / len(dm)
        ratio = mean_m / mean_e if mean_e > 0 else float("inf")
        out[y] = (mean_e, mean_m, ratio)
    return out


def _base_rates(rows: list[dict], min_open_date: date | None) -> dict:
    """Base rate per (config_key, horizon): разпределение на изходите по ЕПИЗОДИ.

    Брои ЕПИЗОДИ, не записи — всеки (episode_id × horizon) е един изход. unresolved
    се отчита отделно и НЕ влиза в дяловете (честен n).
    """
    out: dict = {}
    for r in rows:
        if min_open_date is not None and r["open_date"] < min_open_date:
            continue
        ck = r["config_key"]; y = r["horizon_y"]; oc = r["outcome"]
        bucket = out.setdefault(ck, {}).setdefault(y, {
            "counts": {}, "n_resolved": 0, "n_unresolved": 0, "episode_ids": set(),
        })
        bucket["episode_ids"].add(r["gap_episode_id"])
        if oc == "unresolved":
            bucket["n_unresolved"] += 1
        else:
            bucket["counts"][oc] = bucket["counts"].get(oc, 0) + 1
            bucket["n_resolved"] += 1
    # set → count
    for ck in out:
        for y in out[ck]:
            out[ck][y]["n_episodes"] = len(out[ck][y].pop("episode_ids"))
    return out


def _reconcile(duck, weights: GapWeights, bridge) -> list[dict]:
    """Quantify caveat #1: реконструиран икон-axis vs колекторския (табличния) на overlap-а.

    Разминаването = емпиричната величина на revision/vintage bias-а. Точно съвпадение
    на най-скорошните дати доказва, че bridge-ът е коректен (разминаването е bias, не бъг).
    """
    table = f"{weights.region.lower()}_macro_state"
    df = duck.execute(
        f"SELECT date FROM {table} ORDER BY date"
    ).df()
    out: list[dict] = []
    for d in df["date"].tolist():
        dd = d.date() if hasattr(d, "date") else d
        wk = iso_week_for(dd)
        tbl = economy_axis(duck, wk, weights)
        rec = reconstruct_economy_axis(wk, weights, bridge)
        if tbl is None or rec is None:
            continue
        out.append({
            "date": dd, "week": wk.label,
            "table_axis": round(tbl.axis, 4),
            "recon_axis": round(rec.axis, 4),
            "delta": round(rec.axis - tbl.axis, 4),
        })
    return out


# ── Доклад ──────────────────────────────────────────────────────────────────

_OUTCOME_ORDER = ("market_leads", "economy_leads", "meet", "widen")


def format_report(res: BackfillResult) -> str:
    L: list[str] = []
    L.append("═" * 72)
    L.append(f"  MACHINE BASE RATE [{res.region}] — gap-журнал (Тухла 2a/3б)")
    L.append("═" * 72)
    L.append(f"  Прозорец: {res.week_start} → {res.week_end} "
             f"({res.n_weeks_computed} седмици с изчислим gap "
             f"от {res.n_weeks_total_generated} генерирани)")
    L.append(f"  σ_gap={res.sigma_gap:.4f}  τ_open={res.tau_open:.4f}  τ_close={res.tau_close:.4f}")
    L.append(f"  σ_economy={res.sigma_economy:.4f}  σ_markets={res.sigma_markets:.4f}")
    n_cens = sum(1 for e in res.episodes if e.censored)
    L.append(f"  ЕПИЗОДИ: {len(res.episodes)} (censored: {n_cens}) — броим епизоди, не записи")
    L.append("")
    # Епизоди списък
    L.append("  Епизоди (open → close, config, peak gap):")
    for e in res.episodes:
        close = e.close_date.isoformat() if e.close_date else "ОТВОРЕН"
        L.append(f"    {e.episode_id:<22} {e.open_date} → {close:<10} "
                 f"{e.config_key:<8} peak={e.peak_gap:+.3f} ({e.n_weeks}w)")
    L.append("")
    # Base rates — двоен доклад
    for window_name, label in (("full", "ПЪЛЕН 2021→"),
                               ("post_2022", "POST-REFLATION 2022→")):
        L.append("─" * 72)
        L.append(f"  BASE RATE — {label}")
        L.append("─" * 72)
        br = res.base_rates.get(window_name, {})
        if not br:
            L.append("    (няма епизоди в прозореца)")
            continue
        for ck in sorted(br):
            L.append(f"  config_key = {ck}")
            for y in sorted(br[ck]):
                b = br[ck][y]
                n = b["n_episodes"]; nr = b["n_resolved"]; nu = b["n_unresolved"]
                parts = []
                for oc in _OUTCOME_ORDER:
                    c = b["counts"].get(oc, 0)
                    if c:
                        pct = (100.0 * c / nr) if nr else 0.0
                        parts.append(f"{oc}={c} ({pct:.0f}%)")
                dist = " · ".join(parts) if parts else "—"
                L.append(f"    Y={y:>2}w: n_eps={n} resolved={nr} unresolved={nu}  {dist}")
        L.append("")
    # Reconciliation
    L.append("─" * 72)
    L.append("  RECONCILIATION (caveat #1 quantified): recon − table икон-axis на overlap")
    L.append("─" * 72)
    for r in res.reconciliation:
        L.append(f"    {r['date']} {r['week']}: table={r['table_axis']:+.4f} "
                 f"recon={r['recon_axis']:+.4f} Δ={r['delta']:+.4f}")
    L.append("")
    # Velocity asymmetry (caveat #3 quantified)
    L.append("─" * 72)
    L.append("  VELOCITY ASYMMETRY (caveat #3): средно |ΔE| vs |ΔM| per хоризонт")
    L.append("─" * 72)
    for y in sorted(res.velocity):
        me, mm, ratio = res.velocity[y]
        L.append(f"    Y={y:>2}w: mean|ΔE|={me:.3f}  mean|ΔM|={mm:.3f}  "
                 f"M/E={ratio:.1f}×  → market_leads ларгели механичен")
    L.append("")
    # Caveats
    L.append("─" * 72)
    for c in CAVEATS:
        L.append(f"  {c}")
        L.append("")
    L.append(f"  Записано: {res.economy_path}")
    L.append(f"            {res.episodes_path}")
    L.append(f"            {res.gap_series_path}")
    L.append("═" * 72)
    return "\n".join(L)
