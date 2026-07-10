# Сателит — пълен data export за 2026-W28

_Период: 2026-07-06 → 2026-07-12_  
_Генериран: 2026-07-10 09:37 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W28.md` (structured briefing) и `narrative_2026-W28.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**8 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **DBA** | +3.63% | +2.51σ | 26.74 | 27.71 | 2026-07-02 | 2026-07-09 | -0.11% | +1.49% | 13 |
| **XLB** | -3.36% | -2.34σ | 52.01 | 50.26 | 2026-07-02 | 2026-07-09 | +0.25% | +1.54% | 13 |
| **XLP** | -2.11% | -1.80σ | 84.99 | 83.20 | 2026-07-02 | 2026-07-09 | +0.30% | +1.33% | 13 |
| **XLI** | -1.52% | -1.70σ | 183.91 | 181.11 | 2026-07-02 | 2026-07-09 | +0.91% | +1.43% | 13 |
| **DBC** | +3.80% | +1.61σ | 26.57 | 27.58 | 2026-07-02 | 2026-07-09 | -0.72% | +2.80% | 13 |
| **DIA** | -0.70% | -1.45σ | 527.88 | 524.19 | 2026-07-02 | 2026-07-09 | +0.99% | +1.17% | 13 |
| **DFEN** | -10.75% | -1.28σ | 85.78 | 76.56 | 2026-07-02 | 2026-07-09 | +2.62% | +10.44% | 13 |
| **LQD** | -0.86% | -1.18σ | 108.64 | 107.71 | 2026-07-02 | 2026-07-09 | -0.00% | +0.72% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-07-12 · **Conditions matched:** 2/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | +4.84% | ✅ | 103.98 | 109.01 | 2026-07-02 | 2026-07-09 |
| DFEN | down ≥ 3.0% | -10.75% | ✅ | 85.78 | 76.56 | 2026-07-02 | 2026-07-09 |
| GLD | down ≥ 1.0% | +0.01% | ❌ | 378.13 | 378.18 | 2026-07-02 | 2026-07-09 |
| URA | down ≥ 3.0% | -2.04% | ❌ | 43.23 | 42.35 | 2026-07-02 | 2026-07-09 |
| UUP | up ≥ 0.5% | +0.07% | ❌ | 28.34 | 28.36 | 2026-07-02 | 2026-07-09 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-07-12 · **Conditions matched:** 0/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | -0.11% | ❌ | 297.58 | 297.24 | 2026-07-02 | 2026-07-09 |
| XLF | up ≥ 1.0% | -0.14% | ❌ | 55.62 | 55.54 | 2026-07-02 | 2026-07-09 |
| XLY | up ≥ 1.0% | -0.23% | ❌ | 117.12 | 116.85 | 2026-07-02 | 2026-07-09 |
| GLD | down ≥ 0.5% | +0.01% | ❌ | 378.13 | 378.18 | 2026-07-02 | 2026-07-09 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2023-W12 (week ending 2023-03-26)
**Cosine similarity:** 0.9442 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.61% | +9.87% | +9.55% |
| **USO** | +10.93% | +2.40% | +32.27% |
| **GLD** | +1.14% | -2.97% | -2.74% |
| **TLT** | +0.36% | -2.55% | -13.04% |
| **XLE** | +8.69% | +0.19% | +16.53% |
| **IWM** | +0.74% | +5.40% | +3.13% |

### Паралел #2: 2023-W30 (week ending 2023-07-30)
**Cosine similarity:** 0.9228 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.70% | -9.80% | +7.48% |
| **USO** | +1.71% | +8.70% | +1.40% |
| **GLD** | -1.09% | +2.36% | +2.83% |
| **TLT** | -3.24% | -14.71% | -4.27% |
| **XLE** | +2.99% | -0.69% | -0.19% |
| **IWM** | -4.17% | -17.03% | +0.61% |

### Паралел #3: 2022-W12 (week ending 2022-03-27)
**Cosine similarity:** 0.9223 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -8.08% | -13.46% | -18.03% |
| **USO** | -5.30% | +0.66% | -19.10% |
| **GLD** | -2.77% | -6.74% | -16.10% |
| **TLT** | -4.71% | -12.07% | -16.94% |
| **XLE** | -6.31% | -8.07% | -8.51% |
| **IWM** | -8.92% | -14.83% | -18.61% |

### Паралел #4: 2021-W49 (week ending 2021-12-12)
**Cosine similarity:** 0.9135 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.14% | -10.45% | -16.65% |
| **USO** | +11.78% | +46.84% | +73.23% |
| **GLD** | +2.23% | +11.11% | +4.78% |
| **TLT** | -3.45% | -9.02% | -22.89% |
| **XLE** | +11.90% | +36.00% | +58.49% |
| **IWM** | -0.75% | -10.27% | -18.17% |

### Паралел #5: 2022-W40 (week ending 2022-10-09)
**Cosine similarity:** 0.8975 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.30% | +7.46% | +13.74% |
| **USO** | -0.84% | -13.68% | -6.44% |
| **GLD** | +0.99% | +10.03% | +18.12% |
| **TLT** | -6.39% | +4.91% | +9.07% |
| **XLE** | +13.79% | +8.14% | +6.05% |
| **IWM** | +6.49% | +5.81% | +3.99% |

### Паралел #6: 2025-W23 (week ending 2025-06-08)
**Cosine similarity:** 0.8825 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.84% | +8.35% | +15.10% |
| **USO** | +7.82% | +1.75% | +0.76% |
| **GLD** | -0.33% | +8.48% | +26.63% |
| **TLT** | +1.17% | +4.94% | +5.60% |
| **XLE** | +6.98% | +5.59% | +11.95% |
| **IWM** | +4.70% | +12.52% | +19.01% |

