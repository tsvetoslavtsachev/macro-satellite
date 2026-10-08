# Сателит — пълен data export за 2026-W40

_Период: 2026-09-28 → 2026-10-04_  
_Генериран: 2026-10-02 12:01 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W40.md` (structured briefing) и `narrative_2026-W40.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**20 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **HYG** | -1.23% | -2.81σ | 77.86 | 76.90 | 2026-09-25 | 2026-10-01 | -0.19% | +0.37% | 13 |
| **EFA** | -2.60% | -2.19σ | 105.56 | 102.82 | 2026-09-25 | 2026-10-01 | +0.23% | +1.29% | 13 |
| **XLP** | -2.11% | -2.05σ | 82.06 | 80.33 | 2026-09-25 | 2026-10-01 | -0.24% | +0.91% | 13 |
| **VEA** | -2.27% | -1.81σ | 71.84 | 70.21 | 2026-09-25 | 2026-10-01 | +0.15% | +1.33% | 13 |
| **XLF** | -2.52% | -1.71σ | 54.84 | 53.46 | 2026-09-25 | 2026-10-01 | +0.19% | +1.58% | 13 |
| **XLC** | -2.67% | -1.59σ | 112.96 | 109.94 | 2026-09-25 | 2026-10-01 | +0.50% | +1.99% | 13 |
| **XLV** | -2.64% | -1.59σ | 170.70 | 166.20 | 2026-09-25 | 2026-10-01 | +0.50% | +1.97% | 13 |
| **UUP** | +1.19% | +1.57σ | 28.62 | 28.96 | 2026-09-25 | 2026-10-01 | +0.05% | +0.73% | 13 |
| **SLV** | -5.37% | -1.40σ | 58.14 | 55.02 | 2026-09-25 | 2026-10-01 | +0.77% | +4.40% | 13 |
| **VWO** | -1.88% | -1.36σ | 60.16 | 59.03 | 2026-09-25 | 2026-10-01 | +0.22% | +1.54% | 13 |
| **DIA** | -1.71% | -1.32σ | 517.49 | 508.62 | 2026-09-25 | 2026-10-01 | +0.00% | +1.30% | 13 |
| **TLT** | -2.03% | -1.25σ | 79.32 | 77.71 | 2026-09-25 | 2026-10-01 | -0.73% | +1.04% | 13 |
| **XLRE** | -2.12% | -1.16σ | 41.56 | 40.68 | 2026-09-25 | 2026-10-01 | -0.64% | +1.27% | 13 |
| **XLB** | -2.53% | -1.15σ | 49.80 | 48.54 | 2026-09-25 | 2026-10-01 | -0.25% | +1.98% | 13 |
| **GDX** | -6.60% | -1.11σ | 92.87 | 86.74 | 2026-09-25 | 2026-10-01 | +1.71% | +7.47% | 13 |
| **LQD** | -1.14% | -1.10σ | 103.21 | 102.03 | 2026-09-25 | 2026-10-01 | -0.45% | +0.63% | 13 |
| **GLD** | -2.71% | -1.09σ | 393.41 | 382.76 | 2026-09-25 | 2026-10-01 | +0.44% | +2.88% | 13 |
| **VNQ** | -2.00% | -1.08σ | 90.99 | 89.17 | 2026-09-25 | 2026-10-01 | -0.61% | +1.28% | 13 |
| **DBA** | -1.44% | -1.04σ | 28.54 | 28.13 | 2026-09-25 | 2026-10-01 | +0.50% | +1.86% | 13 |
| **SPY** | -0.95% | -1.01σ | 771.35 | 763.99 | 2026-09-25 | 2026-10-01 | +0.44% | +1.38% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-10-04 · **Conditions matched:** 4/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | +1.14% | ❌ | 148.33 | 150.02 | 2026-09-25 | 2026-10-01 |
| DFEN | down ≥ 3.0% | -8.56% | ✅ | 51.99 | 47.54 | 2026-09-25 | 2026-10-01 |
| GLD | down ≥ 1.0% | -2.71% | ✅ | 393.41 | 382.76 | 2026-09-25 | 2026-10-01 |
| URA | down ≥ 3.0% | -3.23% | ✅ | 40.91 | 39.59 | 2026-09-25 | 2026-10-01 |
| UUP | up ≥ 0.5% | +1.19% | ✅ | 28.62 | 28.96 | 2026-09-25 | 2026-10-01 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-10-04 · **Conditions matched:** 1/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | -1.05% | ❌ | 281.97 | 279.02 | 2026-09-25 | 2026-10-01 |
| XLF | up ≥ 1.0% | -2.52% | ❌ | 54.84 | 53.46 | 2026-09-25 | 2026-10-01 |
| XLY | up ≥ 1.0% | -1.58% | ❌ | 110.56 | 108.81 | 2026-09-25 | 2026-10-01 |
| GLD | down ≥ 0.5% | -2.71% | ✅ | 393.41 | 382.76 | 2026-09-25 | 2026-10-01 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2023-W39 (week ending 2023-10-01)
**Cosine similarity:** 0.8601 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -2.17% | +11.19% | +22.36% |
| **USO** | -7.22% | -17.57% | -2.63% |
| **GLD** | +7.37% | +11.50% | +19.99% |
| **TLT** | -5.76% | +11.49% | +6.69% |
| **XLE** | -5.75% | -7.25% | +4.45% |
| **IWM** | -6.91% | +13.56% | +18.99% |

