# Сателит — пълен data export за 2026-W38

_Период: 2026-09-14 → 2026-09-20_  
_Генериран: 2026-09-18 10:42 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W38.md` (structured briefing) и `narrative_2026-W38.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**11 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **XLF** | -2.31% | -2.30σ | 57.25 | 55.93 | 2026-09-11 | 2026-09-16 | +0.55% | +1.24% | 13 |
| **DIA** | -2.01% | -1.86σ | 525.79 | 515.22 | 2026-09-11 | 2026-09-16 | +0.20% | +1.19% | 13 |
| **UUP** | +1.18% | +1.58σ | 28.07 | 28.40 | 2026-09-11 | 2026-09-16 | +0.04% | +0.72% | 13 |
| **VEA** | -1.97% | -1.47σ | 72.69 | 71.26 | 2026-09-11 | 2026-09-16 | +0.13% | +1.43% | 13 |
| **EFA** | -1.57% | -1.29σ | 106.70 | 105.02 | 2026-09-11 | 2026-09-16 | +0.13% | +1.32% | 13 |
| **EEM** | -3.12% | -1.15σ | 67.84 | 65.72 | 2026-09-11 | 2026-09-16 | +0.03% | +2.75% | 13 |
| **IWM** | -1.72% | -1.08σ | 288.89 | 283.92 | 2026-09-11 | 2026-09-16 | -0.10% | +1.51% | 13 |
| **VWO** | -1.94% | -1.07σ | 60.35 | 59.18 | 2026-09-11 | 2026-09-16 | +0.12% | +1.92% | 13 |
| **XLI** | -2.12% | -1.06σ | 172.37 | 168.71 | 2026-09-11 | 2026-09-16 | -0.15% | +1.87% | 13 |
| **XLU** | -2.52% | -1.05σ | 42.39 | 41.32 | 2026-09-11 | 2026-09-16 | -0.36% | +2.06% | 13 |
| **SPY** | -1.34% | -1.02σ | 764.29 | 754.05 | 2026-09-11 | 2026-09-16 | +0.24% | +1.54% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-09-20 · **Conditions matched:** 4/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | +0.82% | ❌ | 154.90 | 156.17 | 2026-09-11 | 2026-09-16 |
| DFEN | down ≥ 3.0% | -4.89% | ✅ | 56.08 | 53.34 | 2026-09-11 | 2026-09-16 |
| GLD | down ≥ 1.0% | -1.76% | ✅ | 398.77 | 391.74 | 2026-09-11 | 2026-09-16 |
| URA | down ≥ 3.0% | -4.96% | ✅ | 43.53 | 41.37 | 2026-09-11 | 2026-09-16 |
| UUP | up ≥ 0.5% | +1.18% | ✅ | 28.07 | 28.40 | 2026-09-11 | 2026-09-16 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-09-20 · **Conditions matched:** 1/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | -1.72% | ❌ | 288.89 | 283.92 | 2026-09-11 | 2026-09-16 |
| XLF | up ≥ 1.0% | -2.31% | ❌ | 57.25 | 55.93 | 2026-09-11 | 2026-09-16 |
| XLY | up ≥ 1.0% | -2.46% | ❌ | 112.96 | 110.18 | 2026-09-11 | 2026-09-16 |
| GLD | down ≥ 0.5% | -1.76% | ✅ | 398.77 | 391.74 | 2026-09-11 | 2026-09-16 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2021-W36 (week ending 2021-09-12)
**Cosine similarity:** 0.9288 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -2.65% | +5.68% | -5.70% |
| **USO** | +14.98% | +6.62% | +56.56% |
| **GLD** | -1.51% | -0.36% | +10.71% |
| **TLT** | -3.01% | +0.31% | -9.09% |
| **XLE** | +18.04% | +19.77% | +60.81% |
| **IWM** | -0.05% | -0.77% | -11.23% |

### Паралел #2: 2022-W17 (week ending 2022-05-01)
**Cosine similarity:** 0.9059 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.23% | -0.00% | -5.58% |
| **USO** | +10.77% | +1.15% | -5.62% |
| **GLD** | -3.26% | -7.24% | -13.42% |
| **TLT** | -2.42% | -1.69% | -18.96% |
| **XLE** | +16.03% | +4.35% | +18.76% |
| **IWM** | +0.19% | +1.24% | -0.97% |

### Паралел #3: 2022-W19 (week ending 2022-05-15)
**Cosine similarity:** 0.9011 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -6.93% | +6.32% | -0.80% |
| **USO** | +8.82% | -7.75% | -8.49% |
| **GLD** | -0.13% | -0.55% | -2.51% |
| **TLT** | -6.18% | -0.37% | -15.60% |
| **XLE** | +4.28% | -2.86% | +15.29% |
| **IWM** | -4.88% | +12.52% | +4.96% |

### Паралел #4: 2022-W37 (week ending 2022-09-18)
**Cosine similarity:** 0.8574 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -3.74% | -0.59% | +1.15% |
| **USO** | -1.72% | -7.15% | -16.08% |
| **GLD** | -1.34% | +7.03% | +17.92% |
| **TLT** | -8.17% | +0.04% | -0.21% |
| **XLE** | +4.53% | +7.55% | -1.87% |
| **IWM** | -2.69% | -2.58% | -4.34% |

### Паралел #5: 2021-W24 (week ending 2021-06-20)
**Cosine similarity:** 0.8536 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.89% | +6.38% | +10.83% |
| **USO** | -3.83% | +4.05% | +5.00% |
| **GLD** | +2.70% | -0.70% | +1.74% |
| **TLT** | +2.93% | +2.36% | +3.50% |
| **XLE** | -9.16% | -5.86% | +3.78% |
| **IWM** | -1.72% | +0.16% | -3.15% |

### Паралел #6: 2023-W08 (week ending 2023-02-26)
**Cosine similarity:** 0.8413 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -0.20% | +5.96% | +11.00% |
| **USO** | -3.80% | -3.43% | +7.97% |
| **GLD** | +8.96% | +7.47% | +5.51% |
| **TLT** | +3.53% | +0.12% | -5.69% |
| **XLE** | -4.58% | -6.96% | +3.46% |
| **IWM** | -7.50% | -6.06% | -1.87% |

