# Сателит — пълен data export за 2026-W20

_Период: 2026-05-11 → 2026-05-17_  
_Генериран: 2026-05-17 07:50 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W20.md` (structured briefing) и `narrative_2026-W20.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**16 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **TIP** | -0.71% | -2.55σ | 111.40 | 110.61 | 2026-05-08 | 2026-05-15 | +0.09% | +0.31% | 4 |
| **URA** | -9.51% | -2.11σ | 55.18 | 49.93 | 2026-05-08 | 2026-05-15 | +0.55% | +4.76% | 13 |
| **TLT** | -2.81% | -2.00σ | 86.08 | 83.66 | 2026-05-08 | 2026-05-15 | -0.04% | +1.39% | 13 |
| **IEF** | -1.53% | -1.93σ | 94.96 | 93.51 | 2026-05-08 | 2026-05-15 | -0.01% | +0.78% | 13 |
| **XLE** | +6.71% | +1.76σ | 55.70 | 59.44 | 2026-05-08 | 2026-05-15 | +0.46% | +3.55% | 13 |
| **UUP** | +1.57% | +1.74σ | 27.34 | 27.77 | 2026-05-08 | 2026-05-15 | +0.10% | +0.85% | 13 |
| **VNQ** | -2.80% | -1.43σ | 96.62 | 93.91 | 2026-05-08 | 2026-05-15 | +0.46% | +2.29% | 13 |
| **EEM** | -4.22% | -1.38σ | 67.94 | 65.07 | 2026-05-08 | 2026-05-15 | +1.02% | +3.79% | 13 |
| **VWO** | -3.47% | -1.36σ | 60.54 | 58.44 | 2026-05-08 | 2026-05-15 | +0.47% | +2.89% | 13 |
| **LQD** | -1.23% | -1.35σ | 109.20 | 107.86 | 2026-05-08 | 2026-05-15 | -0.00% | +0.91% | 13 |
| **HYG** | -0.85% | -1.34σ | 80.14 | 79.46 | 2026-05-08 | 2026-05-15 | +0.05% | +0.67% | 13 |
| **XLRE** | -2.66% | -1.31σ | 44.41 | 43.23 | 2026-05-08 | 2026-05-15 | +0.51% | +2.41% | 13 |
| **SHY** | -0.29% | -1.26σ | 82.30 | 82.06 | 2026-05-08 | 2026-05-15 | +0.01% | +0.24% | 13 |
| **XLY** | -3.05% | -1.17σ | 120.20 | 116.53 | 2026-05-08 | 2026-05-15 | +0.20% | +2.79% | 13 |
| **IWM** | -2.31% | -1.15σ | 284.17 | 277.60 | 2026-05-08 | 2026-05-15 | +0.58% | +2.51% | 13 |
| **DBA** | -0.50% | -1.05σ | 27.97 | 27.83 | 2026-05-08 | 2026-05-15 | +0.64% | +1.09% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_5 канонични patterns от `config/divergence_rules.yaml`, evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — 🔔 ТРИГГЕРИРАН
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-05-17 · **Conditions matched:** 5/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | +10.96% | ✅ | 133.59 | 148.23 | 2026-05-08 | 2026-05-15 |
| DFEN | down ≥ 3.0% | -8.87% | ✅ | 65.07 | 59.30 | 2026-05-08 | 2026-05-15 |
| GLD | down ≥ 1.0% | -3.80% | ✅ | 433.77 | 417.29 | 2026-05-08 | 2026-05-15 |
| URA | down ≥ 3.0% | -9.51% | ✅ | 55.18 | 49.93 | 2026-05-08 | 2026-05-15 |
| UUP | up ≥ 0.5% | +1.57% | ✅ | 27.34 | 27.77 | 2026-05-08 | 2026-05-15 |

### Ликвидна стес (flight to quality) (`liquidity_stress`) — не активен
_Дългосрочни trezuri нагоре, високодоходен кредит надолу, злато нагоре. Класически risk-off._  
**Window:** 7d ending 2026-05-17 · **Conditions matched:** 2/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| TLT | up ≥ 1.0% | -2.81% | ❌ | 86.08 | 83.66 | 2026-05-08 | 2026-05-15 |
| HYG | down ≥ 0.5% | -0.85% | ✅ | 80.14 | 79.46 | 2026-05-08 | 2026-05-15 |
| GLD | up ≥ 1.0% | -3.80% | ❌ | 433.77 | 417.29 | 2026-05-08 | 2026-05-15 |
| UUP | up ≥ 0.3% | +1.57% | ✅ | 27.34 | 27.77 | 2026-05-08 | 2026-05-15 |

### Възстановяване на инфлационни очаквания (`inflation_pickup`) — не активен
_Inflation-protected треzuri нагоре, commodities нагоре, dollar надолу. Repricing на real rates._  
**Window:** 7d ending 2026-05-17 · **Conditions matched:** 2/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| DBC | up ≥ 1.5% | +2.94% | ✅ | 30.30 | 31.19 | 2026-05-08 | 2026-05-15 |
| GLD | up ≥ 1.0% | -3.80% | ❌ | 433.77 | 417.29 | 2026-05-08 | 2026-05-15 |
| UUP | down ≥ 0.5% | +1.57% | ❌ | 27.34 | 27.77 | 2026-05-08 | 2026-05-15 |
| TLT | down ≥ 1.0% | -2.81% | ✅ | 86.08 | 83.66 | 2026-05-08 | 2026-05-15 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-05-17 · **Conditions matched:** 1/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | -2.31% | ❌ | 284.17 | 277.60 | 2026-05-08 | 2026-05-15 |
| XLF | up ≥ 1.0% | -0.27% | ❌ | 51.24 | 51.10 | 2026-05-08 | 2026-05-15 |
| XLY | up ≥ 1.0% | -3.05% | ❌ | 120.20 | 116.53 | 2026-05-08 | 2026-05-15 |
| GLD | down ≥ 0.5% | -3.80% | ✅ | 433.77 | 417.29 | 2026-05-08 | 2026-05-15 |

### Защитен pivot (staples + utilities + gold) (`defensive_pivot`) — не активен
_XLP + XLU + GLD едновременно нагоре. Smart money flight to defensives без credit panic._  
**Window:** 7d ending 2026-05-17 · **Conditions matched:** 0/3

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| XLP | up ≥ 1.0% | +0.55% | ❌ | 84.18 | 84.64 | 2026-05-08 | 2026-05-15 |
| XLU | up ≥ 1.0% | -1.90% | ❌ | 44.72 | 43.87 | 2026-05-08 | 2026-05-15 |
| GLD | up ≥ 1.0% | -3.80% | ❌ | 433.77 | 417.29 | 2026-05-08 | 2026-05-15 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2026-W05 (week ending 2026-02-01)
**Cosine similarity:** 0.9669 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.68% | +4.43% | +7.11% |
| **USO** | +13.43% | +79.58% | +86.41% |
| **GLD** | +5.21% | -4.89% | -6.22% |
| **TLT** | +3.37% | -0.28% | -2.55% |
| **XLE** | +10.71% | +16.03% | +17.20% |
| **IWM** | -0.16% | +7.75% | +7.10% |