### Паралел #2: 2022-W33 (week ending 2022-08-21)
**Cosine similarity:** 0.7583 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -9.01% | -6.19% | -3.52% |
| **USO** | -6.54% | -6.79% | -9.51% |
| **GLD** | -4.70% | +0.04% | +5.25% |
| **TLT** | -6.01% | -11.85% | -9.43% |
| **XLE** | -2.97% | +15.32% | +6.33% |
| **IWM** | -8.52% | -5.62% | -0.78% |

### Паралел #3: 2026-W01 (week ending 2026-01-04)
**Cosine similarity:** 0.7189 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.93% | -4.00% | +9.02% |
| **USO** | +12.34% | +100.00% | +50.78% |
| **GLD** | +14.06% | +7.82% | -5.06% |
| **TLT** | -0.31% | -0.28% | -1.75% |
| **XLE** | +13.19% | +29.79% | +16.58% |
| **IWM** | +5.63% | +1.01% | +19.62% |

### Паралел #4: 2025-W44 (week ending 2025-11-02)
**Cosine similarity:** 0.7189 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -0.08% | +1.45% | +5.66% |
| **USO** | -3.25% | +9.59% | +96.80% |
| **GLD** | +5.19% | +20.87% | +14.96% |
| **TLT** | -1.64% | -3.50% | -5.18% |
| **XLE** | +2.28% | +15.85% | +33.55% |
| **IWM** | -0.43% | +5.45% | +13.42% |

### Паралел #5: 2022-W17 (week ending 2022-05-01)
**Cosine similarity:** 0.6872 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.23% | -0.00% | -5.58% |
| **USO** | +10.77% | +1.15% | -5.62% |
| **GLD** | -3.26% | -7.24% | -13.42% |
| **TLT** | -2.42% | -1.69% | -18.96% |
| **XLE** | +16.03% | +4.35% | +18.76% |
| **IWM** | +0.19% | +1.24% | -0.97% |

### Паралел #6: 2026-W11 (week ending 2026-03-15)
**Cosine similarity:** 0.6557 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.86% | +12.00% | +15.40% |
| **USO** | +3.30% | +4.62% | +29.20% |
| **GLD** | -3.42% | -16.12% | -13.47% |
| **TLT** | +0.77% | -0.89% | -6.55% |
| **XLE** | -3.03% | -0.26% | +12.89% |
| **IWM** | +8.97% | +18.80% | +17.15% |

### Паралел #7: 2023-W03 (week ending 2023-01-22)
**Cosine similarity:** 0.6514 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.81% | +4.12% | +14.22% |
| **USO** | -6.79% | -4.67% | -3.58% |
| **GLD** | -4.84% | +2.77% | +1.61% |
| **TLT** | -5.47% | -1.69% | -4.21% |
| **XLE** | -7.08% | -6.08% | -6.83% |
| **IWM** | +1.29% | -4.04% | +5.09% |

### Паралел #8: 2022-W22 (week ending 2022-06-05)
**Cosine similarity:** 0.6430 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -6.96% | -4.46% | -0.88% |
| **USO** | -16.42% | -20.16% | -21.94% |
| **GLD** | -4.54% | -7.72% | -3.08% |
| **TLT** | +0.60% | -5.01% | -7.70% |
| **XLE** | -22.13% | -10.67% | +0.89% |
| **IWM** | -7.61% | -3.73% | +0.53% |

