"""Backfill чрез GitHub commit history на даден файл.

За всеки commit: fetch на raw файла за този SHA → parse → upsert. Idempotent —
проверяваме дали вече имаме дата в съответната таблица преди да fetch-нем.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from datetime import date

import pyarrow.parquet as pq

from ..collectors.base import parser_for
from ..config import DashboardConfig, DashboardsConfig, load_dashboards_config
from ..logging_setup import get_logger
from ..paths import parquet_partition_path
from ..sources import github_history, github_raw
from ..storage import parquet_writer, raw_archive

log = get_logger(__name__)


@dataclass
class BackfillResult:
    name: str
    commits_seen: int = 0
    dates_processed: int = 0
    dates_skipped_existing: int = 0
    rows_written: int = 0
    errors: list[str] = field(default_factory=list)


def _dates_with_data(table: str, candidate_dates: set[date],
                     source_prefix: str | None = None) -> set[date]:
    """Връща subset на dates, които вече имат ред в Parquet таблицата.

    Ако source_prefix е подаден → счита dates за "имащи данни" САМО ако има ред
    със source започващ с този prefix. Това е важно за git backfill — да НЕ
    пропуска дати, които имат само yfinance данни (без rich dashboard fields).
    """
    have: set[date] = set()
    by_month: dict[tuple[int, int], list[date]] = {}
    for d in candidate_dates:
        by_month.setdefault((d.year, d.month), []).append(d)
    for (y, m), dates in by_month.items():
        path = parquet_partition_path(table, y, m)
        if not path.exists():
            continue
        cols = ["date"] + (["source"] if source_prefix else [])
        existing = pq.read_table(path, columns=cols).to_pandas()
        if source_prefix:
            existing = existing[existing["source"].astype(str).str.startswith(source_prefix)]
        existing_set = set(existing["date"].tolist())
        for d in dates:
            if d in existing_set:
                have.add(d)
    return have


def backfill_dashboard(
    d: DashboardConfig,
    since: date | None = None,
    until: date | None = None,
    only_dates: list[date] | None = None,
    throttle_ms: int = 100,
) -> BackfillResult:
    """Backfill един dashboard. `only_dates` (ако подадено) ограничава до конкретни дати."""
    result = BackfillResult(name=d.name)

    commits = github_history.list_file_commits(d.github, since=since, until=until)
    result.commits_seen = len(commits)
    if not commits:
        log.warning("backfill: no commits found", extra={"dashboard": d.name})
        return result

    by_date = github_history.latest_commit_per_date(commits)

    if only_dates is not None:
        wanted = set(only_dates)
        by_date = {dt: c for dt, c in by_date.items() if dt in wanted}

    candidate_dates = set(by_date.keys())
    # Skip only ако вече имаме git-sourced row за тази дата.
    # Дати, които имат само yfinance row → НЕ пропускаме (rich dashboard data missing).
    skip = _dates_with_data(d.table, candidate_dates, source_prefix=f"{d.name}_git")
    result.dates_skipped_existing = len(skip)

    to_process = sorted(d for d in candidate_dates if d not in skip)

    parser = parser_for(d)
    from pathlib import Path
    fname = Path(d.github.file).name

    for snapshot_date in to_process:
        commit = by_date[snapshot_date]
        try:
            raw = github_raw.fetch_at_sha(d.github, commit.sha)
            raw_archive.write(snapshot_date, d.name, fname, raw)
            df = parser(raw, snapshot_date, f"{d.name}_git@{commit.short_sha}")
            n = parquet_writer.upsert(d.table, df, key_cols=d.key_cols)
            result.rows_written += n
            result.dates_processed += 1
            log.info("backfill date ok", extra={
                "dashboard": d.name, "date": str(snapshot_date),
                "sha": commit.short_sha, "rows": n,
            })
            if throttle_ms:
                time.sleep(throttle_ms / 1000)
        except Exception as e:
            result.errors.append(f"{snapshot_date}: {e}")
            log.error("backfill date failed", extra={
                "dashboard": d.name, "date": str(snapshot_date), "error": str(e),
            })

    return result


def backfill_by_name(
    name: str,
    cfg: DashboardsConfig | None = None,
    **kw,
) -> BackfillResult:
    cfg = cfg or load_dashboards_config()
    return backfill_dashboard(cfg.by_name(name), **kw)
