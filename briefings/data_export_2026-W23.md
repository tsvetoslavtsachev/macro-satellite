# Сателит — пълен data export за 2026-W23

_Период: 2026-06-01 → 2026-06-07_  
_Генериран: 2026-06-05 09:53 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W23.md` (structured briefing) и `narrative_2026-W23.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**6 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **TIP** | -1.29% | -2.81σ | 111.21 | 109.78 | 2026-05-29 | 2026-06-04 | +0.03% | +0.47% | 7 |
| **IBIT** | -8.60% | -2.32σ | 41.63 | 38.05 | 2026-05-29 | 2026-06-02 | +0.95% | +4.12% | 13 |
| **DBA** | -2.06% | -1.92σ | 27.25 | 26.69 | 2026-05-29 | 2026-06-04 | +0.36% | +1.26% | 13 |
| **SHY** | -0.33% | -1.27σ | 82.30 | 82.03 | 2026-05-29 | 2026-06-04 | -0.02% | +0.25% | 13 |
| **XLY** | -2.99% | -1.12σ | 120.87 | 117.26 | 2026-05-29 | 2026-06-04 | +0.32% | +2.95% | 13 |
| **XLV** | +1.75% | +1.01σ | 149.47 | 152.08 | 2026-05-29 | 2026-06-04 | -0.48% | +2.21% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_5 канонични patterns от `config/divergence_rules.yaml`, evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — 🔔 ТРИГГЕРИРАН
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-06-07 · **Conditions matched:** 4/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | +5.93% | ✅ | 129.09 | 136.74 | 2026-05-29 | 2026-06-04 |
| DFEN | down ≥ 3.0% | -5.46% | ✅ | 75.07 | 70.97 | 2026-05-29 | 2026-06-04 |
| GLD | down ≥ 1.0% | -1.40% | ✅ | 417.12 | 411.27 | 2026-05-29 | 2026-06-04 |
| URA | down ≥ 3.0% | -0.95% | ❌ | 50.76 | 50.28 | 2026-05-29 | 2026-06-04 |
| UUP | up ≥ 0.5% | +0.65% | ✅ | 27.66 | 27.84 | 2026-05-29 | 2026-06-04 |

### Ликвидна стес (flight to quality) (`liquidity_stress`) — не активен
_Дългосрочни trezuri нагоре, високодоходен кредит надолу, злато нагоре. Класически risk-off._  
**Window:** 7d ending 2026-06-07 · **Conditions matched:** 2/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| TLT | up ≥ 1.0% | -0.30% | ❌ | 85.76 | 85.50 | 2026-05-29 | 2026-06-04 |
| HYG | down ≥ 0.5% | -0.60% | ✅ | 80.31 | 79.83 | 2026-05-29 | 2026-06-04 |
| GLD | up ≥ 1.0% | -1.40% | ❌ | 417.12 | 411.27 | 2026-05-29 | 2026-06-04 |
| UUP | up ≥ 0.3% | +0.65% | ✅ | 27.66 | 27.84 | 2026-05-29 | 2026-06-04 |

### Възстановяване на инфлационни очаквания (`inflation_pickup`) — не активен
_Inflation-protected треzuri нагоре, commodities нагоре, dollar надолу. Repricing на real rates._  
**Window:** 7d ending 2026-06-07 · **Conditions matched:** 0/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| DBC | up ≥ 1.5% | +1.36% | ❌ | 29.48 | 29.88 | 2026-05-29 | 2026-06-04 |
| GLD | up ≥ 1.0% | -1.40% | ❌ | 417.12 | 411.27 | 2026-05-29 | 2026-06-04 |
| UUP | down ≥ 0.5% | +0.65% | ❌ | 27.66 | 27.84 | 2026-05-29 | 2026-06-04 |
| TLT | down ≥ 1.0% | -0.30% | ❌ | 85.76 | 85.50 | 2026-05-29 | 2026-06-04 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-06-07 · **Conditions matched:** 2/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | +0.54% | ❌ | 290.43 | 292.01 | 2026-05-29 | 2026-06-04 |
| XLF | up ≥ 1.0% | +1.18% | ✅ | 51.58 | 52.19 | 2026-05-29 | 2026-06-04 |
| XLY | up ≥ 1.0% | -2.99% | ❌ | 120.87 | 117.26 | 2026-05-29 | 2026-06-04 |
| GLD | down ≥ 0.5% | -1.40% | ✅ | 417.12 | 411.27 | 2026-05-29 | 2026-06-04 |

### Защитен pivot (staples + utilities + gold) (`defensive_pivot`) — не активен
_XLP + XLU + GLD едновременно нагоре. Smart money flight to defensives без credit panic._  
**Window:** 7d ending 2026-06-07 · **Conditions matched:** 0/3

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| XLP | up ≥ 1.0% | -1.05% | ❌ | 82.91 | 82.04 | 2026-05-29 | 2026-06-04 |
| XLU | up ≥ 1.0% | -1.08% | ❌ | 44.42 | 43.94 | 2026-05-29 | 2026-06-04 |
| GLD | up ≥ 1.0% | -1.40% | ❌ | 417.12 | 411.27 | 2026-05-29 | 2026-06-04 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2024-W04 (week ending 2024-01-28)
**Cosine similarity:** 0.9589 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.00% | +4.60% | +12.41% |
| **USO** | +1.03% | +9.97% | +4.12% |
| **GLD** | +0.53% | +15.83% | +17.98% |
| **TLT** | -0.59% | -4.99% | +1.13% |
| **XLE** | +1.95% | +14.56% | +11.19% |
| **IWM** | +4.09% | +1.47% | +15.02% |

### Паралел #2: 2024-W40 (week ending 2024-10-06)
**Cosine similarity:** 0.9402 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.65% | +3.66% | -11.25% |
| **USO** | -2.12% | +2.06% | -11.04% |
| **GLD** | +3.43% | -0.62% | +14.17% |
| **TLT** | -2.61% | -7.66% | -0.76% |
| **XLE** | -3.23% | -5.34% | -14.10% |
| **IWM** | +2.32% | +2.71% | -16.89% |

