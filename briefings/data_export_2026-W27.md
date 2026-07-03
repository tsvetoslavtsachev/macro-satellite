# Сателит — пълен data export за 2026-W27

_Период: 2026-06-29 → 2026-07-05_  
_Генериран: 2026-07-03 09:20 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W27.md` (structured briefing) и `narrative_2026-W27.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**6 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **XLF** | +3.83% | +1.78σ | 53.57 | 55.62 | 2026-06-26 | 2026-07-02 | +0.89% | +1.65% | 13 |
| **TLT** | -1.76% | -1.61σ | 87.04 | 85.51 | 2026-06-26 | 2026-07-02 | +0.19% | +1.21% | 13 |
| **SOXX** | -4.00% | -1.39σ | 589.94 | 566.32 | 2026-06-26 | 2026-07-02 | +4.93% | +6.43% | 13 |
| **XLC** | +3.22% | +1.32σ | 106.18 | 109.60 | 2026-06-26 | 2026-07-02 | -0.03% | +2.46% | 13 |
| **DFEN** | +14.56% | +1.25σ | 74.88 | 85.78 | 2026-06-26 | 2026-07-02 | +2.07% | +9.97% | 13 |
| **IWM** | -0.75% | -1.03σ | 299.83 | 297.58 | 2026-06-26 | 2026-07-02 | +1.65% | +2.33% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_5 канонични patterns от `config/divergence_rules.yaml`, evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-07-05 · **Conditions matched:** 0/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | -1.42% | ❌ | 105.48 | 103.98 | 2026-06-26 | 2026-07-02 |
| DFEN | down ≥ 3.0% | +14.56% | ❌ | 74.88 | 85.78 | 2026-06-26 | 2026-07-02 |
| GLD | down ≥ 1.0% | +1.20% | ❌ | 373.63 | 378.13 | 2026-06-26 | 2026-07-02 |
| URA | down ≥ 3.0% | -0.83% | ❌ | 43.59 | 43.23 | 2026-06-26 | 2026-07-02 |
| UUP | up ≥ 0.5% | -0.42% | ❌ | 28.46 | 28.34 | 2026-06-26 | 2026-07-02 |

### Ликвидна стес (flight to quality) (`liquidity_stress`) — не активен
_Дългосрочни trezuri нагоре, високодоходен кредит надолу, злато нагоре. Класически risk-off._  
**Window:** 7d ending 2026-07-05 · **Conditions matched:** 1/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| TLT | up ≥ 1.0% | -1.76% | ❌ | 87.04 | 85.51 | 2026-06-26 | 2026-07-02 |
| HYG | down ≥ 0.5% | +0.31% | ❌ | 79.46 | 79.71 | 2026-06-26 | 2026-07-02 |
| GLD | up ≥ 1.0% | +1.20% | ✅ | 373.63 | 378.13 | 2026-06-26 | 2026-07-02 |
| UUP | up ≥ 0.3% | -0.42% | ❌ | 28.46 | 28.34 | 2026-06-26 | 2026-07-02 |

### Възстановяване на инфлационни очаквания (`inflation_pickup`) — не активен
_Inflation-protected треzuri нагоре, commodities нагоре, dollar надолу. Repricing на real rates._  
**Window:** 7d ending 2026-07-05 · **Conditions matched:** 2/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| DBC | up ≥ 1.5% | +0.00% | ❌ | 26.57 | 26.57 | 2026-06-26 | 2026-07-02 |
| GLD | up ≥ 1.0% | +1.20% | ✅ | 373.63 | 378.13 | 2026-06-26 | 2026-07-02 |
| UUP | down ≥ 0.5% | -0.42% | ❌ | 28.46 | 28.34 | 2026-06-26 | 2026-07-02 |
| TLT | down ≥ 1.0% | -1.76% | ✅ | 87.04 | 85.51 | 2026-06-26 | 2026-07-02 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-07-05 · **Conditions matched:** 2/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | -0.75% | ❌ | 299.83 | 297.58 | 2026-06-26 | 2026-07-02 |
| XLF | up ≥ 1.0% | +3.83% | ✅ | 53.57 | 55.62 | 2026-06-26 | 2026-07-02 |
| XLY | up ≥ 1.0% | +2.40% | ✅ | 114.37 | 117.12 | 2026-06-26 | 2026-07-02 |
| GLD | down ≥ 0.5% | +1.20% | ❌ | 373.63 | 378.13 | 2026-06-26 | 2026-07-02 |

### Защитен pivot (staples + utilities + gold) (`defensive_pivot`) — не активен
_XLP + XLU + GLD едновременно нагоре. Smart money flight to defensives без credit panic._  
**Window:** 7d ending 2026-07-05 · **Conditions matched:** 1/3

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| XLP | up ≥ 1.0% | +0.33% | ❌ | 84.71 | 84.99 | 2026-06-26 | 2026-07-02 |
| XLU | up ≥ 1.0% | -0.95% | ❌ | 46.20 | 45.76 | 2026-06-26 | 2026-07-02 |
| GLD | up ≥ 1.0% | +1.20% | ✅ | 373.63 | 378.13 | 2026-06-26 | 2026-07-02 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2021-W32 (week ending 2021-08-15)
**Cosine similarity:** 0.7798 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -0.39% | +5.12% | -0.56% |
| **USO** | +3.96% | +18.03% | +38.60% |
| **GLD** | +1.46% | +4.84% | +4.46% |
| **TLT** | +1.85% | -0.44% | -6.23% |
| **XLE** | -1.96% | +17.87% | +46.07% |
| **IWM** | -0.49% | +8.64% | -8.38% |

