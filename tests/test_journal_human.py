"""Тестове за човешката половина на gap-журнала (Phase 6, Тухла 2b).

Покрива verify gate-овете от handoff-а:
  • Стъпка 5: валидна присъда пише; БЕЗ критерий → raise (C3); VRM C6 (corruption raise,
    freshness, non-blocking absence).
  • Стъпка 6: присъда от T се разрешава на T+Y коректно (judgment_date котва, нула
    look-ahead); изход vs залог (direction_hit / axis_hit); PENDING когато Y не е настъпил.
  • Стъпка 7: малък n → 'недостатъчно', не % от n=1; брои ЕПИЗОДИ; n експлицитен.
  • Worksheet round-trip (parse запълнен блок; пропуска празен темплейт).
"""
from __future__ import annotations

from datetime import date, timedelta

import duckdb
import pandas as pd
import pytest

from macro_satellite.analytics.journal import (
    calibration,
    human_store,
    orchestrator,
    resolution,
    store,
    worksheet,
)
from macro_satellite.analytics.journal.human_store import (
    HumanJudgment,
    JournalDisciplineError,
    validate_judgment,
)
from macro_satellite.analytics.journal.resolution import (
    _axis_hit,
    _direction_hit,
    resolve_judgment,
    series_sigmas,
)
from macro_satellite.analytics.journal.vrm_snapshot import (
    VrmCorruptionError,
    VrmSnapshot,
    read_vrm_snapshot,
)
from macro_satellite.analytics.weekly_window import iso_week_for

# ── Helpers ───────────────────────────────────────────────────────────────────

def _mk_judgment(**over) -> HumanJudgment:
    base = dict(
        judgment_id="hj_test", gap_episode_id="ep030_2026-W16", region="US",
        author="Цветослав", judgment_date=date(2026, 6, 3),
        as_of_gap=0.5, as_of_economy_axis=0.05, as_of_markets_axis=0.55,
        config_key="gap_pos", claim_direction="close", claim_axis="market_leads",
        horizon_y_human=8, falsification_criterion="gap още > +0.5 на 8w",
        confidence="med", rationale=None,
        vrm_available=True, vrm_regime="REFLATION", vrm_signal="x", vrm_ks_active=False,
        vrm_alignment=7.0, vrm_last_updated=date(2026, 5, 24), vrm_age_days=10, vrm_stale=False,
    )
    base.update(over)
    return HumanJudgment(**base)


def _gap_series(pairs: list[tuple[float, float]], start: date = date(2026, 1, 5)) -> pd.DataFrame:
    """pairs = [(economy, markets), ...] → подредена седмична gap_series (понеделник start)."""
    recs = []
    for i, (e, m) in enumerate(pairs):
        wk = iso_week_for(start + timedelta(days=7 * i))
        recs.append({"week": wk.label, "week_end": wk.week_end,
                     "economy_axis": e, "markets_axis": m, "gap": m - e})
    return pd.DataFrame(recs)


def _vrm_duck(rows: list[dict]) -> duckdb.DuckDBPyConnection:
    """Мини `vrm` таблица (живата серия, мандат №36) за C6 четеца."""
    con = duckdb.connect()
    con.register("_df", pd.DataFrame(rows))
    con.execute("CREATE TABLE vrm AS SELECT * FROM _df")
    con.unregister("_df")
    return con


# ── Стъпка 5: C3 validation gate ──────────────────────────────────────────────

def test_validate_ok():
    validate_judgment(_mk_judgment())   # не raise-ва


def test_validate_raises_missing_criterion():
    with pytest.raises(JournalDisciplineError):
        validate_judgment(_mk_judgment(falsification_criterion="   "))


def test_validate_raises_close_without_leg():
    with pytest.raises(JournalDisciplineError):
        validate_judgment(_mk_judgment(claim_direction="close", claim_axis=None))


def test_validate_raises_widen_with_leg():
    with pytest.raises(JournalDisciplineError):
        validate_judgment(_mk_judgment(claim_direction="widen", claim_axis="market_leads"))


def test_validate_widen_ok_without_leg():
    validate_judgment(_mk_judgment(claim_direction="widen", claim_axis=None))


def test_validate_raises_bad_horizon():
    with pytest.raises(JournalDisciplineError):
        validate_judgment(_mk_judgment(horizon_y_human=6))


