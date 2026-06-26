#!/usr/bin/env python3
"""CI guard (INIT-22 P6 part 2): fail RED if any archive-covered ETF silently fell back to yfinance.

macro-satellite sources its daily ETF bars FROM the canonical price-archive via the shared reader
``collectors/price/consumer.py`` (base-first, CLOSED yfinance fallback). A silent fallback would
quietly republish ``price_delta`` / ``organism.json`` / the weekly narrative off un-audited fetch
data instead of canon.

This guard makes that LOUD. It anchors on the EXPECTED-BASE universe computed INDEPENDENTLY of the
produced payload (mirroring the A1 manifest anchor + the P6 GC-1 fix -- NEVER trust the shrinkable
produced file): ``etf_universe.yaml`` INTERSECT the price-archive universe (collectors config).
Every symbol in that intersection must be present in ``data/price_source.json`` with
``source == "base"``. The 5 satellite-only symbols outside the archive (DFEN/EFA/VEA/IBIT/ASHR) are
NOT in the intersection -> legitimately fetch, not checked. Computing the intersection (not a
hardcoded allow-list) means a future archive expansion auto-tightens the guard.

Gated on the read PAT in CI; with the secret absent the whole-universe yfinance fallback is
legitimate and this is skipped. Mirrors _etf_remote/scripts/assert_base_sourced.py (ETF-rr) and
dashboards/cot-monitor/scripts/assert_base_sourced.py (A1).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / "data" / "price_source.json"
sys.path.insert(0, str(REPO / "src"))  # so the macro_satellite package imports for the anchor

# Cross-repo shrink tripwire. The expected-base universe is etf_universe.yaml INTERSECT the
# price-archive universe (collectors/price/config.yaml -- a DIFFERENT repo). A cross-repo archive
# shrink or a stale/empty `.collectors` checkout (daily-collect.yml uses fetch-depth:1) would shrink
# `expected` ITSELF, so covered symbols silently revert to un-audited yfinance while CI stays green --
# the exact failure this guard exists to prevent, just triggered from the archive side (a vector the
# GC-1 "never anchor on the produced payload" rule does not cover). 42 are covered today (47 satellite
# - 5 archive-gaps); a floor of 40 trips a catastrophic cross-repo shrink without being brittle to a
# single legitimate satellite-universe edit. Raise it if the covered count is deliberately grown.
EXPECTED_BASE_FLOOR = 40


def _expected_base() -> list[str]:
    """The independent anchor: etf_universe.yaml INTERSECT the price-archive universe.

    Both sides come straight from the authoritative configs (NOT the produced price_source.json),
    so a silent universe-shrink cannot pass green."""
    from macro_satellite.config import load_etf_universe
    from collectors.price.consumer import symbol_to_series  # collectors on PYTHONPATH in CI
    universe = [str(s).strip().upper() for s in load_etf_universe().symbols]
    archive = symbol_to_series()  # {TICKER(upper) -> px_<key>_daily}
    return sorted(s for s in universe if s in archive)


def main() -> int:
    if not SOURCE.exists():
        print(f"assert_base_sourced: {SOURCE} missing -- the base-first ingest must run first",
              file=sys.stderr)
        return 1
    payload = json.loads(SOURCE.read_text(encoding="utf-8"))
    by_symbol = {str(k).upper(): v for k, v in payload.get("by_symbol", {}).items()}

    try:
        expected = _expected_base()
    except ImportError as e:
        print("assert_base_sourced: cannot import the expected-base anchor "
              f"(macro_satellite.config + collectors.price.consumer): {e}", file=sys.stderr)
        return 1
    if not expected:
        print("assert_base_sourced: empty expected-base universe -- configs broken or collectors "
              "not on PYTHONPATH", file=sys.stderr)
        return 1
    if len(expected) < EXPECTED_BASE_FLOOR:
        print(f"assert_base_sourced: expected-base universe shrank to {len(expected)} "
              f"(< floor {EXPECTED_BASE_FLOOR}) -- a cross-repo archive shrink or a stale .collectors "
              "checkout silently loosened the anchor; refusing to pass green.", file=sys.stderr)
        return 1

    offenders = []
    for t in expected:
        src = by_symbol.get(t)
        if src is None:
            offenders.append(f"{t} (MISSING from price_source -- dropped/dead; universe shrank)")
        elif src != "base":
            offenders.append(f"{t} (source={src!r})")

    total = len(expected)
    if offenders:
        print(f"FAIL: {len(offenders)}/{total} archive-covered ETFs did NOT source from the "
              "price-archive base (the read PAT is set, so base sourcing was expected):",
              file=sys.stderr)
        for o in offenders:
            print(f"  - {o}", file=sys.stderr)
        print("The strangler silently reverted to the yfinance fallback (un-audited fetch) or the "
              "published universe shrank. Check the data-core/price-archive checkout + PYTHONPATH "
              "+ DATACORE_ROOT, and any per-symbol archive gap (config.yaml daily-window limit).",
              file=sys.stderr)
        return 1

    print(f"OK: all {total} archive-covered ETFs sourced from the price-archive base (source=base).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
