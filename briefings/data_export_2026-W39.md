# Сателит — пълен data export за 2026-W39

_Период: 2026-09-21 → 2026-09-27_  
_Генериран: 2026-09-25 11:20 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W39.md` (structured briefing) и `narrative_2026-W39.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**15 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **HYG** | -0.81% | -2.11σ | 78.53 | 77.89 | 2026-09-18 | 2026-09-24 | -0.14% | +0.32% | 13 |
| **LQD** | -1.48% | -1.95σ | 104.70 | 103.15 | 2026-09-18 | 2026-09-24 | -0.31% | +0.60% | 13 |
| **XLF** | -2.38% | -1.84σ | 55.86 | 54.53 | 2026-09-18 | 2026-09-24 | +0.33% | +1.48% | 13 |
| **TLT** | -2.25% | -1.78σ | 81.25 | 79.42 | 2026-09-18 | 2026-09-24 | -0.50% | +0.99% | 13 |
| **IEF** | -1.22% | -1.72σ | 90.80 | 89.69 | 2026-09-18 | 2026-09-24 | -0.29% | +0.54% | 13 |
| **XLU** | -4.23% | -1.67σ | 41.10 | 39.36 | 2026-09-18 | 2026-09-24 | -0.63% | +2.16% | 13 |
| **SOXX** | +6.19% | +1.59σ | 533.07 | 566.07 | 2026-09-18 | 2026-09-24 | -1.28% | +4.71% | 13 |
| **UUP** | +1.06% | +1.45σ | 28.39 | 28.69 | 2026-09-18 | 2026-09-24 | +0.03% | +0.71% | 13 |
| **XLE** | -2.66% | -1.40σ | 64.31 | 62.60 | 2026-09-18 | 2026-09-24 | +1.43% | +2.92% | 13 |
| **TIP** | -0.92% | -1.35σ | 105.27 | 104.30 | 2026-09-18 | 2026-09-24 | -0.29% | +0.47% | 13 |
| **XLC** | +2.87% | +1.28σ | 110.81 | 113.99 | 2026-09-18 | 2026-09-24 | +0.12% | +2.14% | 13 |
| **XLP** | -1.33% | -1.26σ | 82.80 | 81.70 | 2026-09-18 | 2026-09-24 | -0.04% | +1.02% | 13 |
| **XLRE** | -2.07% | -1.21σ | 42.53 | 41.65 | 2026-09-18 | 2026-09-24 | -0.23% | +1.53% | 13 |
| **QQQ** | +2.72% | +1.17σ | 721.45 | 741.10 | 2026-09-18 | 2026-09-24 | -0.17% | +2.47% | 13 |
| **VNQ** | -1.87% | -1.06σ | 92.91 | 91.17 | 2026-09-18 | 2026-09-24 | -0.20% | +1.57% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-09-27 · **Conditions matched:** 2/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | -0.47% | ❌ | 153.82 | 153.09 | 2026-09-18 | 2026-09-24 |
| DFEN | down ≥ 3.0% | -1.84% | ❌ | 52.16 | 51.20 | 2026-09-18 | 2026-09-24 |
| GLD | down ≥ 1.0% | -2.36% | ✅ | 401.17 | 391.69 | 2026-09-18 | 2026-09-24 |
| URA | down ≥ 3.0% | -1.90% | ❌ | 41.65 | 40.86 | 2026-09-18 | 2026-09-24 |
| UUP | up ≥ 0.5% | +1.06% | ✅ | 28.39 | 28.69 | 2026-09-18 | 2026-09-24 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-09-27 · **Conditions matched:** 1/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | -0.86% | ❌ | 284.10 | 281.66 | 2026-09-18 | 2026-09-24 |
| XLF | up ≥ 1.0% | -2.38% | ❌ | 55.86 | 54.53 | 2026-09-18 | 2026-09-24 |
| XLY | up ≥ 1.0% | -0.64% | ❌ | 111.03 | 110.32 | 2026-09-18 | 2026-09-24 |
| GLD | down ≥ 0.5% | -2.36% | ✅ | 401.17 | 391.69 | 2026-09-18 | 2026-09-24 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2025-W44 (week ending 2025-11-02)
**Cosine similarity:** 0.8441 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -0.08% | +1.45% | +5.66% |
| **USO** | -3.25% | +9.59% | +96.80% |
| **GLD** | +5.19% | +20.87% | +14.96% |
| **TLT** | -1.64% | -3.50% | -5.18% |
| **XLE** | +2.28% | +15.85% | +33.55% |
| **IWM** | -0.43% | +5.45% | +13.42% |

