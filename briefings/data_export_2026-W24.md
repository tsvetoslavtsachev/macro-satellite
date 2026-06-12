# Сателит — пълен data export за 2026-W24

_Период: 2026-06-08 → 2026-06-14_  
_Генериран: 2026-06-12 10:16 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W24.md` (structured briefing) и `narrative_2026-W24.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**4 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **XLP** | +2.19% | +1.62σ | 83.44 | 85.27 | 2026-06-05 | 2026-06-11 | -0.16% | +1.45% | 13 |
| **IEF** | +0.77% | +1.20σ | 93.62 | 94.34 | 2026-06-05 | 2026-06-11 | -0.17% | +0.78% | 13 |
| **SHY** | +0.28% | +1.15σ | 81.86 | 82.09 | 2026-06-05 | 2026-06-11 | -0.04% | +0.28% | 13 |
| **TLT** | +1.08% | +1.01σ | 85.06 | 85.98 | 2026-06-05 | 2026-06-11 | -0.23% | +1.30% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_5 канонични patterns от `config/divergence_rules.yaml`, evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-06-14 · **Conditions matched:** 1/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | -3.15% | ❌ | 133.02 | 128.83 | 2026-06-05 | 2026-06-11 |
| DFEN | down ≥ 3.0% | +7.70% | ❌ | 68.92 | 74.23 | 2026-06-05 | 2026-06-11 |
| GLD | down ≥ 1.0% | -2.50% | ✅ | 396.24 | 386.32 | 2026-06-05 | 2026-06-11 |
| URA | down ≥ 3.0% | -1.06% | ❌ | 45.31 | 44.83 | 2026-06-05 | 2026-06-11 |
| UUP | up ≥ 0.5% | -0.25% | ❌ | 28.02 | 27.95 | 2026-06-05 | 2026-06-11 |

### Ликвидна стес (flight to quality) (`liquidity_stress`) — не активен
_Дългосрочни trezuri нагоре, високодоходен кредит надолу, злато нагоре. Класически risk-off._  
**Window:** 7d ending 2026-06-14 · **Conditions matched:** 1/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| TLT | up ≥ 1.0% | +1.08% | ✅ | 85.06 | 85.98 | 2026-06-05 | 2026-06-11 |
| HYG | down ≥ 0.5% | +0.64% | ❌ | 79.43 | 79.94 | 2026-06-05 | 2026-06-11 |
| GLD | up ≥ 1.0% | -2.50% | ❌ | 396.24 | 386.32 | 2026-06-05 | 2026-06-11 |
| UUP | up ≥ 0.3% | -0.25% | ❌ | 28.02 | 27.95 | 2026-06-05 | 2026-06-11 |

### Възстановяване на инфлационни очаквания (`inflation_pickup`) — не активен
_Inflation-protected треzuri нагоре, commodities нагоре, dollar надолу. Repricing на real rates._  
**Window:** 7d ending 2026-06-14 · **Conditions matched:** 0/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| DBC | up ≥ 1.5% | -1.30% | ❌ | 29.23 | 28.85 | 2026-06-05 | 2026-06-11 |
| GLD | up ≥ 1.0% | -2.50% | ❌ | 396.24 | 386.32 | 2026-06-05 | 2026-06-11 |
| UUP | down ≥ 0.5% | -0.25% | ❌ | 28.02 | 27.95 | 2026-06-05 | 2026-06-11 |
| TLT | down ≥ 1.0% | +1.08% | ❌ | 85.06 | 85.98 | 2026-06-05 | 2026-06-11 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — 🔔 ТРИГГЕРИРАН
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-06-14 · **Conditions matched:** 3/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | +3.11% | ✅ | 281.65 | 290.41 | 2026-06-05 | 2026-06-11 |
| XLF | up ≥ 1.0% | +0.61% | ❌ | 52.30 | 52.62 | 2026-06-05 | 2026-06-11 |
| XLY | up ≥ 1.0% | +1.25% | ✅ | 114.86 | 116.30 | 2026-06-05 | 2026-06-11 |
| GLD | down ≥ 0.5% | -2.50% | ✅ | 396.24 | 386.32 | 2026-06-05 | 2026-06-11 |

### Защитен pivot (staples + utilities + gold) (`defensive_pivot`) — не активен
_XLP + XLU + GLD едновременно нагоре. Smart money flight to defensives без credit panic._  
**Window:** 7d ending 2026-06-14 · **Conditions matched:** 1/3

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| XLP | up ≥ 1.0% | +2.19% | ✅ | 83.44 | 85.27 | 2026-06-05 | 2026-06-11 |
| XLU | up ≥ 1.0% | -0.68% | ❌ | 44.35 | 44.05 | 2026-06-05 | 2026-06-11 |
| GLD | up ≥ 1.0% | -2.50% | ❌ | 396.24 | 386.32 | 2026-06-05 | 2026-06-11 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2023-W05 (week ending 2023-02-05)
**Cosine similarity:** 0.8679 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -3.41% | +0.45% | +9.17% |
| **USO** | +5.36% | -2.13% | +14.58% |
| **GLD** | -2.79% | +8.07% | +3.88% |
| **TLT** | -4.43% | -0.95% | -8.11% |
| **XLE** | -0.21% | -5.69% | +3.07% |
| **IWM** | -5.32% | -11.12% | -0.79% |

### Паралел #2: 2025-W26 (week ending 2025-06-29)
**Cosine similarity:** 0.8294 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.31% | +7.93% | +12.91% |
| **USO** | +8.90% | +5.10% | -6.55% |
| **GLD** | +1.67% | +15.11% | +38.35% |
| **TLT** | +0.29% | +2.89% | +3.03% |
| **XLE** | +4.28% | +8.76% | +5.41% |
| **IWM** | +3.35% | +12.32% | +17.40% |

### Паралел #3: 2024-W18 (week ending 2024-05-05)
**Cosine similarity:** 0.8293 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.34% | +4.56% | +12.39% |
| **USO** | -5.38% | -2.32% | -4.14% |
| **GLD** | +1.08% | +5.81% | +18.55% |
| **TLT** | +3.50% | +10.48% | +3.13% |
| **XLE** | -2.90% | -3.74% | -3.35% |
| **IWM** | +0.03% | +3.77% | +9.13% |

