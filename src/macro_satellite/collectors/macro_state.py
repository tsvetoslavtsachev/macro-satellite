"""Парсер за us-macro / eu-macro output/api/macro_state.json.

Един JSON snapshot per ден. Flatten-ва lens scores в wide row, executive summary
полета, и сериализира top_anomalies + divergences като JSON strings (за later
expansion в long-format таблици).
"""
from __future__ import annotations

import json
from datetime import date

import pandas as pd

from ..utils.dates import parse_iso_date, parse_iso_datetime, utc_now

_LENSES = ("labor", "growth", "inflation", "liquidity")


def _make_parser(default_region: str):
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
        lenses = d.get("lenses") or {}
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
        for lens in _LENSES:
            lens_data = lenses.get(lens, {}) or {}
            row[f"{lens}_score"] = lens_data.get("score")
            row[f"{lens}_direction"] = lens_data.get("direction")
            row[f"{lens}_breadth_pct"] = lens_data.get("breadth_pct")
            row[f"{lens}_anomalies_count"] = lens_data.get("anomalies_count")
            row[f"{lens}_new_extreme_count"] = lens_data.get("new_extreme_count")

        df = pd.DataFrame([row])
        for c in ("top_anomalies_count", "cross_lens_divergences_count"):
            df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int32")
        for lens in _LENSES:
            df[f"{lens}_anomalies_count"] = pd.to_numeric(
                df[f"{lens}_anomalies_count"], errors="coerce").astype("Int32")
            df[f"{lens}_new_extreme_count"] = pd.to_numeric(
                df[f"{lens}_new_extreme_count"], errors="coerce").astype("Int32")
        return df

    return parse


parse_us = _make_parser("US")
parse_eu = _make_parser("EU")
