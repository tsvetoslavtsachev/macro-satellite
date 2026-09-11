# Сателит — пълен data export за 2026-W37

_Период: 2026-09-07 → 2026-09-13_  
_Генериран: 2026-09-11 10:45 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W37.md` (structured briefing) и `narrative_2026-W37.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**21 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **DIA** | -2.50% | -2.65σ | 534.08 | 520.75 | 2026-09-04 | 2026-09-10 | +0.37% | +1.08% | 13 |
| **XLF** | -2.12% | -2.56σ | 58.10 | 56.87 | 2026-09-04 | 2026-09-10 | +0.82% | +1.15% | 13 |
| **EFA** | -2.48% | -2.11σ | 108.35 | 105.66 | 2026-09-04 | 2026-09-10 | +0.46% | +1.39% | 13 |
| **IEF** | -1.16% | -2.09σ | 92.25 | 91.18 | 2026-09-04 | 2026-09-10 | -0.11% | +0.50% | 13 |
| **HYG** | -0.68% | -1.94σ | 79.16 | 78.62 | 2026-09-04 | 2026-09-10 | -0.03% | +0.34% | 13 |
| **VEA** | -2.49% | -1.88σ | 73.76 | 71.92 | 2026-09-04 | 2026-09-10 | +0.51% | +1.60% | 13 |
| **IWM** | -2.81% | -1.88σ | 296.01 | 287.70 | 2026-09-04 | 2026-09-10 | +0.40% | +1.71% | 13 |
| **XLB** | -3.20% | -1.80σ | 52.44 | 50.76 | 2026-09-04 | 2026-09-10 | +0.29% | +1.94% | 13 |
| **SHY** | -0.33% | -1.78σ | 81.69 | 81.42 | 2026-09-04 | 2026-09-10 | -0.02% | +0.18% | 13 |
| **XLV** | -3.38% | -1.66σ | 171.45 | 165.66 | 2026-09-04 | 2026-09-10 | +0.91% | +2.59% | 13 |
| **XLI** | -2.69% | -1.50σ | 175.27 | 170.55 | 2026-09-04 | 2026-09-10 | +0.06% | +1.84% | 13 |
| **VWO** | -2.44% | -1.49σ | 61.44 | 59.94 | 2026-09-04 | 2026-09-10 | +0.46% | +1.94% | 13 |
| **DBC** | +5.39% | +1.45σ | 31.90 | 33.62 | 2026-09-04 | 2026-09-10 | +0.73% | +3.22% | 13 |
| **LQD** | -1.06% | -1.44σ | 105.48 | 104.36 | 2026-09-04 | 2026-09-10 | -0.19% | +0.60% | 13 |
| **TLT** | -1.74% | -1.42σ | 82.21 | 80.78 | 2026-09-04 | 2026-09-10 | -0.26% | +1.04% | 13 |
| **USO** | +11.57% | +1.38σ | 141.96 | 158.38 | 2026-09-04 | 2026-09-10 | +0.80% | +7.79% | 13 |
| **XLP** | -1.76% | -1.29σ | 84.58 | 83.09 | 2026-09-04 | 2026-09-10 | +0.12% | +1.46% | 13 |
| **SPY** | -1.60% | -1.28σ | 770.19 | 757.83 | 2026-09-04 | 2026-09-10 | +0.35% | +1.52% | 13 |
| **VNQ** | -1.98% | -1.11σ | 96.02 | 94.12 | 2026-09-04 | 2026-09-10 | -0.05% | +1.73% | 13 |
| **XLRE** | -2.00% | -1.10σ | 43.93 | 43.05 | 2026-09-04 | 2026-09-10 | -0.12% | +1.72% | 13 |
| **TIP** | -0.60% | -1.03σ | 106.97 | 106.33 | 2026-09-04 | 2026-09-10 | -0.16% | +0.42% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-09-13 · **Conditions matched:** 3/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | +11.57% | ✅ | 141.96 | 158.38 | 2026-09-04 | 2026-09-10 |
| DFEN | down ≥ 3.0% | -9.59% | ✅ | 61.45 | 55.56 | 2026-09-04 | 2026-09-10 |
| GLD | down ≥ 1.0% | -2.56% | ✅ | 406.77 | 396.36 | 2026-09-04 | 2026-09-10 |
| URA | down ≥ 3.0% | -2.30% | ❌ | 46.06 | 45.00 | 2026-09-04 | 2026-09-10 |
| UUP | up ≥ 0.5% | -0.18% | ❌ | 28.08 | 28.03 | 2026-09-04 | 2026-09-10 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-09-13 · **Conditions matched:** 1/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | -2.81% | ❌ | 296.01 | 287.70 | 2026-09-04 | 2026-09-10 |
| XLF | up ≥ 1.0% | -2.12% | ❌ | 58.10 | 56.87 | 2026-09-04 | 2026-09-10 |
| XLY | up ≥ 1.0% | -2.57% | ❌ | 114.91 | 111.96 | 2026-09-04 | 2026-09-10 |
| GLD | down ≥ 0.5% | -2.56% | ✅ | 406.77 | 396.36 | 2026-09-04 | 2026-09-10 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2026-W11 (week ending 2026-03-15)
**Cosine similarity:** 0.9743 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.86% | +12.00% | +14.43% |
| **USO** | +3.30% | +4.62% | +32.10% |
| **GLD** | -3.42% | -16.12% | -13.99% |
| **TLT** | +0.77% | -0.89% | -6.66% |
| **XLE** | -3.03% | -0.26% | +12.53% |
| **IWM** | +8.97% | +18.80% | +16.67% |