### Паралел #4: 2025-W18 (week ending 2025-05-04)
**Cosine similarity:** 0.8063 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.18% | +10.02% | +21.03% |
| **USO** | +9.19% | +21.01% | +13.36% |
| **GLD** | +3.67% | +3.74% | +23.54% |
| **TLT** | -2.74% | +1.24% | +4.84% |
| **XLE** | +1.95% | +5.25% | +9.30% |
| **IWM** | +4.26% | +7.50% | +23.51% |

### Паралел #5: 2023-W49 (week ending 2023-12-10)
**Cosine similarity:** 0.8052 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.39% | +11.65% | +16.87% |
| **USO** | +1.29% | +10.27% | +9.75% |
| **GLD** | +1.23% | +8.61% | +13.98% |
| **TLT** | +2.53% | +2.23% | -1.28% |
| **XLE** | +1.12% | +8.25% | +11.38% |
| **IWM** | +4.76% | +11.13% | +8.38% |

### Паралел #6: 2025-W22 (week ending 2025-06-01)
**Cosine similarity:** 0.7612 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.10% | +9.77% | +16.61% |
| **USO** | +10.10% | +11.45% | +5.84% |
| **GLD** | +1.30% | +4.77% | +27.76% |
| **TLT** | +2.92% | +1.51% | +6.89% |
| **XLE** | +5.67% | +11.77% | +12.80% |
| **IWM** | +6.60% | +14.99% | +21.98% |

### Паралел #7: 2024-W48 (week ending 2024-12-01)
**Cosine similarity:** 0.7492 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -2.41% | -1.06% | -1.56% |
| **USO** | +5.50% | +5.04% | -6.23% |
| **GLD** | -1.41% | +7.20% | +23.62% |
| **TLT** | -6.38% | -0.56% | -6.21% |
| **XLE** | -9.58% | -3.94% | -13.27% |
| **IWM** | -8.37% | -10.99% | -14.77% |

### Паралел #8: 2022-W27 (week ending 2022-07-10)
**Cosine similarity:** 0.7321 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.84% | -6.28% | +0.72% |
| **USO** | -6.48% | -4.38% | -17.46% |
| **GLD** | +3.02% | -2.72% | +7.03% |
| **TLT** | +4.98% | -9.66% | -5.23% |
| **XLE** | +5.36% | +16.55% | +26.04% |
| **IWM** | +8.31% | -3.48% | +2.13% |

### Паралел #9: 2021-W31 (week ending 2021-08-08)
**Cosine similarity:** 0.7181 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.03% | +6.22% | +2.09% |
| **USO** | +0.99% | +18.88% | +36.45% |
| **GLD** | +1.86% | +3.16% | +2.56% |
| **TLT** | -0.45% | +1.41% | -5.22% |
| **XLE** | -2.38% | +19.10% | +42.68% |
| **IWM** | +1.34% | +8.57% | -10.66% |

### Паралел #10: 2024-W34 (week ending 2024-08-25)
**Cosine similarity:** 0.7051 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.94% | +6.26% | +7.41% |
| **USO** | -2.99% | -1.72% | -0.26% |
| **GLD** | +6.06% | +7.68% | +16.69% |
| **TLT** | +0.59% | -7.22% | -7.01% |
| **XLE** | -0.84% | +8.50% | +2.28% |
| **IWM** | +0.34% | +8.71% | -0.54% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 13 · **Total matching days:** 72 · **History:** 2021-05-17 → 2026-06-11

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 13 | +2.0% | +1.7% | -3.1% | +7.7% | 77% |
| **SPY** | 3m | 13 | +3.2% | +3.7% | -7.0% | +12.1% | 77% |
| **SPY** | 6m | 13 | +8.1% | +11.6% | -6.1% | +22.7% | 77% |
| **USO** | 1m | 13 | +1.0% | -0.8% | -7.2% | +12.7% | 46% |
| **USO** | 3m | 13 | -0.8% | +0.1% | -18.9% | +24.5% | 54% |
| **USO** | 6m | 13 | +12.1% | +0.0% | -8.7% | +109.4% | 54% |
| **GLD** | 1m | 13 | +2.5% | +0.9% | -2.2% | +8.9% | 77% |
| **GLD** | 3m | 13 | +5.8% | +5.9% | -13.1% | +24.5% | 69% |
| **GLD** | 6m | 13 | +6.3% | +10.3% | -13.1% | +25.3% | 69% |
| **TLT** | 1m | 13 | -1.1% | -0.8% | -6.5% | +3.7% | 31% |
| **TLT** | 3m | 13 | +0.5% | +0.6% | -16.2% | +12.6% | 54% |
| **TLT** | 6m | 13 | -2.4% | -0.5% | -17.2% | +9.1% | 38% |

