"""Collector протокол + помощни обвивки.

Parser-ите са top-level функции, regiстрирани като 'module:function' в YAML.
Сигнатура: `parse(raw_bytes: bytes, snapshot_date: date, source: str) -> DataFrame`.
"""
from __future__ import annotations

import importlib
from collections.abc import Callable
from datetime import date

import pandas as pd

from ..config import DashboardConfig

ParserFn = Callable[[bytes, date, str], pd.DataFrame]


class CollectorError(Exception):
    pass


class FetchError(CollectorError):
    pass


class ParseError(CollectorError):
    pass


def load_parser(spec: str) -> ParserFn:
    """spec вид 'module.path:function_name'."""
    if ":" not in spec:
        raise ValueError(f"Parser spec must be 'module:function', got: {spec}")
    mod_name, fn_name = spec.split(":", 1)
    mod = importlib.import_module(mod_name)
    return getattr(mod, fn_name)


def parser_for(dashboard: DashboardConfig) -> ParserFn:
    return load_parser(dashboard.parser)
