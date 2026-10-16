# Сателит — пълен data export за 2026-W42

_Период: 2026-10-12 → 2026-10-18_  
_Генериран: 2026-10-16 10:52 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W42.md` (structured briefing) и `narrative_2026-W42.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**16 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **TLT** | +2.55% | +2.84σ | 77.98 | 79.97 | 2026-10-09 | 2026-10-15 | -0.61% | +1.11% | 13 |
| **TIP** | +0.83% | +2.76σ | 104.42 | 105.29 | 2026-10-09 | 2026-10-15 | -0.27% | +0.40% | 13 |
| **XLP** | +3.90% | +2.75σ | 83.43 | 86.68 | 2026-10-09 | 2026-10-15 | -0.05% | +1.44% | 13 |
| **IEF** | +1.06% | +2.68σ | 89.40 | 90.35 | 2026-10-09 | 2026-10-15 | -0.35% | +0.53% | 13 |
| **EEM** | -4.25% | -2.14σ | 66.80 | 63.96 | 2026-10-09 | 2026-10-15 | +0.01% | +1.99% | 13 |
| **LQD** | +1.06% | +2.04σ | 102.41 | 103.50 | 2026-10-09 | 2026-10-15 | -0.37% | +0.70% | 13 |
| **XLK** | -4.82% | -1.84σ | 198.78 | 189.19 | 2026-10-09 | 2026-10-15 | +0.56% | +2.92% | 13 |
| **SOXX** | -7.99% | -1.59σ | 559.40 | 514.71 | 2026-10-09 | 2026-10-15 | -0.17% | +4.92% | 13 |
| **XLV** | +3.74% | +1.54σ | 170.81 | 177.19 | 2026-10-09 | 2026-10-15 | +0.49% | +2.11% | 13 |
| **QQQ** | -3.10% | -1.53σ | 751.27 | 728.00 | 2026-10-09 | 2026-10-15 | +0.29% | +2.22% | 13 |
| **XLB** | +2.29% | +1.26σ | 49.43 | 50.56 | 2026-10-09 | 2026-10-15 | -0.20% | +1.98% | 13 |
| **SLV** | -5.22% | -1.18σ | 54.78 | 51.92 | 2026-10-09 | 2026-10-15 | +0.22% | +4.63% | 13 |
| **URA** | -7.15% | -1.17σ | 38.90 | 36.12 | 2026-10-09 | 2026-10-15 | -0.61% | +5.56% | 13 |
| **VWO** | -1.62% | -1.07σ | 59.76 | 58.79 | 2026-10-09 | 2026-10-15 | -0.01% | +1.51% | 13 |
| **XLC** | +1.87% | +1.03σ | 110.38 | 112.44 | 2026-10-09 | 2026-10-15 | -0.07% | +1.89% | 13 |
| **SHY** | +0.11% | +1.03σ | 81.20 | 81.29 | 2026-10-09 | 2026-10-15 | -0.06% | +0.17% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-10-18 · **Conditions matched:** 2/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | +6.15% | ✅ | 148.20 | 157.31 | 2026-10-09 | 2026-10-15 |
| DFEN | down ≥ 3.0% | -0.09% | ❌ | 46.63 | 46.59 | 2026-10-09 | 2026-10-15 |
| GLD | down ≥ 1.0% | -0.49% | ❌ | 384.58 | 382.71 | 2026-10-09 | 2026-10-15 |
| URA | down ≥ 3.0% | -7.15% | ✅ | 38.90 | 36.12 | 2026-10-09 | 2026-10-15 |
| UUP | up ≥ 0.5% | -0.07% | ❌ | 29.02 | 29.00 | 2026-10-09 | 2026-10-15 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-10-18 · **Conditions matched:** 0/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | -1.38% | ❌ | 278.94 | 275.08 | 2026-10-09 | 2026-10-15 |
| XLF | up ≥ 1.0% | +0.99% | ❌ | 54.73 | 55.27 | 2026-10-09 | 2026-10-15 |
| XLY | up ≥ 1.0% | +0.50% | ❌ | 112.85 | 113.41 | 2026-10-09 | 2026-10-15 |
| GLD | down ≥ 0.5% | -0.49% | ❌ | 384.58 | 382.71 | 2026-10-09 | 2026-10-15 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2023-W14 (week ending 2023-04-09)
**Cosine similarity:** 0.8350 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.43% | +7.18% | +4.97% |
| **USO** | -7.67% | -6.28% | +5.55% |
| **GLD** | +1.36% | -4.21% | -9.00% |
| **TLT** | -5.05% | -8.71% | -21.87% |
| **XLE** | -5.55% | -4.93% | +0.88% |
| **IWM** | -0.21% | +6.22% | -0.51% |

### Паралел #2: 2022-W09 (week ending 2022-03-06)
**Cosine similarity:** 0.7881 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.36% | -5.00% | -9.24% |
| **USO** | -5.86% | +12.60% | -10.11% |
| **GLD** | -2.42% | -6.04% | -13.29% |
| **TLT** | -8.38% | -17.26% | -21.41% |
| **XLE** | +0.96% | +18.98% | +6.29% |
| **IWM** | +2.18% | -5.84% | -9.35% |

### Паралел #3: 2021-W30 (week ending 2021-08-01)
**Cosine similarity:** 0.7753 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.98% | +4.73% | +0.78% |
| **USO** | -5.17% | +12.81% | +22.33% |
| **GLD** | -0.08% | -1.87% | -1.60% |
| **TLT** | -0.46% | -1.22% | -4.27% |
| **XLE** | -2.00% | +16.36% | +32.88% |
| **IWM** | +2.20% | +3.17% | -11.67% |

