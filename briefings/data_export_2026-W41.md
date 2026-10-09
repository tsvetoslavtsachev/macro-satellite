# Сателит — пълен data export за 2026-W41

_Период: 2026-10-05 → 2026-10-11_  
_Генериран: 2026-10-09 12:42 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W41.md` (structured briefing) и `narrative_2026-W41.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**12 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **XLP** | +3.59% | +4.04σ | 80.53 | 83.42 | 2026-10-02 | 2026-10-08 | -0.41% | +0.99% | 13 |
| **XLU** | +3.11% | +2.00σ | 39.83 | 41.07 | 2026-10-02 | 2026-10-08 | -1.04% | +2.08% | 13 |
| **TIP** | +0.39% | +1.91σ | 104.11 | 104.52 | 2026-10-02 | 2026-10-08 | -0.30% | +0.37% | 13 |
| **IEF** | +0.45% | +1.81σ | 89.05 | 89.45 | 2026-10-02 | 2026-10-08 | -0.42% | +0.48% | 13 |
| **SHY** | +0.19% | +1.74σ | 81.05 | 81.20 | 2026-10-02 | 2026-10-08 | -0.08% | +0.15% | 13 |
| **LQD** | +0.63% | +1.68σ | 101.83 | 102.47 | 2026-10-02 | 2026-10-08 | -0.49% | +0.67% | 13 |
| **VEA** | -1.79% | -1.34σ | 71.13 | 69.86 | 2026-10-02 | 2026-10-08 | +0.04% | +1.37% | 13 |
| **EEM** | -2.32% | -1.28σ | 67.67 | 66.10 | 2026-10-02 | 2026-10-08 | +0.25% | +2.01% | 13 |
| **XLF** | +1.38% | +1.25σ | 53.49 | 54.23 | 2026-10-02 | 2026-10-08 | -0.29% | +1.34% | 13 |
| **HYG** | +0.30% | +1.25σ | 76.91 | 77.14 | 2026-10-02 | 2026-10-08 | -0.27% | +0.46% | 13 |
| **TLT** | +0.50% | +1.18σ | 77.48 | 77.87 | 2026-10-02 | 2026-10-08 | -0.75% | +1.06% | 13 |
| **SOXX** | -4.35% | -1.00σ | 588.90 | 563.28 | 2026-10-02 | 2026-10-08 | +0.42% | +4.76% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-10-11 · **Conditions matched:** 2/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | +0.14% | ❌ | 147.37 | 147.58 | 2026-10-02 | 2026-10-08 |
| DFEN | down ≥ 3.0% | -4.34% | ✅ | 47.44 | 45.38 | 2026-10-02 | 2026-10-08 |
| GLD | down ≥ 1.0% | -0.40% | ❌ | 380.14 | 378.62 | 2026-10-02 | 2026-10-08 |
| URA | down ≥ 3.0% | -3.09% | ✅ | 39.79 | 38.56 | 2026-10-02 | 2026-10-08 |
| UUP | up ≥ 0.5% | +0.31% | ❌ | 28.89 | 28.98 | 2026-10-02 | 2026-10-08 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-10-11 · **Conditions matched:** 2/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | -1.40% | ❌ | 281.52 | 277.57 | 2026-10-02 | 2026-10-08 |
| XLF | up ≥ 1.0% | +1.38% | ✅ | 53.49 | 54.23 | 2026-10-02 | 2026-10-08 |
| XLY | up ≥ 1.0% | +1.52% | ✅ | 110.04 | 111.71 | 2026-10-02 | 2026-10-08 |
| GLD | down ≥ 0.5% | -0.40% | ❌ | 380.14 | 378.62 | 2026-10-02 | 2026-10-08 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2022-W01 (week ending 2022-01-09)
**Cosine similarity:** 0.8252 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -3.25% | -3.97% | -16.61% |
| **USO** | +12.26% | +30.77% | +38.59% |
| **GLD** | +1.72% | +8.18% | -3.25% |
| **TLT** | -2.88% | -12.05% | -20.92% |
| **XLE** | +11.31% | +29.65% | +15.67% |
| **IWM** | -6.16% | -8.42% | -18.73% |

### Паралел #2: 2023-W32 (week ending 2023-08-13)
**Cosine similarity:** 0.7976 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.08% | -1.13% | +12.46% |
| **USO** | +7.34% | -3.31% | -3.47% |
| **GLD** | -0.06% | +1.08% | +5.63% |
| **TLT** | -1.20% | -7.74% | -1.59% |
| **XLE** | +3.43% | -7.22% | -7.33% |
| **IWM** | -3.57% | -11.46% | +4.37% |

### Паралел #3: 2021-W22 (week ending 2021-06-06)
**Cosine similarity:** 0.7271 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.44% | +7.21% | +7.29% |
| **USO** | +5.59% | +2.96% | +1.57% |
| **GLD** | -5.10% | -3.44% | -5.94% |
| **TLT** | +4.89% | +5.92% | +10.33% |
| **XLE** | -5.09% | -12.79% | -1.09% |
| **IWM** | -0.68% | +0.25% | -5.58% |