### Паралел #2: 2024-W40 (week ending 2024-10-06)
**Cosine similarity:** 0.9393 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.65% | +3.66% | -11.25% |
| **USO** | -2.12% | +2.06% | -11.04% |
| **GLD** | +3.43% | -0.62% | +14.17% |
| **TLT** | -2.61% | -7.66% | -0.76% |
| **XLE** | -3.23% | -5.34% | -14.10% |
| **IWM** | +2.32% | +2.71% | -16.89% |

### Паралел #3: 2023-W06 (week ending 2023-02-12)
**Cosine similarity:** 0.9288 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -4.00% | +1.25% | +10.04% |
| **USO** | -9.93% | -11.16% | +6.27% |
| **GLD** | +2.00% | +7.76% | +2.45% |
| **TLT** | +0.93% | +1.61% | -6.30% |
| **XLE** | -9.38% | -12.05% | +1.58% |
| **IWM** | -7.25% | -8.91% | +1.01% |

### Паралел #4: 2024-W11 (week ending 2024-03-17)
**Cosine similarity:** 0.9184 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.24% | +6.46% | +10.59% |
| **USO** | +6.55% | -0.33% | -8.50% |
| **GLD** | +10.77% | +8.02% | +19.51% |
| **TLT** | -4.68% | +2.91% | +10.22% |
| **XLE** | +3.94% | -3.07% | -5.01% |
| **IWM** | -3.39% | -1.29% | +7.70% |

### Паралел #5: 2024-W32 (week ending 2024-08-11)
**Cosine similarity:** 0.8866 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.96% | +12.58% | +13.44% |
| **USO** | -12.15% | -4.05% | -0.47% |
| **GLD** | +3.59% | +10.42% | +17.52% |
| **TLT** | +4.94% | -2.97% | -5.32% |
| **XLE** | -4.78% | +5.72% | +0.71% |
| **IWM** | +0.90% | +15.73% | +10.16% |

### Паралел #6: 2022-W18 (week ending 2022-05-08)
**Cosine similarity:** 0.8666 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.07% | +0.95% | -7.73% |
| **USO** | +9.63% | -12.89% | -6.47% |
| **GLD** | -1.41% | -5.77% | -10.80% |
| **TLT** | +1.46% | +3.04% | -16.07% |
| **XLE** | +11.05% | -10.88% | +12.70% |
| **IWM** | +4.56% | +4.78% | -1.37% |

### Паралел #7: 2021-W37 (week ending 2021-09-19)
**Cosine similarity:** 0.8620 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.09% | +4.55% | +1.37% |
| **USO** | +14.11% | +0.91% | +48.33% |
| **GLD** | +1.03% | +2.46% | +9.48% |
| **TLT** | -3.54% | +1.61% | -9.86% |
| **XLE** | +19.07% | +11.58% | +53.58% |
| **IWM** | +1.83% | -2.71% | -6.27% |

### Паралел #8: 2023-W30 (week ending 2023-07-30)
**Cosine similarity:** 0.8616 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.70% | -9.80% | +7.48% |
| **USO** | +1.71% | +8.70% | +1.40% |
| **GLD** | -1.09% | +2.36% | +2.83% |
| **TLT** | -3.24% | -14.71% | -4.27% |
| **XLE** | +2.99% | -0.69% | -0.19% |
| **IWM** | -4.17% | -17.03% | +0.61% |

### Паралел #9: 2022-W02 (week ending 2022-01-16)
**Cosine similarity:** 0.8511 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -4.01% | -5.50% | -16.51% |
| **USO** | +7.19% | +32.68% | +22.96% |
| **GLD** | +2.01% | +8.47% | -6.28% |
| **TLT** | -4.88% | -14.66% | -17.47% |
| **XLE** | +5.46% | +24.96% | +8.55% |
| **IWM** | -3.85% | -6.98% | -18.86% |

### Паралел #10: 2022-W12 (week ending 2022-03-27)
**Cosine similarity:** 0.8504 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -8.08% | -13.46% | -18.03% |
| **USO** | -5.30% | +0.66% | -19.10% |
| **GLD** | -2.77% | -6.74% | -16.10% |
| **TLT** | -4.71% | -12.07% | -16.94% |
| **XLE** | -6.31% | -8.07% | -8.51% |
| **IWM** | -8.92% | -14.83% | -18.61% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 13 · **Total matching days:** 70 · **History:** 2021-05-17 → 2026-05-15

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 13 | +1.9% | +1.7% | -3.1% | +7.7% | 77% |
| **SPY** | 3m | 13 | +3.2% | +3.9% | -7.0% | +12.1% | 77% |
| **SPY** | 6m | 13 | +8.1% | +11.7% | -6.1% | +22.7% | 77% |
| **USO** | 1m | 13 | +2.0% | +1.5% | -7.2% | +12.7% | 54% |
| **USO** | 3m | 13 | +1.5% | +2.3% | -18.9% | +24.5% | 62% |
| **USO** | 6m | 13 | +14.3% | +4.1% | -8.7% | +107.9% | 62% |
| **GLD** | 1m | 13 | +2.5% | +0.9% | -1.1% | +8.9% | 77% |
| **GLD** | 3m | 13 | +6.9% | +5.9% | -6.2% | +24.5% | 69% |
| **GLD** | 6m | 13 | +7.4% | +10.3% | -12.5% | +25.3% | 69% |
| **TLT** | 1m | 13 | -1.3% | -0.8% | -6.5% | +3.7% | 31% |
| **TLT** | 3m | 13 | +0.1% | +0.6% | -16.2% | +12.6% | 54% |
| **TLT** | 6m | 13 | -2.8% | -3.1% | -17.2% | +9.1% | 38% |

