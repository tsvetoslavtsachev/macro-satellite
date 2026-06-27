"""Tests за datacore-state колектора (collectors/vrm_overlay) — живия VRM мозък.

Доказват: (1) overlay tip → правилен 1-ред за `vrm` таблицата; (2) degrade-safe —
липсва env/файл/ядро → None (не падане, не гадаене); (3) S14 честност — застоял
overlay tip носи СТАРАТА as_of дата → max(date) ще го класифицира stale, не fresh.
"""
from __future__ import annotations

import json
from datetime import date

import pytest

from macro_satellite.collectors import vrm_overlay


def _write_overlay(tmp_path, records):
    state_dir = tmp_path / "state"
    state_dir.mkdir()
    (state_dir / "vrm_overlay.json").write_text(
        json.dumps(records), encoding="utf-8")
    return state_dir


FRESH_TIP = {
    "as_of": "2026-06-19",
    "regime": "REFLATION",
    "alignment_score": 6,
    "gms": {"score": 4, "max": 8, "tier": "MEDIUM"},
    "kill_switch": {"active": None, "variant": None, "applicable": True},
}


def test_collect_overlay_reads_tip(tmp_path, monkeypatch):
    state_dir = _write_overlay(tmp_path, [{"as_of": "2026-06-12", "regime": "GROWTH"},
                                          FRESH_TIP])
    monkeypatch.setenv("DATACORE_STATE_DIR", str(state_dir))

    df = vrm_overlay.collect_overlay()
    assert df is not None and len(df) == 1
    r = df.iloc[0]
    assert r["date"] == date(2026, 6, 19)          # tip (последния запис), не [0]
    assert r["as_of"] == date(2026, 6, 19)
    assert r["regime"] == "REFLATION"
    assert r["alignment_score"] == 6.0
    assert r["gms_score"] == 4.0
    assert r["gms_max"] == 8
    assert r["gms_tier"] == "MEDIUM"
    assert r["ks_active"] is None                    # мозъкът emit-ва None → None (не False)
    assert r["source"] == "vrm_live"


def test_collect_overlay_ks_active_true(tmp_path, monkeypatch):
    tip = {**FRESH_TIP, "kill_switch": {"active": True}}
    state_dir = _write_overlay(tmp_path, [tip])
    monkeypatch.setenv("DATACORE_STATE_DIR", str(state_dir))
    df = vrm_overlay.collect_overlay()
    assert df is not None and bool(df.iloc[0]["ks_active"]) is True


def test_collect_overlay_no_env_returns_none(monkeypatch):
    monkeypatch.delenv("DATACORE_STATE_DIR", raising=False)
    assert vrm_overlay.collect_overlay() is None


def test_collect_overlay_missing_file_returns_none(tmp_path, monkeypatch):
    monkeypatch.setenv("DATACORE_STATE_DIR", str(tmp_path / "nope"))
    assert vrm_overlay.collect_overlay() is None


def test_collect_overlay_missing_core_returns_none(tmp_path, monkeypatch):
    """Cardinal rule — липсва regime ядро → None, не гадаем формат."""
    state_dir = _write_overlay(tmp_path, [{"as_of": "2026-06-19"}])  # без regime
    monkeypatch.setenv("DATACORE_STATE_DIR", str(state_dir))
    assert vrm_overlay.collect_overlay() is None


def test_collect_overlay_stale_tip_keeps_old_date(tmp_path, monkeypatch):
    """S14 честност — застоял мозък → старата as_of минава ПРЕЗ колектора, не се
    подменя с „днес". max(date) после ще го класифицира stale, не fake-fresh."""
    stale_tip = {**FRESH_TIP, "as_of": "2026-01-05"}
    state_dir = _write_overlay(tmp_path, [stale_tip])
    monkeypatch.setenv("DATACORE_STATE_DIR", str(state_dir))
    df = vrm_overlay.collect_overlay()
    assert df is not None
    assert df.iloc[0]["date"] == date(2026, 1, 5)


def test_collect_overlay_bad_json_returns_none(tmp_path, monkeypatch):
    state_dir = tmp_path / "state"
    state_dir.mkdir()
    (state_dir / "vrm_overlay.json").write_text("{ not json", encoding="utf-8")
    monkeypatch.setenv("DATACORE_STATE_DIR", str(state_dir))
    assert vrm_overlay.collect_overlay() is None
