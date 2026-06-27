"""Organism vitrine producer — docs/organism.json.

Консолидиран cross-env snapshot на ЦЕЛИЯ организъм в ЕДИН публичен JSON, четим с
обикновен web fetch от всяка среда (CC · Cowork · claude.ai web/mobile). Това е
производната „снимка"; data-core остава частен.

ADDITIVE — НЕ пипа state_export.py / state.json. Слой над вече-публични входове:
- собствения docs/state.json (data_health за 12 сензора + макро режими)  ← от диска
- treasury-funding-radar funding_state.json (5 лампи)                      ← fetch
- ETF-rotationradar barometer_feed.json (10 индикатора)                    ← fetch
- data-core weekly overlay (VRM детайл — жив мозък)                        ← диск (CI checkout)

Cardinal rule: моделът никога не фабрикува число — детерминистичният път (този
модул) парсва и пише. Падне ли източник → блокът свети `available:false`
(договорът от S14 — мъртъв канал свети честно, не нула).

VRM блокът се сорсва от живия data-core weekly overlay (`source:"data-core-live"`,
Gate 3 flip 24.06). Липсва ли overlay → блокът свети `available:false` (S14 — мъртъв
канал свети честно, не тих stale). Старата excel-frozen VRM_WEEK.md опашка-резерв е
премахната (A3, 27.06) след зелени data-core-live цикли.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ..logging_setup import get_logger
from ..paths import REPO_ROOT
from ..utils.http import fetch_json

log = get_logger(__name__)

ORGANISM_SCHEMA_VERSION = 1

# Външни публични източници (verified 200 · 2026-06-23). Python няма CORS —
# затова producer-ът прави multi-source merge тук; витрината фетчва само изхода.
FUNDING_URL = (
    "https://tsvetoslavtsachev.github.io/treasury-funding-radar/data/funding_state.json"
)
BAROMETER_URL = (
    "https://tsvetoslavtsachev.github.io/ETF-rotationradar/barometer_feed.json"
)
SATELLITE_STATE_URL = (
    "https://raw.githubusercontent.com/tsvetoslavtsachev/macro-satellite/main/docs/state.json"
)
SATELLITE_DASHBOARD_URL = "https://tsvetoslavtsachev.github.io/macro-satellite/"


# ── data-core LIVE state (VRM source-of-truth) ────────────────────────────────
# Gate 3 flip (24.06) направи мозъка жив; producer-ът чете живия weekly overlay.
# Мапингът е огледало на dashboards/vrm-compare read_datacore (доказан срещу Excel
# всяка събота). REGIME/alignment/GMS/KS идват от седмичния vrm_overlay.json[-1]
# (свеж W-FRI запис). Cardinal rule: само това, което мозъкът реално emit-ва —
# еднословният „сигнал" и прозаичните етикети остават None (не фабрикуваме;
# витрината degrade-ва на „—").

REGIME_BG = {
    "REFLATION": "РЕФЛАЦИЯ", "GROWTH": "РАСТЕЖ", "STAGNATION": "СТАГНАЦИЯ",
    "CRISIS": "КРИЗА", "DEFLATION": "ДЕФЛАЦИЯ",
}


def read_vrm_from_datacore(state_dir: Path) -> dict[str, Any] | None:
    """Жив VRM блок от data-core weekly overlay. Връща None ако state липсва или е
    нечетим (→ caller свети `available:false`, S14 честен мъртъв канал). Не
    интерпретира — извлича дословно."""
    ov_path = state_dir / "vrm_overlay.json"
    if not ov_path.exists():
        return None
    try:
        records = json.loads(ov_path.read_text(encoding="utf-8"))
        ov = records[-1]
    except (json.JSONDecodeError, IndexError, OSError, TypeError) as e:  # noqa: BLE001
        log.warning("vrm_overlay read failed",
                    extra={"path": str(ov_path), "error": str(e)})
        return None
    regime = ov.get("regime")
    if not regime:  # липсва ядро → не гадаем формат (cardinal rule)
        return None
    ks = ov.get("kill_switch") or {}
    gms = ov.get("gms") or {}
    align = ov.get("alignment_score")
    gms_score = gms.get("score")
    gms_max = gms.get("max") or 8
    gms_tier = gms.get("tier")
    gms_str = (f"{gms_score}/{gms_max} {gms_tier}".strip()
               if gms_score is not None else None)
    return {
        "available": True,
        "source": "data-core-live",
        "regime": regime,
        "regime_bg": REGIME_BG.get(regime),
        "signal": None,            # мозъкът не emit-ва еднословен сигнал — не фабрикуваме
        "alignment": f"{align}/8" if align is not None else None,
        "alignment_label": None,   # прозаичният етикет е Excel-only
        "gms": gms_str,
        "ks_active": bool(ks.get("active")),
        "ks_status": "неактивен" if ks.get("active") in (None, False) else "активен",
        "as_of": ov.get("as_of"),
    }


# ── Блок-екстрактори (чисти — без I/O) ────────────────────────────────────────

def _organism_health(state: dict[str, Any]) -> dict[str, Any]:
    """Lift на S14 data_health контракта от собствения state.json (тримнат)."""
    dh = state.get("data_health") or {}
    sources = {}
    for name, e in (dh.get("sources") or {}).items():
        sources[name] = {
            "status": e.get("status"),
            "as_of": e.get("as_of"),
            "days_stale": e.get("days_stale"),
        }
    return {
        "checked_at": dh.get("checked_at"),
        "n_live": dh.get("n_live"),
        "n_stale": dh.get("n_stale"),
        "n_missing": dh.get("n_missing"),
        "any_dead": dh.get("any_dead"),
        "sources": sources,
    }


def _macro_from_state(state: dict[str, Any]) -> dict[str, Any]:
    """US/EU/CN режими от собствения state.json (вече агрегирани — не дублираме)."""
    regimes = state.get("regimes") or {}
    out: dict[str, Any] = {}
    for geo, key in (("us", "us_macro"), ("eu", "eu_macro"), ("cn", "cn_macro")):
        r = regimes.get(key)
        if not r:
            out[geo] = None
            continue
        out[geo] = {
            "regime": r.get("regime_key"),
            "label": r.get("regime_label_bg"),
            "as_of": (r.get("as_of") or "")[:10] or None,
            "divergences": r.get("cross_lens_divergences_count"),
        }
    return out


def _funding_block(funding: dict[str, Any] | None) -> dict[str, Any]:
    if not funding:
        return {"available": False, "error": "funding_state.json недостъпен"}
    return {
        "available": True,
        "verdict": funding.get("verdict"),
        "composite": funding.get("composite_score"),
        "lamps": funding.get("lamp_status") or {},
        "any_dead": funding.get("any_dead_source"),
        "as_of": (funding.get("as_of") or "")[:10] or None,
    }


def _barometer_block(baro: dict[str, Any] | None) -> dict[str, Any]:
    if not baro:
        return {"available": False, "error": "barometer_feed.json недостъпен"}
    conf = baro.get("confluence") or {}
    return {
        "available": True,
        "alarm_count": conf.get("alarm_count"),
        "base_count": conf.get("base_count"),
        "net": conf.get("net"),
        "has_confluence": conf.get("has_confluence"),
        "direction": conf.get("direction"),
        "as_of": (baro.get("as_of") or "")[:10] or None,
    }


def build_organism_payload(state: dict[str, Any],
                           funding: dict[str, Any] | None,
                           baro: dict[str, Any] | None,
                           vrm_block: dict[str, Any] | None,
                           now: datetime | None = None) -> dict[str, Any]:
    """Чист merge на вече-фетчнатите входове → organism.json payload.

    `vrm_block` = живия data-core-live VRM (от read_vrm_from_datacore); None = overlay
    липсва/нечетим → блокът свети `available:False` (S14 честен мъртъв канал, не тих
    stale). None за funding/baro = провал при фетч → същото. `state` е задължителен
    (собствения state.json от диска)."""
    now = now or datetime.now(timezone.utc)
    if vrm_block is not None:
        vrm = vrm_block                      # data-core-live (Gate 3 flip 24.06)
    else:
        vrm = {"available": False, "source": "data-core-live",
               "error": "data-core vrm_overlay недостъпен"}

    week = state.get("week") or {}
    return {
        "schema_version": ORGANISM_SCHEMA_VERSION,
        "generated_at": now.astimezone(timezone.utc).isoformat(timespec="seconds"),
        "week": week.get("label"),
        "organism_health": _organism_health(state),
        "vrm": vrm,
        "funding": _funding_block(funding),
        "barometer": _barometer_block(baro),
        "macro": _macro_from_state(state),
        "links": {
            "satellite": SATELLITE_STATE_URL,
            "satellite_dashboard": SATELLITE_DASHBOARD_URL,
            "funding": FUNDING_URL,
            "barometer": BAROMETER_URL,
        },
    }


# ── Оркестрация (с I/O) ───────────────────────────────────────────────────────

def _load_state(state_path: Path) -> dict[str, Any]:
    if not state_path.exists():
        raise FileNotFoundError(
            f"state.json липсва: {state_path}. Пусни `macro-satellite dashboard` първо "
            f"(organism чете готовия state.json)."
        )
    return json.loads(state_path.read_text(encoding="utf-8"))


def _try_fetch_json(url: str) -> dict[str, Any] | None:
    try:
        return fetch_json(url)
    except Exception as e:  # noqa: BLE001 — честен degrade, не криеме
        log.warning("organism source fetch failed",
                    extra={"url": url, "error": str(e)})
        return None


def write_organism_json(state_path: Path | None = None,
                        output_dir: Path | None = None,
                        now: datetime | None = None) -> Path:
    """Чете готовия state.json, фетчва funding+барометър (degrade-safe) + живия
    data-core VRM overlay и пише docs/organism.json. Връща пътя."""
    docs = output_dir or (REPO_ROOT / "docs")
    state_path = state_path or (docs / "state.json")
    state = _load_state(state_path)

    funding = _try_fetch_json(FUNDING_URL)
    baro = _try_fetch_json(BAROMETER_URL)

    # VRM: живия data-core weekly overlay (Gate 3 flip 24.06 → source-of-truth).
    # DATACORE_STATE_DIR сочи към data-core/data/state (CI: .data-core checkout). Липсва ли
    # (без env/checkout/файл) → vrm_block=None → блокът свети available:false (S14 честно).
    state_dir = os.environ.get("DATACORE_STATE_DIR")
    vrm_block = read_vrm_from_datacore(Path(state_dir)) if state_dir else None

    payload = build_organism_payload(state, funding, baro, vrm_block, now=now)

    docs.mkdir(parents=True, exist_ok=True)
    path = docs / "organism.json"
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    dead = [name for name, blk in (
        ("funding", payload["funding"]), ("barometer", payload["barometer"]),
        ("vrm", payload["vrm"])) if not blk.get("available")]
    log.info("organism.json written",
             extra={"path": str(path), "size_kb": path.stat().st_size // 1024,
                    "week": payload["week"], "dead_blocks": dead})
    return path
