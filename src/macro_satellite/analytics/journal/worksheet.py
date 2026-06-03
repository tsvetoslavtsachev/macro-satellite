"""JOURNAL_WEEK.md worksheet (Тухла 2b, Възел 5) — ритуалната повърхност à la VRM_WEEK.md.

Двустъпков ритуал (дисциплината идва от ритуала, не от cron):
  1. journal-prep   → ГЕНЕРИРА pre-filled worksheet (отворени епизоди + VRM C6 снимка +
                      празни ПРИСЪДА блокове + дължими резолюции).
  2. (човек попълва ПРИСЪДА блока/блоковете)
  3. journal-judge  → ПАРСВА worksheet → валидира (C3 raise) → append в JSONL + разрешава.

⚠ Worksheet-ът е ТРАНЗИЕНТЕН (презаписва се всеки prep, като VRM_WEEK.md). Постоянният,
   append-only запис е journal/human_judgments.jsonl. Worksheet ≠ source of truth.

⚠ as_of снимката и VRM се вземат при INGEST (journal-judge), котвани на judgment_date —
   gap-ът от gap_series, VRM през read_vrm_snapshot. Блоковете тук са за ЧЕТЕНЕ; ingest
   пре-смята от единствения източник (gap_series), не вярва на worksheet числата.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date

WORKSHEET_FILE = "JOURNAL_WEEK.md"


@dataclass
class ParsedJudgmentBlock:
    """Суров парснат ПРИСЪДА блок (преди валидация/обогатяване с gap+VRM)."""
    gap_episode_id: str
    claim_direction: str | None
    claim_axis: str | None
    horizon_y_human: int | None
    falsification_criterion: str | None
    confidence: str | None
    rationale: str | None


def _is_placeholder(v: str | None) -> bool:
    """'[close | widen]' / '' / '-' → незапълнено."""
    if v is None:
        return True
    v = v.strip()
    return (not v) or v.startswith("[") or v in ("-", "—", "_")


def _kv(text: str, key: str) -> str | None:
    m = re.search(rf"^{re.escape(key)}\s*:\s*(.*?)\s*$", text, re.MULTILINE)
    if not m:
        return None
    val = m.group(1)
    # отрежи trailing inline коментар (# ...)
    val = re.sub(r"\s+#.*$", "", val).strip()
    return val or None


# ── Генериране (journal-prep) ─────────────────────────────────────────────────

def _empty_judgment_block(episode_id: str) -> str:
    return (
        "```\n"
        f"ПРИСЪДА_ЗА_ЕПИЗОД:        {episode_id}\n"
        "ПОСОКА:                   [close | widen]\n"
        "ЗАТВАРЯЩА_ОС:             [market_leads | economy_leads | meet]   # САМО ако close; иначе празно\n"
        "ХОРИЗОНТ_СЕДМИЦИ:         [4 | 8 | 13]\n"
        "КРИТЕРИЙ_ЗА_ОПРОВЕРЖЕНИЕ: [ЗАДЪЛЖИТЕЛНО — какво конкретно би доказало, че греша]\n"
        "УВЕРЕНОСТ:                [low | med | high]   # опционално\n"
        "ОБОСНОВКА:                [опционално]\n"
        "```\n"
    )


def generate_worksheet(region: str,
                       judgment_date: date,
                       author: str,
                       open_episodes: list[dict],
                       latest_gap: dict | None,
                       vrm,
                       pending_due: list[dict]) -> str:
    """Сглобява JOURNAL_WEEK.md текста.

    Args:
        open_episodes: [{gap_episode_id, config_key, open_date, peak_gap, age_weeks}]
        latest_gap: {week, week_end, gap, economy_axis, markets_axis} (последна седмица) | None
        vrm: VrmSnapshot
        pending_due: [{judgment_id, gap_episode_id, horizon_y, due_week}]
    """
    L: list[str] = []
    L.append("# JOURNAL_WEEK — Тухла 2b · human judgment worksheet")
    L.append("> ⚠ ТРАНЗИЕНТЕН worksheet (като VRM_WEEK.md). Постоянният запис е append-only")
    L.append("> `journal/human_judgments.jsonl`. Този файл се презаписва при всеки journal-prep.")
    L.append("> Дисциплина (C3): присъда БЕЗ КРИТЕРИЙ_ЗА_ОПРОВЕРЖЕНИЕ → journal-judge ГРЪМВА.")
    L.append("")
    L.append(f"**Регион:** {region}")
    L.append(f"**Дата на присъдата (T):** {judgment_date.isoformat()}")
    L.append(f"**Автор:** {author}")
    L.append("")
    L.append("---")
    L.append("")
    # VRM
    L.append("## 🧭 VRM снимка (loose conditioning — НЕ влиза в gap-а)")
    L.append("*Прочетена през C6 hibrid четеца; информативна. НЕ е това, върху което залагаш.*")
    L.append("```")
    L.append(f"VRM_AVAILABLE:    {'ДА' if vrm.available else 'НЕ'}")
    if vrm.available:
        L.append(f"VRM_REGIME:       {vrm.regime}")
        L.append(f"VRM_SIGNAL:       {vrm.signal or '-'}")
        L.append(f"VRM_KS_ACTIVE:    {'ДА' if vrm.ks_active else 'НЕ'}")
        L.append(f"VRM_ALIGNMENT:    {vrm.alignment if vrm.alignment is not None else '-'}")
        L.append(f"VRM_LAST_UPDATED: {vrm.last_updated.isoformat() if vrm.last_updated else '-'}")
        L.append(f"VRM_AGE_DAYS:     {vrm.age_days if vrm.age_days is not None else '-'}")
        L.append(f"VRM_STALE:        {'ДА' if vrm.stale else 'НЕ'}")
    L.append("```")
    L.append("")
    L.append("---")
    L.append("")
    # Open episodes
    L.append("## 📂 ОТВОРЕНИ епизоди (върху които можеш да заложиш)")
    if not open_episodes:
        L.append("*(няма отворени епизоди за региона — нищо за залагане тази седмица)*")
    else:
        gap_note = ""
        if latest_gap:
            gap_note = (f"  (седмица {latest_gap['week']}, край {latest_gap['week_end']})")
        L.append(f"*Машинно-извлечени. GAP_СЕГА = последната седмица в gap_series{gap_note}.*")
        for ep in open_episodes:
            L.append("```")
            L.append(f"EPISODE:   {ep['gap_episode_id']}")
            L.append(f"CONFIG:    {ep['config_key']}")
            L.append(f"OPEN:      {ep['open_date']}  (възраст ~{ep['age_weeks']} седмици)")
            L.append(f"PEAK_GAP:  {ep['peak_gap']:+.3f}")
            if latest_gap:
                L.append(f"GAP_СЕГА:  {latest_gap['gap']:+.3f}")
                L.append(f"ИКОН_ОС:   {latest_gap['economy_axis']:+.3f}")
                L.append(f"ПАЗАР_ОС:  {latest_gap['markets_axis']:+.3f}")
            L.append("```")
    L.append("")
    L.append("---")
    L.append("")
    # Judgment blocks to fill
    L.append("## ✍️ ПРИСЪДА — попълни (копирай блока за втора присъда)")
    L.append("*ПОСОКА: close (gap ще се свие до Y) | widen (ще персистира/расте). ЗАТВАРЯЩА_ОС само при close.*")
    L.append("*Най-информативно (калибрационна философия): close-vs-widen + редкия economy_leads.*")
    L.append("")
    if open_episodes:
        L.append(_empty_judgment_block(open_episodes[0]["gap_episode_id"]))
    else:
        L.append(_empty_judgment_block("<gap_episode_id>"))
    L.append("---")
    L.append("")
    # Pending resolutions
    L.append("## ⏳ РЕЗОЛЮЦИИ ДЪЛЖИМИ (auto при journal-judge)")
    L.append("*Присъди без резолюция, чийто хоризонт е настъпил. journal-judge ще ги разреши.*")
    if not pending_due:
        L.append("*(няма дължими резолюции)*")
    else:
        L.append("```")
        for p in pending_due:
            L.append(f"{p['judgment_id']}  → хоризонт {p['horizon_y']}w настъпи ({p['due_week']})")
        L.append("```")
    L.append("")
    return "\n".join(L)


# ── Парсване (journal-judge) ──────────────────────────────────────────────────

def parse_worksheet(text: str) -> tuple[str | None, date | None, str | None, list[ParsedJudgmentBlock]]:
    """Извлича (region, judgment_date, author, [запълнени ПРИСЪДА блокове]).

    Връща САМО блокове с поне ПОСОКА запълнена (не placeholder) — празните темплейти се
    игнорират. Валидацията (C3 raise при липсващ критерий) е на human_store, не тук.
    """
    region = _header_val(text, "Регион")
    jd_raw = _header_val(text, "Дата на присъдата (T)")
    judgment_date = None
    if jd_raw:
        m = re.search(r"(\d{4}-\d{2}-\d{2})", jd_raw)
        if m:
            judgment_date = date.fromisoformat(m.group(1))
    author = _header_val(text, "Автор")

    blocks: list[ParsedJudgmentBlock] = []
    for block in _fenced_blocks(text):
        if "ПРИСЪДА_ЗА_ЕПИЗОД" not in block:
            continue
        episode = _kv(block, "ПРИСЪДА_ЗА_ЕПИЗОД")
        direction = _kv(block, "ПОСОКА")
        if _is_placeholder(episode) or _is_placeholder(direction):
            continue  # незапълнен темплейт → пропусни тихо
        axis_raw = _kv(block, "ЗАТВАРЯЩА_ОС")
        axis = None if _is_placeholder(axis_raw) else axis_raw.strip().lower()
        hz_raw = _kv(block, "ХОРИЗОНТ_СЕДМИЦИ")
        horizon = None
        if not _is_placeholder(hz_raw):
            m = re.search(r"\d+", hz_raw)
            horizon = int(m.group(0)) if m else None
        crit_raw = _kv(block, "КРИТЕРИЙ_ЗА_ОПРОВЕРЖЕНИЕ")
        criterion = None if _is_placeholder(crit_raw) else crit_raw.strip()
        conf_raw = _kv(block, "УВЕРЕНОСТ")
        confidence = None if _is_placeholder(conf_raw) else conf_raw.strip().lower()
        rat_raw = _kv(block, "ОБОСНОВКА")
        rationale = None if _is_placeholder(rat_raw) else rat_raw.strip()
        blocks.append(ParsedJudgmentBlock(
            gap_episode_id=episode.strip(),
            claim_direction=direction.strip().lower(),
            claim_axis=axis,
            horizon_y_human=horizon,
            falsification_criterion=criterion,
            confidence=confidence,
            rationale=rationale,
        ))
    return region, judgment_date, author, blocks


def _header_val(text: str, label: str) -> str | None:
    m = re.search(rf"\*\*{re.escape(label)}:\*\*\s*(.+)", text)
    return m.group(1).strip() if m else None


def _fenced_blocks(text: str) -> list[str]:
    return re.findall(r"```(.*?)```", text, re.DOTALL)
