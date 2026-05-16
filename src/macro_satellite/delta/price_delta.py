"""Interval price change за един symbol между две дати.

КРИТИЧНО ПРАВИЛО (от плана и handoff-а):
  delta = (price_B / price_A) - 1
  НИКОГА не вади return_1m_A от return_1m_B — това дава lagged-window илюзия,
  не реалния interval ход (пример: USO 7→15 май 2026, lagged разлика ≈ +21pp,
  истински ход = +9.83%).
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date


class MissingDataError(Exception):
    pass


@dataclass
class PriceDelta:
    symbol: str
    date_a: date
    date_b: date
    price_a: float
    price_b: float
    interval_change: float
    sources: list[str]


def interval_change(symbol: str, date_a: date, date_b: date, duck) -> PriceDelta:
    sql = """
    SELECT date, price, source
    FROM etf_prices
    WHERE symbol = ? AND date IN (?, ?)
    ORDER BY date
    """
    df = duck.execute(sql, [symbol, date_a, date_b]).df()
    if len(df) < 2:
        raise MissingDataError(
            f"{symbol}: expected rows for {date_a} and {date_b}, "
            f"got {len(df)} ({df['date'].tolist() if not df.empty else 'none'})"
        )
    # Ако git и yfinance се дублират за същата дата → DISTINCT по date с priority
    # за git. Тук просто wzимаме последния (sorted), който е post-upsert.
    df = df.drop_duplicates(subset=["date"], keep="last").sort_values("date")
    if len(df) != 2:
        raise MissingDataError(
            f"{symbol}: after dedup expected 2 rows, got {len(df)}"
        )
    pa = float(df.iloc[0]["price"])
    pb = float(df.iloc[1]["price"])
    if pa <= 0:
        raise ValueError(f"{symbol}: non-positive price_a={pa}")
    return PriceDelta(
        symbol=symbol,
        date_a=date_a,
        date_b=date_b,
        price_a=pa,
        price_b=pb,
        interval_change=(pb / pa) - 1.0,
        sources=df["source"].tolist(),
    )


def interval_change_many(symbols: list[str], date_a: date, date_b: date,
                         duck) -> dict[str, PriceDelta | str]:
    """Връща dict symbol → PriceDelta или error string. Не вдига exception."""
    out: dict[str, PriceDelta | str] = {}
    for s in symbols:
        try:
            out[s] = interval_change(s, date_a, date_b, duck)
        except (MissingDataError, ValueError) as e:
            out[s] = f"ERROR: {e}"
    return out
