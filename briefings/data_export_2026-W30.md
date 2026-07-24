# Сателит — пълен data export за 2026-W30

_Период: 2026-07-20 → 2026-07-26_  
_Генериран: 2026-07-24 08:29 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W30.md` (structured briefing) и `narrative_2026-W30.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**15 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **XLY** | -5.79% | -2.55σ | 115.44 | 108.76 | 2026-07-17 | 2026-07-23 | -0.30% | +2.15% | 13 |
| **XLC** | -4.76% | -2.23σ | 110.65 | 105.38 | 2026-07-17 | 2026-07-23 | -0.55% | +1.89% | 13 |
| **URA** | +6.20% | +1.74σ | 38.73 | 41.13 | 2026-07-17 | 2026-07-23 | -2.64% | +5.08% | 13 |
| **XLP** | -2.32% | -1.72σ | 85.19 | 83.21 | 2026-07-17 | 2026-07-23 | +0.26% | +1.50% | 13 |
| **DIA** | -0.87% | -1.48σ | 520.81 | 516.26 | 2026-07-17 | 2026-07-23 | +0.41% | +0.87% | 13 |
| **USO** | +12.53% | +1.40σ | 123.96 | 139.49 | 2026-07-17 | 2026-07-23 | +0.85% | +8.35% | 13 |
| **LQD** | -1.21% | -1.39σ | 107.56 | 106.26 | 2026-07-17 | 2026-07-23 | -0.17% | +0.75% | 13 |
| **DBC** | +4.59% | +1.33σ | 28.98 | 30.31 | 2026-07-17 | 2026-07-23 | +0.24% | +3.28% | 13 |
| **GDX** | +5.19% | +1.32σ | 71.32 | 75.02 | 2026-07-17 | 2026-07-23 | -2.42% | +5.76% | 13 |
| **XLU** | +2.26% | +1.26σ | 45.17 | 46.19 | 2026-07-17 | 2026-07-23 | -0.15% | +1.91% | 13 |
| **IEF** | -1.05% | -1.21σ | 93.84 | 92.85 | 2026-07-17 | 2026-07-23 | -0.17% | +0.74% | 13 |
| **SLV** | +2.52% | +1.10σ | 50.78 | 52.06 | 2026-07-17 | 2026-07-23 | -2.70% | +4.74% | 13 |
| **GLD** | +0.84% | +1.07σ | 368.41 | 371.52 | 2026-07-17 | 2026-07-23 | -1.44% | +2.12% | 13 |
| **TLT** | -1.60% | -1.07σ | 84.52 | 83.17 | 2026-07-17 | 2026-07-23 | -0.22% | +1.29% | 13 |
| **XLI** | +1.41% | +1.05σ | 179.41 | 181.94 | 2026-07-17 | 2026-07-23 | +0.26% | +1.09% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-07-26 · **Conditions matched:** 2/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | +12.53% | ✅ | 123.96 | 139.49 | 2026-07-17 | 2026-07-23 |
| DFEN | down ≥ 3.0% | +9.90% | ❌ | 68.05 | 74.79 | 2026-07-17 | 2026-07-23 |
| GLD | down ≥ 1.0% | +0.84% | ❌ | 368.41 | 371.52 | 2026-07-17 | 2026-07-23 |
| URA | down ≥ 3.0% | +6.20% | ❌ | 38.73 | 41.13 | 2026-07-17 | 2026-07-23 |
| UUP | up ≥ 0.5% | +0.81% | ✅ | 28.33 | 28.56 | 2026-07-17 | 2026-07-23 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-07-26 · **Conditions matched:** 0/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | -0.66% | ❌ | 294.04 | 292.09 | 2026-07-17 | 2026-07-23 |
| XLF | up ≥ 1.0% | -0.76% | ❌ | 56.26 | 55.83 | 2026-07-17 | 2026-07-23 |
| XLY | up ≥ 1.0% | -5.79% | ❌ | 115.44 | 108.76 | 2026-07-17 | 2026-07-23 |
| GLD | down ≥ 0.5% | +0.84% | ❌ | 368.41 | 371.52 | 2026-07-17 | 2026-07-23 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2026-W10 (week ending 2026-03-08)
**Cosine similarity:** 0.9579 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.96% | +9.69% | +9.79% |
| **USO** | +26.95% | +22.29% | +28.24% |
| **GLD** | -8.81% | -16.32% | -21.54% |
| **TLT** | -2.06% | -3.84% | -5.98% |
| **XLE** | +6.35% | +1.94% | +4.97% |
| **IWM** | +0.81% | +12.26% | +16.42% |

### Паралел #2: 2025-W24 (week ending 2025-06-15)
**Cosine similarity:** 0.9211 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.21% | +10.12% | +14.20% |
| **USO** | -6.18% | -8.61% | -14.22% |
| **GLD** | -3.02% | +6.05% | +25.02% |
| **TLT** | -1.53% | +4.19% | +1.17% |
| **XLE** | -1.38% | +0.57% | +3.31% |
| **IWM** | +4.75% | +14.10% | +21.52% |

