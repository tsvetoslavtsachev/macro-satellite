"""Cross-asset divergence pattern detector.

Чете config/divergence_rules.yaml. За дадена end_date, изчислява interval change
за всеки symbol в pattern conditions over window_days. Триггерира ако
>= min_conditions_met съвпадат.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path

import yaml
from pydantic import BaseModel

from ..paths import CONFIG_DIR
from .weekly_window import last_close_on_or_before


class _Cond(BaseModel):
    symbol: str
    direction: str
    min_change_pct: float


class _Pattern(BaseModel):
    name: str
    label_bg: str
    description: str = ""
    window_days: int = 7
    conditions: list[_Cond]
    min_conditions_met: int = 2
    # П3а: пенсиониран pattern остава в конфига (история/одит), но не се
    # оценява. Пенсия = enabled: false + коментар в YAML, НЕ триене.
    enabled: bool = True


class _RulesConfig(BaseModel):
    patterns: list[_Pattern]


@dataclass
class ConditionMatch:
    symbol: str
    target_direction: str
    target_min_pct: float
    actual_change_pct: float
    matched: bool
    price_a: float | None
    price_b: float | None
    date_a: date | None
    date_b: date | None


@dataclass
class PatternHit:
    name: str
    label_bg: str
    description: str
    end_date: date
    window_days: int
    matches: list[ConditionMatch] = field(default_factory=list)
    n_matched: int = 0
    triggered: bool = False


def _load_rules(path: Path | None = None) -> _RulesConfig:
    p = path or (CONFIG_DIR / "divergence_rules.yaml")
    with open(p, encoding="utf-8") as f:
        return _RulesConfig.model_validate(yaml.safe_load(f))


def evaluate_pattern(pattern: _Pattern, end_date: date, duck) -> PatternHit:
    start_date = end_date - timedelta(days=pattern.window_days)
    matches: list[ConditionMatch] = []
    for cond in pattern.conditions:
        a = last_close_on_or_before(duck, "etf_prices", "symbol", cond.symbol,
                                    "price", start_date)
        b = last_close_on_or_before(duck, "etf_prices", "symbol", cond.symbol,
                                    "price", end_date)
        if a is None or b is None or a[1] <= 0:
            matches.append(ConditionMatch(
                symbol=cond.symbol,
                target_direction=cond.direction,
                target_min_pct=cond.min_change_pct,
                actual_change_pct=float("nan"),
                matched=False,
                price_a=a[1] if a else None,
                price_b=b[1] if b else None,
                date_a=a[0] if a else None,
                date_b=b[0] if b else None,
            ))
            continue
        change_pct = (b[1] / a[1] - 1.0) * 100.0
        if cond.direction == "up":
            ok = change_pct >= cond.min_change_pct
        elif cond.direction == "down":
            ok = change_pct <= -cond.min_change_pct
        else:
            ok = False
        matches.append(ConditionMatch(
            symbol=cond.symbol,
            target_direction=cond.direction,
            target_min_pct=cond.min_change_pct,
            actual_change_pct=change_pct,
            matched=ok,
            price_a=a[1], price_b=b[1],
            date_a=a[0], date_b=b[0],
        ))
    n_matched = sum(1 for m in matches if m.matched)
    return PatternHit(
        name=pattern.name,
        label_bg=pattern.label_bg,
        description=pattern.description,
        end_date=end_date,
        window_days=pattern.window_days,
        matches=matches,
        n_matched=n_matched,
        triggered=n_matched >= pattern.min_conditions_met,
    )


def evaluate_all(end_date: date, duck, config_path: Path | None = None) -> list[PatternHit]:
    rules = _load_rules(config_path)
    return [evaluate_pattern(p, end_date, duck) for p in rules.patterns if p.enabled]