### Паралел #2: 2024-W21 (week ending 2024-05-26)
**Cosine similarity:** 0.8251 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.91% | +6.17% | +12.48% |
| **USO** | +4.71% | +0.27% | -1.46% |
| **GLD** | -0.63% | +7.46% | +15.71% |
| **TLT** | +3.41% | +7.67% | -1.08% |
| **XLE** | +0.13% | -1.07% | +6.46% |
| **IWM** | -2.38% | +7.27% | +16.22% |

### Паралел #3: 2024-W49 (week ending 2024-12-08)
**Cosine similarity:** 0.7832 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -3.16% | -5.25% | -1.43% |
| **USO** | +11.29% | +2.63% | +1.62% |
| **GLD** | +0.66% | +10.47% | +25.61% |
| **TLT** | -8.97% | -4.53% | -9.58% |
| **XLE** | -3.38% | -3.94% | -8.36% |
| **IWM** | -6.78% | -13.80% | -11.31% |

### Паралел #4: 2024-W03 (week ending 2024-01-21)
**Cosine similarity:** 0.7516 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.97% | +2.64% | +13.80% |
| **USO** | +5.23% | +14.57% | +13.34% |
| **GLD** | -0.24% | +17.61% | +17.99% |
| **TLT** | -1.33% | -5.25% | -1.24% |
| **XLE** | +5.76% | +18.46% | +15.22% |
| **IWM** | +3.35% | +0.37% | +12.69% |

### Паралел #5: 2023-W21 (week ending 2023-05-28)
**Cosine similarity:** 0.7281 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.85% | +4.75% | +8.40% |
| **USO** | -5.40% | +11.81% | +9.29% |
| **GLD** | -1.79% | -1.82% | +2.54% |
| **TLT** | +2.06% | -5.81% | -11.17% |
| **XLE** | +0.20% | +11.20% | +7.82% |
| **IWM** | +4.09% | +4.46% | +1.81% |

### Паралел #6: 2021-W46 (week ending 2021-11-21)
**Cosine similarity:** 0.7079 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.24% | -7.39% | -16.90% |
| **USO** | -4.11% | +20.38% | +51.82% |
| **GLD** | -3.24% | +2.61% | -0.34% |
| **TLT** | +0.52% | -6.83% | -20.12% |
| **XLE** | -0.27% | +24.47% | +49.57% |
| **IWM** | -6.25% | -14.29% | -24.34% |

### Паралел #7: 2023-W45 (week ending 2023-11-12)
**Cosine similarity:** 0.6857 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.33% | +13.75% | +18.21% |
| **USO** | -10.50% | -0.17% | +4.89% |
| **GLD** | +2.22% | +4.51% | +21.84% |
| **TLT** | +7.53% | +6.66% | +2.42% |
| **XLE** | -2.65% | -0.12% | +12.49% |
| **IWM** | +10.58% | +17.88% | +20.81% |

### Паралел #8: 2024-W23 (week ending 2024-06-09)
**Cosine similarity:** 0.6646 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.08% | +1.19% | +13.82% |
| **USO** | +9.24% | -5.60% | -3.81% |
| **GLD** | +3.29% | +8.99% | +14.82% |
| **TLT** | +0.93% | +8.81% | +3.16% |
| **XLE** | -1.37% | -4.42% | +1.14% |
| **IWM** | +0.10% | +3.33% | +18.75% |

### Паралел #9: 2023-W19 (week ending 2023-05-14)
**Cosine similarity:** 0.6645 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +6.09% | +8.28% | +7.05% |
| **USO** | +0.11% | +19.62% | +15.66% |
| **GLD** | -3.36% | -4.93% | -3.91% |
| **TLT** | -2.93% | -8.54% | -15.61% |
| **XLE** | +3.07% | +14.49% | +6.23% |
| **IWM** | +8.81% | +10.58% | -2.09% |

