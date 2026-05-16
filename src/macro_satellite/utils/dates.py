"""Date utilities.

CONVENTION (D4 from plan):
  `date` колоната в Parquet = `updatedAt.date()` в UTC. Просто, deterministic,
  documented. Ако ETF Dashboard commit-ва 22:44 UTC на 15 май, snapshot-а влиза
  като date=2026-05-15. Това отразява "след-пазарния" snapshot за 15 май US пазар.
"""
from __future__ import annotations

import datetime as dt
from datetime import date, datetime, timezone


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def today_utc() -> date:
    return utc_now().date()


def parse_iso_date(s: str) -> date:
    """'2026-05-15' → date(2026, 5, 15)."""
    return date.fromisoformat(s)


def parse_iso_datetime(s: str) -> datetime:
    """'2026-05-15T22:44:31Z' → tz-aware UTC datetime."""
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    d = datetime.fromisoformat(s)
    if d.tzinfo is None:
        d = d.replace(tzinfo=timezone.utc)
    return d.astimezone(timezone.utc)


def date_to_iso(d: date) -> str:
    return d.isoformat()


def date_to_partition(d: date) -> tuple[int, int]:
    return d.year, d.month


def days_between(a: date, b: date) -> int:
    return (b - a).days


def daterange_inclusive(a: date, b: date) -> list[date]:
    return [a + dt.timedelta(days=i) for i in range(days_between(a, b) + 1)]