### Паралел #4: 2025-W12 (week ending 2025-03-23)
**Cosine similarity:** 0.7090 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -6.51% | +5.37% | +17.68% |
| **USO** | -5.99% | +12.64% | -0.37% |
| **GLD** | +11.71% | +11.36% | +21.79% |
| **TLT** | -4.65% | -4.64% | -1.85% |
| **XLE** | -12.03% | -3.83% | -4.32% |
| **IWM** | -8.01% | +2.66% | +19.23% |

### Паралел #5: 2022-W04 (week ending 2022-01-30)
**Cosine similarity:** 0.7011 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -2.71% | -6.78% | -6.78% |
| **USO** | +15.89% | +24.51% | +25.95% |
| **GLD** | +8.69% | +5.87% | -1.80% |
| **TLT** | -1.28% | -16.54% | -17.96% |
| **XLE** | +8.62% | +14.51% | +19.49% |
| **IWM** | +2.17% | -5.28% | -4.10% |

### Паралел #6: 2021-W39 (week ending 2021-10-03)
**Cosine similarity:** 0.6907 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +6.37% | +9.38% | +4.30% |
| **USO** | +8.02% | +2.07% | +39.26% |
| **GLD** | +1.56% | +3.87% | +9.06% |
| **TLT** | +1.20% | +1.95% | -8.92% |
| **XLE** | +7.56% | +3.08% | +43.13% |
| **IWM** | +5.48% | +0.08% | -6.62% |

### Паралел #7: 2022-W18 (week ending 2022-05-08)
**Cosine similarity:** 0.6896 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.07% | +0.52% | -8.51% |
| **USO** | +9.63% | -12.89% | -6.47% |
| **GLD** | -1.41% | -5.77% | -10.80% |
| **TLT** | +1.28% | +2.46% | -17.11% |
| **XLE** | +11.05% | -11.87% | +10.25% |
| **IWM** | +4.56% | +4.50% | -2.14% |

### Паралел #8: 2021-W40 (week ending 2021-10-10)
**Cosine similarity:** 0.6683 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +6.74% | +6.45% | +2.22% |
| **USO** | +4.51% | +2.16% | +33.60% |
| **GLD** | +4.30% | +2.14% | +10.50% |
| **TLT** | +6.40% | +0.27% | -11.81% |
| **XLE** | +4.35% | +8.43% | +40.59% |
| **IWM** | +8.83% | -2.49% | -10.70% |

### Паралел #9: 2023-W29 (week ending 2023-07-23)
**Cosine similarity:** 0.6561 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -3.10% | -6.85% | +6.69% |
| **USO** | +4.77% | +16.97% | -0.25% |
| **GLD** | -3.34% | +0.77% | +3.16% |
| **TLT** | -8.36% | -18.18% | -7.51% |
| **XLE** | +3.88% | +7.07% | -4.90% |
| **IWM** | -5.47% | -14.41% | -1.04% |

### Паралел #10: 2024-W22 (week ending 2024-06-02)
**Cosine similarity:** 0.6073 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.10% | +6.89% | +14.26% |
| **USO** | +8.41% | -0.64% | -4.29% |
| **GLD** | +0.12% | +7.43% | +14.07% |
| **TLT** | +0.18% | +6.68% | +3.89% |
| **XLE** | -2.22% | -2.06% | +2.50% |
| **IWM** | -1.89% | +6.95% | +17.54% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 15 · **Total matching days:** 88 · **History:** 2021-05-17 → 2026-10-08

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 15 | +2.2% | +2.1% | -3.1% | +7.4% | 73% |
| **SPY** | 3m | 15 | +2.8% | +2.5% | -7.3% | +12.0% | 80% |
| **SPY** | 6m | 15 | +7.4% | +8.8% | -6.8% | +21.8% | 80% |
| **USO** | 1m | 15 | +0.0% | -0.8% | -14.3% | +12.7% | 47% |
| **USO** | 3m | 15 | -1.1% | -4.1% | -18.9% | +24.5% | 47% |
| **USO** | 6m | 15 | +13.2% | +0.0% | -8.7% | +109.4% | 53% |
| **GLD** | 1m | 15 | +2.6% | +0.9% | -4.5% | +9.0% | 73% |
| **GLD** | 3m | 15 | +4.8% | +3.1% | -12.6% | +24.5% | 67% |
| **GLD** | 6m | 15 | +5.4% | +4.5% | -12.5% | +25.3% | 67% |
| **TLT** | 1m | 15 | -1.6% | -1.1% | -6.7% | +3.6% | 33% |
| **TLT** | 3m | 15 | -1.1% | -0.5% | -16.5% | +11.1% | 47% |
| **TLT** | 6m | 15 | -5.0% | -6.0% | -18.0% | +7.5% | 27% |