### Паралел #3: 2022-W40 (week ending 2022-10-09)
**Cosine similarity:** 0.9352 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.30% | +7.46% | +13.74% |
| **USO** | -0.84% | -13.68% | -6.44% |
| **GLD** | +0.99% | +10.03% | +18.12% |
| **TLT** | -6.39% | +4.91% | +9.07% |
| **XLE** | +13.79% | +8.14% | +6.05% |
| **IWM** | +6.49% | +5.81% | +3.99% |

### Паралел #4: 2024-W25 (week ending 2024-06-23)
**Cosine similarity:** 0.9231 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.70% | +4.68% | +9.27% |
| **USO** | -2.58% | -7.29% | -7.06% |
| **GLD** | +3.63% | +12.77% | +12.72% |
| **TLT** | -1.22% | +6.27% | -3.76% |
| **XLE** | +1.45% | -0.31% | -4.72% |
| **IWM** | +11.12% | +10.59% | +11.47% |

### Паралел #5: 2026-W05 (week ending 2026-02-01)
**Cosine similarity:** 0.8974 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.68% | +4.43% | +9.71% |
| **USO** | +13.43% | +79.58% | +71.96% |
| **GLD** | +5.21% | -4.89% | -7.57% |
| **TLT** | +3.37% | -0.28% | -0.41% |
| **XLE** | +10.71% | +16.03% | +15.84% |
| **IWM** | -0.16% | +7.75% | +12.66% |

### Паралел #6: 2022-W12 (week ending 2022-03-27)
**Cosine similarity:** 0.8946 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -8.08% | -13.46% | -18.03% |
| **USO** | -5.30% | +0.66% | -19.10% |
| **GLD** | -2.77% | -6.74% | -16.10% |
| **TLT** | -4.71% | -12.07% | -16.94% |
| **XLE** | -6.31% | -8.07% | -8.51% |
| **IWM** | -8.92% | -14.83% | -18.61% |

### Паралел #7: 2021-W22 (week ending 2021-06-06)
**Cosine similarity:** 0.8940 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.78% | +7.56% | +7.99% |
| **USO** | +5.59% | +2.96% | +1.57% |
| **GLD** | -5.10% | -3.44% | -5.94% |
| **TLT** | +5.03% | +6.32% | +11.16% |
| **XLE** | -4.12% | -11.90% | +1.13% |
| **IWM** | -0.53% | +0.40% | -5.15% |

### Паралел #8: 2021-W38 (week ending 2021-09-26)
**Cosine similarity:** 0.8899 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.71% | +6.38% | +2.65% |
| **USO** | +12.79% | +2.53% | +55.81% |
| **GLD** | +2.68% | +3.47% | +11.68% |
| **TLT** | -1.11% | +1.59% | -11.75% |
| **XLE** | +16.19% | +9.26% | +58.22% |
| **IWM** | +2.15% | -0.15% | -7.13% |

### Паралел #9: 2021-W40 (week ending 2021-10-10)
**Cosine similarity:** 0.8876 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +6.74% | +6.82% | +2.90% |
| **USO** | +4.51% | +2.16% | +33.60% |
| **GLD** | +4.30% | +2.14% | +10.50% |
| **TLT** | +6.54% | +0.63% | -11.12% |
| **XLE** | +4.35% | +9.84% | +43.77% |
| **IWM** | +8.83% | -2.19% | -10.25% |

### Паралел #10: 2025-W43 (week ending 2025-10-26)
**Cosine similarity:** 0.8848 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -0.33% | +2.07% | +6.02% |
| **USO** | -5.37% | +1.05% | +80.92% |
| **GLD** | +0.68% | +21.32% | +14.76% |
| **TLT** | -0.99% | -2.80% | -2.72% |
| **XLE** | +0.61% | +12.66% | +31.10% |
| **IWM** | -1.72% | +6.52% | +11.48% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 13 · **Total matching days:** 72 · **History:** 2021-05-17 → 2026-06-04

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 13 | +2.0% | +1.7% | -3.1% | +7.7% | 77% |
| **SPY** | 3m | 13 | +3.6% | +4.6% | -7.0% | +14.8% | 77% |
| **SPY** | 6m | 13 | +8.5% | +11.6% | -6.1% | +22.7% | 77% |
| **USO** | 1m | 13 | +1.0% | -0.8% | -7.2% | +12.7% | 46% |
| **USO** | 3m | 13 | +0.1% | +0.1% | -18.9% | +24.5% | 54% |
| **USO** | 6m | 13 | +13.1% | +0.0% | -8.7% | +109.4% | 54% |
| **GLD** | 1m | 13 | +2.5% | +0.9% | -2.2% | +8.9% | 77% |
| **GLD** | 3m | 13 | +6.7% | +5.9% | -7.5% | +24.5% | 69% |
| **GLD** | 6m | 13 | +7.2% | +10.3% | -12.5% | +25.3% | 69% |
| **TLT** | 1m | 13 | -1.1% | -0.8% | -6.5% | +3.7% | 31% |
| **TLT** | 3m | 13 | +0.4% | +0.6% | -16.2% | +12.6% | 54% |
| **TLT** | 6m | 13 | -2.4% | -0.9% | -17.2% | +9.1% | 38% |