### Паралел #4: 2025-W16 (week ending 2025-04-20)
**Cosine similarity:** 0.7675 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +12.62% | +19.22% | +26.21% |
| **USO** | -1.18% | +9.28% | -2.16% |
| **GLD** | -0.83% | +0.74% | +27.07% |
| **TLT** | -2.40% | -2.62% | +4.19% |
| **XLE** | +2.56% | +5.47% | +5.50% |
| **IWM** | +12.12% | +19.22% | +30.53% |

### Паралел #5: 2022-W50 (week ending 2022-12-18)
**Cosine similarity:** 0.7627 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.78% | +1.75% | +14.66% |
| **USO** | +9.18% | -9.61% | -0.85% |
| **GLD** | +6.48% | +10.18% | +8.90% |
| **TLT** | -0.98% | -0.24% | -4.21% |
| **XLE** | +6.85% | -8.76% | -4.15% |
| **IWM** | +7.14% | -1.80% | +6.64% |

### Паралел #6: 2026-W05 (week ending 2026-02-01)
**Cosine similarity:** 0.7555 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.68% | +4.14% | +7.96% |
| **USO** | +13.43% | +79.58% | +62.44% |
| **GLD** | +5.21% | -4.89% | -16.50% |
| **TLT** | +2.64% | -1.74% | -5.60% |
| **XLE** | +10.71% | +15.28% | +16.65% |
| **IWM** | -0.16% | +7.56% | +12.15% |

### Паралел #7: 2023-W37 (week ending 2023-09-17)
**Cosine similarity:** 0.7478 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.66% | +5.86% | +14.99% |
| **USO** | -3.06% | -17.39% | -6.10% |
| **GLD** | -0.03% | +4.86% | +11.98% |
| **TLT** | -8.29% | +6.66% | -0.02% |
| **XLE** | -0.96% | -8.38% | -0.49% |
| **IWM** | -4.72% | +7.31% | +10.24% |

### Паралел #8: 2025-W01 (week ending 2025-01-05)
**Cosine similarity:** 0.7406 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.66% | -14.64% | +5.64% |
| **USO** | -0.53% | -12.83% | -3.50% |
| **GLD** | +7.81% | +14.88% | +26.14% |
| **TLT** | +1.31% | +6.37% | -0.37% |
| **XLE** | +2.94% | -9.96% | -0.50% |
| **IWM** | +1.11% | -19.27% | -0.60% |

### Паралел #9: 2022-W44 (week ending 2022-11-06)
**Cosine similarity:** 0.7394 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.64% | +9.57% | +9.64% |
| **USO** | -15.09% | -16.17% | -17.95% |
| **GLD** | +5.35% | +10.86% | +19.81% |
| **TLT** | +13.51% | +13.25% | +11.32% |
| **XLE** | -6.67% | -5.97% | -12.24% |
| **IWM** | +0.78% | +10.25% | -2.37% |

### Паралел #10: 2021-W37 (week ending 2021-09-19)
**Cosine similarity:** 0.7233 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.09% | +4.18% | +0.71% |
| **USO** | +14.11% | +0.91% | +48.33% |
| **GLD** | +1.03% | +2.46% | +9.48% |
| **TLT** | -3.67% | +1.11% | -10.55% |
| **XLE** | +17.64% | +10.24% | +49.80% |
| **IWM** | +1.52% | -3.30% | -6.84% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 15 · **Total matching days:** 88 · **History:** 2021-05-17 → 2026-10-15

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 15 | +2.2% | +2.7% | -3.1% | +7.4% | 73% |
| **SPY** | 3m | 15 | +2.8% | +2.5% | -7.3% | +12.0% | 80% |
| **SPY** | 6m | 15 | +7.3% | +8.6% | -6.8% | +21.8% | 80% |
| **USO** | 1m | 15 | +0.1% | -0.8% | -14.3% | +12.7% | 47% |
| **USO** | 3m | 15 | -0.2% | -0.7% | -18.9% | +26.9% | 47% |
| **USO** | 6m | 15 | +14.6% | +4.1% | -8.7% | +109.4% | 60% |
| **GLD** | 1m | 15 | +2.7% | +0.9% | -3.0% | +9.0% | 73% |
| **GLD** | 3m | 15 | +4.9% | +3.9% | -12.6% | +24.5% | 67% |
| **GLD** | 6m | 15 | +5.6% | +4.5% | -12.5% | +25.3% | 67% |
| **TLT** | 1m | 15 | -1.6% | -1.1% | -6.7% | +3.6% | 33% |
| **TLT** | 3m | 15 | -0.8% | -0.5% | -16.5% | +11.1% | 47% |
| **TLT** | 6m | 15 | -4.5% | -5.4% | -18.0% | +7.5% | 27% |

