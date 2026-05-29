# Сателит — пълен data export за 2026-W22

_Период: 2026-05-25 → 2026-05-31_  
_Генериран: 2026-05-29 09:57 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W22.md` (structured briefing) и `narrative_2026-W22.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**8 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **TIP** | +0.72% | +2.11σ | 110.38 | 111.18 | 2026-05-22 | 2026-05-28 | -0.10% | +0.39% | 6 |
| **DFEN** | +13.75% | +1.60σ | 65.96 | 75.03 | 2026-05-22 | 2026-05-28 | -1.88% | +9.74% | 13 |
| **DBC** | -2.69% | -1.33σ | 30.54 | 29.72 | 2026-05-22 | 2026-05-28 | +1.73% | +3.32% | 13 |
| **XLE** | -4.27% | -1.28σ | 59.49 | 56.95 | 2026-05-22 | 2026-05-28 | +0.75% | +3.91% | 13 |
| **USO** | -7.20% | -1.10σ | 140.92 | 130.78 | 2026-05-22 | 2026-05-28 | +4.92% | +11.02% | 13 |
| **TLT** | +1.25% | +1.10σ | 84.68 | 85.74 | 2026-05-22 | 2026-05-28 | -0.32% | +1.43% | 13 |
| **IEF** | +0.70% | +1.09σ | 93.88 | 94.54 | 2026-05-22 | 2026-05-28 | -0.18% | +0.81% | 13 |
| **LQD** | +0.82% | +1.02σ | 108.37 | 109.26 | 2026-05-22 | 2026-05-28 | -0.13% | +0.93% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_5 канонични patterns от `config/divergence_rules.yaml`, evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-05-31 · **Conditions matched:** 0/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | -7.20% | ❌ | 140.92 | 130.78 | 2026-05-22 | 2026-05-28 |
| DFEN | down ≥ 3.0% | +13.75% | ❌ | 65.96 | 75.03 | 2026-05-22 | 2026-05-28 |
| GLD | down ≥ 1.0% | -0.25% | ❌ | 413.82 | 412.77 | 2026-05-22 | 2026-05-28 |
| URA | down ≥ 3.0% | +3.66% | ❌ | 48.96 | 50.75 | 2026-05-22 | 2026-05-28 |
| UUP | up ≥ 0.5% | -0.25% | ❌ | 27.77 | 27.70 | 2026-05-22 | 2026-05-28 |

### Ликвидна стес (flight to quality) (`liquidity_stress`) — не активен
_Дългосрочни trezuri нагоре, високодоходен кредит надолу, злато нагоре. Класически risk-off._  
**Window:** 7d ending 2026-05-31 · **Conditions matched:** 1/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| TLT | up ≥ 1.0% | +1.25% | ✅ | 84.68 | 85.74 | 2026-05-22 | 2026-05-28 |
| HYG | down ≥ 0.5% | +0.40% | ❌ | 79.91 | 80.23 | 2026-05-22 | 2026-05-28 |
| GLD | up ≥ 1.0% | -0.25% | ❌ | 413.82 | 412.77 | 2026-05-22 | 2026-05-28 |
| UUP | up ≥ 0.3% | -0.25% | ❌ | 27.77 | 27.70 | 2026-05-22 | 2026-05-28 |

### Възстановяване на инфлационни очаквания (`inflation_pickup`) — не активен
_Inflation-protected треzuri нагоре, commodities нагоре, dollar надолу. Repricing на real rates._  
**Window:** 7d ending 2026-05-31 · **Conditions matched:** 0/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| DBC | up ≥ 1.5% | -2.69% | ❌ | 30.54 | 29.72 | 2026-05-22 | 2026-05-28 |
| GLD | up ≥ 1.0% | -0.25% | ❌ | 413.82 | 412.77 | 2026-05-22 | 2026-05-28 |
| UUP | down ≥ 0.5% | -0.25% | ❌ | 27.77 | 27.70 | 2026-05-22 | 2026-05-28 |
| TLT | down ≥ 1.0% | +1.25% | ❌ | 84.68 | 85.74 | 2026-05-22 | 2026-05-28 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-05-31 · **Conditions matched:** 2/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | +2.42% | ✅ | 285.12 | 292.03 | 2026-05-22 | 2026-05-28 |
| XLF | up ≥ 1.0% | -1.29% | ❌ | 51.94 | 51.27 | 2026-05-22 | 2026-05-28 |
| XLY | up ≥ 1.0% | +2.42% | ✅ | 119.18 | 122.06 | 2026-05-22 | 2026-05-28 |
| GLD | down ≥ 0.5% | -0.25% | ❌ | 413.82 | 412.77 | 2026-05-22 | 2026-05-28 |

### Защитен pivot (staples + utilities + gold) (`defensive_pivot`) — не активен
_XLP + XLU + GLD едновременно нагоре. Smart money flight to defensives без credit panic._  
**Window:** 7d ending 2026-05-31 · **Conditions matched:** 0/3

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| XLP | up ≥ 1.0% | -0.44% | ❌ | 84.80 | 84.43 | 2026-05-22 | 2026-05-28 |
| XLU | up ≥ 1.0% | -1.59% | ❌ | 45.35 | 44.63 | 2026-05-22 | 2026-05-28 |
| GLD | up ≥ 1.0% | -0.25% | ❌ | 413.82 | 412.77 | 2026-05-22 | 2026-05-28 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2024-W18 (week ending 2024-05-05)
**Cosine similarity:** 0.9419 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.34% | +4.56% | +12.39% |
| **USO** | -5.38% | -2.32% | -4.14% |
| **GLD** | +1.08% | +5.81% | +18.55% |
| **TLT** | +3.50% | +10.48% | +3.13% |
| **XLE** | -2.90% | -3.74% | -3.35% |
| **IWM** | +0.03% | +3.77% | +9.13% |

