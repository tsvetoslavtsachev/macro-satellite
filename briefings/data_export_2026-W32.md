# Сателит — пълен data export за 2026-W32

_Период: 2026-08-03 → 2026-08-09_  
_Генериран: 2026-08-07 07:17 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W32.md` (structured briefing) и `narrative_2026-W32.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**13 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **GLD** | +4.88% | +2.71σ | 371.54 | 389.67 | 2026-07-31 | 2026-08-06 | -0.97% | +2.16% | 13 |
| **URA** | +10.57% | +2.52σ | 39.07 | 43.20 | 2026-07-31 | 2026-08-06 | -2.57% | +5.20% | 13 |
| **DIA** | +2.65% | +2.49σ | 524.32 | 538.19 | 2026-07-31 | 2026-08-06 | +0.45% | +0.88% | 13 |
| **GDX** | +13.25% | +2.49σ | 74.10 | 83.92 | 2026-07-31 | 2026-08-06 | -1.07% | +5.76% | 13 |
| **XLB** | +3.45% | +2.33σ | 50.43 | 52.17 | 2026-07-31 | 2026-08-06 | -0.13% | +1.54% | 13 |
| **XLI** | +2.74% | +1.94σ | 179.84 | 184.76 | 2026-07-31 | 2026-08-06 | +0.31% | +1.25% | 13 |
| **SLV** | +6.67% | +1.76σ | 52.36 | 55.85 | 2026-07-31 | 2026-08-06 | -1.90% | +4.88% | 13 |
| **SPY** | +2.88% | +1.69σ | 747.03 | 768.56 | 2026-07-31 | 2026-08-06 | +0.29% | +1.53% | 13 |
| **XLC** | +2.72% | +1.59σ | 108.24 | 111.18 | 2026-07-31 | 2026-08-06 | -0.56% | +2.06% | 13 |
| **QQQ** | +3.88% | +1.22σ | 687.99 | 714.65 | 2026-07-31 | 2026-08-06 | +0.20% | +3.01% | 13 |
| **XLK** | +5.69% | +1.20σ | 175.35 | 185.33 | 2026-07-31 | 2026-08-06 | +0.70% | +4.15% | 13 |
| **DFEN** | +13.03% | +1.13σ | 75.39 | 85.21 | 2026-07-31 | 2026-08-06 | +2.30% | +9.49% | 13 |
| **IWM** | +2.42% | +1.08σ | 291.20 | 298.25 | 2026-07-31 | 2026-08-06 | +0.34% | +1.92% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-08-09 · **Conditions matched:** 0/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | -7.97% | ❌ | 129.17 | 118.87 | 2026-07-31 | 2026-08-06 |
| DFEN | down ≥ 3.0% | +13.03% | ❌ | 75.39 | 85.21 | 2026-07-31 | 2026-08-06 |
| GLD | down ≥ 1.0% | +4.88% | ❌ | 371.54 | 389.67 | 2026-07-31 | 2026-08-06 |
| URA | down ≥ 3.0% | +10.57% | ❌ | 39.07 | 43.20 | 2026-07-31 | 2026-08-06 |
| UUP | up ≥ 0.5% | +0.07% | ❌ | 28.17 | 28.19 | 2026-07-31 | 2026-08-06 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — 🔔 ТРИГГЕРИРАН
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-08-09 · **Conditions matched:** 3/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | +2.42% | ✅ | 291.20 | 298.25 | 2026-07-31 | 2026-08-06 |
| XLF | up ≥ 1.0% | +1.53% | ✅ | 56.94 | 57.81 | 2026-07-31 | 2026-08-06 |
| XLY | up ≥ 1.0% | +1.73% | ✅ | 116.09 | 118.10 | 2026-07-31 | 2026-08-06 |
| GLD | down ≥ 0.5% | +4.88% | ❌ | 371.54 | 389.67 | 2026-07-31 | 2026-08-06 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2025-W32 (week ending 2025-08-10)
**Cosine similarity:** 0.9438 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.06% | +5.30% | +8.39% |
| **USO** | +0.12% | -2.78% | +5.03% |
| **GLD** | +6.71% | +17.65% | +45.49% |
| **TLT** | +2.22% | +2.61% | +0.29% |
| **XLE** | +3.12% | +5.43% | +25.40% |
| **IWM** | +7.50% | +9.66% | +20.29% |

### Паралел #2: 2026-W15 (week ending 2026-04-12)
**Cosine similarity:** 0.9331 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +8.64% | +11.11% | +13.11% |
| **USO** | +15.61% | -12.91% | -4.77% |
| **GLD** | -0.96% | -13.75% | -10.86% |
| **TLT** | -1.73% | -2.34% | -4.59% |
| **XLE** | +1.11% | -3.27% | +2.14% |
| **IWM** | +8.14% | +13.28% | +14.14% |

