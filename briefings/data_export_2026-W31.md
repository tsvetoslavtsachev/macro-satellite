# Сателит — пълен data export за 2026-W31

_Период: 2026-07-27 → 2026-08-02_  
_Генериран: 2026-07-31 08:51 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W31.md` (structured briefing) и `narrative_2026-W31.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**8 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **UUP** | -1.54% | -2.66σ | 28.58 | 28.14 | 2026-07-24 | 2026-07-30 | +0.30% | +0.69% | 13 |
| **XLI** | -2.34% | -2.46σ | 182.66 | 178.39 | 2026-07-24 | 2026-07-30 | +0.45% | +1.13% | 13 |
| **XLU** | -3.52% | -1.75σ | 46.29 | 44.66 | 2026-07-24 | 2026-07-30 | +0.04% | +2.04% | 13 |
| **DBA** | -2.69% | -1.71σ | 28.24 | 27.48 | 2026-07-24 | 2026-07-30 | +0.25% | +1.72% | 13 |
| **EFA** | +2.74% | +1.60σ | 103.41 | 106.24 | 2026-07-24 | 2026-07-30 | +0.14% | +1.62% | 13 |
| **XLY** | +2.72% | +1.32σ | 109.41 | 112.39 | 2026-07-24 | 2026-07-30 | -0.59% | +2.51% | 13 |
| **GLD** | +1.41% | +1.18σ | 371.90 | 377.16 | 2026-07-24 | 2026-07-30 | -1.14% | +2.17% | 13 |
| **SHY** | +0.20% | +1.06σ | 81.85 | 82.01 | 2026-07-24 | 2026-07-30 | -0.07% | +0.25% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-08-02 · **Conditions matched:** 1/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | -6.74% | ❌ | 136.69 | 127.48 | 2026-07-24 | 2026-07-30 |
| DFEN | down ≥ 3.0% | -3.47% | ✅ | 76.41 | 73.76 | 2026-07-24 | 2026-07-30 |
| GLD | down ≥ 1.0% | +1.41% | ❌ | 371.90 | 377.16 | 2026-07-24 | 2026-07-30 |
| URA | down ≥ 3.0% | -0.43% | ❌ | 39.89 | 39.72 | 2026-07-24 | 2026-07-30 |
| UUP | up ≥ 0.5% | -1.54% | ❌ | 28.58 | 28.14 | 2026-07-24 | 2026-07-30 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-08-02 · **Conditions matched:** 2/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | +0.49% | ❌ | 291.17 | 292.59 | 2026-07-24 | 2026-07-30 |
| XLF | up ≥ 1.0% | +1.23% | ✅ | 56.31 | 57.00 | 2026-07-24 | 2026-07-30 |
| XLY | up ≥ 1.0% | +2.72% | ✅ | 109.41 | 112.39 | 2026-07-24 | 2026-07-30 |
| GLD | down ≥ 0.5% | +1.41% | ❌ | 371.90 | 377.16 | 2026-07-24 | 2026-07-30 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2024-W42 (week ending 2024-10-20)
**Cosine similarity:** 0.9251 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.98% | +2.22% | -9.95% |
| **USO** | +1.30% | +15.61% | -2.66% |
| **GLD** | -3.19% | -0.80% | +21.83% |
| **TLT** | -3.38% | -7.12% | -6.75% |
| **XLE** | +5.58% | +4.01% | -9.79% |
| **IWM** | +2.21% | -0.08% | -17.36% |

### Паралел #2: 2023-W52 (week ending 2023-12-31)
**Cosine similarity:** 0.9159 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.28% | +10.05% | +14.50% |
| **USO** | +9.24% | +18.12% | +19.41% |
| **GLD** | -1.35% | +7.61% | +12.47% |
| **TLT** | -3.20% | -4.31% | -7.18% |
| **XLE** | +1.38% | +12.61% | +8.72% |
| **IWM** | -1.49% | +4.78% | +1.09% |

### Паралел #3: 2025-W40 (week ending 2025-10-05)
**Cosine similarity:** 0.8615 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.90% | +2.09% | -2.00% |
| **USO** | +0.31% | -3.83% | +92.33% |
| **GLD** | +1.31% | +11.36% | +20.07% |
| **TLT** | +0.63% | -2.63% | -2.90% |
| **XLE** | -1.93% | +2.69% | +33.28% |
| **IWM** | -1.88% | +1.20% | +2.22% |

### Паралел #4: 2024-W05 (week ending 2024-02-04)
**Cosine similarity:** 0.8593 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.60% | +3.43% | +7.80% |
| **USO** | +8.80% | +11.29% | +8.71% |
| **GLD** | +4.55% | +12.91% | +19.47% |
| **TLT** | -0.67% | -6.48% | +2.30% |
| **XLE** | +3.99% | +10.84% | +5.84% |
| **IWM** | +4.79% | +3.85% | +7.46% |

### Паралел #5: 2025-W50 (week ending 2025-12-14)
**Cosine similarity:** 0.8515 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.76% | -2.86% | +8.80% |
| **USO** | +6.79% | +74.23% | +82.28% |
| **GLD** | +6.62% | +16.54% | -2.25% |
| **TLT** | +0.55% | -0.92% | -1.80% |
| **XLE** | +3.27% | +26.79% | +26.46% |
| **IWM** | +2.95% | -2.86% | +15.40% |

### Паралел #6: 2023-W16 (week ending 2023-04-23)
**Cosine similarity:** 0.8510 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.46% | +9.70% | +2.18% |
| **USO** | -4.90% | +1.14% | +18.31% |
| **GLD** | -0.45% | -1.12% | -0.36% |
| **TLT** | -3.23% | -2.56% | -20.27% |
| **XLE** | -5.67% | -0.80% | +6.21% |
| **IWM** | -0.08% | +9.52% | -6.26% |

