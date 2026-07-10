# macro-satellite

Аналитичен сателит за ELANA dashboards — daily time-series collector + delta engine.

## Какво прави

Чете daily snapshots от dashboards публикувани в GitHub, съхранява ги като Parquet (партиционирано по year/month), и открива промени между snapshots — без илюзията на lagged returns.

**Принципи:**
1. Запазваме **цените**, не lagged returns. Interval change = `(price_B / price_A) - 1`.
2. Time-series, не snapshot.
3. Daily granularity, weekly/monthly aggregates по-късно.

## Източници (Фаза 1)

| Dashboard | GitHub repo | Файл |
|---|---|---|
| ETF | `tsvetoslavtsachev/ETF-Dashboard` | `data/etfs.json` |
| SP500 Rotation | `tsvetoslavtsachev/SP500-rotationradar` | `docs/data.json` |
| STOXX600 Rotation | `tsvetoslavtsachev/STOXX600-rotationradar` | `docs/data.json` |
| COT Monitor | `tsvetoslavtsachev/cot-monitor` | `data/manifest.json` + `markets/*.json` |
| VRM State | `tsvetoslavtsachev/vrm-state` | `VRM_STATE.md` |

## Runtime

- GitHub Actions workflow (`daily-collect.yml`), cron `0 1 * * *` UTC = 04:00 София.
- Storage commit-нат обратно в repo (Git LFS за `storage/parquet/**`).
- Локални queries върху Parquet с DuckDB.

## CLI

```
python -m macro_satellite collect              # daily live collect
python -m macro_satellite backfill-base --period 5y                              # ETF цени (base-first канон; yfinance CLOSED fallback)
python -m macro_satellite backfill --dashboard sp500_rotation --since 2026-01-01 # github source backfill
python -m macro_satellite delta --from 2026-05-07 --to 2026-05-15
python -m macro_satellite delta --auto-prev    # most-recent vs prev-snapshot
```

## Setup локално

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
python -m pip install -e ".[dev]"
git lfs install
pytest tests/ -v
```

## Организмови етикети (КОКПИТ Вълна 1)

- **COT percentile честно име (B1):** схемата `cot_positioning` носи `percentile_hist` + `hist_weeks` вместо подвеждащото `percentile_5y` (реалният прозорец е ПЪЛНА ИСТОРИЯ, 229-1046 седм — несравним между пазари). Old parquet чете data-safe през `union_by_name=true`; `percentile_3y` остава винаги `None`. Консуматорът `full_export._section_cot` показва „Percentile (пълна история)" + колона „Ист. седмици".
- **О4 бадж на дашборда:** header-ът носи `НАБЛЮДЕНИЕ, НЕ СИГНАЛ · coincident` — уредът наблюдава състояние, не издава сигнал за действие.

Подробности в [DESIGN.md](DESIGN.md).
