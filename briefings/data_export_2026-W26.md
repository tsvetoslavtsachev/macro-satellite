# Сателит — пълен data export за 2026-W26

_Период: 2026-06-22 → 2026-06-28_  
_Генериран: 2026-06-26 09:29 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W26.md` (structured briefing) и `narrative_2026-W26.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**15 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **SLV** | -12.01% | -2.39σ | 59.51 | 52.36 | 2026-06-19 | 2026-06-25 | -0.13% | +4.96% | 13 |
| **XLV** | +4.17% | +2.10σ | 149.40 | 155.63 | 2026-06-19 | 2026-06-25 | +0.26% | +1.86% | 13 |
| **QQQ** | -3.27% | -1.73σ | 740.62 | 716.38 | 2026-06-19 | 2026-06-25 | +1.93% | +3.00% | 13 |
| **GLD** | -4.56% | -1.61σ | 387.12 | 369.46 | 2026-06-19 | 2026-06-25 | -0.47% | +2.54% | 13 |
| **XLK** | -3.59% | -1.61σ | 191.44 | 184.57 | 2026-06-19 | 2026-06-25 | +2.79% | +3.96% | 13 |
| **EEM** | -4.00% | -1.58σ | 70.79 | 67.96 | 2026-06-19 | 2026-06-25 | +1.94% | +3.76% | 13 |
| **URA** | -8.08% | -1.56σ | 47.78 | 43.92 | 2026-06-19 | 2026-06-25 | +0.37% | +5.43% | 13 |
| **SPY** | -1.67% | -1.40σ | 746.74 | 734.30 | 2026-06-19 | 2026-06-25 | +1.11% | +1.98% | 13 |
| **SOXX** | -2.23% | -1.31σ | 639.45 | 625.20 | 2026-06-19 | 2026-06-25 | +5.32% | +5.77% | 13 |
| **GDX** | -8.29% | -1.29σ | 82.51 | 75.67 | 2026-06-18 | 2026-06-25 | +0.46% | +6.76% | 13 |
| **XLC** | -3.32% | -1.21σ | 109.20 | 105.58 | 2026-06-19 | 2026-06-25 | -0.15% | +2.62% | 13 |
| **UUP** | +1.06% | +1.19σ | 28.18 | 28.48 | 2026-06-19 | 2026-06-25 | +0.14% | +0.78% | 13 |
| **XLU** | +2.44% | +1.18σ | 44.76 | 45.85 | 2026-06-19 | 2026-06-25 | +0.09% | +1.98% | 13 |
| **VEA** | -1.59% | -1.08σ | 72.31 | 71.16 | 2026-06-18 | 2026-06-25 | +1.22% | +2.61% | 13 |
| **VWO** | -1.57% | -1.05σ | 59.74 | 58.80 | 2026-06-19 | 2026-06-25 | +1.02% | +2.47% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_5 канонични patterns от `config/divergence_rules.yaml`, evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — 🔔 ТРИГГЕРИРАН
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-06-28 · **Conditions matched:** 4/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | -4.84% | ❌ | 114.87 | 109.31 | 2026-06-19 | 2026-06-25 |
| DFEN | down ≥ 3.0% | -7.35% | ✅ | 80.72 | 74.79 | 2026-06-19 | 2026-06-25 |
| GLD | down ≥ 1.0% | -4.56% | ✅ | 387.12 | 369.46 | 2026-06-19 | 2026-06-25 |
| URA | down ≥ 3.0% | -8.08% | ✅ | 47.78 | 43.92 | 2026-06-19 | 2026-06-25 |
| UUP | up ≥ 0.5% | +1.06% | ✅ | 28.18 | 28.48 | 2026-06-19 | 2026-06-25 |

### Ликвидна стес (flight to quality) (`liquidity_stress`) — не активен
_Дългосрочни trezuri нагоре, високодоходен кредит надолу, злато нагоре. Класически risk-off._  
**Window:** 7d ending 2026-06-28 · **Conditions matched:** 1/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| TLT | up ≥ 1.0% | +0.69% | ❌ | 86.75 | 87.35 | 2026-06-19 | 2026-06-25 |
| HYG | down ≥ 0.5% | -0.16% | ❌ | 80.01 | 79.88 | 2026-06-19 | 2026-06-25 |
| GLD | up ≥ 1.0% | -4.56% | ❌ | 387.12 | 369.46 | 2026-06-19 | 2026-06-25 |
| UUP | up ≥ 0.3% | +1.06% | ✅ | 28.18 | 28.48 | 2026-06-19 | 2026-06-25 |

### Възстановяване на инфлационни очаквания (`inflation_pickup`) — не активен
_Inflation-protected треzuri нагоре, commodities нагоре, dollar надолу. Repricing на real rates._  
**Window:** 7d ending 2026-06-28 · **Conditions matched:** 0/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| DBC | up ≥ 1.5% | -2.81% | ❌ | 27.71 | 26.93 | 2026-06-19 | 2026-06-25 |
| GLD | up ≥ 1.0% | -4.56% | ❌ | 387.12 | 369.46 | 2026-06-19 | 2026-06-25 |
| UUP | down ≥ 0.5% | +1.06% | ❌ | 28.18 | 28.48 | 2026-06-19 | 2026-06-25 |
| TLT | down ≥ 1.0% | +0.69% | ❌ | 86.75 | 87.35 | 2026-06-19 | 2026-06-25 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-06-28 · **Conditions matched:** 1/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | +1.12% | ❌ | 295.59 | 298.91 | 2026-06-19 | 2026-06-25 |
| XLF | up ≥ 1.0% | -0.22% | ❌ | 53.57 | 53.45 | 2026-06-19 | 2026-06-25 |
| XLY | up ≥ 1.0% | -1.85% | ❌ | 115.49 | 113.35 | 2026-06-19 | 2026-06-25 |
| GLD | down ≥ 0.5% | -4.56% | ✅ | 387.12 | 369.46 | 2026-06-19 | 2026-06-25 |