# ── Стъпка 5: VRM C6 hibrid четец ─────────────────────────────────────────────

def test_vrm_corruption_null_regime_raises():
    con = _vrm_duck([{"date": date(2026, 5, 18), "as_of": date(2026, 5, 18),
                      "regime": None, "ks_active": False, "alignment_score": 7.0}])
    with pytest.raises(VrmCorruptionError):
        read_vrm_snapshot(date(2026, 6, 3), duck=con)


def test_vrm_unknown_regime_raises():
    con = _vrm_duck([{"date": date(2026, 5, 18), "as_of": date(2026, 5, 18),
                      "regime": "WHATEVER", "ks_active": False, "alignment_score": 7.0}])
    with pytest.raises(VrmCorruptionError):
        read_vrm_snapshot(date(2026, 6, 3), duck=con)


def test_vrm_valid_freshness():
    con = _vrm_duck([{"date": date(2026, 5, 24), "as_of": date(2026, 5, 24),
                      "regime": "REFLATION", "ks_active": False, "alignment_score": 7.0}])
    s = read_vrm_snapshot(date(2026, 6, 3), duck=con)
    assert s.available and s.regime == "REFLATION"
    assert s.age_days == 10 and not s.stale and s.source == "vrm"
    # Живата серия не носи signal → None честно (мандат №36).
    assert s.signal is None
    assert s.alignment == 7.0 and s.ks_active is False


def test_vrm_stale_flag():
    con = _vrm_duck([{"date": date(2026, 4, 1), "as_of": date(2026, 4, 1),
                      "regime": "REFLATION", "ks_active": True, "alignment_score": 6.0}])
    s = read_vrm_snapshot(date(2026, 6, 3), duck=con)
    assert s.available and s.stale   # > 14 дни


def test_vrm_absent_nonblocking():
    con = duckdb.connect()
    con.execute("CREATE TABLE vrm(date DATE, regime VARCHAR)")  # празна
    s = read_vrm_snapshot(date(2026, 6, 3), duck=con)
    assert not s.available and s.regime is None


def test_vrm_ks_none_stays_none():
    # Мозъкът emit-ва ks_active=None при неизвестно → снимката пази None,
    # не фабрикува False (мандат №36 гейт: None ≠ inactive).
    con = _vrm_duck([{"date": date(2026, 5, 24), "as_of": date(2026, 5, 24),
                      "regime": "REFLATION", "ks_active": None, "alignment_score": 6.0}])
    s = read_vrm_snapshot(date(2026, 6, 3), duck=con)
    assert s.available and s.ks_active is None


# ── Стъпка 6: resolution (judgment_date котва, нула look-ahead) ────────────────

def test_resolve_market_leads():
    # gap_pos на T (+0.8), затваря защото ПАЗАРИ падат до +Y; икон флат → market_leads.
    gs = _gap_series([(0.0, 0.80), (0.0, 0.70), (0.0, 0.55), (0.0, 0.40),
                      (0.0, 0.30), (0.0, 0.20), (0.0, 0.15), (0.0, 0.12), (0.0, 0.10)])
    se, sm = series_sigmas(gs)
    jd = gs.iloc[0]["week_end"]   # дата в week0
    j = _mk_judgment(judgment_date=jd, horizon_y_human=8,
                     claim_direction="close", claim_axis="market_leads")
    r = resolve_judgment(j, gs, se, sm)
    assert r is not None
    assert r.machine_outcome == "market_leads"
    assert r.direction_hit and r.axis_hit


def test_resolve_pending_when_horizon_not_reached():
    gs = _gap_series([(0.0, 0.80), (0.0, 0.70), (0.0, 0.55)])  # само 3 седмици
    se, sm = series_sigmas(gs)
    jd = gs.iloc[0]["week_end"]
    j = _mk_judgment(judgment_date=jd, horizon_y_human=8)
    assert resolve_judgment(j, gs, se, sm) is None   # T+8 не съществува → PENDING


