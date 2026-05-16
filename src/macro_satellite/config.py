"""Зарежда config/dashboards.yaml и config/etf_universe.yaml в pydantic модели."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field

from .paths import CONFIG_DIR


class GithubSource(BaseModel):
    owner: str
    repo: str
    branch: str = "main"
    file: str


class DashboardConfig(BaseModel):
    name: str
    table: str
    github: GithubSource
    parser: str = Field(..., description="module:function')")
    key_cols: list[str] = []
    stale_tolerable_days: int = 7


class DashboardsConfig(BaseModel):
    dashboards: list[DashboardConfig]

    def by_name(self, name: str) -> DashboardConfig:
        for d in self.dashboards:
            if d.name == name:
                return d
        raise KeyError(f"Dashboard not in config: {name}")


class EtfUniverseConfig(BaseModel):
    period: str = "5y"
    interval: str = "1d"
    auto_supplement_from_etf_dashboard: bool = True
    symbols: list[str] = []


def _load_yaml(path: Path) -> dict[str, Any]:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_dashboards_config(path: Path | None = None) -> DashboardsConfig:
    p = path or (CONFIG_DIR / "dashboards.yaml")
    return DashboardsConfig.model_validate(_load_yaml(p))


def load_etf_universe(path: Path | None = None) -> EtfUniverseConfig:
    p = path or (CONFIG_DIR / "etf_universe.yaml")
    return EtfUniverseConfig.model_validate(_load_yaml(p))


def github_raw_url(src: GithubSource, sha: str | None = None) -> str:
    """raw.githubusercontent.com URL за конкретен SHA или branch."""
    ref = sha or src.branch
    return f"https://raw.githubusercontent.com/{src.owner}/{src.repo}/{ref}/{src.file}"
