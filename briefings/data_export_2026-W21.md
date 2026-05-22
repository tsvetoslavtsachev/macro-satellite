# Сателит — пълен data export за 2026-W21

_Период: 2026-05-18 → 2026-05-24_  
_Генериран: 2026-05-22 09:28 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W21.md` (structured briefing) и `narrative_2026-W21.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**7 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **XLV** | +2.10% | +1.30σ | 145.10 | 148.15 | 2026-05-15 | 2026-05-21 | -0.58% | +2.07% | 13 |
| **XLU** | +2.58% | +1.26σ | 43.87 | 45.00 | 2026-05-15 | 2026-05-21 | -0.37% | +2.34% | 13 |
| **DBA** | -0.79% | -1.23σ | 27.83 | 27.61 | 2026-05-15 | 2026-05-21 | +0.59% | +1.12% | 13 |
| **XLRE** | +2.94% | +1.22σ | 43.23 | 44.50 | 2026-05-15 | 2026-05-21 | +0.03% | +2.38% | 13 |
| **VNQ** | +2.94% | +1.22σ | 93.91 | 96.67 | 2026-05-15 | 2026-05-21 | +0.05% | +2.36% | 13 |
| **DBC** | -1.57% | -1.18σ | 31.19 | 30.70 | 2026-05-15 | 2026-05-21 | +2.12% | +3.14% | 13 |
| **DFEN** | +8.30% | +1.04σ | 59.30 | 64.22 | 2026-05-15 | 2026-05-21 | -1.87% | +9.75% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_5 канонични patterns от `config/divergence_rules.yaml`, evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-05-24 · **Conditions matched:** 0/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | -3.84% | ❌ | 148.23 | 142.54 | 2026-05-15 | 2026-05-21 |
| DFEN | down ≥ 3.0% | +8.30% | ❌ | 59.30 | 64.22 | 2026-05-15 | 2026-05-21 |
| GLD | down ≥ 1.0% | -0.07% | ❌ | 417.29 | 416.99 | 2026-05-15 | 2026-05-21 |
| URA | down ≥ 3.0% | -2.14% | ❌ | 49.93 | 48.86 | 2026-05-15 | 2026-05-21 |
| UUP | up ≥ 0.5% | -0.14% | ❌ | 27.77 | 27.73 | 2026-05-15 | 2026-05-21 |

### Ликвидна стес (flight to quality) (`liquidity_stress`) — не активен
_Дългосрочни trezuri нагоре, високодоходен кредит надолу, злато нагоре. Класически risk-off._  
**Window:** 7d ending 2026-05-24 · **Conditions matched:** 0/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| TLT | up ≥ 1.0% | +0.67% | ❌ | 83.66 | 84.22 | 2026-05-15 | 2026-05-21 |
| HYG | down ≥ 0.5% | +0.55% | ❌ | 79.46 | 79.90 | 2026-05-15 | 2026-05-21 |
| GLD | up ≥ 1.0% | -0.07% | ❌ | 417.29 | 416.99 | 2026-05-15 | 2026-05-21 |
| UUP | up ≥ 0.3% | -0.14% | ❌ | 27.77 | 27.73 | 2026-05-15 | 2026-05-21 |

### Възстановяване на инфлационни очаквания (`inflation_pickup`) — не активен
_Inflation-protected треzuri нагоре, commodities нагоре, dollar надолу. Repricing на real rates._  
**Window:** 7d ending 2026-05-24 · **Conditions matched:** 0/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| DBC | up ≥ 1.5% | -1.57% | ❌ | 31.19 | 30.70 | 2026-05-15 | 2026-05-21 |
| GLD | up ≥ 1.0% | -0.07% | ❌ | 417.29 | 416.99 | 2026-05-15 | 2026-05-21 |
| UUP | down ≥ 0.5% | -0.14% | ❌ | 27.77 | 27.73 | 2026-05-15 | 2026-05-21 |
| TLT | down ≥ 1.0% | +0.67% | ❌ | 83.66 | 84.22 | 2026-05-15 | 2026-05-21 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — 🔔 ТРИГГЕРИРАН
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-05-24 · **Conditions matched:** 3/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | +1.76% | ✅ | 277.60 | 282.49 | 2026-05-15 | 2026-05-21 |
| XLF | up ≥ 1.0% | +1.23% | ✅ | 51.10 | 51.73 | 2026-05-15 | 2026-05-21 |
| XLY | up ≥ 1.0% | +1.86% | ✅ | 116.53 | 118.70 | 2026-05-15 | 2026-05-21 |
| GLD | down ≥ 0.5% | -0.07% | ❌ | 417.29 | 416.99 | 2026-05-15 | 2026-05-21 |

