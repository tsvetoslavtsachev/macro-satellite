"""Журнал оркестратор (Тухла 2b, Възел 5) — prep + ingest ритуалните фази.

Тънък слой над worksheet + human_store + resolution + vrm_snapshot. CLI командите
(journal-prep / journal-judge) са обвивки около `prep()` и `ingest()`.

Дисциплината е в РИТУАЛА (DESIGN решение 4): човек пуска prep → попълва worksheet →
пуска judge. Нула cron-write на присъди. journal-judge ГРЪМВА при липсващ критерий (C3).
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta

import pandas as pd

from ...paths import JOURNAL_DIR
from ..weekly_window import iso_week_for
from . import worksheet as ws
from .human_store import (
    HumanJudgment,
    append_judgment,
    make_judgment_id,
    read_judgments,
    resolved_judgment_ids,
)
from .resolution import load_gap_series, resolve_pending
from .store import read_machine_episodes
from .vrm_snapshot import read_vrm_snapshot


@dataclass
class IngestSummary:
    appended: int
    skipped: int           # дубликати (вече в store)
    resolved: int          # новоразрешени този run
    appended_ids: list
    resolved_ids: list


def _latest_gap_row(gap_series: pd.DataFrame) -> dict | None:
    if gap_series.empty:
        return None
    r = gap_series.iloc[-1]
    we = r["week_end"]
    we = we.date() if hasattr(we, "date") else we
    return {"week": str(r["week"]), "week_end": we.isoformat(),
            "gap": float(r["gap"]), "economy_axis": float(r["economy_axis"]),
            "markets_axis": float(r["markets_axis"])}


def _row_at_or_before(gap_series: pd.DataFrame, d: date):
    """Редът за седмицата на `d`, иначе последният с week_end ≤ d (за as_of котвата)."""
    label = iso_week_for(d).label
    hit = gap_series[gap_series["week"] == label]
    if not hit.empty:
        return hit.iloc[0]
    prior = gap_series[gap_series["week_end"].apply(
        lambda x: (x.date() if hasattr(x, "date") else x) <= d)]
    return prior.iloc[-1] if not prior.empty else None


def _open_episodes(region: str, gap_series: pd.DataFrame) -> list[dict]:
    me = read_machine_episodes(region)
    if me.empty:
        return []
    cens = me[me["censored"] == True]  # noqa: E712
    latest_we = None
    if not gap_series.empty:
        latest_we = gap_series.iloc[-1]["week_end"]
        latest_we = latest_we.date() if hasattr(latest_we, "date") else latest_we
    out: list[dict] = []
    seen: set = set()
    for _, r in cens.iterrows():
        eid = r["gap_episode_id"]
        if eid in seen:
            continue
        seen.add(eid)
        od = r["open_date"]
        od = od.date() if hasattr(od, "date") else od
        age_weeks = ((latest_we - od).days // 7) if latest_we else None
        out.append({
            "gap_episode_id": eid,
            "config_key": r["config_key"],
            "open_date": od.isoformat(),
            "peak_gap": float(r["peak_gap"]),
            "age_weeks": age_weeks,
        })
    return out


def _pending_due(region: str, gap_series: pd.DataFrame) -> list[dict]:
    """Неразрешени присъди, чийто хоризонт (T+Y седмица) вече е в серията."""
    if gap_series.empty:
        return []
    latest_we = gap_series.iloc[-1]["week_end"]
    latest_we = latest_we.date() if hasattr(latest_we, "date") else latest_we
    already = resolved_judgment_ids()
    due: list[dict] = []
    for j in read_judgments():
        if j.region.upper() != region.upper() or j.judgment_id in already:
            continue
        t_week = iso_week_for(j.judgment_date)
        y_week = iso_week_for(t_week.week_start + timedelta(days=7 * j.horizon_y_human))
        if y_week.week_end <= latest_we:
            due.append({"judgment_id": j.judgment_id, "gap_episode_id": j.gap_episode_id,
                        "horizon_y": j.horizon_y_human, "due_week": y_week.label})
    return due


def prep(region: str, author: str, judgment_date: date) -> str:
    """Фаза 1 — генерира pre-filled JOURNAL_WEEK.md. Връща пътя."""
    gap_series = load_gap_series(region)
    vrm = read_vrm_snapshot(judgment_date)
    open_eps = _open_episodes(region, gap_series)
    latest_gap = _latest_gap_row(gap_series)
    pending = _pending_due(region, gap_series)
    text = ws.generate_worksheet(region, judgment_date, author, open_eps,
                                 latest_gap, vrm, pending)
    JOURNAL_DIR.mkdir(parents=True, exist_ok=True)
    path = JOURNAL_DIR / ws.WORKSHEET_FILE
    path.write_text(text, encoding="utf-8")
    return str(path)


def ingest(default_region: str = "US") -> IngestSummary:
    """Фаза 3 — парсва JOURNAL_WEEK.md → валидира (C3 raise) → append → разрешава дължимите."""
    path = JOURNAL_DIR / ws.WORKSHEET_FILE
    if not path.exists():
        raise FileNotFoundError(
            f"{path} липсва — пусни 'journal-prep' първо за да генерираш worksheet."
        )
    text = path.read_text(encoding="utf-8")
    region, judgment_date, author, blocks = ws.parse_worksheet(text)
    region = (region or default_region).upper()
    if judgment_date is None:
        raise ValueError("JOURNAL_WEEK.md: липсва 'Дата на присъдата (T)' — не мога да котвирам.")
    if not author:
        raise ValueError("JOURNAL_WEEK.md: липсва 'Автор'.")

    gap_series = load_gap_series(region)
    me = read_machine_episodes(region)
    config_by_ep = (dict(zip(me["gap_episode_id"], me["config_key"], strict=False))
                    if not me.empty else {})

    appended_ids: list = []
    skipped = 0
    for b in blocks:
        as_of_row = _row_at_or_before(gap_series, judgment_date) if not gap_series.empty else None
        if as_of_row is None:
            raise ValueError(
                f"{b.gap_episode_id}: няма gap_series ред за/преди {judgment_date} — "
                f"не мога да котвирам as_of снимката."
            )
        config_key = config_by_ep.get(b.gap_episode_id)
        if config_key is None:
            raise ValueError(
                f"присъда за '{b.gap_episode_id}', но такъв епизод липсва в "
                f"machine_episodes[{region}] — пусни journal-backfill или провери id-то."
            )
        vrm = read_vrm_snapshot(judgment_date)
        horizon = b.horizon_y_human if b.horizon_y_human is not None else -1
        j = HumanJudgment(
            judgment_id=make_judgment_id(b.gap_episode_id, judgment_date, horizon),
            gap_episode_id=b.gap_episode_id,
            region=region,
            author=author,
            judgment_date=judgment_date,
            as_of_gap=float(as_of_row["gap"]),
            as_of_economy_axis=float(as_of_row["economy_axis"]),
            as_of_markets_axis=float(as_of_row["markets_axis"]),
            config_key=config_key,
            claim_direction=b.claim_direction,
            claim_axis=b.claim_axis,
            horizon_y_human=horizon,
            falsification_criterion=b.falsification_criterion or "",
            confidence=b.confidence,
            rationale=b.rationale,
            vrm_available=vrm.available,
            vrm_regime=vrm.regime,
            vrm_signal=vrm.signal,
            vrm_ks_active=vrm.ks_active,
            vrm_alignment=vrm.alignment,
            vrm_last_updated=vrm.last_updated,
            vrm_age_days=vrm.age_days,
            vrm_stale=vrm.stale,
        )
        if append_judgment(j):       # validate_judgment вътре → C3 raise при липсващ критерий
            appended_ids.append(j.judgment_id)
        else:
            skipped += 1

    newly = resolve_pending(region)
    return IngestSummary(
        appended=len(appended_ids), skipped=skipped, resolved=len(newly),
        appended_ids=appended_ids, resolved_ids=[r.resolution_id for r in newly],
    )