### Паралел #7: 2024-W40 (week ending 2024-10-06)
**Cosine similarity:** 0.8801 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.65% | +3.66% | -11.25% |
| **USO** | -2.12% | +2.06% | -11.04% |
| **GLD** | +3.43% | -0.62% | +14.17% |
| **TLT** | -2.61% | -7.66% | -0.76% |
| **XLE** | -3.23% | -5.34% | -14.10% |
| **IWM** | +2.32% | +2.71% | -16.89% |

### Паралел #8: 2024-W04 (week ending 2024-01-28)
**Cosine similarity:** 0.8704 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.00% | +4.60% | +12.41% |
| **USO** | +1.03% | +9.97% | +4.12% |
| **GLD** | +0.53% | +15.83% | +17.98% |
| **TLT** | -0.59% | -4.99% | +1.13% |
| **XLE** | +1.95% | +14.56% | +11.19% |
| **IWM** | +4.09% | +1.47% | +15.02% |

### Паралел #9: 2023-W13 (week ending 2023-04-02)
**Cosine similarity:** 0.8571 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.35% | +8.68% | +5.18% |
| **USO** | -5.10% | -4.35% | +21.70% |
| **GLD** | +2.35% | -2.70% | -6.42% |
| **TLT** | -0.13% | -2.48% | -15.26% |
| **XLE** | -2.80% | -1.14% | +10.90% |
| **IWM** | -3.76% | +5.26% | -0.19% |

### Паралел #10: 2023-W35 (week ending 2023-09-03)
**Cosine similarity:** 0.8456 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -6.23% | +2.11% | +14.53% |
| **USO** | +3.91% | -9.98% | -2.55% |
| **GLD** | -6.08% | +6.61% | +7.10% |
| **TLT** | -10.04% | -1.00% | +1.54% |
| **XLE** | -1.72% | -5.61% | -2.33% |
| **IWM** | -9.91% | -2.66% | +8.78% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 13 · **Total matching days:** 72 · **History:** 2021-05-17 → 2026-07-09

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 13 | +2.0% | +1.7% | -3.1% | +7.7% | 77% |
| **SPY** | 3m | 13 | +3.3% | +4.6% | -7.0% | +12.1% | 77% |
| **SPY** | 6m | 13 | +8.4% | +11.6% | -6.1% | +22.7% | 77% |
| **USO** | 1m | 13 | +1.0% | -0.8% | -7.2% | +12.7% | 46% |
| **USO** | 3m | 13 | -2.8% | -4.1% | -21.9% | +24.5% | 46% |
| **USO** | 6m | 13 | +9.8% | -4.4% | -21.9% | +109.4% | 46% |
| **GLD** | 1m | 13 | +2.5% | +0.9% | -2.2% | +8.9% | 77% |
| **GLD** | 3m | 13 | +5.7% | +5.9% | -12.6% | +24.5% | 69% |
| **GLD** | 6m | 13 | +6.0% | +10.3% | -15.0% | +25.3% | 69% |
| **TLT** | 1m | 13 | -1.1% | -0.8% | -6.5% | +3.7% | 31% |
| **TLT** | 3m | 13 | +0.4% | +0.6% | -16.2% | +12.6% | 62% |
| **TLT** | 6m | 13 | -2.6% | -2.1% | -17.2% | +9.1% | 38% |

