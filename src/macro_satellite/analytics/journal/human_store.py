"""Човешки журнал на присъдите (Тухла 2b) — ОТДЕЛЕН append-only JSONL store.

Два артефакта, и двата в `journal/` (същия git-tracked namespace като машинните
parquet-и, нула замърсяване на колектора — C3):

  • human_judgments.jsonl   — присъдите (залог на T върху ОТВОРЕН gap-епизод).
  • human_resolutions.jsonl — резолюциите (изход на T+Y; ОТДЕЛЕН immutable запис,
                              рефериращ judgment_id — присъдата НЕ се мутира).

Защо JSONL, не parquet (решение 2026-06-03 с Цветослав):
  - append-only е native (нов ред); parquet иска whole-file rewrite → clobber риск.
  - git-diff-friendly = анти-селекция одит трейл (C3: виждаш изтрита/редактирана присъда).
  - DESIGN моделира ритуала по VRM_WEEK.md (git-tracked текст) — JSONL е текст-аналогът.
  - обемът е нисък (един човек, една присъда/седмица) → parquet ефективността е без значение.

Дисциплина (C3): присъда без `falsification_criterion` → raise ШУМНО, не тихо записва.

⚠ VRM полетата са LOOSE conditioning снимка (виж vrm_snapshot.py) — НЕ влизат в
   gap-триангулацията (тавтология модел↔flow). Записват се за по-късна калибрация
   (как се разрешава присъдата при даден VRM режим), не като това, върху което се залага.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, fields
from datetime import date, datetime
from pathlib import Path

from ...paths import JOURNAL_DIR
from ...utils.dates import utc_now
from .attribution import HORIZONS

JUDGMENTS_FILE = "human_judgments.jsonl"
RESOLUTIONS_FILE = "human_resolutions.jsonl"

VALID_DIRECTION = ("close", "widen")
# Затваряща ос (само при close) — речникът СЪВПАДА с attribution изходите → пряко сравним.
VALID_AXIS = ("market_leads", "economy_leads", "meet")
VALID_CONFIDENCE = ("low", "med", "high")


class JournalDisciplineError(ValueError):
    """C3 нарушение — присъда без falsification_criterion или невалиден залог.

    Raise-ва се ШУМНО при ingest; журналът никога не записва присъда тихо без критерий.
    """


# ── Schemas (dataclass = единствената истина за полетата; JSONL ги сериализира) ──

@dataclass
class HumanJudgment:
    """Залог на T за КОЯ ОС ще затвори gap-епизод (или ще се РАЗШИРИ) до хоризонт Y.

    Залогът е разцепен на посока (close/widen) + затваряща ос — защото калибрационната
    философия мери човека ПЪРВИЧНО на close-vs-widen и на редкия economy_leads, НЕ
    на механичния market_leads дял (velocity asymmetry → market_leads е ларгели механичен).
    """
    judgment_id: str
    gap_episode_id: str          # JOIN ключ → machine_episodes
    region: str
    author: str
    judgment_date: date          # T (real-time котва за резолюцията — нула look-ahead)
    as_of_gap: float             # снимка на gap-а при залагане
    as_of_economy_axis: float
    as_of_markets_axis: float
    config_key: str              # gap_pos | gap_neg (денормализирано от епизода)
    claim_direction: str         # close | widen   ← ПЪРВИЧНИЯТ информативен залог
    claim_axis: str | None        # market_leads|economy_leads|meet (None при widen)
    horizon_y_human: int         # 4 | 8 | 13 (от машинните HORIZONS → resolution преизползва classify)
    falsification_criterion: str # ЗАДЪЛЖИТЕЛНО — без него → JournalDisciplineError
    confidence: str | None       # опционално (low|med|high) — за бъдеща калибрация
    rationale: str | None        # опционално свободен текст
    # ── VRM loose снимка (conditioning, НЕ gap-вход) ────────────────────────────
    vrm_available: bool
    vrm_regime: str | None
    vrm_signal: str | None
    vrm_ks_active: bool | None
    vrm_alignment: float | None
    vrm_last_updated: date | None
    vrm_age_days: int | None
    vrm_stale: bool | None
    ingested_at: datetime | None = None


@dataclass
class HumanResolution:
    """Изход на присъда на хоризонт Y — ОТДЕЛЕН immutable запис (рефериращ judgment_id).

    Котва = judgment_date (НЕ episode open_date) → истински real-time forward тест,
    нула look-ahead. Преизползва attribution.classify (същата vol-норм. математика като
    машинния base rate); различен прозорец → НЕ apples-to-apples (prior-vs-realtime).
    """
    resolution_id: str
    judgment_id: str
    gap_episode_id: str
    region: str
    horizon_y: int
    judgment_date: date
    resolved_week: str
    resolved_date: date
    as_of_gap: float
    y_gap: float
    d_economy: float
    d_markets: float
    machine_outcome: str         # market_leads|economy_leads|meet|widen (от classify на T+Y)
    machine_m_share: float | None
    machine_e_share: float | None
    human_claim_direction: str
    human_claim_axis: str | None
    direction_hit: bool          # позна ли close-vs-widen? (ПЪРВИЧНАТА информативна ос)
    axis_hit: bool | None         # ако close & machine затвори: позна ли затварящата ос? (None при widen)
    resolved_at: datetime | None = None


# ── JSON (de)serialization — date/datetime ↔ ISO низове ─────────────────────────

def _to_jsonable(rec) -> dict:
    out: dict = {}
    for k, v in asdict(rec).items():
        if isinstance(v, datetime):
            out[k] = v.isoformat()
        elif isinstance(v, date):
            out[k] = v.isoformat()
        else:
            out[k] = v
    return out


_DATE_FIELDS = {"judgment_date", "vrm_last_updated", "resolved_date"}
_DATETIME_FIELDS = {"ingested_at", "resolved_at"}


def _from_json(d: dict, cls):
    kwargs = {}
    valid = {f.name for f in fields(cls)}
    for k, v in d.items():
        if k not in valid:
            continue
        if v is not None and k in _DATE_FIELDS:
            v = date.fromisoformat(v)
        elif v is not None and k in _DATETIME_FIELDS:
            v = datetime.fromisoformat(v)
        kwargs[k] = v
    return cls(**kwargs)


# ── Validation (C3 gate) ────────────────────────────────────────────────────────

def validate_judgment(j: HumanJudgment) -> None:
    """Raise ШУМНО при дисциплинно нарушение (C3). Извиква се ПРЕДИ всеки append."""
    if not (j.gap_episode_id and j.gap_episode_id.strip()):
        raise JournalDisciplineError("присъда без gap_episode_id (към кой епизод се отнася?)")
    if not (j.author and j.author.strip()):
        raise JournalDisciplineError(f"{j.gap_episode_id}: присъда без author")
    if not (j.falsification_criterion and j.falsification_criterion.strip()):
        raise JournalDisciplineError(
            f"{j.gap_episode_id}: присъда БЕЗ falsification_criterion → отказвам да я "
            f"запиша (C3 — falsifiable или нищо). Какво би доказало, че грешиш?"
        )
    if j.claim_direction not in VALID_DIRECTION:
        raise JournalDisciplineError(
            f"{j.gap_episode_id}: claim_direction='{j.claim_direction}' невалиден "
            f"(очаквам {VALID_DIRECTION})"
        )
    if j.claim_direction == "close":
        if j.claim_axis not in VALID_AXIS:
            raise JournalDisciplineError(
                f"{j.gap_episode_id}: claim_direction=close изисква claim_axis ∈ {VALID_AXIS}, "
                f"а е '{j.claim_axis}'"
            )
    else:  # widen
        if j.claim_axis is not None:
            raise JournalDisciplineError(
                f"{j.gap_episode_id}: claim_direction=widen → claim_axis трябва да е празен "
                f"(а е '{j.claim_axis}')"
            )
    if j.horizon_y_human not in HORIZONS:
        raise JournalDisciplineError(
            f"{j.gap_episode_id}: horizon_y_human={j.horizon_y_human} извън машинните "
            f"хоризонти {HORIZONS}"
        )
    if j.confidence is not None and j.confidence not in VALID_CONFIDENCE:
        raise JournalDisciplineError(
            f"{j.gap_episode_id}: confidence='{j.confidence}' невалиден (очаквам {VALID_CONFIDENCE})"
        )


def make_judgment_id(gap_episode_id: str, judgment_date: date, horizon_y: int) -> str:
    """Стабилен id: епизод × дата × хоризонт (един епизод може да има няколко присъди
    на различни дати/хоризонти — всяка е отделен залог)."""
    return f"hj_{gap_episode_id}_{judgment_date.isoformat()}_{horizon_y}w"


# ── Append-only IO ──────────────────────────────────────────────────────────────

def _ensure_dir() -> Path:
    JOURNAL_DIR.mkdir(parents=True, exist_ok=True)
    return JOURNAL_DIR


def _judgments_path() -> Path:
    return JOURNAL_DIR / JUDGMENTS_FILE


def _resolutions_path() -> Path:
    return JOURNAL_DIR / RESOLUTIONS_FILE


def read_judgments() -> list[HumanJudgment]:
    path = _judgments_path()
    if not path.exists():
        return []
    out: list[HumanJudgment] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        out.append(_from_json(json.loads(line), HumanJudgment))
    return out


def read_resolutions() -> list[HumanResolution]:
    path = _resolutions_path()
    if not path.exists():
        return []
    out: list[HumanResolution] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        out.append(_from_json(json.loads(line), HumanResolution))
    return out


def append_judgment(j: HumanJudgment) -> bool:
    """Валидира (C3 raise) + append. Idempotent: ако judgment_id вече съществува → skip
    (връща False), не дублира (append-only integrity). Връща True ако е записана нова."""
    validate_judgment(j)
    existing = {x.judgment_id for x in read_judgments()}
    if j.judgment_id in existing:
        return False
    if j.ingested_at is None:
        j.ingested_at = utc_now()
    _ensure_dir()
    with _judgments_path().open("a", encoding="utf-8") as f:
        f.write(json.dumps(_to_jsonable(j), ensure_ascii=False) + "\n")
    return True


def append_resolution(r: HumanResolution) -> bool:
    """Append резолюция. Idempotent по resolution_id (skip ако вече разрешена)."""
    existing = {x.resolution_id for x in read_resolutions()}
    if r.resolution_id in existing:
        return False
    if r.resolved_at is None:
        r.resolved_at = utc_now()
    _ensure_dir()
    with _resolutions_path().open("a", encoding="utf-8") as f:
        f.write(json.dumps(_to_jsonable(r), ensure_ascii=False) + "\n")
    return True


def resolved_judgment_ids() -> set[str]:
    return {r.judgment_id for r in read_resolutions()}
