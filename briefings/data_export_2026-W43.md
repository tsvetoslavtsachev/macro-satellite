# Сателит — пълен data export за 2026-W43

_Период: 2026-10-19 → 2026-10-25_  
_Генериран: 2026-10-23 11:08 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W43.md` (structured briefing) и `narrative_2026-W43.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**16 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **IWM** | +2.30% | +1.82σ | 270.44 | 276.67 | 2026-10-16 | 2026-10-22 | -0.63% | +1.61% | 13 |
| **TLT** | +2.11% | +1.79σ | 80.05 | 81.74 | 2026-10-16 | 2026-10-22 | -0.41% | +1.41% | 13 |
| **TIP** | +0.75% | +1.78σ | 105.54 | 106.33 | 2026-10-16 | 2026-10-22 | -0.19% | +0.53% | 13 |
| **IEF** | +0.86% | +1.77σ | 90.42 | 91.20 | 2026-10-16 | 2026-10-22 | -0.28% | +0.65% | 13 |
| **LQD** | +0.85% | +1.48σ | 103.40 | 104.28 | 2026-10-16 | 2026-10-22 | -0.30% | +0.78% | 13 |
| **VWO** | -2.03% | -1.45σ | 58.03 | 56.85 | 2026-10-16 | 2026-10-22 | +0.04% | +1.43% | 13 |
| **SHY** | +0.20% | +1.45σ | 81.36 | 81.52 | 2026-10-16 | 2026-10-22 | -0.06% | +0.18% | 13 |
| **XLC** | -2.63% | -1.40σ | 110.32 | 107.42 | 2026-10-16 | 2026-10-22 | -0.01% | +1.87% | 13 |
| **VNQ** | +0.97% | +1.38σ | 91.76 | 92.65 | 2026-10-16 | 2026-10-22 | -0.65% | +1.17% | 13 |
| **XLF** | +2.04% | +1.38σ | 55.52 | 56.65 | 2026-10-16 | 2026-10-22 | -0.09% | +1.54% | 13 |
| **DIA** | +1.69% | +1.38σ | 519.10 | 527.89 | 2026-10-16 | 2026-10-22 | -0.02% | +1.24% | 13 |
| **XLP** | +2.70% | +1.26σ | 87.62 | 89.99 | 2026-10-16 | 2026-10-22 | +0.24% | +1.96% | 13 |
| **GLD** | -3.41% | -1.25σ | 382.01 | 369.00 | 2026-10-16 | 2026-10-22 | +0.32% | +2.98% | 13 |
| **HYG** | +0.31% | +1.19σ | 76.86 | 77.10 | 2026-10-16 | 2026-10-22 | -0.27% | +0.49% | 13 |
| **GDX** | -6.86% | -1.18σ | 87.71 | 81.69 | 2026-10-16 | 2026-10-22 | +1.85% | +7.37% | 13 |
| **XLRE** | +0.85% | +1.03σ | 42.16 | 42.52 | 2026-10-16 | 2026-10-22 | -0.56% | +1.37% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-10-25 · **Conditions matched:** 3/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | +0.46% | ❌ | 161.76 | 162.51 | 2026-10-16 | 2026-10-22 |
| DFEN | down ≥ 3.0% | -6.58% | ✅ | 48.02 | 44.86 | 2026-10-16 | 2026-10-22 |
| GLD | down ≥ 1.0% | -3.41% | ✅ | 382.01 | 369.00 | 2026-10-16 | 2026-10-22 |
| URA | down ≥ 3.0% | -3.78% | ✅ | 35.43 | 34.09 | 2026-10-16 | 2026-10-22 |
| UUP | up ≥ 0.5% | -0.07% | ❌ | 28.92 | 28.90 | 2026-10-16 | 2026-10-22 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — 🔔 ТРИГГЕРИРАН
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-10-25 · **Conditions matched:** 4/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | +2.30% | ✅ | 270.44 | 276.67 | 2026-10-16 | 2026-10-22 |
| XLF | up ≥ 1.0% | +2.04% | ✅ | 55.52 | 56.65 | 2026-10-16 | 2026-10-22 |
| XLY | up ≥ 1.0% | +2.27% | ✅ | 112.46 | 115.01 | 2026-10-16 | 2026-10-22 |
| GLD | down ≥ 0.5% | -3.41% | ✅ | 382.01 | 369.00 | 2026-10-16 | 2026-10-22 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2025-W22 (week ending 2025-06-01)
**Cosine similarity:** 0.6919 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.79% | +9.44% | +15.95% |
| **USO** | +10.10% | +11.45% | +5.84% |
| **GLD** | +1.30% | +4.77% | +27.76% |
| **TLT** | +2.16% | +0.37% | +4.55% |
| **XLE** | +4.82% | +10.87% | +10.94% |
| **IWM** | +6.31% | +14.68% | +21.30% |

### Паралел #2: 2024-W48 (week ending 2024-12-01)
**Cosine similarity:** 0.5955 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -2.73% | -1.39% | -2.18% |
| **USO** | +5.50% | +5.04% | -6.23% |
| **GLD** | -1.41% | +7.20% | +23.62% |
| **TLT** | -7.07% | -1.64% | -8.18% |
| **XLE** | -10.33% | -4.74% | -14.66% |
| **IWM** | -8.65% | -11.25% | -15.21% |

### Паралел #3: 2025-W09 (week ending 2025-03-02)
**Cosine similarity:** 0.5884 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -5.59% | -0.81% | +8.56% |
| **USO** | +2.47% | -10.73% | -0.51% |
| **GLD** | +9.23% | +15.32% | +20.82% |
| **TLT** | -1.02% | -6.65% | -6.31% |
| **XLE** | +3.30% | -10.41% | -0.67% |
| **IWM** | -7.05% | -4.46% | +9.56% |

