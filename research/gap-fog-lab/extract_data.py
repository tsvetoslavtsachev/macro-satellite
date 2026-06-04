# -*- coding: utf-8 -*-
"""
Извлича gap-журнала (US) в чист JSON за визуализационна лаборатория.
READ-ONLY спрямо journal/ — не пипа нищо в проекта.
Изход: research/gap-fog-lab/data.json
"""
import json
import math
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]  # macro-satellite/
JRN = ROOT / "journal"
OUT = Path(__file__).resolve().parent / "data.json"


def jsonable(v):
    if v is None:
        return None
    if isinstance(v, float) and math.isnan(v):
        return None
    if hasattr(v, "isoformat"):
        return v.isoformat()
    if isinstance(v, (pd.Timestamp,)):
        return v.isoformat()
    return v


# --- 1. gap серия ---
gs = pd.read_csv(JRN.parent / "briefings" / "journal" / "gap_series.csv")
gap_series = [
    {
        "week": r["week"],
        "week_end": r["week_end"],
        "economy": round(float(r["economy_axis"]), 4),
        "markets": round(float(r["markets_axis"]), 4),
        "gap": round(float(r["gap"]), 4),
    }
    for _, r in gs.iterrows()
]

# --- 1b. под-скорове на икон-оста (за качествен панел „под капака") ---
# orientation НЕ се интерпретира (good/bad) — показват се неутрално като компоненти.
econ = pd.read_parquet(JRN / "economy_reconstructed.parquet")
SUBCOLS = ["labor_score", "growth_score", "inflation_score", "liquidity_score", "credit_score"]
subscores = {}
for _, r in econ.iterrows():
    subscores[r["week"]] = {c.replace("_score", ""): (None if pd.isna(r[c]) else round(float(r[c]), 3)) for c in SUBCOLS if c in econ.columns}

# серийни средни/σ за качествено четене „над/под дългосрочната средна" (изчислено, не догадка)
import statistics as _st
_eco = [d["economy"] for d in gap_series]
_mkt = [d["markets"] for d in gap_series]
series_stats = {
    "economy_mean": round(_st.mean(_eco), 4),
    "economy_std": round(_st.pstdev(_eco), 4),
    "markets_mean": round(_st.mean(_mkt), 4),
    "markets_std": round(_st.pstdev(_mkt), 4),
}

# --- 2. епизоди (90 реда = 30 еп × 3 хоризонта) ---
ep = pd.read_parquet(JRN / "machine_episodes.parquet")
episodes = {}
for _, r in ep.iterrows():
    eid = r["gap_episode_id"]
    if eid not in episodes:
        episodes[eid] = {
            "id": eid,
            "config_key": r["config_key"],
            "open_week": r["open_week"],
            "open_date": jsonable(r["open_date"]),
            "close_date": jsonable(r["close_date"]),
            "n_weeks": int(r["n_weeks"]),
            "censored": bool(r["censored"]),
            "open_economy": round(float(r["open_economy_axis"]), 4),
            "open_markets": round(float(r["open_markets_axis"]), 4),
            "open_gap": round(float(r["open_gap"]), 4),
            "peak_gap": round(float(r["peak_gap"]), 4),
            "horizons": [],
        }
    episodes[eid]["horizons"].append(
        {
            "y": int(r["horizon_y"]),
            "y_date": jsonable(r["y_date"]),
            "y_economy": round(float(r["y_economy_axis"]), 4),
            "y_markets": round(float(r["y_markets_axis"]), 4),
            "y_gap": round(float(r["y_gap"]), 4),
            "outcome": r["outcome"],
            "censored_at_y": bool(r["censored_at_y"]),
            "d_economy": None if pd.isna(r["d_economy"]) else round(float(r["d_economy"]), 4),
            "d_markets": None if pd.isna(r["d_markets"]) else round(float(r["d_markets"]), 4),
            "attr_economy": None if pd.isna(r["attribution_economy_share"]) else round(float(r["attribution_economy_share"]), 4),
            "attr_markets": None if pd.isna(r["attribution_markets_share"]) else round(float(r["attribution_markets_share"]), 4),
        }
    )
