"""Organism vitrine producer — docs/organism.json.

Консолидиран cross-env snapshot на ЦЕЛИЯ организъм в ЕДИН публичен JSON, четим с
обикновен web fetch от всяка среда (CC · Cowork · claude.ai web/mobile). Това е
производната „снимка"; data-core остава частен.

ADDITIVE — НЕ пипа state_export.py / state.json. Слой над вече-публични входове:
- собствения docs/state.json (data_health за 12 сензора + макро режими)  ← от диска
- treasury-funding-radar funding_state.json (5 лампи)                      ← fetch
- ETF-rotationradar barometer_feed.json (10 индикатора)                    ← fetch
- vrm-state VRM_WEEK.md (VRM детайл — markdown parse)                      ← fetch

Cardinal rule: моделът никога не фабрикува число — детерминистичният път (този
модул) парсва и пише. Падне ли източник → блокът свети `available:false`
(договорът от S14 — мъртъв канал свети честно, не нула).

Strangler: VRM блокът е `source:"excel-frozen"` (чете VRM_WEEK.md) ДОКАТО мозъчният
Gate 3 flip не стане; после producer-ът ще чете data-core state → `data-core-live`.
Витрината не се променя — само източникът на VRM полето.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ..logging_setup import get_logger
from ..paths import REPO_ROOT
from ..utils.http import fetch_bytes, fetch_json

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
VRM_WEEK_URL = (
    "https://raw.githubusercontent.com/tsvetoslavtsachev/vrm-state/main/VRM_WEEK.md"
)
SATELLITE_STATE_URL = (
    "https://raw.githubusercontent.com/tsvetoslavtsachev/macro-satellite/main/docs/state.json"
)
SATELLITE_DASHBOARD_URL = "https://tsvetoslavtsachev.github.io/macro-satellite/"


# ── VRM_WEEK.md parser ────────────────────────────────────────────────────────
# Полетата в VRM_WEEK.md са `KEY:    value` редове вътре в code-блокове. Парсваме
# само авторитетните ключове; не интерпретираме — извличаме дословно.

def _field(md: str, key: str) -> str | None:
    """Извлича стойността на `KEY: value` ред (key е в началото на реда)."""
    m = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", md, re.MULTILINE)
    return m.group(1).strip() if m else None


def _vrm_last_updated(md: str) -> str | None:
    m = re.search(r"\*\*Последна актуализация:\*\*\s*(\d{4}-\d{2}-\d{2})", md)
    return m.group(1) if m else None


def parse_vrm_week(md: str) -> dict[str, Any]:
    """VRM_WEEK.md → структуриран VRM блок. Връща `available:False` ако ядрото
    (РЕЖИМ) липсва — не гадаем формат (cardinal rule)."""
    regime = _field(md, "РЕЖИМ")
    if not regime:
        return {"available": False, "source": "excel-frozen",
                "error": "VRM_WEEK.md: липсва РЕЖИМ ядро (неочакван формат)"}

    align_score = _field(md, "ALIGNMENT")
    align_max = _field(md, "ALIGNMENT_MAX")
    gms_score = _field(md, "GMS_SCORE")
    gms_max = _field(md, "GMS_MAX")
    gms_label = _field(md, "GMS_LABEL")
    signal_raw = _field(md, "СИГНАЛ")
    ks_active_raw = _field(md, "KS_АКТИВЕН")

    def _ratio(score: str | None, total: str | None) -> str | None:
        if score is None or total is None:
            return None
        try:
            return f"{int(float(score))}/{int(float(total))}"
        except (ValueError, TypeError):
            return f"{score}/{total}"

    alignment = _ratio(align_score, align_max)
    gms_ratio = _ratio(gms_score, gms_max)
    gms = f"{gms_ratio} {gms_label}".strip() if gms_ratio else None

    return {
        "available": True,
        "source": "excel-frozen",
        "regime": regime,
        "regime_bg": _field(md, "РЕЖИМ_БГ"),
        "signal": signal_raw.split(" (")[0].strip() if signal_raw else None,
        "alignment": alignment,
        "alignment_label": _field(md, "ALIGNMENT_LABEL"),
        "gms": gms,
        "ks_active": bool(ks_active_raw and ks_active_raw.strip().upper().startswith("ДА")),
        "ks_status": _field(md, "KS_СТАТУС"),
        "as_of": _vrm_last_updated(md),
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
                           vrm_md: str | None,
                           now: datetime | None = None) -> dict[str, Any]:
    """Чист merge на вече-фетчнатите входове → organism.json payload.

    None за funding/baro/vrm_md = провал при фетч → блокът свети `available:False`.
    `state` е задължителен (собствения state.json от диска)."""
    now = now or datetime.now(timezone.utc)
    if vrm_md is None:
        vrm = {"available": False, "source": "excel-frozen",
               "error": "VRM_WEEK.md недостъпен"}
    else:
        vrm = parse_vrm_week(vrm_md)

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
            "vrm": VRM_WEEK_URL,
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


def _try_fetch_text(url: str) -> str | None:
    try:
        return fetch_bytes(url).decode("utf-8")
    except Exception as e:  # noqa: BLE001
        log.warning("organism source fetch failed",
                    extra={"url": url, "error": str(e)})
        return None


def write_organism_json(state_path: Path | None = None,
                        output_dir: Path | None = None,
                        now: datetime | None = None) -> Path:
    """Чете готовия state.json, фетчва 3-те външни източника (degrade-safe) и пише
    docs/organism.json. Връща пътя."""
    docs = output_dir or (REPO_ROOT / "docs")
    state_path = state_path or (docs / "state.json")
    state = _load_state(state_path)

    funding = _try_fetch_json(FUNDING_URL)
    baro = _try_fetch_json(BAROMETER_URL)
    vrm_md = _try_fetch_text(VRM_WEEK_URL)

    payload = build_organism_payload(state, funding, baro, vrm_md, now=now)

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