### Защитен pivot (staples + utilities + gold) (`defensive_pivot`) — не активен
_XLP + XLU + GLD едновременно нагоре. Smart money flight to defensives без credit panic._  
**Window:** 7d ending 2026-05-24 · **Conditions matched:** 1/3

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| XLP | up ≥ 1.0% | +0.02% | ❌ | 84.64 | 84.66 | 2026-05-15 | 2026-05-21 |
| XLU | up ≥ 1.0% | +2.58% | ✅ | 43.87 | 45.00 | 2026-05-15 | 2026-05-21 |
| GLD | up ≥ 1.0% | -0.07% | ❌ | 417.29 | 416.99 | 2026-05-15 | 2026-05-21 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2025-W26 (week ending 2025-06-29)
**Cosine similarity:** 0.9460 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.31% | +7.93% | +12.91% |
| **USO** | +8.90% | +5.10% | -6.55% |
| **GLD** | +1.67% | +15.11% | +38.35% |
| **TLT** | +0.29% | +2.89% | +3.03% |
| **XLE** | +4.28% | +8.76% | +5.41% |
| **IWM** | +3.35% | +12.32% | +17.40% |

### Паралел #2: 2025-W18 (week ending 2025-05-04)
**Cosine similarity:** 0.9109 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.18% | +10.02% | +21.03% |
| **USO** | +9.19% | +21.01% | +13.36% |
| **GLD** | +3.67% | +3.74% | +23.54% |
| **TLT** | -2.74% | +1.24% | +4.84% |
| **XLE** | +1.95% | +5.25% | +9.30% |
| **IWM** | +4.26% | +7.50% | +23.51% |

### Паралел #3: 2025-W32 (week ending 2025-08-10)
**Cosine similarity:** 0.8972 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.06% | +5.59% | +9.01% |
| **USO** | +0.12% | -2.78% | +5.03% |
| **GLD** | +6.71% | +17.65% | +45.49% |
| **TLT** | +2.61% | +3.73% | +2.53% |
| **XLE** | +3.12% | +6.33% | +27.55% |
| **IWM** | +7.50% | +9.97% | +21.03% |

### Паралел #4: 2024-W42 (week ending 2024-10-20)
**Cosine similarity:** 0.8798 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.98% | +2.57% | -9.38% |
| **USO** | +1.30% | +15.61% | -2.66% |
| **GLD** | -3.19% | -0.80% | +21.83% |
| **TLT** | -3.05% | -6.12% | -4.77% |
| **XLE** | +5.58% | +4.88% | -8.32% |
| **IWM** | +2.21% | +0.21% | -16.93% |

### Паралел #5: 2024-W18 (week ending 2024-05-05)
**Cosine similarity:** 0.8533 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.34% | +4.56% | +12.39% |
| **USO** | -5.38% | -2.32% | -4.14% |
| **GLD** | +1.08% | +5.81% | +18.55% |
| **TLT** | +3.50% | +10.48% | +3.13% |
| **XLE** | -2.90% | -3.74% | -3.35% |
| **IWM** | +0.03% | +3.77% | +9.13% |

### Паралел #6: 2023-W05 (week ending 2023-02-05)
**Cosine similarity:** 0.8379 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -3.41% | +0.45% | +9.17% |
| **USO** | +5.36% | -2.13% | +14.58% |
| **GLD** | -2.79% | +8.07% | +3.88% |
| **TLT** | -4.43% | -0.95% | -8.11% |
| **XLE** | -0.21% | -5.69% | +3.07% |
| **IWM** | -5.32% | -11.12% | -0.79% |