### Паралел #7: 2026-W15 (week ending 2026-04-12)
**Cosine similarity:** 0.8346 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +8.64% | +11.11% | +9.16% |
| **USO** | +15.61% | -12.91% | +2.13% |
| **GLD** | -0.96% | -13.75% | -13.72% |
| **TLT** | -1.73% | -2.34% | -4.27% |
| **XLE** | +1.11% | -3.27% | +3.55% |
| **IWM** | +8.14% | +13.28% | +11.97% |

### Паралел #8: 2025-W26 (week ending 2025-06-29)
**Cosine similarity:** 0.8195 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.31% | +7.63% | +12.26% |
| **USO** | +8.90% | +5.10% | -6.55% |
| **GLD** | +1.67% | +15.11% | +38.35% |
| **TLT** | -0.08% | +1.73% | +0.40% |
| **XLE** | +4.28% | +7.84% | +3.63% |
| **IWM** | +3.35% | +12.00% | +16.68% |

### Паралел #9: 2024-W39 (week ending 2024-09-29)
**Cosine similarity:** 0.8103 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.80% | +4.12% | -2.77% |
| **USO** | -0.87% | +5.09% | +6.40% |
| **GLD** | +4.52% | -1.48% | +15.93% |
| **TLT** | -6.63% | -11.64% | -8.55% |
| **XLE** | +0.75% | -3.02% | +6.01% |
| **IWM** | +0.64% | +0.93% | -9.02% |

### Паралел #10: 2022-W31 (week ending 2022-08-07)
**Cosine similarity:** 0.7938 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -5.49% | -8.98% | -0.27% |
| **USO** | -0.17% | +7.38% | -9.98% |
| **GLD** | -4.21% | -5.34% | +4.94% |
| **TLT** | -7.71% | -19.10% | -8.39% |
| **XLE** | +8.40% | +25.10% | +17.62% |
| **IWM** | -6.55% | -6.35% | +3.24% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 14 · **Total matching days:** 72 · **History:** 2021-05-17 → 2026-07-30

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 14 | +1.9% | +1.3% | -3.1% | +7.4% | 64% |
| **SPY** | 3m | 14 | +2.6% | +2.5% | -7.3% | +12.0% | 71% |
| **SPY** | 6m | 14 | +7.0% | +9.8% | -6.8% | +21.8% | 71% |
| **USO** | 1m | 14 | +0.6% | +0.3% | -14.3% | +12.7% | 50% |
| **USO** | 3m | 14 | -1.8% | -2.0% | -18.9% | +24.5% | 50% |
| **USO** | 6m | 14 | +10.9% | +1.4% | -15.4% | +109.4% | 57% |
| **GLD** | 1m | 14 | +2.6% | +1.6% | -0.9% | +8.9% | 79% |
| **GLD** | 3m | 14 | +5.4% | +4.5% | -12.6% | +24.5% | 71% |
| **GLD** | 6m | 14 | +5.8% | +7.4% | -15.2% | +25.3% | 71% |
| **TLT** | 1m | 14 | -1.4% | -1.1% | -6.7% | +3.6% | 36% |
| **TLT** | 3m | 14 | -0.6% | -0.1% | -16.5% | +11.1% | 50% |
| **TLT** | 6m | 14 | -4.1% | -2.9% | -18.0% | +7.5% | 29% |

