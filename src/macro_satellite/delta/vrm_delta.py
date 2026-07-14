"""VRM state shift между две дати — от живата таблица `vrm` (мандат №36).

ks_status_a/b са деривирани display статуси от ks_active (bool|None):
True→"active", False→"inactive", None→"unknown" — None не е inactive, не
фабрикуваме сигурност. gms идва от gms_score (живото GMS на мозъка).
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from ..utils.vrm import ks_status_from_active


@dataclass
class VrmDelta:
    date_a: date
    date_b: date
    regime_a: str | None
    regime_b: str | None
    regime_changed: bool
    ks_status_a: str | None
    ks_status_b: str | None
    ks_status_changed: bool
    alignment_a: float | None
    alignment_b: float | None
    alignment_delta: float | None
    gms_a: float | None
    gms_b: float | None
    gms_delta: float | None
    found_both: bool


def vrm_shift(date_a: date, date_b: date, duck) -> VrmDelta:
    sql = """
    SELECT date, regime, ks_active, alignment_score, gms_score
    FROM vrm
    WHERE date IN (?, ?)
    ORDER BY date
    """
    df = duck.execute(sql, [date_a, date_b]).df()
    df = df.drop_duplicates(subset=["date"], keep="last")
    found_both = len(df) == 2
    if not found_both:
        return VrmDelta(
            date_a=date_a, date_b=date_b,
            regime_a=None, regime_b=None, regime_changed=False,
            ks_status_a=None, ks_status_b=None, ks_status_changed=False,
            alignment_a=None, alignment_b=None, alignment_delta=None,
            gms_a=None, gms_b=None, gms_delta=None,
            found_both=False,
        )
    df = df.sort_values("date").reset_index(drop=True)
    a, b = df.iloc[0], df.iloc[1]

    def _delta(x, y):
        import pandas as pd
        if pd.isna(x) or pd.isna(y):
            return None
        return float(y) - float(x)

    ks_a = ks_status_from_active(a["ks_active"])
    ks_b = ks_status_from_active(b["ks_active"])

    return VrmDelta(
        date_a=date_a, date_b=date_b,
        regime_a=a["regime"], regime_b=b["regime"],
        regime_changed=a["regime"] != b["regime"],
        ks_status_a=ks_a, ks_status_b=ks_b,
        ks_status_changed=ks_a != ks_b,
        alignment_a=None if (val := a["alignment_score"]) != val else float(val),
        alignment_b=None if (val := b["alignment_score"]) != val else float(val),
        alignment_delta=_delta(a["alignment_score"], b["alignment_score"]),
        gms_a=None if (val := a["gms_score"]) != val else float(val),
        gms_b=None if (val := b["gms_score"]) != val else float(val),
        gms_delta=_delta(a["gms_score"], b["gms_score"]),
        found_both=True,
    )