for e in episodes.values():
    e["horizons"].sort(key=lambda h: h["y"])
episodes = sorted(episodes.values(), key=lambda e: e["open_date"])

# --- 2b. РЕАЛНИ ДВИЖЕНИЯ НА ИНСТРУМЕНТИ през всеки епизод (динамиката, не скорове) ---
# Цените идват от storage/parquet/etf_prices (същите ETF-и, от които се строи markets_axis).
import glob
INSTR = ["SPY", "QQQ", "TLT", "IEF", "HYG", "LQD", "IWM", "XLE", "XLP", "XLY", "GLD"]
_pxfiles = sorted(glob.glob(str(ROOT / "storage" / "parquet" / "etf_prices" / "**" / "data.parquet"), recursive=True))
_px = pd.concat([pd.read_parquet(f, columns=["date", "symbol", "price", "close_yf"]) for f in _pxfiles], ignore_index=True)
_px["px"] = _px["price"].fillna(_px["close_yf"])
_px = _px.dropna(subset=["px"])
_px["date"] = pd.to_datetime(_px["date"]).dt.strftime("%Y-%m-%d")
_px = _px[_px["symbol"].isin(INSTR)].drop_duplicates(subset=["symbol", "date"], keep="last")
# series по символ: списък от (date, px) сортиран
_series = {s: sub.sort_values("date")[["date", "px"]].values.tolist() for s, sub in _px.groupby("symbol")}


def _px_on(sym, target):
    """Последна цена на/преди target (ISO стринг)."""
    ser = _series.get(sym)
    if not ser:
        return None
    last = None
    for d, p in ser:
        if d <= target:
            last = p
        else:
            break
    return last


def _window(sym, d0, d1):
    """min/max/last px в [d0,d1]."""
    ser = _series.get(sym)
    if not ser:
        return None
    vals = [p for d, p in ser if d0 <= d <= d1]
    return vals or None


for e in episodes:
    d0 = e["open_date"]
    d1 = e["close_date"] or _series["SPY"][-1][0]  # отворен епизод → до последна дата
    moves = {}
    for s in INSTR:
        p0 = _px_on(s, d0)
        p1 = _px_on(s, d1)
        if p0 and p1 and p0 > 0:
            moves[s] = round(100 * (p1 - p0) / p0, 1)
    # дъно на SPY вътре в прозореца (drawdown) → за „падна до −X% преди да се върне"
    spw = _window("SPY", d0, d1)
    p0 = _px_on("SPY", d0)
    if spw and p0 and p0 > 0:
        moves["SPY_trough"] = round(100 * (min(spw) - p0) / p0, 1)
        moves["SPY_peak"] = round(100 * (max(spw) - p0) / p0, 1)
    e["market_moves"] = moves

# --- 3. base rate, преизчислен директно от епизодите (verified от source) ---
# по config_key × horizon: брой изходи. Два прозореца: full (2021→) и post-2022.
OUTCOMES = ["market_leads", "economy_leads", "meet", "widen"]


def base_rate(min_open_year=None):
    dist = {}
    for e in episodes:
        if min_open_year and int(e["open_date"][:4]) < min_open_year:
            continue
        ck = e["config_key"]
        for h in e["horizons"]:
            key = (ck, h["y"])
            d = dist.setdefault(key, {o: 0 for o in OUTCOMES})
            d["_n"] = d.get("_n", 0) + 1
            if h["censored_at_y"]:
                d["_unresolved"] = d.get("_unresolved", 0) + 1
            else:
                d[h["outcome"]] = d.get(h["outcome"], 0) + 1
    out = []
    for (ck, y), d in sorted(dist.items()):
        n = d.pop("_n", 0)
        unresolved = d.pop("_unresolved", 0)
        resolved = n - unresolved
        out.append(
            {
                "config_key": ck,
                "horizon": y,
                "n": n,
                "resolved": resolved,
                "unresolved": unresolved,
                "counts": {o: d.get(o, 0) for o in OUTCOMES},
            }
        )
    return out