### Защитен pivot (staples + utilities + gold) (`defensive_pivot`) — не активен
_XLP + XLU + GLD едновременно нагоре. Smart money flight to defensives без credit panic._  
**Window:** 7d ending 2026-06-28 · **Conditions matched:** 1/3

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| XLP | up ≥ 1.0% | +0.31% | ❌ | 83.68 | 83.94 | 2026-06-19 | 2026-06-25 |
| XLU | up ≥ 1.0% | +2.44% | ✅ | 44.76 | 45.85 | 2026-06-19 | 2026-06-25 |
| GLD | up ≥ 1.0% | -4.56% | ❌ | 387.12 | 369.46 | 2026-06-19 | 2026-06-25 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2022-W41 (week ending 2022-10-16)
**Cosine similarity:** 0.8133 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +11.43% | +11.94% | +16.30% |
| **USO** | +4.39% | -0.17% | +2.74% |
| **GLD** | +8.18% | +16.85% | +21.82% |
| **TLT** | +0.92% | +9.09% | +8.20% |
| **XLE** | +17.19% | +13.20% | +10.92% |
| **IWM** | +12.43% | +12.65% | +6.70% |

### Паралел #2: 2021-W47 (week ending 2021-11-28)
**Cosine similarity:** 0.7796 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.27% | -4.29% | -8.92% |
| **USO** | +10.16% | +32.58% | +72.19% |
| **GLD** | +1.07% | +5.81% | +3.60% |
| **TLT** | -1.26% | -8.73% | -20.23% |
| **XLE** | +2.17% | +25.53% | +62.89% |
| **IWM** | +0.26% | -8.86% | -15.38% |

### Паралел #3: 2024-W46 (week ending 2024-11-17)
**Cosine similarity:** 0.7390 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.17% | +4.44% | +2.09% |
| **USO** | +5.09% | +8.70% | -2.37% |
| **GLD** | +3.11% | +12.55% | +24.37% |
| **TLT** | +0.97% | +0.05% | -2.13% |
| **XLE** | -8.57% | -4.12% | -8.30% |
| **IWM** | +1.43% | -0.80% | -7.67% |

### Паралел #4: 2024-W29 (week ending 2024-07-21)
**Cosine similarity:** 0.7320 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.77% | +6.81% | +9.55% |
| **USO** | -5.35% | -8.49% | +5.79% |
| **GLD** | +4.84% | +13.32% | +12.42% |
| **TLT** | +6.54% | +2.02% | -4.22% |
| **XLE** | -3.99% | -1.39% | +3.42% |
| **IWM** | -1.91% | +4.42% | +4.64% |

### Паралел #5: 2024-W44 (week ending 2024-11-03)
**Cosine similarity:** 0.6872 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.76% | +5.74% | -0.12% |
| **USO** | +1.42% | +8.33% | -11.12% |
| **GLD** | -3.38% | +2.41% | +18.03% |
| **TLT** | +2.80% | -2.68% | -1.34% |
| **XLE** | +7.36% | +0.39% | -5.36% |
| **IWM** | +9.61% | +3.73% | -7.97% |

### Паралел #6: 2022-W46 (week ending 2022-11-20)
**Cosine similarity:** 0.6699 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -3.47% | +3.31% | +6.59% |
| **USO** | -4.07% | -2.91% | -7.43% |
| **GLD** | +3.86% | +5.20% | +12.81% |
| **TLT** | +4.31% | +3.51% | +2.99% |
| **XLE** | -6.56% | -6.84% | -11.27% |
| **IWM** | -5.44% | +5.61% | -3.34% |

### Паралел #7: 2024-W30 (week ending 2024-07-28)
**Cosine similarity:** 0.6651 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.14% | +6.68% | +12.39% |
| **USO** | +0.50% | -2.47% | +4.59% |
| **GLD** | +5.78% | +14.82% | +15.87% |
| **TLT** | +5.71% | +0.06% | -4.26% |
| **XLE** | -2.00% | -1.82% | +0.70% |
| **IWM** | -2.44% | -2.04% | +2.65% |

### Паралел #8: 2025-W47 (week ending 2025-11-23)
**Cosine similarity:** 0.6521 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.70% | +4.92% | +13.79% |
| **USO** | +1.44% | +16.67% | +103.35% |
| **GLD** | +10.52% | +25.21% | +10.57% |
| **TLT** | -1.50% | +1.03% | -3.26% |
| **XLE** | +0.38% | +23.79% | +35.07% |
| **IWM** | +7.35% | +12.69% | +21.64% |

### Паралел #9: 2023-W16 (week ending 2023-04-23)
**Cosine similarity:** 0.6471 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.46% | +10.11% | +2.92% |
| **USO** | -4.90% | +1.14% | +18.31% |
| **GLD** | -0.45% | -1.12% | -0.36% |
| **TLT** | -2.98% | -1.79% | -18.92% |
| **XLE** | -5.67% | +0.07% | +7.94% |
| **IWM** | -0.08% | +9.82% | -5.56% |

### Паралел #10: 2023-W49 (week ending 2023-12-10)
**Cosine similarity:** 0.6382 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.39% | +11.65% | +16.87% |
| **USO** | +1.29% | +10.27% | +9.75% |
| **GLD** | +1.23% | +8.61% | +13.98% |
| **TLT** | +2.53% | +2.23% | -1.28% |
| **XLE** | +1.12% | +8.25% | +11.38% |
| **IWM** | +4.76% | +11.13% | +8.38% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 13 · **Total matching days:** 72 · **History:** 2021-05-17 → 2026-06-25

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 13 | +2.0% | +1.7% | -3.1% | +7.7% | 77% |
| **SPY** | 3m | 13 | +3.1% | +3.2% | -7.0% | +12.1% | 77% |
| **SPY** | 6m | 13 | +8.0% | +11.3% | -6.1% | +22.7% | 77% |
| **USO** | 1m | 13 | +1.0% | -0.8% | -7.2% | +12.7% | 46% |
| **USO** | 3m | 13 | -2.8% | -4.1% | -21.7% | +24.5% | 46% |
| **USO** | 6m | 13 | +9.8% | -4.4% | -21.7% | +109.4% | 46% |
| **GLD** | 1m | 13 | +2.5% | +0.9% | -2.2% | +8.9% | 77% |
| **GLD** | 3m | 13 | +5.6% | +5.9% | -12.6% | +24.5% | 69% |
| **GLD** | 6m | 13 | +5.7% | +10.3% | -16.9% | +25.3% | 69% |
| **TLT** | 1m | 13 | -1.1% | -0.8% | -6.5% | +3.7% | 31% |
| **TLT** | 3m | 13 | +0.7% | +1.1% | -16.2% | +12.6% | 69% |
| **TLT** | 6m | 13 | -2.1% | +1.1% | -17.2% | +9.1% | 54% |