**Episodes (последни 5 от 13):**
- `2024-06-21 → 2024-06-21` (1d)
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-28 → 2026-05-15` (11d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 1 · **Total matching days:** 29 · **History:** 2021-05-17 → 2026-05-15

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | +9.1% | +9.1% | +9.1% | +9.1% | 100% |
| **SPY** | 3m | 1 | +9.3% | +9.3% | +9.3% | +9.3% | 100% |
| **SPY** | 6m | 1 | +9.3% | +9.3% | +9.3% | +9.3% | 100% |
| **USO** | 1m | 1 | +7.2% | +7.2% | +7.2% | +7.2% | 100% |
| **USO** | 3m | 1 | +19.0% | +19.0% | +19.0% | +19.0% | 100% |
| **USO** | 6m | 1 | +19.0% | +19.0% | +19.0% | +19.0% | 100% |
| **GLD** | 1m | 1 | -0.2% | -0.2% | -0.2% | -0.2% | 0% |
| **GLD** | 3m | 1 | -4.0% | -4.0% | -4.0% | -4.0% | 0% |
| **GLD** | 6m | 1 | -4.0% | -4.0% | -4.0% | -4.0% | 0% |
| **TLT** | 1m | 1 | -0.6% | -0.6% | -0.6% | -0.6% | 0% |
| **TLT** | 3m | 1 | -3.4% | -3.4% | -3.4% | -3.4% | 0% |
| **TLT** | 6m | 1 | -3.4% | -3.4% | -3.4% | -3.4% | 0% |

**Episodes (последни 5 от 1):**
- `2026-04-08 → 2026-05-15` (29d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 7 · **Total matching days:** 743 · **History:** 2021-05-17 → 2026-05-15

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
- `2024-10-04 → 2026-05-15` (405d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-05-15

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 9 · **Total matching days:** 74 · **History:** 2021-05-17 → 2026-05-15

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 9 | +0.1% | +0.9% | -7.2% | +7.8% | 56% |
| **SPY** | 3m | 9 | +2.1% | +3.9% | -8.0% | +10.7% | 56% |
| **SPY** | 6m | 9 | +1.5% | +4.8% | -20.2% | +14.9% | 67% |
| **USO** | 1m | 9 | +3.4% | -1.6% | -15.0% | +52.9% | 33% |
| **USO** | 3m | 9 | +9.6% | -0.1% | -20.7% | +64.3% | 44% |
| **USO** | 6m | 9 | +11.4% | -0.2% | -27.6% | +64.3% | 44% |
| **GLD** | 1m | 9 | -2.2% | -1.6% | -8.3% | +1.9% | 11% |
| **GLD** | 3m | 9 | -1.2% | -0.0% | -10.9% | +6.4% | 44% |
| **GLD** | 6m | 9 | +0.1% | -0.8% | -11.4% | +25.0% | 33% |
| **TLT** | 1m | 9 | -2.0% | -2.4% | -5.7% | +2.6% | 11% |
| **TLT** | 3m | 9 | -6.1% | -5.7% | -16.9% | +5.4% | 22% |
| **TLT** | 6m | 9 | -9.0% | -6.1% | -21.7% | +3.4% | 11% |

**Episodes (последни 5 от 9):**
- `2023-04-12 → 2023-04-18` (5d)
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-04-09` (27d)
- `2026-04-29 → 2026-05-15` (5d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 16 · **Total matching days:** 275 · **History:** 2021-05-17 → 2026-05-15

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.2% | +2.2% | -4.8% | +9.0% | 75% |
| **SPY** | 3m | 16 | +3.6% | +4.4% | -12.3% | +16.7% | 75% |
| **SPY** | 6m | 16 | +7.2% | +8.2% | -13.5% | +21.9% | 81% |
| **USO** | 1m | 16 | +1.8% | -3.2% | -13.0% | +27.7% | 38% |
| **USO** | 3m | 16 | +3.5% | -1.7% | -14.5% | +29.9% | 38% |
| **USO** | 6m | 16 | +14.7% | +2.3% | -12.4% | +111.6% | 69% |
| **GLD** | 1m | 16 | +2.4% | +1.8% | -6.4% | +9.0% | 75% |
| **GLD** | 3m | 16 | +6.9% | +7.4% | -6.4% | +23.6% | 69% |
| **GLD** | 6m | 16 | +11.7% | +12.1% | -8.4% | +43.8% | 75% |
| **TLT** | 1m | 16 | +0.6% | +0.7% | -6.1% | +8.5% | 56% |
| **TLT** | 3m | 16 | -0.8% | -0.3% | -14.7% | +13.0% | 50% |
| **TLT** | 6m | 16 | -3.0% | -2.0% | -20.6% | +8.6% | 44% |

**Episodes (последни 5 от 16):**
- `2025-03-27 → 2025-05-08` (25d)
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-17 → 2026-04-23` (4d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 18 · **Total matching days:** 289 · **History:** 2021-05-17 → 2026-05-15

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 18 | +0.4% | +1.1% | -8.3% | +7.0% | 50% |
| **SPY** | 3m | 18 | +2.2% | +3.5% | -13.3% | +9.4% | 67% |
| **SPY** | 6m | 18 | +3.8% | +7.2% | -15.7% | +17.6% | 72% |
| **USO** | 1m | 18 | +0.6% | -3.7% | -14.3% | +55.8% | 44% |
| **USO** | 3m | 18 | +4.9% | -1.0% | -12.7% | +85.9% | 44% |
| **USO** | 6m | 18 | +10.4% | -0.1% | -16.0% | +85.9% | 50% |
| **GLD** | 1m | 18 | -0.3% | +0.0% | -12.4% | +7.6% | 50% |
| **GLD** | 3m | 18 | +1.9% | +1.5% | -13.4% | +19.0% | 67% |
| **GLD** | 6m | 18 | +8.4% | +6.0% | -15.8% | +55.5% | 72% |
| **TLT** | 1m | 18 | +0.1% | +0.3% | -5.5% | +5.5% | 56% |
| **TLT** | 3m | 18 | -3.0% | -4.0% | -16.8% | +9.8% | 39% |
| **TLT** | 6m | 18 | -5.5% | -6.1% | -20.5% | +6.7% | 28% |

**Episodes (последни 5 от 18):**
- `2024-10-10 → 2025-01-17` (52d)
- `2025-05-12 → 2025-05-19` (3d)
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-05-15

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (10 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **M2** | M2 паричен агрегат | liquidity | money_supply | 2 | 2.76 | 2.76 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | ✓ |
| **C_AND_I_LOANS** | Търговски и индустриални кредити (C&I) | liquidity | banking_credit | 2 | 2.55 | 2.56 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | ✓ |
| **CPI_SHELTER** | CPI — жилища (shelter) | inflation | goods_services | 2 | 2.46 | 2.46 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | ✓ |
| **DGORDER** | Нови поръчки за дълготрайни стоки | growth | hard_activity | 2 | 2.36 | 2.36 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | - |
| **CPI_SERVICES** | CPI — услуги (всички) | inflation | goods_services | 2 | 2.35 | 2.35 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | ✓ |
| **RSXFS** | Продажби на дребно (без храна) | growth | hard_activity | 2 | 2.33 | 2.33 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | ✓ |
| **UMCSENT** | Michigan Sentiment Index | growth | consumer_sentiment | 2 | 2.33 | 2.33 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | - |
| **PPICORE** | PPI Core (Final Demand без храни и енергия) | inflation | core_measures | 2 | 2.32 | 2.32 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | ✓ |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 2 | 2.31 | 2.31 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | ✓ |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 2 | 2.31 | 2.31 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | ✓ |

### EU (7 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_EMPLOYMENT_EXP** | Очаквания за заетост (3m напред) | labor | labor_sentiment | 2 | 3.14 | 3.14 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | ✓ |
| **EA_RETAIL_CONF** | Доверие в търговията на дребно (DG ECFIN) | growth | sentiment | 2 | 2.68 | 2.68 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | ✓ |
| **EA_COMP_PER_EMPLOYEE** | Компенсация на наетите (D1, EA-20, M€) | labor | wages | 2 | 2.39 | 2.39 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | ✓ |
| **EA_ESI** | Икономически Sentiment Indicator (DG ECFIN ESI) | growth | sentiment | 2 | 2.25 | 2.25 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | ✓ |
| **EA_CONSUMER_CONF** | Потребителско доверие (DG ECFIN, full history от 1985) | growth | sentiment | 2 | 2.10 | 2.10 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | - |
| **EA_RETAIL_VOL** | Търговия на дребно — обем на продажбите (G47, индекс 2021=100) | growth | hard_activity | 2 | 2.02 | 2.02 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | - |
| **EA_PPI_INTERMEDIATE** | PPI междинни стоки (MIG ING, индекс 2021=100) | inflation | producer_prices | 2 | 2.01 | 2.01 | 2026-05-15 00:00:00 | 2026-05-16 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-05-16 00:00:00 · **Generated:** 2026-05-16 18:46:20.874509+03:00

**Режим:** `stagflation_confirmed` (Стагфлация (потвърдена))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 65.6 | expanding | 65.6% | 4 | 3 |
| **growth** | 50.0 | mixed | 50.0% | 6 | 4 |
| **inflation** | 85.7 | expanding | 85.7% | 12 | 11 |
| **liquidity** | 41.7 | mixed | 41.7% | 3 | 2 |

### Top anomalies (10 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **M2** | M2 паричен агрегат | liquidity | money_supply | +2.76 | up | 22686.00 | 2026-03-01 | ✓ max |
| **C_AND_I_LOANS** | Търговски и индустриални кредити (C&I) | liquidity, growth | banking_credit | +2.56 | up | 2865.27 | 2026-04-01 | ✓ max |
| **CPI_SHELTER** | CPI — жилища (shelter) | inflation | goods_services | +2.46 | up | 426.64 | 2026-04-01 | ✓ max |
| **DGORDER** | Нови поръчки за дълготрайни стоки | growth | hard_activity | +2.36 | up | 318909.00 | 2026-03-01 | - |
| **CPI_SERVICES** | CPI — услуги (всички) | inflation | goods_services | +2.35 | up | 429.66 | 2026-04-01 | ✓ max |
| **RSXFS** | Продажби на дребно (без храна) | growth | hard_activity | +2.33 | up | 656115.00 | 2026-04-01 | ✓ max |
| **UMCSENT** | Michigan Sentiment Index | growth | consumer_sentiment | -2.33 | down | 53.30 | 2026-03-01 | - |
| **PPICORE** | PPI Core (Final Demand без храни и енергия) | inflation | core_measures | +2.32 | up | 267.86 | 2026-04-01 | ✓ max |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | +2.31 | up | 156.50 | 2026-04-01 | ✓ max |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.31 | down | 95.71 | 2026-01-01 | ✓ min |

### Narrative hints от макро лещите
- **M2**: M2 YoY → исторически корелира със inflation с 12-24 месечен lag. Но velocity-то варира; не е automatic signal.
- **C_AND_I_LOANS**: Бизнес заемане от банки. Water сигнал за capex intentions + credit supply. YoY crash често предхожда рецесия.
- **CPI_SHELTER**: Shelter е ~1/3 от CPI. OER методология lag-ва market rents с 12-18 месеца. При сривове на пазарни ренти shelter CPI упорито остава висок — дебатен signal.
- **DGORDER**: Aircraft orders са шумни (Boeing cycles). Preferred view: ex-transportation.
- **CPI_SERVICES**: Услугите са 60%+ от CPI. По-инертни от goods. Post-COVID инфлацията мигрира от стоки към услуги.
- **RSXFS**: Не е inflation-adjusted — внимавай при висока inflation (номинален ръст подвеждащ).
- **UMCSENT**: Known за dramatic bottoms. Силно корелира с election cycles, gas prices и post-2024 показва политически bias (D vs R) — гледай breadth с Conference Board/OECD proxy, не individual прочит.
- **PPICORE**: PPI core води CPI core с 1-3 месеца. Недостатъчно проследяван — силен индикатор при конвергенция или дивергенция с CPI core.
- **PPIFIS**: Производствени цени → consumer prices с 1-3 месечен lag. Водещ за CPI при трендови промени.
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.

### Cross-lens divergences (6 entries)
- 🔔 **?**
  - `pair_id`: stagflation_test
  - `name_bg`: Labor tightness × Inflation pressure
  - `question_bg`: Дали labor tightness потвърждава inflation pressure (стагфлация)?
  - `state`: both_up
  - `interpretation`: Стагфлация confirmation — labor tight + inflation hot.
  - `slot_a_label`: Labor tightness
  - `slot_b_label`: Inflation pressure
  - `breadth_a`: 0.9
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
  - `breadth_b`: 0.0
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Realized CPI × Expectations
  - `question_bg`: Дали expectations следват realized inflation, или стоят anchored?
  - `state`: both_up
  - `interpretation`: De-anchoring in progress — expectations следват realized up.
  - `slot_a_label`: Realized inflation
  - `slot_b_label`: Inflation expectations
  - `breadth_a`: 1.0
  - `breadth_b`: 1.0
- 🔔 **?**
  - `pair_id`: credit_policy_transmission
  - `name_bg`: Credit spreads × Policy rates
  - `question_bg`: Дали credit следва policy направление — transmission intact?
  - `state`: both_down
  - `interpretation`: Easing transmits — rates down + credit tightens.
  - `slot_a_label`: Credit stress
  - `slot_b_label`: Policy tightening
  - `breadth_a`: 0.0
  - `breadth_b`: 0.0
- 🔔 **?**
  - `pair_id`: sentiment_vs_hard_data
  - `name_bg`: Consumer sentiment × Hard activity
  - `question_bg`: Дали sentiment потвърждава hard data, или има разминаване?
  - `state`: a_down_b_up
  - `interpretation`: Activity OK, sentiment крачка — strategic pessimism / political bias.
  - `slot_a_label`: Consumer sentiment
  - `slot_b_label`: Hard activity
  - `breadth_a`: 0.0
  - `breadth_b`: 1.0
- 🔔 **?**
  - `pair_id`: model_vs_market
  - `name_bg`: Model-implied × Market-implied inflation
  - `question_bg`: Дали underlying persistence и market pricing-а са съгласни за инфлацията?
  - `state`: both_up
  - `interpretation`: Съгласие — underlying persistent + пазар pricing-ва inflation. Fed зад кривата.
  - `slot_a_label`: Модел (sticky inflation)
  - `slot_b_label`: Пазар (breakevens + survey)
  - `breadth_a`: 1.0
  - `breadth_b`: 1.0

### Executive narrative
> Картината показва потвърдена стагфлационна конфигурация — трудовият пазар остава tight, а инфлационният натиск е broad-based. Най-отклонена леща: Inflation — breadth 86% (разширяване), 12 аномалии, 11 нови екстремума. Expectations също нагоре — de-anchoring в ход, рискът ескалира. За наблюдение следващия релиз: M2, C_AND_I_LOANS, CPI_SHELTER (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: M2 z=+2.76 · NEW-5Y-MAX
- 13 нови екстремуми в top-15 (lookback 5г.)
- Активни двойки: Stagflation test=both_up; Growth × Labor=a_up_b_down; Inflation anchoring=both_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-05-16 00:00:00 · **Generated:** 2026-05-16 19:03:46.744213+03:00

**Режим:** `transition` (Преходно / смесено)  
**Primary driver:** `none`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 36.1 | mixed | 36.1% | 4 | 2 |
| **inflation** | 16.7 | contracting | 16.7% | 1 | 0 |

### Top anomalies (7 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_EMPLOYMENT_EXP** | Очаквания за заетост (3m напред) | labor | labor_sentiment | -3.14 | down | 91.70 | 2026-04-01 | ✓ min |
| **EA_RETAIL_CONF** | Доверие в търговията на дребно (DG ECFIN) | growth | sentiment | -2.68 | down | -9.90 | 2026-04-01 | ✓ min |
| **EA_COMP_PER_EMPLOYEE** | Компенсация на наетите (D1, EA-20, M€) | labor | wages | +2.39 | up | 1952296.20 | 2025-10-01 | ✓ max |
| **EA_ESI** | Икономически Sentiment Indicator (DG ECFIN ESI) | growth | sentiment | -2.25 | down | 93.00 | 2026-04-01 | ✓ min |
| **EA_CONSUMER_CONF** | Потребителско доверие (DG ECFIN, full history от 1985) | growth | sentiment | -2.10 | down | -20.60 | 2026-04-01 | - |
| **EA_RETAIL_VOL** | Търговия на дребно — обем на продажбите (G47, индекс 2021=100) | growth | hard_activity | +2.02 | up | 103.60 | 2026-03-01 | - |
| **EA_PPI_INTERMEDIATE** | PPI междинни стоки (MIG ING, индекс 2021=100) | inflation | producer_prices | +2.01 | up | 118.30 | 2026-03-01 | - |

### Narrative hints от макро лещите
- **EA_EMPLOYMENT_EXP**: DG ECFIN survey: forward-looking labor signal. Limited history (only 12 months in teibs030 dataset).
- **EA_RETAIL_CONF**: Sectoral confidence — retail. Limited history в teibs020.
- **EA_COMP_PER_EMPLOYEE**: Quarterly compensation of employees aggregate (EA-20). YoY growth е headline wage signal — lagged 1Q. Активира stagflation cross-lens срещу HICP services.
- **EA_ESI**: Composite sentiment indicator (ESI ≈ ISM PMI EA equivalent). Заместител на US PMI. Limited history в teibs010 (12 months).
- **EA_CONSUMER_CONF**: Pre-EMU история (1985+). Negative balance е норма; отклонения от mean показват consumer sentiment shifts.
- **EA_RETAIL_VOL**: Consumer spending proxy. По-стабилна от IP — services-driven EA.
- **EA_PPI_INTERMEDIATE**: Producer prices, intermediate goods (proxy за nonenergy PPI). Leading indicator на consumer goods inflation 3-6mo lag. Активира pipeline_inflation cross-lens срещу HICP core.

### Cross-lens divergences (6 entries)
- 🔔 **?**
  - `pair_id`: stagflation_test
  - `name_bg`: Стагфлационен тест
  - `question_bg`: Заплатите ли движат услугите нагоре?
  - `state`: insufficient_data
  - `interpretation`: Insufficient data в една от двете групи.
  - `slot_a_label`: Натиск от заплати
  - `slot_b_label`: Базова/услуги инфлация
  - `breadth_a`: None
  - `breadth_b`: 0.0
- 🔔 **?**
  - `pair_id`: ecb_transmission
  - `name_bg`: Трансмисия на ЕЦБ политиката
  - `question_bg`: ЕЦБ hike-овете стигат ли до банковото кредитиране?
  - `state`: transition
  - `interpretation`: Смесена картина — типично около policy turning points.
  - `slot_a_label`: Policy rates (DFR/MRO)
  - `slot_b_label`: Банково кредитиране (свиване)
  - `breadth_a`: 0.0
  - `breadth_b`: 0.5
- 🔔 **?**
  - `pair_id`: fragmentation_risk
  - `name_bg`: Фрагментационен риск
  - `question_bg`: ЕЦБ hike-овете разширяват ли периферните spreads?
  - `state`: insufficient_data
  - `interpretation`: Insufficient data в една от двете групи.
  - `slot_a_label`: Policy rates
  - `slot_b_label`: Sovereign spreads (BTP/OAT-Bund)
  - `breadth_a`: 0.0
  - `breadth_b`: None
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
  - `breadth_b`: 0.0
- 🔔 **?**
  - `pair_id`: sentiment_vs_hard_data
  - `name_bg`: Очаквания срещу твърди данни
  - `question_bg`: Sentiment отразява ли реалната икономика?
  - `state`: transition
  - `interpretation`: Sentiment turn обикновено leads hard data 3-6mo.
  - `slot_a_label`: Sentiment (ESI, confidence)
  - `slot_b_label`: Hard activity (IP, retail, GDP)
  - `breadth_a`: 0.222
  - `breadth_b`: 0.5

### Executive narrative
> Сигналите са в преход — няма доминираща конфигурация. Следващите 2-3 релиза ще ориентират посоката. Най-отклонена леща: Inflation — breadth 17% (свиване), 1 аномалии, 0 нови екстремума. За наблюдение следващия релиз: EA_EMPLOYMENT_EXP, EA_RETAIL_CONF, EA_COMP_PER_EMPLOYEE (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_EMPLOYMENT_EXP z=-3.14 · NEW-5Y-MIN
- 4 нови екстремуми в top-7 (lookback 5г.)



---

## 8. VRM — пълен текущ snapshot

### VRM_STATE (current)
| Field | Value |
|---|---|
| `date` | 2026-05-16 00:00:00 |
| `regime` | REFLATION |
| `ks_status` | inactive |
| `alignment_score` | 7.0 |
| `alignment_total` | 8 |
| `gms_value` | 0.0 |
| `last_updated_md` | 2026-05-16 00:00:00 |
| `is_change_day` | True |

### VRM_WEEK (current)
| Field | Value |
|---|---|
| `date` | 2026-05-16 00:00:00 |
| `week_start` | 2026-04-25 00:00:00 |
| `week_end` | 2026-05-01 00:00:00 |
| `approved` | True |
| `regime` | REFLATION |
| `regime_bg` | РЕФЛАЦИЯ |
| `signal` | ЗАЩИТИ (KS активен) |
| `alignment` | 6.0 |
| `alignment_label` | УМЕРЕН-ЧИСТ |
| `gms_score` | 3.0 |
| `gms_label` | MEDIUM |
| `ks_active` | True |
| `ks_variant` | A |
| `ks_weeks_active` | 4.0 |
| `ks_portfolio` | TLT 60% / GLD 30% / IEF 10% |
| `ks_eu_portfolio` | IDTL 60% / IGLN 30% / IBTM 10% |
| `spy_4w` | +12.09% |
| `qqq_4w` | +16.94% |
| `xle_4w` | -9.20% |
| `gld_4w` | +4.52% |
| `tlt_4w` | +1.25% |
| `tip_4w` | +1.93% |
| `iwm_4w` | +13.21% |



---

## 9. Rotation events — US + EU, пълни списъци

### US (period: 2026-05-08 → 2026-05-15)

**stable_winner (1m):** +12 entered, -12 exited
  - **Entered:** CVS, DG, EXPE, HII, IBKR, LRCX, NEM, O, SPG, STLD, ULTA, WMT _(включително 6 за първи път в историята: DG, HII, LRCX, NEM, STLD, ULTA)_
  - **Exited:** ADM, APA, BG, CBRE, GS, IVZ, NTRS, PLD, RL, ROK, TPR, WBD

**stable_winner (3m):** +3 entered, -3 exited
  - **Entered:** EXPE, STLD, WELL _(включително 3 за първи път в историята: EXPE, STLD, WELL)_
  - **Exited:** BKR, GLW, WBD

**quality_dip (1m):** +13 entered, -14 exited
  - **Entered:** ADM, APA, BG, CBRE, GS, IVZ, LVS, NTRS, PLD, RL, ROK, TPR, WBD _(включително 9 за първи път в историята: ADM, APA, BG, CBRE, IVZ, LVS, NTRS, PLD, ROK)_
  - **Exited:** BKR, CVS, DG, EXPE, HII, IBKR, LRCX, NEM, O, PLTR, SPG, STLD, ULTA, WMT

**quality_dip (3m):** +3 entered, -4 exited
  - **Entered:** GLW, LVS, WBD _(включително 1 за първи път в историята: LVS)_
  - **Exited:** EXPE, PLTR, STLD, WELL

**faded_bounce (1m):** +10 entered, -21 exited
  - **Entered:** APO, CMG, CNC, IEX, KKR, LII, PAYX, PEG, PYPL, TTD _(включително 1 за първи път в историята: CNC)_
  - **Exited:** ACN, ADBE, BRO, CAG, CLX, CRM, DECK, GDDY, HPQ, HRL, LEN, LYB, MAS, OXY, PCG, SBUX, SW, SWK, XYZ, ZBRA, ZTS

**faded_bounce (3m):** +6 entered, -10 exited
  - **Entered:** AVB, IFF, KMB, PAYX, PYPL, VRSK _(включително 3 за първи път в историята: IFF, KMB, VRSK)_
  - **Exited:** ALGN, CPAY, IR, PCG, RVTY, SBUX, SW, SWK, WY, XYZ

### EU (period: 2026-05-08 → 2026-05-15)

**stable_winner (1m):** +27 entered, -18 exited
  - **Entered:** ANA.MC, AYV.PA, BBVA.MC, BGEO.L, BKT.MC, CABK.MC, CBK.DE, EBS.VI, FR.PA, FRES.L, GAW.L, GBF.DE, HOC.L, IG.MI, KER.PA, LLOY.L, MAP.MC, NKT.CO, NXT.L, ORK.OL, RBI.VI, RR.L, SAN.MC, SBMO.AS, STAN.L, UNI.MC, URW.PA _(включително 14 за първи път в историята: AYV.PA, BGEO.L, CBK.DE, FR.PA, FRES.L, GBF.DE, HOC.L, IG.MI, MAP.MC, NKT.CO, ORK.OL, RR.L, SAN.MC, SBMO.AS)_
  - **Exited:** AAF.L, AVOL.SW, BAMI.MI, BIRG.IR, BMED.MI, BPE.MI, DLG.MI, HM-B.ST, JYSK.CO, KGH.WA, LTMC.MI, MANTA.HE, MBK.WA, NDX1.DE, PKN.WA, SPSN.SW, TPRO.MI, WRT1V.HE

**stable_winner (3m):** +6 entered, -6 exited
  - **Entered:** BGEO.L, EBS.VI, GAW.L, MOBN.SW, NKT.CO, VOE.VI _(включително 3 за първи път в историята: GAW.L, NKT.CO, VOE.VI)_
  - **Exited:** BAMI.MI, BATS.L, SBRY.L, SRP.L, TPRO.MI, UMI.BR

**quality_dip (1m):** +16 entered, -28 exited
  - **Entered:** AAF.L, AVOL.SW, BAMI.MI, BIRG.IR, BMED.MI, BPE.MI, DLG.MI, HM-B.ST, JYSK.CO, KGH.WA, LTMC.MI, NDX1.DE, PKN.WA, SPSN.SW, TPRO.MI, WRT1V.HE _(включително 8 за първи път в историята: AVOL.SW, BMED.MI, BPE.MI, JYSK.CO, KGH.WA, LTMC.MI, NDX1.DE, WRT1V.HE)_
  - **Exited:** AG1.DE, ANA.MC, AYV.PA, BBVA.MC, BGEO.L, BKT.MC, CABK.MC, CBK.DE, EBS.VI, FR.PA, FRES.L, GAW.L, GBF.DE, HOC.L, IG.MI, KER.PA, LLOY.L, MAP.MC, NXT.L, ORK.OL, RBI.VI, RKT.L, RR.L, SAN.MC, SBMO.AS, STAN.L, UNI.MC, URW.PA

**quality_dip (3m):** +6 entered, -9 exited
  - **Entered:** BAMI.MI, BATS.L, SBRY.L, SRP.L, TPRO.MI, UMI.BR _(включително 2 за първи път в историята: TPRO.MI, UMI.BR)_
  - **Exited:** AG1.DE, BGEO.L, EBS.VI, GAW.L, MANTA.HE, MBK.WA, MOBN.SW, RKT.L, VOE.VI

**faded_bounce (1m):** +26 entered, -16 exited
  - **Entered:** AKE.PA, BC.MI, CVC.AS, DB1.DE, DHER.DE, DLN.L, DSY.PA, EDEN.PA, EZJ.L, ITRK.L, LEG.DE, LGEN.L, LSEG.L, MF.PA, MNDI.L, MUV2.DE, PUM.DE, RAA.DE, REL.L, RI.PA, SGO.PA, SIKA.SW, SY1.DE, TEP.PA, WISE.L, WKL.AS _(включително 13 за първи път в историята: BC.MI, DHER.DE, DSY.PA, EZJ.L, ITRK.L, LEG.DE, MF.PA, MNDI.L, RAA.DE, RI.PA, SGO.PA, SIKA.SW, SY1.DE)_
  - **Exited:** BAER.SW, BEI.DE, BME.L, EQT.ST, LUND-B.ST, ORSTED.CO, RACE.MI, ROCK-B.CO, SFSN.SW, SREN.SW, STLAM.MI, SW.PA, TRYG.CO, VZN.SW, WALL-B.ST, WIHL.ST

**faded_bounce (3m):** +5 entered, -4 exited
  - **Entered:** BC.MI, EXO.AS, ITRK.L, SWEC-B.ST, TOM.OL _(включително 4 за първи път в историята: BC.MI, ITRK.L, SWEC-B.ST, TOM.OL)_
  - **Exited:** BEI.DE, GFC.PA, MNDI.L, VER.VI



---

## 10. COT positioning — текуща картина (cot_monitor + cot_cta)

### COT Monitor (38 markets) (snapshot: 2026-05-15 00:00:00)
| Market | Asset class | Net position | Net % | Percentile 5y | Weekly change |
|---|---|---:|---:|---:|---:|
| **soyoil** | Commodities | 162287 | 99.4 | 99.4 | 13967 |
| **soybeans** | Commodities | 214815 | 98.1 | 98.1 | 39664 |
| **aud** | FX | 55851 | 96.2 | 96.2 | 12209 |
| **soymeal** | Commodities | 116082 | 95.4 | 95.4 | -19661 |
| **cattle** | Commodities | 130886 | 92.7 | 92.7 | -5756 |
| **brent** | Commodities | 18394 | 90.1 | 90.1 | 1638 |
| **corn** | Commodities | 299483 | 89.3 | 89.3 | 140000 |
| **copper** | Commodities | 73523 | 87.9 | 87.9 | 21386 |
| **gbpfx** | FX | 37302 | 85.4 | 85.4 | 14971 |
| **eurfx** | FX | 18003 | 82.0 | 82.0 | -7379 |
| **rbob** | Commodities | 63743 | 75.3 | 75.3 | 6431 |
| **platinum** | Commodities | 16132 | 73.8 | 73.8 | -128 |
| **us30y** | Rates | -296196 | 70.4 | 70.4 | -90678 |
| **cotton** | Commodities | 59570 | 67.8 | 67.8 | 42745 |
| **wheat** | Commodities | -19023 | 61.3 | 61.3 | -11757 |
| **vix** | Volatility | -47579 | 60.0 | 60.0 | -17757 |
| **coffee** | Commodities | 25028 | 55.2 | 55.2 | -1321 |
| **hogs** | Commodities | 40860 | 50.2 | 50.2 | -47027 |
| **us5y** | Rates | -2349205 | 48.0 | 48.0 | 105913 |
| **dxy** | FX | -4751 | 40.8 | 40.8 | -1656 |
| **usultra10y** | Rates | -250455 | 39.0 | 39.0 | 38873 |
| **gold** | Commodities | 100627 | 38.5 | 38.5 | 1777 |
| **us2y** | Rates | -1947829 | 36.8 | 36.8 | 131371 |
| **silver** | Commodities | 16195 | 34.9 | 34.9 | 5149 |
| **heatingoil** | Commodities | 9606 | 32.0 | 32.0 | -7139 |
| **palladium** | Commodities | -1924 | 31.8 | 31.8 | -204 |
| **chf** | FX | -7708 | 27.8 | 27.8 | -4287 |
| **cad** | FX | -37663 | 26.4 | 26.4 | 23741 |
| **bitcoin** | Crypto | -11070 | 24.4 | 24.4 | -831 |
| **natgas** | Commodities | -7516 | 24.1 | 24.1 | 388 |
| **russell** | US Equities | -60631 | 23.9 | 23.9 | -9895 |
| **us10y** | Rates | -1956942 | 22.4 | 22.4 | 53029 |
| **cocoa** | Commodities | -13969 | 19.9 | 19.9 | 4136 |
| **sugar** | Commodities | -100456 | 19.0 | 19.0 | 41880 |
| **jpy** | FX | -62440 | 16.1 | 16.1 | -7995 |
| **wti** | Commodities | -34251 | 12.8 | 12.8 | 3411 |
| **sp500** | US Equities | -432438 | 9.0 | 9.0 | -12082 |
| **nasdaq** | US Equities | -73737 | 0.2 | 0.2 | -14845 |

### COT/CTA Positioning (11 markets) (snapshot: 2026-05-15 00:00:00)
| Market | Asset class | Net position | Net % | Percentile 5y | Weekly change |
|---|---|---:|---:|---:|---:|
| **corn** | Commodities | 299483 | 95.5 | 95.5 | 140000 |
| **eurfx** | FX | 18003 | 68.6 | 68.6 | -7379 |
| **bitcoin** | Crypto | -11070 | 66.0 | 66.0 | -831 |
| **gbpfx** | FX | 37302 | 62.8 | 62.8 | 14971 |
| **wti** | Commodities | -34251 | 43.0 | 43.0 | 3411 |
| **dxy** | FX | -4751 | 38.5 | 38.5 | -1656 |
| **us10y** | Rates | -1956942 | 32.0 | 32.0 | 53029 |
| **gold** | Commodities | 100627 | 25.0 | 25.0 | 1777 |
| **vix** | Volatility | -47579 | 18.6 | 18.6 | -17757 |
| **sp500** | US Equities | -432438 | 13.5 | 13.5 | -12082 |
| **nasdaq** | US Equities | -73737 | 0.6 | 0.6 | -14845 |



---

## 11. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MU** | Technology | 96.7 | 70.1% | 87.5% | 222.1% | 702.5% | 3.31 | -30.3% |
| 2 | **SNDK** | Technology | 96.7 | 55.1% | 119.4% | 409.1% | 3192.2% | 3.62 | -31.3% |
| 3 | **INTC** | Technology | 96.1 | 78.5% | 149.4% | 206.1% | 413.9% | 2.30 | -24.2% |
| 4 | **STX** | Technology | 96.1 | 54.9% | 87.0% | 180.7% | 672.9% | 3.30 | -21.0% |
| 5 | **WDC** | Technology | 95.8 | 34.0% | 72.3% | 188.1% | 902.4% | 3.67 | -20.6% |
| 6 | **AMD** | Technology | 95.7 | 74.2% | 118.4% | 89.3% | 299.9% | 2.15 | -27.8% |
| 7 | **CIEN** | Technology | 95.3 | 24.3% | 101.9% | 185.2% | 634.0% | 3.09 | -16.8% |
| 8 | **COHR** | Technology | 95.1 | 31.4% | 87.4% | 156.3% | 413.2% | 2.30 | -26.5% |
| 9 | **GLW** | Technology | 94.9 | 23.8% | 58.7% | 138.1% | 344.0% | 2.89 | -23.0% |
| 10 | **LITE** | Technology | 94.9 | 21.6% | 71.7% | 296.8% | 1244.5% | 3.14 | -28.7% |
| 11 | **FIX** | Industrials | 94.8 | 23.9% | 57.2% | 114.2% | 340.2% | 2.82 | -13.8% |
| 12 | **VRT** | Industrials | 94.4 | 24.9% | 59.1% | 110.2% | 256.8% | 2.21 | -24.8% |
| 13 | **ON** | Technology | 94.3 | 63.4% | 67.6% | 144.4% | 158.6% | 1.74 | -28.1% |
| 14 | **PWR** | Industrials | 94.3 | 31.8% | 51.2% | 73.8% | 127.3% | 2.23 | -11.7% |
| 15 | **CSCO** | Technology | 94.0 | 40.3% | 54.9% | 62.9% | 91.3% | 2.07 | -13.6% |
| 16 | **DELL** | Technology | 94.0 | 40.3% | 120.4% | 80.0% | 133.3% | 1.56 | -32.3% |
| 17 | **KEYS** | Technology | 92.4 | 11.2% | 57.5% | 98.2% | 119.0% | 2.03 | -14.0% |
| 18 | **ADI** | Technology | 91.9 | 22.7% | 29.2% | 84.1% | 91.2% | 2.06 | -15.7% |
| 19 | **LRCX** | Technology | 91.6 | 12.8% | 29.5% | 88.5% | 253.5% | 2.50 | -20.0% |
| 20 | **AMAT** | Technology | 91.5 | 11.7% | 34.3% | 93.3% | 156.9% | 1.97 | -21.4% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **HUBN.SW** | Industrials | 95.2 | 41.0% | 63.0% | 92.7% | 290.5% | 3.53 | -13.5% |
| 2 | **NOKIA.HE** | Technology | 94.9 | 38.9% | 100.4% | 103.0% | 173.4% | 2.20 | -27.6% |
| 3 | **PRY.MI** | Industrials | 94.7 | 29.1% | 52.6% | 92.3% | 179.8% | 2.76 | -11.9% |
| 4 | **AIXA.DE** | Technology | 94.7 | 57.5% | 150.8% | 216.1% | 324.7% | 2.36 | -28.4% |
| 5 | **STMMI.MI** | Technology | 94.0 | 58.6% | 91.7% | 175.9% | 140.6% | 1.78 | -33.5% |
| 6 | **IFX.DE** | Technology | 93.4 | 53.1% | 57.6% | 102.2% | 102.8% | 1.67 | -21.2% |
| 7 | **BESI.AS** | Technology | 92.4 | 23.1% | 57.0% | 94.8% | 142.1% | 1.73 | -20.9% |
| 8 | **HOT.DE** | Industrials | 92.4 | 14.9% | 43.6% | 96.3% | 230.6% | 2.91 | -12.5% |
| 9 | **UMI.BR** | Basic Materials | 92.0 | 51.7% | 38.1% | 58.1% | 209.3% | 2.31 | -28.7% |
| 10 | **SPM.MI** | Energy | 91.6 | 11.5% | 41.5% | 111.6% | 120.8% | 2.48 | -14.7% |
| 11 | **ACS.MC** | Industrials | 91.0 | 10.0% | 37.6% | 76.4% | 137.4% | 2.78 | -9.9% |
| 12 | **NESTE.HE** | Energy | 90.8 | 11.6% | 40.7% | 68.3% | 218.7% | 2.65 | -20.4% |
| 13 | **NDA.DE** | Basic Materials | 90.8 | 15.6% | 26.7% | 92.0% | 175.6% | 2.83 | -15.3% |
| 14 | **SUBC.OL** | Energy | 89.8 | 6.6% | 32.7% | 82.2% | 118.5% | 2.73 | -11.3% |
| 15 | **VK.PA** | Energy | 89.7 | 15.7% | 44.9% | 65.2% | 77.6% | 1.90 | -13.0% |
| 16 | **ASM.AS** | Technology | 88.6 | 20.0% | 29.7% | 69.4% | 88.5% | 1.43 | -26.2% |
| 17 | **PKN.WA** | Energy | 88.4 | 13.0% | 29.0% | 47.4% | 114.9% | 2.44 | -11.9% |
| 18 | **NDX1.DE** | Industrials | 88.3 | 2.3% | 41.2% | 67.4% | 164.5% | 2.18 | -16.1% |
| 19 | **ABBN.SW** | Industrials | 87.7 | 15.8% | 22.5% | 45.3% | 86.7% | 2.27 | -12.1% |
| 20 | **KGH.WA** | Basic Materials | 87.5 | 16.1% | 15.0% | 96.7% | 191.4% | 2.19 | -30.8% |



---

## 12. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **APA** | Energy | 0.792 | 0.943 | 0.762 | 0.862 | 0.433 | +130.8% | 9.1 | +26.2% |
| 2 | **SNDK** | Information Technology | 0.755 | 0.999 | 0.850 | 0.500 | 0.500 | +3380.7% | 48.0 | +39.3% |
| 3 | **CF** | Materials | 0.741 | 0.887 | 0.708 | 0.751 | 0.499 | +46.0% | 11.3 | +27.3% |
| 4 | **EOG** | Energy | 0.737 | 0.800 | 0.640 | 0.809 | 0.685 | +25.8% | 13.8 | +18.2% |
| 5 | **TROW** | Financials | 0.725 | 0.610 | 0.735 | 0.878 | 0.681 | +9.6% | 10.9 | +18.7% |
| 6 | **MNST** | Consumer Staples | 0.693 | 0.764 | 0.757 | 0.500 | 0.742 | +38.6% | 42.1 | +26.7% |
| 7 | **FTNT** | Information Technology | 0.692 | 0.834 | 0.881 | 0.500 | 0.349 | +17.4% | 47.6 | +132.4% |
| 8 | **CBOE** | Financials | 0.690 | 0.897 | 0.788 | 0.265 | 0.789 | +65.2% | 31.1 | +25.1% |
| 9 | **BMY** | Health Care | 0.690 | 0.635 | 0.767 | 0.731 | 0.579 | +28.0% | 16.0 | +38.7% |
| 10 | **PFG** | Financials | 0.690 | 0.767 | 0.500 | 0.790 | 0.748 | +28.0% | 14.4 | +13.4% |
| 11 | **NEM** | Materials | 0.688 | 0.620 | 0.862 | 0.685 | 0.486 | +120.5% | 14.1 | +25.8% |
| 12 | **FFIV** | Information Technology | 0.682 | 0.858 | 0.664 | 0.500 | 0.671 | +27.3% | 29.8 | +20.3% |
| 13 | **GL** | Financials | 0.681 | 0.737 | 0.500 | 0.740 | 0.834 | +28.1% | 10.7 | +20.5% |
| 14 | **HST** | Real Estate | 0.679 | 0.793 | 0.519 | 0.758 | 0.636 | +45.1% | 14.5 | +14.9% |
| 15 | **SPG** | Real Estate | 0.678 | 0.669 | 0.891 | 0.537 | 0.507 | +27.2% | 13.9 | +113.6% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **NRG** | Utilities | 0.130 | 0.128 | 0.115 | 0.139 | 0.148 |
| 502 | **BLDR** | Industrials | 0.211 | 0.036 | 0.175 | 0.500 | 0.154 |
| 501 | **GPC** | Consumer Discretionary | 0.222 | 0.074 | 0.111 | 0.498 | 0.278 |
| 500 | **CSGP** | Real Estate | 0.232 | 0.031 | 0.107 | 0.500 | 0.438 |
| 499 | **AXON** | Industrials | 0.247 | 0.165 | 0.124 | 0.500 | 0.237 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W20.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W20.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-05-11  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
