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


def _stale_sources(successes, tol: dict[str, int],
                   today: date) -> list[tuple[str, date, int, int]]:
    """Канали, чийто най-нов snapshot е над своя stale_tolerable_days.

    Връща (name, snapshot_date, age_days, tolerable). Чист — без I/O — за да е
    gate-able. „Успешен" collect върху застоял source (HTTP 200, 1 ред, стара
    дата) НЕ е истинска свежест: тук го хващаме, за да не минава тихо зелено.
    """
    out: list[tuple[str, date, int, int]] = []
    for r in successes:
        td = tol.get(r.name)
        if td is None or not r.snapshot_date:
            continue
        try:
            snap = date.fromisoformat(str(r.snapshot_date))
        except (ValueError, TypeError):
            continue
        age = (today - snap).days
        if age > td:
            out.append((r.name, snap, age, td))
    return out


def cmd_collect(args) -> int:
    from .config import load_dashboards_config
    from .runner import run_collect
    report = run_collect()
    n_ok = len(report.successes)
    n_fail = len(report.failures)
    print(f"collect: {n_ok} ok, {n_fail} failed")
    for r in report.successes:
        print(f"  + {r.name}: {r.rows_written} rows, snapshot={r.snapshot_date}")
    for r in report.failures:
        print(f"  - {r.name}: {r.error}")

    # S14 · staleness audit — мъртъв/застоял канал НЕ минава тихо зелено.
    # Source-ът може да е изостанал (ръчен ъпдейт лагва, напр. VRM_STATE.md) —
    # не е вина на сателита, затова НЕ фейлваме build-а, но крещим ясно: stdout
    # обобщение + GitHub Actions `::warning::` annotation (изскача в run summary).
    tol = {d.name: d.stale_tolerable_days for d in load_dashboards_config().dashboards}
    stale = _stale_sources(report.successes, tol, date.today())
    if stale:
        print(f"\n⚠ STALE DATA — {len(stale)} канал(а) над толеранса (source изостанал):")
        for name, snap, age, td in stale:
            print(f"  ⚠ {name}: {snap} ({age}д > {td}д толеранс)")
            print(f"::warning title=Stale data::{name} последно обновен {snap} "
                  f"— {age}д назад (толеранс {td}д). Source repo-то изостава.")
    else:
        print("\n✓ всички канали в рамките на толеранса")

    # Exit 0 if AT LEAST ONE dashboard succeeded — transient failures (auth, 404,
    # network) of individual sources shouldn't fail the whole workflow.
    # Exit 1 only if everything failed (likely a systemic problem).
    # NB: staleness НЕ е fail — surfac-ва се като warning, не блокира pipeline-а.
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


def cmd_export_week(args) -> int:
    """Comprehensive data export за downstream analysis."""
    from datetime import date as _date

    from .analytics.full_export import generate_full_export
    from .analytics.weekly_window import current_week, iso_week_for
    from .paths import REPO_ROOT

    if args.week:
        target = iso_week_for(_date.fromisoformat(args.week))
    else:
        target = current_week()

    output_dir = None
    if args.output_dir:
        from pathlib import Path
        output_dir = Path(args.output_dir)

    md, path = generate_full_export(target, output_dir=output_dir)
    size_kb = len(md) // 1024
    print(f"export-week: {target.label}")
    print(f"  written: {path}")
    print(f"  size:    {size_kb} KB ({len(md):,} chars)")
    return 0


def cmd_dashboard(args) -> int:
    """Генерира interactive HTML dashboard в docs/index.html + state.json sidecar."""
    from .visualization.dashboard import generate_dashboard

    path = generate_dashboard(
        heatmap_weeks=args.heatmap_weeks,
        skip_state_export=args.skip_state_json,
    )
    size_kb = path.stat().st_size // 1024
    state_path = path.parent / "state.json"
    # ASCII-only — избягваме UnicodeEncodeError на Windows cp1252 console
    print(f"dashboard generated: {path} ({size_kb} KB)")
    if state_path.exists():
        print(f"state.json:          {state_path} ({state_path.stat().st_size // 1024} KB)")
    print(f"  Local:        file:///{str(path).replace(chr(92), '/')}")
    print(f"  GitHub Pages: https://tsvetoslavtsachev.github.io/macro-satellite/")
    print(f"  AI snapshot:  https://tsvetoslavtsachev.github.io/macro-satellite/state.json")
    return 0


