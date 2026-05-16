"""CLI entry point.

  python -m macro_satellite collect
  python -m macro_satellite backfill --dashboard etf_dashboard --since 2026-01-01
  python -m macro_satellite backfill --dashboard etf_dashboard --dates 2026-05-07,2026-05-15
  python -m macro_satellite backfill-yf
  python -m macro_satellite delta --from 2026-05-07 --to 2026-05-15
  python -m macro_satellite delta --auto-prev
"""
from __future__ import annotations

import argparse
import sys
from datetime import date

from .logging_setup import setup_logging


def _parse_date(s: str) -> date:
    return date.fromisoformat(s)


def _parse_date_list(s: str) -> list[date]:
    return [date.fromisoformat(x.strip()) for x in s.split(",")]


def cmd_collect(args) -> int:
    from .runner import run_collect
    report = run_collect()
    n_ok = len(report.successes)
    n_fail = len(report.failures)
    print(f"collect: {n_ok} ok, {n_fail} failed")
    for r in report.successes:
        print(f"  + {r.name}: {r.rows_written} rows, snapshot={r.snapshot_date}")
    for r in report.failures:
        print(f"  - {r.name}: {r.error}")
    # Exit 0 if AT LEAST ONE dashboard succeeded — transient failures (auth, 404,
    # network) of individual sources shouldn't fail the whole workflow.
    # Exit 1 only if everything failed (likely a systemic problem).
    return 0 if n_ok > 0 else 1


def cmd_backfill(args) -> int:
    from .backfill.github_history import backfill_by_name

    kw = {}
    if args.since:
        kw["since"] = _parse_date(args.since)
    if args.until:
        kw["until"] = _parse_date(args.until)
    if args.dates:
        kw["only_dates"] = _parse_date_list(args.dates)

    res = backfill_by_name(args.dashboard, **kw)
    print(f"backfill {res.name}: commits_seen={res.commits_seen} "
          f"dates_processed={res.dates_processed} "
          f"dates_skipped={res.dates_skipped_existing} "
          f"rows_written={res.rows_written} errors={len(res.errors)}")
    for e in res.errors:
        print(f"  ! {e}")
    return 0 if not res.errors else 1


def cmd_backfill_yf(args) -> int:
    from .backfill.yfinance_backfill import run_yf_backfill
    res = run_yf_backfill()
    print(f"yfinance backfill: requested={res.symbols_requested} "
          f"with_data={res.symbols_with_data} rows_written={res.rows_written} "
          f"errors={len(res.errors)}")
    for e in res.errors:
        print(f"  ! {e}")
    return 0 if not res.errors else 1


def cmd_delta(args) -> int:
    from .delta.writer import find_auto_prev_dates, write_delta

    if args.auto_prev:
        date_a, date_b = find_auto_prev_dates()
    else:
        if not args.from_ or not args.to:
            print("delta requires --from and --to (or --auto-prev)", file=sys.stderr)
            return 2
        date_a = _parse_date(args.from_)
        date_b = _parse_date(args.to)
    payload, path = write_delta(date_a, date_b)
    print(f"delta: {date_a} → {date_b} ({payload['interval_days']}d) → {path}")
    return 0


def cmd_briefing(args) -> int:
    """Генерира седмичен briefing markdown в briefings/."""
    from datetime import date as _date

    from .analytics.briefing import generate_briefing
    from .analytics.weekly_window import current_week, iso_week_for

    if args.week:
        # parse 'YYYY-MM-DD' (anchor date in target week)
        d = _date.fromisoformat(args.week)
        target = iso_week_for(d)
    else:
        target = current_week()
    md, path = generate_briefing(target)
    print(f"briefing: {target.label} ({target.week_start}..{target.week_end})")
    print(f"  written: {path}")
    print(f"  size:    {len(md)} bytes")
    return 0


