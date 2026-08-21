# Сателит — пълен data export за 2026-W34

_Период: 2026-08-17 → 2026-08-23_  
_Генериран: 2026-08-21 06:47 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W34.md` (structured briefing) и `narrative_2026-W34.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**17 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **XLI** | -3.61% | -3.13σ | 186.51 | 179.77 | 2026-08-14 | 2026-08-20 | +0.66% | +1.36% | 13 |
| **IBIT** | +15.63% | +3.01σ | 35.63 | 41.20 | 2026-08-14 | 2026-08-20 | -1.57% | +5.71% | 13 |
| **XLF** | -2.08% | -2.85σ | 58.16 | 56.95 | 2026-08-14 | 2026-08-20 | +1.01% | +1.08% | 13 |
| **DFEN** | -18.08% | -2.34σ | 88.24 | 72.29 | 2026-08-14 | 2026-08-20 | +3.53% | +9.24% | 13 |
| **DIA** | -1.73% | -2.10σ | 536.80 | 527.51 | 2026-08-14 | 2026-08-20 | +0.63% | +1.12% | 13 |
| **IWM** | -2.43% | -1.66σ | 305.09 | 297.67 | 2026-08-14 | 2026-08-20 | +0.75% | +1.92% | 13 |
| **GDX** | +10.98% | +1.37σ | 89.97 | 99.85 | 2026-08-14 | 2026-08-20 | +0.51% | +7.67% | 13 |
| **GLD** | +3.43% | +1.30σ | 401.48 | 415.26 | 2026-08-14 | 2026-08-20 | -0.26% | +2.83% | 13 |
| **SPY** | -1.77% | -1.29σ | 776.34 | 762.60 | 2026-08-14 | 2026-08-20 | +0.39% | +1.68% | 13 |
| **DBC** | +3.70% | +1.27σ | 30.00 | 31.11 | 2026-08-14 | 2026-08-20 | -0.25% | +3.10% | 13 |
| **DBA** | +2.20% | +1.27σ | 27.77 | 28.38 | 2026-08-14 | 2026-08-20 | -0.00% | +1.73% | 13 |
| **SLV** | +5.44% | +1.24σ | 58.48 | 61.66 | 2026-08-14 | 2026-08-20 | -1.13% | +5.27% | 13 |
| **TIP** | +0.50% | +1.15σ | 106.99 | 107.52 | 2026-08-14 | 2026-08-20 | -0.25% | +0.65% | 13 |
| **UUP** | -0.71% | -1.11σ | 28.11 | 27.91 | 2026-08-14 | 2026-08-20 | +0.10% | +0.73% | 13 |
| **XLK** | -3.64% | -1.08σ | 190.01 | 183.10 | 2026-08-14 | 2026-08-20 | +0.66% | +3.98% | 13 |
| **EFA** | -1.19% | -1.04σ | 108.64 | 107.35 | 2026-08-14 | 2026-08-20 | +0.52% | +1.64% | 13 |
| **QQQ** | -2.75% | -1.02σ | 731.07 | 710.93 | 2026-08-14 | 2026-08-20 | +0.28% | +2.96% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-08-23 · **Conditions matched:** 2/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | +6.27% | ✅ | 126.60 | 134.54 | 2026-08-14 | 2026-08-20 |
| DFEN | down ≥ 3.0% | -18.08% | ✅ | 88.24 | 72.29 | 2026-08-14 | 2026-08-20 |
| GLD | down ≥ 1.0% | +3.43% | ❌ | 401.48 | 415.26 | 2026-08-14 | 2026-08-20 |
| URA | down ≥ 3.0% | -2.43% | ❌ | 44.93 | 43.84 | 2026-08-14 | 2026-08-20 |
| UUP | up ≥ 0.5% | -0.71% | ❌ | 28.11 | 27.91 | 2026-08-14 | 2026-08-20 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-08-23 · **Conditions matched:** 0/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | -2.43% | ❌ | 305.09 | 297.67 | 2026-08-14 | 2026-08-20 |
| XLF | up ≥ 1.0% | -2.08% | ❌ | 58.16 | 56.95 | 2026-08-14 | 2026-08-20 |
| XLY | up ≥ 1.0% | -1.29% | ❌ | 118.20 | 116.68 | 2026-08-14 | 2026-08-20 |
| GLD | down ≥ 0.5% | +3.43% | ❌ | 401.48 | 415.26 | 2026-08-14 | 2026-08-20 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2023-W14 (week ending 2023-04-09)
**Cosine similarity:** 0.8989 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.43% | +7.18% | +4.97% |
| **USO** | -7.67% | -6.28% | +5.55% |
| **GLD** | +1.36% | -4.21% | -9.00% |
| **TLT** | -5.05% | -8.71% | -21.87% |
| **XLE** | -5.55% | -4.93% | +0.88% |
| **IWM** | -0.21% | +6.22% | -0.51% |