def cmd_backtest(args) -> int:
    """Backtest на исторически hypothesis (canonical query или ad-hoc condition list)."""
    from .analytics.backtest import (
        ConditionSpec,
        QuerySpec,
        find_query,
        format_report,
        load_canonical_queries,
        run_backtest,
    )
    from .storage.duckdb_conn import get_duck

    duck = get_duck()

    # Mode: --list lists canonical queries
    if args.list:
        print("Canonical queries в config/backtest_queries.yaml:")
        for q in load_canonical_queries():
            print(f"  {q.name:>32}  {q.label_bg}")
        return 0

    # Mode: --query NAME — run pre-defined
    if args.query:
        try:
            q = find_query(args.query)
        except KeyError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 2
    elif args.condition:
        # Ad-hoc: parse conditions like "USO:return_4w>=0.05"
        conds = []
        for raw in args.condition:
            # parse SYMBOL:METRIC OP VALUE
            import re
            m = re.match(r"^([A-Z0-9_]+):([a-z_:0-9]+)([<>=]+)(-?\d+(?:\.\d+)?)$", raw)
            if not m:
                print(f"ERROR: bad condition '{raw}'. Format: SYMBOL:metric>=value", file=sys.stderr)
                return 2
            conds.append(ConditionSpec(
                symbol=m.group(1), metric=m.group(2), op=m.group(3),
                value=float(m.group(4)),
            ))
        q = QuerySpec(
            name="ad_hoc",
            label_bg=f"Ad-hoc: {' AND '.join(args.condition)}",
            conditions=conds,
        )
    else:
        print("ERROR: pass --query NAME, --condition X (1+), или --list", file=sys.stderr)
        return 2

    result = run_backtest(q, duck)

    if args.markdown:
        md = format_report(result)
        from .paths import REPO_ROOT
        out_dir = REPO_ROOT / "briefings" / "backtests"
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"backtest_{q.name}.md"
        path.write_text(md, encoding="utf-8")
        print(f"backtest report written: {path}")
    else:
        # Concise stdout summary
        print(f"=== {result.label_bg or result.query_name} ===")
        print(f"Episodes: {result.n_episodes} (от {result.n_total_matching_days} matching days)")
        print(f"History range: {result.history_start} → {result.history_end}")
        if result.summary_stats:
            print("\nForward returns (mean | median | win_rate):")
            for sym, h_dict in result.summary_stats.items():
                for h, st in h_dict.items():
                    print(f"  {sym:>4} {h:>3}: "
                          f"mean={st['mean']*100:+6.1f}% | "
                          f"median={st['median']*100:+6.1f}% | "
                          f"win_rate={st['win_rate']*100:3.0f}% (n={int(st['n'])})")
        if args.episodes and result.episodes:
            print("\nEpisodes:")
            for ep in result.episodes[:args.episodes]:
                print(f"  {ep.start_date} → {ep.end_date} ({ep.n_days}d)")
    return 0


def cmd_narrative(args) -> int:
    """Генерира narrative briefing markdown (вход за weekly-story-teller)."""
    from datetime import date as _date

    from .analytics.narrative import generate_narrative
    from .analytics.weekly_window import current_week, iso_week_for

    if args.week:
        target = iso_week_for(_date.fromisoformat(args.week))
    else:
        target = current_week()
    md, path = generate_narrative(target)
    print(f"narrative: {target.label}")
    print(f"  written: {path}")
    print(f"  size:    {len(md)} bytes")
    return 0


def cmd_parallels(args) -> int:
    """Top K исторически паралели за дадена седмица + forward returns."""
    from datetime import date as _date

    from .analytics.parallels import find_parallels
    from .analytics.weekly_window import current_week, iso_week_for
    from .storage.duckdb_conn import get_duck

    duck = get_duck()
    if args.week:
        target = iso_week_for(_date.fromisoformat(args.week))
    else:
        target = current_week()
    parallels = find_parallels(duck, target, top_k=args.top_k)
    print(f"Target: {target.label} ({target.week_start}..{target.week_end})")
    print(f"Top {len(parallels)} parallels (cosine similarity vs macro signature):")
    for p in parallels:
        print(f"  {p.match_week} (end {p.match_week_end}): "
              f"cos={p.cosine_similarity:.4f}, common={p.n_common_symbols}")
        for sym in ("SPY", "USO", "GLD", "TLT", "XLE", "IWM"):
            if sym in p.forward_returns:
                fwd = p.forward_returns[sym]
                parts = [f"{h}={v*100:+5.1f}%" for h, v in fwd.items()]
                print(f"      {sym:>4}: " + " | ".join(parts))
    return 0


