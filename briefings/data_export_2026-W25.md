# Сателит — пълен data export за 2026-W25

_Период: 2026-06-15 → 2026-06-21_  
_Генериран: 2026-06-19 10:28 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W25.md` (structured briefing) и `narrative_2026-W25.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**10 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **XLP** | -2.94% | -1.91σ | 85.82 | 83.30 | 2026-06-12 | 2026-06-18 | +0.15% | +1.62% | 13 |
| **XLV** | -2.87% | -1.66σ | 153.81 | 149.40 | 2026-06-12 | 2026-06-18 | +0.25% | +1.88% | 13 |
| **XLRE** | -3.31% | -1.62σ | 45.36 | 43.86 | 2026-06-12 | 2026-06-18 | +0.63% | +2.43% | 13 |
| **XLE** | -6.57% | -1.58σ | 57.55 | 53.77 | 2026-06-12 | 2026-06-18 | +0.12% | +4.23% | 13 |
| **UUP** | +1.25% | +1.57σ | 27.95 | 28.30 | 2026-06-12 | 2026-06-18 | +0.02% | +0.78% | 13 |
| **VNQ** | -2.99% | -1.51σ | 98.51 | 95.56 | 2026-06-12 | 2026-06-18 | +0.62% | +2.39% | 13 |
| **XLI** | +2.68% | +1.27σ | 176.18 | 180.91 | 2026-06-12 | 2026-06-18 | +0.56% | +1.68% | 13 |
| **DBC** | -3.22% | -1.26σ | 28.55 | 27.63 | 2026-06-12 | 2026-06-18 | -0.01% | +2.56% | 13 |
| **DBA** | +1.49% | +1.17σ | 26.24 | 26.63 | 2026-06-12 | 2026-06-18 | -0.14% | +1.39% | 13 |
| **USO** | -8.42% | -1.14σ | 125.43 | 114.87 | 2026-06-12 | 2026-06-18 | +0.66% | +7.95% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_5 канонични patterns от `config/divergence_rules.yaml`, evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-06-21 · **Conditions matched:** 1/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | -8.42% | ❌ | 125.43 | 114.87 | 2026-06-12 | 2026-06-18 |
| DFEN | down ≥ 3.0% | +6.94% | ❌ | 72.22 | 77.23 | 2026-06-12 | 2026-06-18 |
| GLD | down ≥ 1.0% | +0.15% | ❌ | 386.54 | 387.12 | 2026-06-12 | 2026-06-18 |
| URA | down ≥ 3.0% | +4.96% | ❌ | 45.52 | 47.78 | 2026-06-12 | 2026-06-18 |
| UUP | up ≥ 0.5% | +1.25% | ✅ | 27.95 | 28.30 | 2026-06-12 | 2026-06-18 |

### Ликвидна стес (flight to quality) (`liquidity_stress`) — не активен
_Дългосрочни trezuri нагоре, високодоходен кредит надолу, злато нагоре. Класически risk-off._  
**Window:** 7d ending 2026-06-21 · **Conditions matched:** 2/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| TLT | up ≥ 1.0% | +1.14% | ✅ | 85.77 | 86.75 | 2026-06-12 | 2026-06-18 |
| HYG | down ≥ 0.5% | +0.09% | ❌ | 79.94 | 80.01 | 2026-06-12 | 2026-06-18 |
| GLD | up ≥ 1.0% | +0.15% | ❌ | 386.54 | 387.12 | 2026-06-12 | 2026-06-18 |
| UUP | up ≥ 0.3% | +1.25% | ✅ | 27.95 | 28.30 | 2026-06-12 | 2026-06-18 |

### Възстановяване на инфлационни очаквания (`inflation_pickup`) — не активен
_Inflation-protected треzuri нагоре, commodities нагоре, dollar надолу. Repricing на real rates._  
**Window:** 7d ending 2026-06-21 · **Conditions matched:** 0/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| DBC | up ≥ 1.5% | -3.22% | ❌ | 28.55 | 27.63 | 2026-06-12 | 2026-06-18 |
| GLD | up ≥ 1.0% | +0.15% | ❌ | 386.54 | 387.12 | 2026-06-12 | 2026-06-18 |
| UUP | down ≥ 0.5% | +1.25% | ❌ | 27.95 | 28.30 | 2026-06-12 | 2026-06-18 |
| TLT | down ≥ 1.0% | +1.14% | ❌ | 85.77 | 86.75 | 2026-06-12 | 2026-06-18 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-06-21 · **Conditions matched:** 0/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | +0.90% | ❌ | 292.95 | 295.59 | 2026-06-12 | 2026-06-18 |
| XLF | up ≥ 1.0% | +0.43% | ❌ | 53.34 | 53.57 | 2026-06-12 | 2026-06-18 |
| XLY | up ≥ 1.0% | +0.48% | ❌ | 116.60 | 117.16 | 2026-06-12 | 2026-06-18 |
| GLD | down ≥ 0.5% | +0.15% | ❌ | 386.54 | 387.12 | 2026-06-12 | 2026-06-18 |

### Защитен pivot (staples + utilities + gold) (`defensive_pivot`) — не активен
_XLP + XLU + GLD едновременно нагоре. Smart money flight to defensives без credit panic._  
**Window:** 7d ending 2026-06-21 · **Conditions matched:** 0/3

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| XLP | up ≥ 1.0% | -2.94% | ❌ | 85.82 | 83.30 | 2026-06-12 | 2026-06-18 |
| XLU | up ≥ 1.0% | +0.52% | ❌ | 44.53 | 44.76 | 2026-06-12 | 2026-06-18 |
| GLD | up ≥ 1.0% | +0.15% | ❌ | 386.54 | 387.12 | 2026-06-12 | 2026-06-18 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2022-W31 (week ending 2022-08-07)
**Cosine similarity:** 0.9695 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -5.49% | -8.60% | +0.60% |
| **USO** | -0.17% | +7.38% | -9.98% |
| **GLD** | -4.21% | -5.34% | +4.94% |
| **TLT** | -7.52% | -18.54% | -7.07% |
| **XLE** | +8.40% | +26.46% | +20.13% |
| **IWM** | -6.55% | -5.87% | +4.26% |

