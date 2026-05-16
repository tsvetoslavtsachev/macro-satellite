from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

# Force UTF-8 (D11) — Windows CP1252 console иначе чупи всичко с кирилица
os.environ.setdefault("PYTHONUTF8", "1")
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def fixtures_dir() -> Path:
    return FIXTURES


@pytest.fixture
def isolated_storage(tmp_path, monkeypatch):
    """Изолира MACRO_SATELLITE_ROOT в tmp_path. Reimports paths to apply."""
    monkeypatch.setenv("MACRO_SATELLITE_ROOT", str(tmp_path))
    # Force reload на paths модула за да pick-не env var-а
    import importlib

    from macro_satellite import paths
    importlib.reload(paths)
    # Reload upstream modules, които cache-нат paths constants
    from macro_satellite.storage import duckdb_conn, parquet_writer, raw_archive
    for mod in (parquet_writer, raw_archive, duckdb_conn):
        importlib.reload(mod)
    paths.ensure_dirs()
    return tmp_path