### Паралел #3: 2022-W09 (week ending 2022-03-06)
**Cosine similarity:** 0.9120 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.36% | -5.00% | -9.24% |
| **USO** | -5.86% | +12.60% | -10.11% |
| **GLD** | -2.42% | -6.04% | -13.29% |
| **TLT** | -8.38% | -17.26% | -21.41% |
| **XLE** | +0.96% | +18.98% | +6.29% |
| **IWM** | +2.18% | -5.84% | -9.35% |

### Паралел #4: 2026-W11 (week ending 2026-03-15)
**Cosine similarity:** 0.9044 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.86% | +12.00% | +11.46% |
| **USO** | +3.30% | +4.62% | +16.35% |
| **GLD** | -3.42% | -16.12% | -19.38% |
| **TLT** | +0.77% | -0.89% | -3.89% |
| **XLE** | -3.03% | -0.26% | +2.91% |
| **IWM** | +8.97% | +18.80% | +18.45% |

### Паралел #5: 2026-W08 (week ending 2026-02-22)
**Cosine similarity:** 0.9002 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -5.26% | +8.15% | +7.07% |
| **USO** | +41.67% | +74.30% | +72.53% |
| **GLD** | -13.76% | -11.69% | -20.72% |
| **TLT** | -3.80% | -5.29% | -6.98% |
| **XLE** | +10.86% | +8.40% | +8.20% |
| **IWM** | -5.98% | +7.75% | +10.39% |

### Паралел #6: 2023-W30 (week ending 2023-07-30)
**Cosine similarity:** 0.8945 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.70% | -10.12% | +6.67% |
| **USO** | +1.71% | +8.70% | +1.40% |
| **GLD** | -1.09% | +2.36% | +2.83% |
| **TLT** | -3.51% | -15.47% | -6.04% |
| **XLE** | +2.99% | -1.42% | -1.86% |
| **IWM** | -4.17% | -17.42% | -0.23% |

### Паралел #7: 2025-W01 (week ending 2025-01-05)
**Cosine similarity:** 0.8807 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.66% | -14.64% | +5.64% |
| **USO** | -0.53% | -12.83% | -3.50% |
| **GLD** | +7.81% | +14.88% | +26.14% |
| **TLT** | +1.31% | +6.37% | -0.37% |
| **XLE** | +2.94% | -9.96% | -0.50% |
| **IWM** | +1.11% | -19.27% | -0.60% |

### Паралел #8: 2024-W32 (week ending 2024-08-11)
**Cosine similarity:** 0.8775 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.96% | +12.23% | +12.72% |
| **USO** | -12.15% | -4.05% | -0.47% |
| **GLD** | +3.59% | +10.42% | +17.52% |
| **TLT** | +4.60% | -3.92% | -7.26% |
| **XLE** | -4.78% | +4.85% | -0.95% |
| **IWM** | +0.90% | +15.33% | +9.46% |

### Паралел #9: 2023-W06 (week ending 2023-02-12)
**Cosine similarity:** 0.8765 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -4.00% | +0.87% | +9.22% |
| **USO** | -9.93% | -11.16% | +6.27% |
| **GLD** | +2.00% | +7.76% | +2.45% |
| **TLT** | +0.68% | +0.85% | -7.76% |
| **XLE** | -9.38% | -12.96% | -0.34% |
| **IWM** | -7.25% | -9.24% | +0.36% |

### Паралел #10: 2024-W40 (week ending 2024-10-06)
**Cosine similarity:** 0.8711 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.65% | +3.31% | -11.82% |
| **USO** | -2.12% | +2.06% | -11.04% |
| **GLD** | +3.43% | -0.62% | +14.17% |
| **TLT** | -2.94% | -8.64% | -2.83% |
| **XLE** | -3.23% | -6.13% | -15.48% |
| **IWM** | +2.32% | +2.41% | -17.32% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 14 · **Total matching days:** 72 · **History:** 2021-05-17 → 2026-07-23

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 14 | +1.8% | +1.3% | -3.1% | +7.4% | 64% |
| **SPY** | 3m | 14 | +2.6% | +3.1% | -7.3% | +12.0% | 71% |
| **SPY** | 6m | 14 | +6.9% | +9.8% | -6.8% | +21.8% | 71% |
| **USO** | 1m | 14 | +1.3% | +0.3% | -14.3% | +12.7% | 50% |
| **USO** | 3m | 14 | -0.7% | -2.0% | -18.9% | +24.5% | 50% |
| **USO** | 6m | 14 | +12.8% | +2.1% | -8.7% | +109.4% | 57% |
| **GLD** | 1m | 14 | +2.5% | +0.9% | -0.9% | +8.9% | 79% |
| **GLD** | 3m | 14 | +5.3% | +4.5% | -12.6% | +24.5% | 71% |
| **GLD** | 6m | 14 | +5.5% | +7.4% | -16.5% | +25.3% | 71% |
| **TLT** | 1m | 14 | -1.4% | -1.1% | -6.7% | +3.6% | 36% |
| **TLT** | 3m | 14 | -0.5% | -0.1% | -16.5% | +11.1% | 50% |
| **TLT** | 6m | 14 | -4.0% | -2.7% | -18.0% | +7.5% | 29% |

