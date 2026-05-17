"""Tests за visualization.dashboard — основен smoke + проверка на bug fixes."""
from __future__ import annotations

import pytest

from macro_satellite.visualization import dashboard as dash_mod


def test_short_window_is_4_weeks():
    """Bug #2 fix — default дашбордът показва ~4w, не 3y."""
    assert dash_mod.SHORT_WINDOW_DAYS == 28


def test_medium_window_is_13_weeks():
    assert dash_mod.MEDIUM_WINDOW_DAYS == 91


def test_price_chart_symbols_no_duplicates():
    assert len(dash_mod.PRICE_CHART_SYMBOLS) == len(set(dash_mod.PRICE_CHART_SYMBOLS))


def test_generate_dashboard_writes_html(tmp_path):
    """E2E smoke: generate_dashboard produces docs/index.html + state.json."""
    from macro_satellite.storage.duckdb_conn import get_duck
    duck = get_duck()
    try:
        n_rows = duck.execute("SELECT count(*) FROM etf_prices").fetchone()[0]
    except Exception:
        pytest.skip("etf_prices table missing — clean test environment")
    if n_rows == 0:
        pytest.skip("etf_prices table empty — no data to render")

    path = dash_mod.generate_dashboard(output_dir=tmp_path, heatmap_weeks=8)
    assert path.exists()
    assert path.name == "index.html"

    state_path = tmp_path / "state.json"
    assert state_path.exists(), "state.json sidecar трябва да се генерира с dashboard"

    html = path.read_text(encoding="utf-8")
    assert "<!DOCTYPE html>" in html
    # Hero блокът трябва да присъства
    assert "Тази седмица" in html
    # Не трябва да има суров <pre> от briefing (Bug #1)
    # Toлерираме <pre> в code blocks/Plotly internal само ако НЕ е briefing-excerpt
    assert "briefing-excerpt" not in html, "Стария <pre> escape подход не трябва да присъства"
    # state.json трябва да е линкнат
    assert "state.json" in html


def test_generate_dashboard_skip_state(tmp_path):
    """Verify --skip-state-json flag suppresses state.json writing."""
    from macro_satellite.storage.duckdb_conn import get_duck
    duck = get_duck()
    try:
        n_rows = duck.execute("SELECT count(*) FROM etf_prices").fetchone()[0]
    except Exception:
        pytest.skip("etf_prices table missing")
    if n_rows == 0:
        pytest.skip("etf_prices table empty")

    path = dash_mod.generate_dashboard(output_dir=tmp_path, heatmap_weeks=8,
                                        skip_state_export=True)
    assert path.exists()
    state_path = tmp_path / "state.json"
    assert not state_path.exists(), "state.json НЕ трябва да се пише при skip_state_export=True"