### Паралел #7: 2025-W40 (week ending 2025-10-05)
**Cosine similarity:** 0.8335 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.90% | +2.39% | -1.44% |
| **USO** | +0.31% | -3.83% | +92.33% |
| **GLD** | +1.31% | +11.36% | +20.07% |
| **TLT** | +0.99% | -1.55% | -0.72% |
| **XLE** | -1.93% | +3.56% | +35.30% |
| **IWM** | -1.88% | +1.54% | +2.75% |

### Паралел #8: 2023-W01 (week ending 2023-01-08)
**Cosine similarity:** 0.8217 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +6.99% | +5.84% | +13.86% |
| **USO** | +4.52% | +8.38% | +1.57% |
| **GLD** | +0.16% | +7.36% | +2.84% |
| **TLT** | +0.14% | +3.97% | -4.33% |
| **XLE** | +0.90% | -1.93% | -5.95% |
| **IWM** | +10.14% | -1.72% | +4.69% |

### Паралел #9: 2021-W31 (week ending 2021-08-08)
**Cosine similarity:** 0.8078 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.03% | +6.22% | +2.09% |
| **USO** | +0.99% | +18.88% | +36.45% |
| **GLD** | +1.86% | +3.16% | +2.56% |
| **TLT** | -0.45% | +1.41% | -5.22% |
| **XLE** | -2.38% | +19.10% | +42.68% |
| **IWM** | +1.34% | +8.57% | -10.66% |

### Паралел #10: 2024-W05 (week ending 2024-02-04)
**Cosine similarity:** 0.8030 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.60% | +3.75% | +8.48% |
| **USO** | +8.80% | +11.29% | +8.71% |
| **GLD** | +4.55% | +12.91% | +19.47% |
| **TLT** | -0.35% | -5.55% | +4.35% |
| **XLE** | +3.99% | +11.73% | +7.56% |
| **IWM** | +4.79% | +4.12% | +8.04% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 13 · **Total matching days:** 72 · **History:** 2021-05-17 → 2026-05-21

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 13 | +1.9% | +1.7% | -3.1% | +7.7% | 77% |
| **SPY** | 3m | 13 | +3.3% | +4.4% | -7.0% | +12.6% | 77% |
| **SPY** | 6m | 13 | +8.2% | +11.6% | -6.1% | +22.7% | 77% |
| **USO** | 1m | 13 | +1.7% | +1.5% | -7.2% | +12.7% | 54% |
| **USO** | 3m | 13 | +0.8% | +2.1% | -18.9% | +24.5% | 62% |
| **USO** | 6m | 13 | +13.8% | +2.1% | -8.7% | +109.4% | 62% |
| **GLD** | 1m | 13 | +2.5% | +0.9% | -1.2% | +8.9% | 77% |
| **GLD** | 3m | 13 | +6.9% | +5.9% | -6.2% | +24.5% | 69% |
| **GLD** | 6m | 13 | +7.4% | +10.3% | -12.5% | +25.3% | 69% |
| **TLT** | 1m | 13 | -1.3% | -0.8% | -6.5% | +3.7% | 31% |
| **TLT** | 3m | 13 | +0.2% | +0.6% | -16.2% | +12.6% | 54% |
| **TLT** | 6m | 13 | -2.7% | -2.4% | -17.2% | +9.1% | 38% |