### Паралел #7: 2022-W03 (week ending 2022-01-23)
**Cosine similarity:** 0.8364 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.92% | -2.73% | -9.79% |
| **USO** | +7.83% | +25.55% | +22.62% |
| **GLD** | +3.74% | +5.38% | -6.09% |
| **TLT** | -3.51% | -16.46% | -17.46% |
| **XLE** | +7.21% | +22.02% | +13.93% |
| **IWM** | -0.17% | -2.19% | -8.87% |

### Паралел #8: 2023-W38 (week ending 2023-09-24)
**Cosine similarity:** 0.8129 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.58% | +10.04% | +21.09% |
| **USO** | -4.59% | -14.81% | -4.90% |
| **GLD** | +2.42% | +6.52% | +12.17% |
| **TLT** | -6.65% | +7.71% | +2.79% |
| **XLE** | -1.97% | -4.85% | +3.46% |
| **IWM** | -5.77% | +14.04% | +16.08% |

### Паралел #9: 2025-W31 (week ending 2025-08-03)
**Cosine similarity:** 0.7997 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.98% | +9.71% | +11.30% |
| **USO** | -0.90% | -6.33% | +2.66% |
| **GLD** | +5.33% | +19.09% | +43.95% |
| **TLT** | -2.49% | +2.81% | -0.79% |
| **XLE** | +5.76% | +2.97% | +19.29% |
| **IWM** | +8.83% | +14.57% | +20.81% |

### Паралел #10: 2022-W23 (week ending 2022-06-12)
**Cosine similarity:** 0.7809 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -2.30% | +4.31% | +0.89% |
| **USO** | -19.22% | -21.11% | -30.27% |
| **GLD** | -7.85% | -8.43% | -4.29% |
| **TLT** | +1.19% | -4.80% | -6.54% |
| **XLE** | -22.33% | -9.14% | -6.80% |
| **IWM** | -3.99% | +4.93% | +0.02% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 15 · **Total matching days:** 78 · **History:** 2021-05-17 → 2026-09-16

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 15 | +2.0% | +1.7% | -3.1% | +7.4% | 67% |
| **SPY** | 3m | 15 | +2.5% | +2.4% | -7.3% | +12.0% | 73% |
| **SPY** | 6m | 15 | +6.8% | +8.6% | -6.8% | +21.8% | 73% |
| **USO** | 1m | 15 | +0.4% | -0.8% | -14.3% | +12.7% | 47% |
| **USO** | 3m | 15 | -0.3% | -1.4% | -18.9% | +26.0% | 47% |
| **USO** | 6m | 15 | +14.4% | +3.7% | -8.7% | +109.4% | 60% |
| **GLD** | 1m | 15 | +2.8% | +0.9% | -1.2% | +9.0% | 73% |
| **GLD** | 3m | 15 | +5.2% | +5.9% | -12.6% | +24.5% | 67% |
| **GLD** | 6m | 15 | +6.1% | +6.3% | -12.5% | +25.3% | 67% |
| **TLT** | 1m | 15 | -1.4% | -1.1% | -6.7% | +3.6% | 40% |
| **TLT** | 3m | 15 | -0.7% | +0.1% | -16.5% | +11.1% | 53% |
| **TLT** | 6m | 15 | -4.3% | -4.3% | -18.0% | +7.5% | 33% |