### Паралел #9: 2023-W08 (week ending 2023-02-26)
**Cosine similarity:** 0.6305 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -0.20% | +5.96% | +11.00% |
| **USO** | -3.80% | -3.43% | +7.97% |
| **GLD** | +8.96% | +7.47% | +5.51% |
| **TLT** | +3.53% | +0.12% | -5.69% |
| **XLE** | -4.58% | -6.96% | +3.46% |
| **IWM** | -7.50% | -6.06% | -1.87% |

### Паралел #10: 2026-W12 (week ending 2026-03-22)
**Cosine similarity:** 0.6240 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +8.56% | +15.14% | +17.44% |
| **USO** | +5.62% | -5.40% | +26.67% |
| **GLD** | +3.92% | -6.35% | -2.95% |
| **TLT** | +0.86% | +1.07% | -5.34% |
| **XLE** | -5.80% | -9.34% | +8.43% |
| **IWM** | +13.33% | +22.03% | +17.29% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 15 · **Total matching days:** 88 · **History:** 2021-05-17 → 2026-10-01

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 15 | +2.1% | +1.7% | -3.1% | +7.4% | 73% |
| **SPY** | 3m | 15 | +2.7% | +2.5% | -7.3% | +12.0% | 80% |
| **SPY** | 6m | 15 | +7.1% | +8.6% | -6.8% | +21.8% | 80% |
| **USO** | 1m | 15 | +0.1% | -0.8% | -14.3% | +12.7% | 47% |
| **USO** | 3m | 15 | -0.9% | -4.1% | -18.9% | +24.5% | 47% |
| **USO** | 6m | 15 | +13.6% | +0.0% | -8.7% | +109.4% | 53% |
| **GLD** | 1m | 15 | +2.6% | +0.9% | -3.4% | +9.0% | 73% |
| **GLD** | 3m | 15 | +4.9% | +3.9% | -12.6% | +24.5% | 67% |
| **GLD** | 6m | 15 | +5.6% | +4.5% | -12.5% | +25.3% | 67% |
| **TLT** | 1m | 15 | -1.6% | -1.1% | -6.7% | +3.6% | 33% |
| **TLT** | 3m | 15 | -1.2% | -0.5% | -16.5% | +11.1% | 47% |
| **TLT** | 6m | 15 | -5.0% | -6.0% | -18.0% | +7.5% | 27% |