**Episodes (последни 5 от 13):**
- `2024-06-21 → 2024-06-21` (1d)
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-28 → 2026-05-19` (13d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 1 · **Total matching days:** 33 · **History:** 2021-05-17 → 2026-05-21

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | +9.1% | +9.1% | +9.1% | +9.1% | 100% |
| **SPY** | 3m | 1 | +9.9% | +9.9% | +9.9% | +9.9% | 100% |
| **SPY** | 6m | 1 | +9.9% | +9.9% | +9.9% | +9.9% | 100% |
| **USO** | 1m | 1 | +7.2% | +7.2% | +7.2% | +7.2% | 100% |
| **USO** | 3m | 1 | +14.4% | +14.4% | +14.4% | +14.4% | 100% |
| **USO** | 6m | 1 | +14.4% | +14.4% | +14.4% | +14.4% | 100% |
| **GLD** | 1m | 1 | -0.2% | -0.2% | -0.2% | -0.2% | 0% |
| **GLD** | 3m | 1 | -4.0% | -4.0% | -4.0% | -4.0% | 0% |
| **GLD** | 6m | 1 | -4.0% | -4.0% | -4.0% | -4.0% | 0% |
| **TLT** | 1m | 1 | -0.6% | -0.6% | -0.6% | -0.6% | 0% |
| **TLT** | 3m | 1 | -2.7% | -2.7% | -2.7% | -2.7% | 0% |
| **TLT** | 6m | 1 | -2.7% | -2.7% | -2.7% | -2.7% | 0% |

**Episodes (последни 5 от 1):**
- `2026-04-08 → 2026-05-21` (33d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 7 · **Total matching days:** 747 · **History:** 2021-05-17 → 2026-05-21

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
- `2024-10-04 → 2026-05-21` (409d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-05-21

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 9 · **Total matching days:** 76 · **History:** 2021-05-17 → 2026-05-21

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 9 | +0.2% | +0.9% | -7.2% | +7.8% | 56% |
| **SPY** | 3m | 9 | +2.2% | +4.4% | -8.0% | +10.7% | 56% |
| **SPY** | 6m | 9 | +1.7% | +4.8% | -20.2% | +14.9% | 67% |
| **USO** | 1m | 9 | +3.0% | -1.7% | -15.0% | +52.9% | 33% |
| **USO** | 3m | 9 | +8.4% | -0.1% | -20.7% | +58.0% | 44% |
| **USO** | 6m | 9 | +10.3% | -0.2% | -27.6% | +58.0% | 44% |
| **GLD** | 1m | 9 | -2.2% | -1.6% | -8.3% | +1.9% | 11% |
| **GLD** | 3m | 9 | -1.2% | -0.1% | -10.9% | +6.4% | 44% |
| **GLD** | 6m | 9 | +0.1% | -0.8% | -11.4% | +25.0% | 33% |
| **TLT** | 1m | 9 | -1.9% | -2.2% | -5.7% | +2.6% | 11% |
| **TLT** | 3m | 9 | -6.0% | -5.1% | -16.9% | +5.4% | 22% |
| **TLT** | 6m | 9 | -8.9% | -6.1% | -21.7% | +3.4% | 11% |

**Episodes (последни 5 от 9):**
- `2023-04-12 → 2023-04-18` (5d)
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-04-09` (27d)
- `2026-04-29 → 2026-05-19` (7d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 16 · **Total matching days:** 275 · **History:** 2021-05-17 → 2026-05-21

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.2% | +2.2% | -4.8% | +9.0% | 75% |
| **SPY** | 3m | 16 | +3.6% | +4.5% | -12.3% | +16.7% | 75% |
| **SPY** | 6m | 16 | +7.3% | +8.3% | -13.5% | +21.9% | 81% |
| **USO** | 1m | 16 | +1.8% | -3.2% | -13.0% | +27.7% | 38% |
| **USO** | 3m | 16 | +3.2% | -1.7% | -14.5% | +29.9% | 38% |
| **USO** | 6m | 16 | +13.9% | +2.3% | -12.4% | +103.5% | 69% |
| **GLD** | 1m | 16 | +2.4% | +1.8% | -6.4% | +9.0% | 75% |
| **GLD** | 3m | 16 | +6.9% | +7.4% | -6.5% | +23.6% | 69% |
| **GLD** | 6m | 16 | +11.7% | +12.1% | -8.4% | +43.8% | 75% |
| **TLT** | 1m | 16 | +0.6% | +0.7% | -6.1% | +8.5% | 56% |
| **TLT** | 3m | 16 | -0.7% | -0.3% | -14.7% | +13.0% | 50% |
| **TLT** | 6m | 16 | -2.9% | -1.7% | -20.6% | +8.6% | 44% |

**Episodes (последни 5 от 16):**
- `2025-03-27 → 2025-05-08` (25d)
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-17 → 2026-04-23` (4d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 18 · **Total matching days:** 289 · **History:** 2021-05-17 → 2026-05-21

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 18 | +0.4% | +1.1% | -8.3% | +7.0% | 50% |
| **SPY** | 3m | 18 | +2.3% | +3.5% | -13.3% | +9.4% | 67% |
| **SPY** | 6m | 18 | +3.8% | +7.4% | -15.7% | +17.6% | 72% |
| **USO** | 1m | 18 | +0.6% | -3.7% | -14.3% | +55.8% | 44% |
| **USO** | 3m | 18 | +4.5% | -1.0% | -12.7% | +78.8% | 44% |
| **USO** | 6m | 18 | +10.0% | -0.1% | -16.0% | +78.8% | 50% |
| **GLD** | 1m | 18 | -0.3% | +0.0% | -12.4% | +7.6% | 50% |
| **GLD** | 3m | 18 | +1.9% | +1.5% | -13.4% | +19.0% | 67% |
| **GLD** | 6m | 18 | +8.4% | +6.0% | -15.8% | +55.5% | 72% |
| **TLT** | 1m | 18 | +0.1% | +0.3% | -5.5% | +5.5% | 56% |
| **TLT** | 3m | 18 | -2.9% | -4.0% | -16.8% | +9.8% | 39% |
| **TLT** | 6m | 18 | -5.5% | -5.7% | -20.5% | +6.7% | 28% |

**Episodes (последни 5 от 18):**
- `2024-10-10 → 2025-01-17` (52d)
- `2025-05-12 → 2025-05-19` (3d)
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-05-21

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

**Дата:** 2026-05-16 00:00:00 · **Generated:** 2026-05-16 15:46:20.874509+00:00

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

**Дата:** 2026-05-16 00:00:00 · **Generated:** 2026-05-16 16:03:46.744213+00:00

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

### US (period: 2026-05-15 → 2026-05-20)

**stable_winner (1m):** +9 entered, -11 exited
  - **Entered:** ADM, CBOE, COHR, CVNA, GS, HST, STLD, STX, WDC _(включително 4 за първи път в историята: CBOE, COHR, STX, WDC)_
  - **Exited:** CBRE, DG, GEV, GILD, HII, IBKR, LHX, LITE, RTX, SPG, WELL

**stable_winner (3m):** +6 entered, -3 exited
  - **Entered:** COHR, GS, HST, LVS, MS, STLD _(включително 2 за първи път в историята: COHR, LVS)_
  - **Exited:** HAS, LLY, WELL

**quality_dip (1m):** +11 entered, -9 exited
  - **Entered:** CBRE, DG, GEV, GILD, HII, IBKR, LHX, LITE, RTX, SPG, WELL _(включително 2 за първи път в историята: GEV, RTX)_
  - **Exited:** ADM, APH, CVNA, GS, HST, PM, STLD, STX, WDC

**quality_dip (3m):** +4 entered, -7 exited
  - **Entered:** CBOE, HAS, LLY, WELL _(включително 1 за първи път в историята: CBOE)_
  - **Exited:** APH, GS, HST, LVS, MS, PM, STLD

**faded_bounce (1m):** +13 entered, -6 exited
  - **Entered:** ADP, APO, BAX, CHTR, CMG, CPRT, CTAS, GDDY, IT, LEN, LII, PYPL, SW _(включително 3 за първи път в историята: BAX, CPRT, CTAS)_
  - **Exited:** DOW, DVA, GPN, IEX, PGR, STZ

**faded_bounce (3m):** +4 entered, -8 exited
  - **Entered:** ACN, APO, BAX, RVTY _(включително 1 за първи път в историята: BAX)_
  - **Exited:** AJG, BLDR, BRO, COO, CRM, IEX, KMB, WY

### EU (period: 2026-05-15 → 2026-05-20)

**stable_winner (1m):** +16 entered, -8 exited
  - **Entered:** AAF.L, AXFO.ST, BATS.L, CBK.DE, GBF.DE, GLE.PA, IG.MI, INGA.AS, KER.PA, KGH.WA, LPP.WA, SBRY.L, SPSN.SW, TPRO.MI, TSCO.L, WRT1V.HE _(включително 6 за първи път в историята: AXFO.ST, GLE.PA, INGA.AS, LPP.WA, SBRY.L, TSCO.L)_
  - **Exited:** AED.BR, ALLN.SW, BBY.L, BCP.LS, BIRG.IR, BMED.MI, LTMC.MI, ORK.OL

**stable_winner (3m):** +2 entered, -4 exited
  - **Entered:** LPP.WA, VOE.VI _(включително 1 за първи път в историята: LPP.WA)_
  - **Exited:** ALLN.SW, BMW.DE, EBS.VI, NDX1.DE

**quality_dip (1m):** +7 entered, -16 exited
  - **Entered:** AED.BR, ALLN.SW, BBY.L, BCP.LS, BIRG.IR, BMED.MI, LTMC.MI _(включително 1 за първи път в историята: ALLN.SW)_
  - **Exited:** AAF.L, AXFO.ST, BATS.L, CBK.DE, GBF.DE, GLE.PA, HAG.DE, IG.MI, INGA.AS, KER.PA, KGH.WA, SBRY.L, SPSN.SW, TPRO.MI, TSCO.L, WRT1V.HE

**quality_dip (3m):** +4 entered, -3 exited
  - **Entered:** ALLN.SW, BMW.DE, EBS.VI, NDX1.DE _(включително 2 за първи път в историята: ALLN.SW, NDX1.DE)_
  - **Exited:** HAG.DE, ORK.OL, VOE.VI

**faded_bounce (1m):** +17 entered, -14 exited
  - **Entered:** BALD-B.ST, CVC.AS, EQT.ST, EVK.DE, EXO.AS, EXPN.L, GF.SW, LUND-B.ST, PGHN.SW, RAND.AS, ROCK-B.CO, SAGA-B.ST, SGO.PA, SIGN.SW, VNA.DE, WKL.AS, ZURN.SW _(включително 4 за първи път в историята: EVK.DE, EXO.AS, EXPN.L, VNA.DE)_
  - **Exited:** BAKKA.OL, BC.MI, BEI.DE, EQNR.OL, EZJ.L, GFC.PA, HNR1.DE, ICG.L, KRZ.IR, NIBE-B.ST, PNDORA.CO, RMV.L, UTG.L, WPP.L

**faded_bounce (3m):** +5 entered, -5 exited
  - **Entered:** EVK.DE, PGHN.SW, SREN.SW, WKL.AS, ZURN.SW _(включително 3 за първи път в историята: EVK.DE, WKL.AS, ZURN.SW)_
  - **Exited:** AALB.AS, ENX.PA, HNR1.DE, SFSN.SW, VER.VI



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
| 1 | **SNDK** | Technology | 96.7 | 54.1% | 124.2% | 423.8% | 3490.9% | 3.71 | -31.3% |
| 2 | **MU** | Technology | 96.5 | 62.9% | 75.5% | 202.8% | 643.8% | 3.14 | -30.3% |
| 3 | **INTC** | Technology | 96.2 | 79.5% | 166.6% | 242.7% | 456.4% | 2.40 | -24.2% |
| 4 | **STX** | Technology | 95.8 | 34.1% | 84.0% | 188.6% | 597.7% | 3.10 | -21.0% |
| 5 | **AMD** | Technology | 95.6 | 57.3% | 120.1% | 86.1% | 290.1% | 2.09 | -27.8% |
| 6 | **WDC** | Technology | 94.7 | 19.8% | 61.5% | 183.3% | 810.1% | 3.50 | -20.6% |
| 7 | **ON** | Technology | 93.4 | 26.8% | 61.9% | 139.5% | 151.4% | 1.67 | -28.1% |
| 8 | **CIEN** | Technology | 93.2 | 9.7% | 74.2% | 189.3% | 585.0% | 2.94 | -16.8% |
| 9 | **DELL** | Technology | 92.0 | 14.4% | 104.7% | 99.8% | 115.8% | 1.41 | -32.3% |
| 10 | **GLW** | Technology | 91.7 | 9.2% | 39.3% | 123.3% | 281.1% | 2.52 | -23.0% |
| 11 | **CSCO** | Technology | 91.6 | 27.5% | 46.4% | 48.6% | 83.0% | 1.92 | -13.6% |
| 12 | **FIX** | Industrials | 91.1 | 9.7% | 33.8% | 99.7% | 291.2% | 2.56 | -13.8% |
| 13 | **COHR** | Technology | 91.0 | 4.3% | 54.2% | 157.8% | 351.6% | 2.10 | -26.5% |
| 14 | **HPE** | Technology | 90.8 | 17.5% | 59.0% | 61.2% | 98.5% | 1.61 | -23.7% |
| 15 | **LRCX** | Technology | 90.6 | 13.1% | 23.2% | 98.6% | 251.0% | 2.45 | -20.0% |
| 16 | **TXN** | Technology | 90.6 | 31.4% | 40.5% | 99.0% | 66.4% | 1.23 | -29.6% |
| 17 | **LITE** | Technology | 90.3 | 3.7% | 36.6% | 258.6% | 1014.8% | 2.88 | -28.7% |
| 18 | **PWR** | Industrials | 90.1 | 17.2% | 28.2% | 66.4% | 106.2% | 1.91 | -11.7% |
| 19 | **GOOGL** | Communication Services | 89.7 | 17.0% | 28.5% | 36.6% | 134.3% | 2.81 | -20.4% |
| 20 | **SATS** | Communication Services | 89.3 | 14.5% | 23.5% | 111.9% | 544.5% | 1.96 | -34.1% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **NOKIA.HE** | Technology | 94.7 | 36.3% | 97.7% | 100.5% | 161.2% | 2.10 | -27.6% |
| 2 | **TPRO.MI** | Technology | 94.5 | 63.8% | 65.5% | 158.2% | 313.5% | 2.36 | -27.0% |
| 3 | **STMMI.MI** | Technology | 94.0 | 48.2% | 100.1% | 169.8% | 144.2% | 1.79 | -33.5% |
| 4 | **AIXA.DE** | Technology | 93.6 | 21.3% | 124.9% | 197.0% | 320.2% | 2.32 | -28.4% |
| 5 | **PRY.MI** | Industrials | 93.1 | 19.9% | 47.4% | 72.2% | 159.6% | 2.51 | -11.9% |
| 6 | **HUBN.SW** | Industrials | 92.8 | 18.4% | 44.1% | 78.8% | 235.5% | 3.05 | -13.5% |
| 7 | **IFX.DE** | Technology | 92.7 | 41.6% | 53.6% | 89.0% | 97.6% | 1.59 | -21.2% |
| 8 | **BESI.AS** | Technology | 91.8 | 17.5% | 48.1% | 104.8% | 153.2% | 1.82 | -20.9% |
| 9 | **SUBC.OL** | Energy | 91.5 | 17.6% | 33.9% | 76.9% | 111.6% | 2.61 | -11.3% |
| 10 | **NESTE.HE** | Energy | 91.4 | 21.1% | 39.5% | 56.9% | 208.1% | 2.61 | -20.4% |
| 11 | **SPM.MI** | Energy | 90.9 | 13.5% | 33.9% | 94.8% | 116.6% | 2.39 | -14.7% |
| 12 | **UMI.BR** | Basic Materials | 90.9 | 42.1% | 37.1% | 48.9% | 177.8% | 2.07 | -28.7% |
| 13 | **PKN.WA** | Energy | 88.8 | 14.1% | 36.6% | 40.6% | 118.3% | 2.47 | -11.9% |
| 14 | **ENI.MI** | Energy | 88.2 | 6.8% | 32.8% | 48.7% | 89.8% | 2.69 | -12.6% |
| 15 | **NKT.CO** | Industrials | 88.2 | 15.6% | 28.1% | 52.7% | 109.1% | 1.98 | -14.8% |
| 16 | **HOT.DE** | Industrials | 88.0 | 5.8% | 26.8% | 68.8% | 193.4% | 2.54 | -15.9% |
| 17 | **VAR.OL** | Energy | 88.0 | 15.6% | 43.0% | 47.8% | 83.5% | 1.65 | -17.4% |
| 18 | **IGG.L** | Financial Services | 87.7 | 17.5% | 32.6% | 66.7% | 60.1% | 1.80 | -11.5% |
| 19 | **REP.MC** | Energy | 87.3 | 12.0% | 31.6% | 37.4% | 110.7% | 2.46 | -20.4% |
| 20 | **NHY.OL** | Basic Materials | 87.1 | 7.2% | 28.5% | 53.6% | 91.2% | 2.28 | -11.5% |



---

## 12. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **APA** | Energy | 0.791 | 0.941 | 0.761 | 0.860 | 0.439 | +137.0% | 8.9 | +26.2% |
| 2 | **SNDK** | Information Technology | 0.754 | 0.999 | 0.848 | 0.500 | 0.500 | +4036.9% | 52.7 | +39.3% |
| 3 | **CF** | Materials | 0.743 | 0.869 | 0.716 | 0.758 | 0.519 | +39.8% | 11.0 | +27.3% |
| 4 | **EOG** | Energy | 0.738 | 0.797 | 0.638 | 0.811 | 0.700 | +31.6% | 13.8 | +18.2% |
| 5 | **TROW** | Financials | 0.727 | 0.612 | 0.733 | 0.883 | 0.685 | +15.5% | 10.9 | +18.7% |
| 6 | **ANET** | Information Technology | 0.707 | 0.822 | 0.868 | 0.500 | 0.500 | +62.9% | 51.1 | +31.5% |
| 7 | **FTNT** | Information Technology | 0.702 | 0.864 | 0.884 | 0.500 | 0.351 | +25.5% | 50.4 | +132.4% |
| 8 | **BMY** | Health Care | 0.700 | 0.682 | 0.765 | 0.719 | 0.573 | +33.5% | 16.7 | +38.7% |
| 9 | **NEM** | Materials | 0.693 | 0.625 | 0.862 | 0.699 | 0.485 | +104.5% | 14.1 | +25.8% |
| 10 | **PFG** | Financials | 0.692 | 0.779 | 0.500 | 0.785 | 0.745 | +40.2% | 14.9 | +13.4% |
| 11 | **HST** | Real Estate | 0.688 | 0.828 | 0.534 | 0.741 | 0.630 | +61.0% | 15.2 | +14.9% |
| 12 | **FFIV** | Information Technology | 0.688 | 0.883 | 0.661 | 0.500 | 0.666 | +36.0% | 31.6 | +20.3% |
| 13 | **CBOE** | Financials | 0.686 | 0.867 | 0.788 | 0.284 | 0.788 | +52.8% | 30.1 | +25.1% |
| 14 | **SPG** | Real Estate | 0.682 | 0.680 | 0.891 | 0.540 | 0.507 | +37.2% | 14.2 | +113.6% |
| 15 | **GL** | Financials | 0.682 | 0.733 | 0.500 | 0.745 | 0.838 | +32.3% | 10.8 | +20.5% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **NRG** | Utilities | 0.133 | 0.142 | 0.115 | 0.140 | 0.142 |
| 502 | **BLDR** | Industrials | 0.213 | 0.048 | 0.172 | 0.500 | 0.145 |
| 501 | **CSGP** | Real Estate | 0.226 | 0.013 | 0.107 | 0.500 | 0.436 |
| 500 | **GPC** | Consumer Discretionary | 0.238 | 0.132 | 0.111 | 0.495 | 0.274 |
| 499 | **AXON** | Industrials | 0.242 | 0.142 | 0.130 | 0.500 | 0.236 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W21.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W21.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-05-18  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