**Episodes (последни 5 от 13):**
- `2024-06-21 → 2024-06-21` (1d)
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-28 → 2026-05-19` (13d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 1 · **Total matching days:** 49 · **History:** 2021-05-17 → 2026-06-25

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | +9.1% | +9.1% | +9.1% | +9.1% | 100% |
| **SPY** | 3m | 1 | +8.6% | +8.6% | +8.6% | +8.6% | 100% |
| **SPY** | 6m | 1 | +8.6% | +8.6% | +8.6% | +8.6% | 100% |
| **USO** | 1m | 1 | +7.2% | +7.2% | +7.2% | +7.2% | 100% |
| **USO** | 3m | 1 | -12.3% | -12.3% | -12.3% | -12.3% | 0% |
| **USO** | 6m | 1 | -12.3% | -12.3% | -12.3% | -12.3% | 0% |
| **GLD** | 1m | 1 | -0.2% | -0.2% | -0.2% | -0.2% | 0% |
| **GLD** | 3m | 1 | -15.0% | -15.0% | -15.0% | -15.0% | 0% |
| **GLD** | 6m | 1 | -15.0% | -15.0% | -15.0% | -15.0% | 0% |
| **TLT** | 1m | 1 | -0.6% | -0.6% | -0.6% | -0.6% | 0% |
| **TLT** | 3m | 1 | +0.9% | +0.9% | +0.9% | +0.9% | 100% |
| **TLT** | 6m | 1 | +0.9% | +0.9% | +0.9% | +0.9% | 100% |

**Episodes (последни 5 от 1):**
- `2026-04-08 → 2026-06-15` (49d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 7 · **Total matching days:** 772 · **History:** 2021-05-17 → 2026-06-25

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
- `2024-10-04 → 2026-06-25` (434d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-06-25

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 9 · **Total matching days:** 76 · **History:** 2021-05-17 → 2026-06-25

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 9 | +0.4% | +0.9% | -7.2% | +7.8% | 56% |
| **SPY** | 3m | 9 | +2.4% | +3.2% | -8.0% | +12.0% | 56% |
| **SPY** | 6m | 9 | +1.4% | +4.8% | -20.2% | +14.9% | 67% |
| **USO** | 1m | 9 | +2.0% | -1.7% | -15.0% | +52.9% | 33% |
| **USO** | 3m | 9 | +5.3% | -0.1% | -27.4% | +52.2% | 44% |
| **USO** | 6m | 9 | +3.7% | -0.2% | -27.6% | +45.8% | 44% |
| **GLD** | 1m | 9 | -2.2% | -1.6% | -8.3% | +1.9% | 11% |
| **GLD** | 3m | 9 | -2.6% | -2.8% | -12.0% | +6.4% | 44% |
| **GLD** | 6m | 9 | -2.3% | -4.7% | -21.1% | +25.0% | 33% |
| **TLT** | 1m | 9 | -1.7% | -2.2% | -5.7% | +2.6% | 22% |
| **TLT** | 3m | 9 | -5.4% | -4.9% | -16.9% | +5.4% | 33% |
| **TLT** | 6m | 9 | -8.1% | -6.1% | -21.7% | +3.4% | 22% |

**Episodes (последни 5 от 9):**
- `2023-04-12 → 2023-04-18` (5d)
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-04-09` (27d)
- `2026-04-29 → 2026-05-19` (7d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 16 · **Total matching days:** 275 · **History:** 2021-05-17 → 2026-06-25

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.2% | +2.2% | -4.8% | +9.0% | 75% |
| **SPY** | 3m | 16 | +3.6% | +4.4% | -12.3% | +16.7% | 75% |
| **SPY** | 6m | 16 | +7.3% | +8.3% | -13.5% | +21.9% | 81% |
| **USO** | 1m | 16 | +1.8% | -3.2% | -13.0% | +27.7% | 38% |
| **USO** | 3m | 16 | +1.4% | -2.6% | -14.5% | +29.9% | 31% |
| **USO** | 6m | 16 | +11.1% | +1.8% | -12.4% | +87.1% | 62% |
| **GLD** | 1m | 16 | +2.4% | +1.8% | -6.4% | +9.0% | 75% |
| **GLD** | 3m | 16 | +6.2% | +7.4% | -17.1% | +23.6% | 69% |
| **GLD** | 6m | 16 | +10.9% | +12.1% | -17.1% | +43.8% | 75% |
| **TLT** | 1m | 16 | +0.6% | +0.7% | -6.1% | +8.5% | 56% |
| **TLT** | 3m | 16 | -0.5% | +0.2% | -14.7% | +13.0% | 56% |
| **TLT** | 6m | 16 | -2.6% | +0.1% | -20.6% | +8.6% | 50% |

**Episodes (последни 5 от 16):**
- `2025-03-27 → 2025-05-08` (25d)
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-17 → 2026-04-23` (4d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 19 · **Total matching days:** 297 · **History:** 2021-05-17 → 2026-06-25

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 19 | +0.4% | -0.0% | -8.3% | +7.0% | 47% |
| **SPY** | 3m | 19 | +2.2% | +3.1% | -13.3% | +9.4% | 63% |
| **SPY** | 6m | 19 | +3.5% | +6.2% | -15.7% | +17.6% | 68% |
| **USO** | 1m | 19 | -0.4% | -5.6% | -17.8% | +55.8% | 42% |
| **USO** | 3m | 19 | +2.6% | -1.3% | -17.8% | +64.3% | 42% |
| **USO** | 6m | 19 | +6.3% | -5.2% | -17.8% | +75.1% | 47% |
| **GLD** | 1m | 19 | -0.7% | -0.1% | -12.4% | +7.6% | 47% |
| **GLD** | 3m | 19 | +1.4% | +1.3% | -13.7% | +19.0% | 63% |
| **GLD** | 6m | 19 | +7.1% | +6.0% | -22.0% | +55.5% | 68% |
| **TLT** | 1m | 19 | +0.2% | +0.3% | -5.5% | +5.5% | 58% |
| **TLT** | 3m | 19 | -2.6% | -3.8% | -16.8% | +9.8% | 42% |
| **TLT** | 6m | 19 | -4.8% | -1.8% | -20.5% | +6.7% | 32% |

**Episodes (последни 5 от 19):**
- `2025-05-12 → 2025-05-19` (3d)
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-06-25` (8d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-06-25

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (19 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 9 | 2.60 | 2.89 | 2026-05-23 00:00:00 | 2026-06-20 00:00:00 | ✓ |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 9 | 2.33 | 2.34 | 2026-05-23 00:00:00 | 2026-06-20 00:00:00 | ✓ |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | 7 | 2.40 | 2.40 | 2026-06-04 00:00:00 | 2026-06-20 00:00:00 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 7 | 2.29 | 2.29 | 2026-06-04 00:00:00 | 2026-06-20 00:00:00 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | 7 | 2.24 | 2.58 | 2026-06-04 00:00:00 | 2026-06-20 00:00:00 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | 7 | 2.02 | 2.02 | 2026-06-04 00:00:00 | 2026-06-20 00:00:00 | ✓ |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 6 | 2.76 | 2.76 | 2026-06-04 00:00:00 | 2026-06-13 00:00:00 | ✓ |
| **CSUSHPISA** | Case-Shiller US National HPI (SA) | housing | housing_prices | 6 | 2.26 | 2.26 | 2026-06-04 00:00:00 | 2026-06-13 00:00:00 | - |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 5 | 2.30 | 2.39 | 2026-06-06 00:00:00 | 2026-06-20 00:00:00 | ✓ |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | 5 | 2.30 | 2.30 | 2026-06-04 00:00:00 | 2026-06-08 00:00:00 | - |
| **M2** | M2 паричен агрегат | liquidity | money_supply | 3 | 2.76 | 2.76 | 2026-05-23 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **DGORDER** | Нови поръчки за дълготрайни стоки | growth | hard_activity | 3 | 2.72 | 2.90 | 2026-05-23 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **C_AND_I_LOANS** | Търговски и индустриални кредити (C&I) | liquidity | banking_credit | 3 | 2.57 | 2.57 | 2026-05-23 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **UMCSENT** | Michigan Sentiment Index | growth | consumer_sentiment | 3 | 2.57 | 2.57 | 2026-05-23 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CPI_SHELTER** | CPI — жилища (shelter) | inflation | goods_services | 3 | 2.46 | 2.46 | 2026-05-23 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CPI_SERVICES** | CPI — услуги (всички) | inflation | goods_services | 3 | 2.35 | 2.35 | 2026-05-23 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **RSXFS** | Продажби на дребно (без храна) | growth | hard_activity | 2 | 2.33 | 2.33 | 2026-05-23 00:00:00 | 2026-05-30 00:00:00 | ✓ |
| **PPICORE** | PPI Core (Final Demand без храни и енергия) | inflation | core_measures | 2 | 2.32 | 2.32 | 2026-05-23 00:00:00 | 2026-05-30 00:00:00 | ✓ |
| **USSTHPI** | FHFA House Price Index (Q, NSA) | housing | housing_prices | 1 | 2.70 | 2.70 | 2026-06-04 00:00:00 | 2026-06-04 00:00:00 | ✓ |

### EU (13 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 6 | 5.37 | 5.37 | 2026-06-05 00:00:00 | 2026-06-20 00:00:00 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation | sentiment | 6 | 2.98 | 2.98 | 2026-06-05 00:00:00 | 2026-06-20 00:00:00 | - |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | 6 | 2.32 | 2.32 | 2026-06-05 00:00:00 | 2026-06-20 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 6 | 2.29 | 2.31 | 2026-06-05 00:00:00 | 2026-06-20 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 6 | 2.25 | 2.27 | 2026-06-05 00:00:00 | 2026-06-20 00:00:00 | ✓ |
| **EA_COMP_PER_EMPLOYEE** | Компенсация на наетите (D1, EA-20, M€) | labor | wages | 4 | 2.39 | 2.39 | 2026-05-23 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **EA_RETAIL_CONF** | Доверие в търговията на дребно (DG ECFIN) | growth | sentiment | 4 | 2.39 | 2.68 | 2026-05-23 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **EA_PPI_INTERMEDIATE** | PPI междинни стоки (MIG ING, индекс 2021=100) | inflation | producer_prices | 4 | 2.05 | 2.16 | 2026-05-23 00:00:00 | 2026-06-04 00:00:00 | - |
| **EA_RETAIL_VOL** | Търговия на дребно — обем на продажбите (G47, индекс 2021=100) | growth | hard_activity | 4 | 2.03 | 2.06 | 2026-05-23 00:00:00 | 2026-06-04 00:00:00 | - |
| **EA_WAGES_SALARIES** | Работни заплати (D11, EA-20, M€) | labor | wages | 2 | 2.38 | 2.38 | 2026-06-03 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **EA_EMPLOYMENT_EXP** | Очаквания за заетост (3m напред) | labor | labor_sentiment | 1 | 3.14 | 3.14 | 2026-05-23 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **EA_ESI** | Икономически Sentiment Indicator (DG ECFIN ESI) | growth | sentiment | 1 | 2.25 | 2.25 | 2026-05-23 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **EA_CONSUMER_CONF** | Потребителско доверие (DG ECFIN, full history от 1985) | growth | sentiment | 1 | 2.10 | 2.10 | 2026-05-23 00:00:00 | 2026-05-23 00:00:00 | - |

### CN (7 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 6 | 2.56 | 2.56 | 2026-06-02 00:00:00 | 2026-06-22 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 6 | 2.24 | 2.24 | 2026-06-02 00:00:00 | 2026-06-22 00:00:00 | - |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 6 | 2.23 | 2.23 | 2026-06-02 00:00:00 | 2026-06-22 00:00:00 | ✓ |
| **CN_POLICY_RATE** | Политическа лихва — PBoC 7-day repo (%) | credit | rates | 2 | 2.39 | 2.39 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CN_FDI_GDP** | ПЧИ — входящи (% от БВП) | property | investment | 2 | 2.11 | 2.11 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CN_BIS_PROPERTY_YOY** | Жилищни имотни цени (YoY %, BIS номинал) | property | housing | 2 | 2.10 | 2.10 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | - |
| **CN_CREDIT_PRIVATE** | Кредит към частния сектор (% от БВП) | credit | credit_depth | 2 | 2.07 | 2.07 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-06-20 00:00:00 · **Generated:** 2026-06-20 10:10:49.025363+00:00

**Режим:** `stagflation_confirmed` (Стагфлация (потвърдена))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 34.9 | contracting | 25.9% | 2 | 2 |
| **growth** | 43.9 | mixed | 36.0% | 2 | 1 |
| **inflation** | 36.6 | contracting | 27.8% | 4 | 1 |
| **liquidity** | 52.1 | mixed | 42.1% | 0 | 0 |

### Top anomalies (7 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | +2.89 | up | 6.42 | 2026-05-01 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | +2.58 | up | 5.29 | 2026-05-01 | - |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | -2.40 | down | 2.60 | 2026-04-01 | - |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.34 | down | 94.99 | 2026-01-01 | ✓ min |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | +2.29 | up | 4.70 | 2026-04-01 | - |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | +2.28 | up | 55.10 | 2026-05-01 | ✓ max |
| **JTSQUR** | Quits rate — напускания | labor | flow | -2.02 | down | 1.90 | 2026-04-01 | ✓ min |

### Narrative hints от макро лещите
- **PPIFIS**: Производствени цени → consumer prices с 1-3 месечен lag. Водещ за CPI при трендови промени.
- **CPI_GOODS**: Goods inflation реагира бързо на supply shocks. 2022 peak след доставъчните кризи. Сега често е в deflation/близо до 0.
- **PSAVERT**: Hard data компонент. Скочи >30% в COVID — когато survey и hard data разминават, сигналът укрепва.
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **MICH_INFL_1Y**: Household очаквания. По-шумни от market-based, но по-ранни. Extreme movements сигнализират de-anchoring risk.
- **US_PMI_MFG**: Markit mfg — comparable cross-country. ISM е US-only.
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
  - `breadth_a`: 0.8
  - `breadth_b`: 1.0
- 🔔 **?**
  - `pair_id`: growth_labor_lead_lag
  - `name_bg`: Hard activity × Labor claims
  - `question_bg`: Дали hard activity и labor market следват едно тенденция?
  - `state`: a_up_b_down
  - `interpretation`: Activity hot, но claims rise — early labor crack (watchlist).
  - `slot_a_label`: Hard activity
  - `slot_b_label`: Labor market (claims inverted)
  - `breadth_a`: 1.0
  - `breadth_b`: 0.333
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
- 🔔 **?**
  - `pair_id`: sentiment_vs_hard_data
  - `name_bg`: Consumer sentiment × Hard activity
  - `question_bg`: Дали sentiment потвърждава hard data, или има разминаване?
  - `state`: a_down_b_up
  - `interpretation`: Activity OK, sentiment крачка — strategic pessimism / political bias.
  - `slot_a_label`: Consumer sentiment
  - `slot_b_label`: Hard activity
  - `breadth_a`: 0.333
  - `breadth_b`: 1.0
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

### Executive narrative
> Картината показва потвърдена стагфлационна конфигурация — трудовият пазар остава tight, а инфлационният натиск е broad-based. Най-отклонена леща: Инфлация и цени — breadth 71% (разширяване), 4 аномалии, 1 нови екстремума. Expectations също нагоре — de-anchoring в ход, рискът ескалира. За наблюдение следващия релиз: LABOR_SHARE_NBS (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: PPIFIS z=+2.89
- 3 нови екстремуми в top-7 (lookback 5г.)
- Активни двойки: Stagflation test=both_up; Growth × Labor=a_up_b_down; Inflation anchoring=both_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-06-20 00:00:00 · **Generated:** 2026-06-20 10:18:29.895620+00:00

**Режим:** `stagflation_confirmed` (Стагфлация (потвърдена))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 36.5 | contracting | 42.9% | 1 | 0 |
| **growth** | 46.8 | mixed | 23.1% | 1 | 0 |
| **inflation** | 43.3 | mixed | 42.9% | 1 | 0 |
| **credit** | 44.8 | mixed | 36.8% | 3 | 2 |

### Top anomalies (5 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | +5.37 | up | 2.75 | 2026-05-01 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation, growth | sentiment | +2.98 | up | 27.40 | 2026-05-01 | - |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | -2.32 | down | -1.80 | 2026-05-01 | - |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | +2.27 | up | 3.04 | 2026-05-01 | ✓ max |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | +2.25 | up | 3.74 | 2026-05-01 | ✓ max |

### Narrative hints от макро лещите
- **EA_BUND_2Y**: EA-aggregate 2Y yield. Curve slope (10Y-2Y) проксира policy expectations и recession risk.
- **EA_SELLING_PRICE_EXP**: Forward-looking inflation сигнал от business side — мениджърите казват дали ще вдигат цени. Изпреварва HICP с 3-6 месеца.
- **EA_EMP_EXP_SERVICES**: DG ECFIN survey: forward-looking labor сигнал от услугите (~70% от GDP). Дълга история (от 1996) — за разлика от teibs030 (EA_EMPLOYMENT_EXP, 12m). Същата полярност (higher=better). De-singleton-ва labor_sentiment.
- **DE_10Y**: Germany 10Y, Maastricht-criterion measure. Reference за BTP-Bund / OAT-Bund spread изчисления.
- **FR_10Y**: France sovereign yield — компонент на OAT-Bund spread. Core-but-not-DE EA stress indicator.

### Cross-lens divergences (6 entries)
- 🔔 **?**
  - `pair_id`: stagflation_test
  - `name_bg`: Стагфлационен тест
  - `question_bg`: Заплатите ли движат услугите нагоре?
  - `state`: both_up
  - `interpretation`: Стагфлационен риск: заплатите и базовата/услуги инфлация се движат заедно нагоре. Wage-price spiral начало.
  - `slot_a_label`: Натиск от заплати
  - `slot_b_label`: Базова/услуги инфлация
  - `breadth_a`: 1.0
  - `breadth_b`: 1.0
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
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Закотвеност на инфлационните очаквания
  - `question_bg`: Headline отскача — очакванията остават ли закотвени?
  - `state`: insufficient_data
  - `interpretation`: Insufficient data в една от двете групи.
  - `slot_a_label`: Реализирана headline инфлация
  - `slot_b_label`: SPF дългосрочни очаквания
  - `breadth_a`: 0.333
  - `breadth_b`: None
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
- 🔔 **?**
  - `pair_id`: sentiment_vs_hard_data
  - `name_bg`: Очаквания срещу твърди данни
  - `question_bg`: Sentiment отразява ли реалната икономика?
  - `state`: transition
  - `interpretation`: Sentiment turn обикновено leads hard data 3-6mo.
  - `slot_a_label`: Sentiment (ESI, confidence)
  - `slot_b_label`: Hard activity (IP, retail, GDP)
  - `breadth_a`: 0.444
  - `breadth_b`: 0.25

### Executive narrative
> Картината показва потвърдена стагфлационна конфигурация — трудовият пазар остава tight, а инфлационният натиск е broad-based. Най-отклонена леща: Пазар на труда — breadth 75% (разширяване), 1 аномалии, 0 нови екстремума. За наблюдение следващия релиз: DE_10Y, FR_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.37
- 2 нови екстремуми в top-5 (lookback 5г.)
- Активни двойки: Stagflation test=both_up



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-06-22 00:00:00 · **Generated:** 2026-06-22 11:28:52.556482+00:00

**Режим:** `recessionary` (РЕЦЕСИОНЕН)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 30.6 | contracting | -% | - | - |
| **inflation** | 48.0 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 42.4 | mixed | -% | - | - |
| **property** | 25.2 | contracting | -% | - | - |

### Top anomalies (3 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | -2.56 | down | 3.00 | 2026-05-20 | ✓ min |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | -2.24 | down | 1.72 | 2026-05-31 | - |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | +2.23 | up | 15.79 | 2025-12-31 | ✓ max |

### Narrative hints от макро лещите
- **CN_LPR_1Y**: Замества benchmark lending rate от 2019. Главен policy signal.
- **CN_CGB_10Y**: Sovereign benchmark. CGB-UST 10Y spread = capital flow incentive.
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
  - `breadth_a`: 0.833
  - `breadth_b`: 0.333

### Executive narrative
> Претеглен композитен macro score 33.9/100 → режим „РЕЦЕСИОНЕН“. 5 лещи, 3 flagged аномалии (4 застояли изключени), 3 cross-lens двойки.



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

### US (period: 2026-06-18 → 2026-06-24)

**stable_winner (1m):** +12 entered, -9 exited
  - **Entered:** APA, CHRW, CIEN, COHR, EBAY, FCX, GILD, GM, GS, HAL, MS, RL _(включително 2 за първи път в историята: FCX, HAL)_
  - **Exited:** AES, CASY, HAS, MU, NRG, STT, VLO, WELL, WMT

**stable_winner (3m):** +4 entered, -7 exited
  - **Entered:** EBAY, FIX, HAL, NEE _(включително 1 за първи път в историята: HAL)_
  - **Exited:** CFG, HAS, KEY, LVS, NTRS, WELL, WMT

**quality_dip (1m):** +9 entered, -10 exited
  - **Entered:** AES, CASY, HAS, MU, NRG, STT, VLO, WELL, WMT _(включително 2 за първи път в историята: AES, CASY)_
  - **Exited:** APA, CHRW, CIEN, COHR, FCX, GILD, GM, GS, MS, RL

**quality_dip (3m):** +7 entered, -2 exited
  - **Entered:** CFG, HAS, KEY, LVS, NTRS, WELL, WMT _(включително 1 за първи път в историята: NTRS)_
  - **Exited:** FIX, NEE

**faded_bounce (1m):** +11 entered, -7 exited
  - **Entered:** AON, ARE, CLX, CTAS, EFX, ERIE, GPN, KMB, MRSH, SO, TTD _(включително 2 за първи път в историята: AON, SO)_
  - **Exited:** GDDY, IT, LEN, LII, MAS, POOL, STZ

**faded_bounce (3m):** +6 entered, -8 exited
  - **Entered:** AON, ARES, ERIE, IP, KKR, SO _(включително 2 за първи път в историята: AON, SO)_
  - **Exited:** AWK, BRO, EFX, LEN, OTIS, PEG, PGR, STZ

### EU (period: 2026-06-19 → 2026-06-24)

**stable_winner (1m):** +10 entered, -13 exited
  - **Entered:** CA.PA, CBK.DE, ENGI.PA, FTK.DE, HUBN.SW, IDR.MC, KCR.HE, METSO.HE, SWED-A.ST, ZEG.L _(включително 4 за първи път в историята: CA.PA, IDR.MC, KCR.HE, SWED-A.ST)_
  - **Exited:** AAF.L, ACS.MC, ALLN.SW, BARC.L, DLG.MI, ELI.BR, HOC.L, IG.MI, KGF.L, NDA.DE, NESTE.HE, SPSN.SW, VOD.L

**stable_winner (3m):** +5 entered, -8 exited
  - **Entered:** DANSKE.CO, GAW.L, KCR.HE, SWED-A.ST, TPRO.MI _(включително 3 за първи път в историята: DANSKE.CO, KCR.HE, SWED-A.ST)_
  - **Exited:** ALLN.SW, BIRG.IR, ENGI.PA, LTMC.MI, MOBN.SW, NDX1.DE, SPSN.SW, VOD.L

**quality_dip (1m):** +13 entered, -8 exited
  - **Entered:** AAF.L, ACS.MC, ALLN.SW, BARC.L, DLG.MI, ELI.BR, HOC.L, IG.MI, KGF.L, NDA.DE, NESTE.HE, SPSN.SW, VOD.L _(включително 1 за първи път в историята: NDA.DE)_
  - **Exited:** CA.PA, CBK.DE, ENGI.PA, FTK.DE, HUBN.SW, IDR.MC, METSO.HE, ZEG.L

**quality_dip (3m):** +8 entered, -3 exited
  - **Entered:** ALLN.SW, BIRG.IR, ENGI.PA, LTMC.MI, MOBN.SW, NDX1.DE, SPSN.SW, VOD.L _(включително 1 за първи път в историята: VOD.L)_
  - **Exited:** DANSKE.CO, GAW.L, TPRO.MI

**faded_bounce (1m):** +5 entered, -14 exited
  - **Entered:** CMBN.SW, CVC.AS, MF.PA, NEXI.MI, STLAM.MI _(включително 1 за първи път в историята: CMBN.SW)_
  - **Exited:** AUTO.L, BC.MI, ENX.PA, EVK.DE, EXPN.L, IMCD.AS, RACE.MI, RAND.AS, REL.L, SGE.L, SGO.PA, SIGN.SW, TCAP.L, WKL.AS

**faded_bounce (3m):** +7 entered, -7 exited
  - **Entered:** BME.L, MF.PA, NEXI.MI, PNDORA.CO, RI.PA, TRYG.CO, VZN.SW
  - **Exited:** BALD-B.ST, EVK.DE, EXPN.L, ORSTED.CO, RACE.MI, TOM.OL, WKL.AS



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-06-16 00:00:00)
| Market | Asset class | Net position | Net % | Percentile 5y | Weekly change |
|---|---|---:|---:|---:|---:|
| **soyoil** | Commodities | 122914 | 98.8 | 98.8 | -33520 |
| **copper** | Commodities | 71076 | 93.2 | 93.2 | -3923 |
| **cattle** | Commodities | 124349 | 90.5 | 90.5 | -5764 |
| **rbob** | Commodities | 67676 | 79.1 | 79.1 | 5047 |
| **aud** | FX | 41538 | 75.7 | 75.7 | -19640 |
| **vix** | Volatility | -13295 | 73.1 | 73.1 | 38609 |
| **brent** | Commodities | 9347 | 63.6 | 63.6 | -6909 |
| **cotton** | Commodities | 35136 | 56.3 | 56.3 | -26909 |
| **gbpfx** | FX | 16836 | 55.4 | 55.4 | -14533 |
| **eurfx** | FX | -8926 | 50.6 | 50.6 | -25243 |
| **dxy** | FX | -1870 | 49.7 | 49.7 | 9846 |
| **gold** | Commodities | 112918 | 47.9 | 47.9 | 18530 |
| **coffee** | Commodities | 7974 | 46.4 | 46.4 | -9934 |
| **soybeans** | Commodities | 52818 | 44.8 | 44.8 | -154986 |
| **heatingoil** | Commodities | 9447 | 40.5 | 40.5 | -1346 |
| **platinum** | Commodities | 8072 | 39.9 | 39.9 | -5546 |
| **soymeal** | Commodities | 17452 | 35.0 | 35.0 | -113102 |
| **bitcoin** | Crypto | -6607 | 34.1 | 34.1 | 2354 |
| **silver** | Commodities | 12070 | 30.3 | 30.3 | 309 |
| **corn** | Commodities | -46427 | 29.5 | 29.5 | -339781 |
| **nasdaq** | US Equities | -28154 | 26.8 | 26.8 | 17217 |
| **wti** | Commodities | 117885 | 26.5 | 26.5 | -20889 |
| **natgas** | Commodities | -84672 | 24.2 | 24.2 | 11617 |
| **usultra10y** | Rates | -233985 | 20.4 | 20.4 | 42165 |
| **wheat** | Commodities | -69531 | 20.2 | 20.2 | -64732 |
| **chf** | FX | -12366 | 17.9 | 17.9 | -7521 |
| **us30y** | Rates | -310313 | 17.4 | 17.4 | 16070 |
| **russell** | US Equities | -84570 | 15.5 | 15.5 | -17141 |
| **palladium** | Commodities | -4268 | 12.6 | 12.6 | -1495 |
| **us2y** | Rates | -1704817 | 10.8 | 10.8 | 173815 |
| **us5y** | Rates | -2214610 | 10.8 | 10.8 | 91837 |
| **cad** | FX | -65053 | 6.8 | 6.8 | -26399 |
| **cocoa** | Commodities | -25002 | 6.0 | 6.0 | -8836 |
| **jpy** | FX | -96772 | 5.0 | 5.0 | -31827 |
| **sugar** | Commodities | -153130 | 4.2 | 4.2 | -69093 |
| **sp500** | US Equities | -515520 | 3.2 | 3.2 | -113966 |
| **us10y** | Rates | -2082236 | 3.2 | 3.2 | -129499 |
| **hogs** | Commodities | -20959 | 0.7 | 0.7 | -54672 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **WDC** | Technology | 96.4 | 33.0% | 113.9% | 255.8% | 969.2% | 3.45 | -20.6% |
| 2 | **MU** | Technology | 96.3 | 39.6% | 165.2% | 294.6% | 760.9% | 2.93 | -30.3% |
| 3 | **SNDK** | Technology | 96.3 | 29.5% | 172.5% | 705.7% | 3977.7% | 3.68 | -31.3% |
| 4 | **DELL** | Technology | 95.8 | 47.0% | 146.1% | 245.9% | 273.4% | 2.03 | -32.3% |
| 5 | **STX** | Technology | 95.7 | 22.3% | 134.3% | 236.9% | 656.5% | 3.09 | -21.0% |
| 6 | **AMAT** | Technology | 95.6 | 36.3% | 57.7% | 130.3% | 245.0% | 2.37 | -21.4% |
| 7 | **MRVL** | Technology | 95.5 | 40.9% | 199.7% | 229.4% | 292.0% | 1.86 | -26.4% |
| 8 | **LRCX** | Technology | 95.0 | 22.8% | 57.0% | 118.0% | 311.4% | 2.53 | -20.0% |
| 9 | **HPE** | Technology | 94.9 | 30.1% | 104.6% | 101.4% | 179.4% | 2.04 | -23.7% |
| 10 | **KLAC** | Technology | 94.5 | 27.4% | 53.7% | 93.5% | 182.7% | 1.92 | -22.4% |
| 11 | **DD** | Basic Materials | 94.1 | 192.3% | 216.0% | 248.5% | 426.0% | 1.48 | -16.6% |
| 12 | **INTC** | Technology | 93.5 | 9.8% | 198.8% | 257.6% | 521.3% | 2.43 | -24.2% |
| 13 | **AMD** | Technology | 93.4 | 11.2% | 153.1% | 143.5% | 301.1% | 2.03 | -27.8% |
| 14 | **FLEX** | Technology | 93.3 | 13.8% | 118.1% | 134.6% | 225.2% | 1.96 | -18.4% |
| 15 | **CAT** | Industrials | 93.0 | 13.0% | 39.0% | 73.3% | 174.5% | 2.74 | -13.9% |
| 16 | **TER** | Technology | 92.3 | 19.2% | 33.5% | 119.0% | 390.3% | 2.28 | -26.7% |
| 17 | **GLW** | Technology | 91.2 | 6.2% | 45.2% | 135.1% | 301.7% | 2.31 | -23.0% |
| 18 | **FIX** | Industrials | 90.5 | 6.9% | 33.8% | 108.0% | 289.4% | 2.45 | -15.8% |
| 19 | **COHR** | Technology | 90.2 | 4.0% | 44.1% | 111.2% | 386.7% | 2.04 | -26.5% |
| 20 | **NUE** | Basic Materials | 88.8 | 3.7% | 48.3% | 52.2% | 93.8% | 2.10 | -18.4% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **ATS.VI** | Technology | 95.2 | 56.4% | 341.1% | 634.9% | 1213.0% | 3.46 | -24.5% |
| 2 | **TPRO.MI** | Technology | 92.2 | 10.4% | 152.3% | 185.1% | 368.6% | 2.50 | -27.0% |
| 3 | **STMMI.MI** | Technology | 90.9 | 5.9% | 130.3% | 190.1% | 148.9% | 1.72 | -33.5% |
| 4 | **FRO.OL** | Energy | 90.8 | 22.3% | 34.6% | 80.7% | 116.2% | 1.84 | -20.5% |
| 5 | **RBI.VI** | Financial Services | 90.6 | 15.2% | 52.2% | 56.0% | 123.9% | 2.01 | -18.0% |
| 6 | **ASML.AS** | Technology | 90.5 | 11.8% | 29.6% | 74.0% | 129.5% | 1.97 | -15.8% |
| 7 | **GL9.IR** | Consumer Defensive | 90.2 | 15.0% | 40.9% | 63.5% | 89.4% | 2.17 | -8.0% |
| 8 | **IFX.DE** | Technology | 90.1 | 2.6% | 107.7% | 125.9% | 129.4% | 1.76 | -21.2% |
| 9 | **PRY.MI** | Industrials | 89.3 | -1.6% | 57.1% | 76.7% | 158.0% | 2.42 | -13.1% |
| 10 | **AIXA.DE** | Technology | 89.3 | 1.1% | 59.2% | 221.7% | 259.0% | 1.99 | -28.4% |
| 11 | **BESI.AS** | Technology | 88.9 | 3.1% | 60.1% | 124.7% | 126.0% | 1.54 | -20.9% |
| 12 | **SUBC.OL** | Energy | 88.7 | 6.7% | 37.5% | 78.1% | 89.8% | 2.05 | -11.3% |
| 13 | **TIT.MI** | Communication Services | 88.6 | 9.4% | 32.3% | 61.2% | 97.5% | 2.27 | -13.0% |
| 14 | **NOKIA.HE** | Technology | 88.5 | -5.7% | 78.9% | 135.7% | 186.2% | 2.08 | -27.6% |
| 15 | **IFCN.SW** | Technology | 88.3 | 8.6% | 66.1% | 78.9% | 76.6% | 1.40 | -25.5% |
| 16 | **HOT.DE** | Industrials | 87.9 | 5.3% | 31.0% | 56.2% | 221.2% | 2.67 | -15.9% |
| 17 | **ASM.AS** | Technology | 87.7 | 8.5% | 43.0% | 89.9% | 78.7% | 1.24 | -26.2% |
| 18 | **PST.MI** | Financial Services | 87.6 | 14.4% | 46.0% | 37.5% | 65.7% | 2.60 | -15.5% |
| 19 | **VACN.SW** | Industrials | 87.3 | 7.9% | 32.7% | 71.7% | 101.6% | 1.55 | -25.1% |
| 20 | **ABBN.SW** | Industrials | 87.2 | 1.9% | 36.3% | 49.1% | 86.9% | 2.23 | -12.1% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MO** | Consumer Staples | 0.808 | 0.719 | 0.960 | 0.879 | 0.565 | +33.1% | 15.3 | - |
| 2 | **GL** | Financials | 0.756 | 0.812 | 0.670 | 0.735 | 0.851 | +43.6% | 12.2 | +20.5% |
| 3 | **ALL** | Financials | 0.740 | 0.620 | 0.694 | 0.871 | 0.854 | +20.7% | 5.1 | +45.2% |
| 4 | **USB** | Financials | 0.731 | 0.718 | 0.703 | 0.847 | 0.621 | +39.4% | 12.8 | +12.3% |
| 5 | **TROW** | Financials | 0.728 | 0.607 | 0.735 | 0.873 | 0.716 | +16.4% | 11.4 | +18.7% |
| 6 | **MTB** | Financials | 0.719 | 0.678 | 0.671 | 0.824 | 0.723 | +25.8% | 13.3 | +10.3% |
| 7 | **PNC** | Financials | 0.719 | 0.729 | 0.675 | 0.804 | 0.645 | +36.5% | 14.3 | +12.1% |
| 8 | **TRV** | Financials | 0.718 | 0.591 | 0.678 | 0.825 | 0.873 | +22.8% | 9.5 | +25.3% |
| 9 | **RF** | Financials | 0.714 | 0.679 | 0.681 | 0.864 | 0.602 | +33.5% | 12.4 | +11.9% |
| 10 | **KEY** | Financials | 0.714 | 0.716 | 0.641 | 0.838 | 0.648 | +41.7% | 14.4 | +10.0% |
| 11 | **SPG** | Real Estate | 0.708 | 0.802 | 0.891 | 0.511 | 0.485 | +47.2% | 15.7 | +113.6% |
| 12 | **NTRS** | Financials | 0.707 | 0.824 | 0.632 | 0.639 | 0.738 | +44.6% | 18.4 | +14.5% |
| 13 | **CFG** | Financials | 0.707 | 0.796 | 0.598 | 0.782 | 0.618 | +64.2% | 16.7 | +7.7% |
| 14 | **SYF** | Financials | 0.699 | 0.566 | 0.849 | 0.813 | 0.478 | +20.6% | 8.1 | +21.8% |
| 15 | **HST** | Real Estate | 0.697 | 0.882 | 0.534 | 0.704 | 0.639 | +67.3% | 17.0 | +14.9% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | 0.149 | 0.199 | 0.131 | 0.059 | 0.238 |
| 502 | **CSGP** | Real Estate | 0.155 | 0.014 | 0.107 | 0.204 | 0.452 |
| 501 | **NRG** | Utilities | 0.191 | 0.281 | 0.117 | 0.191 | 0.162 |
| 500 | **COIN** | Financials | 0.196 | 0.066 | 0.320 | 0.200 | 0.204 |
| 499 | **TSLA** | Consumer Discretionary | 0.233 | 0.356 | 0.163 | 0.042 | 0.445 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W26.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W26.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-06-22  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
