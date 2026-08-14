# Сателит — пълен data export за 2026-W33

_Период: 2026-08-10 → 2026-08-16_  
_Генериран: 2026-08-14 07:26 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W33.md` (structured briefing) и `narrative_2026-W33.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**2 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **XLE** | +6.19% | +1.58σ | 57.50 | 61.06 | 2026-08-07 | 2026-08-13 | +0.31% | +3.73% | 13 |
| **DBC** | +3.01% | +1.10σ | 28.91 | 29.78 | 2026-08-07 | 2026-08-13 | -0.32% | +3.02% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-08-16 · **Conditions matched:** 1/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | +5.98% | ✅ | 117.98 | 125.03 | 2026-08-07 | 2026-08-13 |
| DFEN | down ≥ 3.0% | -1.36% | ❌ | 85.94 | 84.77 | 2026-08-07 | 2026-08-13 |
| GLD | down ≥ 1.0% | +0.12% | ❌ | 398.47 | 398.96 | 2026-08-07 | 2026-08-13 |
| URA | down ≥ 3.0% | +0.76% | ❌ | 44.91 | 45.25 | 2026-08-07 | 2026-08-13 |
| UUP | up ≥ 0.5% | +0.39% | ❌ | 28.07 | 28.18 | 2026-08-07 | 2026-08-13 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-08-16 · **Conditions matched:** 1/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | +0.64% | ❌ | 301.56 | 303.50 | 2026-08-07 | 2026-08-13 |
| XLF | up ≥ 1.0% | +1.15% | ✅ | 57.60 | 58.26 | 2026-08-07 | 2026-08-13 |
| XLY | up ≥ 1.0% | -1.18% | ❌ | 119.86 | 118.45 | 2026-08-07 | 2026-08-13 |
| GLD | down ≥ 0.5% | +0.12% | ❌ | 398.47 | 398.96 | 2026-08-07 | 2026-08-13 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2022-W40 (week ending 2022-10-09)
**Cosine similarity:** 0.9870 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.30% | +6.97% | +12.79% |
| **USO** | -0.84% | -13.68% | -6.44% |
| **GLD** | +0.99% | +10.03% | +18.12% |
| **TLT** | -6.62% | +4.15% | +7.47% |
| **XLE** | +13.79% | +7.04% | +3.89% |
| **IWM** | +6.49% | +5.32% | +3.13% |

### Паралел #2: 2024-W04 (week ending 2024-01-28)
**Cosine similarity:** 0.9709 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.00% | +4.28% | +11.70% |
| **USO** | +1.03% | +9.97% | +4.12% |
| **GLD** | +0.53% | +15.83% | +17.98% |
| **TLT** | -0.91% | -5.91% | -0.84% |
| **XLE** | +1.95% | +13.64% | +9.42% |
| **IWM** | +4.09% | +1.21% | +14.41% |

### Паралел #3: 2021-W22 (week ending 2021-06-06)
**Cosine similarity:** 0.9578 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.44% | +7.21% | +7.29% |
| **USO** | +5.59% | +2.96% | +1.57% |
| **GLD** | -5.10% | -3.44% | -5.94% |
| **TLT** | +4.89% | +5.92% | +10.33% |
| **XLE** | -5.09% | -12.79% | -1.09% |
| **IWM** | -0.68% | +0.25% | -5.58% |

### Паралел #4: 2021-W38 (week ending 2021-09-26)
**Cosine similarity:** 0.9294 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.71% | +6.01% | +1.98% |
| **USO** | +12.79% | +2.53% | +55.81% |
| **GLD** | +2.68% | +3.47% | +11.68% |
| **TLT** | -1.23% | +1.10% | -12.42% |
| **XLE** | +16.19% | +7.86% | +54.72% |
| **IWM** | +2.15% | -0.45% | -7.59% |

### Паралел #5: 2024-W40 (week ending 2024-10-06)
**Cosine similarity:** 0.9268 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.65% | +3.31% | -11.82% |
| **USO** | -2.12% | +2.06% | -11.04% |
| **GLD** | +3.43% | -0.62% | +14.17% |
| **TLT** | -2.94% | -8.64% | -2.83% |
| **XLE** | -3.23% | -6.13% | -15.48% |
| **IWM** | +2.32% | +2.41% | -17.32% |

### Паралел #6: 2021-W34 (week ending 2021-08-29)
**Cosine similarity:** 0.9205 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -3.67% | +1.94% | -2.78% |
| **USO** | +8.83% | +3.07% | +36.66% |
| **GLD** | -4.78% | -1.96% | +3.74% |
| **TLT** | -3.59% | +0.72% | -8.42% |
| **XLE** | +7.26% | +12.72% | +39.69% |
| **IWM** | -2.26% | -1.57% | -10.56% |

