"""Парсер за us-macro / eu-macro output/api/macro_state.json.

Един JSON snapshot per ден. Flatten-ва lens scores в wide row, executive summary
полета, и сериализира top_anomalies + divergences като JSON strings (за later
expansion в long-format таблици).
"""
from __future__ import annotations

import json
from datetime import date

import pandas as pd

from ..config import macro_lenses, newgen_macro_lenses
from ..utils.dates import parse_iso_date, parse_iso_datetime, utc_now

_LENSES = ("labor", "growth", "inflation", "liquidity")
# Single-source: EU таксономията идва от config.MACRO_LENSES (labor/growth/
# inflation/credit/external — 5 лещи). НЕ дублирай литерал тук.
_EU_LENSES = macro_lenses("EU")


def _make_parser(default_region: str, lenses: tuple[str, ...] = _LENSES):
    def parse(raw: bytes, snapshot_date: date | None = None,
              source: str = f"{default_region.lower()}_macro_state") -> pd.DataFrame:
        d = json.loads(raw)
        if snapshot_date is None:
            as_of = d.get("as_of_date")
            if not as_of:
                raise ValueError(f"{default_region} macro_state: missing as_of_date")
            snapshot_date = parse_iso_date(as_of)

        generated_at = None
        g = d.get("generated_at")
        if g:
            try:
                generated_at = parse_iso_datetime(g)
            except Exception:
                generated_at = None

        es = d.get("executive_summary") or {}
        top_anom = d.get("top_anomalies") or []
        div = d.get("cross_lens_divergences") or []

        row = {
            "date": snapshot_date,
            "region": d.get("region", default_region),
            "generated_at": generated_at,
            "regime_key": es.get("regime_key"),
            "regime_label_bg": es.get("regime_label_bg"),
            "narrative": es.get("narrative"),
            "primary_driver": es.get("primary_driver"),
            "supporting_signals_json": json.dumps(
                es.get("supporting_signals", []), ensure_ascii=False),
            "top_anomalies_count": len(top_anom),
            "top_anomalies_json": json.dumps(top_anom, ensure_ascii=False),
            "cross_lens_divergences_count": len(div),
            "cross_lens_divergences_json": json.dumps(div, ensure_ascii=False),
            "source": source,
            "ingested_at": utc_now(),
        }
        lens_src = d.get("lenses") or {}
        for lens in lenses:
            lens_data = lens_src.get(lens, {}) or {}
            row[f"{lens}_score"] = lens_data.get("score")
            row[f"{lens}_direction"] = lens_data.get("direction")
            row[f"{lens}_breadth_pct"] = lens_data.get("breadth_pct")
            row[f"{lens}_anomalies_count"] = lens_data.get("anomalies_count")
            row[f"{lens}_new_extreme_count"] = lens_data.get("new_extreme_count")

        df = pd.DataFrame([row])
        for c in ("top_anomalies_count", "cross_lens_divergences_count"):
            df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int32")
        for lens in lenses:
            df[f"{lens}_anomalies_count"] = pd.to_numeric(
                df[f"{lens}_anomalies_count"], errors="coerce").astype("Int32")
            df[f"{lens}_new_extreme_count"] = pd.to_numeric(
                df[f"{lens}_new_extreme_count"], errors="coerce").astype("Int32")
        return df

    return parse


parse_us = _make_parser("US")
parse_eu = _make_parser("EU", _EU_LENSES)


_CN_LENSES = ("growth", "inflation", "labor", "credit", "property")