def cmd_journal_backfill(args) -> int:
    """Машинен backfill на gap-журнала → machine base rate (Phase 6, Тухла 2a)."""
    from datetime import date as _date

    from .analytics.journal.backfill import DEFAULT_START, format_report, run_backfill

    region = (args.region or "US").upper()
    start = _date.fromisoformat(args.start) if args.start else DEFAULT_START
    res = run_backfill(start=start, region=region)
    report = format_report(res)
    print(report)
    if args.markdown:
        from .paths import REPO_ROOT
        out_dir = REPO_ROOT / "briefings" / "journal"
        out_dir.mkdir(parents=True, exist_ok=True)
        fname = ("machine_base_rate.md" if region == "US"
                 else f"machine_base_rate_{region.lower()}.md")
        path = out_dir / fname
        path.write_text("```\n" + report + "\n```\n", encoding="utf-8")
        print(f"\nmarkdown report: {path}")

        # gap серия CSV (за чертане/анализ/публикация)
        import csv as _csv
        csv_name = ("gap_series.csv" if region == "US"
                    else f"gap_series_{region.lower()}.csv")
        csv_path = out_dir / csv_name
        with open(csv_path, "w", newline="", encoding="utf-8") as _f:
            _w = _csv.writer(_f)
            _w.writerow(["week", "week_end", "economy_axis", "markets_axis", "gap"])
            for r in res.gap_rows:
                _w.writerow([r["week"], r["week_end"], r["economy_axis"],
                             r["markets_axis"], r["gap"]])
        print(f"gap series CSV:  {csv_path}")
    return 0


def cmd_journal_prep(args) -> int:
    """Тухла 2b фаза 1 — генерира pre-filled JOURNAL_WEEK.md worksheet."""
    from datetime import date as _date

    from .analytics.journal.orchestrator import prep
    from .utils.dates import today_utc

    region = (args.region or "US").upper()
    jd = _date.fromisoformat(args.date) if args.date else today_utc()
    author = args.author or "Цветослав"
    path = prep(region, author, jd)
    print(f"worksheet: {path}")
    print(f"  регион={region}  дата(T)={jd}  автор={author}")
    print("  → попълни ПРИСЪДА блока, после: macro-satellite journal-judge")
    return 0


def cmd_journal_judge(args) -> int:
    """Тухла 2b фаза 3 — парсва worksheet → валидира (C3 raise) → append + разрешава."""
    from .analytics.journal.orchestrator import ingest

    region = (args.region or "US").upper()
    summary = ingest(default_region=region)
    print(f"journal-judge [{region}]:")
    print(f"  записани присъди: {summary.appended}  (дубликати пропуснати: {summary.skipped})")
    for jid in summary.appended_ids:
        print(f"    + {jid}")
    print(f"  новоразрешени: {summary.resolved}")
    for rid in summary.resolved_ids:
        print(f"    ✓ {rid}")
    return 0