### Паралел #7: 2022-W12 (week ending 2022-03-27)
**Cosine similarity:** 0.9193 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -8.08% | -13.83% | -18.72% |
| **USO** | -5.30% | +0.66% | -19.10% |
| **GLD** | -2.77% | -6.74% | -16.10% |
| **TLT** | -4.86% | -12.51% | -17.85% |
| **XLE** | -6.31% | -9.09% | -10.50% |
| **IWM** | -8.92% | -15.05% | -18.83% |

### Паралел #8: 2022-W02 (week ending 2022-01-16)
**Cosine similarity:** 0.9172 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -4.01% | -5.79% | -17.13% |
| **USO** | +7.19% | +32.68% | +22.96% |
| **GLD** | +2.01% | +8.47% | -6.28% |
| **TLT** | -5.01% | -15.02% | -18.27% |
| **XLE** | +5.46% | +23.78% | +6.32% |
| **IWM** | -3.85% | -7.16% | -19.23% |

### Паралел #9: 2021-W40 (week ending 2021-10-10)
**Cosine similarity:** 0.9070 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +6.74% | +6.45% | +2.22% |
| **USO** | +4.51% | +2.16% | +33.60% |
| **GLD** | +4.30% | +2.14% | +10.50% |
| **TLT** | +6.40% | +0.27% | -11.81% |
| **XLE** | +4.35% | +8.43% | +40.59% |
| **IWM** | +8.83% | -2.49% | -10.70% |

### Паралел #10: 2024-W25 (week ending 2024-06-23)
**Cosine similarity:** 0.9011 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.70% | +4.36% | +8.57% |
| **USO** | -2.58% | -7.29% | -7.06% |
| **GLD** | +3.63% | +12.77% | +12.72% |
| **TLT** | -1.53% | +5.24% | -6.01% |
| **XLE** | +0.65% | -1.10% | -6.25% |
| **IWM** | +11.12% | +10.59% | +10.77% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 14 · **Total matching days:** 74 · **History:** 2021-05-17 → 2026-08-13

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 14 | +2.2% | +2.4% | -3.1% | +7.4% | 71% |
| **SPY** | 3m | 14 | +2.9% | +3.4% | -7.3% | +12.0% | 79% |
| **SPY** | 6m | 14 | +8.1% | +10.1% | -6.8% | +21.8% | 79% |
| **USO** | 1m | 14 | +0.4% | +0.0% | -14.3% | +12.7% | 50% |
| **USO** | 3m | 14 | -2.0% | -2.0% | -18.9% | +24.5% | 50% |
| **USO** | 6m | 14 | +10.5% | +0.5% | -17.0% | +109.4% | 57% |
| **GLD** | 1m | 14 | +3.0% | +2.0% | -0.9% | +8.9% | 79% |
| **GLD** | 3m | 14 | +5.8% | +7.1% | -12.6% | +24.5% | 71% |
| **GLD** | 6m | 14 | +7.0% | +9.3% | -12.5% | +25.3% | 71% |
| **TLT** | 1m | 14 | -1.4% | -1.1% | -6.7% | +3.6% | 36% |
| **TLT** | 3m | 14 | -0.6% | -0.1% | -16.5% | +11.1% | 50% |
| **TLT** | 6m | 14 | -4.1% | -3.0% | -18.0% | +7.5% | 29% |