### Паралел #2: 2026-W10 (week ending 2026-03-08)
**Cosine similarity:** 0.9664 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.96% | +9.69% | +14.55% |
| **USO** | +26.95% | +22.29% | +30.51% |
| **GLD** | -8.81% | -16.32% | -14.09% |
| **TLT** | -2.06% | -3.84% | -7.07% |
| **XLE** | +6.35% | +1.94% | +13.24% |
| **IWM** | +0.81% | +12.26% | +17.98% |

### Паралел #3: 2026-W05 (week ending 2026-02-01)
**Cosine similarity:** 0.8983 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.68% | +4.14% | +7.96% |
| **USO** | +13.43% | +79.58% | +62.44% |
| **GLD** | +5.21% | -4.89% | -16.50% |
| **TLT** | +2.64% | -1.74% | -5.60% |
| **XLE** | +10.71% | +15.28% | +16.65% |
| **IWM** | -0.16% | +7.56% | +12.15% |

### Паралел #4: 2026-W17 (week ending 2026-04-26)
**Cosine similarity:** 0.8874 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.13% | +3.50% | +6.15% |
| **USO** | +3.47% | +3.24% | +19.62% |
| **GLD** | -4.44% | -14.16% | -8.51% |
| **TLT** | -1.86% | -3.99% | -6.84% |
| **XLE** | +1.72% | +4.84% | +14.17% |
| **IWM** | +5.01% | +5.25% | +3.99% |

### Паралел #5: 2026-W20 (week ending 2026-05-17)
**Cosine similarity:** 0.8810 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.51% | +5.03% | +2.52% |
| **USO** | -22.10% | -14.59% | +6.85% |
| **GLD** | -4.71% | -3.79% | -5.02% |
| **TLT** | +3.02% | -1.94% | -3.44% |
| **XLE** | -6.86% | +4.16% | +9.24% |
| **IWM** | +5.22% | +9.90% | +3.64% |

### Паралел #6: 2023-W06 (week ending 2023-02-12)
**Cosine similarity:** 0.8774 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -4.00% | +0.87% | +9.22% |
| **USO** | -9.93% | -11.16% | +6.27% |
| **GLD** | +2.00% | +7.76% | +2.45% |
| **TLT** | +0.68% | +0.85% | -7.76% |
| **XLE** | -9.38% | -12.96% | -0.34% |
| **IWM** | -7.25% | -9.24% | +0.36% |

### Паралел #7: 2022-W22 (week ending 2022-06-05)
**Cosine similarity:** 0.8664 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -6.96% | -4.46% | -0.88% |
| **USO** | -16.42% | -20.16% | -21.94% |
| **GLD** | -4.54% | -7.72% | -3.08% |
| **TLT** | +0.60% | -5.01% | -7.70% |
| **XLE** | -22.13% | -10.67% | +0.89% |
| **IWM** | -7.61% | -3.73% | +0.53% |

### Паралел #8: 2022-W09 (week ending 2022-03-06)
**Cosine similarity:** 0.8456 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.36% | -5.00% | -9.24% |
| **USO** | -5.86% | +12.60% | -10.11% |
| **GLD** | -2.42% | -6.04% | -13.29% |
| **TLT** | -8.38% | -17.26% | -21.41% |
| **XLE** | +0.96% | +18.98% | +6.29% |
| **IWM** | +2.18% | -5.84% | -9.35% |

### Паралел #9: 2024-W32 (week ending 2024-08-11)
**Cosine similarity:** 0.8456 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.96% | +12.23% | +12.72% |
| **USO** | -12.15% | -4.05% | -0.47% |
| **GLD** | +3.59% | +10.42% | +17.52% |
| **TLT** | +4.60% | -3.92% | -7.26% |
| **XLE** | -4.78% | +4.85% | -0.95% |
| **IWM** | +0.90% | +15.33% | +9.46% |

### Паралел #10: 2026-W18 (week ending 2026-05-03)
**Cosine similarity:** 0.8252 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.40% | +3.66% | +5.16% |
| **USO** | -3.87% | -9.54% | +10.91% |
| **GLD** | -2.65% | -12.20% | -6.34% |
| **TLT** | +0.05% | -3.92% | -5.64% |
| **XLE** | -1.51% | +1.19% | +10.33% |
| **IWM** | +4.43% | +4.27% | +3.01% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 15 · **Total matching days:** 75 · **History:** 2021-05-17 → 2026-09-10

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 14 | +2.2% | +2.4% | -3.1% | +7.4% | 71% |
| **SPY** | 3m | 14 | +2.7% | +2.5% | -7.3% | +12.0% | 79% |
| **SPY** | 6m | 14 | +7.5% | +9.8% | -6.8% | +21.8% | 79% |
| **USO** | 1m | 14 | +0.5% | +0.3% | -14.3% | +12.7% | 50% |
| **USO** | 3m | 14 | -0.1% | -2.0% | -18.9% | +27.8% | 50% |
| **USO** | 6m | 14 | +15.9% | +4.6% | -8.7% | +109.4% | 64% |
| **GLD** | 1m | 14 | +3.1% | +2.0% | -0.9% | +9.0% | 79% |
| **GLD** | 3m | 14 | +5.8% | +6.7% | -12.6% | +24.5% | 71% |
| **GLD** | 6m | 14 | +6.8% | +8.9% | -12.5% | +25.3% | 71% |
| **TLT** | 1m | 14 | -1.5% | -1.1% | -6.7% | +3.6% | 36% |
| **TLT** | 3m | 14 | -0.7% | -0.1% | -16.5% | +11.1% | 50% |
| **TLT** | 6m | 14 | -4.6% | -5.1% | -18.0% | +7.5% | 29% |

