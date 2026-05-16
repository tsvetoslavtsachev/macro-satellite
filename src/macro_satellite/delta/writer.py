"""Pipeline: orchestrate delta computations + JSON output в deltas/daily/."""
from __future__ import annotations

import dataclasses
import json
from datetime import date

from ..logging_setup import get_logger
from ..paths import delta_output_path
from ..storage.duckdb_conn import get_duck
from ..utils.dates import date_to_iso, days_between, utc_now
from .price_delta import interval_change_many
from .rotation_delta import rotation_event_diff
from .vrm_delta import vrm_shift

log = get_logger(__name__)


def _serialize(obj):
    if dataclasses.is_dataclass(obj):
        d = dataclasses.asdict(obj)
        return {k: _serialize(v) for k, v in d.items()}
    if isinstance(obj, dict):
        return {k: _serialize(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_serialize(x) for x in obj]
    if isinstance(obj, date):
        return date_to_iso(obj)
    return obj


def compute_delta(date_a: date, date_b: date,
                  etf_symbols: list[str] | None = None) -> dict:
    """Изчислява пълен delta пакет между две дати.

    etf_symbols: ако None → използваме default core list.
    """
    if etf_symbols is None:
        etf_symbols = ["USO", "XLE", "DFEN", "URA", "GLD", "TLT", "UUP",
                       "SPY", "QQQ", "IWM"]

    duck = get_duck()
    etf_results = interval_change_many(etf_symbols, date_a, date_b, duck)
    etf_changes = []
    for sym, r in etf_results.items():
        if isinstance(r, str):
            etf_changes.append({"symbol": sym, "error": r})
        else:
            etf_changes.append(dataclasses.asdict(r))

    rot_us = rotation_event_diff(date_a, date_b, "us", duck)
    rot_eu = rotation_event_diff(date_a, date_b, "eu", duck)
    vrm = vrm_shift(date_a, date_b, duck)

    return _serialize({
        "date_a": date_a,
        "date_b": date_b,
        "interval_days": days_between(date_a, date_b),
        "etf_changes": etf_changes,
        "rotation_us": rot_us,
        "rotation_eu": rot_eu,
        "vrm_shift": vrm,
        "generated_at": utc_now().isoformat(),
    })


def write_delta(date_a: date, date_b: date,
                etf_symbols: list[str] | None = None) -> tuple[dict, str]:
    payload = compute_delta(date_a, date_b, etf_symbols=etf_symbols)
    out = delta_output_path(date_to_iso(date_a), date_to_iso(date_b))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False, default=str),
                   encoding="utf-8")
    log.info("delta written", extra={"path": str(out)})
    return payload, str(out)


def _to_date(x) -> date:
    """Convert pandas Timestamp / numpy datetime64 / date → date."""
    if isinstance(x, date) and not hasattr(x, "hour"):
        return x
    # pandas Timestamp has .date(); datetime has .date(); fallback to isoformat slice
    if hasattr(x, "date"):
        return x.date()
    import pandas as pd
    return pd.Timestamp(x).date()


def find_auto_prev_dates() -> tuple[date, date]:
    """Намира (предишна, последна) snapshot дати в etf_prices."""
    duck = get_duck()
    df = duck.execute(
        "SELECT DISTINCT date FROM etf_prices ORDER BY date DESC LIMIT 2"
    ).df()
    if len(df) < 2:
        raise RuntimeError(f"Need >=2 distinct dates in etf_prices, have {len(df)}")
    latest = _to_date(df.iloc[0]["date"])
    prev = _to_date(df.iloc[1]["date"])
    return prev, latest