### Паралел #2: 2023-W05 (week ending 2023-02-05)
**Cosine similarity:** 0.9064 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -3.41% | +0.45% | +9.17% |
| **USO** | +5.36% | -2.13% | +14.58% |
| **GLD** | -2.79% | +8.07% | +3.88% |
| **TLT** | -4.43% | -0.95% | -8.11% |
| **XLE** | -0.21% | -5.69% | +3.07% |
| **IWM** | -5.32% | -11.12% | -0.79% |

### Паралел #3: 2025-W40 (week ending 2025-10-05)
**Cosine similarity:** 0.8939 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.90% | +2.39% | -1.44% |
| **USO** | +0.31% | -3.83% | +92.33% |
| **GLD** | +1.31% | +11.36% | +20.07% |
| **TLT** | +0.99% | -1.55% | -0.72% |
| **XLE** | -1.93% | +3.56% | +35.30% |
| **IWM** | -1.88% | +1.54% | +2.75% |

### Паралел #4: 2024-W18 (week ending 2024-05-05)
**Cosine similarity:** 0.8894 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.34% | +4.56% | +12.39% |
| **USO** | -5.38% | -2.32% | -4.14% |
| **GLD** | +1.08% | +5.81% | +18.55% |
| **TLT** | +3.50% | +10.48% | +3.13% |
| **XLE** | -2.90% | -3.74% | -3.35% |
| **IWM** | +0.03% | +3.77% | +9.13% |

### Паралел #5: 2023-W52 (week ending 2023-12-31)
**Cosine similarity:** 0.8881 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.28% | +10.39% | +15.22% |
| **USO** | +9.24% | +18.12% | +19.41% |
| **GLD** | -1.35% | +7.61% | +12.47% |
| **TLT** | -3.20% | -3.70% | -5.63% |
| **XLE** | +1.38% | +13.52% | +10.48% |
| **IWM** | -1.49% | +5.04% | +1.63% |

### Паралел #6: 2021-W33 (week ending 2021-08-22)
**Cosine similarity:** 0.8847 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.88% | +6.10% | -1.40% |
| **USO** | +14.16% | +23.83% | +49.07% |
| **GLD** | -0.40% | +3.55% | +6.25% |
| **TLT** | +0.35% | -1.08% | -7.49% |
| **XLE** | +4.44% | +20.58% | +52.03% |
| **IWM** | +0.93% | +8.31% | -6.88% |

### Паралел #7: 2025-W29 (week ending 2025-07-20)
**Cosine similarity:** 0.8693 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.95% | +6.16% | +10.84% |
| **USO** | -4.78% | -10.47% | -5.64% |
| **GLD** | -1.01% | +26.14% | +36.61% |
| **TLT** | +2.04% | +8.18% | +5.31% |
| **XLE** | -1.02% | +0.88% | +12.86% |
| **IWM** | +1.75% | +9.79% | +20.28% |

### Паралел #8: 2025-W26 (week ending 2025-06-29)
**Cosine similarity:** 0.8507 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.31% | +7.93% | +12.91% |
| **USO** | +8.90% | +5.10% | -6.55% |
| **GLD** | +1.67% | +15.11% | +38.35% |
| **TLT** | +0.29% | +2.89% | +3.03% |
| **XLE** | +4.28% | +8.76% | +5.41% |
| **IWM** | +3.35% | +12.32% | +17.40% |

### Паралел #9: 2023-W18 (week ending 2023-05-07)
**Cosine similarity:** 0.8452 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.73% | +8.69% | +6.11% |
| **USO** | +1.21% | +17.07% | +18.75% |
| **GLD** | -2.73% | -3.88% | -1.42% |
| **TLT** | -2.11% | -7.22% | -14.96% |
| **XLE** | -0.27% | +9.29% | +9.80% |
| **IWM** | +5.65% | +11.61% | +0.77% |

### Паралел #10: 2023-W16 (week ending 2023-04-23)
**Cosine similarity:** 0.8409 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.46% | +10.11% | +2.92% |
| **USO** | -4.90% | +1.14% | +18.31% |
| **GLD** | -0.45% | -1.12% | -0.36% |
| **TLT** | -2.98% | -1.79% | -18.92% |
| **XLE** | -5.67% | +0.07% | +7.94% |
| **IWM** | -0.08% | +9.82% | -5.56% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 13 · **Total matching days:** 72 · **History:** 2021-05-17 → 2026-06-18

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 13 | +2.0% | +1.7% | -3.1% | +7.7% | 77% |
| **SPY** | 3m | 13 | +3.4% | +4.6% | -7.0% | +13.8% | 77% |
| **SPY** | 6m | 13 | +8.3% | +11.6% | -6.1% | +22.7% | 77% |
| **USO** | 1m | 13 | +1.0% | -0.8% | -7.2% | +12.7% | 46% |
| **USO** | 3m | 13 | -2.4% | -4.1% | -18.9% | +24.5% | 46% |
| **USO** | 6m | 13 | +10.5% | -4.4% | -17.7% | +109.4% | 46% |
| **GLD** | 1m | 13 | +2.5% | +0.9% | -2.2% | +8.9% | 77% |
| **GLD** | 3m | 13 | +6.0% | +5.9% | -10.6% | +24.5% | 69% |
| **GLD** | 6m | 13 | +6.4% | +10.3% | -13.0% | +25.3% | 69% |
| **TLT** | 1m | 13 | -1.1% | -0.8% | -6.5% | +3.7% | 31% |
| **TLT** | 3m | 13 | +0.6% | +0.6% | -16.2% | +12.6% | 62% |
| **TLT** | 6m | 13 | -2.2% | +0.4% | -17.2% | +9.1% | 54% |

