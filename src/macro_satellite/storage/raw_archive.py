"""Копие на оригиналните JSON/MD файлове по дата.

storage/raw/YYYY-MM-DD/<dashboard>/<filename>
"""
from __future__ import annotations

from datetime import date

from ..paths import raw_archive_path
from ..utils.dates import date_to_iso


def write(d: date, dashboard: str, filename: str, content: bytes) -> None:
    p = raw_archive_path(date_to_iso(d), dashboard, filename)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(content)


def read(d: date, dashboard: str, filename: str) -> bytes | None:
    p = raw_archive_path(date_to_iso(d), dashboard, filename)
    if not p.exists():
        return None
    return p.read_bytes()