**Episodes (последни 5 от 15):**
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-08-03` (5d)
- `2026-09-10 → 2026-10-01` (14d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 98 · **History:** 2021-05-17 → 2026-10-01

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +6.3% | +6.3% | +3.5% | +9.1% | 100% |
| **SPY** | 3m | 2 | +5.9% | +5.9% | +1.6% | +10.3% | 100% |
| **SPY** | 6m | 2 | +7.3% | +7.3% | +1.6% | +13.0% | 100% |
| **USO** | 1m | 2 | +5.6% | +5.6% | +4.0% | +7.2% | 100% |
| **USO** | 3m | 2 | +7.5% | +7.5% | -9.9% | +24.8% | 50% |
| **USO** | 6m | 2 | +22.6% | +22.6% | +20.4% | +24.8% | 100% |
| **GLD** | 1m | 2 | +3.5% | +3.5% | -0.2% | +7.2% | 50% |
| **GLD** | 3m | 2 | -5.5% | -5.5% | -13.8% | +2.9% | 50% |
| **GLD** | 6m | 2 | -4.5% | -4.5% | -11.9% | +2.9% | 50% |
| **TLT** | 1m | 2 | -1.4% | -1.4% | -1.8% | -1.0% | 0% |
| **TLT** | 3m | 2 | -5.3% | -5.3% | -7.6% | -2.9% | 0% |
| **TLT** | 6m | 2 | -9.1% | -9.1% | -10.6% | -7.6% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-10-01` (51d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 454 · **History:** 2021-05-17 → 2026-10-01

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
- `2025-11-03 → 2026-10-01` (222d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 1 · **Total matching days:** 1 · **History:** 2021-05-17 → 2026-10-01

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | -1.0% | -1.0% | -1.0% | -1.0% | 0% |
| **SPY** | 3m | 1 | -1.0% | -1.0% | -1.0% | -1.0% | 0% |
| **SPY** | 6m | 1 | -1.0% | -1.0% | -1.0% | -1.0% | 0% |
| **USO** | 1m | 1 | +1.1% | +1.1% | +1.1% | +1.1% | 100% |
| **USO** | 3m | 1 | +1.1% | +1.1% | +1.1% | +1.1% | 100% |
| **USO** | 6m | 1 | +1.1% | +1.1% | +1.1% | +1.1% | 100% |
| **GLD** | 1m | 1 | -2.7% | -2.7% | -2.7% | -2.7% | 0% |
| **GLD** | 3m | 1 | -2.7% | -2.7% | -2.7% | -2.7% | 0% |
| **GLD** | 6m | 1 | -2.7% | -2.7% | -2.7% | -2.7% | 0% |
| **TLT** | 1m | 1 | -2.0% | -2.0% | -2.0% | -2.0% | 0% |
| **TLT** | 3m | 1 | -2.0% | -2.0% | -2.0% | -2.0% | 0% |
| **TLT** | 6m | 1 | -2.0% | -2.0% | -2.0% | -2.0% | 0% |

**Episodes (последни 5 от 1):**
- `2026-09-25 → 2026-09-25` (1d)

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 10 · **Total matching days:** 101 · **History:** 2021-05-17 → 2026-10-01

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 10 | -0.1% | +0.6% | -7.2% | +7.8% | 60% |
| **SPY** | 3m | 10 | +1.8% | +1.3% | -8.3% | +11.6% | 60% |
| **SPY** | 6m | 10 | +1.1% | +3.2% | -20.8% | +14.2% | 70% |
| **USO** | 1m | 10 | +4.1% | +0.5% | -15.0% | +52.9% | 50% |
| **USO** | 3m | 10 | +9.6% | +8.7% | -20.7% | +52.2% | 60% |
| **USO** | 6m | 10 | +11.6% | +5.4% | -27.6% | +56.3% | 60% |
| **GLD** | 1m | 10 | -1.2% | -1.9% | -8.3% | +11.7% | 20% |
| **GLD** | 3m | 10 | -1.4% | -1.3% | -12.0% | +6.4% | 50% |
| **GLD** | 6m | 10 | -0.6% | -2.2% | -15.2% | +25.0% | 40% |
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
**Episodes:** 17 · **Total matching days:** 294 · **History:** 2021-05-17 → 2026-10-01

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 17 | +1.9% | +1.6% | -4.8% | +9.0% | 71% |
| **SPY** | 3m | 17 | +3.0% | +4.2% | -12.6% | +16.2% | 71% |
| **SPY** | 6m | 17 | +6.4% | +7.8% | -14.0% | +21.0% | 76% |
| **USO** | 1m | 17 | +2.4% | -2.2% | -13.0% | +22.9% | 41% |
| **USO** | 3m | 17 | +3.5% | -0.8% | -14.5% | +29.9% | 41% |
| **USO** | 6m | 17 | +13.8% | +2.6% | -12.4% | +87.1% | 71% |
| **GLD** | 1m | 17 | +2.4% | +2.1% | -5.6% | +9.0% | 76% |
| **GLD** | 3m | 17 | +5.7% | +7.2% | -16.8% | +23.6% | 65% |
| **GLD** | 6m | 17 | +10.2% | +9.8% | -13.4% | +43.8% | 71% |
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
**Episodes:** 20 · **Total matching days:** 294 · **History:** 2021-05-17 → 2026-10-01

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 20 | +0.3% | +0.5% | -8.7% | +7.0% | 50% |
| **SPY** | 3m | 20 | +1.9% | +3.2% | -13.7% | +9.1% | 65% |
| **SPY** | 6m | 20 | +3.1% | +5.2% | -16.4% | +16.9% | 70% |
| **USO** | 1m | 20 | -0.5% | -3.7% | -21.8% | +55.8% | 45% |
| **USO** | 3m | 20 | +3.8% | +0.3% | -12.7% | +64.3% | 50% |
| **USO** | 6m | 20 | +8.7% | +3.1% | -16.0% | +75.1% | 55% |
| **GLD** | 1m | 20 | -0.7% | -0.2% | -12.4% | +7.6% | 45% |
| **GLD** | 3m | 20 | +1.6% | +1.5% | -13.7% | +19.0% | 65% |
| **GLD** | 6m | 20 | +7.2% | +4.3% | -15.8% | +55.5% | 65% |
| **TLT** | 1m | 20 | -0.4% | -0.1% | -5.6% | +5.2% | 45% |
| **TLT** | 3m | 20 | -3.7% | -4.7% | -17.3% | +8.7% | 30% |
| **TLT** | 6m | 20 | -7.0% | -7.7% | -21.4% | +4.6% | 20% |

**Episodes (последни 5 от 20):**
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (13d)
- `2026-09-21 → 2026-10-01` (6d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-10-01

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (6 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 5 | 2.74 | 2.75 | 2026-08-29 00:00:00 | 2026-09-26 00:00:00 | ✓ |
| **COMPUTSA** | Завършени жилища (SAAR) | growth | housing_supply | 5 | 2.42 | 2.95 | 2026-08-29 00:00:00 | 2026-09-26 00:00:00 | ✓ |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | 5 | 2.34 | 2.70 | 2026-08-29 00:00:00 | 2026-09-26 00:00:00 | ✓ |
| **JTSQUR** | Quits rate — напускания | labor | flow | 4 | 2.02 | 2.02 | 2026-09-05 00:00:00 | 2026-09-26 00:00:00 | ✓ |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 3 | 2.25 | 2.25 | 2026-08-29 00:00:00 | 2026-09-12 00:00:00 | - |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | 1 | 2.22 | 2.22 | 2026-08-29 00:00:00 | 2026-08-29 00:00:00 | - |

### EU (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.28 | 5.28 | 2026-08-29 00:00:00 | 2026-09-26 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.18 | 2.18 | 2026-08-29 00:00:00 | 2026-09-26 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.15 | 2.17 | 2026-08-29 00:00:00 | 2026-09-26 00:00:00 | ✓ |

### CN (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 9 | 2.54 | 2.55 | 2026-08-31 00:00:00 | 2026-09-28 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 9 | 2.23 | 2.23 | 2026-08-31 00:00:00 | 2026-09-28 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 4 | 2.19 | 2.19 | 2026-09-07 00:00:00 | 2026-09-19 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-09-26 00:00:00 · **Generated:** 2026-09-26 07:41:11.346537+00:00

**Режим:** `transition` (Преходно / смесено)  
**Primary driver:** `none`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 38.6 | mixed | 29.6% | 3 | 2 |
| **growth** | 46.4 | mixed | 44.0% | 1 | 1 |
| **inflation** | 41.2 | mixed | 38.9% | 1 | 1 |
| **liquidity** | 51.8 | mixed | 42.1% | 0 | 0 |

### Top anomalies (4 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **COMPUTSA** | Завършени жилища (SAAR) | growth, housing | housing_supply | -2.95 | down | -27.13 | 2026-08-01 | ✓ min |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.75 | down | 93.45 | 2026-04-01 | ✓ min |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | -2.25 | down | 61.60 | 2026-08-01 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | -2.02 | down | 1.90 | 2026-07-01 | ✓ min |

### Narrative hints от макро лещите
- **COMPUTSA**: Завършва construction pipeline (12-18m след starts). Превишение спрямо sales = inventory build.
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **CIVPART**: Структурни сдвигове (демография, ранно пенсиониране). Пост-COVID не се възстанови напълно.
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
  - `state`: transition
  - `interpretation`: Mixed — waiting for clarification.
  - `slot_a_label`: Hard activity
  - `slot_b_label`: Labor market (claims inverted)
  - `breadth_a`: 0.4
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.8
  - `breadth_b_raw`: 0.667
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Realized CPI × Expectations
  - `question_bg`: Дали expectations следват realized inflation, или стоят anchored?
  - `state`: transition
  - `interpretation`: Monitoring.
  - `slot_a_label`: Realized inflation
  - `slot_b_label`: Inflation expectations
  - `breadth_a`: 0.5
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
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
  - `breadth_a`: 0.333
  - `breadth_b`: 0.4
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.333
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
> Сигналите са в преход — няма доминираща конфигурация. Следващите 2-3 релиза ще ориентират посоката. Най-отклонена леща: Монетарна политика и кредит — breadth 71% (разширяване), 0 аномалии, 0 нови екстремума. За наблюдение следващия релиз: COMPUTSA, LABOR_SHARE_NBS, JTSQUR (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: COMPUTSA z=-2.95 · NEW-5Y-MIN
- 3 нови екстремуми в top-4 (lookback 5г.)
- Активни двойки: Credit × Policy=both_up; model_vs_market=a_down_b_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-09-26 00:00:00 · **Generated:** 2026-09-26 07:59:45.848308+00:00

**Режим:** `disinflation_cooling` (Дезинфлация и охлаждане)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 41.7 | mixed | 42.9% | 0 | 0 |
| **growth** | 42.2 | mixed | 25.0% | 0 | 0 |
| **inflation** | 49.6 | mixed | 42.9% | 0 | 0 |
| **credit** | 44.0 | mixed | 36.8% | 3 | 2 |
| **external** | 38.6 | mixed | 16.7% | 0 | 0 |

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
> Синхронно охлаждане — labor и инфлация отстъпват заедно. Рискът се мести към overshooting, ако claims ускорят. Най-отклонена леща: Растеж и активност — breadth 76% (разширяване), 0 аномалии, 0 нови екстремума. За наблюдение следващия релиз: FR_10Y, DE_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.28
- 2 нови екстремуми в top-3 (lookback 5г.)
- Активни двойки: Stagflation test=both_down; fragmentation_risk=a_up_b_down



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-09-28 00:00:00 · **Generated:** 2026-09-28 12:10:47.229820+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 29.0 | contracting | -% | - | - |
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
> Претеглен композитен macro score 35.0/100 → режим „ВЛОШАВАЩ СЕ“ (5/5 лещи). 5 лещи, 2 flagged аномалии (4 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-09-25 |
| `as_of` | 2026-09-25 |
| `regime` | GROWTH |
| `alignment_score` | 5.0 |
| `gms_score` | 4.0 |
| `gms_max` | 8 |
| `gms_tier` | MEDIUM |
| `ks_status` | inactive |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-09-25 → 2026-09-30)

**stable_winner (1m):** +7 entered, -7 exited
  - **Entered:** ADM, APA, CHRW, EBAY, MAR, PNC, STX
  - **Exited:** EME, ETR, EVRG, FRT, GNRC, NEE, PWR

**stable_winner (3m):** +6 entered, -4 exited
  - **Entered:** AEP, ETR, EVRG, GEV, GM, NEE _(включително 1 за първи път в историята: AEP)_
  - **Exited:** EIX, HWM, MNST, STLD

**quality_dip (1m):** +7 entered, -7 exited
  - **Entered:** EME, ETR, EVRG, FRT, GL, NEE, PWR _(включително 1 за първи път в историята: GL)_
  - **Exited:** ADM, APA, CHRW, EBAY, MAR, PNC, STX

**quality_dip (3m):** +5 entered, -7 exited
  - **Entered:** EIX, GL, HWM, MNST, STLD _(включително 1 за първи път в историята: GL)_
  - **Exited:** AEP, ETR, EVRG, GEV, GM, GNRC, NEE

**faded_bounce (1m):** +17 entered, -11 exited
  - **Entered:** AJG, AZO, BX, CCI, CEG, COIN, CPRT, CTAS, GIS, LDOS, MAA, MOS, NVR, PGR, RSG, VLTO, VRSK _(включително 4 за първи път в историята: AZO, CEG, LDOS, NVR)_
  - **Exited:** AMCR, BAX, BLDR, COO, EQT, HRL, INVH, IP, PYPL, SHW, VST

**faded_bounce (3m):** +4 entered, -4 exited
  - **Entered:** ARES, CEG, TSCO, VRSK _(включително 1 за първи път в историята: CEG)_
  - **Exited:** CLX, INVH, IP, PYPL



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-09-22 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **soymeal** | Commodities | 192368 | 100.0 | 100.0 | 1059 | 95332 |
| **soybeans** | Commodities | 265041 | 99.9 | 99.9 | 1059 | 66787 |
| **corn** | Commodities | 414437 | 99.6 | 99.6 | 1059 | 37924 |
| **copper** | Commodities | 82649 | 96.7 | 96.7 | 1059 | 6203 |
| **rbob** | Commodities | 96163 | 96.6 | 96.6 | 1059 | 16305 |
| **soyoil** | Commodities | 96622 | 93.8 | 93.8 | 1059 | 8180 |
| **sugar** | Commodities | 224006 | 93.7 | 93.7 | 1059 | 16924 |
| **cotton** | Commodities | 81610 | 93.6 | 93.6 | 1059 | -14231 |
| **aud** | FX | 58726 | 88.1 | 88.1 | 1059 | 4665 |
| **jpy** | FX | 7423 | 72.8 | 72.8 | 1059 | 84465 |
| **vix** | Volatility | -15015 | 71.8 | 71.8 | 1018 | 15128 |
| **gold** | Commodities | 131334 | 56.2 | 56.2 | 1059 | -19981 |
| **wheat** | Commodities | -13144 | 52.8 | 52.8 | 1059 | 1027 |
| **gbpfx** | FX | 13239 | 51.5 | 51.5 | 1059 | -34670 |
| **coffee** | Commodities | 11098 | 48.2 | 48.2 | 1059 | -15595 |
| **platinum** | Commodities | 9789 | 46.5 | 46.5 | 1059 | -686 |
| **dxy** | FX | -4495 | 41.9 | 41.9 | 1059 | -13684 |
| **brent** | Commodities | 4425 | 41.7 | 41.7 | 242 | -2813 |
| **eurfx** | FX | -26694 | 41.3 | 41.3 | 1059 | 11665 |
| **cattle** | Commodities | 46983 | 41.0 | 41.0 | 1059 | -10458 |
| **heatingoil** | Commodities | 9732 | 40.8 | 40.8 | 1059 | -7610 |
| **wti** | Commodities | 142588 | 37.2 | 37.2 | 1059 | 38015 |
| **natgas** | Commodities | -65632 | 35.0 | 35.0 | 1059 | 5864 |
| **us30y** | Rates | -162052 | 33.5 | 33.5 | 1059 | 140942 |
| **silver** | Commodities | 13016 | 32.9 | 32.9 | 1059 | -219 |
| **bitcoin** | Crypto | -7953 | 30.5 | 30.5 | 442 | 136 |
| **sp500** | US Equities | -375574 | 26.9 | 26.9 | 1059 | -60370 |
| **nasdaq** | US Equities | -30683 | 25.0 | 25.0 | 1059 | 10549 |
| **us2y** | Rates | -1350740 | 16.5 | 16.5 | 1059 | -117987 |
| **cad** | FX | -46861 | 15.2 | 15.2 | 1059 | 25231 |
| **us5y** | Rates | -1858062 | 14.3 | 14.3 | 1059 | 253748 |
| **chf** | FX | -16457 | 10.6 | 10.6 | 1059 | -7632 |
| **palladium** | Commodities | -5984 | 10.5 | 10.5 | 1059 | -498 |
| **cocoa** | Commodities | -19422 | 8.0 | 8.0 | 1059 | -4795 |
| **us10y** | Rates | -1926947 | 7.5 | 7.5 | 1059 | 207392 |
| **russell** | US Equities | -107982 | 4.9 | 4.9 | 595 | -10282 |
| **usultra10y** | Rates | -395678 | 4.5 | 4.5 | 549 | -23521 |
| **hogs** | Commodities | -35548 | 0.1 | 0.1 | 1059 | -4413 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MRNA** | Healthcare | 97.4 | 37.2% | 165.6% | 279.1% | 454.1% | 1.56 | -34.2% |
| 2 | **ILMN** | Healthcare | 96.4 | 28.1% | 48.8% | 122.0% | 132.5% | 2.19 | -25.7% |
| 3 | **HPE** | Technology | 95.9 | 22.6% | 45.7% | 169.8% | 119.8% | 1.67 | -26.4% |
| 4 | **DELL** | Technology | 95.2 | 18.0% | 26.7% | 229.3% | 244.9% | 1.88 | -32.3% |
| 5 | **VLO** | Energy | 94.8 | 8.0% | 44.4% | 58.2% | 112.9% | 2.15 | -12.1% |
| 6 | **MPC** | Energy | 94.5 | 5.9% | 49.7% | 63.0% | 93.2% | 1.93 | -18.3% |
| 7 | **CRWD** | Technology | 94.2 | 14.6% | 37.0% | 171.2% | 89.2% | 1.35 | -37.2% |
| 8 | **PSX** | Energy | 91.9 | 3.5% | 47.1% | 41.9% | 84.5% | 1.94 | -17.3% |
| 9 | **AMD** | Technology | 91.5 | 30.0% | 13.1% | 200.7% | 191.7% | 1.80 | -27.8% |
| 10 | **CRL** | Healthcare | 91.5 | 2.4% | 28.8% | 71.0% | 96.1% | 1.43 | -33.9% |
| 11 | **NTAP** | Technology | 89.9 | 13.4% | 34.8% | 106.8% | 59.0% | 1.26 | -24.8% |
| 12 | **LITE** | Technology | 89.6 | 6.2% | 21.2% | 38.2% | 462.6% | 1.80 | -42.8% |
| 13 | **FTNT** | Technology | 89.5 | 4.6% | 12.4% | 118.8% | 101.9% | 1.70 | -14.3% |
| 14 | **RVTY** | Healthcare | 89.0 | 18.8% | 35.6% | 74.7% | 53.1% | 1.42 | -30.1% |
| 15 | **PANW** | Technology | 88.9 | 4.0% | 12.9% | 147.8% | 87.4% | 1.31 | -36.0% |
| 16 | **MU** | Technology | 88.7 | 11.1% | 3.2% | 215.3% | 485.9% | 2.27 | -39.1% |
| 17 | **STX** | Technology | 87.2 | 11.4% | 0.9% | 135.8% | 264.5% | 1.83 | -31.8% |
| 18 | **TGT** | Consumer Defensive | 86.7 | -2.6% | 21.2% | 31.5% | 88.4% | 1.83 | -13.5% |
| 19 | **IQV** | Healthcare | 85.1 | 2.9% | 32.3% | 57.6% | 44.5% | 0.86 | -35.9% |
| 20 | **MRVL** | Technology | 85.0 | 24.8% | -2.9% | 166.9% | 157.4% | 1.45 | -48.4% |

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
| 1 | **EIX** | Utilities | 1.824 | 0.266 | 1.059 | 3.216 | -1.011 | - | 5.6 | +19.7% |
| 2 | **CF** | Materials | 1.524 | 0.927 | 1.294 | 1.622 | 0.489 | - | 8.5 | +29.9% |
| 3 | **SNDK** | Information Technology | 1.477 | 1.972 | 1.554 | 0.296 | -0.165 | - | 23.6 | +91.6% |
| 4 | **NEM** | Materials | 1.435 | 1.045 | 1.715 | 0.845 | 0.567 | - | 14.4 | +25.9% |
| 5 | **MO** | Consumer Staples | 1.288 | -0.037 | 2.090 | 1.047 | -0.467 | - | 14.2 | - |
| 6 | **APA** | Energy | 1.198 | 1.042 | 1.267 | 0.734 | -0.153 | - | 9.1 | +26.7% |
| 7 | **EXPE** | Consumer Discretionary | 1.175 | 1.793 | 0.792 | 0.511 | -0.675 | - | 16.6 | +89.5% |
| 8 | **SYF** | Financials | 1.174 | -0.019 | 1.174 | 1.720 | -0.395 | - | 7.3 | +20.8% |
| 9 | **BMY** | Health Care | 1.140 | 0.996 | 0.873 | 1.048 | 0.583 | - | 13.7 | +46.6% |
| 10 | **HST** | Real Estate | 1.128 | 1.320 | 0.482 | 1.144 | -0.304 | - | 15.1 | +15.6% |
| 11 | **MU** | Information Technology | 1.084 | 1.721 | 0.912 | 0.220 | -0.519 | - | 14.3 | +66.6% |
| 12 | **SPG** | Real Estate | 1.083 | 0.730 | 1.392 | 0.591 | -1.355 | - | 14.2 | +120.5% |
| 13 | **MAS** | Industrials | 1.069 | -0.189 | 1.460 | 1.305 | -0.836 | - | 15.8 | +5862.5% |
| 14 | **TGT** | Consumer Staples | 0.976 | 2.464 | -0.088 | 0.352 | -0.763 | - | 16.3 | +26.4% |
| 15 | **TPR** | Consumer Discretionary | 0.906 | 0.646 | 1.142 | 0.488 | -1.026 | - | 16.4 | +197.1% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -1.879 | -1.360 | -0.929 | -2.487 | -0.992 |
| 502 | **TSLA** | Consumer Discretionary | -1.831 | -0.629 | -1.375 | -2.544 | -0.385 |
| 501 | **CSGP** | Real Estate | -1.621 | -3.299 | -0.465 | -0.603 | 0.651 |
| 500 | **BA** | Industrials | -1.611 | -0.674 | -1.206 | -2.134 | -1.084 |
| 499 | **COIN** | Financials | -1.587 | -2.447 | -1.665 | 0.000 | -1.685 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W40.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W40.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd G:\Archive\old-projects\dashboards-root\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-09-28  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