**Episodes (последни 5 от 13):**
- `2024-06-21 → 2024-06-21` (1d)
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-28 → 2026-05-19` (13d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 1 · **Total matching days:** 43 · **History:** 2021-05-17 → 2026-06-04

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | +9.1% | +9.1% | +9.1% | +9.1% | 100% |
| **SPY** | 3m | 1 | +12.0% | +12.0% | +12.0% | +12.0% | 100% |
| **SPY** | 6m | 1 | +12.0% | +12.0% | +12.0% | +12.0% | 100% |
| **USO** | 1m | 1 | +7.2% | +7.2% | +7.2% | +7.2% | 100% |
| **USO** | 3m | 1 | +9.8% | +9.8% | +9.8% | +9.8% | 100% |
| **USO** | 6m | 1 | +9.8% | +9.8% | +9.8% | +9.8% | 100% |
| **GLD** | 1m | 1 | -0.2% | -0.2% | -0.2% | -0.2% | 0% |
| **GLD** | 3m | 1 | -5.4% | -5.4% | -5.4% | -5.4% | 0% |
| **GLD** | 6m | 1 | -5.4% | -5.4% | -5.4% | -5.4% | 0% |
| **TLT** | 1m | 1 | -0.6% | -0.6% | -0.6% | -0.6% | 0% |
| **TLT** | 3m | 1 | -1.3% | -1.3% | -1.3% | -1.3% | 0% |
| **TLT** | 6m | 1 | -1.3% | -1.3% | -1.3% | -1.3% | 0% |

**Episodes (последни 5 от 1):**
- `2026-04-08 → 2026-06-04` (43d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 7 · **Total matching days:** 757 · **History:** 2021-05-17 → 2026-06-04

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
- `2024-10-04 → 2026-06-04` (419d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-06-04

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 9 · **Total matching days:** 76 · **History:** 2021-05-17 → 2026-06-04

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 9 | +0.4% | +0.9% | -7.2% | +7.8% | 56% |
| **SPY** | 3m | 9 | +2.7% | +6.4% | -8.0% | +12.0% | 56% |
| **SPY** | 6m | 9 | +2.1% | +6.4% | -20.2% | +14.9% | 67% |
| **USO** | 1m | 9 | +2.0% | -1.7% | -15.0% | +52.9% | 33% |
| **USO** | 3m | 9 | +7.4% | -0.1% | -20.7% | +52.2% | 44% |
| **USO** | 6m | 9 | +9.1% | -0.2% | -27.6% | +51.6% | 44% |
| **GLD** | 1m | 9 | -2.2% | -1.6% | -8.3% | +1.9% | 11% |
| **GLD** | 3m | 9 | -1.5% | -1.5% | -12.0% | +6.4% | 44% |
| **GLD** | 6m | 9 | -0.2% | -1.5% | -12.1% | +25.0% | 33% |
| **TLT** | 1m | 9 | -1.7% | -2.2% | -5.7% | +2.6% | 22% |
| **TLT** | 3m | 9 | -5.6% | -4.9% | -16.9% | +5.4% | 22% |
| **TLT** | 6m | 9 | -8.6% | -6.1% | -21.7% | +3.4% | 11% |

**Episodes (последни 5 от 9):**
- `2023-04-12 → 2023-04-18` (5d)
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-04-09` (27d)
- `2026-04-29 → 2026-05-19` (7d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 16 · **Total matching days:** 275 · **History:** 2021-05-17 → 2026-06-04

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.2% | +2.2% | -4.8% | +9.0% | 75% |
| **SPY** | 3m | 16 | +3.8% | +5.5% | -12.3% | +16.7% | 75% |
| **SPY** | 6m | 16 | +7.5% | +8.3% | -13.5% | +21.9% | 81% |
| **USO** | 1m | 16 | +1.8% | -3.2% | -13.0% | +27.7% | 38% |
| **USO** | 3m | 16 | +2.9% | -1.7% | -14.5% | +29.9% | 38% |
| **USO** | 6m | 16 | +12.6% | +2.3% | -12.4% | +87.1% | 69% |
| **GLD** | 1m | 16 | +2.4% | +1.8% | -6.4% | +9.0% | 75% |
| **GLD** | 3m | 16 | +6.8% | +7.4% | -7.8% | +23.6% | 69% |
| **GLD** | 6m | 16 | +11.5% | +12.1% | -8.4% | +43.8% | 75% |
| **TLT** | 1m | 16 | +0.6% | +0.7% | -6.1% | +8.5% | 56% |
| **TLT** | 3m | 16 | -0.6% | -0.3% | -14.7% | +13.0% | 50% |
| **TLT** | 6m | 16 | -2.8% | -1.0% | -20.6% | +8.6% | 44% |

**Episodes (последни 5 от 16):**
- `2025-03-27 → 2025-05-08` (25d)
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-17 → 2026-04-23` (4d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 18 · **Total matching days:** 289 · **History:** 2021-05-17 → 2026-06-04

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 18 | +0.4% | +1.1% | -8.3% | +7.0% | 50% |
| **SPY** | 3m | 18 | +2.3% | +3.5% | -13.3% | +9.4% | 67% |
| **SPY** | 6m | 18 | +3.9% | +7.6% | -15.7% | +17.6% | 72% |
| **USO** | 1m | 18 | +0.6% | -3.7% | -14.3% | +55.8% | 44% |
| **USO** | 3m | 18 | +3.7% | -1.0% | -12.7% | +64.3% | 44% |
| **USO** | 6m | 18 | +9.6% | -0.1% | -16.0% | +75.1% | 50% |
| **GLD** | 1m | 18 | -0.3% | +0.0% | -12.4% | +7.6% | 50% |
| **GLD** | 3m | 18 | +1.8% | +1.5% | -13.7% | +19.0% | 67% |
| **GLD** | 6m | 18 | +8.3% | +6.0% | -15.8% | +55.5% | 72% |
| **TLT** | 1m | 18 | +0.1% | +0.3% | -5.5% | +5.5% | 56% |
| **TLT** | 3m | 18 | -2.9% | -4.0% | -16.8% | +9.8% | 39% |
| **TLT** | 6m | 18 | -5.4% | -5.0% | -20.5% | +6.7% | 28% |

**Episodes (последни 5 от 18):**
- `2024-10-10 → 2025-01-17` (52d)
- `2025-05-12 → 2025-05-19` (3d)
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-06-04

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (18 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **M2** | M2 паричен агрегат | liquidity | money_supply | 5 | 2.76 | 2.76 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **DGORDER** | Нови поръчки за дълготрайни стоки | growth | hard_activity | 5 | 2.57 | 2.90 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **C_AND_I_LOANS** | Търговски и индустриални кредити (C&I) | liquidity | banking_credit | 5 | 2.56 | 2.57 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **UMCSENT** | Michigan Sentiment Index | growth | consumer_sentiment | 5 | 2.47 | 2.57 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CPI_SHELTER** | CPI — жилища (shelter) | inflation | goods_services | 5 | 2.46 | 2.46 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 5 | 2.37 | 2.59 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CPI_SERVICES** | CPI — услуги (всички) | inflation | goods_services | 5 | 2.35 | 2.35 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 5 | 2.31 | 2.34 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **RSXFS** | Продажби на дребно (без храна) | growth | hard_activity | 4 | 2.33 | 2.33 | 2026-05-15 00:00:00 | 2026-05-30 00:00:00 | ✓ |
| **PPICORE** | PPI Core (Final Demand без храни и енергия) | inflation | core_measures | 4 | 2.32 | 2.32 | 2026-05-15 00:00:00 | 2026-05-30 00:00:00 | ✓ |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 1 | 2.76 | 2.76 | 2026-06-04 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **USSTHPI** | FHFA House Price Index (Q, NSA) | housing | housing_prices | 1 | 2.70 | 2.70 | 2026-06-04 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | 1 | 2.40 | 2.40 | 2026-06-04 00:00:00 | 2026-06-04 00:00:00 | - |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | 1 | 2.30 | 2.30 | 2026-06-04 00:00:00 | 2026-06-04 00:00:00 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 1 | 2.29 | 2.29 | 2026-06-04 00:00:00 | 2026-06-04 00:00:00 | - |
| **CSUSHPISA** | Case-Shiller US National HPI (SA) | housing | housing_prices | 1 | 2.26 | 2.26 | 2026-06-04 00:00:00 | 2026-06-04 00:00:00 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | 1 | 2.10 | 2.10 | 2026-06-04 00:00:00 | 2026-06-04 00:00:00 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | 1 | 2.02 | 2.02 | 2026-06-04 00:00:00 | 2026-06-04 00:00:00 | ✓ |

### EU (13 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_RETAIL_CONF** | Доверие в търговията на дребно (DG ECFIN) | growth | sentiment | 6 | 2.49 | 2.68 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **EA_COMP_PER_EMPLOYEE** | Компенсация на наетите (D1, EA-20, M€) | labor | wages | 6 | 2.39 | 2.39 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **EA_PPI_INTERMEDIATE** | PPI междинни стоки (MIG ING, индекс 2021=100) | inflation | producer_prices | 6 | 2.04 | 2.16 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | - |
| **EA_RETAIL_VOL** | Търговия на дребно — обем на продажбите (G47, индекс 2021=100) | growth | hard_activity | 6 | 2.02 | 2.06 | 2026-05-15 00:00:00 | 2026-06-04 00:00:00 | - |
| **EA_EMPLOYMENT_EXP** | Очаквания за заетост (3m напред) | labor | labor_sentiment | 3 | 3.14 | 3.14 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **EA_ESI** | Икономически Sentiment Indicator (DG ECFIN ESI) | growth | sentiment | 3 | 2.25 | 2.25 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **EA_CONSUMER_CONF** | Потребителско доверие (DG ECFIN, full history от 1985) | growth | sentiment | 3 | 2.10 | 2.10 | 2026-05-15 00:00:00 | 2026-05-23 00:00:00 | - |
| **EA_WAGES_SALARIES** | Работни заплати (D11, EA-20, M€) | labor | wages | 2 | 2.38 | 2.38 | 2026-06-03 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 1 | 5.37 | 5.37 | 2026-06-05 00:00:00 | 2026-06-05 00:00:00 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation | sentiment | 1 | 2.98 | 2.98 | 2026-06-05 00:00:00 | 2026-06-05 00:00:00 | - |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | 1 | 2.32 | 2.32 | 2026-06-05 00:00:00 | 2026-06-05 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 1 | 2.31 | 2.31 | 2026-06-05 00:00:00 | 2026-06-05 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 1 | 2.23 | 2.23 | 2026-06-05 00:00:00 | 2026-06-05 00:00:00 | ✓ |

### CN (7 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 2 | 2.56 | 2.56 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CN_POLICY_RATE** | Политическа лихва — PBoC 7-day repo (%) | credit | rates | 2 | 2.39 | 2.39 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 2 | 2.24 | 2.24 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | - |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 2 | 2.23 | 2.23 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CN_FDI_GDP** | ПЧИ — входящи (% от БВП) | property | investment | 2 | 2.11 | 2.11 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CN_BIS_PROPERTY_YOY** | Жилищни имотни цени (YoY %, BIS номинал) | property | housing | 2 | 2.10 | 2.10 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | - |
| **CN_CREDIT_PRIVATE** | Кредит към частния сектор (% от БВП) | credit | credit_depth | 2 | 2.07 | 2.07 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-06-04 00:00:00 · **Generated:** 2026-06-04 21:41:09.191760+00:00

**Режим:** `stagflation_confirmed` (Стагфлация (потвърдена))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 35.3 | contracting | 25.9% | 2 | 2 |
| **growth** | 45.2 | mixed | 44.4% | 1 | 0 |
| **inflation** | 34.1 | contracting | 22.2% | 5 | 1 |
| **liquidity** | 51.6 | mixed | 46.7% | 0 | 0 |

### Top anomalies (9 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | -2.76 | down | 1.71 | 2026-03-01 | ✓ min |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | +2.59 | up | 5.99 | 2026-04-01 | - |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | -2.40 | down | 2.60 | 2026-04-01 | - |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.34 | down | 94.99 | 2026-01-01 | ✓ min |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | +2.30 | up | 5.23 | 2026-04-01 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | +2.29 | up | 4.70 | 2026-04-01 | - |
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
  - `state`: a_up_b_down
  - `interpretation`: Модел persistent, пазар разчита на disinflation — contrarian hawkish (моделът обикновено лидера).
  - `slot_a_label`: Модел (sticky inflation)
  - `slot_b_label`: Пазар (breakevens + survey)
  - `breadth_a`: 1.0
  - `breadth_b`: 0.333

### Executive narrative
> Картината показва потвърдена стагфлационна конфигурация — трудовият пазар остава tight, а инфлационният натиск е broad-based. Най-отклонена леща: Инфлация и цени — breadth 76% (разширяване), 5 аномалии, 1 нови екстремума. Обаче inflation expectations остават anchored — Fed narrative-ът за момента държи. За наблюдение следващия релиз: HPIPONM226S, LABOR_SHARE_NBS (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: HPIPONM226S z=-2.76 · NEW-5Y-MIN
- 3 нови екстремуми в top-9 (lookback 5г.)
- Активни двойки: Stagflation test=both_up; Growth × Labor=a_up_b_down; Inflation anchoring=a_up_b_down



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-06-05 00:00:00 · **Generated:** 2026-06-05 07:49:38.699074+00:00

**Режим:** `soft_landing` (Soft landing)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 37.8 | mixed | 57.1% | 1 | 0 |
| **growth** | 50.3 | mixed | 20.0% | 1 | 0 |
| **inflation** | 46.1 | mixed | 71.4% | 1 | 0 |
| **credit** | 42.2 | mixed | 36.8% | 3 | 2 |

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
  - `breadth_b`: 0.75

### Executive narrative
> Конфигурацията подкрепя soft landing — labor остава tight, но инфлацията се охлажда. Fed credibility за момента издържа. Най-отклонена леща: Инфлация и цени — breadth 17% (свиване), 1 аномалии, 0 нови екстремума. За наблюдение следващия релиз: FR_10Y, DE_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.37
- 2 нови екстремуми в top-5 (lookback 5г.)
- Активни двойки: Stagflation test=a_up_b_down; ecb_transmission=a_up_b_down; fragmentation_risk=a_up_b_down



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-06-04 00:00:00 · **Generated:** 2026-06-04 18:51:16.876243+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 30.6 | contracting | -% | - | - |
| **inflation** | 50.6 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 48.5 | mixed | -% | - | - |
| **property** | 25.6 | contracting | -% | - | - |

### Top anomalies (7 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | -2.56 | down | 3.00 | 2026-05-20 | ✓ min |
| **CN_POLICY_RATE** | Политическа лихва — PBoC 7-day repo (%) | credit | rates | -2.39 | down | 1.40 | 2025-06-01 | ✓ min |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | -2.24 | down | 1.72 | 2026-05-31 | - |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | +2.23 | up | 15.79 | 2025-12-31 | ✓ max |
| **CN_FDI_GDP** | ПЧИ — входящи (% от БВП) | property | investment | -2.11 | down | 0.10 | 2024-12-31 | ✓ min |
| **CN_BIS_PROPERTY_YOY** | Жилищни имотни цени (YoY %, BIS номинал) | property | housing | -2.10 | down | -7.52 | 2025-03-31 | - |
| **CN_CREDIT_PRIVATE** | Кредит към частния сектор (% от БВП) | credit | credit_depth | +2.07 | up | 194.17 | 2024-12-31 | ✓ max |

### Narrative hints от макро лещите
- **CN_LPR_1Y**: Замества benchmark lending rate от 2019. Главен policy signal.
- **CN_POLICY_RATE**: PBoC benchmark rate. Намален до 1.4% (2025). Monetary easing цикъл в ход.
- **CN_CGB_10Y**: Sovereign benchmark. CGB-UST 10Y spread = capital flow incentive.
- **CN_YOUTH_UNEMPLOYMENT**: Рекорд 21.3% юни 2023. НБС спря публикуването за 6 месеца. Структурен проблем — образователна система произвежда повече дипломирани, отколкото пазарът може да абсорбира.
- **CN_FDI_GDP**: Срина се до 0.10% GDP (2024) — исторически минимум. Геополитически de-risking от западни компании. Структурна промяна в глобалните вериги на доставки.
- **CN_BIS_PROPERTY_YOY**: BIS жилищни имотни цени YoY (тримесечно, −7.5% 2025-Q1). По-широко покритие (вкл. вторичен пазар) и по-дълга чиста история от 70-градския akshare индекс. Дълбока имотна дефлация.
- **CN_CREDIT_PRIVATE**: 194% от GDP (2024) — изключително висок. Debt overhang ограничава monetary policy transmission. Кредитният импулс (промяна в новия кредит) е по-важен от нивото.

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
> Претеглен композитен macro score 35.9/100 → режим „ВЛОШАВАЩ СЕ“. 5 лещи, 7 flagged аномалии, 3 cross-lens двойки.



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

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-05-29 → 2026-06-03)

**stable_winner (1m):** +11 entered, -9 exited
  - **Entered:** ALB, BEN, BIIB, CBRE, COHR, EL, EME, IBKR, PWR, WMT, WYNN _(включително 4 за първи път в историята: BEN, BIIB, EL, PWR)_
  - **Exited:** BK, C, CHRW, EBAY, INCY, JNJ, NEM, O, ULTA

**stable_winner (3m):** +7 entered, -6 exited
  - **Entered:** BEN, BIIB, GS, IBKR, PWR, WELL, WYNN _(включително 3 за първи път в историята: BEN, BIIB, WYNN)_
  - **Exited:** EBAY, HAS, HST, INCY, JNJ, LITE

**quality_dip (1m):** +8 entered, -9 exited
  - **Entered:** BK, C, CHRW, INCY, JNJ, NEM, O, ULTA _(включително 2 за първи път в историята: BK, CHRW)_
  - **Exited:** ALB, CBRE, COHR, EL, EME, IBKR, PWR, WMT, WYNN

**quality_dip (3m):** +5 entered, -5 exited
  - **Entered:** HAS, HST, INCY, JNJ, LITE _(включително 1 за първи път в историята: JNJ)_
  - **Exited:** GS, IBKR, PWR, WELL, WYNN

**faded_bounce (1m):** +15 entered, -12 exited
  - **Entered:** ARE, ARES, BX, CARR, DPZ, FIS, GPN, KVUE, LULU, LYB, NKE, PGR, RVTY, STZ, TPL _(включително 4 за първи път в историята: DPZ, FIS, NKE, TPL)_
  - **Exited:** BF-B, BRO, CAG, EOG, ERIE, GIS, IP, PEG, TTD, TYL, UPS, ZBH

**faded_bounce (3m):** +9 entered, -10 exited
  - **Entered:** BR, BX, CMG, DPZ, EFX, FDS, KKR, LULU, RVTY _(включително 3 за първи път в историята: BR, BX, DPZ)_
  - **Exited:** BLDR, CLX, ERIE, IP, MRSH, PCG, PGR, TAP, TYL, ZTS

### EU (period: 2026-05-29 → 2026-06-03)

**stable_winner (1m):** +7 entered, -8 exited
  - **Entered:** BARC.L, BATS.L, CBK.DE, FR.PA, PRY.MI, SPSN.SW, UMI.BR _(включително 1 за първи път в историята: PRY.MI)_
  - **Exited:** ACLN.SW, ENR.DE, GLE.PA, INGA.AS, MRL.MC, PRX.AS, SAND.ST, TIT.MI

**stable_winner (3m):** +8 entered, -7 exited
  - **Entered:** BAMI.MI, BIRG.IR, ELI.BR, ENGI.PA, FR.PA, PRY.MI, VWS.CO, ZEG.L _(включително 2 за първи път в историята: ELI.BR, PRY.MI)_
  - **Exited:** ACLN.SW, BBY.L, HM-B.ST, IG.MI, INGA.AS, PAF.L, UNI.MI

**quality_dip (1m):** +6 entered, -7 exited
  - **Entered:** ACLN.SW, ENR.DE, GLE.PA, MRL.MC, SAND.ST, TIT.MI
  - **Exited:** BARC.L, BATS.L, CBK.DE, FR.PA, R3NK.DE, SPSN.SW, UMI.BR

**quality_dip (3m):** +6 entered, -9 exited
  - **Entered:** ACLN.SW, BBY.L, HM-B.ST, IG.MI, PAF.L, UNI.MI _(включително 3 за първи път в историята: ACLN.SW, BBY.L, PAF.L)_
  - **Exited:** BAMI.MI, BIRG.IR, ELI.BR, ENGI.PA, FR.PA, PRX.AS, R3NK.DE, VWS.CO, ZEG.L

**faded_bounce (1m):** +6 entered, -13 exited
  - **Entered:** DKSH.SW, NEXI.MI, RI.PA, SAP.DE, TOM.OL, ZURN.SW _(включително 1 за първи път в историята: SAP.DE)_
  - **Exited:** AAK.ST, BALD-B.ST, DSFIR.AS, III.L, INDT.ST, P911.DE, PUIG.MC, RMV.L, RNO.PA, SIKA.SW, SY1.DE, THULE.ST, ZAL.DE

**faded_bounce (3m):** +12 entered, -9 exited
  - **Entered:** ARCAD.AS, AUTO.L, DHER.DE, GFC.PA, LIFCO-B.ST, NEXI.MI, REY.MI, SGE.L, WISE.L, WKL.AS, WPP.L, ZAL.DE _(включително 5 за първи път в историята: AUTO.L, DHER.DE, LIFCO-B.ST, NEXI.MI, REY.MI)_
  - **Exited:** BALD-B.ST, DGE.L, EQNR.OL, EXO.AS, LEG.DE, P911.DE, PGHN.SW, PUIG.MC, RNO.PA



---

## 11. COT positioning — текуща картина (cot_monitor + cot_cta)

### COT Monitor (38 markets) (snapshot: 2026-05-26 00:00:00)
| Market | Asset class | Net position | Net % | Percentile 5y | Weekly change |
|---|---|---:|---:|---:|---:|
| **soyoil** | Commodities | 141418 | 98.7 | 98.7 | -24307 |
| **aud** | FX | 60234 | 96.8 | 96.8 | 12379 |
| **soymeal** | Commodities | 122979 | 96.4 | 96.4 | 1790 |
| **soybeans** | Commodities | 189552 | 92.8 | 92.8 | 4270 |
| **copper** | Commodities | 71974 | 87.2 | 87.2 | 11178 |
| **cattle** | Commodities | 120569 | 86.1 | 86.1 | -16022 |
| **rbob** | Commodities | 67283 | 83.1 | 83.1 | 4453 |
| **corn** | Commodities | 205504 | 75.8 | 75.8 | -58599 |
| **gbpfx** | FX | 28829 | 74.8 | 74.8 | -53 |
| **brent** | Commodities | 11917 | 73.3 | 73.3 | -4157 |
| **eurfx** | FX | 7296 | 69.5 | 69.5 | -4298 |
| **us30y** | Rates | -320746 | 64.9 | 64.9 | -96917 |
| **cotton** | Commodities | 54200 | 64.7 | 64.7 | 15845 |
| **platinum** | Commodities | 12934 | 64.1 | 64.1 | -1031 |
| **wheat** | Commodities | -18706 | 61.5 | 61.5 | -29370 |
| **vix** | Volatility | -49336 | 58.0 | 58.0 | -9015 |
| **us5y** | Rates | -2071353 | 50.2 | 50.2 | 337019 |
| **us2y** | Rates | -1772557 | 47.6 | 47.6 | 345451 |
| **usultra10y** | Rates | -239726 | 45.8 | 45.8 | -17937 |
| **coffee** | Commodities | 17434 | 45.2 | 45.2 | -11976 |
| **chf** | FX | -4823 | 37.4 | 37.4 | 351 |
| **gold** | Commodities | 96931 | 36.5 | 36.5 | 5357 |
| **bitcoin** | Crypto | -8634 | 29.2 | 29.2 | 1726 |
| **heatingoil** | Commodities | 7730 | 29.0 | 29.0 | -4847 |
| **silver** | Commodities | 10244 | 26.7 | 26.7 | -501 |
| **cad** | FX | -38095 | 25.8 | 25.8 | 15733 |
| **palladium** | Commodities | -3773 | 25.4 | 25.4 | -1431 |
| **natgas** | Commodities | -7516 | 24.4 | 24.4 | 388 |
| **wti** | Commodities | -24599 | 24.2 | 24.2 | 2404 |
| **hogs** | Commodities | 12985 | 21.8 | 21.8 | -44580 |
| **sugar** | Commodities | -92323 | 21.4 | 21.4 | 95022 |
| **us10y** | Rates | -2005980 | 19.6 | 19.6 | 89819 |
| **russell** | US Equities | -68212 | 17.2 | 17.2 | -2937 |
| **cocoa** | Commodities | -18148 | 16.2 | 16.2 | 1737 |
| **dxy** | FX | -12530 | 12.9 | 12.9 | -9369 |
| **jpy** | FX | -70508 | 10.5 | 10.5 | 5294 |
| **sp500** | US Equities | -457780 | 5.2 | 5.2 | -50290 |
| **nasdaq** | US Equities | -70676 | 0.4 | 0.4 | -15013 |

### COT/CTA Positioning (11 markets) (snapshot: 2026-05-26 00:00:00)
| Market | Asset class | Net position | Net % | Percentile 5y | Weekly change |
|---|---|---:|---:|---:|---:|
| **corn** | Commodities | 205504 | 88.5 | 88.5 | -58599 |
| **wti** | Commodities | -24599 | 81.4 | 81.4 | 2404 |
| **bitcoin** | Crypto | -8634 | 79.5 | 79.5 | 1726 |
| **eurfx** | FX | 7296 | 44.9 | 44.9 | -4298 |
| **gbpfx** | FX | 28829 | 35.3 | 35.3 | -53 |
| **us10y** | Rates | -2005980 | 28.2 | 28.2 | 89819 |
| **gold** | Commodities | 96931 | 22.4 | 22.4 | 5357 |
| **vix** | Volatility | -49336 | 18.6 | 18.6 | -9015 |
| **dxy** | FX | -12530 | 17.3 | 17.3 | -9369 |
| **sp500** | US Equities | -457780 | 5.1 | 5.1 | -50290 |
| **nasdaq** | US Equities | -70676 | 1.3 | 1.3 | -15013 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MU** | Technology | 96.8 | 87.3% | 169.5% | 349.3% | 1002.2% | 3.63 | -30.3% |
| 2 | **SNDK** | Technology | 96.7 | 45.8% | 205.7% | 771.4% | 4806.2% | 4.01 | -31.3% |
| 3 | **WDC** | Technology | 96.5 | 34.3% | 127.5% | 263.8% | 1043.3% | 3.83 | -20.6% |
| 4 | **AMD** | Technology | 96.2 | 58.9% | 168.5% | 146.9% | 373.3% | 2.38 | -27.8% |
| 5 | **STX** | Technology | 96.1 | 27.4% | 151.3% | 249.8% | 699.7% | 3.31 | -21.0% |
| 6 | **DELL** | Technology | 96.0 | 99.0% | 187.1% | 221.2% | 295.5% | 2.15 | -32.3% |
| 7 | **HPE** | Technology | 96.0 | 92.1% | 157.6% | 154.5% | 226.1% | 2.44 | -23.7% |
| 8 | **LRCX** | Technology | 95.7 | 32.9% | 54.1% | 122.7% | 319.8% | 2.79 | -20.0% |
| 9 | **ON** | Technology | 95.1 | 31.2% | 114.2% | 165.6% | 214.8% | 2.06 | -28.1% |
| 10 | **INTC** | Technology | 94.8 | 17.7% | 147.3% | 181.7% | 471.0% | 2.42 | -24.2% |
| 11 | **CSCO** | Technology | 94.7 | 36.6% | 57.3% | 68.2% | 102.7% | 2.22 | -13.6% |
| 12 | **AMAT** | Technology | 94.4 | 28.1% | 40.1% | 97.1% | 220.8% | 2.42 | -21.4% |
| 13 | **COHR** | Technology | 94.3 | 26.5% | 51.9% | 155.3% | 443.7% | 2.31 | -26.5% |
| 14 | **CIEN** | Technology | 94.2 | 15.2% | 80.6% | 208.8% | 658.9% | 3.06 | -16.8% |
| 15 | **KLAC** | Technology | 94.0 | 24.2% | 44.2% | 84.1% | 180.5% | 2.14 | -22.4% |
| 16 | **GLW** | Technology | 93.8 | 25.7% | 38.8% | 143.0% | 305.6% | 2.54 | -23.0% |
| 17 | **TER** | Technology | 92.9 | 21.4% | 34.3% | 128.2% | 416.7% | 2.49 | -26.7% |
| 18 | **AKAM** | Technology | 92.5 | 51.6% | 55.7% | 82.8% | 110.5% | 1.34 | -25.4% |
| 19 | **NUE** | Basic Materials | 92.4 | 14.1% | 46.9% | 61.5% | 117.3% | 2.48 | -18.4% |
| 20 | **DDOG** | Technology | 92.2 | 70.7% | 111.5% | 58.5% | 112.6% | 1.14 | -48.6% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **IFX.DE** | Technology | 95.0 | 45.5% | 111.1% | 148.3% | 147.7% | 2.06 | -21.2% |
| 2 | **NOKIA.HE** | Technology | 95.0 | 28.9% | 116.0% | 183.7% | 229.5% | 2.49 | -27.6% |
| 3 | **STMMI.MI** | Technology | 95.0 | 40.5% | 153.5% | 252.9% | 210.0% | 2.20 | -33.5% |
| 4 | **TPRO.MI** | Technology | 94.8 | 75.5% | 110.4% | 175.2% | 367.5% | 2.53 | -27.0% |
| 5 | **HUBN.SW** | Industrials | 94.3 | 26.1% | 55.9% | 104.4% | 263.5% | 3.16 | -13.5% |
| 6 | **AIXA.DE** | Technology | 93.4 | 17.7% | 109.5% | 235.8% | 381.5% | 2.52 | -28.4% |
| 7 | **PRY.MI** | Industrials | 92.5 | 10.4% | 58.8% | 81.8% | 169.7% | 2.61 | -11.9% |
| 8 | **NHY.OL** | Basic Materials | 92.4 | 19.4% | 40.8% | 70.0% | 118.0% | 2.70 | -11.5% |
| 9 | **NDA.DE** | Basic Materials | 92.3 | 18.4% | 36.1% | 95.0% | 171.0% | 2.71 | -15.3% |
| 10 | **UMI.BR** | Basic Materials | 92.3 | 25.2% | 52.7% | 73.1% | 153.5% | 1.86 | -28.7% |
| 11 | **BESI.AS** | Technology | 91.7 | 13.5% | 60.0% | 123.7% | 155.5% | 1.83 | -20.9% |
| 12 | **ASML.AS** | Technology | 90.9 | 20.9% | 28.1% | 60.8% | 124.2% | 1.95 | -15.8% |
| 13 | **FR.PA** | Consumer Cyclical | 90.9 | 61.1% | 55.9% | 55.1% | 100.4% | 1.45 | -27.4% |
| 14 | **KGH.WA** | Basic Materials | 89.9 | 22.9% | 23.6% | 80.5% | 199.8% | 2.18 | -30.8% |
| 15 | **MT.AS** | Basic Materials | 89.1 | 23.9% | 21.9% | 64.5% | 133.4% | 2.08 | -26.2% |
| 16 | **IGG.L** | Financial Services | 88.9 | 19.3% | 35.9% | 59.9% | 68.5% | 2.01 | -11.5% |
| 17 | **DHER.DE** | Consumer Cyclical | 88.8 | 86.4% | 123.1% | 119.4% | 61.4% | 0.73 | -48.7% |
| 18 | **NESTE.HE** | Energy | 88.0 | -0.6% | 33.7% | 89.9% | 220.9% | 2.72 | -20.4% |
| 19 | **GL9.IR** | Consumer Defensive | 86.8 | 10.8% | 29.1% | 50.3% | 80.0% | 2.06 | -8.0% |
| 20 | **ABBN.SW** | Industrials | 86.7 | 9.1% | 20.9% | 55.7% | 81.5% | 2.15 | -12.1% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **APA** | Energy | 0.772 | 0.872 | 0.762 | 0.863 | 0.440 | +115.2% | 8.9 | +26.2% |
| 2 | **SNDK** | Information Technology | 0.754 | 1.000 | 0.848 | 0.500 | 0.500 | +4394.7% | 60.1 | +39.3% |
| 3 | **TROW** | Financials | 0.735 | 0.641 | 0.734 | 0.871 | 0.698 | +19.6% | 11.5 | +18.7% |
| 4 | **ANET** | Information Technology | 0.716 | 0.854 | 0.867 | 0.500 | 0.500 | +70.7% | 57.0 | +31.5% |
| 5 | **FTNT** | Information Technology | 0.716 | 0.913 | 0.885 | 0.500 | 0.344 | +42.6% | 58.0 | +132.4% |
| 6 | **EOG** | Energy | 0.710 | 0.718 | 0.635 | 0.809 | 0.676 | +27.9% | 13.9 | +18.2% |
| 7 | **MNST** | Consumer Staples | 0.699 | 0.774 | 0.754 | 0.500 | 0.768 | +39.6% | 42.8 | +26.7% |
| 8 | **NEM** | Materials | 0.698 | 0.631 | 0.861 | 0.703 | 0.495 | +109.1% | 14.1 | +25.8% |
| 9 | **HST** | Real Estate | 0.694 | 0.877 | 0.533 | 0.709 | 0.622 | +63.8% | 16.6 | +14.9% |
| 10 | **PFG** | Financials | 0.693 | 0.773 | 0.500 | 0.792 | 0.754 | +40.8% | 14.9 | +13.4% |
| 11 | **CF** | Materials | 0.691 | 0.695 | 0.716 | 0.769 | 0.502 | +30.3% | 10.6 | +27.3% |
| 12 | **SPG** | Real Estate | 0.685 | 0.684 | 0.890 | 0.543 | 0.512 | +33.6% | 14.4 | +113.6% |
| 13 | **FFIV** | Information Technology | 0.683 | 0.879 | 0.661 | 0.500 | 0.637 | +38.3% | 33.6 | +20.3% |
| 14 | **IBKR** | Financials | 0.682 | 0.871 | 0.832 | 0.500 | 0.305 | +65.1% | 37.4 | +23.6% |
| 15 | **GL** | Financials | 0.672 | 0.697 | 0.500 | 0.749 | 0.839 | +27.9% | 10.7 | +20.5% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **NRG** | Utilities | 0.145 | 0.170 | 0.117 | 0.141 | 0.155 |
| 502 | **BLDR** | Industrials | 0.223 | 0.072 | 0.174 | 0.500 | 0.162 |
| 501 | **CSGP** | Real Estate | 0.227 | 0.015 | 0.106 | 0.500 | 0.439 |
| 500 | **GPC** | Consumer Discretionary | 0.240 | 0.138 | 0.112 | 0.492 | 0.282 |
| 499 | **AXON** | Industrials | 0.254 | 0.180 | 0.131 | 0.500 | 0.235 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W23.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W23.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-06-01  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