### Паралел #3: 2025-W40 (week ending 2025-10-05)
**Cosine similarity:** 0.9257 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.90% | +2.09% | -2.00% |
| **USO** | +0.31% | -3.83% | +92.33% |
| **GLD** | +1.31% | +11.36% | +20.07% |
| **TLT** | +0.63% | -2.63% | -2.90% |
| **XLE** | -1.93% | +2.69% | +33.28% |
| **IWM** | -1.88% | +1.20% | +2.22% |

### Паралел #4: 2026-W16 (week ending 2026-04-19)
**Cosine similarity:** 0.9137 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.32% | +4.67% | +8.23% |
| **USO** | +31.82% | +6.83% | +2.44% |
| **GLD** | -7.72% | -17.38% | -12.62% |
| **TLT** | -4.65% | -2.93% | -5.23% |
| **XLE** | +11.40% | +4.83% | +5.71% |
| **IWM** | -1.01% | +6.62% | +8.15% |

### Паралел #5: 2025-W04 (week ending 2025-01-26)
**Cosine similarity:** 0.9117 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -2.26% | -9.43% | +4.79% |
| **USO** | -6.87% | -13.28% | -5.97% |
| **GLD** | +5.07% | +19.20% | +20.24% |
| **TLT** | +4.82% | +1.91% | -0.91% |
| **XLE** | -1.83% | -9.77% | -4.61% |
| **IWM** | -5.81% | -15.12% | -1.88% |

### Паралел #6: 2024-W42 (week ending 2024-10-20)
**Cosine similarity:** 0.8330 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.98% | +2.22% | -9.95% |
| **USO** | +1.30% | +15.61% | -2.66% |
| **GLD** | -3.19% | -0.80% | +21.83% |
| **TLT** | -3.38% | -7.12% | -6.75% |
| **XLE** | +5.58% | +4.01% | -9.79% |
| **IWM** | +2.21% | -0.08% | -17.36% |

### Паралел #7: 2024-W39 (week ending 2024-09-29)
**Cosine similarity:** 0.8009 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.80% | +4.12% | -2.77% |
| **USO** | -0.87% | +5.09% | +6.40% |
| **GLD** | +4.52% | -1.48% | +15.93% |
| **TLT** | -6.63% | -11.64% | -8.55% |
| **XLE** | +0.75% | -3.02% | +6.01% |
| **IWM** | +0.64% | +0.93% | -9.02% |

### Паралел #8: 2025-W26 (week ending 2025-06-29)
**Cosine similarity:** 0.7764 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.31% | +7.63% | +12.26% |
| **USO** | +8.90% | +5.10% | -6.55% |
| **GLD** | +1.67% | +15.11% | +38.35% |
| **TLT** | -0.08% | +1.73% | +0.40% |
| **XLE** | +4.28% | +7.84% | +3.63% |
| **IWM** | +3.35% | +12.00% | +16.68% |

### Паралел #9: 2023-W11 (week ending 2023-03-19)
**Cosine similarity:** 0.7750 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +6.21% | +12.68% | +13.69% |
| **USO** | +20.58% | +9.70% | +38.58% |
| **GLD** | +1.35% | -1.16% | -2.95% |
| **TLT** | -2.48% | -3.98% | -13.00% |
| **XLE** | +12.43% | +5.05% | +19.54% |
| **IWM** | +3.97% | +8.59% | +7.23% |

### Паралел #10: 2025-W42 (week ending 2025-10-19)
**Cosine similarity:** 0.7721 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -0.65% | +4.10% | +6.89% |
| **USO** | +6.65% | +5.40% | +70.70% |
| **GLD** | -3.76% | +8.30% | +14.64% |
| **TLT** | -2.35% | -3.73% | -4.53% |
| **XLE** | +5.91% | +10.93% | +27.98% |
| **IWM** | -4.08% | +9.18% | +13.30% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 14 · **Total matching days:** 74 · **History:** 2021-05-17 → 2026-08-06

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 14 | +2.1% | +2.4% | -3.1% | +7.4% | 71% |
| **SPY** | 3m | 14 | +2.8% | +3.0% | -7.3% | +12.0% | 79% |
| **SPY** | 6m | 14 | +7.8% | +9.8% | -6.8% | +21.8% | 79% |
| **USO** | 1m | 14 | +0.1% | -1.2% | -14.3% | +12.7% | 43% |
| **USO** | 3m | 14 | -2.3% | -4.1% | -18.9% | +24.5% | 43% |
| **USO** | 6m | 14 | +9.4% | -3.2% | -21.1% | +109.4% | 43% |
| **GLD** | 1m | 14 | +2.8% | +2.0% | -0.9% | +8.9% | 79% |
| **GLD** | 3m | 14 | +5.7% | +5.8% | -12.6% | +24.5% | 71% |
| **GLD** | 6m | 14 | +6.5% | +8.0% | -12.5% | +25.3% | 71% |
| **TLT** | 1m | 14 | -1.4% | -1.1% | -6.7% | +3.6% | 36% |
| **TLT** | 3m | 14 | -0.6% | -0.1% | -16.5% | +11.1% | 50% |
| **TLT** | 6m | 14 | -4.2% | -3.0% | -18.0% | +7.5% | 29% |

