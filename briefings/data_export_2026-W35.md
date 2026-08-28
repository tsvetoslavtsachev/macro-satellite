# Сателит — пълен data export за 2026-W35

_Период: 2026-08-24 → 2026-08-30_  
_Генериран: 2026-08-28 18:18 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W35.md` (structured briefing) и `narrative_2026-W35.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**3 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **TLT** | +1.32% | +1.45σ | 82.05 | 83.13 | 2026-08-21 | 2026-08-27 | -0.24% | +1.07% | 13 |
| **LQD** | +0.76% | +1.38σ | 105.92 | 106.73 | 2026-08-21 | 2026-08-27 | -0.17% | +0.68% | 13 |
| **XLV** | -1.74% | -1.18σ | 174.62 | 171.58 | 2026-08-21 | 2026-08-27 | +1.21% | +2.49% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-08-30 · **Conditions matched:** 1/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | -3.44% | ❌ | 134.64 | 130.01 | 2026-08-21 | 2026-08-27 |
| DFEN | down ≥ 3.0% | -4.32% | ✅ | 72.14 | 69.02 | 2026-08-21 | 2026-08-27 |
| GLD | down ≥ 1.0% | -0.18% | ❌ | 423.36 | 422.60 | 2026-08-21 | 2026-08-27 |
| URA | down ≥ 3.0% | +4.99% | ❌ | 46.07 | 48.37 | 2026-08-21 | 2026-08-27 |
| UUP | up ≥ 0.5% | +0.43% | ❌ | 27.90 | 28.02 | 2026-08-21 | 2026-08-27 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-08-30 · **Conditions matched:** 0/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | -0.05% | ❌ | 299.96 | 299.81 | 2026-08-21 | 2026-08-27 |
| XLF | up ≥ 1.0% | +0.70% | ❌ | 57.48 | 57.88 | 2026-08-21 | 2026-08-27 |
| XLY | up ≥ 1.0% | -1.81% | ❌ | 118.02 | 115.88 | 2026-08-21 | 2026-08-27 |
| GLD | down ≥ 0.5% | -0.18% | ❌ | 423.36 | 422.60 | 2026-08-21 | 2026-08-27 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2026-W19 (week ending 2026-05-10)
**Cosine similarity:** 0.8870 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -0.08% | +4.83% | +4.54% |
| **USO** | -1.71% | -11.69% | -2.68% |
| **GLD** | -9.91% | -8.14% | -2.58% |
| **TLT** | -1.12% | -3.86% | -3.43% |
| **XLE** | +3.03% | +3.23% | +11.83% |
| **IWM** | +0.30% | +6.12% | +5.50% |

### Паралел #2: 2025-W26 (week ending 2025-06-29)
**Cosine similarity:** 0.8718 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.31% | +7.63% | +12.26% |
| **USO** | +8.90% | +5.10% | -6.55% |
| **GLD** | +1.67% | +15.11% | +38.35% |
| **TLT** | -0.08% | +1.73% | +0.40% |
| **XLE** | +4.28% | +7.84% | +3.63% |
| **IWM** | +3.35% | +12.00% | +16.68% |

### Паралел #3: 2023-W45 (week ending 2023-11-12)
**Cosine similarity:** 0.8445 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.33% | +13.75% | +18.21% |
| **USO** | -10.50% | -0.17% | +4.89% |
| **GLD** | +2.22% | +4.51% | +21.84% |
| **TLT** | +7.53% | +6.66% | +2.42% |
| **XLE** | -2.65% | -0.12% | +12.49% |
| **IWM** | +10.58% | +17.88% | +20.81% |

### Паралел #4: 2023-W05 (week ending 2023-02-05)
**Cosine similarity:** 0.8441 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -3.41% | +0.07% | +8.36% |
| **USO** | +5.36% | -2.13% | +14.58% |
| **GLD** | -2.79% | +8.07% | +3.88% |
| **TLT** | -4.67% | -1.70% | -9.53% |
| **XLE** | -0.21% | -6.67% | +1.12% |
| **IWM** | -5.32% | -11.44% | -1.43% |

### Паралел #5: 2026-W15 (week ending 2026-04-12)
**Cosine similarity:** 0.8421 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +8.64% | +11.11% | +13.49% |
| **USO** | +15.61% | -12.91% | +4.16% |
| **GLD** | -0.96% | -13.75% | -3.32% |
| **TLT** | -1.73% | -2.34% | -3.88% |
| **XLE** | +1.11% | -3.27% | +9.40% |
| **IWM** | +8.14% | +13.28% | +14.74% |

### Паралел #6: 2024-W18 (week ending 2024-05-05)
**Cosine similarity:** 0.8333 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.34% | +4.23% | +11.69% |
| **USO** | -5.38% | -2.32% | -4.14% |
| **GLD** | +1.08% | +5.81% | +18.55% |
| **TLT** | +3.15% | +9.39% | +1.11% |
| **XLE** | -2.90% | -4.50% | -4.90% |
| **IWM** | +0.03% | +3.48% | +8.46% |

### Паралел #7: 2026-W16 (week ending 2026-04-19)
**Cosine similarity:** 0.8280 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.32% | +4.67% | +8.58% |
| **USO** | +31.82% | +6.83% | +12.04% |
| **GLD** | -7.72% | -17.38% | -5.23% |
| **TLT** | -4.65% | -2.93% | -4.53% |
| **XLE** | +11.40% | +4.83% | +13.21% |
| **IWM** | -1.01% | +6.62% | +8.71% |

