"""Merge правила за overlap между git snapshots и yfinance в etf_prices.

Правило: за (date, symbol) където и двата източника имат row → git winner за
полето `price`, source маркер става 'git+yfinance'. yfinance остава дискретен
само за дати/symbols, които git не покрива.

Реализация: разчитаме на това, че backfill редът е (1) yfinance → (2) git history.
parquet_writer.upsert работи по (date, symbol) → git ще overwrite-не yfinance row.
След git phase, итерираме и за git rows checking ако имаше yfinance row за същата
(date, symbol) → ако да, source става 'git+yfinance' и записваме yfinance OHLCV
полета обратно. За simplicity на Фаза 1 — НЕ правим това; git rows запазват само
git fields, yfinance OHLCV се губят за overlap dates. Това е приемливо защото
git цените са истина за overlap, а yfinance OHLCV вече се пази за не-overlap dates.

Този модул е placeholder за по-сложна merge логика във Фаза 2.
"""
from __future__ import annotations