**Episodes (последни 5 от 14):**
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-08-03` (5d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 65 · **History:** 2021-05-17 → 2026-08-13

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +6.3% | +6.3% | +3.5% | +9.1% | 100% |
| **SPY** | 3m | 2 | +6.9% | +6.9% | +3.5% | +10.3% | 100% |
| **SPY** | 6m | 2 | +9.3% | +9.3% | +3.5% | +15.1% | 100% |
| **USO** | 1m | 2 | +5.6% | +5.6% | +4.0% | +7.2% | 100% |
| **USO** | 3m | 2 | -2.9% | -2.9% | -9.9% | +4.0% | 50% |
| **USO** | 6m | 2 | +2.2% | +2.2% | +0.4% | +4.0% | 100% |
| **GLD** | 1m | 2 | +3.5% | +3.5% | -0.2% | +7.2% | 50% |
| **GLD** | 3m | 2 | -3.3% | -3.3% | -13.8% | +7.2% | 50% |
| **GLD** | 6m | 2 | -0.5% | -0.5% | -8.2% | +7.2% | 50% |
| **TLT** | 1m | 2 | -1.4% | -1.4% | -1.8% | -1.0% | 0% |
| **TLT** | 3m | 2 | -2.4% | -2.4% | -2.9% | -1.8% | 0% |
| **TLT** | 6m | 2 | -3.4% | -3.4% | -5.0% | -1.8% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-08-13` (18d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 420 · **History:** 2021-05-17 → 2026-08-13

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
- `2025-11-03 → 2026-08-13` (188d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-08-13

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 9 · **Total matching days:** 86 · **History:** 2021-05-17 → 2026-08-13

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 9 | +0.0% | +0.9% | -7.2% | +7.8% | 56% |
| **SPY** | 3m | 9 | +2.2% | +4.1% | -8.3% | +11.6% | 56% |
| **SPY** | 6m | 9 | +1.6% | +4.1% | -20.8% | +14.3% | 67% |
| **USO** | 1m | 9 | +3.0% | -1.7% | -15.0% | +52.9% | 33% |
| **USO** | 3m | 9 | +7.8% | -0.1% | -20.7% | +52.2% | 44% |
| **USO** | 6m | 9 | +8.1% | -0.2% | -27.6% | +45.8% | 44% |
| **GLD** | 1m | 9 | -1.6% | -1.6% | -8.3% | +5.2% | 22% |
| **GLD** | 3m | 9 | -0.7% | +0.2% | -12.0% | +6.4% | 56% |
| **GLD** | 6m | 9 | +0.2% | -0.8% | -14.8% | +25.0% | 44% |
| **TLT** | 1m | 9 | -2.0% | -2.5% | -6.0% | +2.5% | 11% |
| **TLT** | 3m | 9 | -6.3% | -5.7% | -17.6% | +4.2% | 22% |
| **TLT** | 6m | 9 | -10.1% | -7.8% | -22.3% | +1.2% | 11% |

**Episodes (последни 5 от 9):**
- `2023-04-12 → 2023-04-18` (5d)
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-05-19` (36d)
- `2026-07-22 → 2026-08-03` (8d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 17 · **Total matching days:** 280 · **History:** 2021-05-17 → 2026-08-13

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 17 | +2.0% | +1.6% | -4.8% | +9.0% | 76% |
| **SPY** | 3m | 17 | +3.1% | +4.2% | -12.6% | +16.2% | 76% |
| **SPY** | 6m | 17 | +6.6% | +8.9% | -14.0% | +21.0% | 82% |
| **USO** | 1m | 17 | +1.5% | -2.2% | -13.0% | +22.9% | 41% |
| **USO** | 3m | 17 | +2.3% | -0.8% | -14.5% | +29.9% | 41% |
| **USO** | 6m | 17 | +11.3% | +2.6% | -12.4% | +87.1% | 71% |
| **GLD** | 1m | 17 | +2.3% | +1.4% | -5.6% | +9.0% | 76% |
| **GLD** | 3m | 17 | +5.9% | +7.2% | -16.8% | +23.6% | 71% |
| **GLD** | 6m | 17 | +10.7% | +9.8% | -9.8% | +43.8% | 76% |
| **TLT** | 1m | 17 | +0.3% | -0.0% | -6.3% | +8.2% | 47% |
| **TLT** | 3m | 17 | -1.5% | -1.1% | -15.3% | +11.9% | 35% |
| **TLT** | 6m | 17 | -4.4% | -1.7% | -21.3% | +7.0% | 35% |

**Episodes (последни 5 от 17):**
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)
- `2026-08-07 → 2026-08-13` (5d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 19 · **Total matching days:** 288 · **History:** 2021-05-17 → 2026-08-13

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 19 | +0.4% | +1.0% | -8.7% | +7.0% | 53% |
| **SPY** | 3m | 19 | +2.2% | +3.6% | -13.7% | +9.1% | 68% |
| **SPY** | 6m | 19 | +3.5% | +6.8% | -16.4% | +16.9% | 74% |
| **USO** | 1m | 19 | -0.6% | -5.6% | -21.8% | +55.8% | 42% |
| **USO** | 3m | 19 | +3.2% | -1.3% | -12.7% | +64.3% | 42% |
| **USO** | 6m | 19 | +8.0% | -5.2% | -16.0% | +75.1% | 47% |
| **GLD** | 1m | 19 | -0.6% | -0.1% | -12.4% | +7.6% | 47% |
| **GLD** | 3m | 19 | +1.8% | +1.3% | -13.7% | +19.0% | 68% |
| **GLD** | 6m | 19 | +7.8% | +6.0% | -15.8% | +55.5% | 74% |
| **TLT** | 1m | 19 | -0.2% | -0.1% | -5.6% | +5.2% | 47% |
| **TLT** | 3m | 19 | -3.6% | -4.4% | -17.3% | +8.7% | 32% |
| **TLT** | 6m | 19 | -6.9% | -8.0% | -21.4% | +4.6% | 21% |

**Episodes (последни 5 от 19):**
- `2025-05-12 → 2025-05-19` (3d)
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (13d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-08-13

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (13 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | 5 | 2.52 | 2.70 | 2026-07-11 00:00:00 | 2026-08-08 00:00:00 | ✓ |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 5 | 2.41 | 2.71 | 2026-07-11 00:00:00 | 2026-08-08 00:00:00 | ✓ |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 5 | 2.32 | 2.43 | 2026-07-11 00:00:00 | 2026-08-08 00:00:00 | - |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 5 | 2.30 | 2.89 | 2026-07-11 00:00:00 | 2026-08-08 00:00:00 | - |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 5 | 2.28 | 2.28 | 2026-07-11 00:00:00 | 2026-08-08 00:00:00 | ✓ |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | 5 | 2.06 | 2.22 | 2026-07-11 00:00:00 | 2026-08-08 00:00:00 | - |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | 4 | 2.28 | 2.28 | 2026-07-18 00:00:00 | 2026-08-08 00:00:00 | ✓ |
| **JTSQUR** | Quits rate — напускания | labor | flow | 4 | 2.02 | 2.02 | 2026-07-11 00:00:00 | 2026-08-01 00:00:00 | ✓ |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 3 | 2.39 | 2.56 | 2026-07-11 00:00:00 | 2026-08-08 00:00:00 | - |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | 2 | 2.09 | 2.09 | 2026-08-01 00:00:00 | 2026-08-08 00:00:00 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | 1 | 2.58 | 2.58 | 2026-07-11 00:00:00 | 2026-07-11 00:00:00 | - |
| **CSUSHPISA** | Case-Shiller US National HPI (SA) | housing | housing_prices | 1 | 2.17 | 2.17 | 2026-07-11 00:00:00 | 2026-07-11 00:00:00 | - |
| **MSACSR** | Месеци предлагане — нови жилища | housing | housing_affordability | 1 | 2.02 | 2.02 | 2026-07-18 00:00:00 | 2026-07-18 00:00:00 | ✓ |

### EU (6 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.27 | 5.27 | 2026-07-11 00:00:00 | 2026-08-08 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.15 | 2.15 | 2026-07-11 00:00:00 | 2026-08-08 00:00:00 | - |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.15 | 2.15 | 2026-07-11 00:00:00 | 2026-08-08 00:00:00 | - |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | 4 | 2.38 | 2.38 | 2026-07-18 00:00:00 | 2026-08-08 00:00:00 | - |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | 3 | 2.66 | 2.66 | 2026-07-11 00:00:00 | 2026-07-25 00:00:00 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation | sentiment | 3 | 2.17 | 2.17 | 2026-07-11 00:00:00 | 2026-07-25 00:00:00 | - |

### CN (2 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 6 | 2.55 | 2.56 | 2026-07-13 00:00:00 | 2026-08-10 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 6 | 2.23 | 2.23 | 2026-07-13 00:00:00 | 2026-08-10 00:00:00 | ✓ |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-08-08 00:00:00 · **Generated:** 2026-08-08 07:52:18.096400+00:00

**Режим:** `transition` (Преходно / смесено)  
**Primary driver:** `none`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 36.9 | contracting | 22.2% | 3 | 2 |
| **growth** | 45.9 | mixed | 40.0% | 2 | 1 |
| **inflation** | 39.3 | mixed | 38.9% | 4 | 2 |
| **liquidity** | 50.5 | mixed | 47.4% | 0 | 0 |

### Top anomalies (9 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.71 | down | 93.55 | 2026-04-01 | ✓ min |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | -2.70 | down | 61.40 | 2026-07-01 | ✓ min |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | -2.30 | down | 2.24 | 2026-05-01 | - |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | +2.28 | up | 55.10 | 2026-05-01 | ✓ max |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | -2.28 | down | 0.13 | 2026-06-01 | ✓ min |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | -2.22 | down | 58.90 | 2026-07-01 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | +2.16 | up | 4.60 | 2026-06-01 | - |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | +2.15 | up | 5.51 | 2026-06-01 | - |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | -2.09 | down | 2.70 | 2026-06-01 | - |

### Narrative hints от макро лещите
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **CIVPART**: Структурни сдвигове (демография, ранно пенсиониране). Пост-COVID не се възстанови напълно.
- **HPIPONM226S**: Monthly FHFA версия. Само purchase transactions (без refi appraisals). По-чист от refi-bias.
- **US_PMI_MFG**: Markit mfg — comparable cross-country. ISM е US-only.
- **TRIMMED_MEAN_CPI**: Орязва 8% в опашките (топ и долу). По-стабилна от median при многоизмерен shock.
- **EMRATIO**: Не зависи от definition на 'active labor force'. По-стабилен индикатор на дълбоката заетост.
- **MICH_INFL_1Y**: Household очаквания. По-шумни от market-based, но по-ранни. Extreme movements сигнализират de-anchoring risk.
- **PPIFIS**: Производствени цени → consumer prices с 1-3 месечен lag. Водещ за CPI при трендови промени.
- **PSAVERT**: Hard data компонент. Скочи >30% в COVID — когато survey и hard data разминават, сигналът укрепва.

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
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.333
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
  - `breadth_a_raw`: 1.0
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
  - `state_raw`: both_down
  - `breadth_a_raw`: 0.333
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
  - `breadth_b`: 0.833
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.0
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
  - `breadth_b_raw`: 1.0
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
> Сигналите са в преход — няма доминираща конфигурация. Следващите 2-3 релиза ще ориентират посоката. Най-отклонена леща: Инфлация и цени — breadth 29% (свиване), 4 аномалии, 2 нови екстремума. За наблюдение следващия релиз: LABOR_SHARE_NBS, CIVPART, US_PMI_MFG (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: LABOR_SHARE_NBS z=-2.71 · NEW-5Y-MIN
- 4 нови екстремуми в top-9 (lookback 5г.)
- Активни двойки: Inflation anchoring=both_down; Credit × Policy=a_down_b_up; model_vs_market=both_down



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-08-08 00:00:00 · **Generated:** 2026-08-08 08:06:39.487937+00:00

**Режим:** `policy_dilemma` (Policy dilemma)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 39.7 | mixed | 42.9% | 0 | 0 |
| **growth** | 41.3 | mixed | 16.7% | 0 | 0 |
| **inflation** | 49.6 | mixed | 71.4% | 0 | 0 |
| **credit** | 45.4 | mixed | 36.8% | 3 | 0 |
| **external** | 13.5 | contracting | 16.7% | 1 | 0 |

### Top anomalies (4 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | +5.27 | up | 2.83 | 2026-07-01 | - |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | -2.38 | down | -4969.90 | 2026-05-01 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | +2.15 | up | 3.68 | 2026-06-01 | - |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | +2.15 | up | 2.96 | 2026-06-01 | - |

### Narrative hints от макро лещите
- **EA_BUND_2Y**: EA-aggregate 2Y yield. Curve slope (10Y-2Y) проксира policy expectations и recession risk.
- **EA_TRADE_BALANCE**: Стоковият баланс с третите страни. Срив към дефицит (2022) = енергийната сметка изпреварва износа. Полярност +1.
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
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.667
  - `breadth_b_raw`: 0.75
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
  - `breadth_a_raw`: 0.75
  - `breadth_b_raw`: 1.0

### Executive narrative
> Policy dilemma — labor market е loose, но инфлацията remains hot. ЕЦБ е заклещена между инфлацията и растежа. Най-отклонена леща: Инфлация и цени — breadth 83% (разширяване), 0 аномалии, 0 нови екстремума. За наблюдение: EA_BUND_2Y (z=+5.27) — най-силното отклонение.

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.27
- Активни двойки: Stagflation test=a_down_b_up



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-08-10 00:00:00 · **Generated:** 2026-08-10 07:08:49.119156+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 39.2 | mixed | -% | - | - |
| **inflation** | 44.9 | mixed | -% | - | - |
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
  - `breadth_a`: 0.833
  - `breadth_b`: 0.667

### Executive narrative
> Претеглен композитен macro score 38.4/100 → режим „ВЛОШАВАЩ СЕ“ (5/5 лещи). 5 лещи, 2 flagged аномалии (4 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-08-07 |
| `as_of` | 2026-08-07 |
| `regime` | REFLATION |
| `alignment_score` | 5.0 |
| `gms_score` | 2.0 |
| `gms_max` | 8 |
| `gms_tier` | LOW |
| `ks_status` | inactive |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-08-07 → 2026-08-12)

**stable_winner (1m):** +8 entered, -8 exited
  - **Entered:** ADM, F, GEV, GM, GS, RF, STX, WDC _(включително 1 за първи път в историята: RF)_
  - **Exited:** BEN, CASY, DG, HCA, HOOD, O, SPG, VRT

**stable_winner (3m):** +6 entered, -2 exited
  - **Entered:** AES, BG, GS, KEY, NEE, RL
  - **Exited:** EBAY, EXPE

**quality_dip (1m):** +6 entered, -9 exited
  - **Entered:** BEN, CASY, GNRC, NUE, SPG, VRT _(включително 2 за първи път в историята: GNRC, NUE)_
  - **Exited:** ADM, F, GEV, GM, GS, RF, STX, TER, WDC

**quality_dip (3m):** +4 entered, -11 exited
  - **Entered:** EBAY, EXPE, GNRC, NUE _(включително 2 за първи път в историята: GNRC, NUE)_
  - **Exited:** AES, BG, DG, GS, HCA, HOOD, KEY, NEE, O, RL, TER

**faded_bounce (1m):** +6 entered, -7 exited
  - **Entered:** ADP, DPZ, DXCM, FDS, LII, VLTO
  - **Exited:** ARE, BSX, CMS, FISV, KMB, UBER, ZTS

**faded_bounce (3m):** +4 entered, -7 exited
  - **Entered:** EXE, GPN, LII, PYPL
  - **Exited:** ARE, CMS, CNC, DASH, LEN, PEG, SO

### EU (period: 2026-08-07 → 2026-08-12)

**stable_winner (1m):** +6 entered, -7 exited
  - **Entered:** BCP.LS, ELI.BR, FLS.CO, IHG.L, PKN.WA, REP.MC _(включително 1 за първи път в историята: FLS.CO)_
  - **Exited:** AIXA.DE, ASML.AS, AXFO.ST, BIRG.IR, GL9.IR, HOT.DE, SAN.MC

**stable_winner (3m):** +2 entered, -5 exited
  - **Entered:** METSO.HE, UMI.BR
  - **Exited:** A5G.IR, BIRG.IR, FTK.DE, MOBN.SW, RBI.VI

**quality_dip (1m):** +7 entered, -8 exited
  - **Entered:** AIXA.DE, ASML.AS, BIRG.IR, GL9.IR, HOT.DE, IGG.L, SAN.MC _(включително 1 за първи път в историята: IGG.L)_
  - **Exited:** AZM.MI, BCP.LS, ELI.BR, FLS.CO, IHG.L, ORA.PA, PKN.WA, REP.MC

**quality_dip (3m):** +6 entered, -5 exited
  - **Entered:** A5G.IR, BIRG.IR, FTK.DE, IGG.L, MOBN.SW, RBI.VI _(включително 1 за първи път в историята: IGG.L)_
  - **Exited:** AXFO.ST, AZM.MI, METSO.HE, ORA.PA, UMI.BR

**faded_bounce (3m):** +1 entered, -0 exited
  - **Entered:** MNDI.L



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-08-04 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **copper** | Commodities | 77796 | 95.2 | 95.2 | 1052 | 17399 |
| **soyoil** | Commodities | 80681 | 88.6 | 88.6 | 1052 | -8547 |
| **soymeal** | Commodities | 77451 | 88.5 | 88.5 | 1052 | 58426 |
| **brent** | Commodities | 16795 | 88.5 | 88.5 | 234 | 9188 |
| **vix** | Volatility | 3773 | 85.4 | 85.4 | 1011 | -1339 |
| **cotton** | Commodities | 62279 | 82.4 | 82.4 | 1052 | 23173 |
| **rbob** | Commodities | 69824 | 81.3 | 81.3 | 1052 | -1719 |
| **gbpfx** | FX | 38174 | 78.4 | 78.4 | 1052 | 20195 |
| **aud** | FX | 40637 | 75.4 | 75.4 | 1052 | 10954 |
| **soybeans** | Commodities | 125466 | 74.1 | 74.1 | 1052 | 56787 |
| **dxy** | FX | 3849 | 70.7 | 70.7 | 1052 | 8303 |
| **corn** | Commodities | 181946 | 67.0 | 67.0 | 1052 | 169287 |
| **coffee** | Commodities | 23550 | 61.6 | 61.6 | 1052 | -1961 |
| **gold** | Commodities | 132398 | 57.3 | 57.3 | 1052 | 17544 |
| **cattle** | Commodities | 66067 | 54.9 | 54.9 | 1052 | -47254 |
| **platinum** | Commodities | 10882 | 49.2 | 49.2 | 1052 | 3406 |
| **wheat** | Commodities | -23786 | 45.9 | 45.9 | 1052 | 38539 |
| **heatingoil** | Commodities | 11279 | 44.3 | 44.3 | 1052 | 6476 |
| **sp500** | US Equities | -329999 | 40.3 | 40.3 | 1052 | 31876 |
| **bitcoin** | Crypto | -7240 | 32.6 | 32.6 | 435 | -523 |
| **eurfx** | FX | -52205 | 28.8 | 28.8 | 1052 | -6744 |
| **silver** | Commodities | 11067 | 28.0 | 28.0 | 1052 | -1064 |
| **chf** | FX | -10084 | 23.9 | 23.9 | 1052 | -2866 |
| **jpy** | FX | -60825 | 22.0 | 22.0 | 1052 | 29258 |
| **wti** | Commodities | 101050 | 20.8 | 20.8 | 1052 | 26371 |
| **natgas** | Commodities | -105605 | 16.8 | 16.8 | 1051 | -40551 |
| **us2y** | Rates | -1334181 | 16.6 | 16.6 | 1052 | 422347 |
| **russell** | US Equities | -85145 | 15.3 | 15.3 | 588 | -12883 |
| **cocoa** | Commodities | -11914 | 14.3 | 14.3 | 1052 | 1836 |
| **sugar** | Commodities | -77814 | 13.9 | 13.9 | 1052 | 19899 |
| **us30y** | Rates | -376226 | 11.6 | 11.6 | 1052 | -10743 |
| **palladium** | Commodities | -5429 | 11.3 | 11.3 | 1052 | 953 |
| **us5y** | Rates | -2211439 | 10.8 | 10.8 | 1052 | -36577 |
| **hogs** | Commodities | -9642 | 4.3 | 4.3 | 1052 | 19360 |
| **nasdaq** | US Equities | -78333 | 2.4 | 2.4 | 1052 | -23320 |
| **us10y** | Rates | -2231670 | 2.4 | 2.4 | 1052 | -227647 |
| **usultra10y** | Rates | -419861 | 2.2 | 2.2 | 542 | -68361 |
| **cad** | FX | -101748 | 0.4 | 0.4 | 1052 | -15791 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **DELL** | Technology | 98.3 | 6.1% | 103.1% | 286.3% | 234.4% | 1.78 | -32.3% |
| 2 | **HPE** | Technology | 97.7 | 18.6% | 95.2% | 147.6% | 145.7% | 1.99 | -26.4% |
| 3 | **PANW** | Technology | 97.5 | 9.7% | 79.5% | 133.8% | 109.8% | 1.91 | -36.0% |
| 4 | **CRWD** | Technology | 96.1 | 5.2% | 62.4% | 114.6% | 97.7% | 1.44 | -37.2% |
| 5 | **FTNT** | Technology | 95.6 | -3.6% | 41.2% | 88.0% | 123.7% | 1.86 | -30.9% |
| 6 | **VLO** | Energy | 95.1 | 10.0% | 34.8% | 67.0% | 132.7% | 2.50 | -14.2% |
| 7 | **MPC** | Energy | 94.6 | 14.8% | 38.7% | 72.1% | 95.1% | 2.24 | -18.3% |
| 8 | **MRVL** | Technology | 94.4 | -2.4% | 32.0% | 164.9% | 188.4% | 1.28 | -48.4% |
| 9 | **AMAT** | Technology | 94.1 | -8.0% | 27.3% | 67.0% | 225.4% | 1.76 | -39.6% |
| 10 | **MU** | Technology | 94.0 | -7.3% | 18.9% | 144.3% | 695.9% | 2.44 | -39.1% |
| 11 | **NTAP** | Technology | 93.0 | 15.8% | 74.4% | 92.8% | 67.7% | 1.48 | -24.8% |
| 12 | **DDOG** | Technology | 90.1 | -11.0% | 20.5% | 85.8% | 110.2% | 0.88 | -48.6% |
| 13 | **PSX** | Energy | 90.1 | 12.0% | 29.5% | 45.6% | 76.0% | 2.06 | -17.3% |
| 14 | **STX** | Technology | 90.1 | -0.0% | 8.7% | 122.2% | 483.8% | 2.40 | -31.8% |
| 15 | **CRL** | Healthcare | 89.9 | 23.0% | 68.6% | 56.9% | 55.2% | 1.32 | -33.9% |
| 16 | **CNC** | Healthcare | 89.6 | -2.4% | 13.1% | 69.3% | 172.2% | 1.89 | -32.7% |
| 17 | **STT** | Financial Services | 89.4 | 3.5% | 27.0% | 45.5% | 71.5% | 2.15 | -11.8% |
| 18 | **MRNA** | Healthcare | 89.3 | -5.6% | 19.5% | 51.6% | 164.8% | 1.28 | -35.5% |
| 19 | **AMD** | Technology | 89.1 | -11.9% | 7.7% | 126.1% | 218.2% | 1.40 | -27.8% |
| 20 | **CSCO** | Technology | 88.6 | 5.8% | 25.2% | 44.9% | 69.1% | 1.63 | -15.3% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **ATS.VI** | Technology | 96.3 | -17.2% | 45.0% | 195.5% | 775.2% | 2.51 | -50.1% |
| 2 | **TPRO.MI** | Technology | 95.3 | -8.0% | 47.5% | 65.3% | 403.5% | 2.41 | -32.2% |
| 3 | **RBI.VI** | Financial Services | 89.8 | 12.3% | 30.0% | 46.3% | 88.3% | 1.91 | -18.0% |
| 4 | **AKER.OL** | Industrials | 89.8 | 10.5% | 20.6% | 61.3% | 92.4% | 2.37 | -15.6% |
| 5 | **CCC.L** | Technology | 89.6 | 6.3% | 21.3% | 56.4% | 95.8% | 2.14 | -16.2% |
| 6 | **UNI.MI** | Financial Services | 88.4 | 8.4% | 34.3% | 58.2% | 54.9% | 1.88 | -11.5% |
| 7 | **BMPS.MI** | Financial Services | 88.0 | 4.7% | 39.0% | 54.6% | 55.9% | 1.40 | -25.5% |
| 8 | **REP.MC** | Energy | 87.7 | 8.6% | 17.0% | 52.6% | 86.6% | 2.12 | -20.4% |
| 9 | **SSAB-B.ST** | Basic Materials | 87.2 | 5.1% | 25.7% | 37.4% | 81.8% | 1.80 | -34.3% |
| 10 | **ASML.AS** | Technology | 86.4 | 1.0% | 13.8% | 29.1% | 140.9% | 2.04 | -20.8% |
| 11 | **PKN.WA** | Energy | 86.4 | 6.4% | 12.4% | 49.0% | 95.0% | 2.13 | -12.3% |
| 12 | **DHER.DE** | Consumer Cyclical | 86.4 | 0.3% | 31.3% | 69.5% | 55.0% | 0.72 | -48.7% |
| 13 | **BFT.WA** | Industrials | 85.8 | 10.3% | 39.2% | 40.8% | 47.8% | 1.73 | -17.4% |
| 14 | **GL9.IR** | Consumer Defensive | 84.9 | -0.7% | 15.1% | 41.6% | 72.7% | 2.14 | -10.0% |
| 15 | **BG.VI** | Financial Services | 84.8 | 3.4% | 22.6% | 35.3% | 63.8% | 1.93 | -16.3% |
| 16 | **IFCN.SW** | Technology | 84.5 | 2.7% | 14.5% | 46.6% | 75.9% | 1.36 | -25.5% |
| 17 | **BAMI.MI** | Financial Services | 83.9 | 8.3% | 27.2% | 42.1% | 45.4% | 1.67 | -14.8% |
| 18 | **ACX.MC** | Basic Materials | 83.9 | 12.9% | 25.8% | 32.7% | 57.2% | 1.71 | -14.9% |
| 19 | **SUBC.OL** | Energy | 83.3 | 0.2% | 8.4% | 43.1% | 81.8% | 1.84 | -13.2% |
| 20 | **UNI.MC** | Financial Services | 83.3 | 8.7% | 28.8% | 36.4% | 45.0% | 1.73 | -17.8% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **EIX** | Utilities | 2.350 | 2.109 | 1.025 | 2.998 | -0.669 | - | 7.3 | +19.7% |
| 2 | **SNDK** | Information Technology | 1.759 | 1.809 | 1.775 | 0.877 | 0.000 | - | 20.7 | +91.6% |
| 3 | **CF** | Materials | 1.704 | 1.143 | 1.291 | 1.904 | 0.475 | - | 8.7 | +29.9% |
| 4 | **MO** | Consumer Staples | 1.616 | 0.549 | 2.035 | 1.368 | -0.376 | - | 13.7 | - |
| 5 | **NEM** | Materials | 1.466 | 0.840 | 1.696 | 1.101 | 0.484 | - | 14.4 | +25.9% |
| 6 | **MU** | Information Technology | 1.292 | 1.584 | 0.894 | 0.886 | -0.601 | - | 21.5 | +66.6% |
| 7 | **APA** | Energy | 1.285 | 1.171 | 1.264 | 0.823 | -0.288 | - | 8.4 | +26.7% |
| 8 | **DVA** | Health Care | 1.226 | 1.435 | 0.196 | 1.654 | -1.510 | - | 15.2 | +88.5% |
| 9 | **HST** | Real Estate | 1.221 | 1.418 | 0.479 | 1.331 | -0.237 | - | 15.3 | +15.6% |
| 10 | **SYF** | Financials | 1.187 | -0.029 | 1.184 | 1.764 | -0.454 | - | 8.2 | +20.8% |
| 11 | **MAS** | Industrials | 1.166 | -0.009 | 1.439 | 1.398 | -0.843 | - | 17.2 | +5862.5% |
| 12 | **SPG** | Real Estate | 1.133 | 0.969 | 1.366 | 0.494 | -1.038 | - | 15.6 | +124.3% |
| 13 | **EXPE** | Consumer Discretionary | 0.990 | 1.491 | 0.807 | 0.286 | -0.709 | - | 20.7 | +89.5% |
| 14 | **ES** | Utilities | 0.978 | 0.564 | 1.083 | 0.790 | -0.429 | - | 15.5 | +9.0% |
| 15 | **WDC** | Information Technology | 0.960 | 1.471 | 0.783 | 0.256 | -0.675 | - | 20.1 | +130.8% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -2.005 | -1.734 | -0.905 | -2.552 | -1.174 |
| 502 | **CSGP** | Real Estate | -1.728 | -3.589 | -0.453 | -0.645 | 0.497 |
| 501 | **CEG** | Utilities | -1.683 | -2.594 | -0.585 | -1.293 | -0.800 |
| 500 | **COIN** | Financials | -1.647 | -2.467 | -1.729 | 0.000 | -1.596 |
| 499 | **KKR** | Financials | -1.623 | -1.588 | -0.851 | -1.757 | -0.942 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W33.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W33.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-08-10  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