### Паралел #10: 2022-W27 (week ending 2022-07-10)
**Cosine similarity:** 0.6582 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.84% | -6.66% | -0.15% |
| **USO** | -6.48% | -4.38% | -17.46% |
| **GLD** | +3.02% | -2.72% | +7.03% |
| **TLT** | +4.79% | -10.23% | -6.51% |
| **XLE** | +5.36% | +15.29% | +23.41% |
| **IWM** | +8.31% | -3.98% | +1.13% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 15 · **Total matching days:** 84 · **History:** 2021-05-17 → 2026-09-24

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 15 | +2.1% | +1.7% | -3.1% | +7.4% | 73% |
| **SPY** | 3m | 15 | +2.7% | +2.5% | -7.3% | +12.0% | 80% |
| **SPY** | 6m | 15 | +7.2% | +8.6% | -6.8% | +21.8% | 80% |
| **USO** | 1m | 15 | +0.3% | -0.8% | -14.3% | +12.7% | 47% |
| **USO** | 3m | 15 | -0.6% | -3.3% | -18.9% | +24.5% | 47% |
| **USO** | 6m | 15 | +14.0% | +1.6% | -8.7% | +109.4% | 60% |
| **GLD** | 1m | 15 | +2.8% | +0.9% | -1.2% | +9.0% | 73% |
| **GLD** | 3m | 15 | +5.2% | +5.9% | -12.6% | +24.5% | 67% |
| **GLD** | 6m | 15 | +6.1% | +6.3% | -12.5% | +25.3% | 67% |
| **TLT** | 1m | 15 | -1.5% | -1.1% | -6.7% | +3.6% | 33% |
| **TLT** | 3m | 15 | -0.9% | -0.5% | -16.5% | +11.1% | 47% |
| **TLT** | 6m | 15 | -4.6% | -6.0% | -18.0% | +7.5% | 27% |