### Паралел #2: 2024-W35 (week ending 2024-09-01)
**Cosine similarity:** 0.6790 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.19% | +7.22% | +6.09% |
| **USO** | -3.00% | -3.67% | +1.18% |
| **GLD** | +6.19% | +6.18% | +13.83% |
| **TLT** | +2.74% | -1.65% | -2.20% |
| **XLE** | -0.81% | +5.52% | +1.36% |
| **IWM** | -0.66% | +10.28% | -1.84% |

### Паралел #3: 2025-W15 (week ending 2025-04-13)
**Cosine similarity:** 0.6456 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +9.91% | +17.14% | +23.00% |
| **USO** | +4.71% | +16.30% | +4.41% |
| **GLD** | +0.51% | +3.76% | +23.89% |
| **TLT** | -0.79% | -0.16% | +6.63% |
| **XLE** | +8.72% | +13.90% | +9.83% |
| **IWM** | +13.16% | +20.59% | +29.70% |

### Паралел #4: 2023-W47 (week ending 2023-11-26)
**Cosine similarity:** 0.6119 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.89% | +11.99% | +17.12% |
| **USO** | -0.86% | +1.55% | +6.40% |
| **GLD** | +3.34% | +1.67% | +16.39% |
| **TLT** | +10.68% | +5.54% | +3.77% |
| **XLE** | +1.89% | +2.18% | +9.49% |
| **IWM** | +14.23% | +11.87% | +15.27% |

### Паралел #5: 2025-W50 (week ending 2025-12-14)
**Cosine similarity:** 0.5922 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.06% | -2.57% | +9.42% |
| **USO** | +6.79% | +74.23% | +82.28% |
| **GLD** | +6.62% | +16.54% | -2.25% |
| **TLT** | +0.94% | +0.18% | +0.06% |
| **XLE** | +4.15% | +27.87% | +28.37% |
| **IWM** | +3.30% | -2.53% | +16.00% |

### Паралел #6: 2024-W08 (week ending 2024-02-25)
**Cosine similarity:** 0.5849 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.48% | +4.58% | +11.39% |
| **USO** | +7.47% | +4.77% | +5.05% |
| **GLD** | +6.90% | +14.47% | +23.01% |
| **TLT** | +0.21% | -1.68% | +6.92% |
| **XLE** | +8.52% | +7.15% | +6.85% |
| **IWM** | +2.90% | +3.04% | +10.84% |

### Паралел #7: 2022-W36 (week ending 2022-09-11)
**Cosine similarity:** 0.5706 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -11.66% | -2.88% | -4.26% |
| **USO** | +0.91% | -11.60% | -5.57% |
| **GLD** | -2.92% | +4.53% | +8.79% |
| **TLT** | -7.58% | -1.12% | -1.07% |
| **XLE** | -0.31% | +3.70% | +4.70% |
| **IWM** | -10.04% | -4.19% | -5.06% |

### Паралел #8: 2024-W19 (week ending 2024-05-12)
**Cosine similarity:** 0.5645 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.09% | +2.66% | +15.57% |
| **USO** | +0.28% | +1.22% | -2.88% |
| **GLD** | -2.08% | +2.67% | +13.37% |
| **TLT** | +2.25% | +7.88% | +4.68% |
| **XLE** | -3.56% | -3.95% | +1.55% |
| **IWM** | -1.52% | +1.33% | +17.27% |

### Паралел #9: 2025-W04 (week ending 2025-01-26)
**Cosine similarity:** 0.5524 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -2.26% | -9.16% | +5.42% |
| **USO** | -6.87% | -13.28% | -5.97% |
| **GLD** | +5.07% | +19.20% | +20.24% |
| **TLT** | +5.19% | +2.97% | +1.24% |
| **XLE** | -1.83% | -9.07% | -3.08% |
| **IWM** | -5.81% | -14.93% | -1.39% |