### Паралел #2: 2022-W31 (week ending 2022-08-07)
**Cosine similarity:** 0.9249 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -5.49% | -8.60% | +0.60% |
| **USO** | -0.17% | +7.38% | -9.98% |
| **GLD** | -4.21% | -5.34% | +4.94% |
| **TLT** | -7.52% | -18.54% | -7.07% |
| **XLE** | +8.40% | +26.46% | +20.13% |
| **IWM** | -6.55% | -5.87% | +4.26% |

### Паралел #3: 2023-W05 (week ending 2023-02-05)
**Cosine similarity:** 0.9178 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -3.41% | +0.45% | +9.17% |
| **USO** | +5.36% | -2.13% | +14.58% |
| **GLD** | -2.79% | +8.07% | +3.88% |
| **TLT** | -4.43% | -0.95% | -8.11% |
| **XLE** | -0.21% | -5.69% | +3.07% |
| **IWM** | -5.32% | -11.12% | -0.79% |

### Паралел #4: 2025-W40 (week ending 2025-10-05)
**Cosine similarity:** 0.9092 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.90% | +2.39% | -1.44% |
| **USO** | +0.31% | -3.83% | +92.33% |
| **GLD** | +1.31% | +11.36% | +20.07% |
| **TLT** | +0.99% | -1.55% | -0.72% |
| **XLE** | -1.93% | +3.56% | +35.30% |
| **IWM** | -1.88% | +1.54% | +2.75% |

### Паралел #5: 2025-W26 (week ending 2025-06-29)
**Cosine similarity:** 0.8785 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.31% | +7.93% | +12.91% |
| **USO** | +8.90% | +5.10% | -6.55% |
| **GLD** | +1.67% | +15.11% | +38.35% |
| **TLT** | +0.29% | +2.89% | +3.03% |
| **XLE** | +4.28% | +8.76% | +5.41% |
| **IWM** | +3.35% | +12.32% | +17.40% |

### Паралел #6: 2024-W39 (week ending 2024-09-29)
**Cosine similarity:** 0.8575 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.80% | +4.47% | -2.15% |
| **USO** | -0.87% | +5.09% | +6.40% |
| **GLD** | +4.52% | -1.48% | +15.93% |
| **TLT** | -6.33% | -10.40% | -6.64% |
| **XLE** | +0.75% | -2.20% | +7.73% |
| **IWM** | +0.64% | +1.23% | -8.55% |

### Паралел #7: 2025-W32 (week ending 2025-08-10)
**Cosine similarity:** 0.8409 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.06% | +5.59% | +9.01% |
| **USO** | +0.12% | -2.78% | +5.03% |
| **GLD** | +6.71% | +17.65% | +45.49% |
| **TLT** | +2.61% | +3.73% | +2.53% |
| **XLE** | +3.12% | +6.33% | +27.55% |
| **IWM** | +7.50% | +9.97% | +21.03% |

### Паралел #8: 2022-W13 (week ending 2022-04-03)
**Cosine similarity:** 0.8359 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -8.07% | -15.46% | -20.47% |
| **USO** | +3.40% | +10.11% | -11.99% |
| **GLD** | -3.01% | -6.23% | -13.83% |
| **TLT** | -10.73% | -12.03% | -21.88% |
| **XLE** | +1.86% | -4.76% | -4.46% |
| **IWM** | -9.19% | -17.20% | -19.93% |

### Паралел #9: 2023-W11 (week ending 2023-03-19)
**Cosine similarity:** 0.8297 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +6.21% | +13.10% | +14.51% |
| **USO** | +20.58% | +9.70% | +38.58% |
| **GLD** | +1.35% | -1.16% | -2.95% |
| **TLT** | -2.23% | -3.23% | -11.58% |
| **XLE** | +13.61% | +6.15% | +21.85% |
| **IWM** | +4.35% | +9.29% | +7.92% |

### Паралел #10: 2023-W52 (week ending 2023-12-31)
**Cosine similarity:** 0.8066 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.28% | +10.39% | +15.22% |
| **USO** | +9.24% | +18.12% | +19.41% |
| **GLD** | -1.35% | +7.61% | +12.47% |
| **TLT** | -3.20% | -3.70% | -5.63% |
| **XLE** | +1.38% | +13.52% | +10.48% |
| **IWM** | -1.49% | +5.04% | +1.63% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 13 · **Total matching days:** 72 · **History:** 2021-05-17 → 2026-05-28

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 13 | +2.0% | +1.7% | -3.1% | +7.7% | 77% |
| **SPY** | 3m | 13 | +3.5% | +4.6% | -7.0% | +14.4% | 77% |
| **SPY** | 6m | 13 | +8.5% | +11.6% | -6.1% | +22.7% | 77% |
| **USO** | 1m | 13 | +1.0% | -0.8% | -7.2% | +12.7% | 46% |
| **USO** | 3m | 13 | -0.6% | +0.1% | -18.9% | +24.5% | 54% |
| **USO** | 6m | 13 | +12.4% | +0.0% | -8.7% | +109.4% | 54% |
| **GLD** | 1m | 13 | +2.5% | +0.9% | -2.2% | +8.9% | 77% |
| **GLD** | 3m | 13 | +6.8% | +5.9% | -7.2% | +24.5% | 69% |
| **GLD** | 6m | 13 | +7.3% | +10.3% | -12.5% | +25.3% | 69% |
| **TLT** | 1m | 13 | -1.1% | -0.8% | -6.5% | +3.7% | 31% |
| **TLT** | 3m | 13 | +0.5% | +0.6% | -16.2% | +12.6% | 54% |
| **TLT** | 6m | 13 | -2.4% | -0.6% | -17.2% | +9.1% | 38% |