def cmd_journal_calibrate(args) -> int:
    """Тухла 2b стъпка 7 — machine base rate vs human track record (n-дисциплина)."""
    from .analytics.journal.calibration import format_calibration

    region = (args.region or "US").upper()
    report = format_calibration(region)
    print(report)
    if args.markdown:
        from .paths import REPO_ROOT
        out_dir = REPO_ROOT / "briefings" / "journal"
        out_dir.mkdir(parents=True, exist_ok=True)
        fname = ("calibration.md" if region == "US"
                 else f"calibration_{region.lower()}.md")
        path = out_dir / fname
        path.write_text("```\n" + report + "\n```\n", encoding="utf-8")
        print(f"\nmarkdown report: {path}")
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

    jb = sub.add_parser("journal-backfill",
                        help="Машинен backfill на gap-журнала → machine base rate (Тухла 2a)")
    jb.add_argument("--start", help="ISO начална дата (default 2021-05-17, etf начало)")
    jb.add_argument("--region", default="US", help="US | EU | CN")
    jb.add_argument("--markdown", action="store_true",
                    help="Запиши доклада в briefings/journal/machine_base_rate[_<region>].md")

    jp = sub.add_parser("journal-prep",
                        help="Тухла 2b — генерира pre-filled JOURNAL_WEEK.md worksheet")
    jp.add_argument("--region", default="US", help="US | EU | CN")
    jp.add_argument("--date", help="ISO дата на присъдата T (default: днес)")
    jp.add_argument("--author", default="Цветослав")

    jj = sub.add_parser("journal-judge",
                        help="Тухла 2b — парсва worksheet → валидира (C3) → append + разрешава")
    jj.add_argument("--region", default="US", help="US | EU | CN")

    jc = sub.add_parser("journal-calibrate",
                        help="Тухла 2b — machine base rate vs human track (n-дисциплина)")
    jc.add_argument("--region", default="US", help="US | EU | CN")
    jc.add_argument("--markdown", action="store_true",
                    help="Запиши в briefings/journal/calibration[_<region>].md")

    br = sub.add_parser("briefing", help="Генерира седмичен briefing markdown")
    br.add_argument("--week", help="Anchor date в target седмицата (ISO YYYY-MM-DD). "
                                    "Default: current week.")

    an = sub.add_parser("anomalies", help="ETF moves с |z|>=threshold за седмица")
    an.add_argument("--week", help="Anchor date (ISO YYYY-MM-DD). Default: current.")
    an.add_argument("--threshold", type=float, default=1.5,
                    help="|z| threshold (default 1.5)")

    pa = sub.add_parser("parallels", help="Top K historical parallels + forward returns")
    pa.add_argument("--week", help="Anchor date (ISO YYYY-MM-DD). Default: current.")
    pa.add_argument("--top-k", type=int, default=5, dest="top_k")

    nr = sub.add_parser("narrative", help="Narrative briefing (вход за weekly-story-teller)")
    nr.add_argument("--week", help="Anchor date (ISO YYYY-MM-DD). Default: current.")

    ew = sub.add_parser("export-week",
                         help="Comprehensive data export (за downstream parallel-thinking, deep research)")
    ew.add_argument("--week", help="Anchor date (ISO YYYY-MM-DD). Default: current.")
    ew.add_argument("--output-dir", help="Custom output dir (default: briefings/)")

    db = sub.add_parser("dashboard",
                         help="Генерира HTML dashboard (docs/index.html) + state.json")
    db.add_argument("--heatmap-weeks", type=int, default=13,
                    help="Седмици за z-score heatmap (default 13)")
    db.add_argument("--skip-state-json", action="store_true",
                    help="Не пиши docs/state.json (само HTML)")

    bt = sub.add_parser("backtest", help="Backtest на исторически hypothesis")
    bt.add_argument("--query", help="Name на canonical query от config/backtest_queries.yaml")
    bt.add_argument("--condition", action="append",
                    help="Ad-hoc condition: SYMBOL:metric>=value (повторете за повече)")
    bt.add_argument("--list", action="store_true", help="Покажи canonical queries")
    bt.add_argument("--episodes", type=int, default=10,
                    help="Покажи първите N episode-а (default 10)")
    bt.add_argument("--markdown", action="store_true",
                    help="Запиши пълен markdown report в briefings/backtests/")

    args = p.parse_args(argv)
    handlers = {
        "collect": cmd_collect,
        "backfill": cmd_backfill,
        "backfill-yf": cmd_backfill_yf,
        "delta": cmd_delta,
        "verify": cmd_verify,
        "journal-backfill": cmd_journal_backfill,
        "journal-prep": cmd_journal_prep,
        "journal-judge": cmd_journal_judge,
        "journal-calibrate": cmd_journal_calibrate,
        "briefing": cmd_briefing,
        "anomalies": cmd_anomalies,
        "parallels": cmd_parallels,
        "narrative": cmd_narrative,
        "backtest": cmd_backtest,
        "dashboard": cmd_dashboard,
        "export-week": cmd_export_week,
    }
    return handlers[args.cmd](args)


def main_module() -> None:
    sys.exit(main())


if __name__ == "__main__":
    main_module()