### Паралел #10: 2022-W11 (week ending 2022-03-20)
**Cosine similarity:** 0.5352 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.12% | -17.34% | -12.53% |
| **USO** | +2.97% | +11.66% | -6.35% |
| **GLD** | +1.41% | -4.48% | -13.08% |
| **TLT** | -10.50% | -15.59% | -18.88% |
| **XLE** | +9.81% | +0.42% | +8.39% |
| **IWM** | -2.56% | -19.94% | -13.25% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 13 · **Total matching days:** 72 · **History:** 2021-05-17 → 2026-07-02

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 13 | +2.0% | +1.7% | -3.1% | +7.7% | 77% |
| **SPY** | 3m | 13 | +3.3% | +4.6% | -7.0% | +12.1% | 77% |
| **SPY** | 6m | 13 | +8.2% | +11.6% | -6.1% | +22.7% | 77% |
| **USO** | 1m | 13 | +1.0% | -0.8% | -7.2% | +12.7% | 46% |
| **USO** | 3m | 13 | -3.1% | -4.1% | -25.5% | +24.5% | 46% |
| **USO** | 6m | 13 | +9.2% | -4.4% | -25.5% | +109.4% | 46% |
| **GLD** | 1m | 13 | +2.5% | +0.9% | -2.2% | +8.9% | 77% |
| **GLD** | 3m | 13 | +5.7% | +5.9% | -12.6% | +24.5% | 69% |
| **GLD** | 6m | 13 | +6.0% | +10.3% | -15.0% | +25.3% | 69% |
| **TLT** | 1m | 13 | -1.1% | -0.8% | -6.5% | +3.7% | 31% |
| **TLT** | 3m | 13 | +0.5% | +0.6% | -16.2% | +12.6% | 62% |
| **TLT** | 6m | 13 | -2.4% | -0.9% | -17.2% | +9.1% | 38% |