def test_resolve_widen():
    # gap_pos на T (+0.4), РАЗШИРЯВА се (+0.9 на Y) → widen; залог widen → direction_hit.
    gs = _gap_series([(0.0, 0.40), (0.0, 0.55), (0.0, 0.70), (0.0, 0.80), (0.0, 0.90)])
    se, sm = series_sigmas(gs)
    jd = gs.iloc[0]["week_end"]
    j = _mk_judgment(judgment_date=jd, horizon_y_human=4,
                     claim_direction="widen", claim_axis=None)
    r = resolve_judgment(j, gs, se, sm)
    assert r.machine_outcome == "widen"
    assert r.direction_hit and r.axis_hit is None


def test_direction_and_axis_hit_logic():
    assert _direction_hit("close", "market_leads") is True
    assert _direction_hit("close", "widen") is False
    assert _direction_hit("widen", "widen") is True
    assert _direction_hit("widen", "meet") is False
    assert _axis_hit("close", "market_leads", "market_leads") is True
    assert _axis_hit("close", "economy_leads", "market_leads") is False
    assert _axis_hit("close", "market_leads", "widen") is None   # машината се разшири
    assert _axis_hit("widen", None, "widen") is None


# ── Worksheet round-trip ──────────────────────────────────────────────────────

def test_worksheet_parse_filled_block():
    txt = (
        "**Регион:** US\n"
        "**Дата на присъдата (T):** 2026-06-03\n"
        "**Автор:** Цветослав\n"
        "```\n"
        "ПРИСЪДА_ЗА_ЕПИЗОД:        ep030_2026-W16\n"
        "ПОСОКА:                   close\n"
        "ЗАТВАРЯЩА_ОС:             market_leads\n"
        "ХОРИЗОНТ_СЕДМИЦИ:         8\n"
        "КРИТЕРИЙ_ЗА_ОПРОВЕРЖЕНИЕ: ако gap > +0.5 на 8w\n"
        "УВЕРЕНОСТ:                med\n"
        "ОБОСНОВКА:                институционален bid\n"
        "```\n"
    )
    region, jd, author, blocks = worksheet.parse_worksheet(txt)
    assert region == "US" and jd == date(2026, 6, 3) and author == "Цветослав"
    assert len(blocks) == 1
    b = blocks[0]
    assert b.gap_episode_id == "ep030_2026-W16"
    assert b.claim_direction == "close" and b.claim_axis == "market_leads"
    assert b.horizon_y_human == 8 and b.confidence == "med"
    assert "gap" in b.falsification_criterion


def test_worksheet_skips_empty_template():
    vrm = VrmSnapshot(available=False, regime=None, signal=None, ks_active=None,
                      alignment=None, last_updated=None, age_days=None, stale=None, source=None)
    text = worksheet.generate_worksheet(
        "US", date(2026, 6, 3), "Цветослав",
        [{"gap_episode_id": "ep030_2026-W16", "config_key": "gap_pos",
          "open_date": "2026-04-19", "peak_gap": 0.796, "age_weeks": 7}],
        {"week": "2026-W23", "week_end": "2026-06-07", "gap": 0.56,
         "economy_axis": 0.05, "markets_axis": 0.61},
        vrm, [])
    _, _, _, blocks = worksheet.parse_worksheet(text)
    assert blocks == []   # незапълненият темплейт се пропуска


# ── Стъпки 5–7 end-to-end (изолиран JOURNAL_DIR) ──────────────────────────────

@pytest.fixture
def iso_journal(tmp_path, monkeypatch):
    jd = tmp_path / "journal"
    jd.mkdir()
    for mod in (human_store, resolution, store, orchestrator):
        monkeypatch.setattr(mod, "JOURNAL_DIR", jd, raising=False)
    return jd


def _stub_vrm(*_a, **_k):
    return VrmSnapshot(available=True, regime="REFLATION", signal=None, ks_active=False,
                       alignment=7.0, last_updated=date(2026, 5, 24), age_days=10,
                       stale=False, source="vrm")