def cmd_anomalies(args) -> int:
    """Списък ETF движения с |z|>=threshold за дадена седмица."""
    from datetime import date as _date

    from .analytics.weekly_window import current_week, iso_week_for
    from .analytics.z_scores import scan_universe
    from .analytics.briefing import CORE_ETFS
    from .storage.duckdb_conn import get_duck

    duck = get_duck()
    if args.week:
        target = iso_week_for(_date.fromisoformat(args.week))
    else:
        target = current_week()
    threshold = args.threshold
    results = scan_universe(duck, CORE_ETFS, target, trailing_n=13, z_threshold=threshold)
    print(f"anomalies for {target.label} ({target.week_start}..{target.week_end}), "
          f"|z| >= {threshold}, trailing 13w:")
    if not results:
        print("  none.")
        return 0
    for r in results:
        print(f"  {r.symbol:>6}: {r.weekly_change*100:+6.2f}% "
              f"({r.z_score:+5.2f}σ) "
              f"{r.date_a} {r.price_a:.2f} -> {r.date_b} {r.price_b:.2f}")
    return 0


def cmd_verify(args) -> int:
    """Quick verification — read all parquet tables and print row counts."""
    from .storage.duckdb_conn import get_duck
    from .storage.schema import SCHEMA_REGISTRY
    duck = get_duck()
    for tbl in SCHEMA_REGISTRY:
        try:
            df = duck.execute(
                f"SELECT count(*) AS n, "
                f"COALESCE(CAST(min(date) AS VARCHAR),'-') AS dmin, "
                f"COALESCE(CAST(max(date) AS VARCHAR),'-') AS dmax "
                f"FROM {tbl}"
            ).df()
            n, dmin, dmax = df.iloc[0]["n"], df.iloc[0]["dmin"], df.iloc[0]["dmax"]
            print(f"  {tbl:<22}: {n:>6} rows, dates {dmin}..{dmax}")
        except Exception as e:
            print(f"  {tbl}: ERROR - {e}")
    return 0


def main(argv: list[str] | None = None) -> int:
    setup_logging()
    p = argparse.ArgumentParser(prog="macro-satellite")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("collect", help="Live collect от всички dashboards")

    bf = sub.add_parser("backfill", help="Backfill един dashboard от GitHub history")
    bf.add_argument("--dashboard", required=True)
    bf.add_argument("--since", help="ISO date (e.g. 2026-01-01)")
    bf.add_argument("--until", help="ISO date")
    bf.add_argument("--dates", help="Comma-separated ISO dates, ограничава до тях")

    sub.add_parser("backfill-yf", help="yfinance bootstrap за ETF prices")

    dlt = sub.add_parser("delta", help="Compute delta JSON between two dates")
    dlt.add_argument("--from", dest="from_", help="ISO date A")
    dlt.add_argument("--to", help="ISO date B")
    dlt.add_argument("--auto-prev", action="store_true",
                     help="Most-recent vs prev-snapshot date в etf_prices")

    sub.add_parser("verify", help="Row counts + date ranges на всички таблици")

    br = sub.add_parser("briefing", help="Генерира седмичен briefing markdown")
    br.add_argument("--week", help="Anchor date в target седмицата (ISO YYYY-MM-DD). "
                                    "Default: current week.")

    an = sub.add_parser("anomalies", help="ETF moves с |z|>=threshold за седмица")
    an.add_argument("--week", help="Anchor date (ISO YYYY-MM-DD). Default: current.")
    an.add_argument("--threshold", type=float, default=1.5,
                    help="|z| threshold (default 1.5)")

    args = p.parse_args(argv)
    handlers = {
        "collect": cmd_collect,
        "backfill": cmd_backfill,
        "backfill-yf": cmd_backfill_yf,
        "delta": cmd_delta,
        "verify": cmd_verify,
        "briefing": cmd_briefing,
        "anomalies": cmd_anomalies,
    }
    return handlers[args.cmd](args)


def main_module() -> None:
    sys.exit(main())


if __name__ == "__main__":
    main_module()