### Паралел #8: 2024-W23 (week ending 2024-06-09)
**Cosine similarity:** 0.8181 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.08% | +1.19% | +13.82% |
| **USO** | +9.24% | -5.60% | -3.81% |
| **GLD** | +3.29% | +8.99% | +14.82% |
| **TLT** | +0.93% | +8.81% | +3.16% |
| **XLE** | -1.37% | -4.42% | +1.14% |
| **IWM** | +0.10% | +3.33% | +18.75% |

### Паралел #9: 2024-W02 (week ending 2024-01-14)
**Cosine similarity:** 0.8172 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.65% | +7.17% | +17.48% |
| **USO** | +6.81% | +19.86% | +17.98% |
| **GLD** | -2.73% | +14.33% | +17.61% |
| **TLT** | -4.32% | -6.45% | -2.67% |
| **XLE** | +0.85% | +16.27% | +9.48% |
| **IWM** | +0.71% | +2.83% | +10.30% |

### Паралел #10: 2023-W52 (week ending 2023-12-31)
**Cosine similarity:** 0.8145 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.28% | +10.05% | +14.50% |
| **USO** | +9.24% | +18.12% | +19.41% |
| **GLD** | -1.35% | +7.61% | +12.47% |
| **TLT** | -3.20% | -4.31% | -7.18% |
| **XLE** | +1.38% | +12.61% | +8.72% |
| **IWM** | -1.49% | +4.78% | +1.09% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 14 · **Total matching days:** 74 · **History:** 2021-05-17 → 2026-08-27

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 14 | +2.2% | +2.4% | -3.1% | +7.4% | 71% |
| **SPY** | 3m | 14 | +2.9% | +3.1% | -7.3% | +12.0% | 79% |
| **SPY** | 6m | 14 | +7.9% | +9.8% | -6.8% | +21.8% | 79% |
| **USO** | 1m | 14 | +0.5% | +0.3% | -14.3% | +12.7% | 50% |
| **USO** | 3m | 14 | -1.7% | -2.0% | -18.9% | +24.5% | 50% |
| **USO** | 6m | 14 | +11.3% | +2.1% | -13.7% | +109.4% | 57% |
| **GLD** | 1m | 14 | +3.1% | +2.0% | -0.9% | +9.0% | 79% |
| **GLD** | 3m | 14 | +6.3% | +7.3% | -12.6% | +24.5% | 71% |
| **GLD** | 6m | 14 | +8.2% | +11.4% | -12.5% | +25.3% | 79% |
| **TLT** | 1m | 14 | -1.5% | -1.1% | -6.7% | +3.6% | 36% |
| **TLT** | 3m | 14 | -0.5% | -0.1% | -16.5% | +11.1% | 50% |
| **TLT** | 6m | 14 | -4.0% | -2.7% | -18.0% | +7.5% | 29% |

