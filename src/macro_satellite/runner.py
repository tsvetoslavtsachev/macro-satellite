"""Live collect orchestrator. Чете config, fetch-ва, parse-ва, upsert-ва.

Per-dashboard try/except — един fail не блокира останалите.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from .collectors.base import FetchError, ParseError, parser_for
from .config import DashboardConfig, DashboardsConfig, load_dashboards_config
from .logging_setup import get_logger
from .paths import ensure_dirs
from .sources import github_raw
from .storage import parquet_writer, raw_archive

log = get_logger(__name__)


@dataclass
class DashboardResult:
    name: str
    ok: bool
    rows_written: int = 0
    snapshot_date: str | None = None
    error: str | None = None


@dataclass
class CollectorReport:
    successes: list[DashboardResult] = field(default_factory=list)
    failures: list[DashboardResult] = field(default_factory=list)

    @property
    def all_ok(self) -> bool:
        return not self.failures


def _collect_one(d: DashboardConfig) -> DashboardResult:
    log.info("collect start", extra={"dashboard": d.name, "table": d.table})
    try:
        raw_bytes = github_raw.fetch_latest(d.github)
    except FileNotFoundError as e:
        raise FetchError(str(e)) from e
    except Exception as e:
        raise FetchError(f"{d.name}: fetch failed: {e}") from e

    parser = parser_for(d)
    try:
        df = parser(raw_bytes, None, f"{d.name}_live")
    except Exception as e:
        raise ParseError(f"{d.name}: parser failed: {e}") from e

    if df.empty:
        log.warning("collect produced 0 rows", extra={"dashboard": d.name})
        return DashboardResult(name=d.name, ok=True, rows_written=0)

    snapshot_date: date = df["date"].iloc[0]
    raw_archive.write(snapshot_date, d.name, Path(d.github.file).name, raw_bytes)
    n = parquet_writer.upsert(d.table, df, key_cols=d.key_cols)
    log.info("collect ok", extra={
        "dashboard": d.name, "rows": n, "snapshot_date": str(snapshot_date),
    })
    return DashboardResult(
        name=d.name, ok=True, rows_written=n,
        snapshot_date=str(snapshot_date),
    )


def _collect_datacore_state(d: DashboardConfig) -> DashboardResult:
    """datacore-state източник → жив VRM tip от data-core overlay (READ-ONLY).

    Degrade-safe: липсва ли overlay (без env/checkout/файл) → 0 реда (ok=True), не
    падане → S14 показва сензора честно като 'missing'."""
    from .collectors.vrm_overlay import collect_overlay
    df = collect_overlay(source=f"{d.name}_live")
    if df is None or df.empty:
        log.warning("datacore-state collect produced 0 rows (degrade-safe)",
                    extra={"dashboard": d.name})
        return DashboardResult(name=d.name, ok=True, rows_written=0)
    snapshot_date: date = df["date"].iloc[0]
    n = parquet_writer.upsert(d.table, df, key_cols=d.key_cols)
    log.info("datacore-state collect ok", extra={
        "dashboard": d.name, "rows": n, "snapshot_date": str(snapshot_date),
    })
    return DashboardResult(
        name=d.name, ok=True, rows_written=n, snapshot_date=str(snapshot_date),
    )


def run_collect(cfg: DashboardsConfig | None = None) -> CollectorReport:
    ensure_dirs()
    cfg = cfg or load_dashboards_config()
    report = CollectorReport()
    for d in cfg.dashboards:
        # datacore-state (source_kind: datacore-state за `vrm`) → чете живия data-core
        # overlay и пише таблицата ТУК (преди dashboard/state_export). READ-ONLY към
        # data-core; degrade-safe ако checkout-ът липсва.
        if d.source_kind == "datacore-state":
            try:
                report.successes.append(_collect_datacore_state(d))
            except Exception as e:  # noqa: BLE001
                log.error("collect failed",
                          extra={"dashboard": d.name, "error": str(e)})
                report.failures.append(
                    DashboardResult(name=d.name, ok=False, error=str(e)))
            continue
        # Не-github източници (source_kind: yfinance за etf_prices) се пълнят от
        # собствената си стъпка (backfill-yf), не от дневния github collect. Остават
        # в config-а само за S14 data_health обхождането (свежест от таблицата).
        if d.source_kind != "github":
            log.info("collect skip (non-github source)",
                     extra={"dashboard": d.name, "source_kind": d.source_kind})
            continue
        try:
            res = _collect_one(d)
            report.successes.append(res)
        except Exception as e:
            log.error("collect failed", extra={"dashboard": d.name, "error": str(e)})
            report.failures.append(DashboardResult(name=d.name, ok=False, error=str(e)))

    # Post-collect: expand macro_state JSON columns into long-format tables.
    # Idempotent — re-runs over всички snapshots, upsert per (date, region, key).
    try:
        from .analytics.macro_anomalies_expander import expand_all
        x = expand_all()
        log.info("macro expander", extra={
            f"{r.lower()}_rows": res.anomaly_rows + res.divergence_rows
            for r, res in x.items()
        })
    except Exception as e:
        log.warning("macro expander failed (non-fatal)", extra={"error": str(e)})

    return report
