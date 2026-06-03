"""Калибрационно четене (Тухла 2b, стъпка 7) — machine base rate vs human track record.

⚠ КАЛИБРАЦИОННА ФИЛОСОФИЯ (КЛЮЧОВА — не я наивизирай):
Човекът НЕ се мери срещу машинния `market_leads %`. Това е ЛАРГЕЛИ МЕХАНИЧНО заради
velocity asymmetry (икон-оста е структурно бавна, M/E 4–7× US) — да „биеш" механична база
не е edge. Информативните оси, на които човекът ДОБАВЯ стойност:
  • close-vs-widen — позна ли, че gap-ът ще ПЕРСИСТИРА/расте (особено gap_neg widen ~57% @13w)?
  • economy_leads (рядко ~7%) — позна ли РЕДКИЯ случай, че пазарът предвиди макро-промяна?
  • pos/neg асиметрия + timing — кога да следваш vs fade-ваш.

⚠ n-ДИСЦИПЛИНА: брои ЕПИЗОДИ (distinct gap_episode_id), НЕ записи. n експлицитен ВИНАГИ.
   Малък n (< MIN_EPISODES) → „недостатъчно", НЕ процент от n=1 (фалшива увереност).

⚠ Machine base rate е look-ahead-biased prior (revision bias); human track е real-time
   (judgment_date котва). Различни прозорци → НЕ apples-to-apples: prior-vs-realtime,
   не глава-в-глава. Калибрирай per-регион — base rate-ите между региони НЕ са съизмерими
   (cross-region структурни артефакти, напр. CN gap_pos 22/26 е по СТРОЕЖ).
"""
from __future__ import annotations

from .backfill import POST_REFLATION_CUTOFF, _base_rates
from .human_store import read_judgments, read_resolutions
from .store import read_machine_episodes

# Под този праг ЕПИЗОДИ → „недостатъчно", не процент (n-дисциплина).
MIN_EPISODES = 3


def machine_base_rate(region: str = "US", post_reflation: bool = False) -> dict:
    """Machine base rate от machine_episodes[_<region>].parquet (не пре-смята backfill).

    Връща {config_key: {horizon: {counts, n_resolved, n_unresolved, n_episodes}}}.
    """
    me = read_machine_episodes(region)
    if me.empty:
        return {}
    rows = me.to_dict("records")
    cutoff = POST_REFLATION_CUTOFF if post_reflation else None
    # _base_rates чете r['open_date'] като date; parquet го дава като Timestamp → нормализирай.
    for r in rows:
        od = r.get("open_date")
        if od is not None and hasattr(od, "date") and callable(od.date):
            r["open_date"] = od.date()
    return _base_rates(rows, min_open_date=cutoff)


def human_track(region: str = "US") -> dict:
    """Човешки track по (config_key, horizon) — брои ЕПИЗОДИ, не записи.

    За всеки кош: n_episodes, direction_hit (close-vs-widen), axis_hit, и разбивка по
    залог (widen-calls, economy_leads-calls) с техните попадения. Само РАЗРЕШЕНИ присъди.
    """
    judgments = {j.judgment_id: j for j in read_judgments() if j.region.upper() == region.upper()}
    out: dict = {}
    for r in read_resolutions():
        if r.region.upper() != region.upper():
            continue
        if r.judgment_id not in judgments:
            continue  # резолюция без присъда (не би трябвало) → пропусни
        j = judgments[r.judgment_id]
        bucket = out.setdefault(j.config_key, {}).setdefault(r.horizon_y, {
            "episode_ids": set(),
            "n_direction_hit": 0, "n_direction_total": 0,
            "widen_calls": 0, "widen_hits": 0,
            "close_calls": 0, "close_hits": 0,
            "economy_leads_calls": 0, "economy_leads_hits": 0,
            "n_axis_scored": 0, "n_axis_hit": 0,
        })
        bucket["episode_ids"].add(r.gap_episode_id)
        bucket["n_direction_total"] += 1
        if r.direction_hit:
            bucket["n_direction_hit"] += 1
        if r.human_claim_direction == "widen":
            bucket["widen_calls"] += 1
            if r.direction_hit:
                bucket["widen_hits"] += 1
        else:
            bucket["close_calls"] += 1
            if r.direction_hit:
                bucket["close_hits"] += 1
            if r.human_claim_axis == "economy_leads":
                bucket["economy_leads_calls"] += 1
                if r.machine_outcome == "economy_leads":
                    bucket["economy_leads_hits"] += 1
            if r.axis_hit is not None:
                bucket["n_axis_scored"] += 1
                if r.axis_hit:
                    bucket["n_axis_hit"] += 1
    for ck in out:
        for y in out[ck]:
            out[ck][y]["n_episodes"] = len(out[ck][y].pop("episode_ids"))
    return out


# ── Доклад ──────────────────────────────────────────────────────────────────────

_OUTCOME_ORDER = ("market_leads", "economy_leads", "meet", "widen")