**Episodes (последни 5 от 14):**
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-07-21` (3d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 59 · **History:** 2021-05-17 → 2026-07-30

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +3.9% | +3.9% | -1.3% | +9.1% | 50% |
| **SPY** | 3m | 2 | +4.5% | +4.5% | -1.3% | +10.3% | 50% |
| **SPY** | 6m | 2 | +4.2% | +4.2% | -1.3% | +9.7% | 50% |
| **USO** | 1m | 2 | +6.7% | +6.7% | +6.1% | +7.2% | 100% |
| **USO** | 3m | 2 | -1.9% | -1.9% | -9.9% | +6.1% | 50% |
| **USO** | 6m | 2 | +4.2% | +4.2% | +2.3% | +6.1% | 100% |
| **GLD** | 1m | 2 | +0.6% | +0.6% | -0.2% | +1.3% | 50% |
| **GLD** | 3m | 2 | -6.2% | -6.2% | -13.8% | +1.3% | 50% |
| **GLD** | 6m | 2 | -5.9% | -5.9% | -13.2% | +1.3% | 50% |
| **TLT** | 1m | 2 | -1.2% | -1.2% | -1.5% | -1.0% | 0% |
| **TLT** | 3m | 2 | -2.2% | -2.2% | -2.9% | -1.5% | 0% |
| **TLT** | 6m | 2 | -3.1% | -3.1% | -4.7% | -1.5% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-07-30` (12d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 410 · **History:** 2021-05-17 → 2026-07-30

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
- `2025-11-03 → 2026-07-30` (178d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-07-30

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 9 · **Total matching days:** 84 · **History:** 2021-05-17 → 2026-07-30

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 9 | -0.5% | -0.8% | -7.2% | +7.8% | 44% |
| **SPY** | 3m | 9 | +1.6% | -0.8% | -8.3% | +11.6% | 44% |
| **SPY** | 6m | 9 | +0.5% | +4.1% | -20.8% | +14.2% | 56% |
| **USO** | 1m | 9 | +3.2% | -1.7% | -15.0% | +52.9% | 33% |
| **USO** | 3m | 9 | +8.0% | -0.1% | -20.7% | +52.2% | 44% |
| **USO** | 6m | 9 | +8.7% | -0.2% | -27.6% | +45.8% | 44% |
| **GLD** | 1m | 9 | -2.3% | -1.6% | -8.3% | +1.9% | 11% |
| **GLD** | 3m | 9 | -1.4% | -0.5% | -12.0% | +6.4% | 44% |
| **GLD** | 6m | 9 | -0.9% | -0.8% | -19.4% | +25.0% | 33% |
| **TLT** | 1m | 9 | -2.0% | -2.5% | -6.0% | +2.5% | 11% |
| **TLT** | 3m | 9 | -6.2% | -5.7% | -17.6% | +4.2% | 22% |
| **TLT** | 6m | 9 | -10.0% | -7.8% | -22.3% | +1.2% | 11% |

**Episodes (последни 5 от 9):**
- `2023-04-12 → 2023-04-18` (5d)
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-05-19` (36d)
- `2026-07-22 → 2026-07-30` (6d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 16 · **Total matching days:** 275 · **History:** 2021-05-17 → 2026-07-30

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.1% | +1.9% | -4.8% | +9.0% | 75% |
| **SPY** | 3m | 16 | +3.3% | +4.4% | -12.6% | +16.2% | 75% |
| **SPY** | 6m | 16 | +6.7% | +7.6% | -14.0% | +21.0% | 81% |
| **USO** | 1m | 16 | +1.3% | -3.2% | -13.0% | +22.9% | 38% |
| **USO** | 3m | 16 | +2.0% | -1.7% | -14.5% | +29.9% | 38% |
| **USO** | 6m | 16 | +11.8% | +2.3% | -12.4% | +87.1% | 69% |
| **GLD** | 1m | 16 | +2.5% | +1.8% | -5.6% | +9.0% | 75% |
| **GLD** | 3m | 16 | +6.3% | +7.4% | -16.8% | +23.6% | 69% |
| **GLD** | 6m | 16 | +11.0% | +12.1% | -14.7% | +43.8% | 75% |
| **TLT** | 1m | 16 | +0.4% | +0.3% | -6.3% | +8.2% | 50% |
| **TLT** | 3m | 16 | -1.6% | -1.4% | -15.3% | +11.9% | 38% |
| **TLT** | 6m | 16 | -4.6% | -3.3% | -21.3% | +7.0% | 38% |

**Episodes (последни 5 от 16):**
- `2025-03-27 → 2025-05-08` (25d)
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 19 · **Total matching days:** 288 · **History:** 2021-05-17 → 2026-07-30

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 19 | +0.4% | +1.0% | -8.7% | +7.0% | 53% |
| **SPY** | 3m | 19 | +1.9% | +2.7% | -13.7% | +9.1% | 68% |
| **SPY** | 6m | 19 | +3.0% | +6.8% | -16.4% | +16.9% | 74% |
| **USO** | 1m | 19 | -0.6% | -5.6% | -21.8% | +55.8% | 42% |
| **USO** | 3m | 19 | +3.3% | -1.3% | -12.7% | +64.3% | 42% |
| **USO** | 6m | 19 | +8.2% | -4.2% | -16.0% | +75.1% | 47% |
| **GLD** | 1m | 19 | -0.6% | -0.1% | -12.4% | +7.6% | 47% |
| **GLD** | 3m | 19 | +1.5% | +1.3% | -13.7% | +19.0% | 63% |
| **GLD** | 6m | 19 | +7.3% | +6.0% | -20.3% | +55.5% | 68% |
| **TLT** | 1m | 19 | -0.2% | -0.1% | -5.6% | +5.2% | 47% |
| **TLT** | 3m | 19 | -3.6% | -4.4% | -17.3% | +8.7% | 32% |
| **TLT** | 6m | 19 | -6.8% | -7.9% | -21.4% | +4.6% | 21% |

**Episodes (последни 5 от 19):**
- `2025-05-12 → 2025-05-19` (3d)
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (13d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-07-30

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (12 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 5 | 2.59 | 2.89 | 2026-06-27 00:00:00 | 2026-07-25 00:00:00 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 5 | 2.43 | 2.43 | 2026-06-27 00:00:00 | 2026-07-25 00:00:00 | - |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 5 | 2.34 | 2.34 | 2026-06-27 00:00:00 | 2026-07-25 00:00:00 | ✓ |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 5 | 2.28 | 2.28 | 2026-06-27 00:00:00 | 2026-07-25 00:00:00 | ✓ |
| **JTSQUR** | Quits rate — напускания | labor | flow | 5 | 2.02 | 2.02 | 2026-06-27 00:00:00 | 2026-07-25 00:00:00 | ✓ |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | 4 | 2.47 | 2.47 | 2026-07-04 00:00:00 | 2026-07-25 00:00:00 | ✓ |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | 4 | 2.02 | 2.02 | 2026-07-04 00:00:00 | 2026-07-25 00:00:00 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | 3 | 2.58 | 2.58 | 2026-06-27 00:00:00 | 2026-07-11 00:00:00 | - |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 2 | 2.56 | 2.56 | 2026-07-04 00:00:00 | 2026-07-11 00:00:00 | - |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | 2 | 2.28 | 2.28 | 2026-07-18 00:00:00 | 2026-07-25 00:00:00 | ✓ |
| **CSUSHPISA** | Case-Shiller US National HPI (SA) | housing | housing_prices | 2 | 2.17 | 2.17 | 2026-07-04 00:00:00 | 2026-07-11 00:00:00 | - |
| **MSACSR** | Месеци предлагане — нови жилища | housing | housing_affordability | 2 | 2.02 | 2.02 | 2026-06-27 00:00:00 | 2026-07-18 00:00:00 | ✓ |

### EU (6 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.29 | 5.37 | 2026-06-27 00:00:00 | 2026-07-25 00:00:00 | - |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | 5 | 2.59 | 2.66 | 2026-06-27 00:00:00 | 2026-07-25 00:00:00 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation | sentiment | 5 | 2.33 | 2.98 | 2026-06-27 00:00:00 | 2026-07-25 00:00:00 | - |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.20 | 2.27 | 2026-06-27 00:00:00 | 2026-07-25 00:00:00 | ✓ |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.19 | 2.25 | 2026-06-27 00:00:00 | 2026-07-25 00:00:00 | ✓ |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | 2 | 2.38 | 2.38 | 2026-07-18 00:00:00 | 2026-07-25 00:00:00 | - |

### CN (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 8 | 2.56 | 2.56 | 2026-06-29 00:00:00 | 2026-07-27 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 8 | 2.23 | 2.23 | 2026-06-29 00:00:00 | 2026-07-27 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 1 | 2.22 | 2.22 | 2026-07-08 00:00:00 | 2026-07-08 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-07-25 00:00:00 · **Generated:** 2026-07-25 09:02:42.000695+00:00

**Режим:** `soft_landing` (Soft landing)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 37.7 | contracting | 29.6% | 4 | 3 |
| **growth** | 45.0 | mixed | 36.0% | 1 | 1 |
| **inflation** | 40.1 | mixed | 38.9% | 4 | 2 |
| **liquidity** | 51.5 | mixed | 42.1% | 0 | 0 |

### Top anomalies (8 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | -2.47 | down | 61.50 | 2026-06-01 | ✓ min |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | +2.43 | up | 4.80 | 2026-05-01 | - |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.34 | down | 94.99 | 2026-01-01 | ✓ min |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | +2.28 | up | 55.10 | 2026-05-01 | ✓ max |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | -2.28 | down | 0.13 | 2026-06-01 | ✓ min |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | +2.15 | up | 5.51 | 2026-06-01 | - |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | -2.02 | down | 59.00 | 2026-06-01 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | -2.02 | down | 1.90 | 2026-05-01 | ✓ min |

### Narrative hints от макро лещите
- **CIVPART**: Структурни сдвигове (демография, ранно пенсиониране). Пост-COVID не се възстанови напълно.
- **MICH_INFL_1Y**: Household очаквания. По-шумни от market-based, но по-ранни. Extreme movements сигнализират de-anchoring risk.
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **US_PMI_MFG**: Markit mfg — comparable cross-country. ISM е US-only.
- **TRIMMED_MEAN_CPI**: Орязва 8% в опашките (топ и долу). По-стабилна от median при многоизмерен shock.
- **PPIFIS**: Производствени цени → consumer prices с 1-3 месечен lag. Водещ за CPI при трендови промени.
- **EMRATIO**: Не зависи от definition на 'active labor force'. По-стабилен индикатор на дълбоката заетост.
- **JTSQUR**: Работническа увереност. Ако quits rate пада — хората задържат работата си (pre-recession pattern).

### Cross-lens divergences (6 entries)
- 🔔 **?**
  - `pair_id`: stagflation_test
  - `name_bg`: Labor tightness × Inflation pressure
  - `question_bg`: Дали labor tightness потвърждава inflation pressure (стагфлация)?
  - `state`: a_up_b_down
  - `interpretation`: Soft landing — labor tight, но inflation cools. Fed credibility holds.
  - `slot_a_label`: Labor tightness
  - `slot_b_label`: Inflation pressure
  - `breadth_a`: 0.75
  - `breadth_b`: 0.333
  - `state_raw`: transition
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.5
- 🔔 **?**
  - `pair_id`: growth_labor_lead_lag
  - `name_bg`: Hard activity × Labor claims
  - `question_bg`: Дали hard activity и labor market следват едно тенденция?
  - `state`: transition
  - `interpretation`: Mixed — waiting for clarification.
  - `slot_a_label`: Hard activity
  - `slot_b_label`: Labor market (claims inverted)
  - `breadth_a`: 0.4
  - `breadth_b`: 1.0
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.8
  - `breadth_b_raw`: 1.0
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Realized CPI × Expectations
  - `question_bg`: Дали expectations следват realized inflation, или стоят anchored?
  - `state`: a_down_b_up
  - `interpretation`: Rare — expectations rising while realized cools (stagflation fear narrative?).
  - `slot_a_label`: Realized inflation
  - `slot_b_label`: Inflation expectations
  - `breadth_a`: 0.333
  - `breadth_b`: 0.667
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 0.667
- 🔔 **?**
  - `pair_id`: credit_policy_transmission
  - `name_bg`: Credit spreads × Policy rates
  - `question_bg`: Дали credit следва policy направление — transmission intact?
  - `state`: both_up
  - `interpretation`: Tightening transmits — rates up + credit widens.
  - `slot_a_label`: Credit stress
  - `slot_b_label`: Policy tightening
  - `breadth_a`: 1.0
  - `breadth_b`: 0.833
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.833
- 🔔 **?**
  - `pair_id`: sentiment_vs_hard_data
  - `name_bg`: Consumer sentiment × Hard activity
  - `question_bg`: Дали sentiment потвърждава hard data, или има разминаване?
  - `state`: transition
  - `interpretation`: Monitoring — divergence typical в political transitions.
  - `slot_a_label`: Consumer sentiment
  - `slot_b_label`: Hard activity
  - `breadth_a`: 0.0
  - `breadth_b`: 0.4
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.0
  - `breadth_b_raw`: 0.8
- 🔔 **?**
  - `pair_id`: model_vs_market
  - `name_bg`: Model-implied × Market-implied inflation
  - `question_bg`: Дали underlying persistence и market pricing-а са съгласни за инфлацията?
  - `state`: a_down_b_up
  - `interpretation`: Модел cools, пазар pricing-ва inflation — market overestimating; dovish contrarian setup.
  - `slot_a_label`: Модел (sticky inflation)
  - `slot_b_label`: Пазар (breakevens + survey)
  - `breadth_a`: 0.0
  - `breadth_b`: 0.667
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.0
  - `breadth_b_raw`: 0.667

### Executive narrative
> Конфигурацията подкрепя soft landing — labor остава tight, но инфлацията се охлажда. Fed credibility за момента издържа. Най-отклонена леща: Монетарна политика и кредит — breadth 76% (разширяване), 0 аномалии, 0 нови екстремума. За наблюдение следващия релиз: CIVPART, LABOR_SHARE_NBS, US_PMI_MFG (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: CIVPART z=-2.47 · NEW-5Y-MIN
- 5 нови екстремуми в top-8 (lookback 5г.)
- Активни двойки: Stagflation test=a_up_b_down; Inflation anchoring=a_down_b_up; Credit × Policy=both_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-07-25 00:00:00 · **Generated:** 2026-07-25 09:17:24.326676+00:00

**Режим:** `disinflation_cooling` (Дезинфлация и охлаждане)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 34.9 | contracting | 42.9% | 1 | 0 |
| **growth** | 39.9 | mixed | 8.3% | 1 | 0 |
| **inflation** | 47.8 | mixed | 85.7% | 1 | 0 |
| **credit** | 44.8 | mixed | 36.8% | 3 | 0 |
| **external** | 12.0 | contracting | 16.7% | 1 | 0 |

### Top anomalies (6 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | +5.27 | up | 2.72 | 2026-06-01 | - |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | -2.66 | down | -3.80 | 2026-06-01 | - |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | -2.38 | down | -4969.90 | 2026-05-01 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation, growth | sentiment | +2.17 | up | 22.30 | 2026-06-01 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | +2.15 | up | 3.68 | 2026-06-01 | - |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | +2.15 | up | 2.96 | 2026-06-01 | - |

### Narrative hints от макро лещите
- **EA_BUND_2Y**: EA-aggregate 2Y yield. Curve slope (10Y-2Y) проксира policy expectations и recession risk.
- **EA_EMP_EXP_SERVICES**: DG ECFIN survey: forward-looking labor сигнал от услугите (~70% от GDP). Дълга история (от 1996) — за разлика от teibs030 (EA_EMPLOYMENT_EXP, 12m). Същата полярност (higher=better). De-singleton-ва labor_sentiment.
- **EA_TRADE_BALANCE**: Стоковият баланс с третите страни. Срив към дефицит (2022) = енергийната сметка изпреварва износа. Полярност +1.
- **EA_SELLING_PRICE_EXP**: Forward-looking inflation сигнал от business side — мениджърите казват дали ще вдигат цени. Изпреварва HICP с 3-6 месеца.
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
  - `state`: transition
  - `interpretation`: Смесена картина — типично около policy turning points.
  - `slot_a_label`: Политика (реална лихва + баланс)
  - `slot_b_label`: Банково кредитиране (свиване)
  - `breadth_a`: 0.5
  - `breadth_b`: 0.0
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 0.0
- 🔔 **?**
  - `pair_id`: fragmentation_risk
  - `name_bg`: Фрагментационен риск
  - `question_bg`: ЕЦБ hike-овете разширяват ли периферните spreads?
  - `state`: transition
  - `interpretation`: Mixed signals — гледай individual country drivers.
  - `slot_a_label`: Политика (реална лихва + баланс)
  - `slot_b_label`: Sovereign spreads (BTP/OAT-Bund)
  - `breadth_a`: 0.5
  - `breadth_b`: 0.4
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 0.4
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Закотвеност на инфлационните очаквания
  - `question_bg`: Headline отскача — очакванията остават ли закотвени?
  - `state`: insufficient_data
  - `interpretation`: Insufficient data в една от двете групи.
  - `slot_a_label`: Реализирана headline инфлация
  - `slot_b_label`: SPF дългосрочни очаквания
  - `breadth_a`: 0.0
  - `breadth_b`: None
  - `state_raw`: insufficient_data
  - `breadth_a_raw`: 0.0
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
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.778
  - `breadth_b_raw`: 1.0
- 🔔 **?**
  - `pair_id`: growth_labor_lead_lag
  - `name_bg`: Растеж срещу труд (lead-lag)
  - `question_bg`: Активността и пазарът на труда движат ли се заедно?
  - `state`: transition
  - `interpretation`: Смесена картина — изчакай alignment на двата блока.
  - `slot_a_label`: Твърда активност (IP, retail, GDP)
  - `slot_b_label`: Пазар на труда (сила)
  - `breadth_a`: 0.5
  - `breadth_b`: 0.75
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 1.0

### Executive narrative
> Синхронно охлаждане — labor и инфлация отстъпват заедно. Рискът се мести към overshooting, ако claims ускорят. Най-отклонена леща: Инфлация и цени — breadth 0% (свиване), 1 аномалии, 0 нови екстремума. За наблюдение: EA_BUND_2Y (z=+5.27) — най-силното отклонение.

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.27
- Активни двойки: Stagflation test=both_down



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-07-27 00:00:00 · **Generated:** 2026-07-27 09:24:46.729439+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 46.1 | mixed | -% | - | - |
| **inflation** | 45.7 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 49.3 | mixed | -% | - | - |
| **property** | 28.4 | contracting | -% | - | - |

### Top anomalies (2 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | -2.55 | down | 3.00 | 2026-07-20 | ✓ min |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | +2.23 | up | 15.79 | 2025-12-31 | ✓ max |

### Narrative hints от макро лещите
- **CN_LPR_1Y**: Замества benchmark lending rate от 2019. Главен policy signal.
- **CN_YOUTH_UNEMPLOYMENT**: Рекорд 21.3% юни 2023. НБС спря публикуването за 6 месеца. Структурен проблем — образователна система произвежда повече дипломирани, отколкото пазарът може да абсорбира.

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
  - `state`: a_up_b_down
  - `interpretation`: Policy trap — PBoC разхлабва, но инфлацията пада/е в дефлация. Трансмисията е счупена (Japan-style): по-ниските лихви не вдигат цените при deleveraging.
  - `slot_a_label`: Монетарно разхлабване
  - `slot_b_label`: Инфлация
  - `breadth_a`: 1.0
  - `breadth_b`: 0.25
- 🔔 **?**
  - `pair_id`: external_domestic_balance
  - `name_bg`: Външно търсене × Вътрешна активност
  - `question_bg`: Балансиран ли е растежът, или Китай зависи от износа при слабо вътрешно търсене?
  - `state`: both_up
  - `interpretation`: Балансиран растеж — и износ, и вътрешно търсене се разширяват.
  - `slot_a_label`: Външно търсене
  - `slot_b_label`: Вътрешна активност
  - `breadth_a`: 0.667
  - `breadth_b`: 0.667

### Executive narrative
> Претеглен композитен macro score 40.6/100 → режим „ВЛОШАВАЩ СЕ“ (5/5 лещи). 5 лещи, 2 flagged аномалии (4 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-07-24 |
| `as_of` | 2026-07-24 |
| `regime` | REFLATION |
| `alignment_score` | 4.0 |
| `gms_score` | 2.0 |
| `gms_max` | 8 |
| `gms_tier` | LOW |
| `ks_status` | inactive |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-07-24 → 2026-07-29)

**stable_winner (1m):** +9 entered, -8 exited
  - **Entered:** BEN, C, CFG, EBAY, KEY, MRNA, O, PWR, WELL _(включително 2 за първи път в историята: KEY, MRNA)_
  - **Exited:** APA, DLTR, FIX, GS, HOOD, VRT, WDC, WMT

**stable_winner (3m):** +4 entered, -5 exited
  - **Entered:** ADM, MRNA, PWR, VTR
  - **Exited:** FIX, GS, HAL, RL, VRT

**quality_dip (1m):** +8 entered, -9 exited
  - **Entered:** APA, DLTR, FIX, GS, HOOD, VRT, WDC, WMT _(включително 1 за първи път в историята: FIX)_
  - **Exited:** BEN, C, CFG, EBAY, KEY, MRNA, O, PWR, WELL

**quality_dip (3m):** +5 entered, -4 exited
  - **Entered:** FIX, GS, HAL, RL, VRT _(включително 1 за първи път в историята: HAL)_
  - **Exited:** ADM, MRNA, PWR, VTR

**faded_bounce (1m):** +11 entered, -8 exited
  - **Entered:** BKNG, BSX, CI, CMG, CSGP, DASH, ERIE, FDS, FISV, MKC, ZBH _(включително 4 за първи път в историята: BKNG, CI, CSGP, DASH)_
  - **Exited:** BLDR, CTAS, EFX, IT, LEN, PAYX, PEG, VRSK

**faded_bounce (3m):** +6 entered, -4 exited
  - **Entered:** BKNG, CI, DASH, GIS, OTIS, SO _(включително 3 за първи път в историята: BKNG, CI, DASH)_
  - **Exited:** BLDR, CTAS, IT, PEG

### EU (period: 2026-07-24 → 2026-07-29)

**stable_winner (1m):** +7 entered, -9 exited
  - **Entered:** ALLFG.AS, AZM.MI, ENR.DE, KER.PA, SAND.ST, SPM.MI, UMI.BR _(включително 3 за първи път в историята: ALLFG.AS, AZM.MI, SPM.MI)_
  - **Exited:** ABN.AS, BBVA.MC, BESI.AS, CABK.MC, FR.PA, GLE.PA, LTMC.MI, UNI.MC, VWS.CO

**stable_winner (3m):** +4 entered, -5 exited
  - **Entered:** ASML.AS, FTK.DE, SPM.MI, UMI.BR _(включително 1 за първи път в историята: SPM.MI)_
  - **Exited:** A5G.IR, GLE.PA, SAN.MC, SWED-A.ST, UNI.MC

**quality_dip (1m):** +9 entered, -9 exited
  - **Entered:** ABN.AS, BBVA.MC, BESI.AS, CABK.MC, FR.PA, GLE.PA, LTMC.MI, UNI.MC, VWS.CO _(включително 1 за първи път в историята: BESI.AS)_
  - **Exited:** ALLFG.AS, AZM.MI, ENR.DE, KER.PA, KGF.L, NXT.L, SAAB-B.ST, SAND.ST, UMI.BR

**quality_dip (3m):** +5 entered, -6 exited
  - **Entered:** A5G.IR, GLE.PA, SAN.MC, SWED-A.ST, UNI.MC
  - **Exited:** ASML.AS, FTK.DE, KGF.L, NXT.L, SAAB-B.ST, UMI.BR

**faded_bounce (1m):** +0 entered, -1 exited
  - **Exited:** WISE.L

**faded_bounce (3m):** +1 entered, -0 exited
  - **Entered:** WISE.L



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-07-21 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **soyoil** | Commodities | 125348 | 98.9 | 98.9 | 1050 | 21759 |
| **copper** | Commodities | 73685 | 93.8 | 93.8 | 1050 | 4867 |
| **soymeal** | Commodities | 75152 | 87.4 | 87.4 | 1050 | 66551 |
| **rbob** | Commodities | 73863 | 84.9 | 84.9 | 1050 | 2497 |
| **vix** | Volatility | 3098 | 84.7 | 84.7 | 1009 | 21961 |
| **brent** | Commodities | 14746 | 82.0 | 82.0 | 233 | 6636 |
| **gbpfx** | FX | 33236 | 74.3 | 74.3 | 1050 | 25669 |
| **soybeans** | Commodities | 124900 | 74.0 | 74.0 | 1050 | 88221 |
| **cotton** | Commodities | 53209 | 72.9 | 72.9 | 1050 | 14764 |
| **coffee** | Commodities | 24866 | 63.8 | 63.8 | 1050 | 10864 |
| **aud** | FX | 24788 | 61.4 | 61.4 | 1050 | -14323 |
| **cattle** | Commodities | 75363 | 59.3 | 59.3 | 1050 | -50662 |
| **gold** | Commodities | 123586 | 53.0 | 53.0 | 1050 | 10576 |
| **corn** | Commodities | 92909 | 50.8 | 50.8 | 1050 | 162600 |
| **heatingoil** | Commodities | 13691 | 49.8 | 49.8 | 1050 | 7437 |
| **dxy** | FX | -1938 | 49.5 | 49.5 | 1050 | 3414 |
| **wheat** | Commodities | -19349 | 48.4 | 48.4 | 1050 | 51857 |
| **sp500** | US Equities | -322865 | 42.7 | 42.7 | 1050 | 50603 |
| **bitcoin** | Crypto | -7949 | 30.9 | 30.9 | 433 | -1819 |
| **platinum** | Commodities | 6113 | 30.9 | 30.9 | 1050 | -2405 |
| **eurfx** | FX | -53691 | 28.1 | 28.1 | 1049 | -44765 |
| **chf** | FX | -8897 | 26.9 | 26.9 | 1050 | 4919 |
| **silver** | Commodities | 10003 | 25.1 | 25.1 | 1050 | -1656 |
| **russell** | US Equities | -73468 | 23.2 | 23.2 | 586 | -17040 |
| **natgas** | Commodities | -102694 | 17.9 | 17.9 | 1050 | -19882 |
| **wti** | Commodities | 86905 | 15.5 | 15.5 | 1050 | -13390 |
| **cocoa** | Commodities | -11604 | 14.6 | 14.6 | 1050 | 11354 |
| **us2y** | Rates | -1595128 | 11.8 | 11.8 | 1050 | 192424 |
| **sugar** | Commodities | -96596 | 11.3 | 11.3 | 1050 | 88887 |
| **us5y** | Rates | -2131428 | 11.2 | 11.2 | 1050 | 34145 |
| **palladium** | Commodities | -6609 | 8.9 | 8.9 | 1050 | -1897 |
| **us30y** | Rates | -391386 | 8.9 | 8.9 | 1050 | -40440 |
| **usultra10y** | Rates | -380604 | 5.6 | 5.6 | 540 | -131848 |
| **jpy** | FX | -96185 | 5.2 | 5.2 | 1050 | 907 |
| **us10y** | Rates | -2064805 | 3.3 | 3.3 | 1050 | -126058 |
| **nasdaq** | US Equities | -74690 | 2.8 | 2.8 | 1050 | -23628 |
| **hogs** | Commodities | -18157 | 1.6 | 1.6 | 1050 | 7403 |
| **cad** | FX | -98377 | 0.4 | 0.4 | 1050 | -15000 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **DELL** | Technology | 97.7 | -10.7% | 79.8% | 223.9% | 213.2% | 1.47 | -32.3% |
| 2 | **MU** | Technology | 97.5 | -35.5% | 46.6% | 80.2% | 931.0% | 2.37 | -39.1% |
| 3 | **HPE** | Technology | 96.0 | 0.1% | 59.5% | 107.7% | 117.1% | 1.45 | -26.4% |
| 4 | **STX** | Technology | 95.8 | -21.1% | 32.1% | 106.1% | 549.0% | 2.24 | -31.8% |
| 5 | **AMD** | Technology | 94.3 | -20.4% | 32.9% | 70.4% | 210.7% | 1.25 | -27.8% |
| 6 | **WDC** | Technology | 92.8 | -29.1% | 18.2% | 83.0% | 847.5% | 2.47 | -38.1% |
| 7 | **DDOG** | Technology | 92.1 | 6.3% | 100.8% | 91.2% | 64.9% | 0.83 | -48.6% |
| 8 | **PANW** | Technology | 91.9 | -5.4% | 73.6% | 71.2% | 62.4% | 0.92 | -36.0% |
| 9 | **VLO** | Energy | 91.9 | 13.1% | 26.0% | 66.5% | 88.7% | 2.01 | -14.2% |
| 10 | **HUM** | Healthcare | 91.3 | -6.0% | 59.4% | 77.0% | 70.4% | 0.84 | -47.2% |
| 11 | **CVS** | Healthcare | 90.7 | 2.9% | 31.6% | 49.3% | 78.1% | 1.80 | -16.4% |
| 12 | **CNC** | Healthcare | 90.6 | -4.2% | 24.7% | 48.9% | 140.3% | 1.61 | -55.5% |
| 13 | **DVA** | Healthcare | 90.3 | 9.7% | 60.6% | 128.2% | 51.2% | 1.15 | -31.4% |
| 14 | **CSCO** | Technology | 89.8 | -4.1% | 30.0% | 44.3% | 76.2% | 1.47 | -15.3% |
| 15 | **MPC** | Energy | 89.5 | 19.1% | 33.2% | 81.3% | 51.2% | 1.66 | -18.3% |
| 16 | **FTNT** | Technology | 89.4 | -1.4% | 78.7% | 87.5% | 48.2% | 0.72 | -30.9% |
| 17 | **FLEX** | Technology | 89.1 | -35.4% | 18.2% | 58.2% | 216.0% | 1.06 | -36.4% |
| 18 | **NTAP** | Technology | 89.0 | 12.1% | 60.5% | 74.8% | 47.1% | 1.10 | -24.8% |
| 19 | **CRWD** | Technology | 88.8 | -3.4% | 57.7% | 50.5% | 57.3% | 0.79 | -37.2% |
| 20 | **SNDK** | Technology | 87.7 | -50.5% | 1.4% | 111.0% | 4794.7% | 2.83 | -56.5% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **ATS.VI** | Technology | 95.5 | -33.9% | 39.4% | 217.1% | 778.7% | 2.15 | -46.9% |
| 2 | **TPRO.MI** | Technology | 95.4 | -21.0% | 53.4% | 67.5% | 364.0% | 2.03 | -29.9% |
| 3 | **RBI.VI** | Financial Services | 90.4 | 5.7% | 26.7% | 43.7% | 129.7% | 2.15 | -18.0% |
| 4 | **GL9.IR** | Consumer Defensive | 90.2 | -4.4% | 30.9% | 45.2% | 92.0% | 2.08 | -10.0% |
| 5 | **CCC.L** | Technology | 90.0 | 12.6% | 27.6% | 46.1% | 93.3% | 2.27 | -16.2% |
| 6 | **BMPS.MI** | Financial Services | 88.7 | 7.7% | 40.3% | 47.0% | 63.8% | 1.61 | -25.5% |
| 7 | **ACX.MC** | Basic Materials | 87.1 | 21.5% | 37.8% | 43.7% | 53.2% | 1.87 | -14.9% |
| 8 | **FRO.OL** | Energy | 86.5 | 5.6% | 16.9% | 47.6% | 88.1% | 1.60 | -20.5% |
| 9 | **PKN.WA** | Energy | 86.1 | 15.9% | 19.8% | 47.8% | 66.5% | 1.91 | -12.3% |
| 10 | **AKER.OL** | Industrials | 86.1 | 6.5% | 15.8% | 44.5% | 81.3% | 2.06 | -15.6% |
| 11 | **REP.MC** | Energy | 85.6 | 20.2% | 15.1% | 58.4% | 63.4% | 2.03 | -20.4% |
| 12 | **BFT.WA** | Industrials | 84.9 | 9.6% | 36.3% | 37.1% | 47.8% | 1.68 | -17.4% |
| 13 | **UNI.MI** | Financial Services | 84.8 | 11.6% | 25.7% | 50.4% | 46.4% | 1.73 | -11.5% |
| 14 | **MT.AS** | Basic Materials | 84.5 | 14.7% | 20.9% | 26.9% | 89.7% | 1.81 | -26.2% |
| 15 | **ASML.AS** | Technology | 84.0 | -13.8% | 16.6% | 16.8% | 164.3% | 1.90 | -19.2% |
| 16 | **CABK.MC** | Financial Services | 83.4 | 8.0% | 23.8% | 28.5% | 55.9% | 2.05 | -14.1% |
| 17 | **STMMI.MI** | Technology | 83.4 | -30.0% | -0.3% | 79.1% | 181.8% | 1.22 | -35.8% |
| 18 | **SOBI.ST** | Healthcare | 83.2 | 0.9% | 17.1% | 36.2% | 63.8% | 1.71 | -14.6% |
| 19 | **SSAB-B.ST** | Basic Materials | 83.2 | 14.3% | 25.2% | 34.8% | 60.1% | 1.03 | -34.3% |
| 20 | **DHER.DE** | Consumer Cyclical | 82.8 | 5.4% | 97.9% | 46.4% | 33.1% | 0.53 | -48.7% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **EIX** | Utilities | 1.961 | 2.090 | 0.915 | 2.127 | -0.529 | - | 8.6 | +18.9% |
| 2 | **NEM** | Materials | 1.869 | 1.345 | 1.716 | 1.693 | 0.623 | - | 12.1 | +25.9% |
| 3 | **MO** | Consumer Staples | 1.785 | 1.405 | 1.974 | 1.141 | -0.304 | - | 14.2 | - |
| 4 | **APA** | Energy | 1.739 | 1.565 | 1.189 | 1.737 | -0.310 | - | 8.5 | +26.2% |
| 5 | **HST** | Real Estate | 1.342 | 1.452 | 0.344 | 1.748 | 0.011 | - | 17.1 | +14.9% |
| 6 | **MU** | Information Technology | 1.308 | 1.620 | 0.777 | 1.035 | -0.674 | - | 19.8 | +66.6% |
| 7 | **MAS** | Industrials | 1.250 | 0.251 | 1.454 | 1.389 | 0.000 | - | 16.6 | +5862.5% |
| 8 | **SYF** | Financials | 1.239 | 0.186 | 1.172 | 1.730 | -0.302 | - | 7.9 | +20.8% |
| 9 | **CF** | Materials | 1.153 | 0.175 | 0.985 | 1.724 | 0.512 | - | 11.3 | +27.3% |
| 10 | **EXPE** | Consumer Discretionary | 0.930 | 1.583 | 0.576 | 0.323 | -0.850 | - | 25.9 | +71.5% |
| 11 | **ES** | Utilities | 0.911 | 0.141 | 1.196 | 0.906 | -0.428 | - | 15.8 | +10.9% |
| 12 | **BMY** | Health Care | 0.900 | 0.491 | 0.936 | 0.842 | 0.373 | - | 18.2 | +38.7% |
| 13 | **DVA** | Health Care | 0.883 | 1.101 | 0.153 | 1.101 | -1.482 | - | 23.0 | +81.0% |
| 14 | **INCY** | Health Care | 0.879 | 1.322 | 1.065 | -0.107 | 0.688 | - | 15.7 | +30.7% |
| 15 | **HAS** | Consumer Discretionary | 0.859 | 0.546 | 0.939 | 0.685 | 0.284 | - | 16.8 | +159.6% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **COIN** | Financials | -2.013 | -2.356 | -1.252 | -1.627 | -1.607 |
| 502 | **AXON** | Industrials | -2.002 | -1.496 | -1.154 | -2.490 | -1.145 |
| 501 | **NRG** | Utilities | -1.815 | -1.495 | -0.543 | -2.680 | -2.332 |
| 500 | **KKR** | Financials | -1.773 | -1.571 | -1.407 | -1.557 | -0.893 |
| 499 | **BA** | Industrials | -1.595 | -0.746 | -1.149 | -2.136 | -1.013 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W31.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W31.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-07-27  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