**Episodes (последни 5 от 13):**
- `2024-06-21 → 2024-06-21` (1d)
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-28 → 2026-05-19` (13d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 1 · **Total matching days:** 49 · **History:** 2021-05-17 → 2026-06-18

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | +9.1% | +9.1% | +9.1% | +9.1% | 100% |
| **SPY** | 3m | 1 | +10.5% | +10.5% | +10.5% | +10.5% | 100% |
| **SPY** | 6m | 1 | +10.5% | +10.5% | +10.5% | +10.5% | 100% |
| **USO** | 1m | 1 | +7.2% | +7.2% | +7.2% | +7.2% | 100% |
| **USO** | 3m | 1 | -7.8% | -7.8% | -7.8% | -7.8% | 0% |
| **USO** | 6m | 1 | -7.8% | -7.8% | -7.8% | -7.8% | 0% |
| **GLD** | 1m | 1 | -0.2% | -0.2% | -0.2% | -0.2% | 0% |
| **GLD** | 3m | 1 | -10.9% | -10.9% | -10.9% | -10.9% | 0% |
| **GLD** | 6m | 1 | -10.9% | -10.9% | -10.9% | -10.9% | 0% |
| **TLT** | 1m | 1 | -0.6% | -0.6% | -0.6% | -0.6% | 0% |
| **TLT** | 3m | 1 | +0.2% | +0.2% | +0.2% | +0.2% | 100% |
| **TLT** | 6m | 1 | +0.2% | +0.2% | +0.2% | +0.2% | 100% |

**Episodes (последни 5 от 1):**
- `2026-04-08 → 2026-06-15` (49d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 7 · **Total matching days:** 766 · **History:** 2021-05-17 → 2026-06-18

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
- `2024-10-04 → 2026-06-18` (428d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-06-18

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 9 · **Total matching days:** 76 · **History:** 2021-05-17 → 2026-06-18

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 9 | +0.4% | +0.9% | -7.2% | +7.8% | 56% |
| **SPY** | 3m | 9 | +2.6% | +4.9% | -8.0% | +12.0% | 56% |
| **SPY** | 6m | 9 | +1.8% | +4.9% | -20.2% | +14.9% | 67% |
| **USO** | 1m | 9 | +2.0% | -1.7% | -15.0% | +52.9% | 33% |
| **USO** | 3m | 9 | +5.8% | -0.1% | -23.7% | +52.2% | 44% |
| **USO** | 6m | 9 | +4.8% | -0.2% | -27.6% | +45.8% | 44% |
| **GLD** | 1m | 9 | -2.2% | -1.6% | -8.3% | +1.9% | 11% |
| **GLD** | 3m | 9 | -2.1% | -2.8% | -12.0% | +6.4% | 44% |
| **GLD** | 6m | 9 | -1.4% | -4.7% | -17.3% | +25.0% | 33% |
| **TLT** | 1m | 9 | -1.7% | -2.2% | -5.7% | +2.6% | 22% |
| **TLT** | 3m | 9 | -5.5% | -4.9% | -16.9% | +5.4% | 33% |
| **TLT** | 6m | 9 | -8.2% | -6.1% | -21.7% | +3.4% | 22% |

**Episodes (последни 5 от 9):**
- `2023-04-12 → 2023-04-18` (5d)
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-04-09` (27d)
- `2026-04-29 → 2026-05-19` (7d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 16 · **Total matching days:** 275 · **History:** 2021-05-17 → 2026-06-18

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.2% | +2.2% | -4.8% | +9.0% | 75% |
| **SPY** | 3m | 16 | +3.7% | +4.8% | -12.3% | +16.7% | 75% |
| **SPY** | 6m | 16 | +7.4% | +8.3% | -13.5% | +21.9% | 81% |
| **USO** | 1m | 16 | +1.8% | -3.2% | -13.0% | +27.7% | 38% |
| **USO** | 3m | 16 | +1.7% | -1.8% | -14.5% | +29.9% | 31% |
| **USO** | 6m | 16 | +11.4% | +1.8% | -12.4% | +87.1% | 62% |
| **GLD** | 1m | 16 | +2.4% | +1.8% | -6.4% | +9.0% | 75% |
| **GLD** | 3m | 16 | +6.5% | +7.4% | -13.2% | +23.6% | 69% |
| **GLD** | 6m | 16 | +11.1% | +12.1% | -13.2% | +43.8% | 75% |
| **TLT** | 1m | 16 | +0.6% | +0.7% | -6.1% | +8.5% | 56% |
| **TLT** | 3m | 16 | -0.5% | -0.2% | -14.7% | +13.0% | 50% |
| **TLT** | 6m | 16 | -2.7% | -0.3% | -20.6% | +8.6% | 44% |

**Episodes (последни 5 от 16):**
- `2025-03-27 → 2025-05-08` (25d)
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-17 → 2026-04-23` (4d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 19 · **Total matching days:** 293 · **History:** 2021-05-17 → 2026-06-18

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 19 | +0.5% | +1.2% | -8.3% | +7.0% | 53% |
| **SPY** | 3m | 19 | +2.3% | +3.1% | -13.3% | +9.4% | 68% |
| **SPY** | 6m | 19 | +3.7% | +7.4% | -15.7% | +17.6% | 74% |
| **USO** | 1m | 19 | -0.2% | -5.6% | -14.3% | +55.8% | 42% |
| **USO** | 3m | 19 | +2.8% | -1.3% | -13.6% | +64.3% | 42% |
| **USO** | 6m | 19 | +6.9% | -5.2% | -16.0% | +75.1% | 47% |
| **GLD** | 1m | 19 | -0.4% | -0.1% | -12.4% | +7.6% | 47% |
| **GLD** | 3m | 19 | +1.6% | +1.3% | -13.7% | +19.0% | 63% |
| **GLD** | 6m | 19 | +7.5% | +6.0% | -18.2% | +55.5% | 68% |
| **TLT** | 1m | 19 | +0.2% | +0.3% | -5.5% | +5.5% | 58% |
| **TLT** | 3m | 19 | -2.6% | -3.8% | -16.8% | +9.8% | 42% |
| **TLT** | 6m | 19 | -4.9% | -2.4% | -20.5% | +6.7% | 32% |

**Episodes (последни 5 от 19):**
- `2025-05-12 → 2025-05-19` (3d)
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-06-18` (4d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-06-18

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (19 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 9 | 2.53 | 2.89 | 2026-05-16 00:00:00 | 2026-06-13 00:00:00 | ✓ |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 9 | 2.33 | 2.34 | 2026-05-16 00:00:00 | 2026-06-13 00:00:00 | ✓ |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 6 | 2.76 | 2.76 | 2026-06-04 00:00:00 | 2026-06-13 00:00:00 | ✓ |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | 6 | 2.40 | 2.40 | 2026-06-04 00:00:00 | 2026-06-13 00:00:00 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 6 | 2.29 | 2.29 | 2026-06-04 00:00:00 | 2026-06-13 00:00:00 | - |
| **CSUSHPISA** | Case-Shiller US National HPI (SA) | housing | housing_prices | 6 | 2.26 | 2.26 | 2026-06-04 00:00:00 | 2026-06-13 00:00:00 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | 6 | 2.18 | 2.58 | 2026-06-04 00:00:00 | 2026-06-13 00:00:00 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | 6 | 2.02 | 2.02 | 2026-06-04 00:00:00 | 2026-06-13 00:00:00 | ✓ |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | 5 | 2.30 | 2.30 | 2026-06-04 00:00:00 | 2026-06-08 00:00:00 | - |
| **M2** | M2 паричен агрегат | liquidity | money_supply | 4 | 2.76 | 2.76 | 2026-05-16 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **DGORDER** | Нови поръчки за дълготрайни стоки | growth | hard_activity | 4 | 2.63 | 2.90 | 2026-05-16 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **C_AND_I_LOANS** | Търговски и индустриални кредити (C&I) | liquidity | banking_credit | 4 | 2.57 | 2.57 | 2026-05-16 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **UMCSENT** | Michigan Sentiment Index | growth | consumer_sentiment | 4 | 2.51 | 2.57 | 2026-05-16 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CPI_SHELTER** | CPI — жилища (shelter) | inflation | goods_services | 4 | 2.46 | 2.46 | 2026-05-16 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CPI_SERVICES** | CPI — услуги (всички) | inflation | goods_services | 4 | 2.35 | 2.35 | 2026-05-16 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 4 | 2.31 | 2.39 | 2026-06-06 00:00:00 | 2026-06-13 00:00:00 | ✓ |
| **RSXFS** | Продажби на дребно (без храна) | growth | hard_activity | 3 | 2.33 | 2.33 | 2026-05-16 00:00:00 | 2026-05-30 00:00:00 | ✓ |
| **PPICORE** | PPI Core (Final Demand без храни и енергия) | inflation | core_measures | 3 | 2.32 | 2.32 | 2026-05-16 00:00:00 | 2026-05-30 00:00:00 | ✓ |
| **USSTHPI** | FHFA House Price Index (Q, NSA) | housing | housing_prices | 1 | 2.70 | 2.70 | 2026-06-04 00:00:00 | 2026-06-04 00:00:00 | ✓ |

### EU (13 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.37 | 5.37 | 2026-06-05 00:00:00 | 2026-06-13 00:00:00 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation | sentiment | 5 | 2.98 | 2.98 | 2026-06-05 00:00:00 | 2026-06-13 00:00:00 | - |
| **EA_RETAIL_CONF** | Доверие в търговията на дребно (DG ECFIN) | growth | sentiment | 5 | 2.45 | 2.68 | 2026-05-16 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **EA_COMP_PER_EMPLOYEE** | Компенсация на наетите (D1, EA-20, M€) | labor | wages | 5 | 2.39 | 2.39 | 2026-05-16 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | 5 | 2.32 | 2.32 | 2026-06-05 00:00:00 | 2026-06-13 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.29 | 2.31 | 2026-06-05 00:00:00 | 2026-06-13 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.24 | 2.27 | 2026-06-05 00:00:00 | 2026-06-13 00:00:00 | ✓ |
| **EA_PPI_INTERMEDIATE** | PPI междинни стоки (MIG ING, индекс 2021=100) | inflation | producer_prices | 5 | 2.04 | 2.16 | 2026-05-16 00:00:00 | 2026-06-04 00:00:00 | - |
| **EA_RETAIL_VOL** | Търговия на дребно — обем на продажбите (G47, индекс 2021=100) | growth | hard_activity | 5 | 2.02 | 2.06 | 2026-05-16 00:00:00 | 2026-06-04 00:00:00 | - |
| **EA_EMPLOYMENT_EXP** | Очаквания за заетост (3m напред) | labor | labor_sentiment | 2 | 3.14 | 3.14 | 2026-05-16 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **EA_WAGES_SALARIES** | Работни заплати (D11, EA-20, M€) | labor | wages | 2 | 2.38 | 2.38 | 2026-06-03 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **EA_ESI** | Икономически Sentiment Indicator (DG ECFIN ESI) | growth | sentiment | 2 | 2.25 | 2.25 | 2026-05-16 00:00:00 | 2026-05-23 00:00:00 | ✓ |
| **EA_CONSUMER_CONF** | Потребителско доверие (DG ECFIN, full history от 1985) | growth | sentiment | 2 | 2.10 | 2.10 | 2026-05-16 00:00:00 | 2026-05-23 00:00:00 | - |

### CN (7 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 5 | 2.56 | 2.56 | 2026-06-02 00:00:00 | 2026-06-15 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 5 | 2.24 | 2.24 | 2026-06-02 00:00:00 | 2026-06-15 00:00:00 | - |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 5 | 2.23 | 2.23 | 2026-06-02 00:00:00 | 2026-06-15 00:00:00 | ✓ |
| **CN_POLICY_RATE** | Политическа лихва — PBoC 7-day repo (%) | credit | rates | 2 | 2.39 | 2.39 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CN_FDI_GDP** | ПЧИ — входящи (% от БВП) | property | investment | 2 | 2.11 | 2.11 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CN_BIS_PROPERTY_YOY** | Жилищни имотни цени (YoY %, BIS номинал) | property | housing | 2 | 2.10 | 2.10 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | - |
| **CN_CREDIT_PRIVATE** | Кредит към частния сектор (% от БВП) | credit | credit_depth | 2 | 2.07 | 2.07 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-06-13 00:00:00 · **Generated:** 2026-06-13 09:58:10.179883+00:00

**Режим:** `stagflation_confirmed` (Стагфлация (потвърдена))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 35.1 | contracting | 25.9% | 2 | 2 |
| **growth** | 43.6 | mixed | 40.0% | 2 | 1 |
| **inflation** | 36.4 | contracting | 22.2% | 4 | 1 |
| **liquidity** | 52.1 | mixed | 42.1% | 0 | 0 |

### Top anomalies (9 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | +2.89 | up | 6.42 | 2026-05-01 | - |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | -2.76 | down | 1.71 | 2026-03-01 | ✓ min |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | +2.58 | up | 5.29 | 2026-05-01 | - |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | -2.40 | down | 2.60 | 2026-04-01 | - |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.34 | down | 94.99 | 2026-01-01 | ✓ min |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | +2.29 | up | 4.70 | 2026-04-01 | - |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | +2.28 | up | 55.10 | 2026-05-01 | ✓ max |
| **CSUSHPISA** | Case-Shiller US National HPI (SA) | housing | housing_prices | -2.26 | down | 0.66 | 2026-03-01 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | -2.02 | down | 1.90 | 2026-04-01 | ✓ min |

### Narrative hints от макро лещите
- **PPIFIS**: Производствени цени → consumer prices с 1-3 месечен lag. Водещ за CPI при трендови промени.
- **HPIPONM226S**: Monthly FHFA версия. Само purchase transactions (без refi appraisals). По-чист от refi-bias.
- **CPI_GOODS**: Goods inflation реагира бързо на supply shocks. 2022 peak след доставъчните кризи. Сега често е в deflation/близо до 0.
- **PSAVERT**: Hard data компонент. Скочи >30% в COVID — когато survey и hard data разминават, сигналът укрепва.
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **MICH_INFL_1Y**: Household очаквания. По-шумни от market-based, но по-ранни. Extreme movements сигнализират de-anchoring risk.
- **US_PMI_MFG**: Markit mfg — comparable cross-country. ISM е US-only.
- **CSUSHPISA**: Главен ценови benchmark. Repeat-sales методология; ~2 месеца lag. National композит на 9 census divisions.
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
  - `state`: a_down_b_up
  - `interpretation`: Benign credit despite tightening — liquidity cushion intact.
  - `slot_a_label`: Credit stress
  - `slot_b_label`: Policy tightening
  - `breadth_a`: 0.0
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
  - `state`: a_down_b_up
  - `interpretation`: Модел cools, пазар pricing-ва inflation — market overestimating; dovish contrarian setup.
  - `slot_a_label`: Модел (sticky inflation)
  - `slot_b_label`: Пазар (breakevens + survey)
  - `breadth_a`: 0.333
  - `breadth_b`: 1.0

### Executive narrative
> Картината показва потвърдена стагфлационна конфигурация — трудовият пазар остава tight, а инфлационният натиск е broad-based. Най-отклонена леща: Инфлация и цени — breadth 76% (разширяване), 4 аномалии, 1 нови екстремума. Expectations също нагоре — de-anchoring в ход, рискът ескалира. За наблюдение следващия релиз: HPIPONM226S, LABOR_SHARE_NBS (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: PPIFIS z=+2.89
- 4 нови екстремуми в top-9 (lookback 5г.)
- Активни двойки: Stagflation test=both_up; Growth × Labor=a_up_b_down; Inflation anchoring=both_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-06-13 00:00:00 · **Generated:** 2026-06-13 10:13:35.179455+00:00

**Режим:** `soft_landing` (Soft landing)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 36.5 | contracting | 42.9% | 1 | 0 |
| **growth** | 44.6 | mixed | 15.4% | 1 | 0 |
| **inflation** | 46.1 | mixed | 71.4% | 1 | 0 |
| **credit** | 42.7 | mixed | 36.8% | 3 | 2 |

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
> Конфигурацията подкрепя soft landing — labor остава tight, но инфлацията се охлажда. Fed credibility за момента издържа. Най-отклонена леща: Инфлация и цени — breadth 17% (свиване), 1 аномалии, 0 нови екстремума. За наблюдение следващия релиз: DE_10Y, FR_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.37
- 2 нови екстремуми в top-5 (lookback 5г.)
- Активни двойки: Stagflation test=a_up_b_down; ecb_transmission=a_up_b_down; fragmentation_risk=a_up_b_down



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-06-15 00:00:00 · **Generated:** 2026-06-15 11:41:21.641472+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 30.6 | contracting | -% | - | - |
| **inflation** | 50.6 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 42.4 | mixed | -% | - | - |
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
> Претеглен композитен macro score 35.3/100 → режим „ВЛОШАВАЩ СЕ“. 5 лещи, 3 flagged аномалии (4 застояли изключени), 3 cross-lens двойки.



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

### US (period: 2026-06-12 → 2026-06-17)

**stable_winner (1m):** +3 entered, -5 exited
  - **Entered:** ALB, HST, WELL
  - **Exited:** BG, GM, GS, NTRS, WYNN

**stable_winner (3m):** +3 entered, -4 exited
  - **Entered:** HST, JNJ, WMT
  - **Exited:** KEY, SPG, WELL, WYNN

**quality_dip (1m):** +6 entered, -3 exited
  - **Entered:** BG, GM, GS, HSY, NEE, NTRS _(включително 2 за първи път в историята: HSY, NEE)_
  - **Exited:** ALB, HST, WELL

**quality_dip (3m):** +5 entered, -3 exited
  - **Entered:** HSY, KEY, NEE, SPG, WELL _(включително 3 за първи път в историята: HSY, KEY, NEE)_
  - **Exited:** HST, JNJ, WMT

**faded_bounce (1m):** +9 entered, -7 exited
  - **Entered:** AJG, ARE, BR, BRO, CTAS, MRSH, POOL, STZ, TAP
  - **Exited:** BBY, BLDR, CAG, IT, KMB, SW, TTD

**faded_bounce (3m):** +5 entered, -2 exited
  - **Entered:** BRO, BX, PEG, POOL, TAP
  - **Exited:** NKE, TPL

### EU (period: 2026-06-12 → 2026-06-17)

**stable_winner (1m):** +8 entered, -12 exited
  - **Entered:** A5G.IR, ALLN.SW, BARN.SW, NDX1.DE, NESTE.HE, RWE.DE, TPRO.MI, VOD.L _(включително 2 за първи път в историята: BARN.SW, VOD.L)_
  - **Exited:** AAF.L, AIXA.DE, BBY.L, CCH.L, ELI.BR, FR.PA, HOT.DE, IG.MI, KGF.L, KGX.DE, LPP.WA, UCG.MI

**stable_winner (3m):** +7 entered, -5 exited
  - **Entered:** HOC.L, ISS.CO, NESTE.HE, SAND.ST, SPSN.SW, VOD.L, ZEG.L _(включително 2 за първи път в историята: HOC.L, VOD.L)_
  - **Exited:** AAF.L, BKT.MC, ELI.BR, KER.PA, PKN.WA

**quality_dip (1m):** +10 entered, -8 exited
  - **Entered:** AAF.L, AIXA.DE, BBY.L, CCH.L, ELI.BR, FR.PA, HOT.DE, IG.MI, KGF.L, LPP.WA _(включително 1 за първи път в историята: ELI.BR)_
  - **Exited:** A5G.IR, ALLN.SW, BARN.SW, LLOY.L, NDX1.DE, NESTE.HE, RWE.DE, TPRO.MI

**quality_dip (3m):** +5 entered, -9 exited
  - **Entered:** AAF.L, BKT.MC, ELI.BR, KER.PA, PKN.WA
  - **Exited:** HOC.L, ISS.CO, KGX.DE, LLOY.L, NESTE.HE, SAND.ST, SPSN.SW, UCG.MI, ZEG.L

**faded_bounce (1m):** +14 entered, -8 exited
  - **Entered:** ADM.L, ADYEN.AS, BAKKA.OL, BEI.DE, BEIJ-B.ST, INDT.ST, KNIN.SW, RACE.MI, RMS.PA, SAGA-B.ST, SY1.DE, VER.VI, VZN.SW, WPP.L _(включително 2 за първи път в историята: ADYEN.AS, RMS.PA)_
  - **Exited:** AKE.PA, BPT.L, CVC.AS, DSFIR.AS, ENX.PA, MF.PA, SGE.L, STLAM.MI

**faded_bounce (3m):** +6 entered, -9 exited
  - **Entered:** BALD-B.ST, BOL.PA, SREN.SW, TOM.OL, WALL-B.ST, WPP.L
  - **Exited:** AKE.PA, AUTO.L, ENX.PA, MF.PA, PGHN.SW, SGE.L, SIGN.SW, VER.VI, WISE.L



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-06-09 00:00:00)
| Market | Asset class | Net position | Net % | Percentile 5y | Weekly change |
|---|---|---:|---:|---:|---:|
| **soyoil** | Commodities | 131436 | 98.1 | 98.1 | -30851 |
| **aud** | FX | 42292 | 90.5 | 90.5 | -13559 |
| **copper** | Commodities | 71127 | 86.9 | 86.9 | -2396 |
| **cattle** | Commodities | 109002 | 79.1 | 79.1 | -21884 |
| **rbob** | Commodities | 64334 | 75.8 | 75.8 | 591 |
| **us30y** | Rates | -281933 | 74.0 | 74.0 | 14263 |
| **vix** | Volatility | -35290 | 73.6 | 73.6 | 12289 |
| **gbpfx** | FX | 22312 | 65.6 | 65.6 | -14990 |
| **brent** | Commodities | 9302 | 63.4 | 63.4 | -9092 |
| **soybeans** | Commodities | 90756 | 63.1 | 63.1 | -124059 |
| **soymeal** | Commodities | 52602 | 59.9 | 59.9 | -63480 |
| **cotton** | Commodities | 42204 | 55.9 | 55.9 | -17366 |
| **corn** | Commodities | -5325 | 52.5 | 52.5 | -304808 |
| **platinum** | Commodities | 8377 | 51.9 | 51.9 | -7755 |
| **us2y** | Rates | -1680942 | 50.2 | 50.2 | 266887 |
| **us5y** | Rates | -2230356 | 49.3 | 49.3 | 118849 |
| **eurfx** | FX | -17388 | 44.9 | 44.9 | -35391 |
| **gold** | Commodities | 103660 | 40.1 | 40.1 | 3033 |
| **bitcoin** | Crypto | -5995 | 37.0 | 37.0 | 5075 |
| **usultra10y** | Rates | -260130 | 36.6 | 36.6 | -9675 |
| **coffee** | Commodities | 3132 | 35.9 | 35.9 | -21896 |
| **heatingoil** | Commodities | 9605 | 31.9 | 31.9 | -1 |
| **wheat** | Commodities | -79407 | 28.7 | 28.7 | -60384 |
| **wti** | Commodities | -19790 | 28.1 | 28.1 | 14461 |
| **silver** | Commodities | 9794 | 25.7 | 25.7 | -6401 |
| **natgas** | Commodities | -7128 | 24.7 | 24.7 | 388 |
| **palladium** | Commodities | -4520 | 24.5 | 24.5 | -2596 |
| **chf** | FX | -10785 | 21.1 | 21.1 | -3077 |
| **us10y** | Rates | -1979511 | 20.7 | 20.7 | -22569 |
| **sugar** | Commodities | -130333 | 13.3 | 13.3 | -29877 |
| **russell** | US Equities | -74454 | 12.8 | 12.8 | -13823 |
| **dxy** | FX | -13656 | 11.9 | 11.9 | -8905 |
| **cad** | FX | -58623 | 10.3 | 10.3 | -20960 |
| **cocoa** | Commodities | -27286 | 9.9 | 9.9 | -13317 |
| **sp500** | US Equities | -451586 | 6.5 | 6.5 | -19148 |
| **nasdaq** | US Equities | -56754 | 4.0 | 4.0 | 16983 |
| **hogs** | Commodities | -13701 | 3.0 | 3.0 | -54561 |
| **jpy** | FX | -99844 | 1.7 | 1.7 | -37404 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **WDC** | Technology | 96.8 | 55.3% | 133.6% | 314.2% | 1143.8% | 3.73 | -20.6% |
| 2 | **SNDK** | Technology | 96.7 | 47.0% | 159.9% | 870.3% | 4330.7% | 3.83 | -31.3% |
| 3 | **STX** | Technology | 96.6 | 43.9% | 162.5% | 274.9% | 724.0% | 3.25 | -21.0% |
| 4 | **MU** | Technology | 96.5 | 53.1% | 126.0% | 339.6% | 772.6% | 3.04 | -30.3% |
| 5 | **AMAT** | Technology | 96.0 | 43.5% | 69.9% | 127.5% | 238.3% | 2.38 | -21.4% |
| 6 | **DELL** | Technology | 95.9 | 76.2% | 181.9% | 223.7% | 274.3% | 2.04 | -32.3% |
| 7 | **LRCX** | Technology | 95.9 | 34.7% | 66.6% | 128.2% | 303.8% | 2.55 | -20.0% |
| 8 | **HPE** | Technology | 95.2 | 46.5% | 126.0% | 103.5% | 171.7% | 1.98 | -23.7% |
| 9 | **KLAC** | Technology | 95.0 | 35.9% | 61.2% | 95.4% | 169.2% | 1.89 | -22.4% |
| 10 | **AMD** | Technology | 94.9 | 21.7% | 156.9% | 146.9% | 305.5% | 2.06 | -27.8% |
| 11 | **INTC** | Technology | 93.8 | 11.9% | 168.9% | 222.8% | 483.9% | 2.37 | -24.2% |
| 12 | **TER** | Technology | 93.2 | 27.3% | 36.2% | 110.0% | 367.2% | 2.24 | -26.7% |
| 13 | **CAT** | Industrials | 92.0 | 10.7% | 38.1% | 62.8% | 166.6% | 2.69 | -13.9% |
| 14 | **STLD** | Basic Materials | 92.0 | 18.2% | 60.6% | 60.9% | 107.2% | 2.04 | -20.3% |
| 15 | **NUE** | Basic Materials | 91.9 | 11.5% | 57.3% | 57.0% | 110.8% | 2.40 | -18.4% |
| 16 | **COHR** | Technology | 90.5 | 4.4% | 47.3% | 112.3% | 369.1% | 2.02 | -26.5% |
| 17 | **FIX** | Industrials | 90.1 | 4.2% | 35.8% | 99.7% | 286.5% | 2.47 | -15.8% |
| 18 | **JBL** | Technology | 89.7 | 10.7% | 45.0% | 69.6% | 107.7% | 1.62 | -17.9% |
| 19 | **ON** | Technology | 88.8 | 3.2% | 86.8% | 105.0% | 109.6% | 1.27 | -28.1% |
| 20 | **GLW** | Technology | 88.3 | -1.6% | 35.3% | 99.8% | 249.2% | 2.15 | -23.0% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **TPRO.MI** | Technology | 94.6 | 33.3% | 135.9% | 178.9% | 402.2% | 2.62 | -27.0% |
| 2 | **ASML.AS** | Technology | 94.2 | 32.6% | 39.1% | 78.5% | 156.7% | 2.26 | -15.8% |
| 3 | **STMMI.MI** | Technology | 94.0 | 25.0% | 123.7% | 198.5% | 161.6% | 1.85 | -33.5% |
| 4 | **AIXA.DE** | Technology | 93.3 | 20.0% | 77.2% | 239.5% | 328.4% | 2.29 | -28.4% |
| 5 | **IFX.DE** | Technology | 93.1 | 19.2% | 94.4% | 112.3% | 127.1% | 1.78 | -21.2% |
| 6 | **BESI.AS** | Technology | 92.8 | 21.7% | 65.6% | 135.6% | 153.4% | 1.79 | -20.9% |
| 7 | **ASM.AS** | Technology | 92.5 | 25.3% | 54.4% | 103.7% | 106.2% | 1.59 | -26.2% |
| 8 | **IGG.L** | Financial Services | 90.7 | 20.6% | 40.4% | 64.9% | 79.1% | 2.24 | -11.5% |
| 9 | **RBI.VI** | Financial Services | 90.7 | 21.1% | 49.0% | 49.8% | 126.4% | 2.02 | -18.0% |
| 10 | **KGH.WA** | Basic Materials | 90.6 | 15.5% | 38.3% | 66.2% | 205.5% | 2.17 | -30.8% |
| 11 | **NOKIA.HE** | Technology | 90.5 | 3.8% | 61.4% | 127.0% | 175.1% | 2.00 | -27.6% |
| 12 | **PRY.MI** | Industrials | 90.4 | 3.9% | 50.0% | 75.3% | 160.2% | 2.46 | -13.1% |
| 13 | **SPM.MI** | Energy | 90.1 | 6.4% | 46.2% | 108.5% | 105.1% | 2.16 | -14.7% |
| 14 | **VACN.SW** | Industrials | 89.7 | 16.6% | 37.6% | 75.8% | 105.3% | 1.61 | -25.1% |
| 15 | **SUBC.OL** | Energy | 89.7 | 5.3% | 45.5% | 80.5% | 99.9% | 2.30 | -11.3% |
| 16 | **TIT.MI** | Communication Services | 89.6 | 11.8% | 29.0% | 63.4% | 106.1% | 2.37 | -13.0% |
| 17 | **BMPS.MI** | Financial Services | 89.3 | 27.7% | 67.1% | 49.2% | 72.6% | 1.50 | -25.5% |
| 18 | **TIT.MI** | Communication Services | 89.1 | 11.8% | 29.0% | 63.4% | 106.1% | 2.37 | -13.0% |
| 19 | **HOT.DE** | Industrials | 88.9 | 10.8% | 29.1% | 57.3% | 230.4% | 2.74 | -15.9% |
| 20 | **NDA.DE** | Basic Materials | 88.6 | 7.2% | 27.8% | 75.8% | 154.3% | 2.40 | -16.7% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MO** | Consumer Staples | 0.776 | 0.684 | 0.960 | 0.775 | 0.592 | +25.7% | 14.4 | - |
| 2 | **GL** | Financials | 0.760 | 0.798 | 0.670 | 0.771 | 0.847 | +42.8% | 11.8 | +20.5% |
| 3 | **ALL** | Financials | 0.726 | 0.551 | 0.694 | 0.894 | 0.856 | +15.5% | 4.9 | +45.2% |
| 4 | **TROW** | Financials | 0.723 | 0.696 | 0.734 | 0.756 | 0.698 | +21.5% | 11.5 | +18.7% |
| 5 | **PNC** | Financials | 0.717 | 0.694 | 0.675 | 0.830 | 0.657 | +35.2% | 13.5 | +12.1% |
| 6 | **NTRS** | Financials | 0.715 | 0.836 | 0.632 | 0.665 | 0.725 | +57.4% | 18.0 | +14.5% |
| 7 | **NEM** | Materials | 0.711 | 0.628 | 0.860 | 0.761 | 0.494 | +80.1% | 13.5 | +25.8% |
| 8 | **CFG** | Financials | 0.706 | 0.763 | 0.598 | 0.811 | 0.629 | +66.0% | 15.9 | +7.7% |
| 9 | **MAR** | Consumer Discretionary | 0.701 | 0.834 | 0.860 | 0.388 | 0.641 | +53.6% | 41.5 | - |
| 10 | **HST** | Real Estate | 0.698 | 0.890 | 0.533 | 0.705 | 0.634 | +68.5% | 17.0 | +14.9% |
| 11 | **TRV** | Financials | 0.698 | 0.500 | 0.678 | 0.852 | 0.874 | +18.0% | 9.2 | +25.3% |
| 12 | **APA** | Energy | 0.694 | 0.570 | 0.762 | 0.911 | 0.443 | +72.3% | 7.7 | +26.2% |
| 13 | **HLT** | Consumer Discretionary | 0.693 | 0.756 | 0.894 | 0.337 | 0.760 | +40.5% | 53.3 | - |
| 14 | **SPG** | Real Estate | 0.693 | 0.724 | 0.890 | 0.536 | 0.498 | +40.8% | 14.7 | +113.6% |
| 15 | **AFL** | Financials | 0.690 | 0.539 | 0.693 | 0.779 | 0.840 | +14.2% | 13.2 | +16.5% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | 0.117 | 0.077 | 0.131 | 0.078 | 0.236 |
| 502 | **CSGP** | Real Estate | 0.157 | 0.015 | 0.107 | 0.213 | 0.446 |
| 501 | **NRG** | Utilities | 0.180 | 0.208 | 0.117 | 0.225 | 0.173 |
| 500 | **COIN** | Financials | 0.191 | 0.058 | 0.319 | 0.189 | 0.202 |
| 499 | **DASH** | Consumer Discretionary | 0.261 | 0.312 | 0.306 | 0.119 | 0.303 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W25.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W25.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-06-15  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