def format_calibration(region: str = "US") -> str:
    L: list[str] = []
    L.append("═" * 72)
    L.append(f"  КАЛИБРАЦИЯ [{region}] — machine base rate vs human track record")
    L.append("═" * 72)
    L.append("  Брои ЕПИЗОДИ, не записи. n експлицитен. Малък n → 'недостатъчно', не %.")
    L.append("  ⚠ Човекът НЕ се мери срещу market_leads % (velocity asymmetry → ларгели")
    L.append("     механичен). Информативни: close-vs-widen · редкия economy_leads · pos/neg.")
    L.append("")

    # ── Machine base rate (prior) ─────────────────────────────────────────────
    L.append("─" * 72)
    L.append("  MACHINE BASE RATE (look-ahead-biased prior, ПЪЛЕН прозорец)")
    L.append("─" * 72)
    mbr = machine_base_rate(region, post_reflation=False)
    if not mbr:
        L.append("    (няма machine_episodes за региона — пусни journal-backfill първо)")
    else:
        for ck in sorted(mbr):
            L.append(f"  config_key = {ck}")
            for y in sorted(mbr[ck]):
                b = mbr[ck][y]
                L.append(f"    Y={y:>2}w: {_fmt_dist(b)}")
    L.append("")

    # ── Human track record ─────────────────────────────────────────────────────
    L.append("─" * 72)
    L.append("  HUMAN TRACK RECORD (real-time, judgment_date котва)")
    L.append("─" * 72)
    ht = human_track(region)
    if not ht:
        L.append("    (няма разрешени човешки присъди още — журналът тепърва се пълни)")
    else:
        for ck in sorted(ht):
            L.append(f"  config_key = {ck}")
            for y in sorted(ht[ck]):
                b = ht[ck][y]
                L.append(f"    Y={y:>2}w: {_fmt_human(b)}")
    L.append("")

    # ── Калибрация на информативните оси (само при достатъчен n) ───────────────
    L.append("─" * 72)
    L.append(f"  КАЛИБРАЦИЯ (human vs prior — само на ИНФОРМАТИВНИТЕ оси, при n≥{MIN_EPISODES} еп.)")
    L.append("─" * 72)
    lines = _calibration_lines(mbr, ht)
    if lines:
        L.extend(lines)
    else:
        L.append(f"    Недостатъчно разрешени човешки епизоди за калибрация (трябват "
                 f"≥{MIN_EPISODES} на кош). Журналът се пълни forward — върни се след натрупване.")
    L.append("")
    L.append("═" * 72)
    return "\n".join(L)


def _fmt_dist(bucket: dict) -> str:
    n = bucket["n_episodes"]
    nr = bucket["n_resolved"]
    nu = bucket["n_unresolved"]
    parts = []
    for oc in _OUTCOME_ORDER:
        c = bucket["counts"].get(oc, 0)
        if c:
            pct = (100.0 * c / nr) if nr else 0.0
            parts.append(f"{oc}={c} ({pct:.0f}%)")
    dist = " · ".join(parts) if parts else "—"
    return f"n_eps={n} resolved={nr} unresolved={nu}  {dist}"


def _fmt_human(bucket: dict) -> str:
    n = bucket["n_episodes"]
    if n < MIN_EPISODES:
        return f"n_episodes={n} → недостатъчно (трябват ≥{MIN_EPISODES})"
    dt = bucket["n_direction_total"]
    dh = bucket["n_direction_hit"]
    s = f"n_episodes={n} · close-vs-widen: {dh}/{dt}"
    if bucket["widen_calls"]:
        s += f" · widen-calls {bucket['widen_hits']}/{bucket['widen_calls']}"
    if bucket["economy_leads_calls"]:
        s += f" · economy_leads-calls {bucket['economy_leads_hits']}/{bucket['economy_leads_calls']}"
    if bucket["n_axis_scored"]:
        s += f" · ос {bucket['n_axis_hit']}/{bucket['n_axis_scored']}"
    return s


def _calibration_lines(mbr: dict, ht: dict) -> list[str]:
    """Сравнение human-vs-prior, само за кошове с n_episodes ≥ MIN_EPISODES."""
    out: list[str] = []
    for ck in sorted(ht):
        for y in sorted(ht[ck]):
            hb = ht[ck][y]
            if hb["n_episodes"] < MIN_EPISODES:
                continue
            # prior widen rate за тази (config, horizon)
            mb = mbr.get(ck, {}).get(y)
            prior_widen = None
            if mb and mb["n_resolved"]:
                prior_widen = 100.0 * mb["counts"].get("widen", 0) / mb["n_resolved"]
            human_dir = 100.0 * hb["n_direction_hit"] / hb["n_direction_total"]
            seg = f"  {ck} @{y}w (n={hb['n_episodes']}): close-vs-widen точност {human_dir:.0f}%"
            if prior_widen is not None:
                seg += f" | prior widen-база {prior_widen:.0f}%"
            out.append(seg)
    return out
