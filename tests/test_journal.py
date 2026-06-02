"""Тестове за gap-журнала (Phase 6, Тухла 2a) — чиста логика без cross-repo bridge.

Покрива: attribution.classify (4-те изхода + vol-нормализация), detect_episodes
(праг, хистерезис, клъстериране, censored, config_key), axis_sigma.
"""
from __future__ import annotations

from datetime import date, timedelta

from macro_satellite.analytics.journal.attribution import axis_sigma, classify
from macro_satellite.analytics.journal.episodes import detect_episodes
from macro_satellite.analytics.weekly_window import iso_week_for


def _weeks(n: int, start: date = date(2021, 1, 4)):
    return [iso_week_for(start + timedelta(days=7 * i)) for i in range(n)]


# ── classify: 4-те изхода ─────────────────────────────────────────────────────

def test_classify_market_leads():
    # положителен gap се затваря защото ПАЗАРИ-оста пада (ΔM<0), икономика флат
    oc, m_share, e_share = classify(gap_open=1.0, gap_y=0.2,
                                    d_markets=-0.8, d_economy=0.0,
                                    sigma_m=1.0, sigma_e=1.0)
    assert oc == "market_leads"
    assert m_share > e_share


def test_classify_economy_leads():
    # положителен gap се затваря защото ИКОНОМИКА-оста се качва (ΔE>0), пазари флат
    oc, m_share, e_share = classify(gap_open=1.0, gap_y=0.2,
                                    d_markets=0.0, d_economy=0.8,
                                    sigma_m=1.0, sigma_e=1.0)
    assert oc == "economy_leads"
    assert e_share > m_share


def test_classify_meet():
    # двата крака допринасят съизмеримо
    oc, m_share, e_share = classify(gap_open=1.0, gap_y=0.2,
                                    d_markets=-0.4, d_economy=0.4,
                                    sigma_m=1.0, sigma_e=1.0)
    assert oc == "meet"
    assert abs(m_share - e_share) < 1e-9


def test_classify_widen():
    # |gap| се разшири → присъдата (за затваряне) сгреши
    oc, m_share, e_share = classify(gap_open=0.5, gap_y=0.9,
                                    d_markets=0.4, d_economy=0.0,
                                    sigma_m=1.0, sigma_e=1.0)
    assert oc == "widen"
    assert m_share is None and e_share is None


def test_classify_negative_gap_market_leads():
    # отрицателен gap (пазари по-risk-off): затваря се когато пазари-оста се КАЧВА (ΔM>0)
    oc, m_share, e_share = classify(gap_open=-1.0, gap_y=-0.2,
                                    d_markets=0.8, d_economy=0.0,
                                    sigma_m=1.0, sigma_e=1.0)
    assert oc == "market_leads"


def test_classify_vol_normalization_tilts_to_low_sigma_leg():
    # еднакви сурови Δ, но икономиката е по-малко волатилна (σ_e<σ_m) → икономиката
    # получава по-голям vol-норм. дял (реален принос в собствени σ-единици).
    oc, m_share, e_share = classify(gap_open=1.0, gap_y=0.0,
                                    d_markets=-0.5, d_economy=0.5,
                                    sigma_m=1.0, sigma_e=0.5)
    assert e_share > m_share
    assert oc in ("economy_leads", "meet")


def test_classify_wrong_way_leg_gets_no_credit():
    # gap се свива; икономиката се движи ПРОТИВ затварянето → 0 кредит, пазари водят
    oc, m_share, e_share = classify(gap_open=1.0, gap_y=0.1,
                                    d_markets=-1.0, d_economy=-0.1,
                                    sigma_m=1.0, sigma_e=1.0)
    assert oc == "market_leads"
    assert e_share == 0.0


# ── detect_episodes ───────────────────────────────────────────────────────────

def test_detect_single_episode_and_clustering():
    gaps = [0.0, 0.0, 0.3, 0.4, 0.5, 0.3, 0.05, 0.0, 0.0]
    wks = _weeks(len(gaps))
    eps, meta = detect_episodes(wks, gaps, sigma=0.2)  # τ_open=0.2, τ_close=0.1
    assert meta["tau_open"] == 0.2 and meta["tau_close"] == 0.1
    # клъстерираните седмици 2..5 = ЕДИН епизод (не 4)
    assert len(eps) == 1
    ep = eps[0]
    assert ep.open_index == 2
    assert ep.close_index == 6          # първата седмица |gap|<τ_close (0.05)
    assert ep.config_key == "gap_pos"
    assert not ep.censored
    assert abs(ep.peak_gap - 0.5) < 1e-9


def test_detect_two_episodes_with_sign_flip():
    gaps = [0.0, 0.3, 0.4, 0.05, 0.0, -0.3, -0.4, -0.05, 0.0]
    wks = _weeks(len(gaps))
    eps, _ = detect_episodes(wks, gaps, sigma=0.2)
    assert len(eps) == 2
    assert eps[0].config_key == "gap_pos"
    assert eps[1].config_key == "gap_neg"
    assert eps[0].close_index is not None and eps[1].close_index is not None


def test_detect_censored_episode():
    gaps = [0.0, 0.0, 0.3, 0.4, 0.5]   # отваря и не затваря до края
    wks = _weeks(len(gaps))
    eps, _ = detect_episodes(wks, gaps, sigma=0.2)
    assert len(eps) == 1
    assert eps[0].censored
    assert eps[0].close_index is None
    assert eps[0].close_date is None


def test_detect_below_threshold_no_episodes():
    gaps = [0.05, 0.1, 0.15, 0.05]
    wks = _weeks(len(gaps))
    eps, _ = detect_episodes(wks, gaps, sigma=0.2)
    assert eps == []


def test_axis_sigma_basic():
    # първи разлики на [0,1,2,3] = [1,1,1] → pstdev=0
    assert axis_sigma([0.0, 1.0, 2.0, 3.0]) == 0.0
    # с вариация в разликите → >0
    assert axis_sigma([0.0, 1.0, 0.0, 1.0]) > 0.0
    # None-ове чупят верига от разлики, не крашат
    assert axis_sigma([0.0, None, 2.0, 3.0]) >= 0.0
