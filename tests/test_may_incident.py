"""Acceptance test за 7-15 май 2026 инцидента.

Backfill-ва ETF за двете дати от GitHub history (integration test — изисква мрежа
и евентуално GITHUB_TOKEN за вдигнат rate limit). Проверява, че interval_change
за 7 ETF попада в ±1pp от очакваните стойности от handoff-а.

Защо това е acceptance test: ако този тест минава, цялата pipeline (backfill →
storage → delta → price formula) работи правилно. Той е истинският тест на
архитектурата.
"""
from __future__ import annotations

from datetime import date

import pytest

from macro_satellite.backfill.github_history import backfill_by_name
from macro_satellite.delta.price_delta import interval_change
from macro_satellite.storage.duckdb_conn import get_duck

# S17 Build A (2026-06-21): ETF github-history backfill е премахнат — etf_prices вече
# е yfinance-only, няма etf_dashboard github източник, така че backfill_by_name
# ("etf_dashboard") вече не резолвира. Acceptance-ът (price pipeline) ще се пре-домести
# върху yfinance backfill за двете дати — Build D задача. Дотогава: skip (този модул е
# integration, извън default gate; price формулата е покрита от test_delta_price).
pytestmark = pytest.mark.skip(
    reason="ETF github-history backfill severed in S17 Build A; re-home acceptance on "
           "yfinance — Build D"
)

EXPECTED = {
    "USO":  +0.098,
    "XLE":  +0.062,
    "DFEN": -0.080,
    "URA":  -0.110,
    "GLD":  -0.033,
    "TLT":  -0.023,
    "UUP":  +0.013,
}
TOLERANCE = 0.010


@pytest.fixture(scope="module")
def populated_storage(tmp_path_factory):
    storage = tmp_path_factory.mktemp("storage_root")
    import os
    os.environ["MACRO_SATELLITE_ROOT"] = str(storage)
    import importlib
    from macro_satellite import paths
    importlib.reload(paths)
    from macro_satellite.storage import duckdb_conn, parquet_writer, raw_archive
    for mod in (parquet_writer, raw_archive, duckdb_conn):
        importlib.reload(mod)
    paths.ensure_dirs()

    res = backfill_by_name(
        "etf_dashboard",
        only_dates=[date(2026, 5, 7), date(2026, 5, 15)],
    )
    assert res.dates_processed >= 1, f"backfill failed: {res.errors}"
    return get_duck()


@pytest.mark.integration
@pytest.mark.parametrize("symbol,expected", list(EXPECTED.items()))
def test_may_incident_interval_change(populated_storage, symbol, expected):
    r = interval_change(symbol, date(2026, 5, 7), date(2026, 5, 15), populated_storage)
    assert abs(r.interval_change - expected) <= TOLERANCE, (
        f"{symbol}: got {r.interval_change:+.4f}, expected {expected:+.4f} "
        f"±{TOLERANCE} (price_a={r.price_a}, price_b={r.price_b})"
    )