### Паралел #2: 2022-W09 (week ending 2022-03-06)
**Cosine similarity:** 0.8832 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.36% | -5.00% | -9.24% |
| **USO** | -5.86% | +12.60% | -10.11% |
| **GLD** | -2.42% | -6.04% | -13.29% |
| **TLT** | -8.38% | -17.26% | -21.41% |
| **XLE** | +0.96% | +18.98% | +6.29% |
| **IWM** | +2.18% | -5.84% | -9.35% |

### Паралел #3: 2022-W50 (week ending 2022-12-18)
**Cosine similarity:** 0.8627 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.78% | +1.75% | +14.66% |
| **USO** | +9.18% | -9.61% | -0.85% |
| **GLD** | +6.48% | +10.18% | +8.90% |
| **TLT** | -0.98% | -0.24% | -4.21% |
| **XLE** | +6.85% | -8.76% | -4.15% |
| **IWM** | +7.14% | -1.80% | +6.64% |

### Паралел #4: 2022-W44 (week ending 2022-11-06)
**Cosine similarity:** 0.8619 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.64% | +9.57% | +9.64% |
| **USO** | -15.09% | -16.17% | -17.95% |
| **GLD** | +5.35% | +10.86% | +19.81% |
| **TLT** | +13.51% | +13.25% | +11.32% |
| **XLE** | -6.67% | -5.97% | -12.24% |
| **IWM** | +0.78% | +10.25% | -2.37% |

### Паралел #5: 2025-W02 (week ending 2025-01-12)
**Cosine similarity:** 0.8601 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.28% | -8.02% | +7.43% |
| **USO** | -2.94% | -17.58% | -4.15% |
| **GLD** | +7.73% | +20.03% | +24.55% |
| **TLT** | +3.48% | +1.67% | +0.39% |
| **XLE** | +3.22% | -10.75% | +0.84% |
| **IWM** | +4.09% | -14.97% | +2.25% |

### Паралел #6: 2025-W24 (week ending 2025-06-15)
**Cosine similarity:** 0.8597 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.21% | +10.12% | +14.20% |
| **USO** | -6.18% | -8.61% | -14.22% |
| **GLD** | -3.02% | +6.05% | +25.02% |
| **TLT** | -1.53% | +4.19% | +1.17% |
| **XLE** | -1.38% | +0.57% | +3.31% |
| **IWM** | +4.75% | +14.10% | +21.52% |

### Паралел #7: 2025-W16 (week ending 2025-04-20)
**Cosine similarity:** 0.8553 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +12.62% | +19.22% | +26.21% |
| **USO** | -1.18% | +9.28% | -2.16% |
| **GLD** | -0.83% | +0.74% | +27.07% |
| **TLT** | -2.40% | -2.62% | +4.19% |
| **XLE** | +2.56% | +5.47% | +5.50% |
| **IWM** | +12.12% | +19.22% | +30.53% |

### Паралел #8: 2025-W39 (week ending 2025-09-28)
**Cosine similarity:** 0.8419 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.81% | +4.30% | -4.19% |
| **USO** | -7.31% | -11.09% | +61.26% |
| **GLD** | +5.09% | +20.19% | +19.60% |
| **TLT** | +3.51% | -1.30% | -3.67% |
| **XLE** | -5.03% | -3.90% | +36.01% |
| **IWM** | +3.16% | +4.18% | +0.73% |

### Паралел #9: 2024-W14 (week ending 2024-04-07)
**Cosine similarity:** 0.8260 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -0.25% | +6.98% | +10.52% |
| **USO** | -8.37% | -1.32% | -7.34% |
| **GLD** | -0.43% | +2.69% | +13.88% |
| **TLT** | -0.71% | +1.28% | +4.55% |
| **XLE** | -4.97% | -8.14% | -5.00% |
| **IWM** | +0.25% | -1.75% | +7.19% |

### Паралел #10: 2026-W09 (week ending 2026-03-01)
**Cosine similarity:** 0.8193 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -5.20% | +10.28% | +11.17% |
| **USO** | +55.28% | +57.52% | +64.17% |
| **GLD** | -11.05% | -13.77% | -14.16% |
| **TLT** | -4.55% | -5.57% | -9.34% |
| **XLE** | +9.55% | +0.66% | +14.00% |
| **IWM** | -5.13% | +11.10% | +13.87% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 14 · **Total matching days:** 74 · **History:** 2021-05-17 → 2026-08-20

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 14 | +2.2% | +2.4% | -3.1% | +7.4% | 71% |
| **SPY** | 3m | 14 | +2.8% | +2.6% | -7.3% | +12.0% | 79% |
| **SPY** | 6m | 14 | +7.6% | +9.8% | -6.8% | +21.8% | 79% |
| **USO** | 1m | 14 | +0.5% | +0.3% | -14.3% | +12.7% | 50% |
| **USO** | 3m | 14 | -1.4% | -2.0% | -18.9% | +24.5% | 50% |
| **USO** | 6m | 14 | +12.0% | +2.1% | -10.7% | +109.4% | 57% |
| **GLD** | 1m | 14 | +3.1% | +2.0% | -0.9% | +9.0% | 79% |
| **GLD** | 3m | 14 | +6.2% | +7.3% | -12.6% | +24.5% | 71% |
| **GLD** | 6m | 14 | +7.8% | +11.4% | -12.5% | +25.3% | 71% |
| **TLT** | 1m | 14 | -1.5% | -1.1% | -6.7% | +3.6% | 36% |
| **TLT** | 3m | 14 | -0.6% | -0.1% | -16.5% | +11.1% | 50% |
| **TLT** | 6m | 14 | -4.2% | -3.2% | -18.0% | +7.5% | 29% |