def parse_cn(raw: bytes, snapshot_date: date | None = None,
             source: str = "cn_macro_state") -> pd.DataFrame:
    """Парсер за china-macro output/api/macro_state.json.

    China има различна таксономия (5 lenses) + претеглен composite_score в
    executive_summary, и per-lens regime. Отделна схема (cn_macro_state).
    """
    d = json.loads(raw)
    if snapshot_date is None:
        as_of = d.get("as_of_date")
        if not as_of:
            raise ValueError("CN macro_state: missing as_of_date")
        snapshot_date = parse_iso_date(as_of)

    generated_at = None
    g = d.get("generated_at")
    if g:
        try:
            generated_at = parse_iso_datetime(g)
        except Exception:
            generated_at = None

    es = d.get("executive_summary") or {}
    lenses = d.get("lenses") or {}
    top_anom = d.get("top_anomalies") or []
    div = d.get("cross_lens_divergences") or []

    row = {
        "date": snapshot_date,
        "region": d.get("region", "CN"),
        "generated_at": generated_at,
        "composite_score": es.get("composite_score"),
        "regime_key": es.get("regime_key"),
        "regime_label_bg": es.get("regime_label_bg"),
        "narrative": es.get("narrative"),
        "primary_driver": es.get("primary_driver"),
        "supporting_signals_json": json.dumps(
            es.get("supporting_signals", []), ensure_ascii=False),
        "top_anomalies_count": len(top_anom),
        "top_anomalies_json": json.dumps(top_anom, ensure_ascii=False),
        "cross_lens_divergences_count": len(div),
        "cross_lens_divergences_json": json.dumps(div, ensure_ascii=False),
        "source": source,
        "ingested_at": utc_now(),
    }
    for lens in _CN_LENSES:
        lens_data = lenses.get(lens, {}) or {}
        row[f"{lens}_score"] = lens_data.get("score")
        row[f"{lens}_direction"] = lens_data.get("direction")
        row[f"{lens}_regime"] = lens_data.get("regime")

    df = pd.DataFrame([row])
    for c in ("top_anomalies_count", "cross_lens_divergences_count"):
        df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int32")
    return df


def _make_newgen_parser(region: str, with_yen: bool = False):
    """Парсер за новата генерация (jp/bg; мандат ORGANISM-v1 Ф5).

    `jp-macro-state v1` / `bg-macro-state v1`: executive_summary цитира
    журналния PIT ред на дашборда (композит + n_series/n_lenses/temp_count/
    k1_ratio/composition), лещите носят score/health_z/n_series. jp добавя
    йена-слоя — пазим го като json цитат (редовете са segment_lines дословно;
    наблюдение, не сигнал). Лещовият ред идва от config.NEWGEN_MACRO_LENSES
    (single-source).
    """
    lenses_taxonomy = newgen_macro_lenses(region)

    def parse(raw: bytes, snapshot_date: date | None = None,
              source: str = f"{region.lower()}_macro_state") -> pd.DataFrame:
        d = json.loads(raw)
        if snapshot_date is None:
            as_of = d.get("as_of_date")
            if not as_of:
                raise ValueError(f"{region} macro_state: missing as_of_date")
            snapshot_date = parse_iso_date(as_of)

        generated_at = None
        g = d.get("generated_at")
        if g:
            try:
                generated_at = parse_iso_datetime(g)
            except Exception:
                generated_at = None

        es = d.get("executive_summary") or {}
        temp = d.get("temperature") or {}

        row = {
            "date": snapshot_date,
            "region": d.get("region", region),
            "generated_at": generated_at,
            "engine": d.get("engine"),
            "composite_score": es.get("composite_score"),
            "regime_key": es.get("regime_key"),
            "regime_label_bg": es.get("regime_label_bg"),
            "n_series": es.get("n_series"),
            "n_lenses": es.get("n_lenses"),
            "temp_count": es.get("temp_count"),
            "k1_ratio": es.get("k1_ratio"),
            "composition": es.get("composition"),
            "tension_sentence": es.get("tension_sentence"),
            "temperature_n_hot": temp.get("n_hot"),
            "temperature_n_total": temp.get("n_total"),
            "temperature_hot_json": json.dumps(
                temp.get("hot", []), ensure_ascii=False),
            "source": source,
            "ingested_at": utc_now(),
        }
        lens_src = d.get("lenses") or {}
        for lens in lenses_taxonomy:
            lens_data = lens_src.get(lens, {}) or {}
            row[f"{lens}_score"] = lens_data.get("score")
            row[f"{lens}_health_z"] = lens_data.get("health_z")
            row[f"{lens}_n_series"] = lens_data.get("n_series")
        if with_yen:
            row["yen_layer_json"] = json.dumps(
                d.get("yen_layer"), ensure_ascii=False)
            row["yen_layer_lines_json"] = json.dumps(
                d.get("yen_layer_lines", []), ensure_ascii=False)

        df = pd.DataFrame([row])
        for c in ("n_series", "n_lenses", "temp_count",
                  "temperature_n_hot", "temperature_n_total"):
            df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int32")
        for lens in lenses_taxonomy:
            df[f"{lens}_n_series"] = pd.to_numeric(
                df[f"{lens}_n_series"], errors="coerce").astype("Int32")
        return df

    return parse


parse_jp = _make_newgen_parser("JP", with_yen=True)
parse_bg = _make_newgen_parser("BG")