**Episodes (последни 5 от 15):**
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-08-03` (5d)
- `2026-09-10 → 2026-10-01` (14d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 103 · **History:** 2021-05-17 → 2026-10-08

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +6.3% | +6.3% | +3.5% | +9.1% | 100% |
| **SPY** | 3m | 2 | +6.6% | +6.6% | +2.9% | +10.3% | 100% |
| **SPY** | 6m | 2 | +9.0% | +9.0% | +2.9% | +15.0% | 100% |
| **USO** | 1m | 2 | +5.6% | +5.6% | +4.0% | +7.2% | 100% |
| **USO** | 3m | 2 | +6.4% | +6.4% | -9.9% | +22.8% | 50% |
| **USO** | 6m | 2 | +19.2% | +19.2% | +15.5% | +22.8% | 100% |
| **GLD** | 1m | 2 | +3.5% | +3.5% | -0.2% | +7.2% | 50% |
| **GLD** | 3m | 2 | -6.0% | -6.0% | -13.8% | +1.7% | 50% |
| **GLD** | 6m | 2 | -5.9% | -5.9% | -13.5% | +1.7% | 50% |
| **TLT** | 1m | 2 | -1.4% | -1.4% | -1.8% | -1.0% | 0% |
| **TLT** | 3m | 2 | -5.2% | -5.2% | -7.4% | -2.9% | 0% |
| **TLT** | 6m | 2 | -9.3% | -9.3% | -11.2% | -7.4% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-10-08` (56d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 459 · **History:** 2021-05-17 → 2026-10-08

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
- `2025-11-03 → 2026-10-08` (227d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 1 · **Total matching days:** 1 · **History:** 2021-05-17 → 2026-10-08

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | +0.3% | +0.3% | +0.3% | +0.3% | 100% |
| **SPY** | 3m | 1 | +0.3% | +0.3% | +0.3% | +0.3% | 100% |
| **SPY** | 6m | 1 | +0.3% | +0.3% | +0.3% | +0.3% | 100% |
| **USO** | 1m | 1 | -0.5% | -0.5% | -0.5% | -0.5% | 0% |
| **USO** | 3m | 1 | -0.5% | -0.5% | -0.5% | -0.5% | 0% |
| **USO** | 6m | 1 | -0.5% | -0.5% | -0.5% | -0.5% | 0% |
| **GLD** | 1m | 1 | -3.8% | -3.8% | -3.8% | -3.8% | 0% |
| **GLD** | 3m | 1 | -3.8% | -3.8% | -3.8% | -3.8% | 0% |
| **GLD** | 6m | 1 | -3.8% | -3.8% | -3.8% | -3.8% | 0% |
| **TLT** | 1m | 1 | -1.8% | -1.8% | -1.8% | -1.8% | 0% |
| **TLT** | 3m | 1 | -1.8% | -1.8% | -1.8% | -1.8% | 0% |
| **TLT** | 6m | 1 | -1.8% | -1.8% | -1.8% | -1.8% | 0% |

**Episodes (последни 5 от 1):**
- `2026-09-25 → 2026-09-25` (1d)

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 10 · **Total matching days:** 101 · **History:** 2021-05-17 → 2026-10-08

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 10 | -0.1% | +0.6% | -7.2% | +7.8% | 60% |
| **SPY** | 3m | 10 | +2.1% | +2.6% | -8.3% | +11.6% | 60% |
| **SPY** | 6m | 10 | +1.3% | +3.8% | -20.8% | +14.2% | 70% |
| **USO** | 1m | 10 | +4.1% | +0.5% | -15.0% | +52.9% | 50% |
| **USO** | 3m | 10 | +9.2% | +7.9% | -20.7% | +52.2% | 60% |
| **USO** | 6m | 10 | +11.3% | +4.6% | -27.6% | +56.3% | 60% |
| **GLD** | 1m | 10 | -1.2% | -1.9% | -8.3% | +11.7% | 20% |
| **GLD** | 3m | 10 | -1.6% | -1.5% | -12.0% | +6.4% | 40% |
| **GLD** | 6m | 10 | -0.8% | -2.7% | -15.2% | +25.0% | 30% |
| **TLT** | 1m | 10 | -2.4% | -2.7% | -6.0% | +2.5% | 10% |
| **TLT** | 3m | 10 | -6.7% | -6.1% | -17.6% | +4.2% | 20% |
| **TLT** | 6m | 10 | -10.2% | -8.1% | -22.3% | +1.2% | 10% |

**Episodes (последни 5 от 10):**
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-05-19` (36d)
- `2026-07-22 → 2026-08-03` (8d)
- `2026-09-01 → 2026-09-28` (15d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 17 · **Total matching days:** 294 · **History:** 2021-05-17 → 2026-10-08

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 17 | +1.9% | +1.6% | -4.8% | +9.0% | 71% |
| **SPY** | 3m | 17 | +3.1% | +4.2% | -12.6% | +16.2% | 76% |
| **SPY** | 6m | 17 | +6.6% | +8.9% | -14.0% | +21.0% | 82% |
| **USO** | 1m | 17 | +2.4% | -2.2% | -13.0% | +22.9% | 41% |
| **USO** | 3m | 17 | +3.4% | -0.8% | -14.5% | +29.9% | 41% |
| **USO** | 6m | 17 | +13.5% | +2.6% | -12.4% | +87.1% | 71% |
| **GLD** | 1m | 17 | +2.4% | +2.1% | -5.6% | +9.0% | 76% |
| **GLD** | 3m | 17 | +5.6% | +7.2% | -16.8% | +23.6% | 65% |
| **GLD** | 6m | 17 | +10.1% | +9.8% | -14.4% | +43.8% | 71% |
| **TLT** | 1m | 17 | +0.3% | -0.0% | -6.3% | +8.2% | 47% |
| **TLT** | 3m | 17 | -1.8% | -1.7% | -15.3% | +11.9% | 35% |
| **TLT** | 6m | 17 | -5.0% | -5.9% | -21.3% | +7.0% | 35% |

**Episodes (последни 5 от 17):**
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)
- `2026-08-07 → 2026-09-03` (19d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 20 · **Total matching days:** 299 · **History:** 2021-05-17 → 2026-10-08

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 20 | +0.3% | +0.5% | -8.7% | +7.0% | 55% |
| **SPY** | 3m | 20 | +2.0% | +3.2% | -13.7% | +9.1% | 70% |
| **SPY** | 6m | 20 | +3.2% | +5.8% | -16.4% | +16.9% | 75% |
| **USO** | 1m | 20 | -0.6% | -3.7% | -21.8% | +55.8% | 40% |
| **USO** | 3m | 20 | +3.7% | -0.5% | -12.7% | +64.3% | 45% |
| **USO** | 6m | 20 | +8.6% | +2.3% | -16.0% | +75.1% | 50% |
| **GLD** | 1m | 20 | -0.8% | -0.2% | -12.4% | +7.6% | 45% |
| **GLD** | 3m | 20 | +1.5% | +1.5% | -13.7% | +19.0% | 65% |
| **GLD** | 6m | 20 | +7.1% | +4.3% | -15.8% | +55.5% | 65% |
| **TLT** | 1m | 20 | -0.4% | -0.1% | -5.6% | +5.2% | 45% |
| **TLT** | 3m | 20 | -3.7% | -4.6% | -17.3% | +8.7% | 30% |
| **TLT** | 6m | 20 | -7.0% | -7.7% | -21.4% | +4.6% | 20% |

**Episodes (последни 5 от 20):**
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (13d)
- `2026-09-21 → 2026-10-08` (11d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-10-08

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (8 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **COMPUTSA** | Завършени жилища (SAAR) | growth | housing_supply | 5 | 2.77 | 2.95 | 2026-09-12 00:00:00 | 2026-10-07 00:00:00 | ✓ |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 5 | 2.75 | 2.75 | 2026-09-12 00:00:00 | 2026-10-07 00:00:00 | ✓ |
| **JTSQUR** | Quits rate — напускания | labor | flow | 5 | 2.02 | 2.02 | 2026-09-12 00:00:00 | 2026-10-07 00:00:00 | ✓ |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | 3 | 2.25 | 2.25 | 2026-09-12 00:00:00 | 2026-09-26 00:00:00 | - |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 3 | 2.13 | 2.25 | 2026-09-12 00:00:00 | 2026-10-07 00:00:00 | - |
| **US_PMI_COMPOSITE** | S&P Global US Composite PMI | growth | diffusion_indices | 1 | 2.60 | 2.60 | 2026-10-07 00:00:00 | 2026-10-07 00:00:00 | ✓ |
| **US_PMI_SVCS** | S&P Global US Services PMI | growth | diffusion_indices | 1 | 2.09 | 2.09 | 2026-10-07 00:00:00 | 2026-10-07 00:00:00 | ✓ |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 1 | 2.07 | 2.07 | 2026-10-07 00:00:00 | 2026-10-07 00:00:00 | ✓ |

### EU (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.34 | 5.60 | 2026-09-05 00:00:00 | 2026-10-03 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.18 | 2.18 | 2026-09-05 00:00:00 | 2026-10-03 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.15 | 2.17 | 2026-09-05 00:00:00 | 2026-10-03 00:00:00 | ✓ |

### CN (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 9 | 2.54 | 2.55 | 2026-09-07 00:00:00 | 2026-10-05 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 9 | 2.22 | 2.23 | 2026-09-07 00:00:00 | 2026-10-05 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 4 | 2.19 | 2.19 | 2026-09-07 00:00:00 | 2026-09-19 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-10-07 00:00:00 · **Generated:** 2026-10-07 19:23:40.563723+00:00

**Режим:** `policy_dilemma` (Policy dilemma)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 39.8 | mixed | 33.3% | 2 | 2 |
| **growth** | 49.1 | mixed | 56.0% | 4 | 4 |
| **inflation** | 41.4 | mixed | 38.9% | 1 | 1 |
| **liquidity** | 45.4 | mixed | 36.8% | 0 | 0 |

### Top anomalies (7 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **COMPUTSA** | Завършени жилища (SAAR) | growth, housing | housing_supply | -2.95 | down | -27.13 | 2026-08-01 | ✓ min |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.75 | down | 93.45 | 2026-04-01 | ✓ min |
| **US_PMI_COMPOSITE** | S&P Global US Composite PMI | growth | diffusion_indices | +2.60 | up | 58.40 | 2026-09-01 | ✓ max |
| **US_PMI_SVCS** | S&P Global US Services PMI | growth | diffusion_indices | +2.09 | up | 58.80 | 2026-09-01 | ✓ max |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | +2.07 | up | 55.90 | 2026-09-01 | ✓ max |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | -2.06 | down | 2.57 | 2026-07-01 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | -2.02 | down | 1.90 | 2026-08-01 | ✓ min |

### Narrative hints от макро лещите
- **COMPUTSA**: Завършва construction pipeline (12-18m след starts). Превишение спрямо sales = inventory build.
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **US_PMI_COMPOSITE**: Markit композит — global benchmark, complement към ISM. Flash + final estimates.
- **US_PMI_SVCS**: Markit services — global comparable. ISM Services има различна methodology.
- **US_PMI_MFG**: Markit mfg — comparable cross-country. ISM е US-only.
- **HPIPONM226S**: Monthly FHFA версия. Само purchase transactions (без refi appraisals). По-чист от refi-bias.
- **JTSQUR**: Работническа увереност. Ако quits rate пада — хората задържат работата си (pre-recession pattern).

### Cross-lens divergences (6 entries)
- 🔔 **?**
  - `pair_id`: stagflation_test
  - `name_bg`: Labor tightness × Inflation pressure
  - `question_bg`: Дали labor tightness потвърждава inflation pressure (стагфлация)?
  - `state`: a_down_b_up
  - `interpretation`: Policy dilemma — labor loose, но inflation still hot.
  - `slot_a_label`: Labor tightness
  - `slot_b_label`: Inflation pressure
  - `breadth_a`: 0.2
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.7
  - `breadth_b_raw`: 1.0
- 🔔 **?**
  - `pair_id`: growth_labor_lead_lag
  - `name_bg`: Hard activity × Labor claims
  - `question_bg`: Дали hard activity и labor market следват едно тенденция?
  - `state`: transition
  - `interpretation`: Mixed — waiting for clarification.
  - `slot_a_label`: Hard activity
  - `slot_b_label`: Labor market (claims inverted)
  - `breadth_a`: 0.6
  - `breadth_b`: 1.0
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.8
  - `breadth_b_raw`: 1.0
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Realized CPI × Expectations
  - `question_bg`: Дали expectations следват realized inflation, или стоят anchored?
  - `state`: a_up_b_down
  - `interpretation`: Anchored — realized hot, expectations stable. Credibility holds.
  - `slot_a_label`: Realized inflation
  - `slot_b_label`: Inflation expectations
  - `breadth_a`: 0.667
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
  - `breadth_a`: 0.0
  - `breadth_b`: 0.6
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.0
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
> Policy dilemma — labor market е loose, но инфлацията remains hot. Fed е заклещен между двата мандата. Най-отклонена леща: Инфлация и цени — breadth 64% (разширяване), 1 аномалии, 1 нови екстремума. Обаче inflation expectations остават anchored — Fed narrative-ът за момента държи. За наблюдение следващия релиз: COMPUTSA, LABOR_SHARE_NBS, US_PMI_COMPOSITE (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: COMPUTSA z=-2.95 · NEW-5Y-MIN
- 6 нови екстремуми в top-7 (lookback 5г.)
- Активни двойки: Stagflation test=a_down_b_up; Inflation anchoring=a_up_b_down; Credit × Policy=a_down_b_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-10-03 00:00:00 · **Generated:** 2026-10-03 08:36:03.359444+00:00

**Режим:** `policy_dilemma` (Policy dilemma (индикирана))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 41.1 | mixed | 42.9% | 0 | 0 |
| **growth** | 44.2 | mixed | 25.0% | 0 | 0 |
| **inflation** | 44.3 | mixed | 42.9% | 0 | 0 |
| **credit** | 44.5 | mixed | 36.8% | 3 | 2 |
| **external** | 37.2 | contracting | 16.7% | 0 | 0 |

### Top anomalies (3 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | +5.60 | up | 3.30 | 2026-09-01 | - |
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
  - `breadth_a`: 1.0
  - `breadth_b`: 0.5
  - `state_raw`: transition
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.5
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
  - `breadth_a`: 1.0
  - `breadth_b`: None
  - `state_raw`: insufficient_data
  - `breadth_a_raw`: 1.0
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
  - `breadth_a`: 0.444
  - `breadth_b`: 0.5
  - `state_raw`: transition
  - `breadth_a_raw`: 0.444
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
> Policy dilemma — labor market е loose, но инфлацията remains hot. ЕЦБ е заклещена между инфлацията и растежа. Най-отклонена леща: Инфлация и цени — breadth 100% (разширяване), 0 аномалии, 0 нови екстремума. За наблюдение следващия релиз: FR_10Y, DE_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.60
- 2 нови екстремуми в top-3 (lookback 5г.)
- Активни двойки: Stagflation test=a_down_b_up; fragmentation_risk=a_up_b_down



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-10-05 00:00:00 · **Generated:** 2026-10-05 12:50:48.854932+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 32.9 | contracting | -% | - | - |
| **inflation** | 45.6 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 46.9 | mixed | -% | - | - |
| **property** | 29.5 | contracting | -% | - | - |

### Top anomalies (2 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | -2.54 | down | 3.00 | 2026-09-20 | ✓ min |
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
> Претеглен композитен macro score 36.2/100 → режим „ВЛОШАВАЩ СЕ“ (5/5 лещи). 5 лещи, 2 flagged аномалии (4 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-10-02 |
| `as_of` | 2026-10-02 |
| `regime` | GROWTH |
| `alignment_score` | 4.0 |
| `gms_score` | 1.0 |
| `gms_max` | 8 |
| `gms_tier` | LOW |
| `ks_status` | inactive |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-10-02 → 2026-10-08)

**stable_winner (1m):** +12 entered, -8 exited
  - **Entered:** C, DAL, EVRG, FITB, GEV, GL, GM, HST, KEY, MAR, RF, WDC _(включително 2 за първи път в историята: DAL, GL)_
  - **Exited:** ALB, APA, EXPE, F, FDX, NEM, NTRS, VTR

**stable_winner (3m):** +4 entered, -2 exited
  - **Entered:** DAL, FITB, PWR, WDC _(включително 1 за първи път в историята: DAL)_
  - **Exited:** HWM, MAR

**quality_dip (1m):** +8 entered, -11 exited
  - **Entered:** ALB, APA, EXPE, F, FDX, NEM, NTRS, VTR
  - **Exited:** C, EVRG, FITB, GEV, GL, GM, HST, KEY, MAR, RF, WDC

**quality_dip (3m):** +2 entered, -3 exited
  - **Entered:** HWM, MAR
  - **Exited:** FITB, PWR, WDC

**faded_bounce (1m):** +4 entered, -11 exited
  - **Entered:** AOS, BX, EFX, KMB _(включително 1 за първи път в историята: AOS)_
  - **Exited:** AJG, AVY, BKNG, CEG, DASH, ERIE, LULU, MKC, NFLX, STZ, UBER

**faded_bounce (3m):** +5 entered, -10 exited
  - **Entered:** CPRT, HRL, IP, MOS, OTIS
  - **Exited:** BR, BRO, COO, ERIE, MKC, MRSH, NVR, PGR, STZ, VRSK



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-09-29 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **soymeal** | Commodities | 207416 | 100.0 | 100.0 | 1060 | 48675 |
| **soybeans** | Commodities | 241164 | 99.0 | 99.0 | 1060 | -19 |
| **corn** | Commodities | 377850 | 97.1 | 97.1 | 1060 | -53212 |
| **rbob** | Commodities | 94018 | 95.8 | 95.8 | 1060 | 4755 |
| **copper** | Commodities | 78709 | 95.1 | 95.1 | 1060 | 5709 |
| **sugar** | Commodities | 227821 | 94.4 | 94.4 | 1060 | -15646 |
| **soyoil** | Commodities | 87875 | 91.0 | 91.0 | 1060 | -22037 |
| **cotton** | Commodities | 74593 | 89.2 | 89.2 | 1060 | -33383 |
| **aud** | FX | 60592 | 89.2 | 89.2 | 1060 | 10930 |
| **vix** | Volatility | -7467 | 77.2 | 77.2 | 1019 | 18791 |
| **jpy** | FX | -14161 | 58.7 | 58.7 | 1060 | 88027 |
| **dxy** | FX | 361 | 56.5 | 56.5 | 1060 | -6772 |
| **gold** | Commodities | 124418 | 52.8 | 52.8 | 1060 | -16393 |
| **coffee** | Commodities | 11512 | 48.7 | 48.7 | 1060 | -10838 |
| **heatingoil** | Commodities | 12690 | 47.0 | 47.0 | 1060 | -8295 |
| **wheat** | Commodities | -21670 | 46.8 | 46.8 | 1060 | -36324 |
| **cattle** | Commodities | 51304 | 43.8 | 43.8 | 1060 | 3390 |
| **gbpfx** | FX | 4606 | 41.4 | 41.4 | 1060 | -38561 |
| **platinum** | Commodities | 8067 | 39.9 | 39.9 | 1060 | -580 |
| **brent** | Commodities | 3571 | 37.9 | 37.9 | 243 | -1369 |
| **bitcoin** | Crypto | -6856 | 34.5 | 34.5 | 443 | 764 |
| **eurfx** | FX | -39265 | 34.4 | 34.4 | 1060 | -1092 |
| **nasdaq** | US Equities | -24723 | 31.2 | 31.2 | 1060 | -10631 |
| **wti** | Commodities | 122916 | 29.0 | 29.0 | 1060 | 3297 |
| **sp500** | US Equities | -372489 | 28.1 | 28.1 | 1060 | -54925 |
| **us30y** | Rates | -251395 | 22.4 | 22.4 | 1060 | 51650 |
| **silver** | Commodities | 7738 | 21.6 | 21.6 | 1060 | -4432 |
| **us2y** | Rates | -1165980 | 19.5 | 19.5 | 1060 | 102054 |
| **chf** | FX | -13995 | 14.6 | 14.6 | 1060 | -3697 |
| **us5y** | Rates | -1985787 | 12.6 | 12.6 | 1060 | 216901 |
| **natgas** | Commodities | -132849 | 11.0 | 11.0 | 1060 | -43326 |
| **usultra10y** | Rates | -328471 | 10.2 | 10.2 | 550 | 94886 |
| **cocoa** | Commodities | -19318 | 8.1 | 8.1 | 1060 | -10393 |
| **palladium** | Commodities | -8037 | 7.5 | 7.5 | 1060 | -3458 |
| **cad** | FX | -69644 | 6.4 | 6.4 | 1060 | -894 |
| **us10y** | Rates | -2036432 | 4.3 | 4.3 | 1060 | 26070 |
| **russell** | US Equities | -114554 | 3.5 | 3.5 | 596 | -5055 |
| **hogs** | Commodities | -44186 | 0.1 | 0.1 | 1060 | -15863 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MRNA** | Healthcare | 97.3 | 40.0% | 156.6% | 277.1% | 409.6% | 1.51 | -34.2% |
| 2 | **VLO** | Energy | 97.0 | 10.8% | 51.4% | 78.5% | 139.2% | 2.53 | -12.1% |
| 3 | **MPC** | Energy | 96.6 | 11.2% | 56.5% | 91.9% | 109.0% | 2.26 | -18.3% |
| 4 | **HPE** | Technology | 96.4 | 29.0% | 47.2% | 190.2% | 129.5% | 1.83 | -26.4% |
| 5 | **DELL** | Technology | 95.5 | 8.4% | 28.8% | 213.6% | 270.9% | 1.87 | -32.3% |
| 6 | **PSX** | Energy | 94.8 | 4.8% | 43.9% | 63.7% | 100.7% | 2.24 | -17.3% |
| 7 | **ILMN** | Healthcare | 94.7 | 26.9% | 38.2% | 109.2% | 108.9% | 1.92 | -25.7% |
| 8 | **AMD** | Technology | 92.6 | 27.7% | 18.1% | 178.6% | 148.3% | 1.62 | -27.8% |
| 9 | **CRWD** | Technology | 92.3 | 26.4% | 33.8% | 148.9% | 69.4% | 1.32 | -37.2% |
| 10 | **MRVL** | Technology | 92.0 | 26.3% | 17.1% | 148.9% | 154.0% | 1.45 | -48.4% |
| 11 | **MU** | Technology | 90.9 | 8.8% | 9.7% | 167.5% | 424.3% | 2.12 | -39.1% |
| 12 | **NTAP** | Technology | 90.7 | 24.7% | 37.7% | 137.8% | 59.1% | 1.46 | -24.8% |
| 13 | **LITE** | Technology | 90.0 | 13.5% | 41.4% | 24.0% | 509.3% | 1.95 | -42.8% |
| 14 | **FTNT** | Technology | 89.6 | 20.2% | 15.6% | 126.7% | 82.3% | 1.78 | -14.3% |
| 15 | **BE** | Industrials | 89.5 | 5.1% | 13.3% | 98.5% | 218.8% | 1.04 | -52.6% |
| 16 | **PANW** | Technology | 88.3 | 20.4% | 19.9% | 133.4% | 58.5% | 1.27 | -36.0% |
| 17 | **CRL** | Healthcare | 88.2 | 7.0% | 28.6% | 71.5% | 60.5% | 1.10 | -33.9% |
| 18 | **INTC** | Technology | 86.1 | 8.3% | 0.5% | 91.9% | 185.5% | 1.43 | -41.9% |
| 19 | **RVTY** | Healthcare | 85.5 | 20.9% | 36.1% | 70.0% | 36.4% | 1.17 | -30.1% |
| 20 | **NUE** | Basic Materials | 84.6 | -3.7% | 11.1% | 35.9% | 90.9% | 1.75 | -18.4% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MOH.AT** | Energy | 96.9 | 12.8% | 81.8% | 78.6% | 145.0% | 3.14 | -12.1% |
| 2 | **XTB.WA** | Financial Services | 94.1 | -11.7% | 38.2% | 69.3% | 142.1% | 2.03 | -22.2% |
| 3 | **CCC.L** | Technology | 92.1 | 4.6% | 25.5% | 76.0% | 109.8% | 2.21 | -16.2% |
| 4 | **AKER.OL** | Industrials | 91.7 | 6.2% | 34.5% | 44.1% | 114.9% | 2.51 | -15.6% |
| 5 | **FRO.OL** | Energy | 90.4 | 27.3% | 31.7% | 64.1% | 74.3% | 1.84 | -20.5% |
| 6 | **TKA.DE** | Basic Materials | 90.2 | 9.7% | 37.1% | 87.3% | 70.0% | 1.08 | -41.4% |
| 7 | **RBI.VI** | Financial Services | 89.4 | -0.3% | 15.1% | 71.4% | 120.0% | 2.02 | -18.0% |
| 8 | **MAERSK-B.CO** | Industrials | 88.2 | 12.6% | 47.7% | 46.8% | 57.9% | 1.39 | -22.9% |
| 9 | **REP.MC** | Energy | 87.5 | 8.6% | 41.6% | 23.2% | 95.0% | 2.21 | -20.4% |
| 10 | **ABN.AS** | Financial Services | 86.7 | 4.8% | 16.7% | 62.7% | 67.1% | 1.99 | -18.0% |
| 11 | **PKN.WA** | Energy | 86.5 | 4.2% | 22.6% | 29.9% | 100.4% | 2.16 | -12.3% |
| 12 | **EDEN.PA** | Financial Services | 86.5 | -0.1% | 38.1% | 65.4% | 49.5% | 0.81 | -42.4% |
| 13 | **EZJ.L** | Industrials | 86.2 | -0.5% | 32.5% | 84.1% | 46.8% | 0.89 | -34.9% |
| 14 | **PKO.WA** | Financial Services | 86.1 | 8.3% | 19.4% | 46.8% | 65.1% | 2.18 | -18.2% |
| 15 | **BGEO.L** | Financial Services | 85.8 | 0.5% | 19.7% | 38.6% | 78.7% | 1.82 | -21.0% |
| 16 | **UNI.MC** | Financial Services | 85.5 | 0.0% | 15.9% | 51.7% | 66.2% | 1.97 | -17.8% |
| 17 | **ROR.L** | Industrials | 85.4 | -0.0% | 55.2% | 57.6% | 42.8% | 0.59 | -25.2% |
| 18 | **UNI.MI** | Financial Services | 84.9 | -3.2% | 14.4% | 48.2% | 70.3% | 1.78 | -11.5% |
| 19 | **BCP.LS** | Financial Services | 84.8 | 7.8% | 15.2% | 53.9% | 59.5% | 2.04 | -17.0% |
| 20 | **MT.AS** | Basic Materials | 84.7 | -0.8% | 9.4% | 40.3% | 121.7% | 1.83 | -26.2% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **EIX** | Utilities | 2.247 | 1.438 | 1.058 | 3.251 | -0.936 | - | 5.6 | +19.7% |
| 2 | **CF** | Materials | 1.574 | 1.061 | 1.262 | 1.656 | 0.381 | - | 8.4 | +29.9% |
| 3 | **SNDK** | Information Technology | 1.546 | 1.960 | 1.550 | 0.462 | -0.161 | - | 21.8 | +91.6% |
| 4 | **NEM** | Materials | 1.407 | 0.973 | 1.659 | 0.869 | 0.602 | - | 14.6 | +25.9% |
| 5 | **MU** | Information Technology | 1.350 | 1.593 | 1.231 | 0.647 | -0.534 | - | 13.9 | +88.3% |
| 6 | **MO** | Consumer Staples | 1.325 | 0.071 | 2.143 | 0.931 | -0.439 | - | 15.0 | - |
| 7 | **SYF** | Financials | 1.266 | 0.208 | 1.172 | 1.735 | -0.351 | - | 7.5 | +20.8% |
| 8 | **HST** | Real Estate | 1.237 | 1.655 | 0.472 | 1.146 | -0.315 | - | 15.2 | +15.6% |
| 9 | **BMY** | Health Care | 1.175 | 1.052 | 0.875 | 1.081 | 0.587 | - | 13.1 | +46.6% |
| 10 | **APA** | Energy | 1.155 | 0.906 | 1.265 | 0.729 | -0.112 | - | 9.6 | +26.7% |
| 11 | **SPG** | Real Estate | 1.132 | 0.831 | 1.381 | 0.609 | -1.225 | - | 14.1 | +120.5% |
| 12 | **MAS** | Industrials | 1.095 | -0.101 | 1.453 | 1.267 | -0.821 | - | 16.0 | +5862.5% |
| 13 | **CTVA** | Materials | 1.076 | 0.640 | 0.445 | 1.676 | 0.396 | - | 8.5 | - |
| 14 | **DVA** | Health Care | 1.025 | 0.852 | 0.192 | 1.637 | -1.414 | - | 15.0 | +88.5% |
| 15 | **WDC** | Information Technology | 0.945 | 1.443 | 0.801 | 0.230 | -0.708 | - | 14.6 | +130.8% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -1.972 | -1.621 | -0.923 | -2.510 | -0.969 |
| 502 | **TSLA** | Consumer Discretionary | -1.808 | -0.646 | -1.372 | -2.470 | -0.381 |
| 501 | **COIN** | Financials | -1.765 | -2.921 | -1.666 | 0.000 | -1.665 |
| 500 | **CSGP** | Real Estate | -1.713 | -3.401 | -0.472 | -0.764 | 0.664 |
| 499 | **XYZ** | Financials | -1.564 | -0.264 | -1.853 | -1.658 | -0.999 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W41.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W41.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\macro\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-10-05  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