**Episodes (последни 5 от 13):**
- `2024-06-21 → 2024-06-21` (1d)
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-28 → 2026-05-19` (13d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 1 · **Total matching days:** 49 · **History:** 2021-05-17 → 2026-07-09

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | +9.1% | +9.1% | +9.1% | +9.1% | 100% |
| **SPY** | 3m | 1 | +10.3% | +10.3% | +10.3% | +10.3% | 100% |
| **SPY** | 6m | 1 | +11.2% | +11.2% | +11.2% | +11.2% | 100% |
| **USO** | 1m | 1 | +7.2% | +7.2% | +7.2% | +7.2% | 100% |
| **USO** | 3m | 1 | -9.9% | -9.9% | -9.9% | -9.9% | 0% |
| **USO** | 6m | 1 | -12.5% | -12.5% | -12.5% | -12.5% | 0% |
| **GLD** | 1m | 1 | -0.2% | -0.2% | -0.2% | -0.2% | 0% |
| **GLD** | 3m | 1 | -13.8% | -13.8% | -13.8% | -13.8% | 0% |
| **GLD** | 6m | 1 | -13.0% | -13.0% | -13.0% | -13.0% | 0% |
| **TLT** | 1m | 1 | -0.6% | -0.6% | -0.6% | -0.6% | 0% |
| **TLT** | 3m | 1 | -2.6% | -2.6% | -2.6% | -2.6% | 0% |
| **TLT** | 6m | 1 | -2.4% | -2.4% | -2.4% | -2.4% | 0% |

**Episodes (последни 5 от 1):**
- `2026-04-08 → 2026-06-15` (49d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 7 · **Total matching days:** 781 · **History:** 2021-05-17 → 2026-07-09

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 7 | +1.7% | +1.7% | -4.1% | +5.4% | 71% |
| **SPY** | 3m | 7 | +3.4% | +3.7% | -3.8% | +7.2% | 86% |
| **SPY** | 6m | 7 | +5.9% | +7.7% | -11.3% | +14.0% | 86% |
| **USO** | 1m | 7 | +1.2% | +0.7% | -14.3% | +15.5% | 57% |
| **USO** | 3m | 7 | +2.9% | +2.1% | -12.1% | +17.0% | 57% |
| **USO** | 6m | 7 | +0.4% | +1.5% | -11.0% | +10.7% | 71% |
| **GLD** | 1m | 7 | +3.8% | +3.0% | -1.1% | +7.6% | 86% |
| **GLD** | 3m | 7 | +3.3% | +6.2% | -4.9% | +10.6% | 57% |
| **GLD** | 6m | 7 | +9.1% | +6.5% | +0.0% | +20.3% | 100% |
| **TLT** | 1m | 7 | -0.3% | +1.8% | -6.7% | +5.4% | 57% |
| **TLT** | 3m | 7 | -3.4% | -1.6% | -13.9% | +5.1% | 29% |
| **TLT** | 6m | 7 | -2.1% | -0.8% | -9.3% | +2.4% | 29% |

**Episodes (последни 5 от 7):**
- `2023-02-16 → 2023-03-09` (15d)
- `2023-05-19 → 2023-06-13` (8d)
- `2023-07-05 → 2024-08-12` (265d)
- `2024-08-30 → 2024-08-30` (1d)
- `2024-10-04 → 2026-07-09` (443d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-07-09

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 9 · **Total matching days:** 76 · **History:** 2021-05-17 → 2026-07-09

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 9 | +0.4% | +0.9% | -7.2% | +7.8% | 56% |
| **SPY** | 3m | 9 | +2.6% | +5.6% | -8.0% | +12.0% | 56% |
| **SPY** | 6m | 9 | +1.9% | +5.6% | -20.2% | +14.9% | 67% |
| **USO** | 1m | 9 | +2.0% | -1.7% | -15.0% | +52.9% | 33% |
| **USO** | 3m | 9 | +5.3% | -0.1% | -27.6% | +52.2% | 44% |
| **USO** | 6m | 9 | +3.7% | -0.2% | -27.6% | +45.8% | 44% |
| **GLD** | 1m | 9 | -2.2% | -1.6% | -8.3% | +1.9% | 11% |
| **GLD** | 3m | 9 | -2.4% | -2.8% | -12.0% | +6.4% | 44% |
| **GLD** | 6m | 9 | -1.9% | -4.7% | -19.2% | +25.0% | 33% |
| **TLT** | 1m | 9 | -1.7% | -2.2% | -5.7% | +2.6% | 22% |
| **TLT** | 3m | 9 | -5.8% | -4.9% | -16.9% | +5.4% | 22% |
| **TLT** | 6m | 9 | -8.8% | -6.1% | -21.7% | +3.4% | 11% |

**Episodes (последни 5 от 9):**
- `2023-04-12 → 2023-04-18` (5d)
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-04-09` (27d)
- `2026-04-29 → 2026-05-19` (7d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 16 · **Total matching days:** 275 · **History:** 2021-05-17 → 2026-07-09

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.2% | +2.2% | -4.8% | +9.0% | 75% |
| **SPY** | 3m | 16 | +3.7% | +5.2% | -12.3% | +16.7% | 75% |
| **SPY** | 6m | 16 | +7.4% | +8.3% | -13.5% | +21.9% | 81% |
| **USO** | 1m | 16 | +1.8% | -3.2% | -13.0% | +27.7% | 38% |
| **USO** | 3m | 16 | +1.4% | -2.6% | -14.5% | +29.9% | 31% |
| **USO** | 6m | 16 | +11.1% | +1.8% | -12.4% | +87.1% | 62% |
| **GLD** | 1m | 16 | +2.4% | +1.8% | -6.4% | +9.0% | 75% |
| **GLD** | 3m | 16 | +6.4% | +7.4% | -15.2% | +23.6% | 69% |
| **GLD** | 6m | 16 | +11.0% | +12.1% | -15.2% | +43.8% | 75% |
| **TLT** | 1m | 16 | +0.6% | +0.7% | -6.1% | +8.5% | 56% |
| **TLT** | 3m | 16 | -0.7% | -0.3% | -14.7% | +13.0% | 50% |
| **TLT** | 6m | 16 | -2.8% | -1.6% | -20.6% | +8.6% | 44% |

**Episodes (последни 5 от 16):**
- `2025-03-27 → 2025-05-08` (25d)
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-17 → 2026-04-23` (4d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 19 · **Total matching days:** 301 · **History:** 2021-05-17 → 2026-07-09

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 19 | +0.4% | +1.0% | -8.3% | +7.0% | 53% |
| **SPY** | 3m | 19 | +2.3% | +3.1% | -13.3% | +9.4% | 68% |
| **SPY** | 6m | 19 | +3.8% | +7.4% | -15.7% | +17.6% | 74% |
| **USO** | 1m | 19 | -0.6% | -5.6% | -21.8% | +55.8% | 42% |
| **USO** | 3m | 19 | +2.6% | -1.3% | -18.0% | +64.3% | 42% |
| **USO** | 6m | 19 | +6.3% | -5.2% | -18.0% | +75.1% | 47% |
| **GLD** | 1m | 19 | -0.6% | -0.1% | -12.4% | +7.6% | 47% |
| **GLD** | 3m | 19 | +1.5% | +1.3% | -13.7% | +19.0% | 63% |
| **GLD** | 6m | 19 | +7.3% | +6.0% | -20.1% | +55.5% | 68% |
| **TLT** | 1m | 19 | +0.1% | +0.3% | -5.5% | +5.5% | 58% |
| **TLT** | 3m | 19 | -2.7% | -3.8% | -16.8% | +9.8% | 37% |
| **TLT** | 6m | 19 | -5.2% | -5.0% | -20.5% | +6.7% | 26% |

**Episodes (последни 5 от 19):**
- `2025-05-12 → 2025-05-19` (3d)
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (12d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-07-09

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (13 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 7 | 2.76 | 2.89 | 2026-06-06 00:00:00 | 2026-07-04 00:00:00 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | 7 | 2.37 | 2.58 | 2026-06-06 00:00:00 | 2026-07-04 00:00:00 | - |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 7 | 2.34 | 2.34 | 2026-06-06 00:00:00 | 2026-07-04 00:00:00 | ✓ |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 7 | 2.33 | 2.43 | 2026-06-06 00:00:00 | 2026-07-04 00:00:00 | - |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 7 | 2.30 | 2.39 | 2026-06-06 00:00:00 | 2026-07-04 00:00:00 | ✓ |
| **JTSQUR** | Quits rate — напускания | labor | flow | 7 | 2.02 | 2.02 | 2026-06-06 00:00:00 | 2026-07-04 00:00:00 | ✓ |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 5 | 2.72 | 2.76 | 2026-06-06 00:00:00 | 2026-07-04 00:00:00 | ✓ |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | 5 | 2.40 | 2.40 | 2026-06-06 00:00:00 | 2026-06-20 00:00:00 | - |
| **CSUSHPISA** | Case-Shiller US National HPI (SA) | housing | housing_prices | 5 | 2.24 | 2.26 | 2026-06-06 00:00:00 | 2026-07-04 00:00:00 | - |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | 3 | 2.30 | 2.30 | 2026-06-06 00:00:00 | 2026-06-08 00:00:00 | - |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | 1 | 2.47 | 2.47 | 2026-07-04 00:00:00 | 2026-07-04 00:00:00 | ✓ |
| **MSACSR** | Месеци предлагане — нови жилища | housing | housing_affordability | 1 | 2.02 | 2.02 | 2026-06-27 00:00:00 | 2026-06-27 00:00:00 | ✓ |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | 1 | 2.02 | 2.02 | 2026-07-04 00:00:00 | 2026-07-04 00:00:00 | - |

### EU (5 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 7 | 5.36 | 5.37 | 2026-06-06 00:00:00 | 2026-07-04 00:00:00 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation | sentiment | 7 | 2.86 | 2.98 | 2026-06-06 00:00:00 | 2026-07-04 00:00:00 | - |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | 7 | 2.37 | 2.66 | 2026-06-06 00:00:00 | 2026-07-04 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 7 | 2.27 | 2.31 | 2026-06-06 00:00:00 | 2026-07-04 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 7 | 2.26 | 2.27 | 2026-06-06 00:00:00 | 2026-07-04 00:00:00 | ✓ |

### CN (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 5 | 2.56 | 2.56 | 2026-06-15 00:00:00 | 2026-07-08 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 5 | 2.23 | 2.23 | 2026-06-15 00:00:00 | 2026-07-08 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 3 | 2.23 | 2.24 | 2026-06-15 00:00:00 | 2026-07-08 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-07-04 00:00:00 · **Generated:** 2026-07-04 09:25:45.525311+00:00

**Режим:** `stagflation_confirmed` (Стагфлация (потвърдена))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 35.5 | contracting | 29.6% | 4 | 3 |
| **growth** | 41.6 | mixed | 28.0% | 1 | 1 |
| **inflation** | 36.3 | contracting | 27.8% | 4 | 1 |
| **liquidity** | 51.1 | mixed | 42.1% | 0 | 0 |

### Top anomalies (10 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | +2.89 | up | 6.42 | 2026-05-01 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | +2.58 | up | 5.29 | 2026-05-01 | - |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | -2.56 | down | 2.00 | 2026-04-01 | - |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | -2.47 | down | 61.50 | 2026-06-01 | ✓ min |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | +2.43 | up | 4.80 | 2026-05-01 | - |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.34 | down | 94.99 | 2026-01-01 | ✓ min |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | +2.28 | up | 55.10 | 2026-05-01 | ✓ max |
| **CSUSHPISA** | Case-Shiller US National HPI (SA) | housing | housing_prices | -2.17 | down | 0.84 | 2026-04-01 | - |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | -2.02 | down | 59.00 | 2026-06-01 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | -2.02 | down | 1.90 | 2026-05-01 | ✓ min |

### Narrative hints от макро лещите
- **PPIFIS**: Производствени цени → consumer prices с 1-3 месечен lag. Водещ за CPI при трендови промени.
- **CPI_GOODS**: Goods inflation реагира бързо на supply shocks. 2022 peak след доставъчните кризи. Сега често е в deflation/близо до 0.
- **HPIPONM226S**: Monthly FHFA версия. Само purchase transactions (без refi appraisals). По-чист от refi-bias.
- **CIVPART**: Структурни сдвигове (демография, ранно пенсиониране). Пост-COVID не се възстанови напълно.
- **MICH_INFL_1Y**: Household очаквания. По-шумни от market-based, но по-ранни. Extreme movements сигнализират de-anchoring risk.
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **US_PMI_MFG**: Markit mfg — comparable cross-country. ISM е US-only.
- **CSUSHPISA**: Главен ценови benchmark. Repeat-sales методология; ~2 месеца lag. National композит на 9 census divisions.
- **EMRATIO**: Не зависи от definition на 'active labor force'. По-стабилен индикатор на дълбоката заетост.
- **JTSQUR**: Работническа увереност. Ако quits rate пада — хората задържат работата си (pre-recession pattern).

### Cross-lens divergences (6 entries)
- 🔔 **?**
  - `pair_id`: stagflation_test
  - `name_bg`: Labor tightness × Inflation pressure
  - `question_bg`: Дали labor tightness потвърждава inflation pressure (стагфлация)?
  - `state`: both_up
  - `interpretation`: Стагфлация confirmation — labor tight + inflation hot.
  - `slot_a_label`: Labor tightness
  - `slot_b_label`: Inflation pressure
  - `breadth_a`: 0.75
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 1.0
- 🔔 **?**
  - `pair_id`: growth_labor_lead_lag
  - `name_bg`: Hard activity × Labor claims
  - `question_bg`: Дали hard activity и labor market следват едно тенденция?
  - `state`: both_up
  - `interpretation`: Aligned expansion — activity растяща, claims низки. Healthy.
  - `slot_a_label`: Hard activity
  - `slot_b_label`: Labor market (claims inverted)
  - `breadth_a`: 0.8
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.8
  - `breadth_b_raw`: 0.667
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Realized CPI × Expectations
  - `question_bg`: Дали expectations следват realized inflation, или стоят anchored?
  - `state`: both_up
  - `interpretation`: De-anchoring in progress — expectations следват realized up.
  - `slot_a_label`: Realized inflation
  - `slot_b_label`: Inflation expectations
  - `breadth_a`: 0.667
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.667
- 🔔 **?**
  - `pair_id`: credit_policy_transmission
  - `name_bg`: Credit spreads × Policy rates
  - `question_bg`: Дали credit следва policy направление — transmission intact?
  - `state`: transition
  - `interpretation`: Mixed transmission.
  - `slot_a_label`: Credit stress
  - `slot_b_label`: Policy tightening
  - `breadth_a`: 0.5
  - `breadth_b`: 0.667
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 0.667
- 🔔 **?**
  - `pair_id`: sentiment_vs_hard_data
  - `name_bg`: Consumer sentiment × Hard activity
  - `question_bg`: Дали sentiment потвърждава hard data, или има разминаване?
  - `state`: a_down_b_up
  - `interpretation`: Activity OK, sentiment крачка — strategic pessimism / political bias.
  - `slot_a_label`: Consumer sentiment
  - `slot_b_label`: Hard activity
  - `breadth_a`: 0.0
  - `breadth_b`: 0.8
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
  - `breadth_a`: 0.333
  - `breadth_b`: 0.667
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.333
  - `breadth_b_raw`: 0.667

### Executive narrative
> Картината показва стагфлационна конфигурация — трудовият пазар остава tight, а инфлационният натиск е broad-based. Най-отклонена леща: Инфлация и цени — breadth 71% (разширяване), 4 аномалии, 1 нови екстремума. Expectations също нагоре — de-anchoring в ход, рискът ескалира. За наблюдение следващия релиз: CIVPART (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: PPIFIS z=+2.89
- 5 нови екстремуми в top-11 (lookback 5г.)
- Активни двойки: Stagflation test=both_up; Growth × Labor=both_up; Inflation anchoring=both_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-07-04 00:00:00 · **Generated:** 2026-07-04 09:36:20.127917+00:00

**Режим:** `disinflation_cooling` (Дезинфлация и охлаждане (индикирани))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 34.7 | contracting | 42.9% | 1 | 0 |
| **growth** | 37.8 | mixed | 16.7% | 1 | 0 |
| **inflation** | 50.7 | mixed | 85.7% | 1 | 0 |
| **credit** | 44.7 | mixed | 36.8% | 3 | 2 |
| **external** | 20.2 | contracting | 16.7% | 0 | 0 |

### Top anomalies (5 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | +5.27 | up | 2.72 | 2026-06-01 | - |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | -2.66 | down | -3.80 | 2026-06-01 | - |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | +2.27 | up | 3.04 | 2026-05-01 | ✓ max |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | +2.25 | up | 3.74 | 2026-05-01 | ✓ max |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation, growth | sentiment | +2.17 | up | 22.30 | 2026-06-01 | - |

### Narrative hints от макро лещите
- **EA_BUND_2Y**: EA-aggregate 2Y yield. Curve slope (10Y-2Y) проксира policy expectations и recession risk.
- **EA_EMP_EXP_SERVICES**: DG ECFIN survey: forward-looking labor сигнал от услугите (~70% от GDP). Дълга история (от 1996) — за разлика от teibs030 (EA_EMPLOYMENT_EXP, 12m). Същата полярност (higher=better). De-singleton-ва labor_sentiment.
- **DE_10Y**: Germany 10Y, Maastricht-criterion measure. Reference за BTP-Bund / OAT-Bund spread изчисления.
- **FR_10Y**: France sovereign yield — компонент на OAT-Bund spread. Core-but-not-DE EA stress indicator.
- **EA_SELLING_PRICE_EXP**: Forward-looking inflation сигнал от business side — мениджърите казват дали ще вдигат цени. Изпреварва HICP с 3-6 месеца.

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
  - `breadth_b`: 0.0
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 0.0
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
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 0.778
  - `breadth_b_raw`: 0.25
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
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.25
  - `breadth_b_raw`: 1.0

### Executive narrative
> Синхронно охлаждане — labor и инфлация отстъпват заедно. Рискът се мести към overshooting, ако claims ускорят. Най-отклонена леща: Инфлация и цени — breadth 0% (свиване), 1 аномалии, 0 нови екстремума. За наблюдение следващия релиз: DE_10Y, FR_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.27
- 2 нови екстремуми в top-5 (lookback 5г.)
- Активни двойки: Stagflation test=both_down



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-07-08 00:00:00 · **Generated:** 2026-07-07 22:03:25.916202+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 44.5 | mixed | -% | - | - |
| **inflation** | 48.0 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 52.3 | mixed | -% | - | - |
| **property** | 23.2 | contracting | -% | - | - |

### Top anomalies (3 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | -2.56 | down | 3.00 | 2026-06-22 | ✓ min |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | +2.23 | up | 15.79 | 2025-12-31 | ✓ max |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | -2.22 | down | 1.72 | 2026-06-30 | - |

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
  - `breadth_b`: 0.25
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
> Претеглен композитен macro score 40.1/100 → режим „ВЛОШАВАЩ СЕ“ (5/5 лещи). 5 лещи, 3 flagged аномалии (4 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM_STATE (current)
| Field | Value |
|---|---|
| `date` | 2026-05-31 00:00:00 |
| `regime` | REFLATION |
| `ks_status` | inactive |
| `alignment_score` | 6.0 |
| `alignment_total` | 8 |
| `gms_value` | 0.0 |
| `last_updated_md` | 2026-05-31 00:00:00 |
| `is_change_day` | True |

### VRM_WEEK (current)
| Field | Value |
|---|---|
| `date` | 2026-06-08 00:00:00 |
| `week_start` | 2026-06-08 00:00:00 |
| `week_end` | 2026-06-12 00:00:00 |
| `approved` | True |
| `regime` | REFLATION |
| `regime_bg` | РЕФЛАЦИЯ |
| `signal` | ЗАДРЪЖ (REFLATION 100%, 4-ти месец, Regime_Duration 4.0) |
| `alignment` | 6.0 |
| `alignment_max` | 8 |
| `alignment_label` | ЧИСТ (макро) / оспорено пазарно поведение |
| `gms_score` | 5.0 |
| `gms_max` | 8 |
| `gms_label` | MEDIUM |
| `ks_active` | False |
| `spy_4w` | +0.40% |
| `qqq_4w` | +1.91% |
| `xle_4w` | -3.06% |
| `gld_4w` | -7.49% |
| `tlt_4w` | +2.51% |
| `tip_4w` | -0.89% |
| `iwm_4w` | +5.56% |



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-07-02 → 2026-07-08)

**stable_winner (1m):** +6 entered, -13 exited
  - **Entered:** CAH, EXPE, INCY, MRK, STX, WDC _(включително 1 за първи път в историята: CAH)_
  - **Exited:** ADM, AES, CIEN, CVS, HWM, IBKR, IVZ, MPC, NEM, RTX, VLO, VRT, VTRS

**stable_winner (3m):** +5 entered, -5 exited
  - **Entered:** BEN, CBOE, INCY, JNJ, VTR
  - **Exited:** APA, BIIB, IBKR, PLD, VRT

**quality_dip (1m):** +13 entered, -7 exited
  - **Entered:** ADM, AES, CIEN, CVS, HWM, IBKR, IVZ, MPC, NEM, USB, VLO, VRT, VTRS _(включително 1 за първи път в историята: USB)_
  - **Exited:** CAH, COR, EXPE, INCY, MRK, STX, WDC

**quality_dip (3m):** +6 entered, -7 exited
  - **Entered:** APA, BIIB, IBKR, PLD, USB, VRT _(включително 4 за първи път в историята: APA, BIIB, PLD, USB)_
  - **Exited:** BEN, CBOE, COR, INCY, JNJ, RTX, VTR

**faded_bounce (1m):** +11 entered, -7 exited
  - **Entered:** ABT, BR, CMS, EFX, EOG, MAA, POOL, TPL, TSCO, UNH, ZTS _(включително 3 за първи път в историята: ABT, CMS, MAA)_
  - **Exited:** AVB, BF-B, HUM, IFF, KHC, SW, TAP

**faded_bounce (3m):** +4 entered, -11 exited
  - **Entered:** CAG, CMS, MAA, SO _(включително 2 за първи път в историята: CMS, MAA)_
  - **Exited:** AMCR, BLDR, BR, BX, CHTR, CLX, GDDY, HUM, IFF, SW, TTD

### EU (period: 2026-07-03 → 2026-07-08)

**stable_winner (1m):** +13 entered, -12 exited
  - **Entered:** ACS.MC, AED.BR, BATS.L, BPE.MI, CABK.MC, DLG.MI, ELI.BR, NDA.DE, SAND.ST, URW.PA, VOE.VI, VWS.CO, WRT1V.HE
  - **Exited:** A5G.IR, AAF.L, ABN.AS, ALLN.SW, BBY.L, BIRG.IR, HOC.L, HUBN.SW, NXT.L, PRY.MI, RR.L, ZEG.L

**stable_winner (3m):** +7 entered, -6 exited
  - **Entered:** AED.BR, BBVA.MC, BBY.L, ENGI.PA, JYSK.CO, SPSN.SW, VATN.SW _(включително 2 за първи път в историята: AED.BR, VATN.SW)_
  - **Exited:** A5G.IR, ANA.MC, NESTE.HE, SAND.ST, STAN.L, ZEG.L

**quality_dip (1m):** +14 entered, -13 exited
  - **Entered:** A5G.IR, AAF.L, ABN.AS, ALLN.SW, BBY.L, BIRG.IR, EDPR.LS, HOC.L, HSBA.L, HUBN.SW, NXT.L, PRY.MI, RR.L, ZEG.L _(включително 3 за първи път в историята: EDPR.LS, HSBA.L, PRY.MI)_
  - **Exited:** ACS.MC, AED.BR, BATS.L, BPE.MI, CABK.MC, DLG.MI, ELI.BR, NDA.DE, SAND.ST, URW.PA, VOE.VI, VWS.CO, WRT1V.HE

**quality_dip (3m):** +8 entered, -7 exited
  - **Entered:** A5G.IR, ANA.MC, EDPR.LS, HSBA.L, NESTE.HE, SAND.ST, STAN.L, ZEG.L _(включително 2 за първи път в историята: EDPR.LS, HSBA.L)_
  - **Exited:** AED.BR, BBVA.MC, BBY.L, ENGI.PA, JYSK.CO, SPSN.SW, VATN.SW

**faded_bounce (1m):** +7 entered, -10 exited
  - **Entered:** AUTO.L, BNZL.L, CAP.PA, NTGY.MC, RMV.L, SGE.L, UMG.AS _(включително 2 за първи път в историята: CAP.PA, NTGY.MC)_
  - **Exited:** AMS.MC, BAKKA.OL, DGE.L, DLN.L, DSFIR.AS, GIVN.SW, III.L, SWEC-B.ST, TEP.PA, VPK.AS

**faded_bounce (3m):** +12 entered, -7 exited
  - **Entered:** AUTO.L, BOL.PA, CS.PA, EVD.DE, NTGY.MC, RACE.MI, RAND.AS, RED.MC, RMV.L, SAGA-B.ST, SOP.PA, UMG.AS _(включително 6 за първи път в историята: CS.PA, EVD.DE, NTGY.MC, RED.MC, RMV.L, SOP.PA)_
  - **Exited:** AMS.MC, DLN.L, EVO.ST, NEXI.MI, SGE.L, SY1.DE, TCAP.L



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-06-23 00:00:00)
| Market | Asset class | Net position | Net % | Percentile 5y | Weekly change |
|---|---|---:|---:|---:|---:|
| **soyoil** | Commodities | 103589 | 96.2 | 96.2 | -37829 |
| **copper** | Commodities | 68818 | 92.3 | 92.3 | -3156 |
| **cattle** | Commodities | 126025 | 91.7 | 91.7 | 5456 |
| **rbob** | Commodities | 71366 | 82.9 | 82.9 | 4083 |
| **aud** | FX | 39111 | 74.0 | 74.0 | -21123 |
| **vix** | Volatility | -18863 | 68.9 | 68.9 | 30473 |
| **cotton** | Commodities | 38445 | 59.5 | 59.5 | -15755 |
| **brent** | Commodities | 8110 | 58.5 | 58.5 | -3807 |
| **coffee** | Commodities | 14002 | 51.8 | 51.8 | -3432 |
| **gold** | Commodities | 113010 | 47.9 | 47.9 | 16079 |
| **eurfx** | FX | -15410 | 46.5 | 46.5 | -22706 |
| **gbpfx** | FX | 7567 | 45.8 | 45.8 | -21262 |
| **platinum** | Commodities | 8518 | 41.9 | 41.9 | -4416 |
| **dxy** | FX | -5352 | 39.4 | 39.4 | 7178 |
| **russell** | US Equities | -56428 | 38.0 | 38.0 | 11784 |
| **soybeans** | Commodities | 36679 | 37.9 | 37.9 | -152873 |
| **bitcoin** | Crypto | -6130 | 36.4 | 36.4 | 2504 |
| **heatingoil** | Commodities | 6254 | 35.8 | 35.8 | -1476 |
| **silver** | Commodities | 11659 | 29.8 | 29.8 | 1415 |
| **soymeal** | Commodities | 8601 | 29.1 | 29.1 | -114378 |
| **sp500** | US Equities | -373468 | 27.8 | 27.8 | 84312 |
| **corn** | Commodities | -69691 | 25.4 | 25.4 | -275195 |
| **natgas** | Commodities | -82812 | 24.9 | 24.9 | 51292 |
| **wti** | Commodities | 100295 | 20.2 | 20.2 | -15467 |
| **wheat** | Commodities | -71206 | 19.2 | 19.2 | -52500 |
| **usultra10y** | Rates | -248756 | 17.2 | 17.2 | -9030 |
| **chf** | FX | -13816 | 15.1 | 15.1 | -8993 |
| **us30y** | Rates | -350946 | 14.2 | 14.2 | -30200 |
| **palladium** | Commodities | -4712 | 12.1 | 12.1 | -939 |
| **us5y** | Rates | -2165573 | 10.9 | 10.9 | -94220 |
| **us2y** | Rates | -1787552 | 10.2 | 10.2 | -14995 |
| **nasdaq** | US Equities | -51062 | 8.5 | 8.5 | 617 |
| **cocoa** | Commodities | -22958 | 6.8 | 6.8 | -4810 |
| **us10y** | Rates | -1938747 | 5.9 | 5.9 | 67233 |
| **jpy** | FX | -97092 | 5.0 | 5.0 | -26584 |
| **sugar** | Commodities | -185483 | 2.4 | 2.4 | -93160 |
| **cad** | FX | -83377 | 1.6 | 1.6 | -45282 |
| **hogs** | Commodities | -25560 | 0.2 | 0.2 | -38545 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **SNDK** | Technology | 99.6 | 10.8% | 143.0% | 530.2% | 3348.3% | 3.43 | -31.3% |
| 2 | **MU** | Technology | 99.3 | 9.8% | 151.3% | 204.1% | 621.5% | 2.71 | -30.3% |
| 3 | **INTC** | Technology | 98.7 | 11.2% | 108.3% | 180.0% | 350.8% | 2.09 | -24.2% |
| 4 | **WDC** | Technology | 98.7 | 7.5% | 76.5% | 193.1% | 686.7% | 2.90 | -28.7% |
| 5 | **AMD** | Technology | 98.5 | 10.9% | 133.6% | 134.0% | 246.0% | 1.93 | -27.8% |
| 6 | **DELL** | Technology | 98.5 | 9.5% | 143.9% | 250.9% | 220.9% | 1.90 | -32.3% |
| 7 | **STX** | Technology | 98.5 | 1.6% | 83.6% | 197.5% | 475.4% | 2.55 | -25.0% |
| 8 | **MRVL** | Technology | 98.0 | -12.1% | 112.0% | 157.1% | 269.2% | 1.55 | -27.1% |
| 9 | **AMAT** | Technology | 97.6 | 25.9% | 61.2% | 101.2% | 139.2% | 1.91 | -23.3% |
| 10 | **LRCX** | Technology | 97.0 | 9.9% | 48.6% | 71.4% | 210.5% | 2.03 | -24.7% |
| 11 | **FLEX** | Technology | 96.6 | -12.2% | 95.5% | 116.0% | 195.2% | 1.49 | -18.9% |
| 12 | **HPE** | Technology | 96.6 | -8.9% | 81.9% | 86.9% | 139.5% | 1.52 | -26.4% |
| 13 | **KLAC** | Technology | 94.7 | 14.7% | 43.0% | 64.0% | 112.8% | 1.48 | -28.2% |
| 14 | **CAT** | Industrials | 94.2 | 4.8% | 31.1% | 54.5% | 133.5% | 2.28 | -13.9% |
| 15 | **GLW** | Technology | 94.0 | 3.6% | 24.1% | 108.2% | 242.7% | 1.91 | -28.0% |
| 16 | **COHR** | Technology | 92.9 | -15.9% | 24.3% | 70.1% | 328.1% | 1.61 | -26.5% |
| 17 | **CNC** | Healthcare | 92.4 | 7.6% | 84.8% | 50.2% | 88.6% | 1.30 | -55.5% |
| 18 | **CSCO** | Technology | 92.3 | -6.1% | 41.6% | 52.0% | 79.5% | 1.50 | -13.7% |
| 19 | **ON** | Technology | 92.2 | -20.0% | 47.0% | 59.8% | 114.7% | 0.78 | -33.9% |
| 20 | **VRT** | Industrials | 91.9 | 5.8% | 21.2% | 82.8% | 138.2% | 1.45 | -25.3% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **ATS.VI** | Technology | 97.6 | 24.5% | 171.3% | 395.1% | 634.4% | 2.84 | -27.7% |
| 2 | **TPRO.MI** | Technology | 97.1 | 1.8% | 87.7% | 124.6% | 322.2% | 2.33 | -27.0% |
| 3 | **STMMI.MI** | Technology | 95.6 | -10.6% | 81.3% | 137.5% | 142.4% | 1.43 | -33.5% |
| 4 | **NOKIA.HE** | Technology | 95.4 | -20.4% | 42.4% | 90.5% | 205.5% | 1.70 | -29.0% |
| 5 | **IFX.DE** | Technology | 94.3 | -9.5% | 65.5% | 69.4% | 108.5% | 1.29 | -21.2% |
| 6 | **SOI.PA** | Technology | 94.3 | -37.3% | 81.0% | 274.7% | 222.8% | 0.70 | -54.0% |
| 7 | **RBI.VI** | Financial Services | 93.0 | 17.2% | 46.0% | 57.5% | 94.4% | 2.06 | -18.0% |
| 8 | **GL9.IR** | Consumer Defensive | 92.8 | 16.1% | 44.4% | 72.0% | 74.0% | 2.45 | -8.0% |
| 9 | **ASML.AS** | Technology | 91.2 | -0.3% | 24.8% | 44.0% | 121.3% | 1.79 | -15.8% |
| 10 | **VACN.SW** | Industrials | 90.6 | 7.1% | 36.4% | 54.3% | 84.8% | 1.49 | -25.1% |
| 11 | **AIXA.DE** | Technology | 90.5 | -22.2% | 17.1% | 112.4% | 250.6% | 1.50 | -28.4% |
| 12 | **CCC.L** | Technology | 89.9 | -2.9% | 38.7% | 39.4% | 89.5% | 1.84 | -16.2% |
| 13 | **SUBC.OL** | Energy | 89.4 | 2.6% | 21.0% | 70.6% | 81.7% | 1.99 | -11.3% |
| 14 | **DHER.DE** | Consumer Cyclical | 88.9 | -5.4% | 117.3% | 57.8% | 62.0% | 0.65 | -48.7% |
| 15 | **PRY.MI** | Industrials | 88.8 | -10.0% | 17.2% | 47.5% | 152.3% | 2.05 | -14.7% |
| 16 | **TIT.MI** | Communication Services | 88.8 | 6.7% | 25.6% | 46.6% | 80.2% | 2.19 | -13.0% |
| 17 | **IFCN.SW** | Technology | 88.8 | 0.0% | 56.3% | 58.1% | 57.2% | 1.06 | -25.5% |
| 18 | **ABBN.SW** | Industrials | 88.7 | 0.8% | 26.6% | 38.1% | 78.3% | 2.05 | -12.1% |
| 19 | **AKER.OL** | Industrials | 88.4 | -3.2% | 16.0% | 58.7% | 96.1% | 2.13 | -15.6% |
| 20 | **BESI.AS** | Technology | 87.7 | -13.9% | 17.6% | 53.3% | 121.9% | 1.18 | -24.5% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **EIX** | Utilities | 2.130 | 1.853 | 0.902 | 2.784 | -0.572 | - | 8.1 | +18.9% |
| 2 | **NEM** | Materials | 1.839 | 1.422 | 1.799 | 1.452 | 0.590 | - | 12.3 | +25.8% |
| 3 | **MO** | Consumer Staples | 1.632 | 1.219 | 1.938 | 0.958 | -0.339 | - | 14.9 | - |
| 4 | **HST** | Real Estate | 1.337 | 1.766 | 0.436 | 1.333 | 0.063 | - | 15.8 | +14.9% |
| 5 | **APA** | Energy | 1.335 | 1.385 | 1.142 | 0.910 | -0.384 | - | 7.8 | +26.2% |
| 6 | **SYF** | Financials | 1.240 | 0.112 | 1.198 | 1.786 | -0.633 | - | 7.4 | +21.8% |
| 7 | **CF** | Materials | 1.234 | 0.394 | 0.995 | 1.732 | 0.545 | - | 10.3 | +27.3% |
| 8 | **SPG** | Real Estate | 1.119 | 1.043 | 1.339 | 0.458 | -1.297 | - | 15.3 | +113.6% |
| 9 | **BMY** | Health Care | 1.040 | 0.748 | 0.914 | 0.993 | 0.382 | - | 16.2 | +38.7% |
| 10 | **TPR** | Consumer Discretionary | 0.952 | 1.638 | 1.109 | -0.274 | -0.810 | - | 42.7 | +60.9% |
| 11 | **MRK** | Health Care | 0.903 | 1.377 | 0.852 | 0.123 | 0.450 | - | 35.2 | +18.9% |
| 12 | **VRSN** | Information Technology | 0.900 | -0.363 | 2.200 | 0.256 | 1.708 | - | 29.9 | - |
| 13 | **MAS** | Industrials | 0.878 | -0.126 | 1.258 | 1.011 | -1.675 | - | 19.0 | +8457.1% |
| 14 | **MU** | Information Technology | 0.865 | 1.427 | 0.806 | 0.029 | -0.670 | - | 22.4 | +66.6% |
| 15 | **DVA** | Health Care | 0.862 | 0.944 | 0.190 | 1.144 | -1.480 | - | 22.1 | +81.0% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -2.141 | -1.794 | -1.181 | -2.538 | -1.317 |
| 502 | **COIN** | Financials | -1.963 | -2.303 | -1.251 | -1.532 | -1.705 |
| 501 | **CSGP** | Real Estate | -1.812 | -3.162 | -0.726 | -0.921 | 0.441 |
| 500 | **KKR** | Financials | -1.605 | -1.247 | -1.343 | -1.491 | -0.910 |
| 499 | **NRG** | Utilities | -1.534 | -2.170 | -0.552 | -1.316 | -2.249 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W28.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W28.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-07-06  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