**Episodes (последни 5 от 13):**
- `2024-06-21 → 2024-06-21` (1d)
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-28 → 2026-05-19` (13d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 1 · **Total matching days:** 47 · **History:** 2021-05-17 → 2026-06-11

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | +9.1% | +9.1% | +9.1% | +9.1% | 100% |
| **SPY** | 3m | 1 | +9.1% | +9.1% | +9.1% | +9.1% | 100% |
| **SPY** | 6m | 1 | +9.1% | +9.1% | +9.1% | +9.1% | 100% |
| **USO** | 1m | 1 | +7.2% | +7.2% | +7.2% | +7.2% | 100% |
| **USO** | 3m | 1 | +3.4% | +3.4% | +3.4% | +3.4% | 100% |
| **USO** | 6m | 1 | +3.4% | +3.4% | +3.4% | +3.4% | 100% |
| **GLD** | 1m | 1 | -0.2% | -0.2% | -0.2% | -0.2% | 0% |
| **GLD** | 3m | 1 | -11.1% | -11.1% | -11.1% | -11.1% | 0% |
| **GLD** | 6m | 1 | -11.1% | -11.1% | -11.1% | -11.1% | 0% |
| **TLT** | 1m | 1 | -0.6% | -0.6% | -0.6% | -0.6% | 0% |
| **TLT** | 3m | 1 | -0.7% | -0.7% | -0.7% | -0.7% | 0% |
| **TLT** | 6m | 1 | -0.7% | -0.7% | -0.7% | -0.7% | 0% |

**Episodes (последни 5 от 1):**
- `2026-04-08 → 2026-06-11` (47d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 7 · **Total matching days:** 762 · **History:** 2021-05-17 → 2026-06-11

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
- `2024-10-04 → 2026-06-11` (424d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-06-11

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 9 · **Total matching days:** 76 · **History:** 2021-05-17 → 2026-06-11

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 9 | +0.4% | +0.9% | -7.2% | +7.8% | 56% |
| **SPY** | 3m | 9 | +2.4% | +3.7% | -8.0% | +12.0% | 56% |
| **SPY** | 6m | 9 | +1.5% | +4.8% | -20.2% | +14.9% | 67% |
| **USO** | 1m | 9 | +2.0% | -1.7% | -15.0% | +52.9% | 33% |
| **USO** | 3m | 9 | +6.8% | -0.1% | -20.7% | +52.2% | 44% |
| **USO** | 6m | 9 | +7.6% | -0.2% | -27.6% | +45.8% | 44% |
| **GLD** | 1m | 9 | -2.2% | -1.6% | -8.3% | +1.9% | 11% |
| **GLD** | 3m | 9 | -2.1% | -2.8% | -12.0% | +6.4% | 44% |
| **GLD** | 6m | 9 | -1.5% | -4.7% | -17.5% | +25.0% | 33% |
| **TLT** | 1m | 9 | -1.7% | -2.2% | -5.7% | +2.6% | 22% |
| **TLT** | 3m | 9 | -5.6% | -4.9% | -16.9% | +5.4% | 33% |
| **TLT** | 6m | 9 | -8.4% | -6.1% | -21.7% | +3.4% | 22% |

**Episodes (последни 5 от 9):**
- `2023-04-12 → 2023-04-18` (5d)
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-04-09` (27d)
- `2026-04-29 → 2026-05-19` (7d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 16 · **Total matching days:** 275 · **History:** 2021-05-17 → 2026-06-11

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.2% | +2.2% | -4.8% | +9.0% | 75% |
| **SPY** | 3m | 16 | +3.6% | +4.4% | -12.3% | +16.7% | 75% |
| **SPY** | 6m | 16 | +7.3% | +8.3% | -13.5% | +21.9% | 81% |
| **USO** | 1m | 16 | +1.8% | -3.2% | -13.0% | +27.7% | 38% |
| **USO** | 3m | 16 | +2.5% | -1.7% | -14.5% | +29.9% | 38% |
| **USO** | 6m | 16 | +12.2% | +2.3% | -12.4% | +87.1% | 69% |
| **GLD** | 1m | 16 | +2.4% | +1.8% | -6.4% | +9.0% | 75% |
| **GLD** | 3m | 16 | +6.5% | +7.4% | -13.4% | +23.6% | 69% |
| **GLD** | 6m | 16 | +11.1% | +12.1% | -13.4% | +43.8% | 75% |
| **TLT** | 1m | 16 | +0.6% | +0.7% | -6.1% | +8.5% | 56% |
| **TLT** | 3m | 16 | -0.6% | -0.3% | -14.7% | +13.0% | 50% |
| **TLT** | 6m | 16 | -2.7% | -0.7% | -20.6% | +8.6% | 44% |

**Episodes (последни 5 от 16):**
- `2025-03-27 → 2025-05-08` (25d)
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-17 → 2026-04-23` (4d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 19 · **Total matching days:** 292 · **History:** 2021-05-17 → 2026-06-11

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 19 | +0.4% | +0.0% | -8.3% | +7.0% | 53% |
| **SPY** | 3m | 19 | +2.2% | +3.1% | -13.3% | +9.4% | 68% |
| **SPY** | 6m | 19 | +3.6% | +6.7% | -15.7% | +17.6% | 74% |
| **USO** | 1m | 19 | +0.4% | -3.1% | -14.3% | +55.8% | 42% |
| **USO** | 3m | 19 | +3.4% | -1.3% | -12.7% | +64.3% | 42% |
| **USO** | 6m | 19 | +8.4% | -3.1% | -16.0% | +75.1% | 47% |
| **GLD** | 1m | 19 | -0.5% | -0.1% | -12.4% | +7.6% | 47% |
| **GLD** | 3m | 19 | +1.6% | +1.3% | -13.7% | +19.0% | 63% |
| **GLD** | 6m | 19 | +7.5% | +6.0% | -18.4% | +55.5% | 68% |
| **TLT** | 1m | 19 | +0.1% | +0.3% | -5.5% | +5.5% | 58% |
| **TLT** | 3m | 19 | -2.7% | -3.8% | -16.8% | +9.8% | 42% |
| **TLT** | 6m | 19 | -5.0% | -3.3% | -20.5% | +6.7% | 32% |

**Episodes (последни 5 от 19):**
- `2025-05-12 → 2025-05-19` (3d)
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-06-09` (3d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-06-11

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (19 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 9 | 2.47 | 2.59 | 2026-05-15 00:00:00 | 2026-06-08 00:00:00 | ✓ |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 9 | 2.32 | 2.34 | 2026-05-15 00:00:00 | 2026-06-08 00:00:00 | ✓ |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 5 | 2.76 | 2.76 | 2026-06-04 00:00:00 | 2026-06-08 00:00:00 | ✓ |
| **M2** | M2 паричен агрегат | liquidity | money_supply | 5 | 2.76 | 2.76 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **DGORDER** | Нови поръчки за дълготрайни стоки | growth | hard_activity | 5 | 2.57 | 2.90 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **C_AND_I_LOANS** | Търговски и индустриални кредити (C&I) | liquidity | banking_credit | 5 | 2.56 | 2.57 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **UMCSENT** | Michigan Sentiment Index | growth | consumer_sentiment | 5 | 2.47 | 2.57 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CPI_SHELTER** | CPI — жилища (shelter) | inflation | goods_services | 5 | 2.46 | 2.46 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | 5 | 2.40 | 2.40 | 2026-06-04 00:00:00 | 2026-06-08 00:00:00 | - |
| **CPI_SERVICES** | CPI — услуги (всички) | inflation | goods_services | 5 | 2.35 | 2.35 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | 5 | 2.30 | 2.30 | 2026-06-04 00:00:00 | 2026-06-08 00:00:00 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 5 | 2.29 | 2.29 | 2026-06-04 00:00:00 | 2026-06-08 00:00:00 | - |
| **CSUSHPISA** | Case-Shiller US National HPI (SA) | housing | housing_prices | 5 | 2.26 | 2.26 | 2026-06-04 00:00:00 | 2026-06-08 00:00:00 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | 5 | 2.10 | 2.10 | 2026-06-04 00:00:00 | 2026-06-08 00:00:00 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | 5 | 2.02 | 2.02 | 2026-06-04 00:00:00 | 2026-06-08 00:00:00 | ✓ |
| **RSXFS** | Продажби на дребно (без храна) | growth | hard_activity | 4 | 2.33 | 2.33 | 2026-05-15 00:00:00 | 2026-05-30 00:00:00 | ✓ |
| **PPICORE** | PPI Core (Final Demand без храни и енергия) | inflation | core_measures | 4 | 2.32 | 2.32 | 2026-05-15 00:00:00 | 2026-05-30 00:00:00 | ✓ |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 3 | 2.32 | 2.39 | 2026-06-06 00:00:00 | 2026-06-08 00:00:00 | ✓ |
| **USSTHPI** | FHFA House Price Index (Q, NSA) | housing | housing_prices | 1 | 2.70 | 2.70 | 2026-06-04 00:00:00 | 2026-06-04 00:00:00 | ✓ |

### EU (13 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_RETAIL_CONF** | Доверие в търговията на дребно (DG ECFIN) | growth | sentiment | 6 | 2.49 | 2.68 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **EA_COMP_PER_EMPLOYEE** | Компенсация на наетите (D1, EA-20, M€) | labor | wages | 6 | 2.39 | 2.39 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **EA_PPI_INTERMEDIATE** | PPI междинни стоки (MIG ING, индекс 2021=100) | inflation | producer_prices | 6 | 2.04 | 2.16 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | - |
| **EA_RETAIL_VOL** | Търговия на дребно — обем на продажбите (G47, индекс 2021=100) | growth | hard_activity | 6 | 2.02 | 2.06 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | - |
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 4 | 5.37 | 5.37 | 2026-06-05 00:00:00 | 2026-06-08 00:00:00 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation | sentiment | 4 | 2.98 | 2.98 | 2026-06-05 00:00:00 | 2026-06-08 00:00:00 | - |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | 4 | 2.32 | 2.32 | 2026-06-05 00:00:00 | 2026-06-08 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 4 | 2.31 | 2.31 | 2026-06-05 00:00:00 | 2026-06-08 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 4 | 2.23 | 2.23 | 2026-06-05 00:00:00 | 2026-06-08 00:00:00 | ✓ |
| **EA_EMPLOYMENT_EXP** | Очаквания за заетост (3m напред) | labor | labor_sentiment | 3 | 3.14 | 3.14 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **EA_ESI** | Икономически Sentiment Indicator (DG ECFIN ESI) | growth | sentiment | 3 | 2.25 | 2.25 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **EA_CONSUMER_CONF** | Потребителско доверие (DG ECFIN, full history от 1985) | growth | sentiment | 3 | 2.10 | 2.10 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | - |
| **EA_WAGES_SALARIES** | Работни заплати (D11, EA-20, M€) | labor | wages | 2 | 2.38 | 2.38 | 2026-06-03 00:00:00 | 2026-06-04 00:00:00 | ✓ |

### CN (7 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 4 | 2.56 | 2.56 | 2026-06-02 00:00:00 | 2026-06-08 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 4 | 2.24 | 2.24 | 2026-06-02 00:00:00 | 2026-06-08 00:00:00 | - |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 4 | 2.23 | 2.23 | 2026-06-02 00:00:00 | 2026-06-08 00:00:00 | ✓ |
| **CN_POLICY_RATE** | Политическа лихва — PBoC 7-day repo (%) | credit | rates | 2 | 2.39 | 2.39 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CN_FDI_GDP** | ПЧИ — входящи (% от БВП) | property | investment | 2 | 2.11 | 2.11 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CN_BIS_PROPERTY_YOY** | Жилищни имотни цени (YoY %, BIS номинал) | property | housing | 2 | 2.10 | 2.10 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | - |
| **CN_CREDIT_PRIVATE** | Кредит към частния сектор (% от БВП) | credit | credit_depth | 2 | 2.07 | 2.07 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-06-08 00:00:00 · **Generated:** 2026-06-08 21:30:23.857314+00:00

**Режим:** `stagflation_confirmed` (Стагфлация (потвърдена))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 35.6 | contracting | 29.6% | 2 | 2 |
| **growth** | 43.4 | mixed | 40.0% | 2 | 1 |
| **inflation** | 34.0 | contracting | 22.2% | 5 | 1 |
| **liquidity** | 50.9 | mixed | 36.8% | 0 | 0 |

### Top anomalies (10 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | -2.76 | down | 1.71 | 2026-03-01 | ✓ min |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | +2.59 | up | 5.99 | 2026-04-01 | - |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | -2.40 | down | 2.60 | 2026-04-01 | - |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.34 | down | 94.99 | 2026-01-01 | ✓ min |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | +2.30 | up | 5.23 | 2026-04-01 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | +2.29 | up | 4.70 | 2026-04-01 | - |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | +2.28 | up | 55.10 | 2026-05-01 | ✓ max |
| **CSUSHPISA** | Case-Shiller US National HPI (SA) | housing | housing_prices | -2.26 | down | 0.66 | 2026-03-01 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | +2.10 | up | 4.35 | 2026-04-01 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | -2.02 | down | 1.90 | 2026-04-01 | ✓ min |

### Narrative hints от макро лещите
- **HPIPONM226S**: Monthly FHFA версия. Само purchase transactions (без refi appraisals). По-чист от refi-bias.
- **PPIFIS**: Производствени цени → consumer prices с 1-3 месечен lag. Водещ за CPI при трендови промени.
- **PSAVERT**: Hard data компонент. Скочи >30% в COVID — когато survey и hard data разминават, сигналът укрепва.
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **TRIMMED_MEAN_CPI**: Орязва 8% в опашките (топ и долу). По-стабилна от median при многоизмерен shock.
- **MICH_INFL_1Y**: Household очаквания. По-шумни от market-based, но по-ранни. Extreme movements сигнализират de-anchoring risk.
- **US_PMI_MFG**: Markit mfg — comparable cross-country. ISM е US-only.
- **CSUSHPISA**: Главен ценови benchmark. Repeat-sales методология; ~2 месеца lag. National композит на 9 census divisions.
- **CPI_GOODS**: Goods inflation реагира бързо на supply shocks. 2022 peak след доставъчните кризи. Сега често е в deflation/близо до 0.
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
  - `state`: a_up_b_down
  - `interpretation`: Anchored — realized hot, expectations stable. Credibility holds.
  - `slot_a_label`: Realized inflation
  - `slot_b_label`: Inflation expectations
  - `breadth_a`: 1.0
  - `breadth_b`: 0.333
- 🔔 **?**
  - `pair_id`: credit_policy_transmission
  - `name_bg`: Credit spreads × Policy rates
  - `question_bg`: Дали credit следва policy направление — transmission intact?
  - `state`: transition
  - `interpretation`: Mixed transmission.
  - `slot_a_label`: Credit stress
  - `slot_b_label`: Policy tightening
  - `breadth_a`: 0.5
  - `breadth_b`: 0.833
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
  - `state`: a_up_b_down
  - `interpretation`: Модел persistent, пазар разчита на disinflation — contrarian hawkish (моделът обикновено лидера).
  - `slot_a_label`: Модел (sticky inflation)
  - `slot_b_label`: Пазар (breakevens + survey)
  - `breadth_a`: 1.0
  - `breadth_b`: 0.333

### Executive narrative
> Картината показва потвърдена стагфлационна конфигурация — трудовият пазар остава tight, а инфлационният натиск е broad-based. Най-отклонена леща: Монетарна политика и кредит — breadth 76% (разширяване), 0 аномалии, 0 нови екстремума. Обаче inflation expectations остават anchored — Fed narrative-ът за момента държи. За наблюдение следващия релиз: HPIPONM226S, LABOR_SHARE_NBS (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: HPIPONM226S z=-2.76 · NEW-5Y-MIN
- 4 нови екстремуми в top-10 (lookback 5г.)
- Активни двойки: Stagflation test=both_up; Growth × Labor=a_up_b_down; Inflation anchoring=a_up_b_down



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-06-08 00:00:00 · **Generated:** 2026-06-08 17:26:15.402090+00:00

**Режим:** `soft_landing` (Soft landing)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 36.5 | contracting | 42.9% | 1 | 0 |
| **growth** | 44.6 | mixed | 15.4% | 1 | 0 |
| **inflation** | 46.1 | mixed | 71.4% | 1 | 0 |
| **credit** | 42.3 | mixed | 36.8% | 3 | 2 |

### Top anomalies (5 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | +5.37 | up | 2.75 | 2026-05-01 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation, growth | sentiment | +2.98 | up | 27.40 | 2026-05-01 | - |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | -2.32 | down | -1.80 | 2026-05-01 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | +2.31 | up | 3.73 | 2026-04-01 | ✓ max |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | +2.23 | up | 3.00 | 2026-04-01 | ✓ max |

### Narrative hints от макро лещите
- **EA_BUND_2Y**: EA-aggregate 2Y yield. Curve slope (10Y-2Y) проксира policy expectations и recession risk.
- **EA_SELLING_PRICE_EXP**: Forward-looking inflation сигнал от business side — мениджърите казват дали ще вдигат цени. Изпреварва HICP с 3-6 месеца.
- **EA_EMP_EXP_SERVICES**: DG ECFIN survey: forward-looking labor сигнал от услугите (~70% от GDP). Дълга история (от 1996) — за разлика от teibs030 (EA_EMPLOYMENT_EXP, 12m). Същата полярност (higher=better). De-singleton-ва labor_sentiment.
- **FR_10Y**: France sovereign yield — компонент на OAT-Bund spread. Core-but-not-DE EA stress indicator.
- **DE_10Y**: Germany 10Y, Maastricht-criterion measure. Reference за BTP-Bund / OAT-Bund spread изчисления.

### Cross-lens divergences (6 entries)
- 🔔 **?**
  - `pair_id`: stagflation_test
  - `name_bg`: Стагфлационен тест
  - `question_bg`: Заплатите ли движат услугите нагоре?
  - `state`: a_up_b_down
  - `interpretation`: Wage-led моментум без transfer към услугите още. Early warning — гледай дали ще пробие.
  - `slot_a_label`: Натиск от заплати
  - `slot_b_label`: Базова/услуги инфлация
  - `breadth_a`: 1.0
  - `breadth_b`: 0.0
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
- 🔔 **?**
  - `pair_id`: fragmentation_risk
  - `name_bg`: Фрагментационен риск
  - `question_bg`: ЕЦБ hike-овете разширяват ли периферните spreads?
  - `state`: a_up_b_down
  - `interpretation`: Hike-ове + сжимащи се spreads — smooth transmission, credible policy.
  - `slot_a_label`: Политика (реална лихва + баланс)
  - `slot_b_label`: Sovereign spreads (BTP/OAT-Bund)
  - `breadth_a`: 1.0
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
  - `breadth_b`: 0.0
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

### Executive narrative
> Конфигурацията подкрепя soft landing — labor остава tight, но инфлацията се охлажда. Fed credibility за момента издържа. Най-отклонена леща: Инфлация и цени — breadth 17% (свиване), 1 аномалии, 0 нови екстремума. За наблюдение следващия релиз: FR_10Y, DE_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.37
- 2 нови екстремуми в top-5 (lookback 5г.)
- Активни двойки: Stagflation test=a_up_b_down; ecb_transmission=a_up_b_down; fragmentation_risk=a_up_b_down



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-06-08 00:00:00 · **Generated:** 2026-06-08 17:25:35.544258+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 30.6 | contracting | -% | - | - |
| **inflation** | 50.6 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 48.5 | mixed | -% | - | - |
| **property** | 30.5 | contracting | -% | - | - |

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
> Претеглен композитен macro score 36.9/100 → режим „ВЛОШАВАЩ СЕ“. 5 лещи, 3 flagged аномалии (4 застояли изключени), 3 cross-lens двойки.



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
| `date` | 2026-06-01 00:00:00 |
| `week_start` | 2026-06-01 00:00:00 |
| `week_end` | 2026-06-05 00:00:00 |
| `approved` | True |
| `regime` | REFLATION |
| `regime_bg` | РЕФЛАЦИЯ |
| `signal` | ЗАДРЪЖ (REFLATION 100%, 4-та седмица след ре-входа) |
| `alignment` | 6.0 |
| `alignment_max` | 8 |
| `alignment_label` | УМЕРЕН-ЧИСТ |
| `gms_score` | 3.0 |
| `gms_max` | 8 |
| `gms_label` | MEDIUM |
| `ks_active` | False |
| `spy_4w` | +0.04% |
| `qqq_4w` | -0.72% |
| `xle_4w` | +3.86% |
| `gld_4w` | -8.84% |
| `tlt_4w` | -1.13% |
| `tip_4w` | -1.93% |
| `iwm_4w` | -0.76% |



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-06-05 → 2026-06-10)

**stable_winner (1m):** +7 entered, -3 exited
  - **Entered:** AES, BIIB, BK, HWM, MNST, NEM, VLO _(включително 3 за първи път в историята: AES, HWM, VLO)_
  - **Exited:** EL, EXPE, MS

**stable_winner (3m):** +2 entered, -5 exited
  - **Entered:** MNST, SPG _(включително 1 за първи път в историята: MNST)_
  - **Exited:** CFG, HAS, HST, RL, TPR

**quality_dip (1m):** +4 entered, -7 exited
  - **Entered:** EL, EXPE, FCX, MS _(включително 2 за първи път в историята: FCX, MS)_
  - **Exited:** BIIB, BK, HWM, MNST, NEM, ROK, VLO

**quality_dip (3m):** +7 entered, -3 exited
  - **Entered:** AES, CFG, FCX, HAS, HST, RL, TPR _(включително 4 за първи път в историята: AES, CFG, FCX, TPR)_
  - **Exited:** MNST, ROK, SPG

**faded_bounce (1m):** +9 entered, -8 exited
  - **Entered:** AJG, AXON, BBY, CAG, GIS, INVH, KMB, OKE, PCG _(включително 1 за първи път в историята: INVH)_
  - **Exited:** BLDR, DOW, DVA, FIS, KKR, OTIS, STZ, TAP

**faded_bounce (3m):** +6 entered, -9 exited
  - **Entered:** AJG, CMG, INVH, LULU, MRSH, PCG _(включително 1 за първи път в историята: INVH)_
  - **Exited:** BX, DOW, DVA, ERIE, LEN, OXY, POOL, SW, TAP

### EU (period: 2026-06-05 → 2026-06-10)

**stable_winner (1m):** +13 entered, -18 exited
  - **Entered:** AAF.L, ABN.AS, ALLN.SW, ANTO.L, BAMI.MI, BIRG.IR, ISS.CO, MRL.MC, NDA.DE, NDX1.DE, NKT.CO, REP.MC, SPSN.SW _(включително 2 за първи път в историята: ABN.AS, NDA.DE)_
  - **Exited:** ACLN.SW, AIXA.DE, BBVA.MC, BKT.MC, BPE.MI, CCH.L, FTK.DE, GAW.L, GLE.PA, HOT.DE, KER.PA, LPP.WA, PAF.L, SAN.MC, SAND.ST, TSCO.L, WRT1V.HE, ZEG.L

**stable_winner (3m):** +11 entered, -9 exited
  - **Entered:** AAF.L, ALLFG.AS, BBVA.MC, BBY.L, BKT.MC, FR.PA, GL9.IR, HM-B.ST, LTMC.MI, NDA.DE, UNI.MC _(включително 2 за първи път в историята: BKT.MC, NDA.DE)_
  - **Exited:** BPE.MI, BRBY.L, CCH.L, NKT.CO, PAF.L, SAND.ST, SPSN.SW, TSCO.L, WRT1V.HE

**quality_dip (1m):** +18 entered, -13 exited
  - **Entered:** ACLN.SW, AIXA.DE, BBVA.MC, BKT.MC, BPE.MI, CCH.L, FTK.DE, GAW.L, GLE.PA, HOT.DE, KER.PA, LPP.WA, PAF.L, SAN.MC, SAND.ST, TSCO.L, WRT1V.HE, ZEG.L _(включително 2 за първи път в историята: AIXA.DE, LPP.WA)_
  - **Exited:** AAF.L, ABN.AS, ALLN.SW, ANTO.L, BAMI.MI, BIRG.IR, ISS.CO, MRL.MC, NDX1.DE, NKT.CO, REP.MC, SPSN.SW, UNI.MI

**quality_dip (3m):** +9 entered, -11 exited
  - **Entered:** BPE.MI, BRBY.L, CCH.L, NKT.CO, PAF.L, SAND.ST, SPSN.SW, TSCO.L, WRT1V.HE _(включително 3 за първи път в историята: SAND.ST, TSCO.L, WRT1V.HE)_
  - **Exited:** AAF.L, ALLFG.AS, BBVA.MC, BBY.L, BKT.MC, FR.PA, GL9.IR, HM-B.ST, LTMC.MI, UNI.MC, UNI.MI

**faded_bounce (1m):** +12 entered, -12 exited
  - **Entered:** AAK.ST, BALD-B.ST, BME.L, DSFIR.AS, ENX.PA, EVD.DE, EVK.DE, GFC.PA, RED.MC, SW.PA, VPK.AS, WALL-B.ST _(включително 2 за първи път в историята: EVD.DE, VPK.AS)_
  - **Exited:** BAKKA.OL, BC.MI, BEIJ-B.ST, EZJ.L, III.L, INDT.ST, LSEG.L, NEM.DE, SAP.DE, THULE.ST, TOM.OL, WISE.L

**faded_bounce (3m):** +6 entered, -8 exited
  - **Entered:** DLN.L, GFC.PA, PGHN.SW, SIGN.SW, WISE.L, ZAL.DE
  - **Exited:** BOL.PA, LIFCO-B.ST, NEXI.MI, PNDORA.CO, RACE.MI, REY.MI, SGE.L, SREN.SW



---

## 11. COT positioning — текуща картина (cot_monitor + cot_cta)

### COT Monitor (38 markets) (snapshot: 2026-06-02 00:00:00)
| Market | Asset class | Net position | Net % | Percentile 5y | Weekly change |
|---|---|---:|---:|---:|---:|
| **soyoil** | Commodities | 156433 | 99.0 | 99.0 | -12709 |
| **soymeal** | Commodities | 127070 | 96.4 | 96.4 | 16133 |
| **aud** | FX | 58800 | 96.4 | 96.4 | 2200 |
| **copper** | Commodities | 77131 | 89.9 | 89.9 | 13987 |
| **rbob** | Commodities | 67957 | 85.0 | 85.0 | 1528 |
| **cattle** | Commodities | 114964 | 82.7 | 82.7 | -27001 |
| **soybeans** | Commodities | 156050 | 82.1 | 82.1 | -65567 |
| **vix** | Volatility | -33033 | 75.2 | 75.2 | 5770 |
| **eurfx** | FX | 12027 | 75.2 | 75.2 | 181 |
| **us30y** | Rates | -280062 | 74.8 | 74.8 | 5411 |
| **gbpfx** | FX | 27353 | 72.0 | 72.0 | 1304 |
| **corn** | Commodities | 115082 | 66.5 | 66.5 | -228843 |
| **cotton** | Commodities | 52402 | 63.4 | 63.4 | 1218 |
| **brent** | Commodities | 9159 | 63.3 | 63.3 | -11019 |
| **platinum** | Commodities | 11974 | 61.1 | 61.1 | -350 |
| **us5y** | Rates | -2257595 | 49.1 | 49.1 | 193246 |
| **gold** | Commodities | 111341 | 45.5 | 45.5 | 15677 |
| **us2y** | Rates | -1813011 | 45.1 | 45.1 | 221464 |
| **wheat** | Commodities | -57871 | 41.9 | 41.9 | -47968 |
| **coffee** | Commodities | 12195 | 40.6 | 40.6 | -18840 |
| **heatingoil** | Commodities | 12160 | 40.0 | 40.0 | 392 |
| **bitcoin** | Crypto | -6558 | 34.5 | 34.5 | 5180 |
| **usultra10y** | Rates | -285323 | 29.6 | 29.6 | -6442 |
| **wti** | Commodities | -20566 | 27.6 | 27.6 | 5112 |
| **silver** | Commodities | 10433 | 27.2 | 27.2 | -508 |
| **palladium** | Commodities | -3476 | 26.1 | 26.1 | -1566 |
| **natgas** | Commodities | -7128 | 24.6 | 24.6 | 388 |
| **us10y** | Rates | -1963094 | 22.6 | 22.6 | 40754 |
| **chf** | FX | -9949 | 22.1 | 22.1 | -3315 |
| **cad** | FX | -44601 | 20.0 | 20.0 | 3157 |
| **dxy** | FX | -11112 | 19.9 | 19.9 | -5307 |
| **sugar** | Commodities | -122504 | 14.7 | 14.7 | -8358 |
| **cocoa** | Commodities | -21111 | 14.5 | 14.5 | -4275 |
| **russell** | US Equities | -73340 | 13.5 | 13.5 | -17986 |
| **hogs** | Commodities | -6551 | 6.9 | 6.9 | -57633 |
| **jpy** | FX | -88063 | 4.0 | 4.0 | -35166 |
| **sp500** | US Equities | -500732 | 2.9 | 2.9 | -94857 |
| **nasdaq** | US Equities | -74838 | 0.2 | 0.2 | -18499 |

### COT/CTA Positioning (11 markets) (snapshot: 2026-06-02 00:00:00)
| Market | Asset class | Net position | Net % | Percentile 5y | Weekly change |
|---|---|---:|---:|---:|---:|
| **bitcoin** | Crypto | -6558 | 94.2 | 94.2 | 5180 |
| **wti** | Commodities | -20566 | 90.4 | 90.4 | 5112 |
| **corn** | Commodities | 115082 | 82.7 | 82.7 | -228843 |
| **eurfx** | FX | 12027 | 55.8 | 55.8 | 181 |
| **vix** | Volatility | -33033 | 44.2 | 44.2 | 5770 |
| **gold** | Commodities | 111341 | 35.3 | 35.3 | 15677 |
| **us10y** | Rates | -1963094 | 32.7 | 32.7 | 40754 |
| **gbpfx** | FX | 27353 | 29.5 | 29.5 | 1304 |
| **dxy** | FX | -11112 | 23.1 | 23.1 | -5307 |
| **sp500** | US Equities | -500732 | 1.3 | 1.3 | -94857 |
| **nasdaq** | US Equities | -74838 | 0.6 | 0.6 | -18499 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **DELL** | Technology | 95.6 | 49.7% | 151.7% | 165.4% | 228.7% | 1.83 | -32.3% |
| 2 | **HPE** | Technology | 94.9 | 47.4% | 113.6% | 93.0% | 154.7% | 1.85 | -23.7% |
| 3 | **MU** | Technology | 94.3 | 12.1% | 113.1% | 261.5% | 705.8% | 3.00 | -30.3% |
| 4 | **SNDK** | Technology | 93.3 | 6.2% | 150.7% | 628.8% | 3829.3% | 3.74 | -31.3% |
| 5 | **KLAC** | Technology | 92.6 | 15.9% | 46.0% | 74.8% | 159.2% | 1.89 | -22.4% |
| 6 | **AMAT** | Technology | 92.4 | 12.2% | 41.8% | 85.8% | 194.9% | 2.15 | -21.4% |
| 7 | **LRCX** | Technology | 92.4 | 8.7% | 47.0% | 98.0% | 267.1% | 2.44 | -20.0% |
| 8 | **CSCO** | Technology | 91.6 | 20.3% | 52.9% | 52.3% | 84.4% | 1.83 | -13.6% |
| 9 | **STLD** | Basic Materials | 90.9 | 13.7% | 46.1% | 62.5% | 103.5% | 2.01 | -20.3% |
| 10 | **NUE** | Basic Materials | 90.7 | 8.0% | 46.3% | 58.3% | 107.5% | 2.32 | -18.4% |
| 11 | **STX** | Technology | 90.5 | -2.2% | 111.8% | 187.2% | 534.9% | 2.89 | -21.0% |
| 12 | **AMD** | Technology | 90.3 | -1.4% | 120.9% | 104.6% | 271.6% | 1.95 | -27.8% |
| 13 | **WDC** | Technology | 89.9 | -5.0% | 82.4% | 188.9% | 761.8% | 3.28 | -20.6% |
| 14 | **JBHT** | Industrials | 88.7 | 16.6% | 33.7% | 48.4% | 100.1% | 1.77 | -15.9% |
| 15 | **ON** | Technology | 88.7 | 2.7% | 86.0% | 95.4% | 110.3% | 1.29 | -28.1% |
| 16 | **CASY** | Consumer Defensive | 88.3 | 4.4% | 33.8% | 61.9% | 109.2% | 2.20 | -16.1% |
| 17 | **DDOG** | Technology | 87.8 | 12.5% | 78.5% | 47.5% | 87.9% | 0.93 | -48.6% |
| 18 | **INTC** | Technology | 87.6 | -17.3% | 123.1% | 165.6% | 422.7% | 2.24 | -24.2% |
| 19 | **COHR** | Technology | 87.2 | -6.6% | 41.1% | 90.9% | 337.0% | 1.94 | -26.5% |
| 20 | **NTAP** | Technology | 86.6 | 36.5% | 65.5% | 38.1% | 58.9% | 1.07 | -24.8% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **TPRO.MI** | Technology | 94.5 | 57.2% | 89.2% | 123.5% | 300.0% | 2.25 | -27.0% |
| 2 | **STMMI.MI** | Technology | 93.8 | 28.7% | 110.6% | 180.0% | 137.9% | 1.68 | -33.5% |
| 3 | **IFX.DE** | Technology | 93.2 | 29.2% | 81.8% | 107.3% | 107.7% | 1.59 | -21.2% |
| 4 | **AIXA.DE** | Technology | 92.7 | 16.5% | 70.8% | 198.3% | 284.9% | 2.13 | -28.4% |
| 5 | **BESI.AS** | Technology | 91.6 | 15.6% | 66.5% | 97.9% | 130.8% | 1.63 | -20.9% |
| 6 | **IGG.L** | Financial Services | 91.0 | 24.1% | 41.2% | 64.8% | 77.8% | 2.22 | -11.5% |
| 7 | **NOKIA.HE** | Technology | 90.9 | 4.9% | 79.4% | 127.1% | 157.8% | 1.91 | -27.6% |
| 8 | **ASML.AS** | Technology | 90.2 | 19.1% | 25.9% | 57.0% | 128.6% | 1.99 | -15.8% |
| 9 | **SUBC.OL** | Energy | 90.2 | 12.5% | 35.4% | 77.6% | 97.6% | 2.28 | -11.3% |
| 10 | **DHER.DE** | Consumer Cyclical | 88.4 | 52.4% | 100.9% | 98.8% | 59.3% | 0.71 | -48.7% |
| 11 | **GL9.IR** | Consumer Defensive | 88.0 | 14.7% | 32.2% | 51.5% | 81.1% | 2.05 | -8.0% |
| 12 | **SPM.MI** | Energy | 87.6 | 2.9% | 35.5% | 89.3% | 89.9% | 1.97 | -14.7% |
| 13 | **TIT.MI** | Communication Services | 87.4 | 9.4% | 27.0% | 53.8% | 99.5% | 2.25 | -13.0% |
| 14 | **NHY.OL** | Basic Materials | 87.2 | 5.8% | 26.6% | 55.9% | 107.6% | 2.50 | -11.5% |
| 15 | **VAR.OL** | Energy | 87.2 | 12.5% | 30.4% | 61.4% | 82.2% | 1.63 | -17.4% |
| 16 | **HUBN.SW** | Industrials | 87.0 | -7.0% | 44.7% | 70.7% | 208.0% | 2.68 | -14.1% |
| 17 | **BMPS.MI** | Financial Services | 86.2 | 19.5% | 53.0% | 48.1% | 56.7% | 1.22 | -25.5% |
| 18 | **PRY.MI** | Industrials | 85.5 | -8.4% | 34.9% | 62.5% | 135.9% | 2.19 | -13.1% |
| 19 | **ASM.AS** | Technology | 85.4 | 8.6% | 28.4% | 64.6% | 75.2% | 1.25 | -26.2% |
| 20 | **VACN.SW** | Industrials | 85.1 | 2.9% | 25.3% | 74.8% | 98.0% | 1.53 | -25.1% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MO** | Consumer Staples | 0.798 | 0.669 | 0.960 | 0.887 | 0.587 | +27.8% | 14.9 | - |
| 2 | **GL** | Financials | 0.748 | 0.769 | 0.669 | 0.756 | 0.849 | +39.0% | 11.4 | +20.5% |
| 3 | **APA** | Energy | 0.747 | 0.770 | 0.761 | 0.879 | 0.453 | +82.3% | 8.6 | +26.2% |
| 4 | **TROW** | Financials | 0.746 | 0.675 | 0.734 | 0.872 | 0.700 | +24.6% | 11.6 | +18.7% |
| 5 | **MTB** | Financials | 0.736 | 0.704 | 0.671 | 0.840 | 0.755 | +31.8% | 12.8 | +10.3% |
| 6 | **USB** | Financials | 0.727 | 0.678 | 0.701 | 0.863 | 0.646 | +39.7% | 12.1 | +12.3% |
| 7 | **PNC** | Financials | 0.724 | 0.714 | 0.674 | 0.829 | 0.670 | +39.5% | 13.6 | +12.1% |
| 8 | **KEY** | Financials | 0.724 | 0.735 | 0.639 | 0.851 | 0.663 | +48.7% | 13.7 | +10.0% |
| 9 | **CFG** | Financials | 0.716 | 0.799 | 0.598 | 0.806 | 0.639 | +70.2% | 15.8 | +7.7% |
| 10 | **RF** | Financials | 0.715 | 0.672 | 0.680 | 0.875 | 0.606 | +39.7% | 12.0 | +11.9% |
| 11 | **NTRS** | Financials | 0.715 | 0.843 | 0.632 | 0.655 | 0.726 | +62.1% | 17.9 | +14.5% |
| 12 | **ALL** | Financials | 0.714 | 0.529 | 0.695 | 0.877 | 0.850 | +13.2% | 4.9 | +45.2% |
| 13 | **SPG** | Real Estate | 0.708 | 0.777 | 0.890 | 0.528 | 0.505 | +45.3% | 14.9 | +113.6% |
| 14 | **TFC** | Financials | 0.702 | 0.651 | 0.635 | 0.893 | 0.620 | +35.9% | 12.5 | +8.6% |
| 15 | **MAR** | Consumer Discretionary | 0.701 | 0.858 | 0.860 | 0.363 | 0.629 | +57.0% | 41.6 | - |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | 0.122 | 0.109 | 0.131 | 0.059 | 0.235 |
| 502 | **NRG** | Utilities | 0.144 | 0.095 | 0.117 | 0.220 | 0.170 |
| 501 | **CSGP** | Real Estate | 0.149 | 0.017 | 0.106 | 0.184 | 0.444 |
| 500 | **COIN** | Financials | 0.185 | 0.051 | 0.319 | 0.175 | 0.201 |
| 499 | **DASH** | Consumer Discretionary | 0.216 | 0.155 | 0.307 | 0.112 | 0.327 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W24.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W24.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-06-08  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