### Паралел #4: 2025-W33 (week ending 2025-08-17)
**Cosine similarity:** 0.5839 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.57% | +4.43% | +5.95% |
| **USO** | +3.94% | -1.95% | +4.70% |
| **GLD** | +10.46% | +22.29% | +50.48% |
| **TLT** | +4.57% | +2.86% | +3.84% |
| **XLE** | +4.93% | +7.55% | +27.05% |
| **IWM** | +4.91% | +4.56% | +15.78% |

### Паралел #5: 2022-W43 (week ending 2022-10-30)
**Cosine similarity:** 0.5407 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.60% | +4.28% | +6.92% |
| **USO** | -6.15% | -4.56% | -7.31% |
| **GLD** | +6.25% | +17.01% | +20.66% |
| **TLT** | +5.35% | +10.24% | +9.98% |
| **XLE** | +1.62% | +2.22% | -4.62% |
| **IWM** | -0.43% | +3.51% | -4.35% |

### Паралел #6: 2023-W49 (week ending 2023-12-10)
**Cosine similarity:** 0.5290 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.97% | +11.20% | +16.04% |
| **USO** | +1.29% | +10.27% | +9.75% |
| **GLD** | +1.23% | +8.61% | +13.98% |
| **TLT** | +2.20% | +1.26% | -3.22% |
| **XLE** | +0.16% | +7.22% | +9.44% |
| **IWM** | +4.37% | +10.72% | +7.71% |

### Паралел #7: 2024-W34 (week ending 2024-08-25)
**Cosine similarity:** 0.5046 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.63% | +5.94% | +6.73% |
| **USO** | -2.99% | -1.72% | -0.26% |
| **GLD** | +6.06% | +7.68% | +16.69% |
| **TLT** | +0.26% | -8.13% | -8.92% |
| **XLE** | -1.65% | +7.61% | +0.60% |
| **IWM** | +0.34% | +8.34% | -1.17% |

### Паралел #8: 2023-W50 (week ending 2023-12-17)
**Cosine similarity:** 0.4978 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.19% | +8.63% | +15.65% |
| **USO** | +0.15% | +13.67% | +13.30% |
| **GLD** | +0.49% | +6.80% | +15.36% |
| **TLT** | -4.37% | -6.26% | -4.52% |
| **XLE** | -4.26% | +8.61% | +4.44% |
| **IWM** | -3.15% | +2.73% | +0.86% |

### Паралел #9: 2024-W30 (week ending 2024-07-28)
**Cosine similarity:** 0.4927 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.14% | +6.36% | +11.67% |
| **USO** | +0.50% | -2.47% | +4.59% |
| **GLD** | +5.78% | +14.82% | +15.87% |
| **TLT** | +5.36% | -0.91% | -6.20% |
| **XLE** | -2.00% | -2.63% | -0.95% |
| **IWM** | -2.44% | -2.38% | +1.99% |

### Паралел #10: 2026-W12 (week ending 2026-03-22)
**Cosine similarity:** 0.4849 · **Common symbols:** 10/10

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
**Episodes:** 16 · **Total matching days:** 93 · **History:** 2021-05-17 → 2026-10-22

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.1% | +2.2% | -3.1% | +7.4% | 75% |
| **SPY** | 3m | 16 | +2.5% | +2.5% | -7.3% | +12.0% | 81% |
| **SPY** | 6m | 16 | +6.7% | +8.0% | -6.8% | +21.8% | 81% |
| **USO** | 1m | 16 | +0.1% | -0.2% | -14.3% | +12.7% | 50% |
| **USO** | 3m | 16 | +0.3% | +0.3% | -18.9% | +30.5% | 56% |
| **USO** | 6m | 16 | +14.4% | +3.4% | -8.7% | +109.4% | 69% |
| **GLD** | 1m | 16 | +2.3% | +0.8% | -3.4% | +9.0% | 69% |
| **GLD** | 3m | 16 | +4.2% | +3.4% | -12.6% | +24.5% | 62% |
| **GLD** | 6m | 16 | +4.4% | +3.4% | -12.5% | +25.3% | 62% |
| **TLT** | 1m | 16 | -1.4% | -1.1% | -6.7% | +3.6% | 38% |
| **TLT** | 3m | 16 | -0.5% | +0.5% | -16.5% | +11.1% | 56% |
| **TLT** | 6m | 16 | -3.7% | -2.8% | -18.0% | +7.5% | 38% |