**Episodes (последни 5 от 15):**
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-08-03` (5d)
- `2026-09-10 → 2026-09-24` (10d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 93 · **History:** 2021-05-17 → 2026-09-24

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +6.3% | +6.3% | +3.5% | +9.1% | 100% |
| **SPY** | 3m | 2 | +6.2% | +6.2% | +2.0% | +10.3% | 100% |
| **SPY** | 6m | 2 | +7.8% | +7.8% | +2.0% | +13.5% | 100% |
| **USO** | 1m | 2 | +5.6% | +5.6% | +4.0% | +7.2% | 100% |
| **USO** | 3m | 2 | +8.7% | +8.7% | -9.9% | +27.4% | 50% |
| **USO** | 6m | 2 | +25.1% | +25.1% | +22.9% | +27.4% | 100% |
| **GLD** | 1m | 2 | +3.5% | +3.5% | -0.2% | +7.2% | 50% |
| **GLD** | 3m | 2 | -4.3% | -4.3% | -13.8% | +5.3% | 50% |
| **GLD** | 6m | 2 | -2.3% | -2.3% | -9.9% | +5.3% | 50% |
| **TLT** | 1m | 2 | -1.4% | -1.4% | -1.8% | -1.0% | 0% |
| **TLT** | 3m | 2 | -4.2% | -4.2% | -5.5% | -2.9% | 0% |
| **TLT** | 6m | 2 | -7.1% | -7.1% | -8.6% | -5.5% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-09-24` (46d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 449 · **History:** 2021-05-17 → 2026-09-24

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
- `2025-11-03 → 2026-09-24` (217d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-09-24

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 10 · **Total matching days:** 100 · **History:** 2021-05-17 → 2026-09-24

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 10 | -0.1% | +0.8% | -7.2% | +7.8% | 60% |
| **SPY** | 3m | 10 | +1.9% | +1.7% | -8.3% | +11.6% | 60% |
| **SPY** | 6m | 10 | +1.1% | +3.4% | -20.8% | +14.2% | 70% |
| **USO** | 1m | 10 | +4.3% | +0.5% | -15.0% | +52.9% | 50% |
| **USO** | 3m | 10 | +10.0% | +9.8% | -20.7% | +52.2% | 60% |
| **USO** | 6m | 10 | +12.1% | +6.5% | -27.6% | +56.3% | 60% |
| **GLD** | 1m | 10 | -0.9% | -1.4% | -8.3% | +11.7% | 20% |
| **GLD** | 3m | 10 | -1.0% | -0.5% | -12.0% | +6.4% | 50% |
| **GLD** | 6m | 10 | -0.2% | -1.0% | -15.2% | +25.0% | 40% |
| **TLT** | 1m | 10 | -2.2% | -2.7% | -6.0% | +2.5% | 10% |
| **TLT** | 3m | 10 | -6.3% | -5.2% | -17.6% | +4.2% | 20% |
| **TLT** | 6m | 10 | -9.8% | -8.1% | -22.3% | +1.2% | 10% |

**Episodes (последни 5 от 10):**
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-05-19` (36d)
- `2026-07-22 → 2026-08-03` (8d)
- `2026-09-01 → 2026-09-24` (14d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 17 · **Total matching days:** 294 · **History:** 2021-05-17 → 2026-09-24

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 17 | +1.9% | +1.6% | -4.8% | +9.0% | 71% |
| **SPY** | 3m | 17 | +3.1% | +4.2% | -12.6% | +16.2% | 71% |
| **SPY** | 6m | 17 | +6.4% | +8.2% | -14.0% | +21.0% | 76% |
| **USO** | 1m | 17 | +2.4% | -2.2% | -13.0% | +22.9% | 41% |
| **USO** | 3m | 17 | +3.7% | -0.8% | -14.5% | +29.9% | 41% |
| **USO** | 6m | 17 | +14.1% | +2.6% | -12.4% | +87.1% | 71% |
| **GLD** | 1m | 17 | +2.4% | +2.1% | -5.6% | +9.0% | 76% |
| **GLD** | 3m | 17 | +5.8% | +7.2% | -16.8% | +23.6% | 65% |
| **GLD** | 6m | 17 | +10.5% | +9.8% | -11.4% | +43.8% | 71% |
| **TLT** | 1m | 17 | +0.3% | -0.0% | -6.3% | +8.2% | 47% |
| **TLT** | 3m | 17 | -1.7% | -1.7% | -15.3% | +11.9% | 35% |
| **TLT** | 6m | 17 | -4.8% | -4.0% | -21.3% | +7.0% | 35% |

**Episodes (последни 5 от 17):**
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)
- `2026-08-07 → 2026-09-03` (19d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 20 · **Total matching days:** 291 · **History:** 2021-05-17 → 2026-09-24

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 20 | +0.3% | +0.5% | -8.7% | +7.0% | 50% |
| **SPY** | 3m | 20 | +2.0% | +3.2% | -13.7% | +9.1% | 65% |
| **SPY** | 6m | 20 | +3.1% | +5.4% | -16.4% | +16.9% | 70% |
| **USO** | 1m | 20 | -0.4% | -3.7% | -21.8% | +55.8% | 45% |
| **USO** | 3m | 20 | +3.9% | +1.4% | -12.7% | +64.3% | 50% |
| **USO** | 6m | 20 | +8.9% | +4.2% | -16.0% | +75.1% | 55% |
| **GLD** | 1m | 20 | -0.6% | -0.2% | -12.4% | +7.6% | 45% |
| **GLD** | 3m | 20 | +1.7% | +1.5% | -13.7% | +19.0% | 65% |
| **GLD** | 6m | 20 | +7.5% | +4.3% | -15.8% | +55.5% | 65% |
| **TLT** | 1m | 20 | -0.3% | -0.1% | -5.6% | +5.2% | 45% |
| **TLT** | 3m | 20 | -3.6% | -3.9% | -17.3% | +8.7% | 30% |
| **TLT** | 6m | 20 | -6.8% | -7.0% | -21.4% | +4.6% | 20% |

**Episodes (последни 5 от 20):**
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (13d)
- `2026-09-21 → 2026-09-24` (3d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-09-24

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (8 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 5 | 2.74 | 2.75 | 2026-08-22 00:00:00 | 2026-09-19 00:00:00 | ✓ |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | 5 | 2.43 | 2.70 | 2026-08-22 00:00:00 | 2026-09-19 00:00:00 | ✓ |
| **COMPUTSA** | Завършени жилища (SAAR) | growth | housing_supply | 5 | 2.24 | 2.95 | 2026-08-22 00:00:00 | 2026-09-19 00:00:00 | ✓ |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 3 | 2.25 | 2.25 | 2026-08-29 00:00:00 | 2026-09-12 00:00:00 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | 3 | 2.02 | 2.02 | 2026-09-05 00:00:00 | 2026-09-19 00:00:00 | ✓ |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | 2 | 2.22 | 2.22 | 2026-08-22 00:00:00 | 2026-08-29 00:00:00 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 1 | 2.16 | 2.16 | 2026-08-22 00:00:00 | 2026-08-22 00:00:00 | - |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | 1 | 2.09 | 2.09 | 2026-08-22 00:00:00 | 2026-08-22 00:00:00 | - |

### EU (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.28 | 5.28 | 2026-08-22 00:00:00 | 2026-09-19 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.18 | 2.18 | 2026-08-22 00:00:00 | 2026-09-19 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.16 | 2.17 | 2026-08-22 00:00:00 | 2026-09-19 00:00:00 | ✓ |

### CN (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 9 | 2.55 | 2.55 | 2026-08-24 00:00:00 | 2026-09-21 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 9 | 2.22 | 2.23 | 2026-08-24 00:00:00 | 2026-09-21 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 4 | 2.19 | 2.19 | 2026-09-07 00:00:00 | 2026-09-19 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-09-19 00:00:00 · **Generated:** 2026-09-19 07:20:51.220083+00:00

**Режим:** `transition` (Преходно / смесено)  
**Primary driver:** `none`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 38.5 | mixed | 29.6% | 3 | 2 |
| **growth** | 46.3 | mixed | 44.0% | 1 | 1 |
| **inflation** | 40.8 | mixed | 38.9% | 1 | 1 |
| **liquidity** | 52.3 | mixed | 42.1% | 0 | 0 |

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
  - `breadth_a`: 0.6
  - `breadth_b`: 1.0
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
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
  - `breadth_b`: 0.333
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.333
- 🔔 **?**
  - `pair_id`: credit_policy_transmission
  - `name_bg`: Credit spreads × Policy rates
  - `question_bg`: Дали credit следва policy направление — transmission intact?
  - `state`: a_down_b_up
  - `interpretation`: Benign credit despite tightening — liquidity cushion intact.
  - `slot_a_label`: Credit stress
  - `slot_b_label`: Policy tightening
  - `breadth_a`: 0.0
  - `breadth_b`: 1.0
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.0
  - `breadth_b_raw`: 1.0
- 🔔 **?**
  - `pair_id`: sentiment_vs_hard_data
  - `name_bg`: Consumer sentiment × Hard activity
  - `question_bg`: Дали sentiment потвърждава hard data, или има разминаване?
  - `state`: transition
  - `interpretation`: Monitoring — divergence typical в political transitions.
  - `slot_a_label`: Consumer sentiment
  - `slot_b_label`: Hard activity
  - `breadth_a`: 0.667
  - `breadth_b`: 0.6
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.667
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
  - `breadth_b`: 0.333
  - `state_raw`: both_down
  - `breadth_a_raw`: 0.0
  - `breadth_b_raw`: 0.333

### Executive narrative
> Сигналите са в преход — няма доминираща конфигурация. Следващите 2-3 релиза ще ориентират посоката. Най-отклонена леща: Инфлация и цени — breadth 62% (разширяване), 1 аномалии, 1 нови екстремума. За наблюдение следващия релиз: COMPUTSA, LABOR_SHARE_NBS, JTSQUR (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: COMPUTSA z=-2.95 · NEW-5Y-MIN
- 3 нови екстремуми в top-4 (lookback 5г.)
- Активни двойки: Credit × Policy=a_down_b_up; model_vs_market=both_down



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-09-19 00:00:00 · **Generated:** 2026-09-19 07:32:44.399284+00:00

**Режим:** `disinflation_cooling` (Дезинфлация и охлаждане)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 41.7 | mixed | 42.9% | 0 | 0 |
| **growth** | 41.8 | mixed | 25.0% | 0 | 0 |
| **inflation** | 49.6 | mixed | 42.9% | 0 | 0 |
| **credit** | 43.1 | mixed | 36.8% | 3 | 2 |
| **external** | 38.8 | mixed | 25.0% | 0 | 0 |

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

**Дата:** 2026-09-21 00:00:00 · **Generated:** 2026-09-21 11:18:34.894475+00:00

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
| `date` | 2026-09-18 |
| `as_of` | 2026-09-18 |
| `regime` | GROWTH |
| `alignment_score` | 3.0 |
| `gms_score` | 3.0 |
| `gms_max` | 8 |
| `gms_tier` | MEDIUM |
| `ks_status` | inactive |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-09-18 → 2026-09-23)

**stable_winner (1m):** +5 entered, -9 exited
  - **Entered:** CAT, FCX, HLT, PFG, VTR _(включително 2 за първи път в историята: HLT, PFG)_
  - **Exited:** AEP, EME, GEV, IBKR, INCY, IRM, MRK, STLD, VLO

**stable_winner (3m):** +8 entered, -9 exited
  - **Entered:** EIX, FDX, HLT, IBKR, LITE, NEM, SATS, VTR _(включително 1 за първи път в историята: HLT)_
  - **Exited:** BG, CAH, CFG, EVRG, FITB, IRM, LLY, PNC, WDC

**quality_dip (1m):** +10 entered, -5 exited
  - **Entered:** AEP, EME, GEV, IBKR, INCY, IRM, MRK, STLD, VLO, WST _(включително 1 за първи път в историята: WST)_
  - **Exited:** CAT, FCX, HLT, PFG, VTR

**quality_dip (3m):** +10 entered, -8 exited
  - **Entered:** BG, CAH, CFG, EVRG, FITB, IRM, LLY, PNC, WDC, WST _(включително 2 за първи път в историята: EVRG, WST)_
  - **Exited:** EIX, FDX, HLT, IBKR, LITE, NEM, SATS, VTR

**faded_bounce (1m):** +13 entered, -6 exited
  - **Entered:** COIN, EOG, EQT, FISV, JKHY, MKC, PGR, PODD, RSG, SBAC, SPGI, UBER, VLTO _(включително 2 за първи път в историята: SBAC, SPGI)_
  - **Exited:** ARES, AXON, CLX, DPZ, HRL, IP

**faded_bounce (3m):** +5 entered, -1 exited
  - **Entered:** ISRG, SBAC, STZ, VLTO, VRSK _(включително 3 за първи път в историята: ISRG, SBAC, VLTO)_
  - **Exited:** TDG

### EU (period: 2026-09-18 → 2026-09-21)

**stable_winner (1m):** +3 entered, -7 exited
  - **Entered:** BG.VI, NOKIA.HE, ZEG.L _(включително 1 за първи път в историята: NOKIA.HE)_
  - **Exited:** ACLN.SW, CA.PA, FR.PA, GLE.PA, ITX.MC, ORA.PA, PKN.WA

**stable_winner (3m):** +3 entered, -3 exited
  - **Entered:** BBVA.MC, BCP.LS, RXL.PA
  - **Exited:** FRO.OL, ING.WA, MBK.WA

**quality_dip (1m):** +7 entered, -3 exited
  - **Entered:** AAL.L, CA.PA, FR.PA, GLE.PA, ITX.MC, ORA.PA, PKN.WA _(включително 1 за първи път в историята: AAL.L)_
  - **Exited:** BG.VI, NOKIA.HE, ZEG.L

**quality_dip (3m):** +4 entered, -4 exited
  - **Entered:** AAL.L, FRO.OL, ING.WA, MBK.WA _(включително 1 за първи път в историята: AAL.L)_
  - **Exited:** ACLN.SW, BBVA.MC, BCP.LS, RXL.PA

**faded_bounce (1m):** +7 entered, -6 exited
  - **Entered:** DCC.L, EXPN.L, LATO-B.ST, LIFCO-B.ST, TBCG.L, TOM.OL, TW.L
  - **Exited:** ARCAD.AS, BME.L, EZJ.L, HNR1.DE, SCA-B.ST, VTY.L

**faded_bounce (3m):** +5 entered, -2 exited
  - **Entered:** BC.MI, FDJU.PA, GFC.PA, RI.PA, RMS.PA
  - **Exited:** EZJ.L, WKL.AS



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-09-15 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **soymeal** | Commodities | 185546 | 100.0 | 100.0 | 1058 | 102522 |
| **corn** | Commodities | 426842 | 99.8 | 99.8 | 1058 | 176337 |
| **soybeans** | Commodities | 244710 | 99.4 | 99.4 | 1058 | 93048 |
| **cotton** | Commodities | 97903 | 98.3 | 98.3 | 1058 | 19235 |
| **soyoil** | Commodities | 110894 | 97.5 | 97.5 | 1058 | 12657 |
| **sugar** | Commodities | 236288 | 95.7 | 95.7 | 1058 | 84939 |
| **copper** | Commodities | 65541 | 90.9 | 90.9 | 1058 | -13684 |
| **rbob** | Commodities | 83217 | 90.5 | 90.5 | 1058 | 8892 |
| **aud** | FX | 61135 | 89.4 | 89.4 | 1058 | 9027 |
| **jpy** | FX | 23170 | 85.5 | 85.5 | 1058 | 91141 |
| **vix** | Volatility | -16504 | 70.7 | 70.7 | 1017 | 2589 |
| **wheat** | Commodities | -4706 | 60.1 | 60.1 | 1058 | 21779 |
| **gold** | Commodities | 137060 | 59.8 | 59.8 | 1058 | -8862 |
| **gbpfx** | FX | 18878 | 57.4 | 57.4 | 1058 | -23999 |
| **brent** | Commodities | 7241 | 54.8 | 54.8 | 241 | 249 |
| **coffee** | Commodities | 15654 | 52.5 | 52.5 | 1058 | -11085 |
| **sp500** | US Equities | -293143 | 50.6 | 50.6 | 1058 | -11741 |
| **nasdaq** | US Equities | -6387 | 49.5 | 49.5 | 1058 | 55384 |
| **heatingoil** | Commodities | 13468 | 49.1 | 49.1 | 1058 | -3002 |
| **platinum** | Commodities | 9182 | 44.7 | 44.7 | 1058 | 2244 |
| **dxy** | FX | -4909 | 40.9 | 40.9 | 1058 | -13021 |
| **eurfx** | FX | -28156 | 40.3 | 40.3 | 1058 | 29560 |
| **cattle** | Commodities | 45262 | 39.7 | 39.7 | 1058 | -16252 |
| **bitcoin** | Crypto | -6354 | 36.5 | 36.5 | 441 | 1085 |
| **wti** | Commodities | 136768 | 35.6 | 35.6 | 1058 | 32733 |
| **silver** | Commodities | 12632 | 32.4 | 32.4 | 1058 | 1864 |
| **us30y** | Rates | -211735 | 28.3 | 28.3 | 1058 | 149648 |
| **cad** | FX | -39022 | 20.8 | 20.8 | 1058 | 49875 |
| **natgas** | Commodities | -100024 | 19.2 | 19.2 | 1058 | -124 |
| **us2y** | Rates | -1294575 | 17.4 | 17.4 | 1058 | -51571 |
| **cocoa** | Commodities | -12445 | 14.0 | 14.0 | 1058 | 1168 |
| **chf** | FX | -14964 | 12.8 | 12.8 | 1058 | -5893 |
| **us5y** | Rates | -1986928 | 12.6 | 12.6 | 1058 | 182886 |
| **palladium** | Commodities | -5638 | 11.2 | 11.2 | 1058 | -268 |
| **russell** | US Equities | -97203 | 9.4 | 9.4 | 594 | 2583 |
| **us10y** | Rates | -1868126 | 7.9 | 7.9 | 1058 | 360887 |
| **usultra10y** | Rates | -399246 | 4.0 | 4.0 | 548 | -45769 |
| **hogs** | Commodities | -31401 | 0.1 | 0.1 | 1058 | -7915 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MRNA** | Healthcare | 97.3 | 31.1% | 201.4% | 254.7% | 422.9% | 1.48 | -34.2% |
| 2 | **ILMN** | Healthcare | 95.7 | 16.4% | 54.8% | 106.3% | 113.5% | 1.80 | -25.7% |
| 3 | **VLO** | Energy | 95.3 | 8.6% | 55.6% | 56.8% | 112.3% | 2.16 | -12.1% |
| 4 | **DELL** | Technology | 95.2 | 26.9% | 26.9% | 212.3% | 223.3% | 1.89 | -32.3% |
| 5 | **MPC** | Energy | 94.9 | 7.1% | 58.0% | 60.3% | 96.8% | 2.01 | -18.3% |
| 6 | **HPE** | Technology | 93.6 | 19.2% | 28.2% | 162.2% | 111.6% | 1.56 | -26.4% |
| 7 | **AMD** | Technology | 93.1 | 34.6% | 18.2% | 199.3% | 185.8% | 1.82 | -27.8% |
| 8 | **PSX** | Energy | 92.8 | 6.0% | 52.9% | 41.1% | 92.3% | 2.13 | -17.3% |
| 9 | **PANW** | Technology | 92.6 | 12.1% | 37.9% | 150.2% | 68.6% | 1.26 | -36.0% |
| 10 | **CRL** | Healthcare | 92.3 | -7.1% | 37.2% | 74.2% | 94.0% | 1.20 | -33.9% |
| 11 | **CRWD** | Technology | 92.2 | 37.7% | 56.0% | 167.2% | 54.7% | 1.32 | -37.2% |
| 12 | **FTNT** | Technology | 91.2 | 17.6% | 23.0% | 125.3% | 78.8% | 1.69 | -14.3% |
| 13 | **MU** | Technology | 88.3 | 17.7% | 2.2% | 171.2% | 453.9% | 2.27 | -39.1% |
| 14 | **MRK** | Healthcare | 87.6 | -1.1% | 23.5% | 28.9% | 91.8% | 1.98 | -11.4% |
| 15 | **NTAP** | Technology | 87.0 | 5.1% | 26.6% | 89.8% | 52.6% | 0.99 | -24.8% |
| 16 | **RVTY** | Healthcare | 86.2 | 15.5% | 34.6% | 62.6% | 42.9% | 1.18 | -30.1% |
| 17 | **SNDK** | Technology | 85.7 | 21.7% | -5.1% | 158.6% | 1350.8% | 2.46 | -56.5% |
| 18 | **TGT** | Consumer Defensive | 85.7 | -8.0% | 11.5% | 37.1% | 104.2% | 1.91 | -14.6% |
| 19 | **IQV** | Healthcare | 85.3 | 2.9% | 44.3% | 61.3% | 38.5% | 0.76 | -35.9% |
| 20 | **DDOG** | Technology | 85.2 | 11.4% | 12.9% | 105.2% | 63.2% | 0.82 | -48.6% |

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
| 1 | **EIX** | Utilities | 2.496 | 2.150 | 1.056 | 3.253 | -1.006 | - | 5.4 | +19.7% |
| 2 | **CF** | Materials | 1.695 | 1.087 | 1.293 | 1.911 | 0.529 | - | 8.8 | +29.9% |
| 3 | **NEM** | Materials | 1.532 | 1.183 | 1.717 | 0.945 | 0.521 | - | 15.3 | +25.9% |
| 4 | **SNDK** | Information Technology | 1.503 | 2.010 | 1.560 | 0.307 | -0.179 | - | 23.8 | +91.6% |
| 5 | **MO** | Consumer Staples | 1.278 | -0.072 | 2.091 | 1.012 | -0.465 | - | 14.5 | - |
| 6 | **APA** | Energy | 1.277 | 1.183 | 1.261 | 0.803 | -0.128 | - | 9.2 | +26.7% |
| 7 | **HST** | Real Estate | 1.230 | 1.517 | 0.476 | 1.250 | -0.263 | - | 14.8 | +15.6% |
| 8 | **EXPE** | Consumer Discretionary | 1.179 | 1.780 | 0.795 | 0.535 | -0.694 | - | 16.5 | +89.5% |
| 9 | **SYF** | Financials | 1.171 | -0.101 | 1.173 | 1.777 | -0.488 | - | 7.3 | +20.8% |
| 10 | **BMY** | Health Care | 1.142 | 0.979 | 0.873 | 1.069 | 0.568 | - | 13.5 | +46.6% |
| 11 | **SPG** | Real Estate | 1.129 | 0.838 | 1.384 | 0.599 | -1.351 | - | 14.4 | +120.5% |
| 12 | **MAS** | Industrials | 1.046 | -0.323 | 1.455 | 1.350 | -0.818 | - | 15.7 | +5862.5% |
| 13 | **TGT** | Consumer Staples | 1.016 | 2.611 | -0.094 | 0.359 | -0.770 | - | 16.2 | +26.4% |
| 14 | **MU** | Information Technology | 0.971 | 1.768 | 0.904 | -0.103 | -0.552 | - | 24.4 | +66.6% |
| 15 | **TPR** | Consumer Discretionary | 0.956 | 0.637 | 1.150 | 0.599 | -1.016 | - | 15.4 | +197.1% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -1.916 | -1.487 | -0.921 | -2.497 | -0.989 |
| 502 | **TSLA** | Consumer Discretionary | -1.902 | -0.864 | -1.376 | -2.519 | -0.363 |
| 501 | **COIN** | Financials | -1.678 | -2.657 | -1.692 | 0.000 | -1.698 |
| 500 | **KKR** | Financials | -1.669 | -1.874 | -0.846 | -1.609 | -0.853 |
| 499 | **BA** | Industrials | -1.595 | -0.642 | -1.171 | -2.165 | -1.126 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W39.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W39.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-09-21  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