**Episodes (последни 5 от 14):**
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-08-03` (5d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 75 · **History:** 2021-05-17 → 2026-08-27

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +6.3% | +6.3% | +3.5% | +9.1% | 100% |
| **SPY** | 3m | 2 | +6.4% | +6.4% | +2.6% | +10.3% | 100% |
| **SPY** | 6m | 2 | +8.3% | +8.3% | +2.6% | +14.1% | 100% |
| **USO** | 1m | 2 | +5.6% | +5.6% | +4.0% | +7.2% | 100% |
| **USO** | 3m | 2 | -0.9% | -0.9% | -9.9% | +8.2% | 50% |
| **USO** | 6m | 2 | +6.3% | +6.3% | +4.4% | +8.2% | 100% |
| **GLD** | 1m | 2 | +3.5% | +3.5% | -0.2% | +7.2% | 50% |
| **GLD** | 3m | 2 | -0.1% | -0.1% | -13.8% | +13.6% | 50% |
| **GLD** | 6m | 2 | +5.4% | +5.4% | -2.7% | +13.6% | 50% |
| **TLT** | 1m | 2 | -1.4% | -1.4% | -1.8% | -1.0% | 0% |
| **TLT** | 3m | 2 | -2.0% | -2.0% | -2.9% | -1.1% | 0% |
| **TLT** | 6m | 2 | -2.7% | -2.7% | -4.4% | -1.1% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-08-27` (28d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 430 · **History:** 2021-05-17 → 2026-08-27

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
- `2025-11-03 → 2026-08-27` (198d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-08-27

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 9 · **Total matching days:** 86 · **History:** 2021-05-17 → 2026-08-27

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 9 | -0.2% | +0.9% | -7.2% | +7.8% | 56% |
| **SPY** | 3m | 9 | +2.1% | +3.2% | -8.3% | +11.6% | 56% |
| **SPY** | 6m | 9 | +1.4% | +4.1% | -20.8% | +14.2% | 67% |
| **USO** | 1m | 9 | +3.8% | -1.3% | -15.0% | +52.9% | 44% |
| **USO** | 3m | 9 | +8.2% | -0.1% | -20.7% | +52.2% | 44% |
| **USO** | 6m | 9 | +9.2% | -0.2% | -27.6% | +45.8% | 44% |
| **GLD** | 1m | 9 | -0.9% | -1.6% | -8.3% | +11.7% | 22% |
| **GLD** | 3m | 9 | -0.0% | +0.2% | -12.0% | +11.5% | 56% |
| **GLD** | 6m | 9 | +1.5% | -0.8% | -11.4% | +25.0% | 44% |
| **TLT** | 1m | 9 | -2.1% | -2.5% | -6.0% | +2.5% | 11% |
| **TLT** | 3m | 9 | -6.2% | -5.7% | -17.6% | +4.2% | 22% |
| **TLT** | 6m | 9 | -9.9% | -7.8% | -22.3% | +1.2% | 11% |

**Episodes (последни 5 от 9):**
- `2023-04-12 → 2023-04-18` (5d)
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-05-19` (36d)
- `2026-07-22 → 2026-08-03` (8d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 17 · **Total matching days:** 290 · **History:** 2021-05-17 → 2026-08-27

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 17 | +1.9% | +1.6% | -4.8% | +9.0% | 71% |
| **SPY** | 3m | 17 | +3.1% | +4.2% | -12.6% | +16.2% | 71% |
| **SPY** | 6m | 17 | +6.5% | +8.8% | -14.0% | +21.0% | 76% |
| **USO** | 1m | 17 | +1.8% | -2.2% | -13.0% | +22.9% | 41% |
| **USO** | 3m | 17 | +2.5% | -0.8% | -14.5% | +29.9% | 41% |
| **USO** | 6m | 17 | +11.8% | +2.6% | -12.4% | +87.1% | 71% |
| **GLD** | 1m | 17 | +2.7% | +2.2% | -5.6% | +9.0% | 76% |
| **GLD** | 3m | 17 | +6.3% | +7.2% | -16.8% | +23.6% | 71% |
| **GLD** | 6m | 17 | +11.3% | +9.8% | -8.4% | +43.8% | 76% |
| **TLT** | 1m | 17 | +0.4% | +0.4% | -6.3% | +8.2% | 53% |
| **TLT** | 3m | 17 | -1.4% | -1.1% | -15.3% | +11.9% | 41% |
| **TLT** | 6m | 17 | -4.3% | -1.7% | -21.3% | +7.0% | 41% |

**Episodes (последни 5 от 17):**
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)
- `2026-08-07 → 2026-08-27` (15d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 19 · **Total matching days:** 288 · **History:** 2021-05-17 → 2026-08-27

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 19 | +0.4% | +1.0% | -8.7% | +7.0% | 53% |
| **SPY** | 3m | 19 | +2.1% | +3.6% | -13.7% | +9.1% | 68% |
| **SPY** | 6m | 19 | +3.4% | +6.8% | -16.4% | +16.9% | 74% |
| **USO** | 1m | 19 | -0.6% | -5.6% | -21.8% | +55.8% | 42% |
| **USO** | 3m | 19 | +3.4% | -1.3% | -12.7% | +64.3% | 42% |
| **USO** | 6m | 19 | +8.3% | -2.3% | -16.0% | +75.1% | 47% |
| **GLD** | 1m | 19 | -0.6% | -0.1% | -12.4% | +7.6% | 47% |
| **GLD** | 3m | 19 | +2.1% | +1.7% | -13.7% | +19.0% | 68% |
| **GLD** | 6m | 19 | +8.3% | +6.0% | -15.8% | +55.5% | 74% |
| **TLT** | 1m | 19 | -0.2% | -0.1% | -5.6% | +5.2% | 47% |
| **TLT** | 3m | 19 | -3.6% | -4.4% | -17.3% | +8.7% | 32% |
| **TLT** | 6m | 19 | -6.8% | -7.4% | -21.4% | +4.6% | 21% |

**Episodes (последни 5 от 19):**
- `2025-05-12 → 2025-05-19` (3d)
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (13d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-08-27

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (11 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | 5 | 2.61 | 2.70 | 2026-07-25 00:00:00 | 2026-08-22 00:00:00 | ✓ |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 5 | 2.56 | 2.71 | 2026-07-25 00:00:00 | 2026-08-22 00:00:00 | ✓ |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 5 | 2.21 | 2.43 | 2026-07-25 00:00:00 | 2026-08-22 00:00:00 | - |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | 5 | 2.14 | 2.22 | 2026-07-25 00:00:00 | 2026-08-22 00:00:00 | - |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 4 | 2.28 | 2.28 | 2026-07-25 00:00:00 | 2026-08-15 00:00:00 | ✓ |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | 4 | 2.09 | 2.09 | 2026-08-01 00:00:00 | 2026-08-22 00:00:00 | - |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 3 | 2.30 | 2.30 | 2026-08-01 00:00:00 | 2026-08-15 00:00:00 | - |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | 3 | 2.28 | 2.28 | 2026-07-25 00:00:00 | 2026-08-08 00:00:00 | ✓ |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 3 | 2.15 | 2.15 | 2026-07-25 00:00:00 | 2026-08-08 00:00:00 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | 2 | 2.02 | 2.02 | 2026-07-25 00:00:00 | 2026-08-01 00:00:00 | ✓ |
| **COMPUTSA** | Завършени жилища (SAAR) | growth | housing_supply | 1 | 2.06 | 2.06 | 2026-08-22 00:00:00 | 2026-08-22 00:00:00 | - |

### EU (6 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.27 | 5.27 | 2026-07-25 00:00:00 | 2026-08-22 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.16 | 2.17 | 2026-07-25 00:00:00 | 2026-08-22 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.16 | 2.17 | 2026-07-25 00:00:00 | 2026-08-22 00:00:00 | ✓ |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | 3 | 2.38 | 2.38 | 2026-07-25 00:00:00 | 2026-08-08 00:00:00 | - |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | 1 | 2.66 | 2.66 | 2026-07-25 00:00:00 | 2026-07-25 00:00:00 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation | sentiment | 1 | 2.17 | 2.17 | 2026-07-25 00:00:00 | 2026-07-25 00:00:00 | - |

### CN (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 7 | 2.55 | 2.55 | 2026-07-27 00:00:00 | 2026-08-24 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 7 | 2.23 | 2.23 | 2026-07-27 00:00:00 | 2026-08-24 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 1 | 2.19 | 2.19 | 2026-08-22 00:00:00 | 2026-08-22 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-08-22 00:00:00 · **Generated:** 2026-08-22 03:08:12.995120+00:00

**Режим:** `transition` (Преходно / смесено)  
**Primary driver:** `none`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 36.3 | contracting | 22.2% | 3 | 2 |
| **growth** | 45.0 | mixed | 48.0% | 2 | 0 |
| **inflation** | 40.6 | mixed | 38.9% | 2 | 1 |
| **liquidity** | 51.6 | mixed | 47.4% | 0 | 0 |

### Top anomalies (6 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.71 | down | 93.55 | 2026-04-01 | ✓ min |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | -2.70 | down | 61.40 | 2026-07-01 | ✓ min |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | -2.22 | down | 58.90 | 2026-07-01 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | +2.16 | up | 4.60 | 2026-06-01 | - |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | -2.09 | down | 2.70 | 2026-06-01 | - |
| **COMPUTSA** | Завършени жилища (SAAR) | growth, housing | housing_supply | -2.06 | down | -16.76 | 2026-07-01 | - |

### Narrative hints от макро лещите
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **CIVPART**: Структурни сдвигове (демография, ранно пенсиониране). Пост-COVID не се възстанови напълно.
- **EMRATIO**: Не зависи от definition на 'active labor force'. По-стабилен индикатор на дълбоката заетост.
- **MICH_INFL_1Y**: Household очаквания. По-шумни от market-based, но по-ранни. Extreme movements сигнализират de-anchoring risk.
- **PSAVERT**: Hard data компонент. Скочи >30% в COVID — когато survey и hard data разминават, сигналът укрепва.
- **COMPUTSA**: Завършва construction pipeline (12-18m след starts). Превишение спрямо sales = inventory build.

### Cross-lens divergences (6 entries)
- 🔔 **?**
  - `pair_id`: stagflation_test
  - `name_bg`: Labor tightness × Inflation pressure
  - `question_bg`: Дали labor tightness потвърждава inflation pressure (стагфлация)?
  - `state`: transition
  - `interpretation`: Transition — signals not aligned; watch next releases.
  - `slot_a_label`: Labor tightness
  - `slot_b_label`: Inflation pressure
  - `breadth_a`: 0.5
  - `breadth_b`: 0.0
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.667
- 🔔 **?**
  - `pair_id`: growth_labor_lead_lag
  - `name_bg`: Hard activity × Labor claims
  - `question_bg`: Дали hard activity и labor market следват едно тенденция?
  - `state`: transition
  - `interpretation`: Mixed — waiting for clarification.
  - `slot_a_label`: Hard activity
  - `slot_b_label`: Labor market (claims inverted)
  - `breadth_a`: 0.4
  - `breadth_b`: 0.333
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 0.8
  - `breadth_b_raw`: 0.333
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Realized CPI × Expectations
  - `question_bg`: Дали expectations следват realized inflation, или стоят anchored?
  - `state`: both_down
  - `interpretation`: Joint disinflation — expectations потвърждават cooling.
  - `slot_a_label`: Realized inflation
  - `slot_b_label`: Inflation expectations
  - `breadth_a`: 0.0
  - `breadth_b`: 0.0
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 0.667
  - `breadth_b_raw`: 0.0
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
  - `breadth_a`: 0.333
  - `breadth_b`: 0.4
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.333
  - `breadth_b_raw`: 0.8
- 🔔 **?**
  - `pair_id`: model_vs_market
  - `name_bg`: Model-implied × Market-implied inflation
  - `question_bg`: Дали underlying persistence и market pricing-а са съгласни за инфлацията?
  - `state`: a_up_b_down
  - `interpretation`: Модел persistent, пазар разчита на disinflation — contrarian hawkish (моделът обикновено лидера).
  - `slot_a_label`: Модел (sticky inflation)
  - `slot_b_label`: Пазар (breakevens + survey)
  - `breadth_a`: 0.667
  - `breadth_b`: 0.0
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 0.667
  - `breadth_b_raw`: 0.0

### Executive narrative
> Сигналите са в преход — няма доминираща конфигурация. Следващите 2-3 релиза ще ориентират посоката. Най-отклонена леща: Растеж и активност — breadth 66% (смесено), 2 аномалии, 0 нови екстремума. За наблюдение следващия релиз: LABOR_SHARE_NBS, CIVPART (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: LABOR_SHARE_NBS z=-2.71 · NEW-5Y-MIN
- 2 нови екстремуми в top-6 (lookback 5г.)
- Активни двойки: Inflation anchoring=both_down; Credit × Policy=both_up; model_vs_market=a_up_b_down



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-08-22 00:00:00 · **Generated:** 2026-08-22 03:24:52.043720+00:00

**Режим:** `policy_dilemma` (Policy dilemma)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 40.1 | mixed | 42.9% | 0 | 0 |
| **growth** | 40.8 | mixed | 16.7% | 0 | 0 |
| **inflation** | 49.6 | mixed | 57.1% | 0 | 0 |
| **credit** | 44.7 | mixed | 36.8% | 3 | 2 |
| **external** | 17.6 | contracting | 25.0% | 0 | 0 |

### Top anomalies (3 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | +5.27 | up | 2.83 | 2026-07-01 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | +2.17 | up | 3.85 | 2026-07-01 | ✓ max |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | +2.17 | up | 3.07 | 2026-07-01 | ✓ max |

### Narrative hints от макро лещите
- **EA_BUND_2Y**: EA-aggregate 2Y yield. Curve slope (10Y-2Y) проксира policy expectations и recession risk.
- **FR_10Y**: France sovereign yield — компонент на OAT-Bund spread. Core-but-not-DE EA stress indicator.
- **DE_10Y**: Germany 10Y, Maastricht-criterion measure. Reference за BTP-Bund / OAT-Bund spread изчисления.

### Cross-lens divergences (7 entries)
- 🔔 **?**
  - `pair_id`: stagflation_test
  - `name_bg`: Стагфлационен тест
  - `question_bg`: Заплатите ли движат услугите нагоре?
  - `state`: a_down_b_up
  - `interpretation`: Sticky services без wage support — не sustainable. Очаквай корекция надолу в core.
  - `slot_a_label`: Натиск от заплати
  - `slot_b_label`: Базова/услуги инфлация
  - `breadth_a`: 0.0
  - `breadth_b`: 1.0
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 1.0
- 🔔 **?**
  - `pair_id`: ecb_transmission
  - `name_bg`: Трансмисия на ЕЦБ политиката
  - `question_bg`: ЕЦБ hike-овете стигат ли до банковото кредитиране?
  - `state`: transition
  - `interpretation`: Смесена картина — типично около policy turning points.
  - `slot_a_label`: Политика (реална лихва + баланс)
  - `slot_b_label`: Банково кредитиране (свиване)
  - `breadth_a`: 0.5
  - `breadth_b`: 1.0
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 1.0
- 🔔 **?**
  - `pair_id`: fragmentation_risk
  - `name_bg`: Фрагментационен риск
  - `question_bg`: ЕЦБ hike-овете разширяват ли периферните spreads?
  - `state`: transition
  - `interpretation`: Mixed signals — гледай individual country drivers.
  - `slot_a_label`: Политика (реална лихва + баланс)
  - `slot_b_label`: Sovereign spreads (BTP/OAT-Bund)
  - `breadth_a`: 0.5
  - `breadth_b`: 1.0
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 1.0
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
  - `breadth_b`: 1.0
  - `state_raw`: insufficient_data
  - `breadth_a_raw`: None
  - `breadth_b_raw`: 1.0
- 🔔 **?**
  - `pair_id`: sentiment_vs_hard_data
  - `name_bg`: Очаквания срещу твърди данни
  - `question_bg`: Sentiment отразява ли реалната икономика?
  - `state`: transition
  - `interpretation`: Sentiment turn обикновено leads hard data 3-6mo.
  - `slot_a_label`: Sentiment (ESI, confidence)
  - `slot_b_label`: Hard activity (IP, retail, GDP)
  - `breadth_a`: 0.667
  - `breadth_b`: 0.5
  - `state_raw`: transition
  - `breadth_a_raw`: 0.667
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
  - `breadth_b`: 0.75
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 1.0

### Executive narrative
> Policy dilemma — labor market е loose, но инфлацията remains hot. ЕЦБ е заклещена между инфлацията и растежа. Най-отклонена леща: Инфлация и цени — breadth 83% (разширяване), 0 аномалии, 0 нови екстремума. За наблюдение следващия релиз: FR_10Y, DE_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.27
- 2 нови екстремуми в top-3 (lookback 5г.)
- Активни двойки: Stagflation test=a_down_b_up



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-08-24 00:00:00 · **Generated:** 2026-08-24 06:51:19.761752+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 38.6 | mixed | -% | - | - |
| **inflation** | 44.9 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 47.8 | mixed | -% | - | - |
| **property** | 28.6 | contracting | -% | - | - |

### Top anomalies (2 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | -2.55 | down | 3.00 | 2026-08-20 | ✓ min |
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
  - `breadth_a`: 0.333
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
  - `state`: a_up_b_down
  - `interpretation`: Export-dependence — износът носи растежа, докато вътрешното търсене е слабо. Небалансирано възстановяване, уязвимо на тарифи/външни шокове.
  - `slot_a_label`: Външно търсене
  - `slot_b_label`: Вътрешна активност
  - `breadth_a`: 0.833
  - `breadth_b`: 0.333

### Executive narrative
> Претеглен композитен macro score 37.8/100 → режим „ВЛОШАВАЩ СЕ“ (5/5 лещи). 5 лещи, 2 flagged аномалии (4 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-08-21 |
| `as_of` | 2026-08-21 |
| `regime` | REFLATION |
| `alignment_score` | 5.0 |
| `gms_score` | 4.0 |
| `gms_max` | 8 |
| `gms_tier` | MEDIUM |
| `ks_status` | inactive |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-08-21 → 2026-08-27)

**stable_winner (1m):** +14 entered, -17 exited
  - **Entered:** BKR, FDX, FIX, GILD, GM, HST, IBKR, IRM, NUE, PLD, RL, ROST, TGT, WDC _(включително 3 за първи път в историята: FDX, NUE, TGT)_
  - **Exited:** ADM, BG, COHR, ETR, EXPE, F, FCX, FITB, GOOG, GOOGL, JNJ, KEY, NEE, PNC, PWR, RF, VLO

**stable_winner (3m):** +6 entered, -9 exited
  - **Entered:** EQIX, EXPE, HST, MRNA, SPG, TGT _(включително 2 за първи път в историята: EQIX, TGT)_
  - **Exited:** ADM, BG, CHRW, F, GS, PNC, PWR, TSLA, VTR

**quality_dip (1m):** +17 entered, -14 exited
  - **Entered:** ADM, BG, CVS, ETR, EXPE, FCX, FITB, GOOG, GOOGL, JNJ, KEY, MO, NEE, PNC, PWR, RF, VLO _(включително 4 за първи път в историята: FITB, GOOG, MO, PNC)_
  - **Exited:** BKR, EL, FIX, GILD, GM, HII, HST, IBKR, IRM, NUE, PLD, RL, ROST, WDC

**quality_dip (3m):** +11 entered, -8 exited
  - **Entered:** ADM, BG, CHRW, CVS, FDX, GS, MO, PNC, PWR, TSLA, VTR _(включително 3 за първи път в историята: FDX, MO, TSLA)_
  - **Exited:** COHR, EL, EQIX, EXPE, HII, HST, MRNA, SPG

**faded_bounce (1m):** +12 entered, -10 exited
  - **Entered:** ADP, AMT, ARES, BX, CHTR, DASH, EFX, NKE, PEG, TDG, TSCO, TTD _(включително 2 за първи път в историята: AMT, TDG)_
  - **Exited:** CAG, CARR, COIN, EQT, HRL, INVH, MKC, POOL, RSG, TPL

**faded_bounce (3m):** +4 entered, -6 exited
  - **Entered:** BSX, CLX, CSGP, TDG _(включително 1 за първи път в историята: TDG)_
  - **Exited:** CARR, CI, FISV, GIS, GPN, LII

### EU (period: 2026-08-21 → 2026-08-27)

**stable_winner (1m):** +14 entered, -19 exited
  - **Entered:** BBVA.MC, BGEO.L, EMG.L, FR.PA, GAW.L, HM-B.ST, HSBA.L, ITX.MC, KER.PA, SBRY.L, SDR.L, STAN.L, TSCO.L, UNI.MC _(включително 3 за първи път в историята: EMG.L, HSBA.L, SDR.L)_
  - **Exited:** ABBN.SW, BCP.LS, BOL.ST, CABK.MC, DANSKE.CO, EDPR.LS, ELI.BR, ENR.DE, ING.WA, JYSK.CO, LTMC.MI, MOBN.SW, NDA.DE, NDX1.DE, NESTE.HE, SAN.MC, VATN.SW, VOE.VI, VWS.CO

**stable_winner (3m):** +5 entered, -8 exited
  - **Entered:** BAMI.MI, BBVA.MC, EBS.VI, ING.WA, NOKIA.HE _(включително 2 за първи път в историята: ING.WA, NOKIA.HE)_
  - **Exited:** ACS.MC, BCP.LS, CABK.MC, GL9.IR, IHG.L, INGA.AS, NKT.CO, VWS.CO

**quality_dip (1m):** +22 entered, -20 exited
  - **Entered:** ABBN.SW, BAMI.MI, BCP.LS, BOL.ST, CABK.MC, DANSKE.CO, EDPR.LS, ELI.BR, ENR.DE, ING.WA, JYSK.CO, LTMC.MI, MOBN.SW, NDA.DE, NDX1.DE, NESTE.HE, NOKIA.HE, SALM.OL, SAN.MC, VATN.SW, VOE.VI, VWS.CO _(включително 4 за първи път в историята: BOL.ST, ING.WA, NOKIA.HE, SALM.OL)_
  - **Exited:** BARC.L, BBVA.MC, BGEO.L, EMG.L, FR.PA, GAW.L, HM-B.ST, HSBA.L, IGG.L, INCH.L, ITX.MC, KER.PA, RR.L, SBRY.L, SDR.L, SSE.L, STAN.L, TSCO.L, UNI.MC, VOD.L

**quality_dip (3m):** +9 entered, -9 exited
  - **Entered:** ACS.MC, BCP.LS, CABK.MC, GL9.IR, IHG.L, INGA.AS, NKT.CO, SALM.OL, VWS.CO _(включително 3 за първи път в историята: ACS.MC, IHG.L, SALM.OL)_
  - **Exited:** BARC.L, BBVA.MC, EBS.VI, IGG.L, INCH.L, ING.WA, RR.L, SSE.L, VOD.L

**faded_bounce (1m):** +3 entered, -40 exited
  - **Entered:** LISP.SW, REL.L, TBCG.L _(включително 1 за първи път в историята: LISP.SW)_
  - **Exited:** ADYEN.AS, AMS.MC, BC.MI, BEIJ-B.ST, BKW.SW, BME.L, BOL.PA, CMBN.SW, DGE.L, DSFIR.AS, DSY.PA, EXO.AS, FDJU.PA, FPE3.DE, GIVN.SW, III.L, LATO-B.ST, LEG.DE, LIFCO-B.ST, MNDI.L, PGHN.SW, RAA.DE, RED.MC, RI.PA, RMS.PA, SAP.DE, SGE.L, SGO.PA, STLAM.MI, SWEC-B.ST, SY1.DE, TE.PA, TOM.OL, TRYG.CO, VNA.DE, VPK.AS, VZN.SW, WIE.VI, WISE.L, ZURN.SW

**faded_bounce (3m):** +2 entered, -4 exited
  - **Entered:** LISP.SW, MNDI.L _(включително 1 за първи път в историята: LISP.SW)_
  - **Exited:** FDJU.PA, FPE3.DE, RAA.DE, SGE.L



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-08-18 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **copper** | Commodities | 79225 | 95.6 | 95.6 | 1054 | 5540 |
| **soyoil** | Commodities | 98237 | 94.7 | 94.7 | 1054 | -27111 |
| **cotton** | Commodities | 78668 | 91.8 | 91.8 | 1054 | 25459 |
| **soymeal** | Commodities | 83024 | 89.8 | 89.8 | 1054 | 7872 |
| **aud** | FX | 52108 | 84.2 | 84.2 | 1054 | 27320 |
| **soybeans** | Commodities | 151662 | 82.9 | 82.9 | 1054 | 26762 |
| **gbpfx** | FX | 42877 | 81.6 | 81.6 | 1054 | 9641 |
| **rbob** | Commodities | 70040 | 81.5 | 81.5 | 1053 | 1089 |
| **corn** | Commodities | 250505 | 81.4 | 81.4 | 1054 | 157596 |
| **dxy** | FX | 8112 | 81.1 | 81.1 | 1054 | 10050 |
| **sugar** | Commodities | 151349 | 77.3 | 77.3 | 1054 | 247945 |
| **vix** | Volatility | -19093 | 68.2 | 68.2 | 1013 | -22191 |
| **coffee** | Commodities | 26739 | 65.9 | 65.9 | 1054 | 1873 |
| **gold** | Commodities | 145922 | 64.0 | 64.0 | 1054 | 22336 |
| **heatingoil** | Commodities | 16470 | 55.1 | 55.1 | 1054 | 2779 |
| **sp500** | US Equities | -281402 | 55.0 | 55.0 | 1054 | 41463 |
| **brent** | Commodities | 6992 | 53.2 | 53.2 | 237 | -7754 |
| **cattle** | Commodities | 61514 | 51.0 | 51.0 | 1054 | -13849 |
| **wheat** | Commodities | -26485 | 44.3 | 44.3 | 1054 | -7136 |
| **platinum** | Commodities | 6938 | 34.5 | 34.5 | 1054 | 825 |
| **bitcoin** | Crypto | -7439 | 32.0 | 32.0 | 437 | 510 |
| **silver** | Commodities | 10768 | 27.4 | 27.4 | 1054 | 765 |
| **eurfx** | FX | -57716 | 27.1 | 27.1 | 1054 | -1045 |
| **chf** | FX | -9071 | 26.7 | 26.7 | 1054 | -174 |
| **wti** | Commodities | 104035 | 21.9 | 21.9 | 1054 | 17130 |
| **natgas** | Commodities | -99900 | 19.3 | 19.3 | 1054 | 2794 |
| **us2y** | Rates | -1243004 | 17.9 | 17.9 | 1054 | 352124 |
| **jpy** | FX | -67971 | 17.5 | 17.5 | 1054 | 28214 |
| **us30y** | Rates | -361383 | 14.0 | 14.0 | 1054 | 30003 |
| **cocoa** | Commodities | -13613 | 12.9 | 12.9 | 1054 | -2009 |
| **palladium** | Commodities | -5370 | 11.7 | 11.7 | 1054 | 1239 |
| **us5y** | Rates | -2169814 | 11.0 | 11.0 | 1054 | -38386 |
| **usultra10y** | Rates | -353477 | 8.3 | 8.3 | 544 | 27127 |
| **russell** | US Equities | -99786 | 7.6 | 7.6 | 590 | -26318 |
| **nasdaq** | US Equities | -61771 | 4.9 | 4.9 | 1054 | 12919 |
| **us10y** | Rates | -2229013 | 2.5 | 2.5 | 1054 | -164208 |
| **cad** | FX | -88897 | 1.3 | 1.3 | 1054 | 9480 |
| **hogs** | Commodities | -23486 | 0.8 | 0.8 | 1054 | -5329 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **DELL** | Technology | 97.6 | 18.3% | 52.2% | 277.4% | 203.1% | 1.78 | -32.3% |
| 2 | **MRNA** | Healthcare | 96.5 | 168.2% | 214.3% | 191.3% | 120.1% | 1.37 | -35.5% |
| 3 | **HPE** | Technology | 95.8 | 21.1% | 48.9% | 170.2% | 106.3% | 1.68 | -26.4% |
| 4 | **VLO** | Energy | 95.7 | 16.9% | 45.4% | 75.8% | 106.7% | 2.33 | -12.1% |
| 5 | **MPC** | Energy | 94.6 | 18.7% | 47.0% | 86.3% | 80.2% | 2.10 | -18.3% |
| 6 | **MRVL** | Technology | 93.5 | 40.5% | 23.4% | 203.1% | 139.7% | 1.48 | -48.4% |
| 7 | **PANW** | Technology | 93.0 | 6.4% | 36.6% | 134.3% | 72.8% | 1.35 | -36.0% |
| 8 | **FTNT** | Technology | 92.0 | 5.0% | 23.1% | 103.7% | 93.2% | 1.71 | -29.2% |
| 9 | **PSX** | Energy | 91.4 | 18.3% | 39.5% | 61.5% | 62.8% | 1.98 | -17.3% |
| 10 | **NTAP** | Technology | 90.0 | 11.1% | 36.2% | 91.8% | 60.0% | 1.25 | -24.8% |
| 11 | **CRL** | Healthcare | 89.4 | 22.7% | 79.4% | 76.1% | 46.5% | 1.19 | -33.9% |
| 12 | **CRWD** | Technology | 88.8 | 4.1% | 17.3% | 108.3% | 73.6% | 1.12 | -37.2% |
| 13 | **MU** | Technology | 88.0 | 14.4% | 1.1% | 118.9% | 605.9% | 2.54 | -39.1% |
| 14 | **STT** | Financial Services | 88.0 | 6.0% | 23.2% | 48.8% | 63.0% | 2.03 | -11.8% |
| 15 | **CNC** | Healthcare | 87.0 | 2.4% | 11.3% | 53.4% | 119.8% | 1.56 | -32.7% |
| 16 | **TGT** | Consumer Defensive | 86.8 | 14.6% | 28.8% | 43.3% | 53.3% | 1.70 | -20.3% |
| 17 | **EXPE** | Consumer Cyclical | 86.1 | 12.7% | 47.5% | 64.4% | 39.7% | 0.84 | -37.4% |
| 18 | **SNDK** | Technology | 85.8 | 36.8% | -5.7% | 137.1% | 2243.1% | 2.97 | -56.5% |
| 19 | **STX** | Technology | 85.5 | 13.3% | -2.7% | 101.1% | 359.4% | 2.18 | -31.8% |
| 20 | **MRK** | Healthcare | 85.4 | 16.1% | 28.2% | 26.9% | 59.7% | 1.92 | -11.4% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **AKER.OL** | Industrials | 91.1 | 32.5% | 26.6% | 80.5% | 75.9% | 2.60 | -15.6% |
| 2 | **RBI.VI** | Financial Services | 90.7 | 9.2% | 28.4% | 50.8% | 101.9% | 2.03 | -18.0% |
| 3 | **CCC.L** | Technology | 90.7 | 14.3% | 18.9% | 73.3% | 107.2% | 2.53 | -16.2% |
| 4 | **ATS.VI** | Technology | 88.3 | 24.8% | 6.6% | 190.1% | 477.2% | 2.42 | -50.1% |
| 5 | **TKA.DE** | Basic Materials | 87.3 | 23.5% | 29.1% | 39.8% | 78.5% | 1.39 | -41.4% |
| 6 | **REP.MC** | Energy | 86.5 | 1.3% | 17.6% | 40.0% | 91.9% | 1.97 | -20.4% |
| 7 | **BMPS.MI** | Financial Services | 86.5 | 0.6% | 27.0% | 53.2% | 58.8% | 1.35 | -25.5% |
| 8 | **UNI.MI** | Financial Services | 86.4 | 7.2% | 33.9% | 40.9% | 54.8% | 1.80 | -11.5% |
| 9 | **ABN.AS** | Financial Services | 85.9 | 12.6% | 22.7% | 52.0% | 54.7% | 1.97 | -18.0% |
| 10 | **NESTE.HE** | Energy | 85.5 | 3.8% | 12.6% | 49.3% | 90.3% | 1.59 | -20.4% |
| 11 | **BFT.WA** | Industrials | 85.0 | 0.4% | 22.1% | 40.6% | 62.1% | 1.72 | -17.4% |
| 12 | **BBVA.MC** | Financial Services | 83.7 | 8.7% | 25.1% | 29.7% | 53.9% | 1.66 | -18.7% |
| 13 | **ACX.MC** | Basic Materials | 83.4 | 3.3% | 16.5% | 35.1% | 70.4% | 1.66 | -14.9% |
| 14 | **BAYN.DE** | Healthcare | 83.3 | 2.7% | 39.4% | 16.9% | 71.3% | 1.31 | -30.6% |
| 15 | **BG.VI** | Financial Services | 83.3 | 5.4% | 17.2% | 40.0% | 57.3% | 1.85 | -16.3% |
| 16 | **PKN.WA** | Energy | 83.2 | -0.2% | 10.5% | 36.0% | 87.3% | 1.81 | -12.3% |
| 17 | **SSAB-B.ST** | Basic Materials | 83.0 | 6.7% | 11.3% | 35.5% | 82.7% | 1.78 | -27.7% |
| 18 | **ASML.AS** | Technology | 82.8 | 11.1% | 8.7% | 23.1% | 115.5% | 1.98 | -20.8% |
| 19 | **UNI.MC** | Financial Services | 82.8 | 12.4% | 26.0% | 37.6% | 43.1% | 1.82 | -17.8% |
| 20 | **GL9.IR** | Consumer Defensive | 81.4 | 1.2% | 11.1% | 35.5% | 62.5% | 1.95 | -10.4% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **EIX** | Utilities | 2.512 | 2.596 | 1.023 | 2.963 | -0.691 | - | 7.7 | +19.7% |
| 2 | **CF** | Materials | 1.737 | 1.214 | 1.292 | 1.910 | 0.450 | - | 9.3 | +29.9% |
| 3 | **SNDK** | Information Technology | 1.714 | 1.889 | 1.760 | 0.712 | -0.121 | - | 20.3 | +91.6% |
| 4 | **MO** | Consumer Staples | 1.555 | 0.564 | 2.013 | 1.206 | -0.347 | - | 14.6 | - |
| 5 | **NEM** | Materials | 1.328 | 0.645 | 1.725 | 0.879 | 0.514 | - | 16.6 | +25.9% |
| 6 | **TPR** | Consumer Discretionary | 1.313 | 1.874 | 1.132 | 0.416 | -1.009 | - | 17.9 | +197.1% |
| 7 | **APA** | Energy | 1.283 | 1.149 | 1.261 | 0.840 | -0.360 | - | 8.7 | +26.7% |
| 8 | **MU** | Information Technology | 1.266 | 1.658 | 0.885 | 0.770 | -0.581 | - | 21.2 | +66.6% |
| 9 | **HST** | Real Estate | 1.244 | 1.444 | 0.479 | 1.368 | -0.211 | - | 15.1 | +15.6% |
| 10 | **DVA** | Health Care | 1.228 | 1.402 | 0.200 | 1.681 | -1.468 | - | 15.3 | +88.5% |
| 11 | **SPG** | Real Estate | 1.173 | 1.042 | 1.363 | 0.539 | -1.448 | - | 15.2 | +120.5% |
| 12 | **SYF** | Financials | 1.138 | -0.172 | 1.181 | 1.743 | -0.425 | - | 8.2 | +20.8% |
| 13 | **MAS** | Industrials | 1.122 | -0.169 | 1.436 | 1.410 | -0.842 | - | 17.0 | +5862.5% |
| 14 | **ES** | Utilities | 1.045 | 1.012 | 1.080 | 0.559 | -0.408 | - | 18.6 | +9.0% |
| 15 | **TRV** | Financials | 1.026 | 1.408 | 0.327 | 1.014 | 0.673 | - | 10.0 | +26.5% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -1.986 | -1.637 | -0.916 | -2.560 | -0.996 |
| 502 | **TSLA** | Consumer Discretionary | -1.771 | -0.553 | -1.353 | -2.482 | -0.342 |
| 501 | **CSGP** | Real Estate | -1.636 | -3.308 | -0.456 | -0.690 | 0.629 |
| 500 | **CEG** | Utilities | -1.606 | -2.242 | -0.592 | -1.413 | -0.717 |
| 499 | **BA** | Industrials | -1.605 | -0.645 | -1.140 | -2.217 | -1.198 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W35.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W35.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-08-24  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