**Episodes (последни 5 от 13):**
- `2024-06-21 → 2024-06-21` (1d)
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-28 → 2026-05-19` (13d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 1 · **Total matching days:** 49 · **History:** 2021-05-17 → 2026-07-02

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | +9.1% | +9.1% | +9.1% | +9.1% | 100% |
| **SPY** | 3m | 1 | +10.2% | +10.2% | +10.2% | +10.2% | 100% |
| **SPY** | 6m | 1 | +10.2% | +10.2% | +10.2% | +10.2% | 100% |
| **USO** | 1m | 1 | +7.2% | +7.2% | +7.2% | +7.2% | 100% |
| **USO** | 3m | 1 | -16.5% | -16.5% | -16.5% | -16.5% | 0% |
| **USO** | 6m | 1 | -16.5% | -16.5% | -16.5% | -16.5% | 0% |
| **GLD** | 1m | 1 | -0.2% | -0.2% | -0.2% | -0.2% | 0% |
| **GLD** | 3m | 1 | -13.0% | -13.0% | -13.0% | -13.0% | 0% |
| **GLD** | 6m | 1 | -13.0% | -13.0% | -13.0% | -13.0% | 0% |
| **TLT** | 1m | 1 | -0.6% | -0.6% | -0.6% | -0.6% | 0% |
| **TLT** | 3m | 1 | -1.3% | -1.3% | -1.3% | -1.3% | 0% |
| **TLT** | 6m | 1 | -1.3% | -1.3% | -1.3% | -1.3% | 0% |

**Episodes (последни 5 от 1):**
- `2026-04-08 → 2026-06-15` (49d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 7 · **Total matching days:** 777 · **History:** 2021-05-17 → 2026-07-02

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
- `2024-10-04 → 2026-07-02` (439d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-07-02

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 9 · **Total matching days:** 76 · **History:** 2021-05-17 → 2026-07-02

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 9 | +0.4% | +0.9% | -7.2% | +7.8% | 56% |
| **SPY** | 3m | 9 | +2.5% | +4.7% | -8.0% | +12.0% | 56% |
| **SPY** | 6m | 9 | +1.7% | +4.8% | -20.2% | +14.9% | 67% |
| **USO** | 1m | 9 | +2.0% | -1.7% | -15.0% | +52.9% | 33% |
| **USO** | 3m | 9 | +4.9% | -0.1% | -31.0% | +52.2% | 44% |
| **USO** | 6m | 9 | +2.7% | -0.2% | -31.0% | +45.8% | 44% |
| **GLD** | 1m | 9 | -2.2% | -1.6% | -8.3% | +1.9% | 11% |
| **GLD** | 3m | 9 | -2.4% | -2.8% | -12.0% | +6.4% | 44% |
| **GLD** | 6m | 9 | -1.9% | -4.7% | -19.2% | +25.0% | 33% |
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
**Episodes:** 16 · **Total matching days:** 275 · **History:** 2021-05-17 → 2026-07-02

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.2% | +2.2% | -4.8% | +9.0% | 75% |
| **SPY** | 3m | 16 | +3.6% | +4.7% | -12.3% | +16.7% | 75% |
| **SPY** | 6m | 16 | +7.4% | +8.3% | -13.5% | +21.9% | 81% |
| **USO** | 1m | 16 | +1.8% | -3.2% | -13.0% | +27.7% | 38% |
| **USO** | 3m | 16 | +1.2% | -2.6% | -14.5% | +29.9% | 31% |
| **USO** | 6m | 16 | +10.8% | +1.8% | -12.4% | +87.1% | 62% |
| **GLD** | 1m | 16 | +2.4% | +1.8% | -6.4% | +9.0% | 75% |
| **GLD** | 3m | 16 | +6.4% | +7.4% | -15.2% | +23.6% | 69% |
| **GLD** | 6m | 16 | +11.0% | +12.1% | -15.2% | +43.8% | 75% |
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
**Episodes:** 19 · **Total matching days:** 301 · **History:** 2021-05-17 → 2026-07-02

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 19 | +0.4% | +1.0% | -8.3% | +7.0% | 53% |
| **SPY** | 3m | 19 | +2.3% | +3.1% | -13.3% | +9.4% | 68% |
| **SPY** | 6m | 19 | +3.7% | +7.4% | -15.7% | +17.6% | 74% |
| **USO** | 1m | 19 | -0.6% | -5.6% | -21.8% | +55.8% | 42% |
| **USO** | 3m | 19 | +2.4% | -1.3% | -21.8% | +64.3% | 42% |
| **USO** | 6m | 19 | +5.8% | -5.2% | -21.8% | +75.1% | 47% |
| **GLD** | 1m | 19 | -0.6% | -0.1% | -12.4% | +7.6% | 47% |
| **GLD** | 3m | 19 | +1.5% | +1.3% | -13.7% | +19.0% | 63% |
| **GLD** | 6m | 19 | +7.3% | +6.0% | -20.1% | +55.5% | 68% |
| **TLT** | 1m | 19 | +0.1% | +0.3% | -5.5% | +5.5% | 58% |
| **TLT** | 3m | 19 | -2.7% | -3.8% | -16.8% | +9.8% | 42% |
| **TLT** | 6m | 19 | -5.1% | -3.8% | -20.5% | +6.7% | 32% |

**Episodes (последни 5 от 19):**
- `2025-05-12 → 2025-05-19` (3d)
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (12d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-07-02

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (20 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 9 | 2.66 | 2.89 | 2026-05-30 00:00:00 | 2026-06-27 00:00:00 | ✓ |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 9 | 2.33 | 2.34 | 2026-05-30 00:00:00 | 2026-06-27 00:00:00 | ✓ |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 8 | 2.31 | 2.43 | 2026-06-04 00:00:00 | 2026-06-27 00:00:00 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | 8 | 2.28 | 2.58 | 2026-06-04 00:00:00 | 2026-06-27 00:00:00 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | 8 | 2.02 | 2.02 | 2026-06-04 00:00:00 | 2026-06-27 00:00:00 | ✓ |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | 7 | 2.40 | 2.40 | 2026-06-04 00:00:00 | 2026-06-20 00:00:00 | - |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 6 | 2.76 | 2.76 | 2026-06-04 00:00:00 | 2026-06-13 00:00:00 | ✓ |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 6 | 2.30 | 2.39 | 2026-06-06 00:00:00 | 2026-06-27 00:00:00 | ✓ |
| **CSUSHPISA** | Case-Shiller US National HPI (SA) | housing | housing_prices | 6 | 2.26 | 2.26 | 2026-06-04 00:00:00 | 2026-06-13 00:00:00 | - |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | 5 | 2.30 | 2.30 | 2026-06-04 00:00:00 | 2026-06-08 00:00:00 | - |
| **DGORDER** | Нови поръчки за дълготрайни стоки | growth | hard_activity | 2 | 2.90 | 2.90 | 2026-05-30 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **M2** | M2 паричен агрегат | liquidity | money_supply | 2 | 2.76 | 2.76 | 2026-05-30 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **C_AND_I_LOANS** | Търговски и индустриални кредити (C&I) | liquidity | banking_credit | 2 | 2.57 | 2.57 | 2026-05-30 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **UMCSENT** | Michigan Sentiment Index | growth | consumer_sentiment | 2 | 2.57 | 2.57 | 2026-05-30 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CPI_SHELTER** | CPI — жилища (shelter) | inflation | goods_services | 2 | 2.46 | 2.46 | 2026-05-30 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CPI_SERVICES** | CPI — услуги (всички) | inflation | goods_services | 2 | 2.35 | 2.35 | 2026-05-30 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **USSTHPI** | FHFA House Price Index (Q, NSA) | housing | housing_prices | 1 | 2.70 | 2.70 | 2026-06-04 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **RSXFS** | Продажби на дребно (без храна) | growth | hard_activity | 1 | 2.33 | 2.33 | 2026-05-30 00:00:00 | 2026-05-30 00:00:00 | ✓ |
| **PPICORE** | PPI Core (Final Demand без храни и енергия) | inflation | core_measures | 1 | 2.32 | 2.32 | 2026-05-30 00:00:00 | 2026-05-30 00:00:00 | ✓ |
| **MSACSR** | Месеци предлагане — нови жилища | housing | housing_affordability | 1 | 2.02 | 2.02 | 2026-06-27 00:00:00 | 2026-06-27 00:00:00 | ✓ |

### EU (10 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 7 | 5.37 | 5.37 | 2026-06-05 00:00:00 | 2026-06-27 00:00:00 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation | sentiment | 7 | 2.98 | 2.98 | 2026-06-05 00:00:00 | 2026-06-27 00:00:00 | - |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | 7 | 2.32 | 2.32 | 2026-06-05 00:00:00 | 2026-06-27 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 7 | 2.28 | 2.31 | 2026-06-05 00:00:00 | 2026-06-27 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 7 | 2.25 | 2.27 | 2026-06-05 00:00:00 | 2026-06-27 00:00:00 | ✓ |
| **EA_COMP_PER_EMPLOYEE** | Компенсация на наетите (D1, EA-20, M€) | labor | wages | 3 | 2.39 | 2.39 | 2026-05-30 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **EA_RETAIL_CONF** | Доверие в търговията на дребно (DG ECFIN) | growth | sentiment | 3 | 2.29 | 2.29 | 2026-05-30 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **EA_PPI_INTERMEDIATE** | PPI междинни стоки (MIG ING, индекс 2021=100) | inflation | producer_prices | 3 | 2.06 | 2.16 | 2026-05-30 00:00:00 | 2026-06-04 00:00:00 | - |
| **EA_RETAIL_VOL** | Търговия на дребно — обем на продажбите (G47, индекс 2021=100) | growth | hard_activity | 3 | 2.03 | 2.06 | 2026-05-30 00:00:00 | 2026-06-04 00:00:00 | - |
| **EA_WAGES_SALARIES** | Работни заплати (D11, EA-20, M€) | labor | wages | 2 | 2.38 | 2.38 | 2026-06-03 00:00:00 | 2026-06-04 00:00:00 | ✓ |

### CN (7 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 7 | 2.56 | 2.56 | 2026-06-02 00:00:00 | 2026-06-29 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 7 | 2.23 | 2.23 | 2026-06-02 00:00:00 | 2026-06-29 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 6 | 2.24 | 2.24 | 2026-06-02 00:00:00 | 2026-06-22 00:00:00 | - |
| **CN_POLICY_RATE** | Политическа лихва — PBoC 7-day repo (%) | credit | rates | 2 | 2.39 | 2.39 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CN_FDI_GDP** | ПЧИ — входящи (% от БВП) | property | investment | 2 | 2.11 | 2.11 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |
| **CN_BIS_PROPERTY_YOY** | Жилищни имотни цени (YoY %, BIS номинал) | property | housing | 2 | 2.10 | 2.10 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | - |
| **CN_CREDIT_PRIVATE** | Кредит към частния сектор (% от БВП) | credit | credit_depth | 2 | 2.07 | 2.07 | 2026-06-02 00:00:00 | 2026-06-04 00:00:00 | ✓ |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-06-27 00:00:00 · **Generated:** 2026-06-27 09:30:58.620455+00:00

**Режим:** `stagflation_confirmed` (Стагфлация (потвърдена))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 35.3 | contracting | 29.6% | 2 | 2 |
| **growth** | 41.7 | mixed | 28.0% | 1 | 1 |
| **inflation** | 36.6 | contracting | 33.3% | 4 | 1 |
| **liquidity** | 52.8 | mixed | 42.1% | 0 | 0 |

### Top anomalies (7 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | +2.89 | up | 6.42 | 2026-05-01 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | +2.58 | up | 5.29 | 2026-05-01 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | +2.43 | up | 4.80 | 2026-05-01 | - |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.34 | down | 94.99 | 2026-01-01 | ✓ min |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | +2.28 | up | 55.10 | 2026-05-01 | ✓ max |
| **JTSQUR** | Quits rate — напускания | labor | flow | -2.02 | down | 1.90 | 2026-04-01 | ✓ min |
| **MSACSR** | Месеци предлагане — нови жилища | housing | housing_affordability | +2.02 | up | 10.30 | 2026-05-01 | ✓ max |

### Narrative hints от макро лещите
- **PPIFIS**: Производствени цени → consumer prices с 1-3 месечен lag. Водещ за CPI при трендови промени.
- **CPI_GOODS**: Goods inflation реагира бързо на supply shocks. 2022 peak след доставъчните кризи. Сега често е в deflation/близо до 0.
- **MICH_INFL_1Y**: Household очаквания. По-шумни от market-based, но по-ранни. Extreme movements сигнализират de-anchoring risk.
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **US_PMI_MFG**: Markit mfg — comparable cross-country. ISM е US-only.
- **JTSQUR**: Работническа увереност. Ако quits rate пада — хората задържат работата си (pre-recession pattern).
- **MSACSR**: Inventory ÷ current sales rate. <4 = tight market, 6 = balanced, >7 = oversupplied. Класически recession leading.

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
  - `breadth_a`: 0.8
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
  - `state`: both_up
  - `interpretation`: Tightening transmits — rates up + credit widens.
  - `slot_a_label`: Credit stress
  - `slot_b_label`: Policy tightening
  - `breadth_a`: 1.0
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
  - `breadth_b`: 0.8
- 🔔 **?**
  - `pair_id`: model_vs_market
  - `name_bg`: Model-implied × Market-implied inflation
  - `question_bg`: Дали underlying persistence и market pricing-а са съгласни за инфлацията?
  - `state`: both_down
  - `interpretation`: Съгласие — disinflation confirmation. Converging view.
  - `slot_a_label`: Модел (sticky inflation)
  - `slot_b_label`: Пазар (breakevens + survey)
  - `breadth_a`: 0.333
  - `breadth_b`: 0.333

### Executive narrative
> Картината показва потвърдена стагфлационна конфигурация — трудовият пазар остава tight, а инфлационният натиск е broad-based. Най-отклонена леща: Инфлация и цени — breadth 67% (разширяване), 4 аномалии, 1 нови екстремума. Обаче inflation expectations остават anchored — Fed narrative-ът за момента държи. За наблюдение следващия релиз: LABOR_SHARE_NBS, US_PMI_MFG (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: PPIFIS z=+2.89
- 4 нови екстремуми в top-7 (lookback 5г.)
- Активни двойки: Stagflation test=both_up; Growth × Labor=a_up_b_down; Inflation anchoring=a_up_b_down



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-06-27 00:00:00 · **Generated:** 2026-06-27 09:37:52.401003+00:00

**Режим:** `stagflation_confirmed` (Стагфлация (потвърдена))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 36.5 | contracting | 42.9% | 1 | 0 |
| **growth** | 38.1 | mixed | 16.7% | 1 | 0 |
| **inflation** | 43.3 | mixed | 42.9% | 1 | 0 |
| **credit** | 44.7 | mixed | 36.8% | 3 | 2 |

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

**Дата:** 2026-06-29 00:00:00 · **Generated:** 2026-06-29 10:17:36.943237+00:00

**Режим:** `recessionary` (РЕЦЕСИОНЕН)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 29.9 | contracting | -% | - | - |
| **inflation** | 48.0 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 42.4 | mixed | -% | - | - |
| **property** | 23.2 | contracting | -% | - | - |

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
  - `breadth_a`: 0.833
  - `breadth_b`: 0.333

### Executive narrative
> Претеглен композитен macro score 33.3/100 → режим „РЕЦЕСИОНЕН“. 5 лещи, 2 flagged аномалии (5 застояли изключени), 3 cross-lens двойки.



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

### US (period: 2026-06-26 → 2026-07-01)

**stable_winner (1m):** +13 entered, -12 exited
  - **Entered:** AES, BG, CHRW, CVNA, DLTR, GS, HSY, LHX, NEM, PLD, SPG, VRT, WBD _(включително 2 за първи път в историята: DLTR, HSY)_
  - **Exited:** APA, BEN, CBOE, CIEN, COHR, EL, GE, GILD, HAL, MRK, PWR, STX

**stable_winner (3m):** +2 entered, -4 exited
  - **Entered:** IBKR, PWR
  - **Exited:** CFG, JNJ, KEY, NEE

**quality_dip (1m):** +12 entered, -13 exited
  - **Entered:** APA, BEN, CBOE, CIEN, COHR, EL, GILD, HAL, MRK, PWR, RF, STX _(включително 4 за първи път в историята: BEN, HAL, MRK, RF)_
  - **Exited:** AES, BG, CHRW, CVNA, DLTR, GS, HSY, LHX, NEM, PLD, SPG, VRT, WBD

**quality_dip (3m):** +5 entered, -3 exited
  - **Entered:** CFG, JNJ, KEY, NEE, RF _(включително 1 за първи път в историята: RF)_
  - **Exited:** GE, IBKR, PWR

**faded_bounce (1m):** +5 entered, -9 exited
  - **Entered:** AVB, AWK, BRO, HRL, RSG _(включително 1 за първи път в историята: RSG)_
  - **Exited:** APO, CARR, CMG, CPRT, FISV, LII, NKE, TAP, TPL

**faded_bounce (3m):** +7 entered, -2 exited
  - **Entered:** BR, CARR, DPZ, HRL, LII, PEG, SW _(включително 1 за първи път в историята: HRL)_
  - **Exited:** KKR, MAS

### EU (period: 2026-06-26 → 2026-07-01)

**stable_winner (1m):** +9 entered, -12 exited
  - **Entered:** ASML.AS, CBK.DE, EBS.VI, GLE.PA, IG.MI, ITX.MC, MRL.MC, NDA.DE, TIT.MI _(включително 1 за първи път в историята: ITX.MC)_
  - **Exited:** A5G.IR, AAF.L, AED.BR, BATS.L, BIRG.IR, BKT.MC, CCH.L, DANSKE.CO, IDR.MC, METSO.HE, RR.L, STAN.L

**stable_winner (3m):** +12 entered, -9 exited
  - **Entered:** ALLN.SW, BARC.L, BBY.L, BIRG.IR, COFB.BR, DLG.MI, FR.PA, GAW.L, IG.MI, PKN.WA, SPSN.SW, TIT.MI _(включително 1 за първи път в историята: COFB.BR)_
  - **Exited:** ANA.MC, BATS.L, BBVA.MC, CABK.MC, KCR.HE, LTMC.MI, REP.MC, URW.PA, WRT1V.HE

**quality_dip (1m):** +12 entered, -8 exited
  - **Entered:** A5G.IR, AAF.L, AED.BR, BATS.L, BIRG.IR, BKT.MC, CCH.L, DANSKE.CO, IDR.MC, METSO.HE, RR.L, STAN.L
  - **Exited:** ASML.AS, CBK.DE, EBS.VI, GLE.PA, IG.MI, MRL.MC, NDA.DE, TIT.MI

**quality_dip (3m):** +10 entered, -12 exited
  - **Entered:** ANA.MC, BATS.L, BBVA.MC, CABK.MC, ITX.MC, KCR.HE, LTMC.MI, REP.MC, URW.PA, WRT1V.HE _(включително 3 за първи път в историята: ANA.MC, ITX.MC, KCR.HE)_
  - **Exited:** ALLN.SW, BARC.L, BBY.L, BIRG.IR, COFB.BR, DLG.MI, FR.PA, GAW.L, IG.MI, PKN.WA, SPSN.SW, TIT.MI

**faded_bounce (1m):** +6 entered, -9 exited
  - **Entered:** AMS.MC, BPT.L, EVD.DE, HNR1.DE, SGE.L, SWEC-B.ST _(включително 1 за първи път в историята: AMS.MC)_
  - **Exited:** AAK.ST, ADM.L, ENX.PA, GF.SW, INPST.AS, PSON.L, RED.MC, SIGN.SW, STLAM.MI

**faded_bounce (3m):** +7 entered, -10 exited
  - **Entered:** BEI.DE, BOL.PA, EXPN.L, NEXI.MI, ORSTED.CO, SY1.DE, TOM.OL _(включително 1 за първи път в историята: SY1.DE)_
  - **Exited:** CMBN.SW, CVC.AS, DSFIR.AS, ENX.PA, INPST.AS, PSON.L, SAGA-B.ST, THULE.ST, UMG.AS, WISE.L



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
| 1 | **AMAT** | Technology | 96.0 | 42.1% | 90.7% | 148.1% | 258.2% | 2.27 | -21.4% |
| 2 | **KLAC** | Technology | 95.4 | 37.2% | 81.0% | 111.7% | 199.1% | 1.90 | -22.4% |
| 3 | **LRCX** | Technology | 95.3 | 23.5% | 83.2% | 122.9% | 304.2% | 2.39 | -20.0% |
| 4 | **SNDK** | Technology | 95.0 | 15.4% | 219.9% | 732.0% | 4381.2% | 3.64 | -31.3% |
| 5 | **MRVL** | Technology | 94.6 | 24.0% | 174.8% | 217.6% | 252.4% | 1.69 | -26.4% |
| 6 | **GLW** | Technology | 94.5 | 24.9% | 62.5% | 148.7% | 324.1% | 2.23 | -23.0% |
| 7 | **INTC** | Technology | 94.4 | 16.2% | 187.8% | 246.3% | 467.1% | 2.28 | -24.2% |
| 8 | **WDC** | Technology | 93.8 | 9.6% | 121.3% | 233.3% | 837.6% | 3.12 | -21.4% |
| 9 | **CAT** | Industrials | 92.9 | 14.6% | 40.2% | 72.1% | 158.1% | 2.43 | -13.9% |
| 10 | **MRNA** | Healthcare | 92.8 | 57.4% | 42.7% | 132.7% | 162.8% | 1.39 | -35.5% |
| 11 | **TER** | Technology | 92.7 | 15.7% | 44.2% | 116.7% | 376.5% | 2.15 | -26.7% |
| 12 | **AMD** | Technology | 92.2 | 6.0% | 165.9% | 150.9% | 281.2% | 1.94 | -27.8% |
| 13 | **MU** | Technology | 91.4 | -0.3% | 205.6% | 250.8% | 739.5% | 2.80 | -30.3% |
| 14 | **STX** | Technology | 91.3 | -0.6% | 133.8% | 226.1% | 539.3% | 2.74 | -21.0% |
| 15 | **FLEX** | Technology | 91.0 | 3.7% | 134.5% | 145.4% | 207.6% | 1.80 | -18.4% |
| 16 | **PANW** | Technology | 90.9 | 17.2% | 119.6% | 88.4% | 72.0% | 1.23 | -36.0% |
| 17 | **GEV** | Industrials | 90.3 | 19.4% | 30.0% | 71.3% | 115.0% | 1.42 | -24.6% |
| 18 | **COHR** | Technology | 89.8 | 1.6% | 54.8% | 95.0% | 313.2% | 1.81 | -26.5% |
| 19 | **FIX** | Industrials | 89.8 | 4.3% | 35.3% | 96.4% | 248.6% | 2.19 | -15.8% |
| 20 | **HUM** | Healthcare | 88.8 | 25.0% | 136.7% | 59.7% | 69.9% | 0.96 | -47.2% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **ATS.VI** | Technology | 94.6 | 29.7% | 276.8% | 505.0% | 1032.6% | 3.18 | -24.5% |
| 2 | **ASML.AS** | Technology | 92.7 | 12.3% | 47.0% | 78.8% | 150.9% | 2.15 | -15.8% |
| 3 | **VACN.SW** | Industrials | 90.4 | 13.4% | 46.2% | 87.2% | 115.0% | 1.69 | -25.1% |
| 4 | **ASM.AS** | Technology | 90.2 | 11.8% | 56.5% | 92.6% | 95.5% | 1.43 | -26.2% |
| 5 | **GL9.IR** | Consumer Defensive | 90.2 | 11.2% | 42.6% | 69.1% | 92.0% | 2.26 | -8.0% |
| 6 | **TPRO.MI** | Technology | 89.7 | -0.3% | 142.0% | 183.3% | 379.7% | 2.53 | -27.0% |
| 7 | **TIT.MI** | Communication Services | 89.3 | 11.3% | 35.8% | 58.4% | 98.7% | 2.30 | -13.0% |
| 8 | **RBI.VI** | Financial Services | 89.3 | 11.4% | 56.0% | 48.1% | 117.8% | 1.94 | -18.0% |
| 9 | **PST.MI** | Financial Services | 88.6 | 16.3% | 48.4% | 39.1% | 68.7% | 2.70 | -15.5% |
| 10 | **BG.VI** | Financial Services | 87.9 | 16.8% | 42.4% | 43.0% | 72.4% | 1.96 | -16.3% |
| 11 | **BESI.AS** | Technology | 87.8 | -1.6% | 58.4% | 111.9% | 134.1% | 1.61 | -20.9% |
| 12 | **IFCN.SW** | Technology | 87.7 | 5.9% | 86.1% | 85.9% | 73.9% | 1.35 | -25.5% |
| 13 | **SUBC.OL** | Energy | 87.6 | 6.6% | 26.8% | 72.3% | 98.0% | 2.18 | -11.3% |
| 14 | **STMMI.MI** | Technology | 87.4 | -8.5% | 118.4% | 178.8% | 147.9% | 1.70 | -33.5% |
| 15 | **ABBN.SW** | Industrials | 86.9 | 0.1% | 36.5% | 48.6% | 90.8% | 2.29 | -12.1% |
| 16 | **PRY.MI** | Industrials | 86.9 | -7.5% | 46.0% | 66.9% | 142.6% | 2.27 | -13.1% |
| 17 | **HOT.DE** | Industrials | 86.9 | 3.4% | 31.6% | 49.5% | 209.8% | 2.58 | -15.9% |
| 18 | **NOKIA.HE** | Technology | 86.4 | -14.5% | 66.6% | 109.0% | 166.4% | 1.91 | -27.4% |
| 19 | **IFX.DE** | Technology | 86.3 | -11.5% | 105.0% | 108.1% | 116.8% | 1.62 | -21.2% |
| 20 | **AIXA.DE** | Technology | 86.3 | -10.9% | 58.3% | 199.1% | 219.1% | 1.81 | -28.4% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MO** | Consumer Staples | 0.812 | 0.714 | 0.960 | 0.886 | 0.587 | +30.2% | 15.2 | - |
| 2 | **ALL** | Financials | 0.778 | 0.768 | 0.693 | 0.866 | 0.822 | +29.0% | 5.5 | +45.2% |
| 3 | **GL** | Financials | 0.767 | 0.847 | 0.670 | 0.735 | 0.854 | +49.9% | 12.5 | +20.5% |
| 4 | **TROW** | Financials | 0.763 | 0.750 | 0.734 | 0.849 | 0.704 | +24.6% | 12.7 | +18.7% |
| 5 | **TRV** | Financials | 0.754 | 0.724 | 0.679 | 0.814 | 0.868 | +31.7% | 10.2 | +25.3% |
| 6 | **USB** | Financials | 0.736 | 0.716 | 0.703 | 0.842 | 0.662 | +33.9% | 12.9 | +12.3% |
| 7 | **CINF** | Financials | 0.726 | 0.763 | 0.539 | 0.837 | 0.842 | +32.1% | 11.0 | +18.7% |
| 8 | **PNC** | Financials | 0.721 | 0.731 | 0.676 | 0.795 | 0.670 | +31.2% | 14.5 | +12.1% |
| 9 | **MTB** | Financials | 0.716 | 0.655 | 0.672 | 0.822 | 0.747 | +21.4% | 13.4 | +10.3% |
| 10 | **SPG** | Real Estate | 0.708 | 0.795 | 0.891 | 0.516 | 0.491 | +42.0% | 15.7 | +113.6% |
| 11 | **NTRS** | Financials | 0.708 | 0.815 | 0.632 | 0.646 | 0.750 | +37.1% | 18.5 | +14.5% |
| 12 | **RF** | Financials | 0.705 | 0.644 | 0.682 | 0.864 | 0.610 | +27.0% | 12.6 | +11.9% |
| 13 | **HST** | Real Estate | 0.704 | 0.868 | 0.536 | 0.741 | 0.650 | +55.9% | 15.9 | +14.9% |
| 14 | **CFG** | Financials | 0.698 | 0.765 | 0.598 | 0.782 | 0.620 | +53.5% | 16.8 | +7.7% |
| 15 | **EG** | Financials | 0.697 | 0.573 | 0.574 | 0.888 | 0.873 | +11.4% | 7.6 | +13.8% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **NRG** | Utilities | 0.152 | 0.150 | 0.117 | 0.199 | 0.151 |
| 502 | **CSGP** | Real Estate | 0.155 | 0.017 | 0.106 | 0.200 | 0.453 |
| 501 | **COIN** | Financials | 0.203 | 0.108 | 0.319 | 0.175 | 0.205 |
| 500 | **AXON** | Industrials | 0.251 | 0.548 | 0.131 | 0.050 | 0.233 |
| 499 | **KKR** | Financials | 0.253 | 0.189 | 0.160 | 0.400 | 0.322 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W27.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W27.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-06-29  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