**Episodes (последни 5 от 15):**
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-08-03` (5d)
- `2026-09-10 → 2026-09-16` (4d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 87 · **History:** 2021-05-17 → 2026-09-16

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +6.3% | +6.3% | +3.5% | +9.1% | 100% |
| **SPY** | 3m | 2 | +5.3% | +5.3% | +0.3% | +10.3% | 100% |
| **SPY** | 6m | 2 | +5.9% | +5.9% | +0.3% | +11.5% | 100% |
| **USO** | 1m | 2 | +5.6% | +5.6% | +4.0% | +7.2% | 100% |
| **USO** | 3m | 2 | +10.0% | +10.0% | -9.9% | +30.0% | 50% |
| **USO** | 6m | 2 | +27.7% | +27.7% | +25.4% | +30.0% | 100% |
| **GLD** | 1m | 2 | +3.5% | +3.5% | -0.2% | +7.2% | 50% |
| **GLD** | 3m | 2 | -4.3% | -4.3% | -13.8% | +5.3% | 50% |
| **GLD** | 6m | 2 | -2.3% | -2.3% | -9.8% | +5.3% | 50% |
| **TLT** | 1m | 2 | -1.4% | -1.4% | -1.8% | -1.0% | 0% |
| **TLT** | 3m | 2 | -3.4% | -3.4% | -3.8% | -2.9% | 0% |
| **TLT** | 6m | 2 | -5.4% | -5.4% | -6.9% | -3.8% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-09-15` (40d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 443 · **History:** 2021-05-17 → 2026-09-16

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 8 | +0.0% | +0.8% | -4.5% | +3.4% | 75% |
| **SPY** | 3m | 8 | +4.4% | +5.7% | -3.3% | +9.6% | 88% |
| **SPY** | 6m | 8 | +9.4% | +9.5% | -1.6% | +20.3% | 88% |
| **USO** | 1m | 8 | -0.5% | -2.6% | -8.7% | +13.1% | 38% |
| **USO** | 3m | 8 | -2.2% | -0.7% | -14.6% | +7.9% | 38% |
| **USO** | 6m | 8 | +11.6% | -3.0% | -8.2% | +102.9% | 38% |
| **GLD** | 1m | 8 | +3.7% | +3.8% | -0.5% | +10.2% | 75% |
| **GLD** | 3m | 8 | +11.1% | +12.7% | +1.6% | +17.5% | 100% |
| **GLD** | 6m | 8 | +17.2% | +12.9% | +10.5% | +29.7% | 100% |
| **TLT** | 1m | 8 | -0.4% | -0.2% | -6.4% | +5.4% | 50% |
| **TLT** | 3m | 8 | +3.2% | +3.2% | -4.1% | +10.4% | 62% |
| **TLT** | 6m | 8 | -0.2% | -1.2% | -5.3% | +4.9% | 38% |

**Episodes (последни 5 от 8):**
- `2024-07-01 → 2024-07-01` (1d)
- `2024-11-13 → 2024-11-13` (1d)
- `2024-12-18 → 2025-02-24` (44d)
- `2025-03-12 → 2025-10-09` (128d)
- `2025-11-03 → 2026-09-16` (211d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-09-16

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 10 · **Total matching days:** 97 · **History:** 2021-05-17 → 2026-09-16

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 10 | -0.3% | -0.1% | -7.2% | +7.8% | 50% |
| **SPY** | 3m | 10 | +1.5% | -0.1% | -8.3% | +11.6% | 50% |
| **SPY** | 6m | 10 | +0.8% | +2.5% | -20.8% | +14.2% | 60% |
| **USO** | 1m | 10 | +4.5% | +0.5% | -15.0% | +52.9% | 50% |
| **USO** | 3m | 10 | +10.5% | +10.9% | -20.7% | +52.2% | 60% |
| **USO** | 6m | 10 | +12.5% | +7.6% | -27.6% | +56.3% | 60% |
| **GLD** | 1m | 10 | -0.9% | -1.4% | -8.3% | +11.7% | 20% |
| **GLD** | 3m | 10 | -1.0% | -0.5% | -12.0% | +6.4% | 50% |
| **GLD** | 6m | 10 | -0.2% | -1.0% | -15.2% | +25.0% | 40% |
| **TLT** | 1m | 10 | -2.0% | -2.1% | -6.0% | +2.5% | 10% |
| **TLT** | 3m | 10 | -6.0% | -4.9% | -17.6% | +4.2% | 20% |
| **TLT** | 6m | 10 | -9.5% | -8.1% | -22.3% | +1.2% | 10% |

**Episodes (последни 5 от 10):**
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-05-19` (36d)
- `2026-07-22 → 2026-08-03` (8d)
- `2026-09-01 → 2026-09-16` (11d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 17 · **Total matching days:** 294 · **History:** 2021-05-17 → 2026-09-16

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 17 | +1.9% | +1.6% | -4.8% | +9.0% | 71% |
| **SPY** | 3m | 17 | +3.0% | +4.2% | -12.6% | +16.2% | 71% |
| **SPY** | 6m | 17 | +6.2% | +6.4% | -14.0% | +21.0% | 76% |
| **USO** | 1m | 17 | +2.4% | -2.2% | -13.0% | +22.9% | 41% |
| **USO** | 3m | 17 | +3.8% | -0.8% | -14.5% | +32.4% | 41% |
| **USO** | 6m | 17 | +14.4% | +2.6% | -12.4% | +87.1% | 71% |
| **GLD** | 1m | 17 | +2.4% | +2.1% | -5.6% | +9.0% | 76% |
| **GLD** | 3m | 17 | +5.8% | +7.2% | -16.8% | +23.6% | 65% |
| **GLD** | 6m | 17 | +10.5% | +9.8% | -11.4% | +43.8% | 71% |
| **TLT** | 1m | 17 | +0.3% | -0.0% | -6.3% | +8.2% | 47% |
| **TLT** | 3m | 17 | -1.6% | -1.7% | -15.3% | +11.9% | 35% |
| **TLT** | 6m | 17 | -4.6% | -2.3% | -21.3% | +7.0% | 35% |

**Episodes (последни 5 от 17):**
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)
- `2026-08-07 → 2026-09-03` (19d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 19 · **Total matching days:** 288 · **History:** 2021-05-17 → 2026-09-16

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 19 | +0.4% | +1.0% | -8.7% | +7.0% | 53% |
| **SPY** | 3m | 19 | +2.1% | +3.6% | -13.7% | +9.1% | 68% |
| **SPY** | 6m | 19 | +3.2% | +6.8% | -16.4% | +16.9% | 74% |
| **USO** | 1m | 19 | -0.6% | -5.6% | -21.8% | +55.8% | 42% |
| **USO** | 3m | 19 | +3.9% | -0.6% | -12.7% | +64.3% | 47% |
| **USO** | 6m | 19 | +9.4% | +5.0% | -16.0% | +75.1% | 53% |
| **GLD** | 1m | 19 | -0.6% | -0.1% | -12.4% | +7.6% | 47% |
| **GLD** | 3m | 19 | +1.9% | +1.7% | -13.7% | +19.0% | 68% |
| **GLD** | 6m | 19 | +7.9% | +6.0% | -15.8% | +55.5% | 68% |
| **TLT** | 1m | 19 | -0.2% | -0.1% | -5.6% | +5.2% | 47% |
| **TLT** | 3m | 19 | -3.6% | -4.4% | -17.3% | +8.7% | 32% |
| **TLT** | 6m | 19 | -6.9% | -7.4% | -21.4% | +4.6% | 21% |

**Episodes (последни 5 от 19):**
- `2025-05-12 → 2025-05-19` (3d)
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (13d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-09-16

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (9 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 5 | 2.73 | 2.75 | 2026-08-15 00:00:00 | 2026-09-12 00:00:00 | ✓ |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | 5 | 2.52 | 2.70 | 2026-08-15 00:00:00 | 2026-09-12 00:00:00 | ✓ |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 4 | 2.27 | 2.30 | 2026-08-15 00:00:00 | 2026-09-12 00:00:00 | - |
| **COMPUTSA** | Завършени жилища (SAAR) | growth | housing_supply | 4 | 2.06 | 2.06 | 2026-08-22 00:00:00 | 2026-09-12 00:00:00 | - |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | 3 | 2.22 | 2.22 | 2026-08-15 00:00:00 | 2026-08-29 00:00:00 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 2 | 2.16 | 2.16 | 2026-08-15 00:00:00 | 2026-08-22 00:00:00 | - |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | 2 | 2.09 | 2.09 | 2026-08-15 00:00:00 | 2026-08-22 00:00:00 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | 2 | 2.02 | 2.02 | 2026-09-05 00:00:00 | 2026-09-12 00:00:00 | ✓ |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 1 | 2.28 | 2.28 | 2026-08-15 00:00:00 | 2026-08-15 00:00:00 | ✓ |

### EU (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.27 | 5.28 | 2026-08-15 00:00:00 | 2026-09-12 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.18 | 2.18 | 2026-08-15 00:00:00 | 2026-09-12 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.16 | 2.17 | 2026-08-15 00:00:00 | 2026-09-12 00:00:00 | ✓ |

### CN (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 9 | 2.55 | 2.55 | 2026-08-17 00:00:00 | 2026-09-14 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 9 | 2.22 | 2.23 | 2026-08-17 00:00:00 | 2026-09-14 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 4 | 2.19 | 2.19 | 2026-08-22 00:00:00 | 2026-09-14 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-09-12 00:00:00 · **Generated:** 2026-09-12 07:10:04.385767+00:00

**Режим:** `transition` (Преходно / смесено)  
**Primary driver:** `none`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 37.7 | contracting | 29.6% | 3 | 2 |
| **growth** | 46.3 | mixed | 44.0% | 1 | 0 |
| **inflation** | 40.9 | mixed | 38.9% | 1 | 1 |
| **liquidity** | 52.2 | mixed | 42.1% | 0 | 0 |

### Top anomalies (5 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.75 | down | 93.45 | 2026-04-01 | ✓ min |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | -2.25 | down | 2.30 | 2026-06-01 | - |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | -2.25 | down | 61.60 | 2026-08-01 | - |
| **COMPUTSA** | Завършени жилища (SAAR) | growth, housing | housing_supply | -2.06 | down | -16.76 | 2026-07-01 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | -2.02 | down | 1.90 | 2026-07-01 | ✓ min |

### Narrative hints от макро лещите
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **HPIPONM226S**: Monthly FHFA версия. Само purchase transactions (без refi appraisals). По-чист от refi-bias.
- **CIVPART**: Структурни сдвигове (демография, ранно пенсиониране). Пост-COVID не се възстанови напълно.
- **COMPUTSA**: Завършва construction pipeline (12-18m след starts). Превишение спрямо sales = inventory build.
- **JTSQUR**: Работническа увереност. Ако quits rate пада — хората задържат работата си (pre-recession pattern).

### Cross-lens divergences (6 entries)
- 🔔 **?**
  - `pair_id`: stagflation_test
  - `name_bg`: Labor tightness × Inflation pressure
  - `question_bg`: Дали labor tightness потвърждава inflation pressure (стагфлация)?
  - `state`: transition
  - `interpretation`: Transition — signals not aligned; watch next releases.
  - `slot_a_label`: Labor tightness
  - `slot_b_label`: Inflation pressure
  - `breadth_a`: 0.2
  - `breadth_b`: 0.5
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.7
  - `breadth_b_raw`: 1.0
- 🔔 **?**
  - `pair_id`: growth_labor_lead_lag
  - `name_bg`: Hard activity × Labor claims
  - `question_bg`: Дали hard activity и labor market следват едно тенденция?
  - `state`: a_down_b_up
  - `interpretation`: Activity cools, labor stable — late-cycle decoupling.
  - `slot_a_label`: Hard activity
  - `slot_b_label`: Labor market (claims inverted)
  - `breadth_a`: 0.2
  - `breadth_b`: 1.0
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.8
  - `breadth_b_raw`: 1.0
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Realized CPI × Expectations
  - `question_bg`: Дали expectations следват realized inflation, или стоят anchored?
  - `state`: transition
  - `interpretation`: Monitoring.
  - `slot_a_label`: Realized inflation
  - `slot_b_label`: Inflation expectations
  - `breadth_a`: 0.5
  - `breadth_b`: 0.0
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.0
- 🔔 **?**
  - `pair_id`: credit_policy_transmission
  - `name_bg`: Credit spreads × Policy rates
  - `question_bg`: Дали credit следва policy направление — transmission intact?
  - `state`: a_down_b_up
  - `interpretation`: Benign credit despite tightening — liquidity cushion intact.
  - `slot_a_label`: Credit stress
  - `slot_b_label`: Policy tightening
  - `breadth_a`: 0.0
  - `breadth_b`: 0.667
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.0
  - `breadth_b_raw`: 0.667
- 🔔 **?**
  - `pair_id`: sentiment_vs_hard_data
  - `name_bg`: Consumer sentiment × Hard activity
  - `question_bg`: Дали sentiment потвърждава hard data, или има разминаване?
  - `state`: a_up_b_down
  - `interpretation`: Sentiment ahead of data — watch for confirmation.
  - `slot_a_label`: Consumer sentiment
  - `slot_b_label`: Hard activity
  - `breadth_a`: 0.667
  - `breadth_b`: 0.2
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.667
  - `breadth_b_raw`: 0.8
- 🔔 **?**
  - `pair_id`: model_vs_market
  - `name_bg`: Model-implied × Market-implied inflation
  - `question_bg`: Дали underlying persistence и market pricing-а са съгласни за инфлацията?
  - `state`: both_down
  - `interpretation`: Съгласие — disinflation confirmation. Converging view.
  - `slot_a_label`: Модел (sticky inflation)
  - `slot_b_label`: Пазар (breakevens + survey)
  - `breadth_a`: 0.0
  - `breadth_b`: 0.0
  - `state_raw`: both_down
  - `breadth_a_raw`: 0.0
  - `breadth_b_raw`: 0.0

### Executive narrative
> Сигналите са в преход — няма доминираща конфигурация. Следващите 2-3 релиза ще ориентират посоката. Най-отклонена леща: Растеж и активност — breadth 61% (смесено), 1 аномалии, 0 нови екстремума. За наблюдение следващия релиз: LABOR_SHARE_NBS, JTSQUR (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: LABOR_SHARE_NBS z=-2.75 · NEW-5Y-MIN
- 2 нови екстремуми в top-5 (lookback 5г.)
- Активни двойки: Growth × Labor=a_down_b_up; Credit × Policy=a_down_b_up; Sentiment × Hard=a_up_b_down



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-09-12 00:00:00 · **Generated:** 2026-09-12 07:21:02.940739+00:00

**Режим:** `disinflation_cooling` (Дезинфлация и охлаждане)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 41.7 | mixed | 42.9% | 0 | 0 |
| **growth** | 42.6 | mixed | 25.0% | 0 | 0 |
| **inflation** | 49.6 | mixed | 42.9% | 0 | 0 |
| **credit** | 42.9 | mixed | 36.8% | 3 | 2 |
| **external** | 34.3 | contracting | 16.7% | 0 | 0 |

### Top anomalies (3 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | +5.28 | up | 2.92 | 2026-08-01 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | +2.18 | up | 4.00 | 2026-08-01 | ✓ max |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | +2.14 | up | 3.19 | 2026-08-01 | ✓ max |

### Narrative hints от макро лещите
- **EA_BUND_2Y**: EA-aggregate 2Y yield. Curve slope (10Y-2Y) проксира policy expectations и recession risk.
- **FR_10Y**: France sovereign yield — компонент на OAT-Bund spread. Core-but-not-DE EA stress indicator.
- **DE_10Y**: Germany 10Y, Maastricht-criterion measure. Reference за BTP-Bund / OAT-Bund spread изчисления.

### Cross-lens divergences (7 entries)
- 🔔 **?**
  - `pair_id`: stagflation_test
  - `name_bg`: Стагфлационен тест
  - `question_bg`: Заплатите ли движат услугите нагоре?
  - `state`: both_down
  - `interpretation`: Дезинфлация broad-based: и заплати, и базова отстъпват. ЕЦБ има пространство за политика.
  - `slot_a_label`: Натиск от заплати
  - `slot_b_label`: Базова/услуги инфлация
  - `breadth_a`: 0.0
  - `breadth_b`: 0.0
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.0
- 🔔 **?**
  - `pair_id`: ecb_transmission
  - `name_bg`: Трансмисия на ЕЦБ политиката
  - `question_bg`: ЕЦБ hike-овете стигат ли до банковото кредитиране?
  - `state`: a_up_b_down
  - `interpretation`: ECB hike-ва, но lending не се свива — transmission lag или счупен. Risk: real economy не отчита restrictive stance.
  - `slot_a_label`: Политика (реална лихва + баланс)
  - `slot_b_label`: Банково кредитиране (свиване)
  - `breadth_a`: 1.0
  - `breadth_b`: 0.0
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.0
- 🔔 **?**
  - `pair_id`: fragmentation_risk
  - `name_bg`: Фрагментационен риск
  - `question_bg`: ЕЦБ hike-овете разширяват ли периферните spreads?
  - `state`: a_up_b_down
  - `interpretation`: Hike-ове + сжимащи се spreads — smooth transmission, credible policy.
  - `slot_a_label`: Политика (реална лихва + баланс)
  - `slot_b_label`: Sovereign spreads (BTP/OAT-Bund)
  - `breadth_a`: 1.0
  - `breadth_b`: 0.2
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.2
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Закотвеност на инфлационните очаквания
  - `question_bg`: Headline отскача — очакванията остават ли закотвени?
  - `state`: insufficient_data
  - `interpretation`: Insufficient data в една от двете групи.
  - `slot_a_label`: Реализирана headline инфлация
  - `slot_b_label`: SPF дългосрочни очаквания
  - `breadth_a`: 0.667
  - `breadth_b`: None
  - `state_raw`: insufficient_data
  - `breadth_a_raw`: 0.667
  - `breadth_b_raw`: None
- 🔔 **?**
  - `pair_id`: pipeline_inflation
  - `name_bg`: Pipeline инфлация
  - `question_bg`: PPI води ли core inflation?
  - `state`: insufficient_data
  - `interpretation`: Insufficient data в една от двете групи.
  - `slot_a_label`: PPI междинни стоки
  - `slot_b_label`: Core инфлация (HICP)
  - `breadth_a`: None
  - `breadth_b`: 0.0
  - `state_raw`: insufficient_data
  - `breadth_a_raw`: None
  - `breadth_b_raw`: 0.0
- 🔔 **?**
  - `pair_id`: sentiment_vs_hard_data
  - `name_bg`: Очаквания срещу твърди данни
  - `question_bg`: Sentiment отразява ли реалната икономика?
  - `state`: transition
  - `interpretation`: Sentiment turn обикновено leads hard data 3-6mo.
  - `slot_a_label`: Sentiment (ESI, confidence)
  - `slot_b_label`: Hard activity (IP, retail, GDP)
  - `breadth_a`: 0.778
  - `breadth_b`: 0.5
  - `state_raw`: transition
  - `breadth_a_raw`: 0.778
  - `breadth_b_raw`: 0.5
- 🔔 **?**
  - `pair_id`: growth_labor_lead_lag
  - `name_bg`: Растеж срещу труд (lead-lag)
  - `question_bg`: Активността и пазарът на труда движат ли се заедно?
  - `state`: transition
  - `interpretation`: Смесена картина — изчакай alignment на двата блока.
  - `slot_a_label`: Твърда активност (IP, retail, GDP)
  - `slot_b_label`: Пазар на труда (сила)
  - `breadth_a`: 0.5
  - `breadth_b`: 0.5
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 0.75

### Executive narrative
> Синхронно охлаждане — labor и инфлация отстъпват заедно. Рискът се мести към overshooting, ако claims ускорят. Най-отклонена леща: Финансови условия, кредит и спредове — breadth 80% (разширяване), 3 аномалии, 2 нови екстремума. За наблюдение следващия релиз: FR_10Y, DE_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.28
- 2 нови екстремуми в top-3 (lookback 5г.)
- Активни двойки: Stagflation test=both_down; ecb_transmission=a_up_b_down; fragmentation_risk=a_up_b_down



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-09-14 00:00:00 · **Generated:** 2026-09-14 11:05:27.432797+00:00

**Режим:** `recessionary` (РЕЦЕСИОНЕН)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 28.7 | contracting | -% | - | - |
| **inflation** | 45.6 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 46.9 | mixed | -% | - | - |
| **property** | 28.6 | contracting | -% | - | - |

### Top anomalies (3 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | -2.55 | down | 3.00 | 2026-08-20 | ✓ min |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | +2.23 | up | 15.79 | 2025-12-31 | ✓ max |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | -2.19 | down | 1.72 | 2026-07-31 | - |

### Narrative hints от макро лещите
- **CN_LPR_1Y**: Замества benchmark lending rate от 2019. Главен policy signal.
- **CN_YOUTH_UNEMPLOYMENT**: Рекорд 21.3% юни 2023. НБС спря публикуването за 6 месеца. Структурен проблем — образователна система произвежда повече дипломирани, отколкото пазарът може да абсорбира.
- **CN_CGB_10Y**: Sovereign benchmark. CGB-UST 10Y spread = capital flow incentive.

### Cross-lens divergences (3 entries)
- 🔔 **?**
  - `pair_id`: credit_real_economy
  - `name_bg`: Кредитна експанзия × Реален сектор
  - `question_bg`: Превръща ли се кредитът в реална инвестиция, или ликвидността засяда (debt-deflation)?
  - `state`: transition
  - `interpretation`: Преход — кредит и реален сектор не са ясно aligned; чакай следващ TSF/FAI print.
  - `slot_a_label`: Кредитна експанзия
  - `slot_b_label`: Имоти и инвестиции
  - `breadth_a`: 0.5
  - `breadth_b`: 0.45
- 🔔 **?**
  - `pair_id`: monetary_inflation_trap
  - `name_bg`: Монетарно разхлабване × Инфлация
  - `question_bg`: Води ли разхлабването на PBoC до инфлация, или политиката бута в дефлация (policy trap)?
  - `state`: transition
  - `interpretation`: Преход — посоките на политиката и инфлацията не са ясно aligned.
  - `slot_a_label`: Монетарно разхлабване
  - `slot_b_label`: Инфлация
  - `breadth_a`: 1.0
  - `breadth_b`: 0.5
- 🔔 **?**
  - `pair_id`: external_domestic_balance
  - `name_bg`: Външно търсене × Вътрешна активност
  - `question_bg`: Балансиран ли е растежът, или Китай зависи от износа при слабо вътрешно търсене?
  - `state`: a_up_b_down
  - `interpretation`: Export-dependence — износът носи растежа, докато вътрешното търсене е слабо. Небалансирано възстановяване, уязвимо на тарифи/външни шокове.
  - `slot_a_label`: Външно търсене
  - `slot_b_label`: Вътрешна активност
  - `breadth_a`: 0.833
  - `breadth_b`: 0.333

### Executive narrative
> Претеглен композитен macro score 34.8/100 → режим „РЕЦЕСИОНЕН“ (5/5 лещи). 5 лещи, 3 flagged аномалии (3 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-09-11 |
| `as_of` | 2026-09-11 |
| `regime` | GROWTH |
| `alignment_score` | 4.0 |
| `gms_score` | 4.0 |
| `gms_max` | 8 |
| `gms_tier` | MEDIUM |
| `ks_status` | inactive |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-09-11 → 2026-09-16)

**stable_winner (1m):** +6 entered, -8 exited
  - **Entered:** AEP, INCY, IVZ, NEE, STLD, VLO
  - **Exited:** CAH, CIEN, FIX, GEV, JNJ, TPR, VTR, WBD

**stable_winner (3m):** +2 entered, -3 exited
  - **Entered:** BG, WDC
  - **Exited:** CAT, PNC, WBD

**quality_dip (1m):** +9 entered, -7 exited
  - **Entered:** CAH, CIEN, F, FIX, GEV, JNJ, TPR, VTR, WBD
  - **Exited:** AEP, INCY, IVZ, NEE, STLD, TSLA, VLO

**quality_dip (3m):** +4 entered, -3 exited
  - **Entered:** CAT, F, PNC, WBD
  - **Exited:** BG, TSLA, WDC

**faded_bounce (1m):** +6 entered, -4 exited
  - **Entered:** BSX, CPRT, ISRG, LEN, MKC, ZTS _(включително 1 за първи път в историята: ISRG)_
  - **Exited:** CHTR, EOG, EXE, VLTO

**faded_bounce (3m):** +3 entered, -4 exited
  - **Entered:** CPB, PODD, POOL
  - **Exited:** CHTR, SHW, STZ, TPL

### EU (period: 2026-09-11 → 2026-09-16)

**stable_winner (1m):** +12 entered, -12 exited
  - **Entered:** ABN.AS, ACLN.SW, AVOL.SW, CA.PA, EMG.L, GAW.L, HOC.L, IHG.L, INGA.AS, SAN.MC, SPM.MI, VWS.CO
  - **Exited:** BAMI.MI, BG.VI, CABK.MC, GLEN.L, INCH.L, METSO.HE, MT.AS, NDX1.DE, PKN.WA, RR.L, SDR.L, SUBC.OL

**stable_winner (3m):** +11 entered, -9 exited
  - **Entered:** BBVA.MC, BBY.L, BCP.LS, BEZ.L, BGEO.L, COFB.BR, ISS.CO, JYSK.CO, SAN.MC, UNI.MC, VWS.CO _(включително 1 за първи път в историята: BEZ.L)_
  - **Exited:** AAF.L, AIXA.DE, BPE.MI, MBK.WA, PKN.WA, RR.L, SAND.ST, SUBC.OL, TELIA.ST

**quality_dip (1m):** +11 entered, -12 exited
  - **Entered:** BAMI.MI, BEZ.L, BG.VI, CABK.MC, GLEN.L, ISS.CO, METSO.HE, MT.AS, NDX1.DE, PKN.WA, SDR.L _(включително 1 за първи път в историята: BEZ.L)_
  - **Exited:** ABN.AS, ACLN.SW, AVOL.SW, CA.PA, EMG.L, GAW.L, HOC.L, IHG.L, INGA.AS, SAN.MC, SPM.MI, VWS.CO

**quality_dip (3m):** +7 entered, -10 exited
  - **Entered:** AAF.L, AIXA.DE, BPE.MI, MBK.WA, PKN.WA, SAND.ST, TELIA.ST _(включително 1 за първи път в историята: TELIA.ST)_
  - **Exited:** BBVA.MC, BBY.L, BCP.LS, BGEO.L, COFB.BR, INCH.L, JYSK.CO, SAN.MC, UNI.MC, VWS.CO

**faded_bounce (1m):** +7 entered, -11 exited
  - **Entered:** BWY.L, ICG.L, KRZ.IR, RED.MC, SAGA-B.ST, VPK.AS, WKL.AS _(включително 1 за първи път в историята: BWY.L)_
  - **Exited:** CS.PA, GF.SW, GFC.PA, HNR1.DE, HOLM-B.ST, MUV2.DE, ORSTED.CO, SQN.SW, SREN.SW, TBCG.L, UTG.L

**faded_bounce (3m):** +5 entered, -3 exited
  - **Entered:** ADYEN.AS, BWY.L, LEG.DE, SGO.PA, WKL.AS _(включително 1 за първи път в историята: BWY.L)_
  - **Exited:** ADS.DE, RMS.PA, SQN.SW



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-09-08 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **soymeal** | Commodities | 159558 | 100.0 | 100.0 | 1057 | 87982 |
| **soybeans** | Commodities | 266031 | 100.0 | 100.0 | 1057 | 164669 |
| **corn** | Commodities | 425171 | 99.8 | 99.8 | 1057 | 258401 |
| **cotton** | Commodities | 100170 | 98.7 | 98.7 | 1057 | 27300 |
| **sugar** | Commodities | 247051 | 97.0 | 97.0 | 1057 | 188061 |
| **copper** | Commodities | 82017 | 96.7 | 96.7 | 1057 | 1137 |
| **soyoil** | Commodities | 101768 | 95.7 | 95.7 | 1057 | 20846 |
| **rbob** | Commodities | 92926 | 95.5 | 95.5 | 1057 | 22886 |
| **aud** | FX | 49779 | 82.4 | 82.4 | 1057 | 1238 |
| **dxy** | FX | 6186 | 76.7 | 76.7 | 1057 | 414 |
| **gbpfx** | FX | 34627 | 75.0 | 75.0 | 1057 | -6043 |
| **wheat** | Commodities | 4262 | 67.0 | 67.0 | 1057 | 35663 |
| **vix** | Volatility | -23270 | 64.8 | 64.8 | 1016 | -11143 |
| **gold** | Commodities | 139548 | 61.5 | 61.5 | 1057 | -2320 |
| **coffee** | Commodities | 18080 | 55.2 | 55.2 | 1057 | -6090 |
| **heatingoil** | Commodities | 16004 | 54.2 | 54.2 | 1057 | 1966 |
| **platinum** | Commodities | 9667 | 46.0 | 46.0 | 1057 | 2030 |
| **brent** | Commodities | 5360 | 45.4 | 45.4 | 240 | -2270 |
| **cattle** | Commodities | 47250 | 41.0 | 41.0 | 1057 | -17412 |
| **eurfx** | FX | -33285 | 37.6 | 37.6 | 1057 | 27315 |
| **sp500** | US Equities | -341104 | 37.3 | 37.3 | 1057 | -60658 |
| **wti** | Commodities | 139339 | 36.4 | 36.4 | 1057 | 35624 |
| **silver** | Commodities | 14176 | 35.0 | 35.0 | 1057 | 3864 |
| **jpy** | FX | -49098 | 31.5 | 31.5 | 1057 | 3972 |
| **bitcoin** | Crypto | -7892 | 30.9 | 30.9 | 440 | -840 |
| **nasdaq** | US Equities | -31872 | 23.8 | 23.8 | 1057 | 57253 |
| **us30y** | Rates | -276965 | 21.3 | 21.3 | 1057 | 87859 |
| **natgas** | Commodities | -96677 | 20.3 | 20.3 | 1057 | 13705 |
| **us2y** | Rates | -1290479 | 17.5 | 17.5 | 1057 | 69042 |
| **chf** | FX | -13440 | 15.5 | 15.5 | 1057 | -2008 |
| **cocoa** | Commodities | -11536 | 15.0 | 15.0 | 1057 | 2475 |
| **palladium** | Commodities | -4261 | 13.6 | 13.6 | 1057 | 643 |
| **us5y** | Rates | -2066289 | 12.2 | 12.2 | 1057 | 81455 |
| **cad** | FX | -55448 | 10.4 | 10.4 | 1057 | 36557 |
| **us10y** | Rates | -1938754 | 6.8 | 6.8 | 1057 | 224960 |
| **russell** | US Equities | -110147 | 4.0 | 4.0 | 593 | -14989 |
| **usultra10y** | Rates | -426360 | 2.2 | 2.2 | 547 | -64633 |
| **hogs** | Commodities | -23556 | 1.0 | 1.0 | 1057 | -8435 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **DELL** | Technology | 97.1 | 17.4% | 39.6% | 269.9% | 283.2% | 2.03 | -32.3% |
| 2 | **MRNA** | Healthcare | 97.0 | 125.9% | 162.8% | 170.0% | 169.9% | 1.39 | -34.2% |
| 3 | **VLO** | Energy | 97.0 | 16.2% | 65.8% | 72.4% | 125.0% | 2.53 | -12.1% |
| 4 | **MPC** | Energy | 96.5 | 15.9% | 65.7% | 78.6% | 101.8% | 2.35 | -18.3% |
| 5 | **CRWD** | Technology | 94.7 | 12.8% | 42.1% | 122.9% | 92.4% | 1.33 | -37.2% |
| 6 | **PSX** | Energy | 94.2 | 10.6% | 54.7% | 55.1% | 87.8% | 2.22 | -17.3% |
| 7 | **PANW** | Technology | 93.4 | -0.0% | 34.2% | 122.0% | 86.7% | 1.24 | -36.0% |
| 8 | **CRL** | Healthcare | 93.0 | -4.6% | 48.0% | 77.9% | 88.3% | 1.19 | -33.9% |
| 9 | **HPE** | Technology | 91.3 | -1.6% | 17.2% | 164.0% | 136.8% | 1.43 | -26.4% |
| 10 | **FTNT** | Technology | 90.4 | 10.2% | 16.8% | 106.5% | 92.4% | 1.71 | -14.3% |
| 11 | **NTAP** | Technology | 87.0 | -6.2% | 19.1% | 89.4% | 67.3% | 0.94 | -24.8% |
| 12 | **AMD** | Technology | 86.9 | 1.3% | 1.0% | 161.1% | 214.0% | 1.57 | -27.8% |
| 13 | **RVTY** | Healthcare | 86.8 | 25.4% | 44.0% | 66.9% | 38.6% | 1.31 | -30.1% |
| 14 | **APA** | Energy | 86.4 | 7.7% | 31.7% | 26.6% | 87.8% | 1.43 | -27.7% |
| 15 | **MRK** | Healthcare | 86.3 | 7.2% | 26.6% | 26.7% | 71.7% | 1.89 | -11.4% |
| 16 | **CNC** | Healthcare | 86.2 | 2.5% | 7.5% | 88.9% | 97.3% | 1.37 | -32.7% |
| 17 | **TGT** | Consumer Defensive | 85.4 | 2.4% | 16.8% | 34.8% | 77.4% | 1.81 | -19.6% |
| 18 | **LITE** | Technology | 84.9 | -5.1% | 5.0% | 41.5% | 474.1% | 1.70 | -42.8% |
| 19 | **STT** | Financial Services | 84.7 | -5.2% | 7.3% | 52.2% | 76.6% | 1.88 | -11.8% |
| 20 | **NUE** | Basic Materials | 84.0 | -4.4% | 0.9% | 61.8% | 95.2% | 1.83 | -18.4% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **CCC.L** | Technology | 92.1 | 4.6% | 25.5% | 76.0% | 109.8% | 2.21 | -16.2% |
| 2 | **AKER.OL** | Industrials | 91.7 | 6.2% | 34.5% | 44.1% | 114.9% | 2.51 | -15.6% |
| 3 | **FRO.OL** | Energy | 90.4 | 27.3% | 31.7% | 64.1% | 74.3% | 1.84 | -20.5% |
| 4 | **TKA.DE** | Basic Materials | 90.2 | 9.7% | 37.1% | 87.3% | 70.0% | 1.08 | -41.4% |
| 5 | **RBI.VI** | Financial Services | 89.4 | -0.3% | 15.1% | 71.4% | 120.0% | 2.02 | -18.0% |
| 6 | **MAERSK-B.CO** | Industrials | 88.2 | 12.6% | 47.7% | 46.8% | 57.9% | 1.39 | -22.9% |
| 7 | **REP.MC** | Energy | 87.5 | 8.6% | 41.6% | 23.2% | 95.0% | 2.21 | -20.4% |
| 8 | **ABN.AS** | Financial Services | 86.7 | 4.8% | 16.7% | 62.7% | 67.1% | 1.99 | -18.0% |
| 9 | **PKN.WA** | Energy | 86.5 | 4.2% | 22.6% | 29.9% | 100.4% | 2.16 | -12.3% |
| 10 | **EDEN.PA** | Financial Services | 86.5 | -0.1% | 38.1% | 65.4% | 49.5% | 0.81 | -42.4% |
| 11 | **PKO.WA** | Financial Services | 86.1 | 8.3% | 19.4% | 46.8% | 65.1% | 2.18 | -19.6% |
| 12 | **BGEO.L** | Financial Services | 85.8 | 0.5% | 19.7% | 38.6% | 78.7% | 1.82 | -21.0% |
| 13 | **UNI.MC** | Financial Services | 85.5 | 0.0% | 15.9% | 51.7% | 66.2% | 1.97 | -17.8% |
| 14 | **ROR.L** | Industrials | 85.4 | -0.0% | 55.2% | 57.6% | 42.8% | 0.59 | -25.2% |
| 15 | **UNI.MI** | Financial Services | 84.9 | -3.2% | 14.4% | 48.2% | 70.3% | 1.78 | -11.5% |
| 16 | **BCP.LS** | Financial Services | 84.8 | 7.8% | 15.2% | 53.9% | 59.5% | 2.04 | -17.0% |
| 17 | **MT.AS** | Basic Materials | 84.7 | -0.8% | 9.4% | 40.3% | 121.7% | 1.83 | -26.2% |
| 18 | **EQNR.OL** | Energy | 84.5 | 9.8% | 31.2% | 28.8% | 64.8% | 1.48 | -25.8% |
| 19 | **EBP.WA** | Financial Services | 84.5 | 2.9% | 15.7% | 49.7% | 61.2% | 1.77 | -17.6% |
| 20 | **BBVA.MC** | Financial Services | 84.4 | -0.2% | 15.1% | 41.9% | 63.5% | 1.57 | -18.7% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **EIX** | Utilities | 2.360 | 1.844 | 1.056 | 3.180 | -1.006 | - | 5.7 | +19.7% |
| 2 | **CF** | Materials | 1.550 | 0.858 | 1.295 | 1.745 | 0.540 | - | 9.9 | +29.9% |
| 3 | **NEM** | Materials | 1.540 | 1.197 | 1.714 | 0.946 | 0.523 | - | 15.7 | +25.9% |
| 4 | **SNDK** | Information Technology | 1.540 | 1.876 | 1.562 | 0.499 | -0.182 | - | 21.9 | +91.6% |
| 5 | **APA** | Energy | 1.217 | 1.144 | 1.261 | 0.675 | -0.241 | - | 9.6 | +26.7% |
| 6 | **HST** | Real Estate | 1.206 | 1.335 | 0.482 | 1.341 | -0.260 | - | 14.7 | +15.6% |
| 7 | **MO** | Consumer Staples | 1.201 | -0.334 | 2.061 | 1.081 | -0.426 | - | 14.7 | - |
| 8 | **SYF** | Financials | 1.165 | -0.075 | 1.175 | 1.742 | -0.401 | - | 7.6 | +20.8% |
| 9 | **SPG** | Real Estate | 1.133 | 0.795 | 1.393 | 0.631 | -1.403 | - | 14.4 | +120.5% |
| 10 | **BMY** | Health Care | 1.098 | 0.874 | 0.876 | 1.044 | 0.571 | - | 13.8 | +46.6% |
| 11 | **EXPE** | Consumer Discretionary | 1.026 | 1.535 | 0.801 | 0.346 | -0.664 | - | 17.9 | +89.5% |
| 12 | **MU** | Information Technology | 1.008 | 1.639 | 0.910 | 0.083 | -0.582 | - | 22.1 | +66.6% |
| 13 | **MAS** | Industrials | 0.995 | -0.501 | 1.460 | 1.378 | -0.804 | - | 15.7 | +5862.5% |
| 14 | **TPR** | Consumer Discretionary | 0.980 | 0.750 | 1.156 | 0.545 | -1.011 | - | 16.0 | +197.1% |
| 15 | **ALL** | Financials | 0.958 | 0.920 | 0.424 | 1.150 | 1.197 | - | 5.0 | +46.1% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -1.885 | -1.365 | -0.928 | -2.519 | -1.042 |
| 502 | **TSLA** | Consumer Discretionary | -1.822 | -0.715 | -1.372 | -2.452 | -0.366 |
| 501 | **COIN** | Financials | -1.736 | -2.782 | -1.696 | 0.000 | -1.719 |
| 500 | **CSGP** | Real Estate | -1.582 | -3.161 | -0.465 | -0.635 | 0.677 |
| 499 | **KKR** | Financials | -1.559 | -1.518 | -0.847 | -1.639 | -0.870 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W38.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W38.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-09-14  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
