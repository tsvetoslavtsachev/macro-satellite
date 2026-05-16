"""Rotation event diff между две дати.

Открива тикерите, които са влезли или излезли от 'stable_winner', 'quality_dip',
'faded_bounce' квадранти, поотделно за 1m и 3m horizon.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date

QUADRANTS_OF_INTEREST = ("stable_winner", "quality_dip", "faded_bounce")


@dataclass
class RotationDelta:
    universe: str  # 'us' или 'eu'
    date_a: date
    date_b: date
    # event_type → list[ticker]
    events: dict[str, list[str]] = field(default_factory=dict)


def rotation_event_diff(date_a: date, date_b: date, universe: str, duck) -> RotationDelta:
    table = f"rotation_{universe}"
    sql = f"SELECT ticker, quadrant_1m, quadrant_3m FROM {table} WHERE date = ?"
    a = duck.execute(sql, [date_a]).df()
    b = duck.execute(sql, [date_b]).df()

    out = RotationDelta(universe=universe, date_a=date_a, date_b=date_b)

    if a.empty or b.empty:
        out.events["_warning"] = [f"empty snapshot: a={len(a)}, b={len(b)}"]
        return out

    merged = a.merge(b, on="ticker", how="outer", suffixes=("_a", "_b"))
    for q in QUADRANTS_OF_INTEREST:
        for horizon in ("1m", "3m"):
            col_a = f"quadrant_{horizon}_a"
            col_b = f"quadrant_{horizon}_b"
            entered = merged[(merged[col_a] != q) & (merged[col_b] == q)]
            exited = merged[(merged[col_a] == q) & (merged[col_b] != q)]
            out.events[f"entered_{q}_{horizon}"] = sorted(entered["ticker"].dropna().tolist())
            out.events[f"exited_{q}_{horizon}"] = sorted(exited["ticker"].dropna().tolist())
    return out
