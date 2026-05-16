"""Expand JSON columns from us_macro_state / eu_macro_state into long-format tables.

Идемпотентен — преизграждa rows за всеки (date, region, series_id). Може да
тече след всеки collect или като one-shot backfill върху цялата история.

Source: macro_state.top_anomalies_json (list of {series_id, name_bg, lens,
peer_group, z_score, direction, current_value, last_date, is_new_extreme,
new_extreme_direction, narrative_hint}).
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date

import pandas as pd

from ..logging_setup import get_logger
from ..storage import parquet_writer
from ..storage.duckdb_conn import get_duck
from ..utils.dates import utc_now

log = get_logger(__name__)


@dataclass
class ExpandResult:
    region: str
    snapshots_seen: int = 0
    anomaly_rows: int = 0
    divergence_rows: int = 0


def _parse_iso_date(s) -> date | None:
    if not s:
        return None
    if isinstance(s, date):
        return s
    try:
        return date.fromisoformat(str(s)[:10])
    except (ValueError, TypeError):
        return None


def expand_region(region: str, duck=None) -> ExpandResult:
    """Чете <region>_macro_state, expand-ва JSON columns, upsert-ва в long-format."""
    duck = duck or get_duck()
    table = f"{region.lower()}_macro_state"
    sql = (f"SELECT date, top_anomalies_json, cross_lens_divergences_json "
           f"FROM {table} ORDER BY date")
    df = duck.execute(sql).df()
    result = ExpandResult(region=region.upper(), snapshots_seen=len(df))
    if df.empty:
        return result

    now = utc_now()
    anomaly_rows: list[dict] = []
    divergence_rows: list[dict] = []
    source = f"{region.lower()}_macro_state_expander"

    for _, row in df.iterrows():
        snap_date = row["date"]
        if hasattr(snap_date, "date") and callable(snap_date.date):
            snap_date = snap_date.date()

        # anomalies
        try:
            items = json.loads(row["top_anomalies_json"] or "[]")
        except Exception:
            items = []
        for it in items:
            lenses = it.get("lens") or []
            if isinstance(lenses, str):
                lenses = [lenses]
            primary_lens = lenses[0] if lenses else None
            anomaly_rows.append({
                "date": snap_date,
                "region": region.upper(),
                "series_id": it.get("series_id"),
                "name_bg": it.get("name_bg"),
                "lens": primary_lens,
                "lenses_json": json.dumps(lenses, ensure_ascii=False),
                "peer_group": it.get("peer_group"),
                "z_score": it.get("z_score"),
                "direction": it.get("direction"),
                "current_value": it.get("current_value"),
                "last_observation_date": _parse_iso_date(it.get("last_date")),
                "is_new_extreme": bool(it.get("is_new_extreme")),
                "new_extreme_direction": it.get("new_extreme_direction"),
                "narrative_hint": it.get("narrative_hint"),
                "source": source,
                "ingested_at": now,
            })

        # divergences
        try:
            divs = json.loads(row["cross_lens_divergences_json"] or "[]")
        except Exception:
            divs = []
        for d in divs:
            divergence_rows.append({
                "date": snap_date,
                "region": region.upper(),
                "name": d.get("name") or d.get("test") or d.get("key"),
                "label_bg": d.get("label_bg") or d.get("label"),
                "triggered": bool(d.get("triggered", d.get("active", True))),
                "payload_json": json.dumps(d, ensure_ascii=False),
                "source": source,
                "ingested_at": now,
            })

    if anomaly_rows:
        a_df = pd.DataFrame(anomaly_rows)
        n = parquet_writer.upsert("macro_anomalies", a_df,
                                  key_cols=["region", "series_id"])
        result.anomaly_rows = n
        log.info("macro_anomalies upserted",
                 extra={"region": region, "rows": n})

    if divergence_rows:
        d_df = pd.DataFrame(divergence_rows)
        n = parquet_writer.upsert("macro_divergences", d_df,
                                  key_cols=["region", "name"])
        result.divergence_rows = n
        log.info("macro_divergences upserted",
                 extra={"region": region, "rows": n})

    return result


def expand_all(duck=None) -> dict[str, ExpandResult]:
    duck = duck or get_duck()
    return {r: expand_region(r, duck) for r in ("US", "EU")}


def persistent_anomalies(region: str, lookback_weeks: int = 4,
                         min_occurrences: int = 2,
                         min_abs_z: float = 2.0,
                         duck=None) -> pd.DataFrame:
    """Връща серии, които са появили се в top_anomalies поне `min_occurrences` пъти
    за последните `lookback_weeks` седмици, с |z| >= min_abs_z в поне 1 запис.

    Сортирано по (брой появявания desc, средно |z| desc).
    """
    duck = duck or get_duck()
    sql = """
    WITH recent AS (
      SELECT date, series_id, name_bg, lens, peer_group, z_score, direction,
             is_new_extreme
      FROM macro_anomalies
      WHERE region = ?
        AND date >= (SELECT max(date) FROM macro_anomalies WHERE region = ?)
                   - INTERVAL (?) DAY
    )
    SELECT series_id,
           any_value(name_bg) AS name_bg,
           any_value(lens) AS lens,
           any_value(peer_group) AS peer_group,
           count(*) AS occurrences,
           avg(abs(z_score)) AS mean_abs_z,
           max(abs(z_score)) AS max_abs_z,
           min(date) AS first_date,
           max(date) AS last_date,
           bool_or(is_new_extreme) AS any_new_extreme
    FROM recent
    GROUP BY series_id
    HAVING count(*) >= ? AND max(abs(z_score)) >= ?
    ORDER BY occurrences DESC, mean_abs_z DESC
    """
    days = lookback_weeks * 7
    return duck.execute(sql, [region.upper(), region.upper(), days,
                              min_occurrences, min_abs_z]).df()