**Episodes (последни 5 от 13):**
- `2024-06-21 → 2024-06-21` (1d)
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-28 → 2026-05-19` (13d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 1 · **Total matching days:** 38 · **History:** 2021-05-17 → 2026-05-28

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | +9.1% | +9.1% | +9.1% | +9.1% | 100% |
| **SPY** | 3m | 1 | +11.6% | +11.6% | +11.6% | +11.6% | 100% |
| **SPY** | 6m | 1 | +11.6% | +11.6% | +11.6% | +11.6% | 100% |
| **USO** | 1m | 1 | +7.2% | +7.2% | +7.2% | +7.2% | 100% |
| **USO** | 3m | 1 | +5.0% | +5.0% | +5.0% | +5.0% | 100% |
| **USO** | 6m | 1 | +5.0% | +5.0% | +5.0% | +5.0% | 100% |
| **GLD** | 1m | 1 | -0.2% | -0.2% | -0.2% | -0.2% | 0% |
| **GLD** | 3m | 1 | -5.0% | -5.0% | -5.0% | -5.0% | 0% |
| **GLD** | 6m | 1 | -5.0% | -5.0% | -5.0% | -5.0% | 0% |
| **TLT** | 1m | 1 | -0.6% | -0.6% | -0.6% | -0.6% | 0% |
| **TLT** | 3m | 1 | -1.0% | -1.0% | -1.0% | -1.0% | 0% |
| **TLT** | 6m | 1 | -1.0% | -1.0% | -1.0% | -1.0% | 0% |

**Episodes (последни 5 от 1):**
- `2026-04-08 → 2026-05-28` (38d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 7 · **Total matching days:** 752 · **History:** 2021-05-17 → 2026-05-28

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
- `2024-10-04 → 2026-05-28` (414d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-05-28

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 9 · **Total matching days:** 76 · **History:** 2021-05-17 → 2026-05-28

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 9 | +0.4% | +0.9% | -7.2% | +7.8% | 56% |
| **SPY** | 3m | 9 | +2.6% | +6.0% | -8.0% | +11.2% | 56% |
| **SPY** | 6m | 9 | +2.0% | +6.0% | -20.2% | +14.9% | 67% |
| **USO** | 1m | 9 | +2.1% | -1.7% | -15.0% | +52.9% | 33% |
| **USO** | 3m | 9 | +6.1% | -0.1% | -20.7% | +45.0% | 44% |
| **USO** | 6m | 9 | +8.0% | -0.2% | -27.6% | +45.8% | 44% |
| **GLD** | 1m | 9 | -2.3% | -1.6% | -8.3% | +1.9% | 11% |
| **GLD** | 3m | 9 | -1.4% | -1.1% | -11.8% | +6.4% | 44% |
| **GLD** | 6m | 9 | -0.1% | -1.1% | -11.8% | +25.0% | 33% |
| **TLT** | 1m | 9 | -1.7% | -2.2% | -5.7% | +2.6% | 22% |
| **TLT** | 3m | 9 | -5.6% | -4.9% | -16.9% | +5.4% | 33% |
| **TLT** | 6m | 9 | -8.5% | -6.1% | -21.7% | +3.4% | 22% |

**Episodes (последни 5 от 9):**
- `2023-04-12 → 2023-04-18` (5d)
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-04-09` (27d)
- `2026-04-29 → 2026-05-19` (7d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 16 · **Total matching days:** 275 · **History:** 2021-05-17 → 2026-05-28

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.2% | +2.2% | -4.8% | +9.0% | 75% |
| **SPY** | 3m | 16 | +3.7% | +5.4% | -12.3% | +16.7% | 75% |
| **SPY** | 6m | 16 | +7.5% | +8.3% | -13.5% | +21.9% | 81% |
| **USO** | 1m | 16 | +1.8% | -3.2% | -13.0% | +27.7% | 38% |
| **USO** | 3m | 16 | +2.6% | -1.7% | -14.5% | +29.9% | 38% |
| **USO** | 6m | 16 | +12.3% | +2.3% | -12.4% | +87.1% | 69% |
| **GLD** | 1m | 16 | +2.4% | +1.8% | -6.4% | +9.0% | 75% |
| **GLD** | 3m | 16 | +6.9% | +7.4% | -7.4% | +23.6% | 69% |
| **GLD** | 6m | 16 | +11.5% | +12.1% | -8.4% | +43.8% | 75% |
| **TLT** | 1m | 16 | +0.6% | +0.7% | -6.1% | +8.5% | 56% |
| **TLT** | 3m | 16 | -0.6% | -0.3% | -14.7% | +13.0% | 50% |
| **TLT** | 6m | 16 | -2.8% | -0.8% | -20.6% | +8.6% | 44% |

**Episodes (последни 5 от 16):**
- `2025-03-27 → 2025-05-08` (25d)
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-17 → 2026-04-23` (4d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 18 · **Total matching days:** 289 · **History:** 2021-05-17 → 2026-05-28

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 18 | +0.4% | +1.1% | -8.3% | +7.0% | 50% |
| **SPY** | 3m | 18 | +2.3% | +3.5% | -13.3% | +9.4% | 67% |
| **SPY** | 6m | 18 | +3.9% | +7.6% | -15.7% | +17.6% | 72% |
| **USO** | 1m | 18 | +0.6% | -3.7% | -14.3% | +55.8% | 44% |
| **USO** | 3m | 18 | +3.7% | -1.0% | -12.7% | +64.3% | 44% |
| **USO** | 6m | 18 | +9.2% | -0.1% | -16.0% | +75.1% | 50% |
| **GLD** | 1m | 18 | -0.3% | +0.0% | -12.4% | +7.6% | 50% |
| **GLD** | 3m | 18 | +1.8% | +1.5% | -13.7% | +19.0% | 67% |
| **GLD** | 6m | 18 | +8.3% | +6.0% | -15.8% | +55.5% | 72% |
| **TLT** | 1m | 18 | +0.1% | +0.3% | -5.5% | +5.5% | 56% |
| **TLT** | 3m | 18 | -2.9% | -4.0% | -16.8% | +9.8% | 39% |
| **TLT** | 6m | 18 | -5.4% | -4.9% | -20.5% | +6.7% | 28% |

**Episodes (последни 5 от 18):**
- `2024-10-10 → 2025-01-17` (52d)
- `2025-05-12 → 2025-05-19` (3d)
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-05-28

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (10 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **M2** | M2 паричен агрегат | liquidity | money_supply | 3 | 2.76 | 2.76 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **C_AND_I_LOANS** | Търговски и индустриални кредити (C&I) | liquidity | banking_credit | 3 | 2.56 | 2.57 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **CPI_SHELTER** | CPI — жилища (shelter) | inflation | goods_services | 3 | 2.46 | 2.46 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **UMCSENT** | Michigan Sentiment Index | growth | consumer_sentiment | 3 | 2.41 | 2.57 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **DGORDER** | Нови поръчки за дълготрайни стоки | growth | hard_activity | 3 | 2.36 | 2.36 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | - |
| **CPI_SERVICES** | CPI — услуги (всички) | inflation | goods_services | 3 | 2.35 | 2.35 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **RSXFS** | Продажби на дребно (без храна) | growth | hard_activity | 3 | 2.33 | 2.33 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **PPICORE** | PPI Core (Final Demand без храни и енергия) | inflation | core_measures | 3 | 2.32 | 2.32 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 3 | 2.31 | 2.31 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 3 | 2.31 | 2.31 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |

### EU (7 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_EMPLOYMENT_EXP** | Очаквания за заетост (3m напред) | labor | labor_sentiment | 3 | 3.14 | 3.14 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **EA_RETAIL_CONF** | Доверие в търговията на дребно (DG ECFIN) | growth | sentiment | 3 | 2.68 | 2.68 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **EA_COMP_PER_EMPLOYEE** | Компенсация на наетите (D1, EA-20, M€) | labor | wages | 3 | 2.39 | 2.39 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **EA_ESI** | Икономически Sentiment Indicator (DG ECFIN ESI) | growth | sentiment | 3 | 2.25 | 2.25 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **EA_CONSUMER_CONF** | Потребителско доверие (DG ECFIN, full history от 1985) | growth | sentiment | 3 | 2.10 | 2.10 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | - |
| **EA_RETAIL_VOL** | Търговия на дребно — обем на продажбите (G47, индекс 2021=100) | growth | hard_activity | 3 | 2.02 | 2.02 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | - |
| **EA_PPI_INTERMEDIATE** | PPI междинни стоки (MIG ING, индекс 2021=100) | inflation | producer_prices | 3 | 2.01 | 2.01 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-05-23 00:00:00 · **Generated:** 2026-05-23 09:04:28.014712+00:00

**Режим:** `stagflation_confirmed` (Стагфлация (потвърдена))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 57.3 | expanding | 57.3% | 4 | 3 |
| **growth** | 43.3 | mixed | 43.3% | 6 | 5 |
| **inflation** | 85.7 | expanding | 85.7% | 12 | 11 |
| **liquidity** | 40.3 | mixed | 40.3% | 3 | 2 |

### Top anomalies (10 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **M2** | M2 паричен агрегат | liquidity | money_supply | +2.76 | up | 22686.00 | 2026-03-01 | ✓ max |
| **C_AND_I_LOANS** | Търговски и индустриални кредити (C&I) | liquidity, growth | banking_credit | +2.57 | up | 2873.58 | 2026-04-01 | ✓ max |
| **UMCSENT** | Michigan Sentiment Index | growth | consumer_sentiment | -2.57 | down | 49.80 | 2026-04-01 | ✓ min |
| **CPI_SHELTER** | CPI — жилища (shelter) | inflation | goods_services | +2.46 | up | 426.64 | 2026-04-01 | ✓ max |
| **DGORDER** | Нови поръчки за дълготрайни стоки | growth | hard_activity | +2.36 | up | 318909.00 | 2026-03-01 | - |
| **CPI_SERVICES** | CPI — услуги (всички) | inflation | goods_services | +2.35 | up | 429.66 | 2026-04-01 | ✓ max |
| **RSXFS** | Продажби на дребно (без храна) | growth | hard_activity | +2.33 | up | 656115.00 | 2026-04-01 | ✓ max |
| **PPICORE** | PPI Core (Final Demand без храни и енергия) | inflation | core_measures | +2.32 | up | 267.86 | 2026-04-01 | ✓ max |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | +2.31 | up | 156.50 | 2026-04-01 | ✓ max |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.31 | down | 95.71 | 2026-01-01 | ✓ min |

### Narrative hints от макро лещите
- **M2**: M2 YoY → исторически корелира със inflation с 12-24 месечен lag. Но velocity-то варира; не е automatic signal.
- **C_AND_I_LOANS**: Бизнес заемане от банки. Water сигнал за capex intentions + credit supply. YoY crash често предхожда рецесия.
- **UMCSENT**: Known за dramatic bottoms. Силно корелира с election cycles, gas prices и post-2024 показва политически bias (D vs R) — гледай breadth с Conference Board/OECD proxy, не individual прочит.
- **CPI_SHELTER**: Shelter е ~1/3 от CPI. OER методология lag-ва market rents с 12-18 месеца. При сривове на пазарни ренти shelter CPI упорито остава висок — дебатен signal.
- **DGORDER**: Aircraft orders са шумни (Boeing cycles). Preferred view: ex-transportation.
- **CPI_SERVICES**: Услугите са 60%+ от CPI. По-инертни от goods. Post-COVID инфлацията мигрира от стоки към услуги.
- **RSXFS**: Не е inflation-adjusted — внимавай при висока inflation (номинален ръст подвеждащ).
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
  - `state`: both_up
  - `interpretation`: Aligned expansion — activity растяща, claims низки. Healthy.
  - `slot_a_label`: Hard activity
  - `slot_b_label`: Labor market (claims inverted)
  - `breadth_a`: 1.0
  - `breadth_b`: 0.667
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
  - `state`: transition
  - `interpretation`: Mixed transmission.
  - `slot_a_label`: Credit stress
  - `slot_b_label`: Policy tightening
  - `breadth_a`: 0.0
  - `breadth_b`: 0.5
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
> Картината показва потвърдена стагфлационна конфигурация — трудовият пазар остава tight, а инфлационният натиск е broad-based. Най-отклонена леща: Inflation — breadth 86% (разширяване), 12 аномалии, 11 нови екстремума. Expectations също нагоре — de-anchoring в ход, рискът ескалира. За наблюдение следващия релиз: M2, C_AND_I_LOANS, UMCSENT (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: M2 z=+2.76 · NEW-5Y-MAX
- 14 нови екстремуми в top-15 (lookback 5г.)
- Активни двойки: Stagflation test=both_up; Growth × Labor=both_up; Inflation anchoring=both_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-05-23 00:00:00 · **Generated:** 2026-05-23 09:20:33.277050+00:00

**Режим:** `transition` (Преходно / смесено)  
**Primary driver:** `none`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 48.6 | mixed | 48.6% | 4 | 2 |
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
  - `state`: a_down_b_up
  - `interpretation`: Narrative pessimism, но fundamentals OK. Sentiment trailing real activity — temporary.
  - `slot_a_label`: Sentiment (ESI, confidence)
  - `slot_b_label`: Hard activity (IP, retail, GDP)
  - `breadth_a`: 0.222
  - `breadth_b`: 0.75

### Executive narrative
> Сигналите са в преход — няма доминираща конфигурация. Следващите 2-3 релиза ще ориентират посоката. Най-отклонена леща: Inflation — breadth 17% (свиване), 1 аномалии, 0 нови екстремума. За наблюдение следващия релиз: EA_EMPLOYMENT_EXP, EA_RETAIL_CONF, EA_COMP_PER_EMPLOYEE (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_EMPLOYMENT_EXP z=-3.14 · NEW-5Y-MIN
- 4 нови екстремуми в top-7 (lookback 5г.)
- Активни двойки: Sentiment × Hard=a_down_b_up



---

## 8. VRM — пълен текущ snapshot

### VRM_STATE (current)
| Field | Value |
|---|---|
| `date` | 2026-05-26 00:00:00 |
| `regime` | REFLATION |
| `ks_status` | inactive |
| `alignment_score` | 7.0 |
| `alignment_total` | 8 |
| `gms_value` | 0.0 |
| `last_updated_md` | 2026-05-26 00:00:00 |
| `is_change_day` | True |

### VRM_WEEK (current)
| Field | Value |
|---|---|
| `date` | 2026-05-18 00:00:00 |
| `week_start` | 2026-05-18 00:00:00 |
| `week_end` | 2026-05-22 00:00:00 |
| `approved` | True |
| `regime` | REFLATION |
| `regime_bg` | РЕФЛАЦИЯ |
| `signal` | ЗАДРЪЖ (REFLATION 100%, KS деактивиран) |
| `alignment` | 7.0 |
| `alignment_max` | 8 |
| `alignment_label` | УМЕРЕН-ЧИСТ (формално) / ОСПОРВАН ПО СЪЩЕСТВО |
| `gms_score` | 0.0 |
| `gms_max` | 8 |
| `gms_label` | LOW |
| `ks_active` | False |
| `spy_4w` | +4.38% |
| `qqq_4w` | +7.94% |
| `xle_4w` | +4.92% |
| `gld_4w` | -4.45% |
| `tlt_4w` | -2.31% |
| `tip_4w` | -1.28% |
| `iwm_4w` | +3.10% |



---

## 9. Rotation events — US + EU, пълни списъци

### US (period: 2026-05-22 → 2026-05-27)

**stable_winner (1m):** +5 entered, -5 exited
  - **Entered:** C, MU, PLD, VRT, WELL _(включително 1 за първи път в историята: MU)_
  - **Exited:** ALB, APA, CBOE, STX, WDC

**stable_winner (3m):** +4 entered, -3 exited
  - **Entered:** CVS, EME, INCY, LLY _(включително 1 за първи път в историята: CVS)_
  - **Exited:** IBKR, JCI, LITE

**quality_dip (1m):** +5 entered, -5 exited
  - **Entered:** ALB, APA, CBOE, STX, WDC _(включително 1 за първи път в историята: CBOE)_
  - **Exited:** C, MU, PLD, VRT, WELL

**quality_dip (3m):** +3 entered, -4 exited
  - **Entered:** IBKR, JCI, LITE _(включително 1 за първи път в историята: IBKR)_
  - **Exited:** CVS, EME, INCY, LLY

**faded_bounce (1m):** +10 entered, -7 exited
  - **Entered:** ADBE, BR, CAG, CMG, DECK, FISV, IT, KKR, PYPL, TTD _(включително 1 за първи път в историята: BR)_
  - **Exited:** AWK, BAX, BX, CHTR, DOW, LII, PAYX

**faded_bounce (3m):** +7 entered, -3 exited
  - **Entered:** BF-B, CNC, ELV, FISV, KKR, NKE, TAP _(включително 3 за първи път в историята: CNC, ELV, TAP)_
  - **Exited:** ACN, DXCM, VRSK

### EU (period: 2026-05-22 → 2026-05-27)

**stable_winner (1m):** +12 entered, -13 exited
  - **Entered:** ANTO.L, BAMI.MI, BMED.MI, DBK.DE, GLE.PA, HM-B.ST, IG.MI, KGF.L, LLOY.L, PRX.AS, TIT.MI, WRT1V.HE _(включително 2 за първи път в историята: DBK.DE, KGF.L)_
  - **Exited:** AXFO.ST, BARC.L, BKT.MC, BMW.DE, ENGI.PA, ENR.DE, FR.PA, FTK.DE, ISS.CO, MAP.MC, MRL.MC, SAN.MC, VWS.CO

**stable_winner (3m):** +6 entered, -9 exited
  - **Entered:** BAMI.MI, BPE.MI, IG.MI, ISS.CO, MOBN.SW, UNI.MI _(включително 3 за първи път в историята: IG.MI, ISS.CO, UNI.MI)_
  - **Exited:** AVOL.SW, BIRG.IR, BMW.DE, EBS.VI, ENGI.PA, FR.PA, JYSK.CO, METSO.HE, SBRY.L

**quality_dip (1m):** +14 entered, -13 exited
  - **Entered:** AXFO.ST, BARC.L, BKT.MC, BMW.DE, CCL.L, ENGI.PA, ENR.DE, FR.PA, FTK.DE, ISS.CO, MAP.MC, MRL.MC, SAN.MC, VWS.CO _(включително 4 за първи път в историята: CCL.L, ENGI.PA, ISS.CO, MRL.MC)_
  - **Exited:** ANTO.L, BAMI.MI, BMED.MI, DBK.DE, GLE.PA, HM-B.ST, IG.MI, KGF.L, LLOY.L, PRX.AS, RHM.DE, TIT.MI, WRT1V.HE

**quality_dip (3m):** +10 entered, -7 exited
  - **Entered:** AVOL.SW, BIRG.IR, BMW.DE, CCL.L, EBS.VI, ENGI.PA, FR.PA, JYSK.CO, METSO.HE, SBRY.L _(включително 4 за първи път в историята: AVOL.SW, CCL.L, FR.PA, METSO.HE)_
  - **Exited:** BAMI.MI, BPE.MI, IG.MI, ISS.CO, MOBN.SW, RHM.DE, UNI.MI

**faded_bounce (1m):** +10 entered, -11 exited
  - **Entered:** ADM.L, BOL.PA, DB1.DE, EDEN.PA, EQT.ST, GF.SW, III.L, RMV.L, RNO.PA, SREN.SW _(включително 3 за първи път в историята: ADM.L, BOL.PA, III.L)_
  - **Exited:** ADS.DE, BALD-B.ST, CAST.ST, CVC.AS, DKSH.SW, HNR1.DE, LEG.DE, MUV2.DE, RED.MC, VNA.DE, ZURN.SW

**faded_bounce (3m):** +8 entered, -3 exited
  - **Entered:** ADM.L, DB1.DE, DCC.L, HNR1.DE, RAND.AS, REL.L, RNO.PA, WALL-B.ST _(включително 3 за първи път в историята: ADM.L, RAND.AS, REL.L)_
  - **Exited:** CAST.ST, PGHN.SW, SREN.SW



---

## 10. COT positioning — текуща картина (cot_monitor + cot_cta)

### COT Monitor (38 markets) (snapshot: 2026-05-19 00:00:00)
| Market | Asset class | Net position | Net % | Percentile 5y | Weekly change |
|---|---|---:|---:|---:|---:|
| **soyoil** | Commodities | 156434 | 99.2 | 99.2 | -9010 |
| **soymeal** | Commodities | 130554 | 96.9 | 96.9 | 9698 |
| **aud** | FX | 61178 | 96.9 | 96.9 | 12853 |
| **soybeans** | Commodities | 207804 | 96.4 | 96.4 | 14920 |
| **cattle** | Commodities | 130113 | 92.0 | 92.0 | -4682 |
| **corn** | Commodities | 293354 | 89.1 | 89.1 | 108948 |
| **copper** | Commodities | 74999 | 88.3 | 88.3 | 15867 |
| **brent** | Commodities | 16256 | 85.7 | 85.7 | 184 |
| **eurfx** | FX | 16317 | 80.5 | 80.5 | -4000 |
| **gbpfx** | FX | 31369 | 78.4 | 78.4 | 2232 |
| **rbob** | Commodities | 62629 | 73.7 | 73.7 | 3581 |
| **wheat** | Commodities | -4799 | 72.5 | 72.5 | 5918 |
| **cotton** | Commodities | 62045 | 70.5 | 70.5 | 27581 |
| **platinum** | Commodities | 13618 | 66.3 | 66.3 | -2270 |
| **us30y** | Rates | -326383 | 64.3 | 64.3 | -110223 |
| **vix** | Volatility | -51904 | 56.0 | 56.0 | -9521 |
| **us5y** | Rates | -2306447 | 48.7 | 48.7 | 102139 |
| **coffee** | Commodities | 17908 | 45.5 | 45.5 | -5925 |
| **hogs** | Commodities | 33713 | 41.3 | 41.3 | -31878 |
| **us2y** | Rates | -1878632 | 41.1 | 41.1 | 227341 |
| **chf** | FX | -4845 | 36.9 | 36.9 | -1079 |
| **gold** | Commodities | 94388 | 34.8 | 34.8 | -1110 |
| **heatingoil** | Commodities | 10793 | 34.1 | 34.1 | -3221 |
| **usultra10y** | Rates | -276150 | 31.7 | 31.7 | -53610 |
| **silver** | Commodities | 11761 | 29.6 | 29.6 | 2898 |
| **bitcoin** | Crypto | -8961 | 28.5 | 28.5 | 1761 |
| **palladium** | Commodities | -2773 | 26.8 | 26.8 | -1039 |
| **cad** | FX | -38654 | 25.1 | 25.1 | 25561 |
| **natgas** | Commodities | -7516 | 24.3 | 24.3 | 388 |
| **us10y** | Rates | -1952737 | 23.2 | 23.2 | 87538 |
| **sugar** | Commodities | -84037 | 22.6 | 22.6 | 105523 |
| **wti** | Commodities | -28426 | 19.3 | 19.3 | 3060 |
| **russell** | US Equities | -67429 | 18.3 | 18.3 | -11611 |
| **cocoa** | Commodities | -16166 | 17.8 | 17.8 | 220 |
| **dxy** | FX | -11716 | 16.1 | 16.1 | -9307 |
| **sp500** | US Equities | -401554 | 14.5 | 14.5 | 10767 |
| **jpy** | FX | -64945 | 14.2 | 14.2 | 3552 |
| **nasdaq** | US Equities | -65822 | 1.1 | 1.1 | -11584 |

### COT/CTA Positioning (11 markets) (snapshot: 2026-05-19 00:00:00)
| Market | Asset class | Net position | Net % | Percentile 5y | Weekly change |
|---|---|---:|---:|---:|---:|
| **corn** | Commodities | 293354 | 94.9 | 94.9 | 108948 |
| **bitcoin** | Crypto | -8961 | 77.6 | 77.6 | 1761 |
| **eurfx** | FX | 16317 | 64.7 | 64.7 | -4000 |
| **wti** | Commodities | -28426 | 64.7 | 64.7 | 3060 |
| **gbpfx** | FX | 31369 | 42.3 | 42.3 | 2232 |
| **us10y** | Rates | -1952737 | 33.3 | 33.3 | 87538 |
| **sp500** | US Equities | -401554 | 25.6 | 25.6 | 10767 |
| **dxy** | FX | -11716 | 19.2 | 19.2 | -9307 |
| **gold** | Commodities | 94388 | 18.6 | 18.6 | -1110 |
| **vix** | Volatility | -51904 | 17.3 | 17.3 | -9521 |
| **nasdaq** | US Equities | -65822 | 3.2 | 3.2 | -11584 |



---

## 11. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MU** | Technology | 96.7 | 77.0% | 116.5% | 348.1% | 896.7% | 3.48 | -30.3% |
| 2 | **SNDK** | Technology | 96.7 | 48.6% | 151.4% | 693.9% | 4164.9% | 3.87 | -31.3% |
| 3 | **INTC** | Technology | 96.2 | 43.3% | 159.8% | 253.0% | 507.3% | 2.53 | -24.2% |
| 4 | **STX** | Technology | 96.1 | 46.1% | 106.8% | 268.2% | 682.2% | 3.27 | -21.0% |
| 5 | **AMD** | Technology | 96.0 | 48.1% | 135.0% | 143.2% | 349.2% | 2.30 | -27.8% |
| 6 | **WDC** | Technology | 95.9 | 32.4% | 82.5% | 281.7% | 962.0% | 3.72 | -20.6% |
| 7 | **DELL** | Technology | 95.0 | 41.4% | 148.0% | 151.1% | 176.5% | 1.81 | -32.3% |
| 8 | **ON** | Technology | 94.2 | 27.4% | 79.2% | 167.4% | 202.6% | 1.99 | -28.1% |
| 9 | **CIEN** | Technology | 94.0 | 15.0% | 64.7% | 226.5% | 625.6% | 3.02 | -16.8% |
| 10 | **CSCO** | Technology | 93.7 | 35.6% | 52.1% | 59.0% | 94.0% | 2.10 | -13.6% |
| 11 | **HPE** | Technology | 93.6 | 30.0% | 81.5% | 83.5% | 119.0% | 1.80 | -23.7% |
| 12 | **COHR** | Technology | 93.0 | 18.2% | 41.9% | 172.5% | 384.6% | 2.20 | -26.5% |
| 13 | **LRCX** | Technology | 92.9 | 22.9% | 28.0% | 124.2% | 296.3% | 2.68 | -20.0% |
| 14 | **NUE** | Basic Materials | 92.3 | 14.6% | 40.9% | 62.9% | 130.6% | 2.56 | -18.4% |
| 15 | **TXN** | Technology | 91.9 | 18.4% | 49.2% | 101.5% | 85.1% | 1.50 | -29.6% |
| 16 | **PWR** | Industrials | 90.8 | 15.1% | 30.4% | 70.6% | 119.0% | 2.08 | -11.7% |
| 17 | **AKAM** | Technology | 90.3 | 50.6% | 44.4% | 62.3% | 90.4% | 1.16 | -25.4% |
| 18 | **STLD** | Basic Materials | 90.3 | 14.7% | 35.2% | 64.2% | 108.8% | 2.01 | -20.3% |
| 19 | **NXPI** | Technology | 90.2 | 39.0% | 40.8% | 73.7% | 74.6% | 1.18 | -24.6% |
| 20 | **DDOG** | Technology | 89.8 | 67.2% | 101.0% | 40.8% | 93.8% | 1.02 | -48.6% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **NOKIA.HE** | Technology | 95.2 | 51.1% | 110.7% | 140.9% | 190.7% | 2.27 | -27.6% |
| 2 | **TPRO.MI** | Technology | 94.7 | 79.8% | 76.6% | 161.2% | 349.4% | 2.49 | -27.0% |
| 3 | **STMMI.MI** | Technology | 94.6 | 36.9% | 102.0% | 208.5% | 162.0% | 1.94 | -33.5% |
| 4 | **AIXA.DE** | Technology | 94.3 | 29.9% | 137.4% | 229.7% | 363.6% | 2.47 | -28.4% |
| 5 | **IFX.DE** | Technology | 94.2 | 43.1% | 64.4% | 134.9% | 124.5% | 1.87 | -21.2% |
| 6 | **PRY.MI** | Industrials | 93.1 | 17.6% | 50.8% | 75.1% | 155.3% | 2.47 | -11.9% |
| 7 | **UMI.BR** | Basic Materials | 92.9 | 54.1% | 42.8% | 79.7% | 172.4% | 2.02 | -28.7% |
| 8 | **HUBN.SW** | Industrials | 92.9 | 16.8% | 46.6% | 88.5% | 235.3% | 3.01 | -13.5% |
| 9 | **BESI.AS** | Technology | 90.8 | 11.4% | 44.6% | 123.6% | 161.0% | 1.88 | -20.9% |
| 10 | **NHY.OL** | Basic Materials | 89.5 | 8.8% | 38.5% | 60.2% | 102.1% | 2.43 | -11.5% |
| 11 | **IGG.L** | Financial Services | 89.1 | 20.1% | 38.1% | 75.4% | 62.0% | 1.84 | -11.5% |
| 12 | **NKT.CO** | Industrials | 88.2 | 15.2% | 30.5% | 50.1% | 108.1% | 1.96 | -14.8% |
| 13 | **NDA.DE** | Basic Materials | 88.0 | 9.0% | 19.1% | 93.0% | 165.5% | 2.67 | -15.3% |
| 14 | **DHER.DE** | Consumer Cyclical | 87.8 | 99.4% | 101.2% | 140.8% | 53.8% | 0.65 | -48.7% |
| 15 | **GL9.IR** | Consumer Defensive | 87.3 | 20.8% | 29.7% | 47.8% | 70.7% | 1.87 | -8.0% |
| 16 | **NESTE.HE** | Energy | 86.8 | 2.1% | 29.8% | 54.8% | 198.3% | 2.56 | -20.4% |
| 17 | **HOT.DE** | Industrials | 86.7 | 6.4% | 19.3% | 68.0% | 196.1% | 2.56 | -15.9% |
| 18 | **ASM.AS** | Technology | 86.2 | 7.3% | 25.1% | 88.3% | 87.2% | 1.41 | -26.2% |
| 19 | **ACS.MC** | Industrials | 85.7 | 4.4% | 16.9% | 67.5% | 124.8% | 2.55 | -12.0% |
| 20 | **ABBN.SW** | Industrials | 85.5 | 7.1% | 20.8% | 50.6% | 77.5% | 2.07 | -12.1% |



---

## 12. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **APA** | Energy | 0.782 | 0.904 | 0.761 | 0.870 | 0.436 | +123.7% | 8.5 | +26.2% |
| 2 | **SNDK** | Information Technology | 0.754 | 0.998 | 0.848 | 0.500 | 0.500 | +4255.6% | 56.1 | +39.3% |
| 3 | **TROW** | Financials | 0.730 | 0.622 | 0.734 | 0.878 | 0.690 | +16.6% | 11.2 | +18.7% |
| 4 | **EOG** | Energy | 0.724 | 0.747 | 0.638 | 0.826 | 0.680 | +28.4% | 13.2 | +18.2% |
| 5 | **AAPL** | Information Technology | 0.716 | 0.780 | 0.883 | 0.500 | 0.615 | +56.2% | 37.8 | +141.5% |
| 6 | **KLAC** | Information Technology | 0.707 | 0.935 | 0.898 | 0.500 | 0.217 | +156.3% | 54.7 | +95.0% |
| 7 | **ANET** | Information Technology | 0.707 | 0.821 | 0.869 | 0.500 | 0.500 | +79.2% | 53.2 | +31.5% |
| 8 | **FTNT** | Information Technology | 0.703 | 0.870 | 0.885 | 0.500 | 0.339 | +27.4% | 50.3 | +132.4% |
| 9 | **HST** | Real Estate | 0.694 | 0.860 | 0.536 | 0.724 | 0.627 | +58.7% | 15.8 | +14.9% |
| 10 | **PFG** | Financials | 0.688 | 0.764 | 0.500 | 0.786 | 0.747 | +37.8% | 14.8 | +13.4% |
| 11 | **FFIV** | Information Technology | 0.685 | 0.882 | 0.662 | 0.500 | 0.646 | +34.4% | 31.5 | +20.3% |
| 12 | **GOOGL** | Communication Services | 0.684 | 0.881 | 0.722 | 0.500 | 0.524 | +128.0% | 29.8 | +38.9% |
| 13 | **GOOG** | Communication Services | 0.683 | 0.871 | 0.722 | 0.500 | 0.534 | +124.2% | 29.4 | +38.9% |
| 14 | **CBOE** | Financials | 0.678 | 0.831 | 0.788 | 0.304 | 0.777 | +51.0% | 29.4 | +25.1% |
| 15 | **MNST** | Consumer Staples | 0.677 | 0.706 | 0.756 | 0.500 | 0.757 | +37.6% | 42.5 | +26.7% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **BLDR** | Industrials | 0.217 | 0.056 | 0.172 | 0.500 | 0.161 |
| 502 | **NRG** | Utilities | 0.224 | 0.138 | 0.116 | 0.500 | 0.152 |
| 501 | **CSGP** | Real Estate | 0.228 | 0.016 | 0.106 | 0.500 | 0.439 |
| 500 | **AXON** | Industrials | 0.229 | 0.100 | 0.130 | 0.500 | 0.235 |
| 499 | **GPC** | Consumer Discretionary | 0.237 | 0.130 | 0.111 | 0.492 | 0.279 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W22.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W22.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-05-25  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