**Episodes (последни 5 от 14):**
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-08-03` (5d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 61 · **History:** 2021-05-17 → 2026-08-06

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +5.7% | +5.7% | +2.2% | +9.1% | 100% |
| **SPY** | 3m | 2 | +6.2% | +6.2% | +2.2% | +10.3% | 100% |
| **SPY** | 6m | 2 | +8.0% | +8.0% | +2.2% | +13.7% | 100% |
| **USO** | 1m | 2 | +3.1% | +3.1% | -1.1% | +7.2% | 50% |
| **USO** | 3m | 2 | -5.5% | -5.5% | -9.9% | -1.1% | 0% |
| **USO** | 6m | 2 | -2.8% | -2.8% | -4.6% | -1.1% | 0% |
| **GLD** | 1m | 2 | +2.3% | +2.3% | -0.2% | +4.7% | 50% |
| **GLD** | 3m | 2 | -4.6% | -4.6% | -13.8% | +4.7% | 50% |
| **GLD** | 6m | 2 | -2.8% | -2.8% | -10.3% | +4.7% | 50% |
| **TLT** | 1m | 2 | -1.4% | -1.4% | -1.9% | -1.0% | 0% |
| **TLT** | 3m | 2 | -2.4% | -2.4% | -2.9% | -1.9% | 0% |
| **TLT** | 6m | 2 | -3.5% | -3.5% | -5.1% | -1.9% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-08-03` (14d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 415 · **History:** 2021-05-17 → 2026-08-06

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
- `2025-11-03 → 2026-08-06` (183d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-08-06

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 9 · **Total matching days:** 86 · **History:** 2021-05-17 → 2026-08-06

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 9 | -0.1% | +0.9% | -7.2% | +7.8% | 56% |
| **SPY** | 3m | 9 | +2.0% | +2.8% | -8.3% | +11.6% | 56% |
| **SPY** | 6m | 9 | +1.3% | +4.1% | -20.8% | +14.2% | 67% |
| **USO** | 1m | 9 | +2.5% | -1.7% | -15.0% | +52.9% | 33% |
| **USO** | 3m | 9 | +7.3% | -0.1% | -20.7% | +52.2% | 44% |
| **USO** | 6m | 9 | +6.9% | -0.2% | -27.6% | +45.8% | 44% |
| **GLD** | 1m | 9 | -1.9% | -1.6% | -8.3% | +2.8% | 22% |
| **GLD** | 3m | 9 | -1.0% | +0.2% | -12.0% | +6.4% | 56% |
| **GLD** | 6m | 9 | -0.3% | -0.8% | -16.8% | +25.0% | 44% |
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
**Episodes:** 16 · **Total matching days:** 275 · **History:** 2021-05-17 → 2026-08-06

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.1% | +1.9% | -4.8% | +9.0% | 75% |
| **SPY** | 3m | 16 | +3.3% | +4.4% | -12.6% | +16.2% | 75% |
| **SPY** | 6m | 16 | +6.9% | +8.6% | -14.0% | +21.0% | 81% |
| **USO** | 1m | 16 | +1.3% | -3.2% | -13.0% | +22.9% | 38% |
| **USO** | 3m | 16 | +2.0% | -1.7% | -14.5% | +29.9% | 38% |
| **USO** | 6m | 16 | +11.3% | +1.8% | -12.4% | +87.1% | 62% |
| **GLD** | 1m | 16 | +2.5% | +1.8% | -5.6% | +9.0% | 75% |
| **GLD** | 3m | 16 | +6.3% | +7.4% | -16.8% | +23.6% | 69% |
| **GLD** | 6m | 16 | +11.2% | +12.1% | -11.9% | +43.8% | 75% |
| **TLT** | 1m | 16 | +0.4% | +0.3% | -6.3% | +8.2% | 50% |
| **TLT** | 3m | 16 | -1.6% | -1.4% | -15.3% | +11.9% | 38% |
| **TLT** | 6m | 16 | -4.6% | -3.4% | -21.3% | +7.0% | 38% |

**Episodes (последни 5 от 16):**
- `2025-03-27 → 2025-05-08` (25d)
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 19 · **Total matching days:** 288 · **History:** 2021-05-17 → 2026-08-06

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 19 | +0.4% | +1.0% | -8.7% | +7.0% | 53% |
| **SPY** | 3m | 19 | +2.1% | +3.6% | -13.7% | +9.1% | 68% |
| **SPY** | 6m | 19 | +3.4% | +6.8% | -16.4% | +16.9% | 74% |
| **USO** | 1m | 19 | -0.6% | -5.6% | -21.8% | +55.8% | 42% |
| **USO** | 3m | 19 | +3.0% | -1.3% | -12.7% | +64.3% | 42% |
| **USO** | 6m | 19 | +7.3% | -5.2% | -16.0% | +75.1% | 47% |
| **GLD** | 1m | 19 | -0.6% | -0.1% | -12.4% | +7.6% | 47% |
| **GLD** | 3m | 19 | +1.7% | +1.3% | -13.7% | +19.0% | 63% |
| **GLD** | 6m | 19 | +7.6% | +6.0% | -17.7% | +55.5% | 68% |
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
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-08-06

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (13 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | 5 | 2.47 | 2.47 | 2026-07-04 00:00:00 | 2026-08-01 00:00:00 | ✓ |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 5 | 2.45 | 2.89 | 2026-07-04 00:00:00 | 2026-08-01 00:00:00 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 5 | 2.37 | 2.43 | 2026-07-04 00:00:00 | 2026-08-01 00:00:00 | - |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 5 | 2.34 | 2.34 | 2026-07-04 00:00:00 | 2026-08-01 00:00:00 | ✓ |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 5 | 2.28 | 2.28 | 2026-07-04 00:00:00 | 2026-08-01 00:00:00 | ✓ |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | 5 | 2.02 | 2.02 | 2026-07-04 00:00:00 | 2026-08-01 00:00:00 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | 5 | 2.02 | 2.02 | 2026-07-04 00:00:00 | 2026-08-01 00:00:00 | ✓ |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 3 | 2.48 | 2.56 | 2026-07-04 00:00:00 | 2026-08-01 00:00:00 | - |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | 3 | 2.28 | 2.28 | 2026-07-18 00:00:00 | 2026-08-01 00:00:00 | ✓ |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | 2 | 2.58 | 2.58 | 2026-07-04 00:00:00 | 2026-07-11 00:00:00 | - |
| **CSUSHPISA** | Case-Shiller US National HPI (SA) | housing | housing_prices | 2 | 2.17 | 2.17 | 2026-07-04 00:00:00 | 2026-07-11 00:00:00 | - |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | 1 | 2.09 | 2.09 | 2026-08-01 00:00:00 | 2026-08-01 00:00:00 | - |
| **MSACSR** | Месеци предлагане — нови жилища | housing | housing_affordability | 1 | 2.02 | 2.02 | 2026-07-18 00:00:00 | 2026-07-18 00:00:00 | ✓ |

### EU (6 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.27 | 5.27 | 2026-07-04 00:00:00 | 2026-08-01 00:00:00 | - |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.17 | 2.27 | 2026-07-04 00:00:00 | 2026-08-01 00:00:00 | ✓ |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.17 | 2.25 | 2026-07-04 00:00:00 | 2026-08-01 00:00:00 | ✓ |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | 4 | 2.66 | 2.66 | 2026-07-04 00:00:00 | 2026-07-25 00:00:00 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation | sentiment | 4 | 2.17 | 2.17 | 2026-07-04 00:00:00 | 2026-07-25 00:00:00 | - |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | 3 | 2.38 | 2.38 | 2026-07-18 00:00:00 | 2026-08-01 00:00:00 | - |

### CN (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 8 | 2.56 | 2.56 | 2026-07-06 00:00:00 | 2026-08-03 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 8 | 2.23 | 2.23 | 2026-07-06 00:00:00 | 2026-08-03 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 1 | 2.22 | 2.22 | 2026-07-08 00:00:00 | 2026-07-08 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-08-01 00:00:00 · **Generated:** 2026-08-01 09:08:44.722832+00:00

**Режим:** `soft_landing` (Soft landing)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 37.2 | contracting | 25.9% | 4 | 3 |
| **growth** | 45.7 | mixed | 40.0% | 2 | 1 |
| **inflation** | 40.4 | mixed | 38.9% | 4 | 2 |
| **liquidity** | 52.0 | mixed | 47.4% | 0 | 0 |

### Top anomalies (10 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | -2.47 | down | 61.50 | 2026-06-01 | ✓ min |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.34 | down | 94.99 | 2026-01-01 | ✓ min |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | -2.30 | down | 2.24 | 2026-05-01 | - |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | +2.28 | up | 55.10 | 2026-05-01 | ✓ max |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | -2.28 | down | 0.13 | 2026-06-01 | ✓ min |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | +2.16 | up | 4.60 | 2026-06-01 | - |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | +2.15 | up | 5.51 | 2026-06-01 | - |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | -2.09 | down | 2.70 | 2026-06-01 | - |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | -2.02 | down | 59.00 | 2026-06-01 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | -2.02 | down | 1.90 | 2026-05-01 | ✓ min |

### Narrative hints от макро лещите
- **CIVPART**: Структурни сдвигове (демография, ранно пенсиониране). Пост-COVID не се възстанови напълно.
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **HPIPONM226S**: Monthly FHFA версия. Само purchase transactions (без refi appraisals). По-чист от refi-bias.
- **US_PMI_MFG**: Markit mfg — comparable cross-country. ISM е US-only.
- **TRIMMED_MEAN_CPI**: Орязва 8% в опашките (топ и долу). По-стабилна от median при многоизмерен shock.
- **MICH_INFL_1Y**: Household очаквания. По-шумни от market-based, но по-ранни. Extreme movements сигнализират de-anchoring risk.
- **PPIFIS**: Производствени цени → consumer prices с 1-3 месечен lag. Водещ за CPI при трендови промени.
- **PSAVERT**: Hard data компонент. Скочи >30% в COVID — когато survey и hard data разминават, сигналът укрепва.
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
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.667
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Realized CPI × Expectations
  - `question_bg`: Дали expectations следват realized inflation, или стоят anchored?
  - `state`: both_down
  - `interpretation`: Joint disinflation — expectations потвърждават cooling.
  - `slot_a_label`: Realized inflation
  - `slot_b_label`: Inflation expectations
  - `breadth_a`: 0.0
  - `breadth_b`: 0.333
  - `state_raw`: both_down
  - `breadth_a_raw`: 0.333
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
> Конфигурацията подкрепя soft landing — labor остава tight, но инфлацията се охлажда. Fed credibility за момента издържа. Най-отклонена леща: Инфлация и цени — breadth 33% (свиване), 4 аномалии, 2 нови екстремума. За наблюдение следващия релиз: CIVPART, LABOR_SHARE_NBS, US_PMI_MFG (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: CIVPART z=-2.47 · NEW-5Y-MIN
- 5 нови екстремуми в top-10 (lookback 5г.)
- Активни двойки: Stagflation test=a_up_b_down; Inflation anchoring=both_down; Credit × Policy=a_down_b_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-08-01 00:00:00 · **Generated:** 2026-08-01 09:32:53.580743+00:00

**Режим:** `policy_dilemma` (Policy dilemma (индикирана))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 39.7 | mixed | 42.9% | 0 | 0 |
| **growth** | 42.2 | mixed | 16.7% | 0 | 0 |
| **inflation** | 51.2 | mixed | 85.7% | 0 | 0 |
| **credit** | 45.4 | mixed | 36.8% | 3 | 0 |
| **external** | 12.0 | contracting | 16.7% | 1 | 0 |

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
  - `state`: both_up
  - `interpretation`: Healthy expansion: sentiment + hard data confirm-ват растеж.
  - `slot_a_label`: Sentiment (ESI, confidence)
  - `slot_b_label`: Hard activity (IP, retail, GDP)
  - `breadth_a`: 0.667
  - `breadth_b`: 0.75
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.667
  - `breadth_b_raw`: 1.0
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
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 1.0

### Executive narrative
> Policy dilemma — labor market е loose, но инфлацията remains hot. ЕЦБ е заклещена между инфлацията и растежа. Най-отклонена леща: Инфлация и цени — breadth 83% (разширяване), 0 аномалии, 0 нови екстремума. За наблюдение: EA_BUND_2Y (z=+5.27) — най-силното отклонение.

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.27
- Активни двойки: Stagflation test=a_down_b_up; Sentiment × Hard=both_up; Growth × Labor=both_up



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-08-03 00:00:00 · **Generated:** 2026-08-03 09:10:50.049599+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 39.2 | mixed | -% | - | - |
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
> Претеглен композитен macro score 38.5/100 → режим „ВЛОШАВАЩ СЕ“ (5/5 лещи). 5 лещи, 2 flagged аномалии (4 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-07-31 |
| `as_of` | 2026-07-31 |
| `regime` | REFLATION |
| `alignment_score` | 5.0 |
| `gms_score` | 2.0 |
| `gms_max` | 8 |
| `gms_tier` | LOW |
| `ks_status` | inactive |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-07-31 → 2026-08-05)

**stable_winner (1m):** +4 entered, -5 exited
  - **Entered:** HWM, MU, NTRS, TSLA _(включително 1 за първи път в историята: TSLA)_
  - **Exited:** CHRW, EBAY, EIX, GEV, GM

**stable_winner (3m):** +4 entered, -3 exited
  - **Entered:** HWM, TSLA, VRT, VTRS _(включително 2 за първи път в историята: HWM, TSLA)_
  - **Exited:** BIIB, HST, IRM

**quality_dip (1m):** +5 entered, -3 exited
  - **Entered:** CHRW, EBAY, EIX, GEV, GM _(включително 1 за първи път в историята: EIX)_
  - **Exited:** HWM, MU, NTRS

**quality_dip (3m):** +3 entered, -3 exited
  - **Entered:** BIIB, HST, IRM _(включително 1 за първи път в историята: IRM)_
  - **Exited:** HWM, VRT, VTRS

**faded_bounce (1m):** +6 entered, -3 exited
  - **Entered:** DXCM, EOG, FDS, GPN, LULU, PYPL
  - **Exited:** AON, HRL, LII

**faded_bounce (3m):** +4 entered, -5 exited
  - **Entered:** ABT, BSX, DPZ, EFX _(включително 1 за първи път в историята: BSX)_
  - **Exited:** ARES, DECK, ERIE, EXE, PCG

### EU (period: 2026-07-31 → 2026-08-06)

**stable_winner (1m):** +2 entered, -3 exited
  - **Entered:** BPE.MI, METSO.HE
  - **Exited:** AED.BR, BBVA.MC, GLE.PA

**stable_winner (3m):** +8 entered, -6 exited
  - **Entered:** ALLN.SW, DANSKE.CO, EBS.VI, EDPR.LS, LOTB.BR, MOBN.SW, SAND.ST, UNI.MC _(включително 2 за първи път в историята: EDPR.LS, LOTB.BR)_
  - **Exited:** AED.BR, BBVA.MC, ELI.BR, HUBN.SW, PKN.WA, UMI.BR

**quality_dip (1m):** +6 entered, -4 exited
  - **Entered:** BBVA.MC, FLS.CO, GLE.PA, GLEN.L, LOTB.BR, SDR.L _(включително 4 за първи път в историята: FLS.CO, GLEN.L, LOTB.BR, SDR.L)_
  - **Exited:** BPE.MI, CCH.L, IDR.MC, METSO.HE

**quality_dip (3m):** +8 entered, -9 exited
  - **Entered:** BBVA.MC, ELI.BR, FLS.CO, GLEN.L, HUBN.SW, PKN.WA, SDR.L, UMI.BR _(включително 4 за първи път в историята: FLS.CO, GLEN.L, HUBN.SW, SDR.L)_
  - **Exited:** ALLN.SW, CCH.L, DANSKE.CO, EBS.VI, EDPR.LS, IDR.MC, MOBN.SW, SAND.ST, UNI.MC

**faded_bounce (1m):** +2 entered, -7 exited
  - **Entered:** TE.PA, WIE.VI _(включително 2 за първи път в историята: TE.PA, WIE.VI)_
  - **Exited:** AUTO.L, EVD.DE, G24.DE, LSEG.L, RMV.L, UMG.AS, WPP.L

**faded_bounce (3m):** +2 entered, -3 exited
  - **Entered:** TE.PA, WIE.VI _(включително 2 за първи път в историята: TE.PA, WIE.VI)_
  - **Exited:** MF.PA, TBCG.L, WISE.L



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-07-28 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **soyoil** | Commodities | 109855 | 97.0 | 97.0 | 1051 | 17623 |
| **soymeal** | Commodities | 88655 | 91.8 | 91.8 | 1051 | 86814 |
| **copper** | Commodities | 66490 | 91.7 | 91.7 | 1051 | 5123 |
| **brent** | Commodities | 16795 | 88.5 | 88.5 | 234 | 9188 |
| **rbob** | Commodities | 73967 | 84.9 | 84.9 | 1051 | 1659 |
| **soybeans** | Commodities | 155001 | 84.2 | 84.2 | 1051 | 123801 |
| **gbpfx** | FX | 41097 | 80.5 | 80.5 | 1051 | 24824 |
| **vix** | Volatility | -12289 | 73.2 | 73.2 | 1010 | -10272 |
| **cotton** | Commodities | 52410 | 72.1 | 72.1 | 1051 | 20425 |
| **corn** | Commodities | 168399 | 64.4 | 64.4 | 1051 | 214608 |
| **coffee** | Commodities | 25136 | 64.1 | 64.1 | 1051 | 3913 |
| **aud** | FX | 27618 | 63.5 | 63.5 | 1051 | -4159 |
| **wheat** | Commodities | -6880 | 58.0 | 58.0 | 1051 | 62150 |
| **cattle** | Commodities | 66523 | 55.0 | 55.0 | 1051 | -52780 |
| **gold** | Commodities | 120328 | 51.5 | 51.5 | 1051 | 3511 |
| **dxy** | FX | -1601 | 50.5 | 50.5 | 1051 | 3979 |
| **sp500** | US Equities | -297476 | 49.5 | 49.5 | 1051 | 62993 |
| **heatingoil** | Commodities | 11374 | 44.4 | 44.4 | 1051 | 2880 |
| **bitcoin** | Crypto | -6873 | 33.4 | 33.4 | 434 | -1560 |
| **platinum** | Commodities | 6377 | 32.2 | 32.2 | 1051 | -1485 |
| **chf** | FX | -9647 | 25.3 | 25.3 | 1051 | 19 |
| **eurfx** | FX | -65198 | 24.8 | 24.8 | 1051 | -32554 |
| **wti** | Commodities | 108307 | 22.9 | 22.9 | 1051 | 14594 |
| **silver** | Commodities | 8387 | 22.4 | 22.4 | 1051 | -4360 |
| **russell** | US Equities | -74620 | 22.0 | 22.0 | 587 | 9738 |
| **natgas** | Commodities | -105605 | 16.8 | 16.8 | 1051 | -40551 |
| **cocoa** | Commodities | -14127 | 12.1 | 12.1 | 1051 | 2569 |
| **us2y** | Rates | -1564294 | 12.1 | 12.1 | 1051 | 184581 |
| **us5y** | Rates | -2108638 | 11.3 | 11.3 | 1051 | 37652 |
| **palladium** | Commodities | -6173 | 10.1 | 10.1 | 1051 | -184 |
| **sugar** | Commodities | -112413 | 9.1 | 9.1 | 1051 | 38162 |
| **us30y** | Rates | -389522 | 9.1 | 9.1 | 1051 | -47600 |
| **nasdaq** | US Equities | -58298 | 5.1 | 5.1 | 1051 | 10319 |
| **jpy** | FX | -101990 | 4.5 | 4.5 | 1051 | 13410 |
| **hogs** | Commodities | -10884 | 3.7 | 3.7 | 1051 | 16483 |
| **usultra10y** | Rates | -400210 | 3.3 | 3.3 | 541 | -88928 |
| **us10y** | Rates | -2155739 | 2.7 | 2.7 | 1051 | -185888 |
| **cad** | FX | -102495 | 0.3 | 0.3 | 1051 | -14394 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **DELL** | Technology | 98.4 | 11.1% | 114.2% | 296.8% | 224.0% | 1.82 | -32.3% |
| 2 | **MU** | Technology | 97.6 | -4.8% | 39.5% | 113.1% | 772.1% | 2.59 | -39.1% |
| 3 | **HPE** | Technology | 97.2 | 22.4% | 77.7% | 146.7% | 121.7% | 1.87 | -26.4% |
| 4 | **PANW** | Technology | 96.8 | 7.6% | 97.1% | 118.2% | 97.1% | 1.72 | -36.0% |
| 5 | **AMD** | Technology | 95.4 | -6.6% | 35.7% | 99.1% | 191.9% | 1.35 | -27.8% |
| 6 | **AMAT** | Technology | 94.6 | -3.6% | 30.2% | 68.1% | 205.5% | 1.73 | -39.6% |
| 7 | **DDOG** | Technology | 94.5 | 10.3% | 94.3% | 136.7% | 84.6% | 1.08 | -48.6% |
| 8 | **CRWD** | Technology | 94.0 | 7.8% | 76.2% | 99.0% | 71.2% | 1.18 | -37.2% |
| 9 | **MRVL** | Technology | 93.2 | -8.5% | 25.1% | 179.6% | 202.0% | 1.26 | -48.4% |
| 10 | **FLEX** | Technology | 92.4 | -7.3% | 26.4% | 84.7% | 158.2% | 1.29 | -36.4% |
| 11 | **NTAP** | Technology | 92.2 | 12.9% | 64.0% | 97.0% | 62.9% | 1.36 | -24.8% |
| 12 | **CNC** | Healthcare | 92.1 | 1.3% | 26.4% | 57.6% | 152.3% | 1.82 | -32.7% |
| 13 | **FTNT** | Technology | 92.1 | 3.4% | 82.5% | 107.0% | 61.0% | 1.00 | -30.9% |
| 14 | **VLO** | Energy | 91.0 | 14.0% | 20.3% | 59.6% | 100.5% | 2.21 | -14.2% |
| 15 | **WDC** | Technology | 90.7 | -2.4% | 11.6% | 79.0% | 590.3% | 2.44 | -38.1% |
| 16 | **HUM** | Healthcare | 90.2 | -7.8% | 52.2% | 89.9% | 61.8% | 0.72 | -47.2% |
| 17 | **STX** | Technology | 89.8 | 1.2% | 8.7% | 88.9% | 439.0% | 2.32 | -31.8% |
| 18 | **CSCO** | Technology | 89.5 | 8.7% | 29.3% | 47.5% | 66.6% | 1.66 | -15.3% |
| 19 | **STT** | Financial Services | 88.9 | 4.0% | 26.4% | 45.5% | 68.1% | 2.09 | -11.8% |
| 20 | **NUE** | Basic Materials | 87.5 | 20.8% | 18.7% | 48.2% | 68.2% | 2.15 | -18.4% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **ATS.VI** | Technology | 95.5 | -31.6% | 36.4% | 197.4% | 954.7% | 2.50 | -50.1% |
| 2 | **TPRO.MI** | Technology | 94.8 | -18.5% | 39.8% | 74.8% | 372.6% | 2.10 | -32.2% |
| 3 | **RBI.VI** | Financial Services | 91.8 | 9.2% | 34.9% | 43.5% | 133.3% | 2.27 | -18.0% |
| 4 | **AKER.OL** | Industrials | 88.5 | 6.5% | 17.9% | 50.4% | 98.8% | 2.30 | -15.6% |
| 5 | **UNI.MI** | Financial Services | 88.4 | 4.5% | 31.1% | 49.6% | 64.0% | 1.92 | -11.5% |
| 6 | **BMPS.MI** | Financial Services | 88.1 | 3.9% | 36.1% | 42.5% | 67.8% | 1.58 | -25.5% |
| 7 | **REP.MC** | Energy | 87.4 | 19.6% | 19.0% | 58.7% | 69.1% | 2.12 | -20.4% |
| 8 | **CCC.L** | Technology | 87.2 | 5.0% | 22.1% | 36.5% | 92.9% | 2.06 | -16.2% |
| 9 | **SSAB-B.ST** | Basic Materials | 86.5 | 9.3% | 26.2% | 42.0% | 66.2% | 1.65 | -34.3% |
| 10 | **GL9.IR** | Consumer Defensive | 86.0 | -8.8% | 13.3% | 41.7% | 100.9% | 2.07 | -10.0% |
| 11 | **ACX.MC** | Basic Materials | 86.0 | 12.8% | 21.9% | 43.1% | 65.8% | 1.86 | -14.9% |
| 12 | **ABN.AS** | Financial Services | 85.2 | 3.1% | 30.5% | 26.9% | 70.2% | 1.97 | -18.0% |
| 13 | **DHER.DE** | Consumer Cyclical | 85.0 | 1.0% | 79.8% | 47.3% | 43.3% | 0.59 | -48.7% |
| 14 | **MT.AS** | Basic Materials | 84.6 | 5.5% | 15.8% | 27.6% | 121.8% | 1.98 | -26.2% |
| 15 | **BFT.WA** | Industrials | 84.6 | 7.3% | 31.8% | 39.4% | 47.8% | 1.62 | -17.4% |
| 16 | **PKN.WA** | Energy | 84.2 | 12.1% | 9.6% | 47.5% | 78.9% | 2.03 | -12.3% |
| 17 | **HSBA.L** | Financial Services | 84.1 | 10.1% | 24.8% | 24.3% | 58.1% | 2.03 | -18.1% |
| 18 | **FRO.OL** | Energy | 83.7 | 3.0% | 10.0% | 41.3% | 90.3% | 1.57 | -20.5% |
| 19 | **IFX.DE** | Technology | 83.5 | -20.6% | 3.8% | 50.8% | 131.0% | 1.16 | -38.1% |
| 20 | **BG.VI** | Financial Services | 83.2 | -0.6% | 17.4% | 31.1% | 69.8% | 1.91 | -16.3% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **EIX** | Utilities | 2.305 | 1.938 | 0.992 | 3.031 | -0.717 | - | 6.9 | +19.7% |
| 2 | **MO** | Consumer Staples | 1.680 | 1.012 | 1.958 | 1.198 | -0.402 | - | 14.4 | - |
| 3 | **NEM** | Materials | 1.649 | 1.074 | 1.771 | 1.270 | 0.570 | - | 13.3 | +25.9% |
| 4 | **APA** | Energy | 1.323 | 1.666 | 0.908 | 0.857 | -0.436 | - | 8.5 | +26.2% |
| 5 | **CF** | Materials | 1.253 | 0.354 | 1.015 | 1.762 | 0.489 | - | 8.7 | +27.3% |
| 6 | **SPG** | Real Estate | 1.182 | 1.153 | 1.352 | 0.469 | -1.346 | - | 15.6 | +113.6% |
| 7 | **HST** | Real Estate | 1.182 | 1.437 | 0.397 | 1.276 | 0.112 | - | 15.9 | +14.9% |
| 8 | **SYF** | Financials | 1.174 | 0.051 | 1.179 | 1.654 | -0.451 | - | 8.1 | +20.8% |
| 9 | **DVA** | Health Care | 1.159 | 1.254 | 0.216 | 1.588 | -1.464 | - | 17.4 | +88.5% |
| 10 | **MAS** | Industrials | 1.157 | 0.007 | 1.455 | 1.342 | -0.834 | - | 17.4 | +5862.5% |
| 11 | **MU** | Information Technology | 1.062 | 1.591 | 0.904 | 0.262 | -0.628 | - | 19.9 | +66.6% |
| 12 | **BMY** | Health Care | 0.980 | 0.576 | 0.866 | 1.025 | 0.636 | - | 14.1 | +46.6% |
| 13 | **MAR** | Consumer Discretionary | 0.958 | 1.692 | 1.335 | -0.581 | 0.508 | - | 37.7 | - |
| 14 | **ES** | Utilities | 0.931 | 0.521 | 1.024 | 0.772 | -0.425 | - | 15.4 | +9.0% |
| 15 | **VLO** | Energy | 0.928 | 1.817 | -0.101 | 0.834 | -0.042 | - | 12.6 | +27.6% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -1.884 | -1.083 | -1.205 | -2.482 | -1.148 |
| 502 | **KKR** | Financials | -1.813 | -1.657 | -1.294 | -1.672 | -0.886 |
| 501 | **XYZ** | Financials | -1.596 | -0.320 | -2.145 | -1.390 | -1.250 |
| 500 | **MOS** | Materials | -1.567 | -2.417 | -1.511 | -0.100 | 0.006 |
| 499 | **COIN** | Financials | -1.557 | -2.329 | -1.648 | 0.000 | -1.592 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W32.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W32.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-08-03  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