**Episodes (последни 5 от 15):**
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-08-03` (5d)
- `2026-09-10 → 2026-09-10` (1d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 84 · **History:** 2021-05-17 → 2026-09-10

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +6.3% | +6.3% | +3.5% | +9.1% | 100% |
| **SPY** | 3m | 2 | +5.5% | +5.5% | +0.8% | +10.3% | 100% |
| **SPY** | 6m | 2 | +6.5% | +6.5% | +0.8% | +12.1% | 100% |
| **USO** | 1m | 2 | +5.6% | +5.6% | +4.0% | +7.2% | 100% |
| **USO** | 3m | 2 | +10.9% | +10.9% | -9.9% | +31.8% | 50% |
| **USO** | 6m | 2 | +29.5% | +29.5% | +27.1% | +31.8% | 100% |
| **GLD** | 1m | 2 | +3.5% | +3.5% | -0.2% | +7.2% | 50% |
| **GLD** | 3m | 2 | -3.7% | -3.7% | -13.8% | +6.5% | 50% |
| **GLD** | 6m | 2 | -1.1% | -1.1% | -8.8% | +6.5% | 50% |
| **TLT** | 1m | 2 | -1.4% | -1.4% | -1.8% | -1.0% | 0% |
| **TLT** | 3m | 2 | -3.4% | -3.4% | -3.9% | -2.9% | 0% |
| **TLT** | 6m | 2 | -5.5% | -5.5% | -7.1% | -3.9% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-09-10` (37d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 439 · **History:** 2021-05-17 → 2026-09-10

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
- `2025-11-03 → 2026-09-10` (207d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-09-10

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 10 · **Total matching days:** 93 · **History:** 2021-05-17 → 2026-09-10

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 10 | -0.2% | +0.2% | -7.2% | +7.8% | 50% |
| **SPY** | 3m | 10 | +1.6% | +0.4% | -8.3% | +11.6% | 50% |
| **SPY** | 6m | 10 | +0.9% | +2.8% | -20.8% | +14.2% | 60% |
| **USO** | 1m | 10 | +4.7% | +0.5% | -15.0% | +52.9% | 50% |
| **USO** | 3m | 10 | +10.8% | +11.7% | -20.7% | +52.2% | 60% |
| **USO** | 6m | 10 | +12.9% | +8.4% | -27.6% | +56.3% | 60% |
| **GLD** | 1m | 10 | -0.8% | -0.9% | -8.3% | +11.7% | 20% |
| **GLD** | 3m | 10 | -0.7% | +0.1% | -12.0% | +6.4% | 50% |
| **GLD** | 6m | 10 | +0.1% | -0.4% | -15.2% | +25.0% | 40% |
| **TLT** | 1m | 10 | -2.0% | -2.1% | -6.0% | +2.5% | 10% |
| **TLT** | 3m | 10 | -6.0% | -4.9% | -17.6% | +4.2% | 20% |
| **TLT** | 6m | 10 | -9.5% | -8.1% | -22.3% | +1.2% | 10% |

**Episodes (последни 5 от 10):**
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-05-19` (36d)
- `2026-07-22 → 2026-08-03` (8d)
- `2026-09-01 → 2026-09-10` (7d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 17 · **Total matching days:** 294 · **History:** 2021-05-17 → 2026-09-10

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 17 | +1.9% | +1.6% | -4.8% | +9.0% | 71% |
| **SPY** | 3m | 17 | +3.0% | +4.2% | -12.6% | +16.2% | 71% |
| **SPY** | 6m | 17 | +6.3% | +6.9% | -14.0% | +21.0% | 76% |
| **USO** | 1m | 17 | +2.4% | -2.2% | -13.0% | +22.9% | 41% |
| **USO** | 3m | 17 | +3.9% | -0.8% | -14.5% | +34.2% | 41% |
| **USO** | 6m | 17 | +14.6% | +2.6% | -12.4% | +87.1% | 71% |
| **GLD** | 1m | 17 | +2.4% | +2.1% | -5.6% | +9.0% | 76% |
| **GLD** | 3m | 17 | +5.9% | +7.2% | -16.8% | +23.6% | 65% |
| **GLD** | 6m | 17 | +10.6% | +9.8% | -10.3% | +43.8% | 71% |
| **TLT** | 1m | 17 | +0.3% | -0.0% | -6.3% | +8.2% | 47% |
| **TLT** | 3m | 17 | -1.6% | -1.7% | -15.3% | +11.9% | 35% |
| **TLT** | 6m | 17 | -4.6% | -2.4% | -21.3% | +7.0% | 35% |

**Episodes (последни 5 от 17):**
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)
- `2026-08-07 → 2026-09-03` (19d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 19 · **Total matching days:** 288 · **History:** 2021-05-17 → 2026-09-10

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 19 | +0.4% | +1.0% | -8.7% | +7.0% | 53% |
| **SPY** | 3m | 19 | +2.1% | +3.6% | -13.7% | +9.1% | 68% |
| **SPY** | 6m | 19 | +3.3% | +6.8% | -16.4% | +16.9% | 74% |
| **USO** | 1m | 19 | -0.6% | -5.6% | -21.8% | +55.8% | 42% |
| **USO** | 3m | 19 | +3.9% | -0.6% | -12.7% | +64.3% | 47% |
| **USO** | 6m | 19 | +9.5% | +5.0% | -16.0% | +75.1% | 53% |
| **GLD** | 1m | 19 | -0.6% | -0.1% | -12.4% | +7.6% | 47% |
| **GLD** | 3m | 19 | +1.9% | +1.7% | -13.7% | +19.0% | 68% |
| **GLD** | 6m | 19 | +8.0% | +6.0% | -15.8% | +55.5% | 74% |
| **TLT** | 1m | 19 | -0.2% | -0.1% | -5.6% | +5.2% | 47% |
| **TLT** | 3m | 19 | -3.6% | -4.4% | -17.3% | +8.7% | 32% |
| **TLT** | 6m | 19 | -6.9% | -7.4% | -21.4% | +4.6% | 21% |

**Episodes (последни 5 от 19):**
- `2025-05-12 → 2025-05-19` (3d)
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (13d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-09-10

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (11 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 5 | 2.72 | 2.75 | 2026-08-08 00:00:00 | 2026-09-05 00:00:00 | ✓ |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | 5 | 2.61 | 2.70 | 2026-08-08 00:00:00 | 2026-09-05 00:00:00 | ✓ |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 4 | 2.28 | 2.30 | 2026-08-08 00:00:00 | 2026-09-05 00:00:00 | - |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | 4 | 2.22 | 2.22 | 2026-08-08 00:00:00 | 2026-08-29 00:00:00 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 3 | 2.16 | 2.16 | 2026-08-08 00:00:00 | 2026-08-22 00:00:00 | - |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | 3 | 2.09 | 2.09 | 2026-08-08 00:00:00 | 2026-08-22 00:00:00 | - |
| **COMPUTSA** | Завършени жилища (SAAR) | growth | housing_supply | 3 | 2.06 | 2.06 | 2026-08-22 00:00:00 | 2026-09-05 00:00:00 | - |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 2 | 2.28 | 2.28 | 2026-08-08 00:00:00 | 2026-08-15 00:00:00 | ✓ |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | 1 | 2.28 | 2.28 | 2026-08-08 00:00:00 | 2026-08-08 00:00:00 | ✓ |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 1 | 2.15 | 2.15 | 2026-08-08 00:00:00 | 2026-08-08 00:00:00 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | 1 | 2.02 | 2.02 | 2026-09-05 00:00:00 | 2026-09-05 00:00:00 | ✓ |

### EU (4 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.27 | 5.28 | 2026-08-08 00:00:00 | 2026-09-05 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.17 | 2.17 | 2026-08-08 00:00:00 | 2026-09-05 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.16 | 2.17 | 2026-08-08 00:00:00 | 2026-09-05 00:00:00 | ✓ |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | 1 | 2.38 | 2.38 | 2026-08-08 00:00:00 | 2026-08-08 00:00:00 | - |

### CN (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 9 | 2.55 | 2.55 | 2026-08-10 00:00:00 | 2026-09-07 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 9 | 2.22 | 2.23 | 2026-08-10 00:00:00 | 2026-09-07 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 2 | 2.19 | 2.19 | 2026-08-22 00:00:00 | 2026-09-07 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-09-05 00:00:00 · **Generated:** 2026-09-05 06:56:51.507421+00:00

**Режим:** `disinflation_cooling` (Дезинфлация и охлаждане (индикирани))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 37.6 | contracting | 29.6% | 3 | 2 |
| **growth** | 45.9 | mixed | 44.0% | 1 | 0 |
| **inflation** | 40.9 | mixed | 38.9% | 1 | 1 |
| **liquidity** | 52.6 | mixed | 47.4% | 0 | 0 |

### Top anomalies (5 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.75 | down | 93.45 | 2026-04-01 | ✓ min |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | -2.25 | down | 2.30 | 2026-06-01 | - |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | -2.25 | down | 61.60 | 2026-08-01 | - |
| **COMPUTSA** | Завършени жилища (SAAR) | growth, housing | housing_supply | -2.06 | down | -16.76 | 2026-07-01 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | -2.02 | down | 1.90 | 2026-07-01 | ✓ min |

### Narrative hints от макро лещите
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **HPIPONM226S**: Monthly FHFA версия. Само purchase transactions (без refi appraisals). По-чист от refi-bias.
- **CIVPART**: Структурни сдвигове (демография, ранно пенсиониране). Пост-COVID не се възстанови напълно.
- **COMPUTSA**: Завършва construction pipeline (12-18m след starts). Превишение спрямо sales = inventory build.
- **JTSQUR**: Работническа увереност. Ако quits rate пада — хората задържат работата си (pre-recession pattern).

### Cross-lens divergences (6 entries)
- 🔔 **?**
  - `pair_id`: stagflation_test
  - `name_bg`: Labor tightness × Inflation pressure
  - `question_bg`: Дали labor tightness потвърждава inflation pressure (стагфлация)?
  - `state`: both_down
  - `interpretation`: Joint cooling — labor охлажда, inflation cools (disinflation в ход).
  - `slot_a_label`: Labor tightness
  - `slot_b_label`: Inflation pressure
  - `breadth_a`: 0.2
  - `breadth_b`: 0.167
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.7
  - `breadth_b_raw`: 0.833
- 🔔 **?**
  - `pair_id`: growth_labor_lead_lag
  - `name_bg`: Hard activity × Labor claims
  - `question_bg`: Дали hard activity и labor market следват едно тенденция?
  - `state`: both_down
  - `interpretation`: Synchronized slowdown — activity cools + claims spike.
  - `slot_a_label`: Hard activity
  - `slot_b_label`: Labor market (claims inverted)
  - `breadth_a`: 0.2
  - `breadth_b`: 0.0
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 0.8
  - `breadth_b_raw`: 0.0
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Realized CPI × Expectations
  - `question_bg`: Дали expectations следват realized inflation, или стоят anchored?
  - `state`: both_down
  - `interpretation`: Joint disinflation — expectations потвърждават cooling.
  - `slot_a_label`: Realized inflation
  - `slot_b_label`: Inflation expectations
  - `breadth_a`: 0.167
  - `breadth_b`: 0.0
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 0.833
  - `breadth_b_raw`: 0.0
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
  - `state`: a_up_b_down
  - `interpretation`: Sentiment ahead of data — watch for confirmation.
  - `slot_a_label`: Consumer sentiment
  - `slot_b_label`: Hard activity
  - `breadth_a`: 0.667
  - `breadth_b`: 0.2
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.667
  - `breadth_b_raw`: 0.8
- 🔔 **?**
  - `pair_id`: model_vs_market
  - `name_bg`: Model-implied × Market-implied inflation
  - `question_bg`: Дали underlying persistence и market pricing-а са съгласни за инфлацията?
  - `state`: a_up_b_down
  - `interpretation`: Модел persistent, пазар разчита на disinflation — contrarian hawkish (моделът обикновено лидера).
  - `slot_a_label`: Модел (sticky inflation)
  - `slot_b_label`: Пазар (breakevens + survey)
  - `breadth_a`: 0.667
  - `breadth_b`: 0.0
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 0.667
  - `breadth_b_raw`: 0.0

### Executive narrative
> Синхронно охлаждане — labor и инфлация отстъпват заедно. Рискът се мести към overshooting, ако claims ускорят. Най-отклонена леща: Монетарна политика и кредит — breadth 30% (свиване), 0 аномалии, 0 нови екстремума. За наблюдение следващия релиз: LABOR_SHARE_NBS, JTSQUR (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: LABOR_SHARE_NBS z=-2.75 · NEW-5Y-MIN
- 2 нови екстремуми в top-5 (lookback 5г.)
- Активни двойки: Stagflation test=both_down; Growth × Labor=both_down; Inflation anchoring=both_down



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-09-05 00:00:00 · **Generated:** 2026-09-05 07:07:05.236728+00:00

**Режим:** `disinflation_cooling` (Дезинфлация и охлаждане (индикирани))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 42.2 | mixed | 42.9% | 0 | 0 |
| **growth** | 40.7 | mixed | 25.0% | 0 | 0 |
| **inflation** | 49.6 | mixed | 42.9% | 0 | 0 |
| **credit** | 43.9 | mixed | 36.8% | 3 | 2 |
| **external** | 34.3 | contracting | 16.7% | 0 | 0 |

### Top anomalies (3 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | +5.28 | up | 2.92 | 2026-08-01 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | +2.17 | up | 3.85 | 2026-07-01 | ✓ max |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | +2.17 | up | 3.07 | 2026-07-01 | ✓ max |

### Narrative hints от макро лещите
- **EA_BUND_2Y**: EA-aggregate 2Y yield. Curve slope (10Y-2Y) проксира policy expectations и recession risk.
- **FR_10Y**: France sovereign yield — компонент на OAT-Bund spread. Core-but-not-DE EA stress indicator.
- **DE_10Y**: Germany 10Y, Maastricht-criterion measure. Reference за BTP-Bund / OAT-Bund spread изчисления.

### Cross-lens divergences (7 entries)
- 🔔 **?**
  - `pair_id`: stagflation_test
  - `name_bg`: Стагфлационен тест
  - `question_bg`: Заплатите ли движат услугите нагоре?
  - `state`: both_down
  - `interpretation`: Дезинфлация broad-based: и заплати, и базова отстъпват. ЕЦБ има пространство за политика.
  - `slot_a_label`: Натиск от заплати
  - `slot_b_label`: Базова/услуги инфлация
  - `breadth_a`: 0.0
  - `breadth_b`: 0.0
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.0
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
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.0
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
  - `breadth_a`: 0.667
  - `breadth_b`: None
  - `state_raw`: insufficient_data
  - `breadth_a_raw`: 0.667
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
  - `breadth_b`: 0.0
  - `state_raw`: insufficient_data
  - `breadth_a_raw`: None
  - `breadth_b_raw`: 0.0
- 🔔 **?**
  - `pair_id`: sentiment_vs_hard_data
  - `name_bg`: Очаквания срещу твърди данни
  - `question_bg`: Sentiment отразява ли реалната икономика?
  - `state`: transition
  - `interpretation`: Sentiment turn обикновено leads hard data 3-6mo.
  - `slot_a_label`: Sentiment (ESI, confidence)
  - `slot_b_label`: Hard activity (IP, retail, GDP)
  - `breadth_a`: 0.778
  - `breadth_b`: 0.5
  - `state_raw`: transition
  - `breadth_a_raw`: 0.778
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
  - `breadth_b`: 0.75
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 1.0

### Executive narrative
> Синхронно охлаждане — labor и инфлация отстъпват заедно. Рискът се мести към overshooting, ако claims ускорят. Най-отклонена леща: Финансови условия, кредит и спредове — breadth 100% (разширяване), 3 аномалии, 2 нови екстремума. За наблюдение следващия релиз: FR_10Y, DE_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.28
- 2 нови екстремуми в top-3 (lookback 5г.)
- Активни двойки: Stagflation test=both_down; ecb_transmission=a_up_b_down; fragmentation_risk=both_up



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-09-07 00:00:00 · **Generated:** 2026-09-07 10:53:01.945192+00:00

**Режим:** `recessionary` (РЕЦЕСИОНЕН)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 28.7 | contracting | -% | - | - |
| **inflation** | 44.9 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 47.8 | mixed | -% | - | - |
| **property** | 28.6 | contracting | -% | - | - |

### Top anomalies (3 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | -2.55 | down | 3.00 | 2026-08-20 | ✓ min |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | +2.23 | up | 15.79 | 2025-12-31 | ✓ max |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | -2.19 | down | 1.72 | 2026-07-31 | - |

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
  - `breadth_a`: 0.333
  - `breadth_b`: 0.45
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
> Претеглен композитен macro score 34.9/100 → режим „РЕЦЕСИОНЕН“ (5/5 лещи). 5 лещи, 3 flagged аномалии (3 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-09-04 |
| `as_of` | 2026-09-04 |
| `regime` | GROWTH |
| `alignment_score` | 3.0 |
| `gms_score` | 5.0 |
| `gms_max` | 8 |
| `gms_tier` | MEDIUM |
| `ks_status` | inactive |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-09-04 → 2026-09-09)

**stable_winner (1m):** +6 entered, -5 exited
  - **Entered:** APA, IBKR, JNJ, MRNA, NEM, VRT
  - **Exited:** BIIB, BK, CASY, FIX, VLO

**stable_winner (3m):** +7 entered, -6 exited
  - **Entered:** CFG, FITB, GM, LLY, NEE, PFG, PNC _(включително 1 за първи път в историята: PFG)_
  - **Exited:** EIX, MAR, MNST, STLD, VTR, WELL

**quality_dip (1m):** +8 entered, -7 exited
  - **Entered:** BIIB, BK, CASY, F, FIX, LLY, PFG, VLO _(включително 1 за първи път в историята: PFG)_
  - **Exited:** APA, FCX, IBKR, JNJ, MRNA, NEM, VRT

**quality_dip (3m):** +7 entered, -6 exited
  - **Entered:** EIX, F, MAR, MNST, STLD, VTR, WELL _(включително 2 за първи път в историята: EIX, MAR)_
  - **Exited:** CFG, FCX, FITB, GM, NEE, PNC

**faded_bounce (1m):** +10 entered, -5 exited
  - **Entered:** BSX, CPB, EQT, EXE, IP, KVUE, NKE, OKE, PEG, POOL
  - **Exited:** CMG, EFX, MOS, SO, TTD

**faded_bounce (3m):** +8 entered, -3 exited
  - **Entered:** CLX, EOG, FIS, GIS, KMB, MKC, PEG, STZ _(включително 1 за първи път в историята: MKC)_
  - **Exited:** CARR, TDG, VRSK

### EU (period: 2026-09-04 → 2026-09-09)

**stable_winner (1m):** +10 entered, -11 exited
  - **Entered:** ABN.AS, BAMI.MI, BESI.AS, EBS.VI, ELE.MC, FRES.L, KER.PA, LOTB.BR, SDR.L, STAN.L _(включително 2 за първи път в историята: ELE.MC, LOTB.BR)_
  - **Exited:** BG.VI, BPE.MI, DANSKE.CO, ELI.BR, HM-B.ST, HSBA.L, ING.WA, ITX.MC, MBK.WA, NDA.DE, SWED-A.ST

**stable_winner (3m):** +9 entered, -7 exited
  - **Entered:** AVOL.SW, EBS.VI, ELE.MC, HM-B.ST, INDU-C.ST, ING.WA, JYSK.CO, RWE.DE, RXL.PA _(включително 3 за първи път в историята: ELE.MC, INDU-C.ST, RXL.PA)_
  - **Exited:** BBVA.MC, BPE.MI, FR.PA, FRO.OL, NDA.DE, NKT.CO, PKN.WA

**quality_dip (1m):** +13 entered, -13 exited
  - **Entered:** BG.VI, BPE.MI, DANSKE.CO, ELI.BR, HM-B.ST, INDU-C.ST, ING.WA, ITX.MC, MBK.WA, NDA.DE, NHY.OL, RXL.PA, SWED-A.ST _(включително 3 за първи път в историята: INDU-C.ST, NHY.OL, RXL.PA)_
  - **Exited:** ABN.AS, BAMI.MI, BBY.L, BESI.AS, EBS.VI, FRES.L, FTK.DE, KER.PA, LOTB.BR, SDR.L, STAN.L, SUBC.OL, TSCO.L

**quality_dip (3m):** +8 entered, -11 exited
  - **Entered:** BBVA.MC, BPE.MI, FR.PA, FRO.OL, NDA.DE, NHY.OL, NKT.CO, PKN.WA _(включително 3 за първи път в историята: FRO.OL, NDA.DE, NHY.OL)_
  - **Exited:** AVOL.SW, BBY.L, EBS.VI, FTK.DE, HM-B.ST, HSBA.L, ING.WA, JYSK.CO, RWE.DE, SUBC.OL, TSCO.L

**faded_bounce (1m):** +8 entered, -10 exited
  - **Entered:** ADM.L, BME.L, CAP.PA, RI.PA, SREN.SW, STLAM.MI, TOM.OL, VTY.L
  - **Exited:** ADYEN.AS, CS.PA, HNR1.DE, LIFCO-B.ST, LSEG.L, MNDI.L, MUV2.DE, NEM.DE, NEXI.MI, VER.VI

**faded_bounce (3m):** +0 entered, -1 exited
  - **Exited:** BPT.L



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-09-01 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **corn** | Commodities | 431062 | 100.0 | 100.0 | 1056 | 249116 |
| **soymeal** | Commodities | 158741 | 100.0 | 100.0 | 1056 | 81290 |
| **cotton** | Commodities | 107976 | 99.8 | 99.8 | 1056 | 45697 |
| **soybeans** | Commodities | 241183 | 99.3 | 99.3 | 1056 | 115717 |
| **soyoil** | Commodities | 109912 | 97.2 | 97.2 | 1056 | 29231 |
| **sugar** | Commodities | 243467 | 96.7 | 96.7 | 1056 | 321281 |
| **rbob** | Commodities | 89263 | 93.7 | 93.7 | 1056 | 19439 |
| **copper** | Commodities | 73000 | 93.3 | 93.3 | 1056 | -4796 |
| **aud** | FX | 49662 | 82.4 | 82.4 | 1056 | 9025 |
| **gbpfx** | FX | 43167 | 81.7 | 81.7 | 1056 | 4993 |
| **dxy** | FX | 7133 | 79.2 | 79.2 | 1056 | 3284 |
| **wheat** | Commodities | 14654 | 76.3 | 76.3 | 1056 | 38440 |
| **heatingoil** | Commodities | 20985 | 64.0 | 64.0 | 1056 | 9706 |
| **vix** | Volatility | -26258 | 62.9 | 62.9 | 1015 | -30031 |
| **gold** | Commodities | 140811 | 62.2 | 62.2 | 1056 | 8413 |
| **coffee** | Commodities | 22350 | 60.3 | 60.3 | 1056 | -1200 |
| **brent** | Commodities | 4940 | 43.9 | 43.9 | 239 | -3091 |
| **sp500** | US Equities | -317564 | 43.8 | 43.8 | 1056 | 12435 |
| **platinum** | Commodities | 8647 | 42.8 | 42.8 | 1056 | -2235 |
| **cattle** | Commodities | 47914 | 41.4 | 41.4 | 1056 | -18153 |
| **nasdaq** | US Equities | -14092 | 41.1 | 41.1 | 1056 | 64241 |
| **eurfx** | FX | -38173 | 35.0 | 35.0 | 1056 | 14032 |
| **bitcoin** | Crypto | -7620 | 31.2 | 31.2 | 439 | -380 |
| **silver** | Commodities | 12170 | 31.1 | 31.1 | 1056 | 1103 |
| **wti** | Commodities | 119619 | 27.5 | 27.5 | 1056 | 18569 |
| **chf** | FX | -10298 | 23.7 | 23.7 | 1056 | -214 |
| **natgas** | Commodities | -89523 | 22.2 | 22.2 | 1056 | 37022 |
| **us30y** | Rates | -303045 | 18.5 | 18.5 | 1056 | 73181 |
| **cocoa** | Commodities | -8925 | 18.4 | 18.4 | 1056 | 2989 |
| **us2y** | Rates | -1268034 | 17.7 | 17.7 | 1056 | 66147 |
| **palladium** | Commodities | -4579 | 13.1 | 13.1 | 1056 | 850 |
| **us5y** | Rates | -2202688 | 10.9 | 10.9 | 1056 | 8751 |
| **cad** | FX | -68750 | 6.7 | 6.7 | 1056 | 32998 |
| **jpy** | FX | -102188 | 4.5 | 4.5 | 1056 | -41363 |
| **russell** | US Equities | -109499 | 4.4 | 4.4 | 592 | -24354 |
| **us10y** | Rates | -2062502 | 3.9 | 3.9 | 1056 | 169168 |
| **usultra10y** | Rates | -423357 | 2.2 | 2.2 | 546 | -3496 |
| **hogs** | Commodities | -28323 | 0.5 | 0.5 | 1056 | -18681 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **DELL** | Technology | 97.2 | 16.9% | 40.4% | 274.0% | 277.0% | 2.04 | -32.3% |
| 2 | **MRNA** | Healthcare | 96.6 | 126.7% | 184.1% | 146.7% | 140.9% | 1.30 | -34.2% |
| 3 | **VLO** | Energy | 96.4 | 23.5% | 53.9% | 80.8% | 104.4% | 2.44 | -12.1% |
| 4 | **MPC** | Energy | 95.1 | 25.0% | 55.2% | 86.8% | 79.2% | 2.24 | -18.3% |
| 5 | **CRWD** | Technology | 93.2 | -7.7% | 28.9% | 90.5% | 110.4% | 1.16 | -37.2% |
| 6 | **HPE** | Technology | 93.0 | 7.7% | 22.4% | 181.8% | 137.5% | 1.68 | -26.4% |
| 7 | **PSX** | Energy | 93.0 | 21.6% | 46.5% | 62.5% | 69.5% | 2.21 | -17.3% |
| 8 | **PANW** | Technology | 92.6 | -13.0% | 28.6% | 102.4% | 95.1% | 1.08 | -36.0% |
| 9 | **MU** | Technology | 91.3 | 19.4% | 9.8% | 155.1% | 556.0% | 2.50 | -39.1% |
| 10 | **CRL** | Healthcare | 91.0 | 0.5% | 46.6% | 66.3% | 71.0% | 1.08 | -33.9% |
| 11 | **LITE** | Technology | 90.8 | 21.6% | 20.4% | 47.2% | 444.5% | 1.92 | -42.8% |
| 12 | **SNDK** | Technology | 90.5 | 42.5% | 7.1% | 185.1% | 1656.0% | 2.77 | -56.5% |
| 13 | **AMD** | Technology | 90.2 | 11.0% | 9.6% | 156.4% | 210.1% | 1.69 | -27.8% |
| 14 | **FTNT** | Technology | 89.4 | -4.3% | 13.6% | 86.7% | 104.3% | 1.55 | -23.0% |
| 15 | **STX** | Technology | 89.0 | 10.6% | 4.8% | 131.1% | 326.8% | 2.04 | -31.8% |
| 16 | **STT** | Financial Services | 88.5 | 2.8% | 18.1% | 58.4% | 71.5% | 2.10 | -11.8% |
| 17 | **APA** | Energy | 88.1 | 9.3% | 23.3% | 42.9% | 90.7% | 1.50 | -27.7% |
| 18 | **TGT** | Consumer Defensive | 86.6 | 4.4% | 25.4% | 32.7% | 71.5% | 1.76 | -19.6% |
| 19 | **INTC** | Technology | 86.3 | 8.9% | -1.6% | 127.1% | 298.4% | 1.84 | -41.9% |
| 20 | **NTAP** | Technology | 85.0 | -7.0% | 12.3% | 92.2% | 66.9% | 0.94 | -24.8% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **RBI.VI** | Financial Services | 94.2 | 4.5% | 37.2% | 72.4% | 127.0% | 2.25 | -18.0% |
| 2 | **AKER.OL** | Industrials | 93.7 | 18.0% | 32.9% | 77.9% | 105.9% | 2.76 | -15.6% |
| 3 | **ATS.VI** | Technology | 93.3 | 16.4% | 22.2% | 238.5% | 652.6% | 2.65 | -50.1% |
| 4 | **CCC.L** | Technology | 91.1 | 7.0% | 25.1% | 64.0% | 100.0% | 2.10 | -16.2% |
| 5 | **TKA.DE** | Basic Materials | 90.4 | 24.1% | 46.2% | 69.5% | 65.9% | 1.26 | -41.4% |
| 6 | **SOI.PA** | Technology | 90.4 | 19.5% | 16.8% | 231.3% | 292.8% | 1.46 | -55.0% |
| 7 | **ABN.AS** | Financial Services | 89.6 | 10.8% | 32.4% | 63.5% | 62.3% | 2.09 | -18.0% |
| 8 | **UNI.MI** | Financial Services | 87.3 | -0.9% | 21.2% | 50.2% | 72.7% | 1.92 | -11.5% |
| 9 | **MT.AS** | Basic Materials | 87.2 | 6.2% | 20.1% | 35.6% | 116.1% | 1.94 | -26.2% |
| 10 | **BBVA.MC** | Financial Services | 87.1 | 3.0% | 31.8% | 37.1% | 60.2% | 1.62 | -18.7% |
| 11 | **PKO.WA** | Financial Services | 87.1 | 8.2% | 27.0% | 46.6% | 61.0% | 2.04 | -19.6% |
| 12 | **PKN.WA** | Energy | 87.0 | 6.4% | 16.8% | 41.6% | 98.7% | 2.19 | -12.3% |
| 13 | **BCP.LS** | Financial Services | 86.7 | 6.5% | 27.9% | 44.4% | 58.4% | 1.98 | -17.0% |
| 14 | **BMPS.MI** | Financial Services | 86.6 | -2.1% | 13.3% | 73.4% | 77.8% | 1.62 | -25.5% |
| 15 | **INGA.AS** | Financial Services | 86.4 | 5.8% | 30.4% | 43.8% | 51.3% | 1.83 | -16.9% |
| 16 | **REP.MC** | Energy | 86.4 | 10.1% | 21.6% | 33.9% | 87.6% | 2.14 | -20.4% |
| 17 | **BG.VI** | Financial Services | 86.3 | -1.1% | 16.9% | 51.4% | 71.6% | 1.94 | -16.3% |
| 18 | **EBP.WA** | Financial Services | 86.3 | 4.1% | 23.9% | 50.6% | 58.7% | 1.74 | -18.4% |
| 19 | **BGEO.L** | Financial Services | 86.3 | 10.1% | 32.1% | 34.1% | 64.3% | 1.85 | -21.0% |
| 20 | **STAN.L** | Financial Services | 86.2 | 3.3% | 28.0% | 40.8% | 58.4% | 1.59 | -20.4% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **EIX** | Utilities | 2.430 | 1.966 | 1.057 | 3.248 | -0.974 | - | 5.9 | +19.7% |
| 2 | **CF** | Materials | 1.589 | 1.011 | 1.295 | 1.704 | 0.563 | - | 10.0 | +29.9% |
| 3 | **NEM** | Materials | 1.559 | 1.292 | 1.719 | 0.902 | 0.452 | - | 15.9 | +25.9% |
| 4 | **SNDK** | Information Technology | 1.475 | 1.867 | 1.561 | 0.347 | -0.073 | - | 23.0 | +91.6% |
| 5 | **TPR** | Consumer Discretionary | 1.390 | 1.863 | 1.149 | 0.593 | -1.030 | - | 15.9 | +197.1% |
| 6 | **APA** | Energy | 1.364 | 1.377 | 1.264 | 0.836 | -0.372 | - | 9.4 | +26.7% |
| 7 | **MO** | Consumer Staples | 1.310 | -0.026 | 2.060 | 1.077 | -0.453 | - | 14.3 | - |
| 8 | **HST** | Real Estate | 1.211 | 1.357 | 0.476 | 1.343 | -0.221 | - | 14.9 | +15.6% |
| 9 | **SYF** | Financials | 1.173 | -0.126 | 1.179 | 1.798 | -0.420 | - | 7.7 | +20.8% |
| 10 | **SPG** | Real Estate | 1.151 | 0.827 | 1.384 | 0.658 | -1.367 | - | 14.4 | +120.5% |
| 11 | **BMY** | Health Care | 1.079 | 0.842 | 0.873 | 1.028 | 0.567 | - | 14.0 | +46.6% |
| 12 | **EXPE** | Consumer Discretionary | 1.065 | 1.536 | 0.798 | 0.451 | -0.705 | - | 17.2 | +89.5% |
| 13 | **ALL** | Financials | 1.005 | 1.054 | 0.415 | 1.160 | 1.166 | - | 5.0 | +46.1% |
| 14 | **TGT** | Consumer Staples | 0.978 | 2.450 | -0.105 | 0.412 | -0.750 | - | 16.2 | +26.4% |
| 15 | **MAS** | Industrials | 0.970 | -0.604 | 1.439 | 1.424 | -0.808 | - | 15.6 | +5862.5% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -1.846 | -1.333 | -0.911 | -2.466 | -1.036 |
| 502 | **COIN** | Financials | -1.678 | -2.611 | -1.706 | 0.000 | -1.702 |
| 501 | **TSLA** | Consumer Discretionary | -1.649 | -0.250 | -1.353 | -2.448 | -0.395 |
| 500 | **KKR** | Financials | -1.597 | -1.600 | -0.847 | -1.662 | -0.850 |
| 499 | **BA** | Industrials | -1.554 | -0.557 | -1.143 | -2.163 | -1.164 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W37.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W37.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-09-07  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