**Episodes (последни 5 от 14):**
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-07-21` (3d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 55 · **History:** 2021-05-17 → 2026-07-23

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +3.6% | +3.6% | -1.8% | +9.1% | 50% |
| **SPY** | 3m | 2 | +4.2% | +4.2% | -1.8% | +10.3% | 50% |
| **SPY** | 6m | 2 | +3.7% | +3.7% | -1.8% | +9.2% | 50% |
| **USO** | 1m | 2 | +11.7% | +11.7% | +7.2% | +16.1% | 100% |
| **USO** | 3m | 2 | +3.1% | +3.1% | -9.9% | +16.1% | 50% |
| **USO** | 6m | 2 | +14.0% | +14.0% | +12.0% | +16.1% | 100% |
| **GLD** | 1m | 2 | -0.2% | -0.2% | -0.2% | -0.2% | 0% |
| **GLD** | 3m | 2 | -7.0% | -7.0% | -13.8% | -0.2% | 0% |
| **GLD** | 6m | 2 | -7.3% | -7.3% | -14.5% | -0.2% | 0% |
| **TLT** | 1m | 2 | -1.0% | -1.0% | -1.1% | -1.0% | 0% |
| **TLT** | 3m | 2 | -2.0% | -2.0% | -2.9% | -1.1% | 0% |
| **TLT** | 6m | 2 | -2.7% | -2.7% | -4.3% | -1.1% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-07-23` (8d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 405 · **History:** 2021-05-17 → 2026-07-23

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
- `2025-11-03 → 2026-07-23` (173d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-07-23

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 9 · **Total matching days:** 80 · **History:** 2021-05-17 → 2026-07-23

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 9 | -0.6% | -1.2% | -7.2% | +7.8% | 44% |
| **SPY** | 3m | 9 | +1.6% | -1.2% | -8.3% | +11.6% | 44% |
| **SPY** | 6m | 9 | +0.4% | +4.1% | -20.8% | +14.2% | 56% |
| **USO** | 1m | 9 | +4.2% | -1.3% | -15.0% | +52.9% | 44% |
| **USO** | 3m | 9 | +9.0% | +5.9% | -20.7% | +52.2% | 56% |
| **USO** | 6m | 9 | +11.1% | +4.5% | -27.6% | +54.6% | 56% |
| **GLD** | 1m | 9 | -2.4% | -2.0% | -8.3% | +1.9% | 11% |
| **GLD** | 3m | 9 | -1.5% | -2.0% | -12.0% | +6.4% | 44% |
| **GLD** | 6m | 9 | -1.2% | -2.0% | -20.6% | +25.0% | 33% |
| **TLT** | 1m | 9 | -1.9% | -2.5% | -6.0% | +2.5% | 11% |
| **TLT** | 3m | 9 | -6.2% | -5.7% | -17.6% | +4.2% | 22% |
| **TLT** | 6m | 9 | -9.9% | -7.8% | -22.3% | +1.2% | 11% |

**Episodes (последни 5 от 9):**
- `2023-04-12 → 2023-04-18` (5d)
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-05-19` (36d)
- `2026-07-22 → 2026-07-23` (2d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 16 · **Total matching days:** 275 · **History:** 2021-05-17 → 2026-07-23

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.1% | +1.9% | -4.8% | +9.0% | 75% |
| **SPY** | 3m | 16 | +3.3% | +4.4% | -12.6% | +16.2% | 75% |
| **SPY** | 6m | 16 | +6.6% | +7.6% | -14.0% | +21.0% | 81% |
| **USO** | 1m | 16 | +1.3% | -3.2% | -13.0% | +22.9% | 38% |
| **USO** | 3m | 16 | +2.0% | -1.7% | -14.5% | +29.9% | 38% |
| **USO** | 6m | 16 | +12.4% | +2.3% | -12.4% | +87.1% | 69% |
| **GLD** | 1m | 16 | +2.5% | +1.8% | -5.6% | +9.0% | 75% |
| **GLD** | 3m | 16 | +6.3% | +7.4% | -16.8% | +23.6% | 69% |
| **GLD** | 6m | 16 | +11.0% | +12.1% | -16.0% | +43.8% | 75% |
| **TLT** | 1m | 16 | +0.4% | +0.3% | -6.3% | +8.2% | 50% |
| **TLT** | 3m | 16 | -1.6% | -1.4% | -15.3% | +11.9% | 38% |
| **TLT** | 6m | 16 | -4.6% | -3.1% | -21.3% | +7.0% | 38% |

**Episodes (последни 5 от 16):**
- `2025-03-27 → 2025-05-08` (25d)
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 19 · **Total matching days:** 288 · **History:** 2021-05-17 → 2026-07-23

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 19 | +0.4% | +1.0% | -8.7% | +7.0% | 53% |
| **SPY** | 3m | 19 | +1.9% | +2.7% | -13.7% | +9.1% | 68% |
| **SPY** | 6m | 19 | +2.9% | +6.5% | -16.4% | +16.9% | 74% |
| **USO** | 1m | 19 | -0.6% | -5.6% | -21.8% | +55.8% | 42% |
| **USO** | 3m | 19 | +3.8% | -0.6% | -12.7% | +64.3% | 47% |
| **USO** | 6m | 19 | +9.5% | +4.9% | -16.0% | +75.1% | 53% |
| **GLD** | 1m | 19 | -0.6% | -0.1% | -12.4% | +7.6% | 47% |
| **GLD** | 3m | 19 | +1.4% | +1.3% | -13.7% | +19.0% | 63% |
| **GLD** | 6m | 19 | +7.1% | +6.0% | -21.5% | +55.5% | 68% |
| **TLT** | 1m | 19 | -0.2% | -0.1% | -5.6% | +5.2% | 47% |
| **TLT** | 3m | 19 | -3.6% | -4.4% | -17.3% | +8.7% | 32% |
| **TLT** | 6m | 19 | -6.8% | -7.5% | -21.4% | +4.6% | 21% |

**Episodes (последни 5 от 19):**
- `2025-05-12 → 2025-05-19` (3d)
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (13d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-07-23

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (13 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 5 | 2.74 | 2.89 | 2026-06-20 00:00:00 | 2026-07-18 00:00:00 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 5 | 2.40 | 2.43 | 2026-06-20 00:00:00 | 2026-07-18 00:00:00 | - |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 5 | 2.34 | 2.34 | 2026-06-20 00:00:00 | 2026-07-18 00:00:00 | ✓ |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 5 | 2.28 | 2.28 | 2026-06-20 00:00:00 | 2026-07-18 00:00:00 | ✓ |
| **JTSQUR** | Quits rate — напускания | labor | flow | 5 | 2.02 | 2.02 | 2026-06-20 00:00:00 | 2026-07-18 00:00:00 | ✓ |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | 4 | 2.58 | 2.58 | 2026-06-20 00:00:00 | 2026-07-11 00:00:00 | - |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | 3 | 2.47 | 2.47 | 2026-07-04 00:00:00 | 2026-07-18 00:00:00 | ✓ |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | 3 | 2.02 | 2.02 | 2026-07-04 00:00:00 | 2026-07-18 00:00:00 | - |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 2 | 2.56 | 2.56 | 2026-07-04 00:00:00 | 2026-07-11 00:00:00 | - |
| **CSUSHPISA** | Case-Shiller US National HPI (SA) | housing | housing_prices | 2 | 2.17 | 2.17 | 2026-07-04 00:00:00 | 2026-07-11 00:00:00 | - |
| **MSACSR** | Месеци предлагане — нови жилища | housing | housing_affordability | 2 | 2.02 | 2.02 | 2026-06-27 00:00:00 | 2026-07-18 00:00:00 | ✓ |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | 1 | 2.40 | 2.40 | 2026-06-20 00:00:00 | 2026-06-20 00:00:00 | - |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | 1 | 2.28 | 2.28 | 2026-07-18 00:00:00 | 2026-07-18 00:00:00 | ✓ |

### EU (6 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.31 | 5.37 | 2026-06-20 00:00:00 | 2026-07-18 00:00:00 | - |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | 5 | 2.52 | 2.66 | 2026-06-20 00:00:00 | 2026-07-18 00:00:00 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation | sentiment | 5 | 2.49 | 2.98 | 2026-06-20 00:00:00 | 2026-07-18 00:00:00 | - |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.22 | 2.27 | 2026-06-20 00:00:00 | 2026-07-18 00:00:00 | ✓ |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.21 | 2.25 | 2026-06-20 00:00:00 | 2026-07-18 00:00:00 | ✓ |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | 1 | 2.38 | 2.38 | 2026-07-18 00:00:00 | 2026-07-18 00:00:00 | - |

### CN (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 7 | 2.56 | 2.56 | 2026-06-22 00:00:00 | 2026-07-20 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 7 | 2.23 | 2.23 | 2026-06-22 00:00:00 | 2026-07-20 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 2 | 2.23 | 2.24 | 2026-06-22 00:00:00 | 2026-07-08 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-07-18 00:00:00 · **Generated:** 2026-07-18 08:50:49.340283+00:00

**Режим:** `soft_landing` (Soft landing (индикиран))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 36.3 | contracting | 29.6% | 4 | 3 |
| **growth** | 44.9 | mixed | 36.0% | 1 | 1 |
| **inflation** | 40.8 | mixed | 38.9% | 4 | 2 |
| **liquidity** | 53.1 | mixed | 42.1% | 0 | 0 |

### Top anomalies (9 серии)
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
| **MSACSR** | Месеци предлагане — нови жилища | housing | housing_affordability | +2.02 | up | 10.30 | 2026-05-01 | ✓ max |

### Narrative hints от макро лещите
- **CIVPART**: Структурни сдвигове (демография, ранно пенсиониране). Пост-COVID не се възстанови напълно.
- **MICH_INFL_1Y**: Household очаквания. По-шумни от market-based, но по-ранни. Extreme movements сигнализират de-anchoring risk.
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **US_PMI_MFG**: Markit mfg — comparable cross-country. ISM е US-only.
- **TRIMMED_MEAN_CPI**: Орязва 8% в опашките (топ и долу). По-стабилна от median при многоизмерен shock.
- **PPIFIS**: Производствени цени → consumer prices с 1-3 месечен lag. Водещ за CPI при трендови промени.
- **EMRATIO**: Не зависи от definition на 'active labor force'. По-стабилен индикатор на дълбоката заетост.
- **JTSQUR**: Работническа увереност. Ако quits rate пада — хората задържат работата си (pre-recession pattern).
- **MSACSR**: Inventory ÷ current sales rate. <4 = tight market, 6 = balanced, >7 = oversupplied. Класически recession leading.

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
  - `breadth_b`: 1.0
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 1.0
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
  - `breadth_b`: 1.0
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.0
  - `breadth_b_raw`: 1.0

### Executive narrative
> Конфигурацията подкрепя soft landing — labor остава tight, но инфлацията се охлажда. Fed credibility за момента издържа. Най-отклонена леща: Пазар на труда — breadth 42% (смесено), 4 аномалии, 3 нови екстремума. За наблюдение следващия релиз: CIVPART, LABOR_SHARE_NBS, US_PMI_MFG (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: CIVPART z=-2.47 · NEW-5Y-MIN
- 6 нови екстремуми в top-9 (lookback 5г.)
- Активни двойки: Stagflation test=a_up_b_down; Inflation anchoring=a_down_b_up; Credit × Policy=a_down_b_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-07-18 00:00:00 · **Generated:** 2026-07-18 09:08:57.945465+00:00

**Режим:** `disinflation_cooling` (Дезинфлация и охлаждане)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 34.9 | contracting | 42.9% | 1 | 0 |
| **growth** | 38.9 | mixed | 8.3% | 1 | 0 |
| **inflation** | 47.8 | mixed | 85.7% | 1 | 0 |
| **credit** | 45.0 | mixed | 36.8% | 3 | 0 |
| **external** | 15.7 | contracting | 12.5% | 1 | 0 |

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

**Дата:** 2026-07-20 00:00:00 · **Generated:** 2026-07-20 08:32:59.599410+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 43.7 | mixed | -% | - | - |
| **inflation** | 46.3 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 52.3 | mixed | -% | - | - |
| **property** | 23.4 | contracting | -% | - | - |

### Top anomalies (2 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | -2.56 | down | 3.00 | 2026-06-22 | ✓ min |
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
  - `breadth_a`: 0.667
  - `breadth_b`: 0.333

### Executive narrative
> Претеглен композитен macro score 39.7/100 → режим „ВЛОШАВАЩ СЕ“ (5/5 лещи). 5 лещи, 2 flagged аномалии (5 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-07-10 |
| `as_of` | 2026-07-10 |
| `regime` | REFLATION |
| `alignment_score` | 6.0 |
| `gms_score` | 2.0 |
| `gms_max` | 8 |
| `gms_tier` | LOW |
| `ks_status` | unknown |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-07-17 → 2026-07-22)

**stable_winner (1m):** +9 entered, -8 exited
  - **Entered:** ADM, APA, BIIB, DD, F, FITB, HOOD, INCY, VLO _(включително 3 за първи път в историята: DD, FITB, HOOD)_
  - **Exited:** BKR, CASY, CVS, FCX, IDXX, NEM, SATS, WDC

**stable_winner (3m):** +4 entered, -6 exited
  - **Entered:** DD, FITB, MU, VLO _(включително 4 за първи път в историята: DD, FITB, MU, VLO)_
  - **Exited:** BG, CVS, FCX, IBKR, NEM, PWR

**quality_dip (1m):** +7 entered, -8 exited
  - **Entered:** BKR, CASY, FCX, IDXX, NEM, SATS, WDC _(включително 1 за първи път в историята: SATS)_
  - **Exited:** ADM, APA, BIIB, DD, F, HOOD, INCY, VLO

**quality_dip (3m):** +5 entered, -3 exited
  - **Entered:** BG, FCX, IBKR, NEM, PWR
  - **Exited:** DD, MU, VLO

**faded_bounce (1m):** +11 entered, -11 exited
  - **Entered:** ADP, AVB, AWK, BLDR, CAG, CPB, LII, MKC, OTIS, POOL, RSG
  - **Exited:** ARE, ARES, AXON, CLX, DPZ, DXCM, EFX, ELV, ERIE, OKE, PYPL

**faded_bounce (3m):** +4 entered, -4 exited
  - **Entered:** EFX, OTIS, TPL, TTD
  - **Exited:** CARR, ELV, KVUE, SO

### EU (period: 2026-07-17 → 2026-07-22)

**stable_winner (1m):** +13 entered, -16 exited
  - **Entered:** ACS.MC, ALLN.SW, ANA.MC, FR.PA, HOT.DE, IHG.L, MT.AS, NDA.DE, NDX1.DE, SAAB-B.ST, SPSN.SW, SWED-A.ST, VWS.CO _(включително 2 за първи път в историята: IHG.L, MT.AS)_
  - **Exited:** ABN.AS, ABVX.PA, ANTO.L, BAB.L, BARC.L, CA.PA, CBK.DE, CCL.L, COFB.BR, HOC.L, METSO.HE, NKT.CO, PRY.MI, RR.L, SSE.L, WRT1V.HE

**stable_winner (3m):** +5 entered, -9 exited
  - **Entered:** GAW.L, IHG.L, MRL.MC, MT.AS, VWS.CO _(включително 2 за първи път в историята: IHG.L, MT.AS)_
  - **Exited:** ABVX.PA, ASML.AS, BCP.LS, BIRG.IR, HSBA.L, LPP.WA, SAN.MC, STAN.L, UNI.MC

**quality_dip (1m):** +16 entered, -11 exited
  - **Entered:** ABN.AS, ABVX.PA, ANTO.L, BAB.L, BARC.L, CA.PA, CBK.DE, CCL.L, COFB.BR, HOC.L, METSO.HE, NKT.CO, PRY.MI, RR.L, SSE.L, WRT1V.HE _(включително 1 за първи път в историята: ABVX.PA)_
  - **Exited:** ACS.MC, ALLN.SW, ANA.MC, FR.PA, HOT.DE, NDA.DE, NDX1.DE, SAAB-B.ST, SPSN.SW, SWED-A.ST, VWS.CO

**quality_dip (3m):** +9 entered, -3 exited
  - **Entered:** ABVX.PA, ASML.AS, BCP.LS, BIRG.IR, HSBA.L, LPP.WA, SAN.MC, STAN.L, UNI.MC _(включително 1 за първи път в историята: ABVX.PA)_
  - **Exited:** GAW.L, MRL.MC, VWS.CO

**faded_bounce (1m):** +9 entered, -11 exited
  - **Entered:** DNP.WA, GFC.PA, INDT.ST, RAA.DE, SGE.L, SGO.PA, SWEC-B.ST, TBCG.L, TOM.OL _(включително 1 за първи път в историята: TBCG.L)_
  - **Exited:** ADM.L, ADYEN.AS, EXO.AS, HOLN.SW, ICG.L, III.L, ITRK.L, LSEG.L, MF.PA, RMS.PA, WALL-B.ST

**faded_bounce (3m):** +9 entered, -6 exited
  - **Entered:** HNR1.DE, MUV2.DE, NEM.DE, ORSTED.CO, SAP.DE, SOF.BR, TOM.OL, VPK.AS, WKL.AS _(включително 1 за първи път в историята: SOF.BR)_
  - **Exited:** BEI.DE, BEIJ-B.ST, DKSH.SW, HOLN.SW, ITRK.L, SIGN.SW



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-07-14 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **soyoil** | Commodities | 113029 | 98.3 | 98.3 | 1049 | -9885 |
| **vix** | Volatility | 10189 | 91.0 | 91.0 | 1008 | 23484 |
| **copper** | Commodities | 61932 | 90.6 | 90.6 | 1049 | -9144 |
| **rbob** | Commodities | 68951 | 80.5 | 80.5 | 1049 | 1275 |
| **brent** | Commodities | 12938 | 76.3 | 76.3 | 232 | 3591 |
| **cattle** | Commodities | 96324 | 73.9 | 73.9 | 1049 | -28025 |
| **cotton** | Commodities | 49684 | 69.8 | 69.8 | 1049 | 14548 |
| **gbpfx** | FX | 28541 | 69.3 | 69.3 | 1049 | 11705 |
| **coffee** | Commodities | 24967 | 63.9 | 63.9 | 1049 | 16993 |
| **soymeal** | Commodities | 47852 | 63.6 | 63.6 | 1049 | 30400 |
| **aud** | FX | 27222 | 63.2 | 63.2 | 1049 | -14316 |
| **gold** | Commodities | 119147 | 51.1 | 51.1 | 1049 | 6229 |
| **soybeans** | Commodities | 72688 | 50.8 | 50.8 | 1049 | 19870 |
| **heatingoil** | Commodities | 10919 | 43.7 | 43.7 | 1049 | 1472 |
| **dxy** | FX | -4866 | 41.4 | 41.4 | 1049 | -2996 |
| **corn** | Commodities | 43391 | 40.7 | 40.7 | 1049 | 89818 |
| **platinum** | Commodities | 8146 | 40.3 | 40.3 | 1049 | 74 |
| **wheat** | Commodities | -36798 | 38.2 | 38.2 | 1049 | 32733 |
| **bitcoin** | Crypto | -7491 | 31.9 | 31.9 | 432 | -884 |
| **sp500** | US Equities | -365002 | 30.5 | 30.5 | 1049 | 150518 |
| **eurfx** | FX | -53691 | 28.1 | 28.1 | 1049 | -44765 |
| **silver** | Commodities | 10377 | 25.9 | 25.9 | 1049 | -1693 |
| **chf** | FX | -9500 | 25.7 | 25.7 | 1049 | 2866 |
| **natgas** | Commodities | -105501 | 16.9 | 16.9 | 1049 | -20829 |
| **wti** | Commodities | 86383 | 15.0 | 15.0 | 1049 | -31502 |
| **cocoa** | Commodities | -11200 | 14.6 | 14.6 | 1049 | 13802 |
| **russell** | US Equities | -88112 | 13.3 | 13.3 | 585 | -3542 |
| **us30y** | Rates | -365688 | 12.9 | 12.9 | 1049 | -55375 |
| **sugar** | Commodities | -94593 | 11.5 | 11.5 | 1049 | 58537 |
| **us2y** | Rates | -1671766 | 11.3 | 11.3 | 1049 | 33051 |
| **us5y** | Rates | -2156750 | 11.1 | 11.1 | 1049 | 57860 |
| **palladium** | Commodities | -6205 | 9.9 | 9.9 | 1049 | -1937 |
| **jpy** | FX | -90461 | 6.2 | 6.2 | 1049 | 6311 |
| **usultra10y** | Rates | -378565 | 5.9 | 5.9 | 539 | -144580 |
| **nasdaq** | US Equities | -64163 | 4.3 | 4.3 | 1049 | -36009 |
| **us10y** | Rates | -2079653 | 3.2 | 3.2 | 1049 | 2583 |
| **cad** | FX | -92771 | 0.5 | 0.5 | 1049 | -27718 |
| **hogs** | Commodities | -30438 | 0.2 | 0.2 | 1049 | -9479 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **SNDK** | Technology | 99.5 | -29.7% | 77.0% | 252.9% | 5364.4% | 3.34 | -42.0% |
| 2 | **MU** | Technology | 99.3 | -20.8% | 113.5% | 163.0% | 971.4% | 2.74 | -30.3% |
| 3 | **STX** | Technology | 98.8 | -16.9% | 62.3% | 179.2% | 636.7% | 2.53 | -31.8% |
| 4 | **DELL** | Technology | 98.4 | 5.7% | 108.4% | 299.7% | 229.6% | 1.82 | -32.3% |
| 5 | **AMD** | Technology | 98.3 | 0.1% | 94.2% | 138.2% | 251.4% | 1.78 | -27.8% |
| 6 | **INTC** | Technology | 97.8 | -27.2% | 54.9% | 111.3% | 505.9% | 1.89 | -32.6% |
| 7 | **WDC** | Technology | 97.6 | -24.0% | 45.1% | 149.8% | 968.7% | 2.75 | -37.4% |
| 8 | **HPE** | Technology | 97.0 | -0.6% | 67.8% | 138.3% | 139.2% | 1.64 | -26.4% |
| 9 | **AMAT** | Technology | 96.2 | -13.5% | 40.6% | 74.5% | 234.8% | 1.80 | -27.3% |
| 10 | **MRVL** | Technology | 95.5 | -31.4% | 39.5% | 164.6% | 322.2% | 1.36 | -40.5% |
| 11 | **FLEX** | Technology | 95.3 | -18.5% | 49.2% | 97.2% | 192.4% | 1.32 | -26.4% |
| 12 | **CNC** | Healthcare | 93.5 | 3.5% | 68.3% | 44.0% | 132.2% | 1.64 | -55.5% |
| 13 | **VLO** | Energy | 92.1 | 27.5% | 33.9% | 70.1% | 70.9% | 2.05 | -14.2% |
| 14 | **LRCX** | Technology | 91.6 | -22.0% | 23.7% | 43.8% | 304.8% | 1.86 | -29.2% |
| 15 | **DDOG** | Technology | 90.5 | 11.0% | 90.1% | 110.1% | 52.4% | 0.78 | -48.6% |
| 16 | **CSCO** | Technology | 90.3 | -7.3% | 25.6% | 54.4% | 80.8% | 1.44 | -15.3% |
| 17 | **KLAC** | Technology | 90.1 | -20.2% | 20.4% | 44.8% | 188.9% | 1.36 | -31.2% |
| 18 | **PANW** | Technology | 90.1 | 17.1% | 91.6% | 82.2% | 43.3% | 1.14 | -36.0% |
| 19 | **DVA** | Healthcare | 90.0 | 10.7% | 54.8% | 123.3% | 50.4% | 1.14 | -31.4% |
| 20 | **HUM** | Healthcare | 89.9 | 10.5% | 83.3% | 49.5% | 63.4% | 1.07 | -47.2% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **ATS.VI** | Technology | 97.5 | -24.9% | 103.6% | 367.7% | 1040.8% | 2.72 | -32.9% |
| 2 | **TPRO.MI** | Technology | 96.8 | -18.1% | 75.4% | 98.0% | 402.0% | 2.24 | -27.0% |
| 3 | **STMMI.MI** | Technology | 94.9 | -17.4% | 52.8% | 137.4% | 147.3% | 1.30 | -33.5% |
| 4 | **NESTE.HE** | Energy | 93.7 | 23.5% | 36.0% | 69.0% | 115.7% | 2.26 | -20.4% |
| 5 | **IFX.DE** | Technology | 92.9 | -21.4% | 36.8% | 65.7% | 133.1% | 1.20 | -27.7% |
| 6 | **CCC.L** | Technology | 92.9 | 13.1% | 40.7% | 60.2% | 92.2% | 2.28 | -16.2% |
| 7 | **ASML.AS** | Technology | 92.0 | -3.8% | 27.8% | 38.5% | 171.0% | 2.26 | -15.8% |
| 8 | **RBI.VI** | Financial Services | 91.2 | -0.4% | 25.2% | 53.5% | 134.8% | 2.08 | -18.0% |
| 9 | **AKER.OL** | Industrials | 90.1 | 7.2% | 23.4% | 55.4% | 94.2% | 2.31 | -15.6% |
| 10 | **GL9.IR** | Consumer Defensive | 89.6 | 0.2% | 32.2% | 47.2% | 78.1% | 1.98 | -8.7% |
| 11 | **IFCN.SW** | Technology | 88.8 | -11.0% | 36.3% | 50.3% | 76.6% | 1.04 | -25.5% |
| 12 | **BMPS.MI** | Financial Services | 88.7 | 4.3% | 37.5% | 42.5% | 71.3% | 1.65 | -25.5% |
| 13 | **PKN.WA** | Energy | 88.5 | 17.0% | 24.7% | 62.3% | 66.4% | 1.97 | -12.3% |
| 14 | **BFT.WA** | Industrials | 86.6 | 11.6% | 33.8% | 40.9% | 55.2% | 1.91 | -17.4% |
| 15 | **NOKIA.HE** | Technology | 86.5 | -23.6% | 5.5% | 68.1% | 203.4% | 1.55 | -39.7% |
| 16 | **SUBC.OL** | Energy | 86.5 | -3.5% | 15.0% | 51.5% | 84.5% | 1.81 | -11.3% |
| 17 | **DHER.DE** | Consumer Cyclical | 85.9 | 5.3% | 95.4% | 59.2% | 41.3% | 0.63 | -48.7% |
| 18 | **MYCR.ST** | Technology | 85.9 | 11.7% | 29.3% | 70.5% | 46.7% | 1.20 | -17.8% |
| 19 | **REP.MC** | Energy | 85.6 | 18.0% | 17.3% | 54.3% | 61.6% | 1.95 | -20.4% |
| 20 | **BAMI.MI** | Financial Services | 85.4 | -0.1% | 28.5% | 31.3% | 66.8% | 1.88 | -14.8% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **EIX** | Utilities | 2.314 | 2.371 | 0.910 | 2.750 | -0.587 | - | 8.7 | +18.9% |
| 2 | **NEM** | Materials | 1.900 | 1.579 | 1.809 | 1.470 | 0.579 | - | 12.3 | +25.8% |
| 3 | **MO** | Consumer Staples | 1.593 | 1.156 | 1.936 | 0.942 | -0.346 | - | 15.0 | - |
| 4 | **APA** | Energy | 1.429 | 1.665 | 1.151 | 0.889 | -0.345 | - | 8.5 | +26.2% |
| 5 | **HST** | Real Estate | 1.285 | 1.754 | 0.406 | 1.233 | 0.067 | - | 16.3 | +14.9% |
| 6 | **SYF** | Financials | 1.274 | 0.268 | 1.134 | 1.806 | -0.359 | - | 7.4 | +20.8% |
| 7 | **SPG** | Real Estate | 1.143 | 1.177 | 1.334 | 0.416 | -1.319 | - | 15.6 | +113.6% |
| 8 | **CF** | Materials | 1.083 | 0.119 | 0.981 | 1.621 | 0.527 | - | 11.4 | +27.3% |
| 9 | **MAS** | Industrials | 0.928 | 0.091 | 1.258 | 0.956 | -1.656 | - | 19.1 | +8457.1% |
| 10 | **DVA** | Health Care | 0.912 | 1.141 | 0.174 | 1.094 | -1.456 | - | 22.6 | +81.0% |
| 11 | **MU** | Information Technology | 0.903 | 1.601 | 0.805 | -0.026 | -0.686 | - | 22.4 | +66.6% |
| 12 | **BIIB** | Health Care | 0.884 | 1.402 | 0.156 | 0.801 | 0.985 | - | 21.6 | +7.7% |
| 13 | **BMY** | Health Care | 0.862 | 0.421 | 0.907 | 0.853 | 0.348 | - | 17.2 | +38.7% |
| 14 | **GILD** | Health Care | 0.831 | 0.325 | 1.221 | 0.528 | 0.655 | - | 17.8 | +43.4% |
| 15 | **EXPE** | Consumer Discretionary | 0.827 | 1.020 | 0.582 | 0.556 | -0.769 | - | 22.7 | +71.5% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -2.141 | -1.919 | -1.148 | -2.453 | -1.279 |
| 502 | **COIN** | Financials | -2.016 | -2.319 | -1.274 | -1.630 | -1.636 |
| 501 | **CSGP** | Real Estate | -1.708 | -2.959 | -0.786 | -0.771 | 0.442 |
| 500 | **KKR** | Financials | -1.660 | -1.318 | -1.373 | -1.544 | -0.910 |
| 499 | **BA** | Industrials | -1.546 | -0.578 | -1.184 | -2.139 | -1.037 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W30.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W30.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-07-20  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
