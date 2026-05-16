"""VRM state shift между две дати."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date


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
    SELECT date, regime, ks_status, alignment_score, gms_value
    FROM vrm_state
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

    return VrmDelta(
        date_a=date_a, date_b=date_b,
        regime_a=a["regime"], regime_b=b["regime"],
        regime_changed=a["regime"] != b["regime"],
        ks_status_a=a["ks_status"], ks_status_b=b["ks_status"],
        ks_status_changed=a["ks_status"] != b["ks_status"],
        alignment_a=None if (val := a["alignment_score"]) != val else float(val),
        alignment_b=None if (val := b["alignment_score"]) != val else float(val),
        alignment_delta=_delta(a["alignment_score"], b["alignment_score"]),
        gms_a=None if (val := a["gms_value"]) != val else float(val),
        gms_b=None if (val := b["gms_value"]) != val else float(val),
        gms_delta=_delta(a["gms_value"], b["gms_value"]),
        found_both=True,
    )