def test_ingest_writes_and_resolves(iso_journal, monkeypatch):
    # Синтетичен gap_series (market_leads close на 8w) + machine_episodes config map.
    gs = _gap_series([(0.0, 0.80), (0.0, 0.70), (0.0, 0.55), (0.0, 0.40),
                      (0.0, 0.30), (0.0, 0.20), (0.0, 0.15), (0.0, 0.12), (0.0, 0.10)])
    store.write_gap_series(gs.copy(), "US")
    monkeypatch.setattr(orchestrator, "read_machine_episodes",
                        lambda region: pd.DataFrame([{"gap_episode_id": "epT", "config_key": "gap_pos"}]))
    monkeypatch.setattr(orchestrator, "read_vrm_snapshot", _stub_vrm)

    jd = gs.iloc[0]["week_end"]   # week0 → T+8 е в серията → ще се разреши веднага
    (iso_journal / worksheet.WORKSHEET_FILE).write_text(
        f"**Регион:** US\n**Дата на присъдата (T):** {jd.isoformat()}\n**Автор:** Цветослав\n"
        "```\n"
        "ПРИСЪДА_ЗА_ЕПИЗОД:        epT\n"
        "ПОСОКА:                   close\n"
        "ЗАТВАРЯЩА_ОС:             market_leads\n"
        "ХОРИЗОНТ_СЕДМИЦИ:         8\n"
        "КРИТЕРИЙ_ЗА_ОПРОВЕРЖЕНИЕ: gap още > +0.5 на 8w\n"
        "```\n", encoding="utf-8")

    summary = orchestrator.ingest("US")
    assert summary.appended == 1
    assert summary.resolved == 1                       # T+8 наличен → разрешен веднага
    judgments = human_store.read_judgments()
    assert len(judgments) == 1 and judgments[0].gap_episode_id == "epT"
    resolutions = human_store.read_resolutions()
    assert len(resolutions) == 1 and resolutions[0].machine_outcome == "market_leads"
    assert resolutions[0].direction_hit and resolutions[0].axis_hit

    # Idempotent re-ingest → нула нови (append-only integrity).
    summary2 = orchestrator.ingest("US")
    assert summary2.appended == 0 and summary2.resolved == 0


def test_ingest_raises_on_missing_criterion(iso_journal, monkeypatch):
    gs = _gap_series([(0.0, 0.80), (0.0, 0.70)])
    store.write_gap_series(gs.copy(), "US")
    monkeypatch.setattr(orchestrator, "read_machine_episodes",
                        lambda region: pd.DataFrame([{"gap_episode_id": "epT", "config_key": "gap_pos"}]))
    monkeypatch.setattr(orchestrator, "read_vrm_snapshot", _stub_vrm)
    jd = gs.iloc[0]["week_end"]
    (iso_journal / worksheet.WORKSHEET_FILE).write_text(
        f"**Регион:** US\n**Дата на присъдата (T):** {jd.isoformat()}\n**Автор:** Цветослав\n"
        "```\n"
        "ПРИСЪДА_ЗА_ЕПИЗОД:        epT\n"
        "ПОСОКА:                   close\n"
        "ЗАТВАРЯЩА_ОС:             market_leads\n"
        "ХОРИЗОНТ_СЕДМИЦИ:         8\n"
        "КРИТЕРИЙ_ЗА_ОПРОВЕРЖЕНИЕ:\n"      # ПРАЗЕН критерий → C3 raise
        "```\n", encoding="utf-8")
    with pytest.raises(JournalDisciplineError):
        orchestrator.ingest("US")


# ── Стъпка 7: калибрация n-дисциплина ─────────────────────────────────────────

def test_calibration_small_n_says_insufficient(iso_journal, monkeypatch):
    # Един разрешен епизод → под MIN_EPISODES → 'недостатъчно', не процент.
    monkeypatch.setattr(calibration, "read_machine_episodes", lambda region: pd.DataFrame())
    j = _mk_judgment(judgment_id="hj_epT_2026-06-07_8w", gap_episode_id="epT")
    human_store.append_judgment(j)
    r = human_store.HumanResolution(
        resolution_id="hr_hj_epT_2026-06-07_8w", judgment_id=j.judgment_id,
        gap_episode_id="epT", region="US", horizon_y=8, judgment_date=j.judgment_date,
        resolved_week="2026-W31", resolved_date=date(2026, 8, 2), as_of_gap=0.5, y_gap=0.1,
        d_economy=0.0, d_markets=-0.4, machine_outcome="market_leads",
        machine_m_share=0.9, machine_e_share=0.1, human_claim_direction="close",
        human_claim_axis="market_leads", direction_hit=True, axis_hit=True)
    human_store.append_resolution(r)

    report = calibration.format_calibration("US")
    assert "недостатъчно" in report.lower()
    # n трябва да е експлицитен (n_episodes=1), не скрит зад процент.
    assert "n_episodes=1" in report