**Episodes (последни 5 от 16):**
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-08-03` (5d)
- `2026-09-10 → 2026-10-01` (14d)
- `2026-10-16 → 2026-10-22` (5d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 113 · **History:** 2021-05-17 → 2026-10-22

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +6.3% | +6.3% | +3.5% | +9.1% | 100% |
| **SPY** | 3m | 2 | +6.9% | +6.9% | +3.5% | +10.3% | 100% |
| **SPY** | 6m | 2 | +8.3% | +8.3% | +1.6% | +15.0% | 100% |
| **USO** | 1m | 2 | +5.6% | +5.6% | +4.0% | +7.2% | 100% |
| **USO** | 3m | 2 | +8.7% | +8.7% | -9.9% | +27.4% | 50% |
| **USO** | 6m | 2 | +25.4% | +25.4% | +15.5% | +35.2% | 100% |
| **GLD** | 1m | 2 | +3.5% | +3.5% | -0.2% | +7.2% | 50% |
| **GLD** | 3m | 2 | -5.6% | -5.6% | -13.8% | +2.6% | 50% |
| **GLD** | 6m | 2 | -7.2% | -7.2% | -13.5% | -0.8% | 0% |
| **TLT** | 1m | 2 | -1.4% | -1.4% | -1.8% | -1.0% | 0% |
| **TLT** | 3m | 2 | -4.9% | -4.9% | -6.8% | -2.9% | 0% |
| **TLT** | 6m | 2 | -7.0% | -7.0% | -11.2% | -2.8% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-10-22` (66d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 469 · **History:** 2021-05-17 → 2026-10-22

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
- `2025-11-03 → 2026-10-22` (237d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 1 · **Total matching days:** 1 · **History:** 2021-05-17 → 2026-10-22

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | -1.0% | -1.0% | -1.0% | -1.0% | 0% |
| **SPY** | 3m | 1 | -1.0% | -1.0% | -1.0% | -1.0% | 0% |
| **SPY** | 6m | 1 | -1.0% | -1.0% | -1.0% | -1.0% | 0% |
| **USO** | 1m | 1 | +9.6% | +9.6% | +9.6% | +9.6% | 100% |
| **USO** | 3m | 1 | +9.6% | +9.6% | +9.6% | +9.6% | 100% |
| **USO** | 6m | 1 | +9.6% | +9.6% | +9.6% | +9.6% | 100% |
| **GLD** | 1m | 1 | -6.2% | -6.2% | -6.2% | -6.2% | 0% |
| **GLD** | 3m | 1 | -6.2% | -6.2% | -6.2% | -6.2% | 0% |
| **GLD** | 6m | 1 | -6.2% | -6.2% | -6.2% | -6.2% | 0% |
| **TLT** | 1m | 1 | +3.1% | +3.1% | +3.1% | +3.1% | 100% |
| **TLT** | 3m | 1 | +3.1% | +3.1% | +3.1% | +3.1% | 100% |
| **TLT** | 6m | 1 | +3.1% | +3.1% | +3.1% | +3.1% | 100% |

**Episodes (последни 5 от 1):**
- `2026-09-25 → 2026-09-25` (1d)

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 10 · **Total matching days:** 101 · **History:** 2021-05-17 → 2026-10-22

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 10 | -0.1% | +0.6% | -7.2% | +7.8% | 60% |
| **SPY** | 3m | 10 | +1.9% | +1.9% | -8.3% | +11.6% | 60% |
| **SPY** | 6m | 10 | +1.1% | +3.2% | -20.8% | +14.2% | 70% |
| **USO** | 1m | 10 | +4.1% | +0.5% | -15.0% | +52.9% | 50% |
| **USO** | 3m | 10 | +11.2% | +12.2% | -20.7% | +52.2% | 60% |
| **USO** | 6m | 10 | +13.5% | +9.9% | -27.6% | +56.3% | 60% |
| **GLD** | 1m | 10 | -1.2% | -1.9% | -8.3% | +11.7% | 20% |
| **GLD** | 3m | 10 | -1.9% | -1.4% | -12.0% | +6.4% | 40% |
| **GLD** | 6m | 10 | -1.3% | -3.7% | -15.2% | +25.0% | 30% |
| **TLT** | 1m | 10 | -2.4% | -2.7% | -6.0% | +2.5% | 10% |
| **TLT** | 3m | 10 | -5.9% | -4.9% | -17.6% | +4.2% | 20% |
| **TLT** | 6m | 10 | -9.2% | -8.1% | -22.3% | +1.2% | 10% |

**Episodes (последни 5 от 10):**
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-05-19` (36d)
- `2026-07-22 → 2026-08-03` (8d)
- `2026-09-01 → 2026-09-28` (15d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 17 · **Total matching days:** 294 · **History:** 2021-05-17 → 2026-10-22

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 17 | +1.9% | +1.6% | -4.8% | +9.0% | 71% |
| **SPY** | 3m | 17 | +3.0% | +4.2% | -12.6% | +16.2% | 71% |
| **SPY** | 6m | 17 | +6.4% | +8.1% | -14.0% | +21.0% | 76% |
| **USO** | 1m | 17 | +2.4% | -2.2% | -13.0% | +22.9% | 41% |
| **USO** | 3m | 17 | +4.1% | -0.8% | -14.5% | +37.7% | 41% |
| **USO** | 6m | 17 | +14.9% | +2.6% | -12.4% | +87.1% | 71% |
| **GLD** | 1m | 17 | +2.4% | +2.1% | -5.6% | +9.0% | 76% |
| **GLD** | 3m | 17 | +5.5% | +7.2% | -16.8% | +23.6% | 65% |
| **GLD** | 6m | 17 | +10.0% | +9.8% | -14.1% | +43.8% | 71% |
| **TLT** | 1m | 17 | +0.3% | -0.0% | -6.3% | +8.2% | 47% |
| **TLT** | 3m | 17 | -1.5% | -1.2% | -15.3% | +11.9% | 35% |
| **TLT** | 6m | 17 | -4.6% | -1.7% | -21.3% | +7.0% | 35% |

**Episodes (последни 5 от 17):**
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)
- `2026-08-07 → 2026-09-03` (19d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 20 · **Total matching days:** 304 · **History:** 2021-05-17 → 2026-10-22

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 20 | +0.3% | +0.5% | -8.7% | +7.0% | 50% |
| **SPY** | 3m | 20 | +1.9% | +3.2% | -13.7% | +9.1% | 65% |
| **SPY** | 6m | 20 | +3.1% | +5.2% | -16.4% | +16.9% | 70% |
| **USO** | 1m | 20 | -0.2% | -3.7% | -21.8% | +55.8% | 45% |
| **USO** | 3m | 20 | +4.2% | +1.5% | -12.7% | +64.3% | 50% |
| **USO** | 6m | 20 | +9.6% | +5.1% | -16.0% | +75.1% | 55% |
| **GLD** | 1m | 20 | -0.8% | -0.2% | -12.4% | +7.6% | 45% |
| **GLD** | 3m | 20 | +1.4% | +1.5% | -13.7% | +19.0% | 65% |
| **GLD** | 6m | 20 | +6.9% | +4.3% | -15.8% | +55.5% | 65% |
| **TLT** | 1m | 20 | -0.2% | -0.1% | -5.6% | +5.2% | 45% |
| **TLT** | 3m | 20 | -3.4% | -3.9% | -17.3% | +8.7% | 30% |
| **TLT** | 6m | 20 | -6.5% | -5.6% | -21.4% | +4.6% | 20% |

**Episodes (последни 5 от 20):**
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (13d)
- `2026-09-21 → 2026-10-15` (16d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-10-22

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (10 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **COMPUTSA** | Завършени жилища (SAAR) | growth | housing_supply | 6 | 2.95 | 2.95 | 2026-09-19 00:00:00 | 2026-10-17 00:00:00 | ✓ |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 6 | 2.75 | 2.75 | 2026-09-19 00:00:00 | 2026-10-17 00:00:00 | ✓ |
| **JTSQUR** | Quits rate — напускания | labor | flow | 6 | 2.02 | 2.02 | 2026-09-19 00:00:00 | 2026-10-17 00:00:00 | ✓ |
| **US_PMI_COMPOSITE** | S&P Global US Composite PMI | growth | diffusion_indices | 3 | 2.60 | 2.60 | 2026-10-07 00:00:00 | 2026-10-17 00:00:00 | ✓ |
| **US_PMI_SVCS** | S&P Global US Services PMI | growth | diffusion_indices | 3 | 2.09 | 2.09 | 2026-10-07 00:00:00 | 2026-10-17 00:00:00 | ✓ |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 3 | 2.07 | 2.07 | 2026-10-07 00:00:00 | 2026-10-17 00:00:00 | ✓ |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 3 | 2.06 | 2.06 | 2026-10-03 00:00:00 | 2026-10-10 00:00:00 | - |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | 2 | 2.25 | 2.25 | 2026-09-19 00:00:00 | 2026-09-26 00:00:00 | - |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 1 | 2.43 | 2.43 | 2026-10-17 00:00:00 | 2026-10-17 00:00:00 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | 1 | 2.06 | 2.06 | 2026-10-17 00:00:00 | 2026-10-17 00:00:00 | - |

### EU (5 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.47 | 5.60 | 2026-09-19 00:00:00 | 2026-10-17 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.24 | 2.45 | 2026-09-19 00:00:00 | 2026-10-17 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.16 | 2.25 | 2026-09-19 00:00:00 | 2026-10-17 00:00:00 | ✓ |
| **EA_OAT_BUND_SPREAD** | OAT-Bund spread (FR-DE 10Y, pp) | credit | sovereign_spreads | 1 | 2.48 | 2.48 | 2026-10-17 00:00:00 | 2026-10-17 00:00:00 | ✓ |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | 1 | 2.18 | 2.18 | 2026-10-17 00:00:00 | 2026-10-17 00:00:00 | - |

### CN (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 9 | 2.54 | 2.54 | 2026-09-21 00:00:00 | 2026-10-19 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 9 | 2.22 | 2.23 | 2026-09-21 00:00:00 | 2026-10-19 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 4 | 2.19 | 2.19 | 2026-10-10 00:00:00 | 2026-10-19 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-10-17 00:00:00 · **Generated:** 2026-10-17 06:57:24.713375+00:00

**Режим:** `policy_dilemma` (Policy dilemma)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 39.7 | mixed | 33.3% | 2 | 2 |
| **growth** | 48.7 | mixed | 56.0% | 4 | 4 |
| **inflation** | 38.4 | mixed | 33.3% | 3 | 1 |
| **liquidity** | 45.2 | mixed | 26.3% | 0 | 0 |

### Top anomalies (8 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **COMPUTSA** | Завършени жилища (SAAR) | growth, housing | housing_supply | -2.95 | down | -27.13 | 2026-08-01 | ✓ min |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.75 | down | 93.45 | 2026-04-01 | ✓ min |
| **US_PMI_COMPOSITE** | S&P Global US Composite PMI | growth | diffusion_indices | +2.60 | up | 58.40 | 2026-09-01 | ✓ max |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | +2.43 | up | 6.35 | 2026-09-01 | - |
| **US_PMI_SVCS** | S&P Global US Services PMI | growth | diffusion_indices | +2.09 | up | 58.80 | 2026-09-01 | ✓ max |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | +2.07 | up | 55.90 | 2026-09-01 | ✓ max |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | +2.06 | up | 5.08 | 2026-09-01 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | -2.02 | down | 1.90 | 2026-08-01 | ✓ min |

### Narrative hints от макро лещите
- **COMPUTSA**: Завършва construction pipeline (12-18m след starts). Превишение спрямо sales = inventory build.
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **US_PMI_COMPOSITE**: Markit композит — global benchmark, complement към ISM. Flash + final estimates.
- **PPIFIS**: Производствени цени → consumer prices с 1-3 месечен lag. Водещ за CPI при трендови промени.
- **US_PMI_SVCS**: Markit services — global comparable. ISM Services има различна methodology.
- **US_PMI_MFG**: Markit mfg — comparable cross-country. ISM е US-only.
- **CPI_GOODS**: Goods inflation реагира бързо на supply shocks. 2022 peak след доставъчните кризи. Сега често е в deflation/близо до 0.
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
  - `breadth_b`: 1.0
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
  - `breadth_b`: 0.333
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 0.8
  - `breadth_b_raw`: 0.333
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Realized CPI × Expectations
  - `question_bg`: Дали expectations следват realized inflation, или стоят anchored?
  - `state`: both_up
  - `interpretation`: De-anchoring in progress — expectations следват realized up.
  - `slot_a_label`: Realized inflation
  - `slot_b_label`: Inflation expectations
  - `breadth_a`: 1.0
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
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
  - `state`: both_up
  - `interpretation`: Съгласие — underlying persistent + пазар pricing-ва inflation. Fed зад кривата.
  - `slot_a_label`: Модел (sticky inflation)
  - `slot_b_label`: Пазар (breakevens + survey)
  - `breadth_a`: 1.0
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.667

### Executive narrative
> Policy dilemma — labor market е loose, но инфлацията remains hot. Fed е заклещен между двата мандата. Най-отклонена леща: Инфлация и цени — breadth 88% (разширяване), 3 аномалии, 1 нови екстремума. Expectations също нагоре — de-anchoring в ход, рискът ескалира. За наблюдение следващия релиз: COMPUTSA, LABOR_SHARE_NBS, US_PMI_COMPOSITE (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: COMPUTSA z=-2.95 · NEW-5Y-MIN
- 6 нови екстремуми в top-8 (lookback 5г.)
- Активни двойки: Stagflation test=a_down_b_up; Inflation anchoring=both_up; Credit × Policy=a_down_b_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-10-17 00:00:00 · **Generated:** 2026-10-17 07:11:44.978209+00:00

**Режим:** `policy_dilemma` (Policy dilemma)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 41.1 | mixed | 42.9% | 0 | 0 |
| **growth** | 44.5 | mixed | 25.0% | 0 | 0 |
| **inflation** | 43.2 | mixed | 42.9% | 0 | 0 |
| **credit** | 42.9 | mixed | 36.8% | 4 | 3 |
| **external** | 57.8 | mixed | 50.0% | 1 | 0 |

### Top anomalies (5 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | +5.60 | up | 3.30 | 2026-09-01 | - |
| **EA_OAT_BUND_SPREAD** | OAT-Bund spread (FR-DE 10Y, pp) | credit | sovereign_spreads | +2.48 | up | 0.97 | 2026-09-01 | ✓ max |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | +2.45 | up | 4.44 | 2026-09-01 | ✓ max |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | +2.25 | up | 3.47 | 2026-09-01 | ✓ max |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | -2.18 | down | -6826.60 | 2026-08-01 | - |

### Narrative hints от макро лещите
- **EA_BUND_2Y**: EA-aggregate 2Y yield. Curve slope (10Y-2Y) проксира policy expectations и recession risk.
- **EA_OAT_BUND_SPREAD**: Core-but-not-DE EA stress proxy. Captures France-specific stress (e.g., 2024 budget crisis).
- **FR_10Y**: France sovereign yield — компонент на OAT-Bund spread. Core-but-not-DE EA stress indicator.
- **DE_10Y**: Germany 10Y, Maastricht-criterion measure. Reference за BTP-Bund / OAT-Bund spread изчисления.
- **EA_TRADE_BALANCE**: Стоковият баланс с третите страни. Срив към дефицит (2022) = енергийната сметка изпреварва износа. Полярност +1.

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
  - `state`: both_up
  - `interpretation`: Fragmentation risk: hike-овете разширяват periphery spreads. Ако упорства — TPI activation candidate. 2011-2012 patron.
  - `slot_a_label`: Политика (реална лихва + баланс)
  - `slot_b_label`: Sovereign spreads (BTP/OAT-Bund)
  - `breadth_a`: 1.0
  - `breadth_b`: 1.0
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 1.0
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
> Policy dilemma — labor market е loose, но инфлацията remains hot. ЕЦБ е заклещена между инфлацията и растежа. Най-отклонена леща: Инфлация и цени — breadth 100% (разширяване), 0 аномалии, 0 нови екстремума. За наблюдение следващия релиз: EA_OAT_BUND_SPREAD, FR_10Y, DE_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.60
- 3 нови екстремуми в top-5 (lookback 5г.)
- Активни двойки: Stagflation test=a_down_b_up; fragmentation_risk=both_up



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-10-19 00:00:00 · **Generated:** 2026-10-19 11:24:28.391025+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 43.2 | mixed | -% | - | - |
| **inflation** | 41.7 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 45.7 | mixed | -% | - | - |
| **property** | 31.1 | contracting | -% | - | - |

### Top anomalies (3 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | -2.54 | down | 3.00 | 2026-09-20 | ✓ min |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | +2.23 | up | 15.79 | 2025-12-31 | ✓ max |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | -2.19 | down | 1.68 | 2026-09-30 | - |

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
  - `state`: both_up
  - `interpretation`: Балансиран растеж — и износ, и вътрешно търсене се разширяват.
  - `slot_a_label`: Външно търсене
  - `slot_b_label`: Вътрешна активност
  - `breadth_a`: 0.667
  - `breadth_b`: 0.667

### Executive narrative
> Претеглен композитен macro score 38.7/100 → режим „ВЛОШАВАЩ СЕ“ (5/5 лещи). 5 лещи, 3 flagged аномалии (3 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-10-16 |
| `as_of` | 2026-10-16 |
| `regime` | GROWTH |
| `alignment_score` | 3.0 |
| `gms_score` | 2.0 |
| `gms_max` | 8 |
| `gms_tier` | LOW |
| `ks_status` | inactive |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-10-16 → 2026-10-21)

**stable_winner (1m):** +13 entered, -7 exited
  - **Entered:** BIIB, CFG, DAL, EQIX, FIX, HLT, INCY, MAR, MPC, STLD, STT, VTRS, WBD
  - **Exited:** AIZ, F, FDX, HAS, SATS, VTR, WELL

**stable_winner (3m):** +8 entered, -4 exited
  - **Entered:** EQIX, ETR, HLT, HST, IBKR, IVZ, MAR, MPC _(включително 1 за първи път в историята: MPC)_
  - **Exited:** ADM, EBAY, F, USB

**quality_dip (1m):** +7 entered, -12 exited
  - **Entered:** AIZ, F, FDX, HAS, SATS, VTR, WELL
  - **Exited:** BIIB, CFG, DAL, EQIX, FIX, HLT, INCY, MAR, STLD, STT, VTRS, WBD

**quality_dip (3m):** +4 entered, -7 exited
  - **Entered:** ADM, EBAY, F, USB
  - **Exited:** EQIX, ETR, HLT, HST, IBKR, IVZ, MAR

**faded_bounce (1m):** +10 entered, -7 exited
  - **Entered:** APTV, BLDR, COIN, EXE, FISV, KMI, LII, OTIS, SHW, XYL _(включително 3 за първи път в историята: APTV, KMI, XYL)_
  - **Exited:** BAX, DXCM, ERIE, FDS, GIS, JKHY, NFLX

**faded_bounce (3m):** +4 entered, -4 exited
  - **Entered:** BR, BX, CEG, NKE
  - **Exited:** AMCR, EQT, ERIE, PGR

### EU (period: 2026-10-16 → 2026-10-22)

**stable_winner (1m):** +24 entered, -13 exited
  - **Entered:** AAL.L, ABBN.SW, ABI.BR, ANTO.L, BAMI.MI, BBY.L, BG.VI, BIRG.IR, CA.PA, FRES.L, GLE.PA, HOC.L, HUBN.SW, ISS.CO, MBK.WA, NDX1.DE, PAF.L, PRY.MI, SGRO.L, SSE.L, TPRO.MI, VACN.SW, VOE.VI, ZAB.WA _(включително 4 за първи път в историята: AAL.L, ABI.BR, SGRO.L, ZAB.WA)_
  - **Exited:** AAF.L, CABK.MC, DANSKE.CO, DLG.MI, GLEN.L, JYSK.CO, LOTB.BR, RBI.VI, SAND.ST, STMMI.MI, TIT.MI, VWS.CO, WRT1V.HE

**stable_winner (3m):** +5 entered, -4 exited
  - **Entered:** HOC.L, LPP.WA, SGRO.L, VACN.SW, ZAB.WA _(включително 2 за първи път в историята: SGRO.L, ZAB.WA)_
  - **Exited:** CPG.L, DANSKE.CO, DLG.MI, PKN.WA

**quality_dip (1m):** +13 entered, -23 exited
  - **Entered:** AAF.L, CABK.MC, DANSKE.CO, DLG.MI, GLEN.L, JYSK.CO, LOTB.BR, RBI.VI, SAND.ST, STMMI.MI, TIT.MI, VWS.CO, WRT1V.HE
  - **Exited:** AAL.L, ABBN.SW, ABI.BR, ANTO.L, BAMI.MI, BBY.L, BESI.AS, BG.VI, BIRG.IR, CA.PA, FRES.L, GLE.PA, HOC.L, HUBN.SW, ISS.CO, MBK.WA, NDX1.DE, PAF.L, PRY.MI, SSE.L, TPRO.MI, VACN.SW, VOE.VI

**quality_dip (3m):** +4 entered, -4 exited
  - **Entered:** CPG.L, DANSKE.CO, DLG.MI, PKN.WA
  - **Exited:** BESI.AS, HOC.L, LPP.WA, VACN.SW

**faded_bounce (1m):** +7 entered, -13 exited
  - **Entered:** BPT.L, BTRW.L, EVD.DE, HNR1.DE, NEM.DE, R3NK.DE, UMG.AS _(включително 1 за първи път в историята: R3NK.DE)_
  - **Exited:** BALD-B.ST, BEI.DE, CAP.PA, DB1.DE, ENX.PA, EXPN.L, IMCD.AS, LIFCO-B.ST, PNN.L, REL.L, TEP.PA, WKL.AS, WPP.L

**faded_bounce (3m):** +4 entered, -8 exited
  - **Entered:** BEIJ-B.ST, G24.DE, SQN.SW, WIE.VI
  - **Exited:** BOL.PA, ENX.PA, HER.MI, IMCD.AS, PNN.L, RI.PA, SREN.SW, WISE.L



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-10-13 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **soymeal** | Commodities | 206131 | 99.8 | 99.8 | 1062 | 20585 |
| **sugar** | Commodities | 261841 | 98.5 | 98.5 | 1062 | 25553 |
| **soybeans** | Commodities | 237491 | 98.3 | 98.3 | 1062 | -7219 |
| **rbob** | Commodities | 97646 | 96.8 | 96.8 | 1062 | 14429 |
| **soyoil** | Commodities | 89328 | 91.8 | 91.8 | 1062 | -21566 |
| **copper** | Commodities | 61170 | 89.2 | 89.2 | 1062 | -4371 |
| **vix** | Volatility | 1105 | 83.7 | 83.7 | 1021 | 17609 |
| **cotton** | Commodities | 65699 | 83.7 | 83.7 | 1062 | -32204 |
| **aud** | FX | 50591 | 82.8 | 82.8 | 1062 | -10544 |
| **corn** | Commodities | 230877 | 76.4 | 76.4 | 1062 | -195965 |
| **dxy** | FX | 2076 | 64.0 | 64.0 | 1062 | 6985 |
| **gbpfx** | FX | 10313 | 48.5 | 48.5 | 1062 | -8565 |
| **coffee** | Commodities | 10267 | 47.6 | 47.6 | 1062 | -5387 |
| **jpy** | FX | -33673 | 47.1 | 47.1 | 1062 | -56843 |
| **gold** | Commodities | 111079 | 46.3 | 46.3 | 1062 | -25981 |
| **heatingoil** | Commodities | 11754 | 45.0 | 45.0 | 1062 | -1714 |
| **nasdaq** | US Equities | -11593 | 44.8 | 44.8 | 1062 | -5206 |
| **cattle** | Commodities | 48748 | 42.0 | 42.0 | 1062 | 3486 |
| **bitcoin** | Crypto | -5844 | 40.0 | 40.0 | 445 | 510 |
| **wheat** | Commodities | -33038 | 39.6 | 39.6 | 1062 | -28332 |
| **platinum** | Commodities | 7022 | 35.0 | 35.0 | 1062 | -2160 |
| **us30y** | Rates | -154020 | 34.8 | 34.8 | 1062 | 57715 |
| **brent** | Commodities | 1427 | 31.8 | 31.8 | 245 | -5814 |
| **eurfx** | FX | -68001 | 23.8 | 23.8 | 1062 | -39845 |
| **wti** | Commodities | 102765 | 21.2 | 21.2 | 1062 | -34003 |
| **sp500** | US Equities | -408726 | 19.9 | 19.9 | 1062 | -115583 |
| **silver** | Commodities | 5735 | 18.2 | 18.2 | 1062 | -6897 |
| **us2y** | Rates | -1367408 | 16.1 | 16.1 | 1062 | -72833 |
| **chf** | FX | -14941 | 13.0 | 13.0 | 1062 | 23 |
| **russell** | US Equities | -91647 | 12.5 | 12.5 | 598 | 5556 |
| **natgas** | Commodities | -126156 | 12.3 | 12.3 | 1062 | -26132 |
| **cocoa** | Commodities | -14377 | 12.2 | 12.2 | 1062 | -1932 |
| **us5y** | Rates | -2104391 | 11.9 | 11.9 | 1062 | -117463 |
| **usultra10y** | Rates | -335858 | 9.8 | 9.8 | 552 | 63388 |
| **palladium** | Commodities | -10860 | 3.8 | 3.8 | 1062 | -5222 |
| **us10y** | Rates | -2205937 | 2.5 | 2.5 | 1062 | -337811 |
| **cad** | FX | -88112 | 1.5 | 1.5 | 1062 | -49090 |
| **hogs** | Commodities | -42088 | 0.2 | 0.2 | 1062 | -10687 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MRNA** | Healthcare | 97.6 | 34.6% | 331.1% | 342.1% | 570.2% | 1.68 | -34.2% |
| 2 | **MPC** | Energy | 96.9 | 20.1% | 50.3% | 112.1% | 112.7% | 2.51 | -18.3% |
| 3 | **VLO** | Energy | 96.8 | 15.8% | 43.6% | 88.0% | 140.4% | 2.63 | -12.1% |
| 4 | **ILMN** | Healthcare | 96.1 | 14.3% | 43.7% | 116.8% | 148.7% | 2.08 | -25.7% |
| 5 | **PSX** | Energy | 95.6 | 13.0% | 40.9% | 82.8% | 102.8% | 2.49 | -17.3% |
| 6 | **TWLO** | Technology | 94.6 | -6.3% | 44.1% | 77.2% | 161.0% | 1.38 | -24.7% |
| 7 | **CRWD** | Technology | 93.1 | -4.3% | 30.5% | 105.1% | 98.6% | 1.09 | -37.2% |
| 8 | **HPE** | Technology | 93.0 | -4.7% | 22.4% | 105.2% | 171.7% | 1.58 | -26.4% |
| 9 | **DELL** | Technology | 90.5 | -11.4% | 10.8% | 127.0% | 275.9% | 1.59 | -32.3% |
| 10 | **NTAP** | Technology | 90.5 | 12.8% | 32.2% | 96.7% | 66.7% | 1.33 | -24.8% |
| 11 | **CRL** | Healthcare | 90.4 | 21.0% | 50.4% | 86.6% | 54.8% | 1.27 | -33.9% |
| 12 | **MRVL** | Technology | 90.2 | -6.7% | 17.0% | 55.6% | 206.1% | 1.29 | -48.4% |
| 13 | **FTNT** | Technology | 90.1 | -0.1% | 14.8% | 99.8% | 105.3% | 1.59 | -14.3% |
| 14 | **APA** | Energy | 88.9 | 17.3% | 36.3% | 31.3% | 94.6% | 1.74 | -27.7% |
| 15 | **RVTY** | Healthcare | 88.1 | 9.3% | 38.4% | 66.1% | 50.6% | 1.17 | -30.1% |
| 16 | **AMD** | Technology | 86.1 | -11.4% | 2.4% | 82.1% | 159.3% | 1.17 | -27.8% |
| 17 | **CNC** | Healthcare | 85.8 | 11.0% | 10.2% | 80.4% | 77.8% | 1.34 | -32.7% |
| 18 | **MRK** | Healthcare | 85.8 | -0.7% | 15.6% | 34.5% | 80.0% | 1.84 | -11.4% |
| 19 | **PANW** | Technology | 85.0 | -7.3% | 6.6% | 91.6% | 76.8% | 0.92 | -36.0% |
| 20 | **DDOG** | Technology | 84.1 | 10.3% | 11.7% | 106.7% | 58.3% | 0.75 | -48.6% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MOH.AT** | Energy | 95.1 | 4.3% | 32.8% | 99.7% | 168.0% | 3.09 | -12.1% |
| 2 | **MAERSK-B.CO** | Industrials | 92.3 | 2.4% | 40.6% | 60.4% | 94.0% | 1.68 | -22.9% |
| 3 | **FRO.OL** | Energy | 90.4 | -2.8% | 27.9% | 51.7% | 110.7% | 1.62 | -20.5% |
| 4 | **ALE.WA** | Consumer Cyclical | 87.3 | 16.8% | 28.6% | 92.3% | 46.5% | 1.74 | -28.9% |
| 5 | **REP.MC** | Energy | 84.9 | -0.8% | 9.8% | 42.4% | 102.2% | 2.00 | -20.4% |
| 6 | **BME.L** | Consumer Cyclical | 84.9 | 13.4% | 30.7% | 61.2% | 43.2% | 1.12 | -41.2% |
| 7 | **DEMANT.CO** | Healthcare | 84.8 | 18.4% | 34.5% | 63.6% | 36.4% | 1.35 | -26.8% |
| 8 | **VAR.OL** | Energy | 84.2 | 7.9% | 17.1% | 32.3% | 82.3% | 1.76 | -19.4% |
| 9 | **ABN.AS** | Financial Services | 83.9 | -8.2% | 10.1% | 40.9% | 86.8% | 1.90 | -18.0% |
| 10 | **TKA.DE** | Basic Materials | 83.7 | -5.8% | 16.5% | 57.3% | 64.5% | 0.75 | -41.4% |
| 11 | **EBP.WA** | Financial Services | 83.5 | -3.2% | 16.3% | 30.4% | 78.2% | 1.90 | -10.9% |
| 12 | **OMV.VI** | Energy | 83.4 | 4.2% | 13.7% | 36.1% | 68.5% | 2.33 | -10.8% |
| 13 | **BFT.WA** | Industrials | 83.4 | 11.2% | 12.3% | 49.4% | 59.3% | 1.96 | -17.4% |
| 14 | **DSFIR.AS** | Basic Materials | 83.3 | 13.9% | 33.3% | 73.4% | 29.7% | 1.18 | -27.4% |
| 15 | **VONN.SW** | Financial Services | 82.9 | -1.9% | 12.6% | 37.6% | 62.8% | 2.47 | -6.0% |
| 16 | **LOTB.BR** | Consumer Defensive | 82.8 | 5.6% | 23.4% | 32.4% | 52.5% | 1.82 | -11.9% |
| 17 | **ATS.VI** | Technology | 82.6 | -14.0% | -4.5% | 64.9% | 544.8% | 1.99 | -50.1% |
| 18 | **EMSN.SW** | Basic Materials | 81.7 | 6.9% | 16.1% | 37.0% | 49.2% | 2.19 | -8.0% |
| 19 | **CCC.L** | Technology | 81.7 | -10.3% | 1.8% | 43.2% | 106.4% | 1.67 | -16.2% |
| 20 | **OCTV-SDB.ST** | Technology | 81.5 | 12.3% | 30.4% | -% | -% | 1.32 | -20.5% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **EIX** | Utilities | 1.915 | 0.635 | 1.066 | 3.066 | -0.939 | - | 6.0 | +19.7% |
| 2 | **SNDK** | Information Technology | 1.742 | 1.915 | 1.548 | 0.983 | -0.118 | - | 17.1 | +91.6% |
| 3 | **CF** | Materials | 1.558 | 1.073 | 1.255 | 1.583 | 0.357 | - | 8.8 | +29.9% |
| 4 | **MU** | Information Technology | 1.367 | 1.452 | 1.229 | 0.803 | -0.486 | - | 12.3 | +88.3% |
| 5 | **MO** | Consumer Staples | 1.336 | 0.539 | 1.861 | 0.822 | -0.435 | - | 15.6 | - |
| 6 | **NEM** | Materials | 1.323 | 0.730 | 1.604 | 0.908 | 0.583 | - | 14.4 | +25.9% |
| 7 | **HST** | Real Estate | 1.247 | 1.879 | 0.481 | 0.959 | -0.337 | - | 16.8 | +15.6% |
| 8 | **APA** | Energy | 1.183 | 1.053 | 1.250 | 0.669 | -0.135 | - | 10.5 | +26.7% |
| 9 | **SPG** | Real Estate | 1.172 | 0.974 | 1.393 | 0.551 | -1.198 | - | 14.5 | +120.5% |
| 10 | **BMY** | Health Care | 1.162 | 0.963 | 0.878 | 1.107 | 0.580 | - | 13.9 | +46.6% |
| 11 | **SYF** | Financials | 1.158 | -0.172 | 1.178 | 1.755 | -0.085 | - | 7.7 | +20.8% |
| 12 | **TGT** | Consumer Staples | 1.079 | 2.652 | -0.096 | 0.503 | -0.699 | - | 16.4 | +26.4% |
| 13 | **DVA** | Health Care | 1.063 | 0.871 | 0.187 | 1.704 | -1.418 | - | 15.7 | +88.5% |
| 14 | **MAS** | Industrials | 1.048 | -0.128 | 1.460 | 1.129 | -0.735 | - | 18.0 | +5862.5% |
| 15 | **EXPE** | Consumer Discretionary | 0.969 | 1.358 | 0.784 | 0.383 | -0.671 | - | 17.8 | +89.5% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -2.039 | -1.701 | -0.936 | -2.561 | -0.955 |
| 502 | **CSGP** | Real Estate | -1.770 | -3.290 | -0.456 | -1.031 | 0.673 |
| 501 | **TSLA** | Consumer Discretionary | -1.764 | -0.449 | -1.385 | -2.469 | -0.395 |
| 500 | **BA** | Industrials | -1.674 | -0.671 | -1.207 | -2.247 | -1.073 |
| 499 | **XYZ** | Financials | -1.531 | -0.212 | -1.818 | -1.613 | -0.886 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W43.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W43.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\macro\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-10-19  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