**Episodes (последни 5 от 15):**
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-08-03` (5d)
- `2026-09-10 → 2026-10-01` (14d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 108 · **History:** 2021-05-17 → 2026-10-15

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +6.3% | +6.3% | +3.5% | +9.1% | 100% |
| **SPY** | 3m | 2 | +6.9% | +6.9% | +3.5% | +10.3% | 100% |
| **SPY** | 6m | 2 | +8.8% | +8.8% | +2.7% | +15.0% | 100% |
| **USO** | 1m | 2 | +5.6% | +5.6% | +4.0% | +7.2% | 100% |
| **USO** | 3m | 2 | +8.7% | +8.7% | -9.9% | +27.4% | 50% |
| **USO** | 6m | 2 | +23.2% | +23.2% | +15.5% | +30.9% | 100% |
| **GLD** | 1m | 2 | +3.5% | +3.5% | -0.2% | +7.2% | 50% |
| **GLD** | 3m | 2 | -5.6% | -5.6% | -13.8% | +2.6% | 50% |
| **GLD** | 6m | 2 | -5.3% | -5.3% | -13.5% | +2.8% | 50% |
| **TLT** | 1m | 2 | -1.4% | -1.4% | -1.8% | -1.0% | 0% |
| **TLT** | 3m | 2 | -4.9% | -4.9% | -6.8% | -2.9% | 0% |
| **TLT** | 6m | 2 | -8.1% | -8.1% | -11.2% | -4.9% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-10-15` (61d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 464 · **History:** 2021-05-17 → 2026-10-15

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
- `2025-11-03 → 2026-10-15` (232d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 1 · **Total matching days:** 1 · **History:** 2021-05-17 → 2026-10-15

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | +0.1% | +0.1% | +0.1% | +0.1% | 100% |
| **SPY** | 3m | 1 | +0.1% | +0.1% | +0.1% | +0.1% | 100% |
| **SPY** | 6m | 1 | +0.1% | +0.1% | +0.1% | +0.1% | 100% |
| **USO** | 1m | 1 | +6.1% | +6.1% | +6.1% | +6.1% | 100% |
| **USO** | 3m | 1 | +6.1% | +6.1% | +6.1% | +6.1% | 100% |
| **USO** | 6m | 1 | +6.1% | +6.1% | +6.1% | +6.1% | 100% |
| **GLD** | 1m | 1 | -2.7% | -2.7% | -2.7% | -2.7% | 0% |
| **GLD** | 3m | 1 | -2.7% | -2.7% | -2.7% | -2.7% | 0% |
| **GLD** | 6m | 1 | -2.7% | -2.7% | -2.7% | -2.7% | 0% |
| **TLT** | 1m | 1 | +0.8% | +0.8% | +0.8% | +0.8% | 100% |
| **TLT** | 3m | 1 | +0.8% | +0.8% | +0.8% | +0.8% | 100% |
| **TLT** | 6m | 1 | +0.8% | +0.8% | +0.8% | +0.8% | 100% |

**Episodes (последни 5 от 1):**
- `2026-09-25 → 2026-09-25` (1d)

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 10 · **Total matching days:** 101 · **History:** 2021-05-17 → 2026-10-15

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 10 | -0.1% | +0.6% | -7.2% | +7.8% | 60% |
| **SPY** | 3m | 10 | +2.0% | +2.3% | -8.3% | +11.6% | 60% |
| **SPY** | 6m | 10 | +1.3% | +3.7% | -20.8% | +14.2% | 70% |
| **USO** | 1m | 10 | +4.1% | +0.5% | -15.0% | +52.9% | 50% |
| **USO** | 3m | 10 | +10.7% | +11.3% | -20.7% | +52.2% | 60% |
| **USO** | 6m | 10 | +12.7% | +8.0% | -27.6% | +56.3% | 60% |
| **GLD** | 1m | 10 | -1.2% | -1.9% | -8.3% | +11.7% | 20% |
| **GLD** | 3m | 10 | -1.4% | -1.3% | -12.0% | +6.4% | 50% |
| **GLD** | 6m | 10 | -0.6% | -2.2% | -15.2% | +25.0% | 40% |
| **TLT** | 1m | 10 | -2.4% | -2.7% | -6.0% | +2.5% | 10% |
| **TLT** | 3m | 10 | -6.2% | -4.9% | -17.6% | +4.2% | 20% |
| **TLT** | 6m | 10 | -9.7% | -8.1% | -22.3% | +1.2% | 10% |

**Episodes (последни 5 от 10):**
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-05-19` (36d)
- `2026-07-22 → 2026-08-03` (8d)
- `2026-09-01 → 2026-09-28` (15d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 17 · **Total matching days:** 294 · **History:** 2021-05-17 → 2026-10-15

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 17 | +1.9% | +1.6% | -4.8% | +9.0% | 71% |
| **SPY** | 3m | 17 | +3.1% | +4.2% | -12.6% | +16.2% | 71% |
| **SPY** | 6m | 17 | +6.5% | +8.9% | -14.0% | +21.0% | 76% |
| **USO** | 1m | 17 | +2.4% | -2.2% | -13.0% | +22.9% | 41% |
| **USO** | 3m | 17 | +3.9% | -0.8% | -14.5% | +33.3% | 41% |
| **USO** | 6m | 17 | +14.5% | +2.6% | -12.4% | +87.1% | 71% |
| **GLD** | 1m | 17 | +2.4% | +2.1% | -5.6% | +9.0% | 76% |
| **GLD** | 3m | 17 | +5.7% | +7.2% | -16.8% | +23.6% | 65% |
| **GLD** | 6m | 17 | +10.2% | +9.8% | -13.4% | +43.8% | 71% |
| **TLT** | 1m | 17 | +0.3% | -0.0% | -6.3% | +8.2% | 47% |
| **TLT** | 3m | 17 | -1.7% | -1.7% | -15.3% | +11.9% | 35% |
| **TLT** | 6m | 17 | -4.7% | -3.4% | -21.3% | +7.0% | 35% |

**Episodes (последни 5 от 17):**
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)
- `2026-08-07 → 2026-09-03` (19d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 20 · **Total matching days:** 304 · **History:** 2021-05-17 → 2026-10-15

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 20 | +0.3% | +0.5% | -8.7% | +7.0% | 50% |
| **SPY** | 3m | 20 | +2.0% | +3.2% | -13.7% | +9.1% | 65% |
| **SPY** | 6m | 20 | +3.2% | +5.7% | -16.4% | +16.9% | 70% |
| **USO** | 1m | 20 | -0.3% | -3.7% | -21.8% | +55.8% | 45% |
| **USO** | 3m | 20 | +4.0% | +1.5% | -12.7% | +64.3% | 50% |
| **USO** | 6m | 20 | +9.2% | +5.1% | -16.0% | +75.1% | 55% |
| **GLD** | 1m | 20 | -0.7% | -0.2% | -12.4% | +7.6% | 45% |
| **GLD** | 3m | 20 | +1.6% | +1.5% | -13.7% | +19.0% | 65% |
| **GLD** | 6m | 20 | +7.2% | +4.3% | -15.8% | +55.5% | 65% |
| **TLT** | 1m | 20 | -0.3% | -0.1% | -5.6% | +5.2% | 45% |
| **TLT** | 3m | 20 | -3.6% | -3.9% | -17.3% | +8.7% | 30% |
| **TLT** | 6m | 20 | -6.7% | -6.7% | -21.4% | +4.6% | 20% |

**Episodes (последни 5 от 20):**
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (13d)
- `2026-09-21 → 2026-10-15` (16d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-10-15

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (8 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **COMPUTSA** | Завършени жилища (SAAR) | growth | housing_supply | 6 | 2.80 | 2.95 | 2026-09-12 00:00:00 | 2026-10-10 00:00:00 | ✓ |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 6 | 2.75 | 2.75 | 2026-09-12 00:00:00 | 2026-10-10 00:00:00 | ✓ |
| **JTSQUR** | Quits rate — напускания | labor | flow | 6 | 2.02 | 2.02 | 2026-09-12 00:00:00 | 2026-10-10 00:00:00 | ✓ |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 4 | 2.11 | 2.25 | 2026-09-12 00:00:00 | 2026-10-10 00:00:00 | - |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | 3 | 2.25 | 2.25 | 2026-09-12 00:00:00 | 2026-09-26 00:00:00 | - |
| **US_PMI_COMPOSITE** | S&P Global US Composite PMI | growth | diffusion_indices | 2 | 2.60 | 2.60 | 2026-10-07 00:00:00 | 2026-10-10 00:00:00 | ✓ |
| **US_PMI_SVCS** | S&P Global US Services PMI | growth | diffusion_indices | 2 | 2.09 | 2.09 | 2026-10-07 00:00:00 | 2026-10-10 00:00:00 | ✓ |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 2 | 2.07 | 2.07 | 2026-10-07 00:00:00 | 2026-10-10 00:00:00 | ✓ |

### EU (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.41 | 5.60 | 2026-09-12 00:00:00 | 2026-10-10 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.18 | 2.18 | 2026-09-12 00:00:00 | 2026-10-10 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.14 | 2.14 | 2026-09-12 00:00:00 | 2026-10-10 00:00:00 | ✓ |

### CN (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 9 | 2.54 | 2.55 | 2026-09-14 00:00:00 | 2026-10-12 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 9 | 2.22 | 2.23 | 2026-09-14 00:00:00 | 2026-10-12 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 4 | 2.19 | 2.19 | 2026-09-14 00:00:00 | 2026-10-12 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-10-10 00:00:00 · **Generated:** 2026-10-10 08:29:59.207902+00:00

**Режим:** `policy_dilemma` (Policy dilemma)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 39.8 | mixed | 33.3% | 2 | 2 |
| **growth** | 49.3 | mixed | 56.0% | 4 | 4 |
| **inflation** | 41.7 | mixed | 38.9% | 1 | 1 |
| **liquidity** | 44.9 | mixed | 36.8% | 0 | 0 |

### Top anomalies (7 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **COMPUTSA** | Завършени жилища (SAAR) | growth, housing | housing_supply | -2.95 | down | -27.13 | 2026-08-01 | ✓ min |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.75 | down | 93.45 | 2026-04-01 | ✓ min |
| **US_PMI_COMPOSITE** | S&P Global US Composite PMI | growth | diffusion_indices | +2.60 | up | 58.40 | 2026-09-01 | ✓ max |
| **US_PMI_SVCS** | S&P Global US Services PMI | growth | diffusion_indices | +2.09 | up | 58.80 | 2026-09-01 | ✓ max |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | +2.07 | up | 55.90 | 2026-09-01 | ✓ max |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | -2.06 | down | 2.57 | 2026-07-01 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | -2.02 | down | 1.90 | 2026-08-01 | ✓ min |

### Narrative hints от макро лещите
- **COMPUTSA**: Завършва construction pipeline (12-18m след starts). Превишение спрямо sales = inventory build.
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **US_PMI_COMPOSITE**: Markit композит — global benchmark, complement към ISM. Flash + final estimates.
- **US_PMI_SVCS**: Markit services — global comparable. ISM Services има различна methodology.
- **US_PMI_MFG**: Markit mfg — comparable cross-country. ISM е US-only.
- **HPIPONM226S**: Monthly FHFA версия. Само purchase transactions (без refi appraisals). По-чист от refi-bias.
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
  - `breadth_b`: 0.667
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
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.8
  - `breadth_b_raw`: 0.667
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Realized CPI × Expectations
  - `question_bg`: Дали expectations следват realized inflation, или стоят anchored?
  - `state`: a_up_b_down
  - `interpretation`: Anchored — realized hot, expectations stable. Credibility holds.
  - `slot_a_label`: Realized inflation
  - `slot_b_label`: Inflation expectations
  - `breadth_a`: 0.667
  - `breadth_b`: 0.0
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.0
- 🔔 **?**
  - `pair_id`: credit_policy_transmission
  - `name_bg`: Credit spreads × Policy rates
  - `question_bg`: Дали credit следва policy направление — transmission intact?
  - `state`: transition
  - `interpretation`: Mixed transmission.
  - `slot_a_label`: Credit stress
  - `slot_b_label`: Policy tightening
  - `breadth_a`: 0.5
  - `breadth_b`: 0.667
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
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
  - `breadth_b`: 0.6
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.0
  - `breadth_b_raw`: 0.8
- 🔔 **?**
  - `pair_id`: model_vs_market
  - `name_bg`: Model-implied × Market-implied inflation
  - `question_bg`: Дали underlying persistence и market pricing-а са съгласни за инфлацията?
  - `state`: both_down
  - `interpretation`: Съгласие — disinflation confirmation. Converging view.
  - `slot_a_label`: Модел (sticky inflation)
  - `slot_b_label`: Пазар (breakevens + survey)
  - `breadth_a`: 0.0
  - `breadth_b`: 0.0
  - `state_raw`: both_down
  - `breadth_a_raw`: 0.0
  - `breadth_b_raw`: 0.0

### Executive narrative
> Policy dilemma — labor market е loose, но инфлацията remains hot. Fed е заклещен между двата мандата. Най-отклонена леща: Инфлация и цени — breadth 64% (разширяване), 1 аномалии, 1 нови екстремума. Обаче inflation expectations остават anchored — Fed narrative-ът за момента държи. За наблюдение следващия релиз: COMPUTSA, LABOR_SHARE_NBS, US_PMI_COMPOSITE (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: COMPUTSA z=-2.95 · NEW-5Y-MIN
- 6 нови екстремуми в top-7 (lookback 5г.)
- Активни двойки: Stagflation test=a_down_b_up; Inflation anchoring=a_up_b_down; model_vs_market=both_down



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-10-10 00:00:00 · **Generated:** 2026-10-10 08:58:34.337160+00:00

**Режим:** `policy_dilemma` (Policy dilemma)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 41.1 | mixed | 42.9% | 0 | 0 |
| **growth** | 45.3 | mixed | 25.0% | 0 | 0 |
| **inflation** | 43.4 | mixed | 42.9% | 0 | 0 |
| **credit** | 44.2 | mixed | 36.8% | 3 | 2 |
| **external** | 61.6 | mixed | 33.3% | 0 | 0 |

### Top anomalies (3 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | +5.60 | up | 3.30 | 2026-09-01 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | +2.18 | up | 4.00 | 2026-08-01 | ✓ max |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | +2.14 | up | 3.19 | 2026-08-01 | ✓ max |

### Narrative hints от макро лещите
- **EA_BUND_2Y**: EA-aggregate 2Y yield. Curve slope (10Y-2Y) проксира policy expectations и recession risk.
- **FR_10Y**: France sovereign yield — компонент на OAT-Bund spread. Core-but-not-DE EA stress indicator.
- **DE_10Y**: Germany 10Y, Maastricht-criterion measure. Reference за BTP-Bund / OAT-Bund spread изчисления.

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
  - `state`: a_up_b_down
  - `interpretation`: Hike-ове + сжимащи се spreads — smooth transmission, credible policy.
  - `slot_a_label`: Политика (реална лихва + баланс)
  - `slot_b_label`: Sovereign spreads (BTP/OAT-Bund)
  - `breadth_a`: 1.0
  - `breadth_b`: 0.2
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.2
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
  - `breadth_b`: 0.75
  - `state_raw`: transition
  - `breadth_a_raw`: 0.444
  - `breadth_b_raw`: 0.75
- 🔔 **?**
  - `pair_id`: growth_labor_lead_lag
  - `name_bg`: Растеж срещу труд (lead-lag)
  - `question_bg`: Активността и пазарът на труда движат ли се заедно?
  - `state`: transition
  - `interpretation`: Смесена картина — изчакай alignment на двата блока.
  - `slot_a_label`: Твърда активност (IP, retail, GDP)
  - `slot_b_label`: Пазар на труда (сила)
  - `breadth_a`: 0.75
  - `breadth_b`: 0.5
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.75
  - `breadth_b_raw`: 0.75

### Executive narrative
> Policy dilemma — labor market е loose, но инфлацията remains hot. ЕЦБ е заклещена между инфлацията и растежа. Най-отклонена леща: Инфлация и цени — breadth 100% (разширяване), 0 аномалии, 0 нови екстремума. За наблюдение следващия релиз: FR_10Y, DE_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.60
- 2 нови екстремуми в top-3 (lookback 5г.)
- Активни двойки: Stagflation test=a_down_b_up; fragmentation_risk=a_up_b_down



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-10-12 00:00:00 · **Generated:** 2026-10-12 13:43:26.243919+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 42.1 | mixed | -% | - | - |
| **inflation** | 45.6 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 46.9 | mixed | -% | - | - |
| **property** | 29.5 | contracting | -% | - | - |

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
  - `state`: a_up_b_down
  - `interpretation`: Export-dependence — износът носи растежа, докато вътрешното търсене е слабо. Небалансирано възстановяване, уязвимо на тарифи/външни шокове.
  - `slot_a_label`: Външно търсене
  - `slot_b_label`: Вътрешна активност
  - `breadth_a`: 0.667
  - `breadth_b`: 0.333

### Executive narrative
> Претеглен композитен macro score 39.0/100 → режим „ВЛОШАВАЩ СЕ“ (5/5 лещи). 5 лещи, 3 flagged аномалии (3 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-10-09 |
| `as_of` | 2026-10-09 |
| `regime` | GROWTH |
| `alignment_score` | 4.0 |
| `gms_score` | 1.0 |
| `gms_max` | 8 |
| `gms_tier` | LOW |
| `ks_status` | inactive |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-10-09 → 2026-10-14)

**stable_winner (1m):** +7 entered, -10 exited
  - **Entered:** AES, APA, FITB, GL, PFG, PLD, SPG
  - **Exited:** EQIX, F, GEV, GOOG, GOOGL, MS, ROST, SNDK, STT, VLO

**stable_winner (3m):** +3 entered, -5 exited
  - **Entered:** CFG, FDX, HST
  - **Exited:** EQIX, ETR, GEV, PWR, SNDK

**quality_dip (1m):** +10 entered, -7 exited
  - **Entered:** EQIX, F, GEV, GOOG, GOOGL, MS, ROST, SNDK, STT, VLO _(включително 1 за първи път в историята: SNDK)_
  - **Exited:** AES, APA, FITB, GL, PFG, PLD, SPG

**quality_dip (3m):** +5 entered, -3 exited
  - **Entered:** EQIX, ETR, GEV, PWR, SNDK _(включително 1 за първи път в историята: SNDK)_
  - **Exited:** CFG, FDX, HST

**faded_bounce (1m):** +3 entered, -7 exited
  - **Entered:** AVY, BX, UBER
  - **Exited:** CCI, DPZ, NFLX, OKE, OTIS, SBAC, TAP

**faded_bounce (3m):** +8 entered, -5 exited
  - **Entered:** COIN, EFX, MOS, MRSH, NVR, PGR, PYPL, TAP _(включително 1 за първи път в историята: COIN)_
  - **Exited:** CEG, SBAC, SPGI, STZ, VST

### EU (period: 2026-10-09 → 2026-10-15)

**stable_winner (1m):** +9 entered, -18 exited
  - **Entered:** CCL.L, CPG.L, DLG.MI, ELE.MC, HSBA.L, LPP.WA, MBK.WA, SAND.ST, SWED-A.ST _(включително 1 за първи път в историята: CPG.L)_
  - **Exited:** AAF.L, ASML.AS, BATS.L, BG.VI, BIRG.IR, CABK.MC, EBS.VI, GL9.IR, HOC.L, IHG.L, KGH.WA, NKT.CO, NOKIA.HE, PAF.L, REP.MC, STMMI.MI, UNI.MC, WRT1V.HE

**stable_winner (3m):** +8 entered, -8 exited
  - **Entered:** AAF.L, ABI.BR, BBVA.MC, BEZ.L, EMG.L, HSBA.L, SDR.L, SPSN.SW _(включително 2 за първи път в историята: ABI.BR, SDR.L)_
  - **Exited:** GAW.L, HOC.L, INDU-C.ST, KGH.WA, NOKIA.HE, ORA.PA, SAND.ST, VACN.SW

**quality_dip (1m):** +20 entered, -10 exited
  - **Entered:** AAF.L, ABI.BR, ASML.AS, BG.VI, BIRG.IR, CABK.MC, CFR.SW, EBS.VI, GL9.IR, HOC.L, IHG.L, KGH.WA, NKT.CO, NOKIA.HE, PAF.L, REP.MC, STMMI.MI, SUBC.OL, UNI.MC, WRT1V.HE _(включително 3 за първи път в историята: ABI.BR, CFR.SW, STMMI.MI)_
  - **Exited:** CCL.L, CPG.L, DLG.MI, ELE.MC, HSBA.L, IG.MI, LPP.WA, MBK.WA, SAND.ST, SWED-A.ST

**quality_dip (3m):** +10 entered, -9 exited
  - **Entered:** CFR.SW, GAW.L, HOC.L, INDU-C.ST, KGH.WA, NOKIA.HE, ORA.PA, SAND.ST, SUBC.OL, VACN.SW _(включително 3 за първи път в историята: CFR.SW, KGH.WA, VACN.SW)_
  - **Exited:** AAF.L, BATS.L, BBVA.MC, BEZ.L, EMG.L, HSBA.L, IG.MI, SDR.L, SPSN.SW

**faded_bounce (1m):** +12 entered, -10 exited
  - **Entered:** ARCAD.AS, EVD.DE, G24.DE, ICG.L, MNDI.L, PGHN.SW, RED.MC, RMV.L, SCA-B.ST, SIKA.SW, SQN.SW, STLAM.MI
  - **Exited:** BEI.DE, CS.PA, DSFIR.AS, LIGHT.AS, ORSTED.CO, SAP.DE, SGE.L, TW.L, VEND.OL, VPK.AS

**faded_bounce (3m):** +7 entered, -6 exited
  - **Entered:** ADYEN.AS, BOL.PA, HNR1.DE, ICG.L, MUV2.DE, REL.L, RMV.L
  - **Exited:** BEIJ-B.ST, CMBN.SW, DSFIR.AS, EQT.ST, LIFCO-B.ST, RMS.PA



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-10-06 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **soymeal** | Commodities | 206804 | 99.9 | 99.9 | 1061 | 47246 |
| **soybeans** | Commodities | 251660 | 99.5 | 99.5 | 1061 | -14371 |
| **sugar** | Commodities | 257364 | 97.8 | 97.8 | 1061 | 10313 |
| **rbob** | Commodities | 96812 | 96.8 | 96.8 | 1061 | 3886 |
| **soyoil** | Commodities | 99447 | 94.6 | 94.6 | 1061 | -2321 |
| **corn** | Commodities | 317359 | 90.5 | 90.5 | 1061 | -107812 |
| **copper** | Commodities | 61465 | 89.4 | 89.4 | 1061 | -20552 |
| **vix** | Volatility | 5494 | 86.6 | 86.6 | 1020 | 28764 |
| **aud** | FX | 54133 | 85.7 | 85.7 | 1061 | 4354 |
| **cotton** | Commodities | 63837 | 82.9 | 82.9 | 1061 | -36333 |
| **dxy** | FX | 864 | 59.0 | 59.0 | 1061 | -5322 |
| **jpy** | FX | -25043 | 52.9 | 52.9 | 1061 | 24055 |
| **coffee** | Commodities | 13929 | 51.3 | 51.3 | 1061 | -4151 |
| **gbpfx** | FX | 12432 | 50.5 | 50.5 | 1061 | -22195 |
| **gold** | Commodities | 114820 | 48.0 | 48.0 | 1061 | -24728 |
| **cattle** | Commodities | 50920 | 43.7 | 43.7 | 1061 | 3670 |
| **heatingoil** | Commodities | 10953 | 43.5 | 43.5 | 1061 | -5051 |
| **wheat** | Commodities | -29543 | 41.8 | 41.8 | 1061 | -33805 |
| **platinum** | Commodities | 8117 | 40.2 | 40.2 | 1061 | -1550 |
| **nasdaq** | US Equities | -19212 | 36.2 | 36.2 | 1061 | 12660 |
| **brent** | Commodities | 2411 | 34.8 | 34.8 | 244 | -2949 |
| **bitcoin** | Crypto | -6852 | 34.7 | 34.7 | 444 | 1040 |
| **eurfx** | FX | -44261 | 32.0 | 32.0 | 1061 | -10976 |
| **us30y** | Rates | -189678 | 31.0 | 31.0 | 1061 | 87287 |
| **wti** | Commodities | 104491 | 22.1 | 22.1 | 1061 | -34848 |
| **silver** | Commodities | 7608 | 21.3 | 21.3 | 1061 | -6568 |
| **chf** | FX | -11350 | 20.6 | 20.6 | 1061 | 2090 |
| **sp500** | US Equities | -415087 | 18.2 | 18.2 | 1061 | -73983 |
| **us2y** | Rates | -1257484 | 18.1 | 18.1 | 1061 | 32995 |
| **cocoa** | Commodities | -14494 | 12.1 | 12.1 | 1061 | -2958 |
| **usultra10y** | Rates | -319061 | 12.0 | 12.0 | 551 | 107299 |
| **us5y** | Rates | -2127567 | 11.6 | 11.6 | 1061 | -61278 |
| **natgas** | Commodities | -144681 | 9.2 | 9.2 | 1061 | -48004 |
| **palladium** | Commodities | -9521 | 5.9 | 5.9 | 1061 | -5260 |
| **russell** | US Equities | -105317 | 5.5 | 5.5 | 597 | 4830 |
| **us10y** | Rates | -2139785 | 3.1 | 3.1 | 1061 | -201031 |
| **cad** | FX | -79625 | 3.1 | 3.1 | 1061 | -24177 |
| **hogs** | Commodities | -35272 | 0.3 | 0.3 | 1061 | -11716 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MPC** | Energy | 97.7 | 18.0% | 59.0% | 118.8% | 127.8% | 2.65 | -18.3% |
| 2 | **VLO** | Energy | 97.7 | 15.8% | 53.7% | 97.3% | 151.2% | 2.75 | -12.1% |
| 3 | **MRNA** | Healthcare | 97.5 | 57.4% | 258.4% | 317.1% | 437.7% | 1.63 | -34.2% |
| 4 | **PSX** | Energy | 96.5 | 12.2% | 48.5% | 86.5% | 110.2% | 2.59 | -17.3% |
| 5 | **ILMN** | Healthcare | 95.8 | 22.2% | 42.8% | 105.5% | 133.9% | 2.08 | -25.7% |
| 6 | **HPE** | Technology | 95.5 | 13.2% | 40.2% | 157.7% | 128.8% | 1.58 | -26.4% |
| 7 | **DELL** | Technology | 95.3 | -6.5% | 30.0% | 187.9% | 258.8% | 1.61 | -32.3% |
| 8 | **MRVL** | Technology | 94.0 | 10.7% | 30.3% | 82.3% | 148.4% | 1.24 | -48.4% |
| 9 | **TWLO** | Technology | 93.2 | 12.0% | 31.2% | 102.2% | 119.1% | 1.42 | -24.7% |
| 10 | **CRWD** | Technology | 91.4 | 2.8% | 22.3% | 142.5% | 90.7% | 1.16 | -37.2% |
| 11 | **NTAP** | Technology | 91.0 | 17.2% | 39.5% | 122.6% | 61.9% | 1.36 | -24.8% |
| 12 | **AMD** | Technology | 90.7 | 13.2% | 13.9% | 121.2% | 133.0% | 1.37 | -27.8% |
| 13 | **FTNT** | Technology | 90.3 | 6.8% | 14.5% | 131.1% | 104.7% | 1.77 | -14.3% |
| 14 | **APA** | Energy | 89.6 | -0.1% | 39.2% | 31.2% | 115.0% | 1.61 | -27.7% |
| 15 | **MU** | Technology | 89.5 | -1.4% | 7.2% | 100.4% | 381.7% | 1.89 | -39.1% |
| 16 | **CRL** | Healthcare | 88.6 | 10.7% | 31.8% | 67.3% | 59.9% | 1.18 | -33.9% |
| 17 | **RVTY** | Healthcare | 88.4 | 8.5% | 36.3% | 63.9% | 54.4% | 1.22 | -30.1% |
| 18 | **CNC** | Healthcare | 86.3 | 3.7% | 9.8% | 86.6% | 86.1% | 1.29 | -32.7% |
| 19 | **PANW** | Technology | 85.2 | -0.0% | 6.0% | 128.5% | 75.9% | 1.08 | -36.0% |
| 20 | **SNDK** | Technology | 84.9 | -8.3% | -0.6% | 57.4% | 1037.3% | 2.05 | -56.5% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MOH.AT** | Energy | 96.6 | 3.2% | 48.5% | 98.3% | 170.8% | 3.10 | -12.1% |
| 2 | **FRO.OL** | Energy | 94.5 | 21.5% | 54.4% | 69.1% | 104.0% | 2.07 | -20.5% |
| 3 | **SOI.PA** | Technology | 93.0 | 17.8% | 61.1% | 48.5% | 215.0% | 1.24 | -55.0% |
| 4 | **MAERSK-B.CO** | Industrials | 92.2 | 5.7% | 44.5% | 57.8% | 89.5% | 1.69 | -22.9% |
| 5 | **CCC.L** | Technology | 91.6 | 9.2% | 25.5% | 80.1% | 96.1% | 2.13 | -16.2% |
| 6 | **ATS.VI** | Technology | 91.3 | 33.4% | 15.7% | 138.5% | 442.6% | 2.34 | -50.1% |
| 7 | **REP.MC** | Energy | 90.4 | 3.9% | 22.6% | 54.0% | 110.7% | 2.26 | -20.4% |
| 8 | **OMV.VI** | Energy | 86.6 | 2.3% | 19.7% | 39.5% | 78.0% | 2.49 | -10.8% |
| 9 | **TPRO.MI** | Technology | 85.7 | 11.6% | 3.0% | 70.9% | 225.9% | 1.98 | -32.2% |
| 10 | **ROR.L** | Industrials | 85.7 | 1.8% | 69.5% | 51.1% | 44.6% | 0.64 | -25.2% |
| 11 | **VAR.OL** | Energy | 84.8 | -1.1% | 27.8% | 28.1% | 76.8% | 1.43 | -19.4% |
| 12 | **IFCN.SW** | Technology | 83.9 | 23.4% | 15.2% | 60.9% | 54.5% | 1.46 | -25.5% |
| 13 | **AKER.OL** | Industrials | 83.5 | -12.4% | 13.3% | 28.6% | 108.3% | 1.79 | -19.5% |
| 14 | **ABN.AS** | Financial Services | 83.1 | -4.5% | 9.8% | 41.8% | 75.9% | 1.82 | -18.0% |
| 15 | **ENI.MI** | Energy | 82.9 | 8.1% | 23.0% | 20.7% | 69.8% | 2.13 | -18.4% |
| 16 | **EQNR.OL** | Energy | 82.7 | 0.6% | 23.7% | 22.2% | 79.0% | 1.46 | -25.8% |
| 17 | **TKA.DE** | Basic Materials | 82.2 | -7.9% | 16.6% | 49.2% | 59.7% | 0.64 | -41.4% |
| 18 | **DEMANT.CO** | Healthcare | 82.0 | 20.2% | 25.9% | 69.4% | 29.5% | 1.24 | -29.2% |
| 19 | **PKO.WA** | Financial Services | 81.9 | -1.4% | 15.8% | 25.3% | 73.4% | 2.03 | -12.3% |
| 20 | **EBP.WA** | Financial Services | 81.2 | 0.2% | 14.3% | 26.5% | 69.9% | 1.87 | -10.9% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **EIX** | Utilities | 2.033 | 0.962 | 1.063 | 3.125 | -0.926 | - | 5.7 | +19.7% |
| 2 | **SNDK** | Information Technology | 1.672 | 1.988 | 1.547 | 0.738 | -0.136 | - | 20.0 | +91.6% |
| 3 | **CF** | Materials | 1.609 | 1.234 | 1.258 | 1.581 | 0.377 | - | 8.7 | +29.9% |
| 4 | **MO** | Consumer Staples | 1.461 | 0.383 | 2.134 | 0.958 | -0.436 | - | 15.2 | - |
| 5 | **MU** | Information Technology | 1.371 | 1.521 | 1.238 | 0.739 | -0.549 | - | 13.1 | +88.3% |
| 6 | **NEM** | Materials | 1.331 | 0.765 | 1.613 | 0.883 | 0.586 | - | 15.1 | +25.9% |
| 7 | **HST** | Real Estate | 1.230 | 1.769 | 0.483 | 1.024 | -0.287 | - | 16.1 | +15.6% |
| 8 | **APA** | Energy | 1.227 | 1.119 | 1.263 | 0.703 | -0.080 | - | 10.0 | +26.7% |
| 9 | **SYF** | Financials | 1.226 | 0.133 | 1.190 | 1.661 | -0.160 | - | 7.8 | +20.8% |
| 10 | **BMY** | Health Care | 1.185 | 0.971 | 0.879 | 1.165 | 0.601 | - | 12.8 | +46.6% |
| 11 | **SPG** | Real Estate | 1.127 | 0.774 | 1.390 | 0.610 | -1.220 | - | 14.5 | +120.5% |
| 12 | **MAS** | Industrials | 1.111 | -0.046 | 1.460 | 1.219 | -0.798 | - | 16.8 | +5862.5% |
| 13 | **DVA** | Health Care | 1.085 | 1.032 | 0.192 | 1.642 | -1.407 | - | 16.1 | +88.5% |
| 14 | **EXPE** | Consumer Discretionary | 1.029 | 1.520 | 0.792 | 0.380 | -0.665 | - | 18.2 | +89.5% |
| 15 | **TGT** | Consumer Staples | 0.986 | 2.447 | -0.087 | 0.452 | -0.746 | - | 15.9 | +26.4% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -2.048 | -1.829 | -0.927 | -2.513 | -0.907 |
| 502 | **TSLA** | Consumer Discretionary | -1.812 | -0.653 | -1.372 | -2.450 | -0.305 |
| 501 | **COIN** | Financials | -1.709 | -2.741 | -1.660 | 0.000 | -1.655 |
| 500 | **CSGP** | Real Estate | -1.704 | -3.304 | -0.460 | -0.860 | 0.706 |
| 499 | **CEG** | Utilities | -1.616 | -2.288 | -0.617 | -1.360 | -0.778 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W42.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W42.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\macro\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-10-12  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