**Episodes (последни 5 от 14):**
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-08-03` (5d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 70 · **History:** 2021-05-17 → 2026-08-20

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +6.3% | +6.3% | +3.5% | +9.1% | 100% |
| **SPY** | 3m | 2 | +5.8% | +5.8% | +1.4% | +10.3% | 100% |
| **SPY** | 6m | 2 | +7.1% | +7.1% | +1.4% | +12.8% | 100% |
| **USO** | 1m | 2 | +5.6% | +5.6% | +4.0% | +7.2% | 100% |
| **USO** | 3m | 2 | +1.0% | +1.0% | -9.9% | +12.0% | 50% |
| **USO** | 6m | 2 | +10.0% | +10.0% | +8.0% | +12.0% | 100% |
| **GLD** | 1m | 2 | +3.5% | +3.5% | -0.2% | +7.2% | 50% |
| **GLD** | 3m | 2 | -1.1% | -1.1% | -13.8% | +11.6% | 50% |
| **GLD** | 6m | 2 | +3.6% | +3.6% | -4.4% | +11.6% | 50% |
| **TLT** | 1m | 2 | -1.4% | -1.4% | -1.8% | -1.0% | 0% |
| **TLT** | 3m | 2 | -2.5% | -2.5% | -2.9% | -2.1% | 0% |
| **TLT** | 6m | 2 | -3.7% | -3.7% | -5.3% | -2.1% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-08-20` (23d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 425 · **History:** 2021-05-17 → 2026-08-20

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
- `2025-11-03 → 2026-08-20` (193d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-08-20

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 9 · **Total matching days:** 86 · **History:** 2021-05-17 → 2026-08-20

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 9 | -0.2% | +0.9% | -7.2% | +7.8% | 56% |
| **SPY** | 3m | 9 | +1.9% | +2.0% | -8.3% | +11.6% | 56% |
| **SPY** | 6m | 9 | +1.1% | +4.1% | -20.8% | +14.2% | 67% |
| **USO** | 1m | 9 | +3.8% | -1.3% | -15.0% | +52.9% | 44% |
| **USO** | 3m | 9 | +8.6% | +2.2% | -20.7% | +52.2% | 56% |
| **USO** | 6m | 9 | +10.1% | +2.2% | -27.6% | +49.2% | 56% |
| **GLD** | 1m | 9 | -1.2% | -1.6% | -8.3% | +9.5% | 22% |
| **GLD** | 3m | 9 | -0.2% | +0.2% | -12.0% | +9.5% | 56% |
| **GLD** | 6m | 9 | +1.1% | -0.8% | -11.4% | +25.0% | 44% |
| **TLT** | 1m | 9 | -2.0% | -2.5% | -6.0% | +2.5% | 11% |
| **TLT** | 3m | 9 | -6.3% | -5.7% | -17.6% | +4.2% | 22% |
| **TLT** | 6m | 9 | -10.1% | -7.9% | -22.3% | +1.2% | 11% |

**Episodes (последни 5 от 9):**
- `2023-04-12 → 2023-04-18` (5d)
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-05-19` (36d)
- `2026-07-22 → 2026-08-03` (8d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 17 · **Total matching days:** 285 · **History:** 2021-05-17 → 2026-08-20

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 17 | +1.9% | +1.6% | -4.8% | +9.0% | 71% |
| **SPY** | 3m | 17 | +3.0% | +4.2% | -12.6% | +16.2% | 71% |
| **SPY** | 6m | 17 | +6.4% | +7.6% | -14.0% | +21.0% | 76% |
| **USO** | 1m | 17 | +2.0% | -2.2% | -13.0% | +22.9% | 41% |
| **USO** | 3m | 17 | +2.7% | -0.8% | -14.5% | +29.9% | 41% |
| **USO** | 6m | 17 | +12.3% | +2.6% | -12.4% | +87.1% | 71% |
| **GLD** | 1m | 17 | +2.6% | +2.2% | -5.6% | +9.0% | 76% |
| **GLD** | 3m | 17 | +6.1% | +7.2% | -16.8% | +23.6% | 71% |
| **GLD** | 6m | 17 | +11.1% | +9.8% | -8.4% | +43.8% | 76% |
| **TLT** | 1m | 17 | +0.3% | -0.0% | -6.3% | +8.2% | 47% |
| **TLT** | 3m | 17 | -1.5% | -1.1% | -15.3% | +11.9% | 35% |
| **TLT** | 6m | 17 | -4.4% | -1.7% | -21.3% | +7.0% | 35% |

**Episodes (последни 5 от 17):**
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)
- `2026-08-07 → 2026-08-20` (10d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 19 · **Total matching days:** 288 · **History:** 2021-05-17 → 2026-08-20

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 19 | +0.4% | +1.0% | -8.7% | +7.0% | 53% |
| **SPY** | 3m | 19 | +2.1% | +3.4% | -13.7% | +9.1% | 68% |
| **SPY** | 6m | 19 | +3.3% | +6.8% | -16.4% | +16.9% | 74% |
| **USO** | 1m | 19 | -0.6% | -5.6% | -21.8% | +55.8% | 42% |
| **USO** | 3m | 19 | +3.6% | -0.6% | -12.7% | +64.3% | 47% |
| **USO** | 6m | 19 | +9.0% | +1.1% | -16.0% | +75.1% | 53% |
| **GLD** | 1m | 19 | -0.6% | -0.1% | -12.4% | +7.6% | 47% |
| **GLD** | 3m | 19 | +2.0% | +1.7% | -13.7% | +19.0% | 68% |
| **GLD** | 6m | 19 | +8.2% | +6.0% | -15.8% | +55.5% | 74% |
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
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-08-20

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (11 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | 5 | 2.56 | 2.70 | 2026-07-18 00:00:00 | 2026-08-15 00:00:00 | ✓ |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 5 | 2.48 | 2.71 | 2026-07-18 00:00:00 | 2026-08-15 00:00:00 | ✓ |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 5 | 2.28 | 2.28 | 2026-07-18 00:00:00 | 2026-08-15 00:00:00 | ✓ |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 5 | 2.27 | 2.43 | 2026-07-18 00:00:00 | 2026-08-15 00:00:00 | - |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | 5 | 2.10 | 2.22 | 2026-07-18 00:00:00 | 2026-08-15 00:00:00 | - |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | 4 | 2.28 | 2.28 | 2026-07-18 00:00:00 | 2026-08-08 00:00:00 | ✓ |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 4 | 2.15 | 2.15 | 2026-07-18 00:00:00 | 2026-08-08 00:00:00 | - |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 3 | 2.30 | 2.30 | 2026-08-01 00:00:00 | 2026-08-15 00:00:00 | - |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | 3 | 2.09 | 2.09 | 2026-08-01 00:00:00 | 2026-08-15 00:00:00 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | 3 | 2.02 | 2.02 | 2026-07-18 00:00:00 | 2026-08-01 00:00:00 | ✓ |
| **MSACSR** | Месеци предлагане — нови жилища | housing | housing_affordability | 1 | 2.02 | 2.02 | 2026-07-18 00:00:00 | 2026-07-18 00:00:00 | ✓ |

### EU (6 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.27 | 5.27 | 2026-07-18 00:00:00 | 2026-08-15 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.16 | 2.17 | 2026-07-18 00:00:00 | 2026-08-15 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.15 | 2.17 | 2026-07-18 00:00:00 | 2026-08-15 00:00:00 | ✓ |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | 4 | 2.38 | 2.38 | 2026-07-18 00:00:00 | 2026-08-08 00:00:00 | - |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | 2 | 2.66 | 2.66 | 2026-07-18 00:00:00 | 2026-07-25 00:00:00 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation | sentiment | 2 | 2.17 | 2.17 | 2026-07-18 00:00:00 | 2026-07-25 00:00:00 | - |

### CN (2 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 7 | 2.55 | 2.56 | 2026-07-20 00:00:00 | 2026-08-17 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 7 | 2.23 | 2.23 | 2026-07-20 00:00:00 | 2026-08-17 00:00:00 | ✓ |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-08-15 00:00:00 · **Generated:** 2026-08-15 03:05:37.434097+00:00

**Режим:** `transition` (Преходно / смесено)  
**Primary driver:** `none`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 36.5 | contracting | 22.2% | 3 | 2 |
| **growth** | 45.4 | mixed | 40.0% | 2 | 1 |
| **inflation** | 41.2 | mixed | 38.9% | 2 | 1 |
| **liquidity** | 52.6 | mixed | 47.4% | 0 | 0 |

### Top anomalies (7 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.71 | down | 93.55 | 2026-04-01 | ✓ min |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | -2.70 | down | 61.40 | 2026-07-01 | ✓ min |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | -2.30 | down | 2.24 | 2026-05-01 | - |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | +2.28 | up | 55.10 | 2026-05-01 | ✓ max |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | -2.22 | down | 58.90 | 2026-07-01 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | +2.16 | up | 4.60 | 2026-06-01 | - |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | -2.09 | down | 2.70 | 2026-06-01 | - |

### Narrative hints от макро лещите
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **CIVPART**: Структурни сдвигове (демография, ранно пенсиониране). Пост-COVID не се възстанови напълно.
- **HPIPONM226S**: Monthly FHFA версия. Само purchase transactions (без refi appraisals). По-чист от refi-bias.
- **US_PMI_MFG**: Markit mfg — comparable cross-country. ISM е US-only.
- **EMRATIO**: Не зависи от definition на 'active labor force'. По-стабилен индикатор на дълбоката заетост.
- **MICH_INFL_1Y**: Household очаквания. По-шумни от market-based, но по-ранни. Extreme movements сигнализират de-anchoring risk.
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
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.8
  - `breadth_b_raw`: 0.667
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Realized CPI × Expectations
  - `question_bg`: Дали expectations следват realized inflation, или стоят anchored?
  - `state`: a_down_b_up
  - `interpretation`: Rare — expectations rising while realized cools (stagflation fear narrative?).
  - `slot_a_label`: Realized inflation
  - `slot_b_label`: Inflation expectations
  - `breadth_a`: 0.0
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.667
  - `breadth_b_raw`: 0.667
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
  - `state`: both_up
  - `interpretation`: Съгласие — underlying persistent + пазар pricing-ва inflation. Fed зад кривата.
  - `slot_a_label`: Модел (sticky inflation)
  - `slot_b_label`: Пазар (breakevens + survey)
  - `breadth_a`: 0.667
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.667
  - `breadth_b_raw`: 0.667

### Executive narrative
> Сигналите са в преход — няма доминираща конфигурация. Следващите 2-3 релиза ще ориентират посоката. Най-отклонена леща: Монетарна политика и кредит — breadth 31% (смесено), 0 аномалии, 0 нови екстремума. За наблюдение следващия релиз: LABOR_SHARE_NBS, CIVPART, US_PMI_MFG (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: LABOR_SHARE_NBS z=-2.71 · NEW-5Y-MIN
- 3 нови екстремуми в top-7 (lookback 5г.)
- Активни двойки: Inflation anchoring=a_down_b_up; Credit × Policy=a_down_b_up; model_vs_market=both_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-08-15 00:00:00 · **Generated:** 2026-08-15 03:22:07.933600+00:00

**Режим:** `policy_dilemma` (Policy dilemma)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 40.1 | mixed | 42.9% | 0 | 0 |
| **growth** | 42.2 | mixed | 16.7% | 0 | 0 |
| **inflation** | 49.6 | mixed | 71.4% | 0 | 0 |
| **credit** | 44.8 | mixed | 36.8% | 3 | 2 |
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
  - `state`: both_up
  - `interpretation`: Healthy expansion: sentiment + hard data confirm-ват растеж.
  - `slot_a_label`: Sentiment (ESI, confidence)
  - `slot_b_label`: Hard activity (IP, retail, GDP)
  - `breadth_a`: 0.667
  - `breadth_b`: 0.75
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.667
  - `breadth_b_raw`: 0.75
- 🔔 **?**
  - `pair_id`: growth_labor_lead_lag
  - `name_bg`: Растеж срещу труд (lead-lag)
  - `question_bg`: Активността и пазарът на труда движат ли се заедно?
  - `state`: both_up
  - `interpretation`: Синхронна експанзия: активността расте и трудовият пазар се засилва. Класическа expansion конфигурация.
  - `slot_a_label`: Твърда активност (IP, retail, GDP)
  - `slot_b_label`: Пазар на труда (сила)
  - `breadth_a`: 0.75
  - `breadth_b`: 0.75
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.75
  - `breadth_b_raw`: 1.0

### Executive narrative
> Policy dilemma — labor market е loose, но инфлацията remains hot. ЕЦБ е заклещена между инфлацията и растежа. Най-отклонена леща: Инфлация и цени — breadth 83% (разширяване), 0 аномалии, 0 нови екстремума. За наблюдение следващия релиз: FR_10Y, DE_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.27
- 2 нови екстремуми в top-3 (lookback 5г.)
- Активни двойки: Stagflation test=a_down_b_up; Sentiment × Hard=both_up; Growth × Labor=both_up



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-08-17 00:00:00 · **Generated:** 2026-08-17 06:52:12.099814+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 39.2 | mixed | -% | - | - |
| **inflation** | 44.9 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 47.8 | mixed | -% | - | - |
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
  - `state`: both_up
  - `interpretation`: Балансиран растеж — и износ, и вътрешно търсене се разширяват.
  - `slot_a_label`: Външно търсене
  - `slot_b_label`: Вътрешна активност
  - `breadth_a`: 0.833
  - `breadth_b`: 0.667

### Executive narrative
> Претеглен композитен macro score 38.0/100 → режим „ВЛОШАВАЩ СЕ“ (5/5 лещи). 5 лещи, 2 flagged аномалии (4 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-08-14 |
| `as_of` | 2026-08-14 |
| `regime` | REFLATION |
| `alignment_score` | 5.0 |
| `gms_score` | 3.0 |
| `gms_max` | 8 |
| `gms_tier` | MEDIUM |
| `ks_status` | inactive |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-08-14 → 2026-08-19)

**stable_winner (1m):** +8 entered, -6 exited
  - **Entered:** CASY, CBOE, COHR, GM, HAS, LITE, TPR, VRT
  - **Exited:** EIX, GEV, KEY, MNST, MRNA, PLD

**stable_winner (3m):** +5 entered, -4 exited
  - **Entered:** BG, HST, IBKR, IRM, VTR
  - **Exited:** CFG, GS, NEE, NTRS

**quality_dip (1m):** +6 entered, -10 exited
  - **Entered:** EIX, GEV, KEY, MNST, MRNA, PLD
  - **Exited:** CASY, CBOE, COHR, GM, HAS, LITE, LVS, TPR, ULTA, VRT

**quality_dip (3m):** +4 entered, -7 exited
  - **Entered:** CFG, GS, NEE, NTRS
  - **Exited:** BG, HST, IBKR, IRM, LVS, ULTA, VTR

**faded_bounce (1m):** +5 entered, -4 exited
  - **Entered:** BSX, CI, EFX, EQT, FIS _(включително 1 за първи път в историята: EQT)_
  - **Exited:** CMS, LII, OTIS, PODD

**faded_bounce (3m):** +4 entered, -2 exited
  - **Entered:** ARE, DASH, FIS, PODD _(включително 1 за първи път в историята: FIS)_
  - **Exited:** BSX, CSGP

### EU (period: 2026-08-14 → 2026-08-19)

**stable_winner (1m):** +8 entered, -3 exited
  - **Entered:** ABVX.PA, ASML.AS, BOL.ST, CA.PA, ING.WA, NESTE.HE, SAN.MC, URW.PA _(включително 2 за първи път в историята: BOL.ST, ING.WA)_
  - **Exited:** ACS.MC, SAND.ST, TPE.WA

**stable_winner (3m):** +5 entered, -4 exited
  - **Entered:** BOL.ST, DLG.MI, ELI.BR, RBI.VI, VWS.CO _(включително 1 за първи път в историята: BOL.ST)_
  - **Exited:** A5G.IR, CA.PA, SAND.ST, SPM.MI

**quality_dip (1m):** +2 entered, -7 exited
  - **Entered:** ACS.MC, SAND.ST
  - **Exited:** ABVX.PA, ASML.AS, BRBY.L, CA.PA, NESTE.HE, SAN.MC, URW.PA

**quality_dip (3m):** +5 entered, -6 exited
  - **Entered:** A5G.IR, CA.PA, ING.WA, SAND.ST, SPM.MI _(включително 2 за първи път в историята: ING.WA, SPM.MI)_
  - **Exited:** BRBY.L, DLG.MI, ELI.BR, RBI.VI, TPE.WA, VWS.CO

**faded_bounce (1m):** +2 entered, -2 exited
  - **Entered:** FDJU.PA, ICG.L
  - **Exited:** DGE.L, SGE.L

**faded_bounce (3m):** +1 entered, -1 exited
  - **Entered:** FDJU.PA _(включително 1 за първи път в историята: FDJU.PA)_
  - **Exited:** UMG.AS



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-08-11 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **copper** | Commodities | 80880 | 96.3 | 96.3 | 1053 | 18948 |
| **cotton** | Commodities | 72870 | 89.4 | 89.4 | 1053 | 23186 |
| **soyoil** | Commodities | 80922 | 88.8 | 88.8 | 1053 | -32107 |
| **soymeal** | Commodities | 71576 | 84.8 | 84.8 | 1053 | 23724 |
| **aud** | FX | 48541 | 81.9 | 81.9 | 1053 | 21319 |
| **rbob** | Commodities | 70040 | 81.5 | 81.5 | 1053 | 1089 |
| **gbpfx** | FX | 40670 | 80.0 | 80.0 | 1053 | 12129 |
| **dxy** | FX | 5772 | 76.2 | 76.2 | 1053 | 10638 |
| **vix** | Volatility | -12127 | 73.1 | 73.1 | 1012 | -22316 |
| **corn** | Commodities | 166770 | 64.1 | 64.1 | 1053 | 123379 |
| **soybeans** | Commodities | 101362 | 63.1 | 63.1 | 1053 | 28674 |
| **coffee** | Commodities | 24170 | 62.8 | 62.8 | 1053 | -797 |
| **gold** | Commodities | 141868 | 62.5 | 62.5 | 1053 | 22721 |
| **sp500** | US Equities | -280446 | 55.1 | 55.1 | 1053 | 84556 |
| **brent** | Commodities | 7630 | 55.1 | 55.1 | 236 | -5308 |
| **cattle** | Commodities | 64662 | 53.8 | 53.8 | 1053 | -31662 |
| **heatingoil** | Commodities | 14038 | 51.3 | 51.3 | 1053 | 3119 |
| **sugar** | Commodities | 58990 | 49.6 | 49.6 | 1053 | 153583 |
| **wheat** | Commodities | -31401 | 41.0 | 41.0 | 1053 | 5397 |
| **platinum** | Commodities | 7637 | 38.0 | 38.0 | 1053 | -509 |
| **bitcoin** | Crypto | -7052 | 33.3 | 33.3 | 436 | 439 |
| **jpy** | FX | -53070 | 28.2 | 28.2 | 1053 | 37391 |
| **eurfx** | FX | -60600 | 26.1 | 26.1 | 1053 | -6909 |
| **silver** | Commodities | 10312 | 26.0 | 26.0 | 1053 | -65 |
| **wti** | Commodities | 103715 | 21.6 | 21.6 | 1053 | 17332 |
| **chf** | FX | -11432 | 20.0 | 20.0 | 1053 | -1932 |
| **us2y** | Rates | -1359521 | 16.3 | 16.3 | 1053 | 312245 |
| **natgas** | Commodities | -110382 | 16.1 | 16.1 | 1053 | -4881 |
| **us30y** | Rates | -364824 | 13.4 | 13.4 | 1053 | 864 |
| **cocoa** | Commodities | -14011 | 12.2 | 12.2 | 1053 | -2811 |
| **palladium** | Commodities | -4904 | 12.2 | 12.2 | 1053 | 1301 |
| **us5y** | Rates | -2147744 | 11.2 | 11.2 | 1053 | 9006 |
| **russell** | US Equities | -95158 | 9.5 | 9.5 | 589 | -7046 |
| **usultra10y** | Rates | -361727 | 7.7 | 7.7 | 543 | 16838 |
| **us10y** | Rates | -2163714 | 2.7 | 2.7 | 1053 | -84061 |
| **hogs** | Commodities | -15121 | 2.4 | 2.4 | 1053 | 15317 |
| **nasdaq** | US Equities | -89125 | 1.5 | 1.5 | 1053 | -24962 |
| **cad** | FX | -92005 | 0.9 | 0.9 | 1053 | 766 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **DELL** | Technology | 98.0 | 8.3% | 86.3% | 276.5% | 196.3% | 1.62 | -32.3% |
| 2 | **MU** | Technology | 96.9 | -3.5% | 34.1% | 122.7% | 687.0% | 2.47 | -39.1% |
| 3 | **HPE** | Technology | 96.7 | 13.7% | 63.4% | 148.9% | 120.5% | 1.68 | -26.4% |
| 4 | **MRNA** | Healthcare | 96.5 | 192.3% | 281.4% | 274.2% | 112.4% | 1.46 | -35.5% |
| 5 | **PANW** | Technology | 95.8 | 5.2% | 49.8% | 136.1% | 94.2% | 1.61 | -36.0% |
| 6 | **MRVL** | Technology | 95.5 | 14.1% | 34.6% | 200.2% | 171.6% | 1.38 | -48.4% |
| 7 | **VLO** | Energy | 95.2 | 10.4% | 33.0% | 75.1% | 134.1% | 2.52 | -12.1% |
| 8 | **MPC** | Energy | 95.0 | 13.1% | 38.1% | 82.0% | 100.4% | 2.27 | -18.3% |
| 9 | **SNDK** | Technology | 92.8 | -1.3% | 13.4% | 161.3% | 3391.7% | 3.04 | -56.5% |
| 10 | **CRWD** | Technology | 92.2 | 5.5% | 30.7% | 94.0% | 79.3% | 1.23 | -37.2% |
| 11 | **PSX** | Energy | 92.1 | 14.8% | 33.5% | 57.1% | 78.7% | 2.18 | -17.3% |
| 12 | **STX** | Technology | 91.5 | -6.7% | 13.6% | 96.8% | 466.6% | 2.21 | -31.8% |
| 13 | **NTAP** | Technology | 91.0 | 17.3% | 61.8% | 93.5% | 54.9% | 1.31 | -24.8% |
| 14 | **FTNT** | Technology | 90.8 | -3.3% | 19.8% | 89.4% | 95.8% | 1.52 | -30.4% |
| 15 | **AMD** | Technology | 90.6 | -14.3% | 12.7% | 133.1% | 209.1% | 1.32 | -27.8% |
| 16 | **AMAT** | Technology | 89.8 | -12.1% | 22.1% | 34.7% | 247.8% | 1.83 | -39.6% |
| 17 | **CRL** | Healthcare | 88.5 | 32.2% | 90.2% | 83.5% | 39.8% | 1.24 | -33.9% |
| 18 | **STT** | Financial Services | 88.3 | 1.4% | 23.8% | 45.0% | 69.1% | 2.00 | -11.8% |
| 19 | **CNC** | Healthcare | 86.2 | -4.3% | 9.4% | 50.2% | 133.2% | 1.54 | -32.7% |
| 20 | **DDOG** | Technology | 86.0 | -8.3% | 8.5% | 91.8% | 97.4% | 0.82 | -48.6% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **ATS.VI** | Technology | 94.2 | -7.1% | 27.8% | 185.4% | 660.2% | 2.42 | -50.1% |
| 2 | **CCC.L** | Technology | 91.7 | 4.0% | 25.7% | 69.4% | 104.2% | 2.19 | -16.2% |
| 3 | **RBI.VI** | Financial Services | 90.2 | 16.5% | 35.2% | 51.1% | 77.5% | 1.86 | -18.0% |
| 4 | **REP.MC** | Energy | 88.7 | 10.6% | 20.1% | 55.8% | 85.0% | 2.14 | -20.4% |
| 5 | **AKER.OL** | Industrials | 88.5 | 15.3% | 14.3% | 65.9% | 92.4% | 2.51 | -15.6% |
| 6 | **UNI.MI** | Financial Services | 87.6 | 10.8% | 34.2% | 56.7% | 50.9% | 1.85 | -11.5% |
| 7 | **BMPS.MI** | Financial Services | 87.2 | 6.9% | 40.4% | 54.8% | 49.8% | 1.35 | -25.5% |
| 8 | **SSAB-B.ST** | Basic Materials | 87.0 | 7.2% | 20.2% | 43.6% | 81.9% | 1.85 | -34.3% |
| 9 | **PKN.WA** | Energy | 86.7 | 4.5% | 11.8% | 52.8% | 98.1% | 2.12 | -12.3% |
| 10 | **NESTE.HE** | Energy | 85.7 | -7.3% | 8.5% | 51.4% | 127.8% | 1.74 | -20.4% |
| 11 | **ASML.AS** | Technology | 85.5 | 1.5% | 14.8% | 24.3% | 141.0% | 2.03 | -20.8% |
| 12 | **BFT.WA** | Industrials | 85.3 | 4.4% | 26.8% | 41.4% | 55.3% | 1.71 | -17.4% |
| 13 | **ABN.AS** | Financial Services | 85.1 | 11.0% | 24.5% | 48.1% | 50.5% | 1.81 | -18.0% |
| 14 | **ZAB.WA** | Consumer Defensive | 84.8 | -3.9% | 32.3% | 44.1% | 50.8% | 1.12 | -17.2% |
| 15 | **FRO.OL** | Energy | 83.9 | 9.8% | 11.4% | 38.5% | 89.9% | 1.71 | -20.5% |
| 16 | **TPRO.MI** | Technology | 83.3 | -1.6% | -2.9% | 59.5% | 356.1% | 2.34 | -32.2% |
| 17 | **UNI.MC** | Financial Services | 83.3 | 10.9% | 29.5% | 37.9% | 42.7% | 1.75 | -17.8% |
| 18 | **BG.VI** | Financial Services | 82.9 | 1.2% | 18.3% | 36.4% | 58.1% | 1.72 | -16.3% |
| 19 | **DHER.DE** | Consumer Cyclical | 82.8 | -3.8% | 12.2% | 71.5% | 61.6% | 0.72 | -48.7% |
| 20 | **BAMI.MI** | Financial Services | 82.7 | 7.8% | 27.7% | 41.4% | 40.3% | 1.51 | -14.8% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **EIX** | Utilities | 2.467 | 2.396 | 1.026 | 3.005 | -0.682 | - | 7.7 | +19.7% |
| 2 | **CF** | Materials | 1.756 | 1.222 | 1.295 | 1.936 | 0.476 | - | 9.3 | +29.9% |
| 3 | **SNDK** | Information Technology | 1.658 | 1.835 | 1.754 | 0.610 | -0.218 | - | 21.7 | +91.6% |
| 4 | **MO** | Consumer Staples | 1.600 | 0.674 | 2.002 | 1.224 | -0.471 | - | 14.1 | - |
| 5 | **NEM** | Materials | 1.427 | 0.816 | 1.720 | 0.973 | 0.489 | - | 16.1 | +25.9% |
| 6 | **APA** | Energy | 1.304 | 1.246 | 1.260 | 0.794 | -0.344 | - | 9.4 | +26.7% |
| 7 | **DVA** | Health Care | 1.292 | 1.516 | 0.198 | 1.732 | -1.447 | - | 14.8 | +88.5% |
| 8 | **TPR** | Consumer Discretionary | 1.248 | 1.689 | 1.141 | 0.390 | -1.000 | - | 17.9 | +197.1% |
| 9 | **HST** | Real Estate | 1.190 | 1.376 | 0.486 | 1.270 | -0.194 | - | 15.5 | +15.6% |
| 10 | **SYF** | Financials | 1.122 | -0.256 | 1.187 | 1.766 | -0.438 | - | 7.9 | +20.8% |
| 11 | **MAS** | Industrials | 1.111 | -0.190 | 1.456 | 1.373 | -0.840 | - | 16.9 | +5862.5% |
| 12 | **SPG** | Real Estate | 1.100 | 0.853 | 1.374 | 0.498 | -1.410 | - | 15.5 | +120.5% |
| 13 | **MU** | Information Technology | 0.994 | 1.610 | 0.885 | 0.101 | -0.567 | - | 22.0 | +66.6% |
| 14 | **BMY** | Health Care | 0.985 | 0.635 | 0.864 | 0.980 | 0.614 | - | 14.4 | +46.6% |
| 15 | **TRV** | Financials | 0.921 | 1.109 | 0.328 | 1.003 | 0.720 | - | 9.8 | +26.5% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -1.987 | -1.632 | -0.917 | -2.561 | -1.115 |
| 502 | **CSGP** | Real Estate | -1.716 | -3.479 | -0.445 | -0.742 | 0.540 |
| 501 | **BA** | Industrials | -1.678 | -0.861 | -1.160 | -2.186 | -1.177 |
| 500 | **CEG** | Utilities | -1.652 | -2.444 | -0.613 | -1.318 | -0.799 |
| 499 | **KKR** | Financials | -1.589 | -1.574 | -0.849 | -1.671 | -0.965 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W34.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W34.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-08-17  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