base_full = base_rate()
base_post2022 = base_rate(min_open_year=2022)

# --- 4. човешки присъди ---
hj_path = JRN / "human_judgments.jsonl"
human = []
if hj_path.exists():
    for line in hj_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            human.append(json.loads(line))

# --- 5. резолюции (ако има) ---
hr_path = JRN / "human_resolutions.jsonl"
resolutions = []
if hr_path.exists():
    for line in hr_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            resolutions.append(json.loads(line))

data = {
    "meta": {
        "region": "US",
        "window": [gap_series[0]["week"], gap_series[-1]["week"]],
        "n_weeks": len(gap_series),
        "n_episodes": len(episodes),
        # σ/τ/velocity от последния journal-backfill (2026-06-04, нова health методология)
        "tau_open": 0.6328,
        "tau_close": 0.3164,
        "sigma_gap": 0.6328,
        "sigma_economy": 0.0205,
        "sigma_markets": 0.3738,
        "velocity_asymmetry": {
            "4": {"dE": 0.031, "dM": 0.431, "ratio": 13.9},
            "8": {"dE": 0.065, "dM": 0.577, "ratio": 8.9},
            "13": {"dE": 0.070, "dM": 0.862, "ratio": 12.3},
        },
        "note": "machine base rate = perfect-hindsight (revision-biased backfill), НЕ real-time edge. Методология: робастен z + полярност + U-инфлация (виж LENS_SCORING_METHODOLOGY.md)",
        "data_start_note": "И двете оси реконструирани само от 2021-W24 (пазар-ос от ETF цени, които започват 2021-05). 'Десетилетия назад' изисква отделна реконструкция.",
        "series_stats": series_stats,
    },
    "gap_series": gap_series,
    "subscores": subscores,
    "episodes": episodes,
    "base_rate_full": base_full,
    "base_rate_post2022": base_post2022,
    "human_judgments": human,
    "human_resolutions": resolutions,
}

def sanitize(v):
    """Рекурсивно: NaN/Inf float → None (валиден JSON за браузър)."""
    if isinstance(v, float):
        return None if (math.isnan(v) or math.isinf(v)) else v
    if isinstance(v, dict):
        return {k: sanitize(x) for k, x in v.items()}
    if isinstance(v, list):
        return [sanitize(x) for x in v]
    return v


data = sanitize(data)
_blob = json.dumps(data, ensure_ascii=False, indent=None, allow_nan=False)
OUT.write_text(_blob, encoding="utf-8")
print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")

# Инжектирай в self-contained data-blob на index.html (визуализацията чете ВГРАДЕНИЯ
# blob, не fetch-ва data.json — за да работи от file:// и при upload). Без тази стъпка
# index.html остава на старите числа.
import re as _re
_idx = Path(__file__).resolve().parent / "index.html"
if _idx.exists():
    _html = _idx.read_text(encoding="utf-8")
    _new, _n = _re.subn(
        r'(<script id="data-blob" type="application/json">).*?(</script>)',
        lambda m: m.group(1) + _blob + m.group(2),
        _html, count=1, flags=_re.DOTALL,
    )
    if _n:
        _idx.write_text(_new, encoding="utf-8")
        print(f"injected data-blob into {_idx.name}")
    else:
        print("WARN: data-blob marker not found in index.html")
print(f"  gap_series: {len(gap_series)} weeks")
print(f"  episodes: {len(episodes)}")
print(f"  base_rate_full keys: {len(base_full)}  post2022: {len(base_post2022)}")
print(f"  human_judgments: {len(human)}  resolutions: {len(resolutions)}")
# Sanity: разпечатай gap_pos разпределение за сверка с machine_base_rate.md
for row in base_full:
    if row["config_key"] == "gap_pos":
        c = row["counts"]
        tot = row["resolved"]
        pct = {k: (round(100 * v / tot) if tot else 0) for k, v in c.items()}
        print(f"  CHECK gap_pos Y={row['horizon']:>2}w n={row['n']} resolved={tot} {pct}")
