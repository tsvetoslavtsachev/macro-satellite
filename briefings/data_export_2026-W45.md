# Сателит — пълен data export за 2026-W45

_Период: 2026-11-02 → 2026-11-08_  
_Генериран: 2026-11-08 12:21 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W45.md` (structured briefing) и `narrative_2026-W45.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**18 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **XLE** | -12.00% | -4.34σ | 70.02 | 61.62 | 2026-10-30 | 2026-11-06 | +1.30% | +3.07% | 13 |
| **DBC** | -6.16% | -3.25σ | 33.61 | 31.54 | 2026-10-30 | 2026-11-06 | +1.05% | +2.21% | 13 |
| **USO** | -12.10% | -2.55σ | 168.83 | 148.41 | 2026-10-30 | 2026-11-06 | +2.24% | +5.62% | 13 |
| **XLK** | -8.23% | -2.51σ | 179.51 | 164.74 | 2026-10-30 | 2026-11-06 | +0.24% | +3.37% | 13 |
| **XLC** | +4.89% | +2.37σ | 99.90 | 104.79 | 2026-10-30 | 2026-11-06 | -0.59% | +2.31% | 13 |
| **SPY** | -2.70% | -2.13σ | 755.72 | 735.29 | 2026-10-30 | 2026-11-06 | +0.10% | +1.32% | 13 |
| **QQQ** | -4.98% | -2.03σ | 690.49 | 656.10 | 2026-10-30 | 2026-11-06 | +0.06% | +2.48% | 13 |
| **VNQ** | +1.91% | +1.84σ | 93.94 | 95.73 | 2026-10-30 | 2026-11-06 | -0.39% | +1.25% | 13 |
| **GDX** | +13.63% | +1.66σ | 77.09 | 87.60 | 2026-10-30 | 2026-11-06 | +0.59% | +7.86% | 13 |
| **XLRE** | +1.92% | +1.61σ | 43.17 | 44.00 | 2026-10-30 | 2026-11-06 | -0.32% | +1.39% | 13 |
| **VEA** | -2.22% | -1.60σ | 69.44 | 67.90 | 2026-10-30 | 2026-11-06 | -0.12% | +1.31% | 13 |
| **DBA** | -2.90% | -1.57σ | 26.89 | 26.11 | 2026-10-30 | 2026-11-06 | -0.16% | +1.75% | 13 |
| **GLD** | +4.71% | +1.52σ | 355.78 | 372.52 | 2026-10-30 | 2026-11-06 | -0.28% | +3.28% | 13 |
| **XLI** | -2.83% | -1.43σ | 167.40 | 162.67 | 2026-10-30 | 2026-11-06 | -0.54% | +1.61% | 13 |
| **XLY** | +1.91% | +1.20σ | 115.38 | 117.58 | 2026-10-30 | 2026-11-06 | -0.03% | +1.62% | 13 |
| **SLV** | +5.09% | +1.19σ | 44.60 | 46.87 | 2026-10-30 | 2026-11-06 | -1.09% | +5.21% | 13 |
| **EEM** | -2.80% | -1.16σ | 61.04 | 59.33 | 2026-10-30 | 2026-11-06 | -0.35% | +2.12% | 13 |
| **EFA** | -1.43% | -1.10σ | 103.37 | 101.89 | 2026-10-30 | 2026-11-06 | -0.16% | +1.16% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-11-08 · **Conditions matched:** 2/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | -12.10% | ❌ | 168.83 | 148.41 | 2026-10-30 | 2026-11-06 |
| DFEN | down ≥ 3.0% | -4.83% | ✅ | 47.86 | 45.55 | 2026-10-30 | 2026-11-06 |
| GLD | down ≥ 1.0% | +4.71% | ❌ | 355.78 | 372.52 | 2026-10-30 | 2026-11-06 |
| URA | down ≥ 3.0% | -4.12% | ✅ | 33.73 | 32.34 | 2026-10-30 | 2026-11-06 |
| UUP | up ≥ 0.5% | +0.45% | ❌ | 29.00 | 29.13 | 2026-10-30 | 2026-11-06 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-11-08 · **Conditions matched:** 2/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | -2.03% | ❌ | 279.33 | 273.67 | 2026-10-30 | 2026-11-06 |
| XLF | up ≥ 1.0% | +1.15% | ✅ | 56.51 | 57.16 | 2026-10-30 | 2026-11-06 |
| XLY | up ≥ 1.0% | +1.91% | ✅ | 115.38 | 117.58 | 2026-10-30 | 2026-11-06 |
| GLD | down ≥ 0.5% | +4.71% | ❌ | 355.78 | 372.52 | 2026-10-30 | 2026-11-06 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2025-W05 (week ending 2025-02-02)
**Cosine similarity:** 0.9168 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -4.15% | -5.83% | +3.31% |
| **USO** | -6.04% | -17.96% | -0.72% |
| **GLD** | +4.06% | +15.25% | +19.55% |
| **TLT** | +4.18% | -0.03% | +0.07% |
| **XLE** | -0.76% | -6.46% | -2.34% |
| **IWM** | -8.86% | -11.48% | -5.10% |

### Паралел #2: 2021-W50 (week ending 2021-12-19)
**Cosine similarity:** 0.8733 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -0.73% | -3.34% | -20.44% |
| **USO** | +20.07% | +46.99% | +64.12% |
| **GLD** | +0.95% | +6.85% | +2.07% |
| **TLT** | -7.11% | -11.53% | -25.69% |
| **XLE** | +19.13% | +35.88% | +35.17% |
| **IWM** | -3.40% | -3.66% | -23.22% |

### Паралел #3: 2022-W49 (week ending 2022-12-11)
**Cosine similarity:** 0.8683 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -0.69% | -1.87% | +9.31% |
| **USO** | +4.85% | +6.83% | +0.13% |
| **GLD** | +4.60% | +4.08% | +8.97% |
| **TLT** | -2.20% | -0.70% | -4.15% |
| **XLE** | +6.28% | -0.06% | -1.63% |
| **IWM** | +1.06% | -1.37% | +3.59% |

### Паралел #4: 2024-W44 (week ending 2024-11-03)
**Cosine similarity:** 0.8538 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.76% | +5.39% | -0.75% |
| **USO** | +1.42% | +8.33% | -11.12% |
| **GLD** | -3.38% | +2.41% | +18.03% |
| **TLT** | +2.44% | -3.39% | -3.42% |
| **XLE** | +7.36% | -0.44% | -6.87% |
| **IWM** | +9.61% | +3.42% | -8.45% |

### Паралел #5: 2023-W43 (week ending 2023-10-29)
**Cosine similarity:** 0.8281 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +10.77% | +18.68% | +23.76% |
| **USO** | -9.06% | -6.71% | +2.59% |
| **GLD** | +1.67% | +0.46% | +16.37% |
| **TLT** | +8.43% | +11.15% | +4.59% |
| **XLE** | +0.02% | -0.45% | +13.13% |
| **IWM** | +9.76% | +20.82% | +22.29% |

### Паралел #6: 2024-W36 (week ending 2024-09-08)
**Cosine similarity:** 0.8223 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +6.07% | +12.48% | +6.58% |
| **USO** | +9.95% | +1.90% | +4.58% |
| **GLD** | +5.09% | +5.34% | +16.37% |
| **TLT** | -4.59% | -5.19% | -9.49% |
| **XLE** | +5.88% | +5.82% | +1.65% |
| **IWM** | +4.66% | +14.93% | -0.94% |

### Паралел #7: 2023-W18 (week ending 2023-05-07)
**Cosine similarity:** 0.8205 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.73% | +8.28% | +5.35% |
| **USO** | +1.21% | +17.07% | +18.75% |
| **GLD** | -2.73% | -3.88% | -1.42% |
| **TLT** | -2.37% | -7.97% | -16.46% |
| **XLE** | -0.27% | +8.34% | +8.04% |
| **IWM** | +5.65% | +11.30% | +0.02% |

### Паралел #8: 2021-W33 (week ending 2021-08-22)
**Cosine similarity:** 0.8143 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -2.19% | +5.76% | -2.06% |
| **USO** | +14.16% | +23.83% | +49.07% |
| **GLD** | -0.40% | +3.55% | +6.25% |
| **TLT** | +0.23% | -1.45% | -8.18% |
| **XLE** | +3.18% | +19.13% | +48.29% |
| **IWM** | +0.93% | +7.98% | -7.45% |

### Паралел #9: 2025-W47 (week ending 2025-11-23)
**Cosine similarity:** 0.8090 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.39% | +4.61% | +13.14% |
| **USO** | +1.44% | +16.67% | +103.35% |
| **GLD** | +10.52% | +25.21% | +10.57% |
| **TLT** | -2.23% | -0.10% | -5.39% |
| **XLE** | -0.47% | +22.75% | +33.06% |
| **IWM** | +6.99% | +12.31% | +21.02% |

### Паралел #10: 2022-W07 (week ending 2022-02-20)
**Cosine similarity:** 0.8040 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.54% | -10.27% | -2.78% |
| **USO** | +21.35% | +26.12% | +14.40% |
| **GLD** | +1.26% | -2.87% | -8.13% |
| **TLT** | -6.91% | -14.27% | -18.22% |
| **XLE** | +11.05% | +20.16% | +16.77% |
| **IWM** | +4.03% | -11.73% | -2.42% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 16 · **Total matching days:** 96 · **History:** 2021-05-17 → 2026-11-06

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +1.9% | +2.2% | -3.7% | +7.4% | 69% |
| **SPY** | 3m | 16 | +2.0% | +2.5% | -7.3% | +12.0% | 69% |
| **SPY** | 6m | 16 | +6.0% | +8.6% | -6.8% | +21.8% | 62% |
| **USO** | 1m | 16 | -0.4% | -1.2% | -14.3% | +12.7% | 44% |
| **USO** | 3m | 16 | -0.8% | -5.1% | -18.9% | +30.5% | 44% |
| **USO** | 6m | 16 | +12.7% | +2.1% | -8.7% | +109.4% | 56% |
| **GLD** | 1m | 16 | +2.3% | +0.8% | -3.0% | +9.0% | 69% |
| **GLD** | 3m | 16 | +4.3% | +3.4% | -12.6% | +24.5% | 62% |
| **GLD** | 6m | 16 | +4.6% | +3.4% | -12.5% | +25.3% | 62% |
| **TLT** | 1m | 16 | -1.3% | -1.1% | -6.7% | +3.6% | 38% |
| **TLT** | 3m | 16 | -0.5% | +0.5% | -16.5% | +11.1% | 56% |
| **TLT** | 6m | 16 | -3.7% | -2.7% | -18.0% | +7.5% | 38% |

**Episodes (последни 5 от 16):**
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-08-03` (5d)
- `2026-09-10 → 2026-10-01` (14d)
- `2026-10-16 → 2026-10-27` (8d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 120 · **History:** 2021-05-17 → 2026-11-06

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +6.3% | +6.3% | +3.5% | +9.1% | 100% |
| **SPY** | 3m | 2 | +6.9% | +6.9% | +3.5% | +10.3% | 100% |
| **SPY** | 6m | 2 | +6.4% | +6.4% | -2.2% | +15.0% | 50% |
| **USO** | 1m | 2 | +5.6% | +5.6% | +4.0% | +7.2% | 100% |
| **USO** | 3m | 2 | +8.7% | +8.7% | -9.9% | +27.4% | 50% |
| **USO** | 6m | 2 | +19.5% | +19.5% | +15.5% | +23.5% | 100% |
| **GLD** | 1m | 2 | +3.5% | +3.5% | -0.2% | +7.2% | 50% |
| **GLD** | 3m | 2 | -5.6% | -5.6% | -13.8% | +2.6% | 50% |
| **GLD** | 6m | 2 | -6.7% | -6.7% | -13.5% | +0.1% | 50% |
| **TLT** | 1m | 2 | -1.4% | -1.4% | -1.8% | -1.0% | 0% |
| **TLT** | 3m | 2 | -4.9% | -4.9% | -6.8% | -2.9% | 0% |
| **TLT** | 6m | 2 | -6.9% | -6.9% | -11.2% | -2.6% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-11-04` (73d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 480 · **History:** 2021-05-17 → 2026-11-06

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
- `2025-11-03 → 2026-11-06` (248d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 1 · **Total matching days:** 1 · **History:** 2021-05-17 → 2026-11-06

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | -1.5% | -1.5% | -1.5% | -1.5% | 0% |
| **SPY** | 3m | 1 | -4.7% | -4.7% | -4.7% | -4.7% | 0% |
| **SPY** | 6m | 1 | -4.7% | -4.7% | -4.7% | -4.7% | 0% |
| **USO** | 1m | 1 | +14.3% | +14.3% | +14.3% | +14.3% | 100% |
| **USO** | 3m | 1 | +0.1% | +0.1% | +0.1% | +0.1% | 100% |
| **USO** | 6m | 1 | +0.1% | +0.1% | +0.1% | +0.1% | 100% |
| **GLD** | 1m | 1 | -6.8% | -6.8% | -6.8% | -6.8% | 0% |
| **GLD** | 3m | 1 | -5.3% | -5.3% | -5.3% | -5.3% | 0% |
| **GLD** | 6m | 1 | -5.3% | -5.3% | -5.3% | -5.3% | 0% |
| **TLT** | 1m | 1 | +2.5% | +2.5% | +2.5% | +2.5% | 100% |
| **TLT** | 3m | 1 | +3.3% | +3.3% | +3.3% | +3.3% | 100% |
| **TLT** | 6m | 1 | +3.3% | +3.3% | +3.3% | +3.3% | 100% |

**Episodes (последни 5 от 1):**
- `2026-09-25 → 2026-09-25` (1d)

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 10 · **Total matching days:** 101 · **History:** 2021-05-17 → 2026-11-06

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 10 | -0.1% | +0.6% | -7.2% | +7.8% | 60% |
| **SPY** | 3m | 10 | +1.5% | -0.0% | -8.3% | +11.6% | 50% |
| **SPY** | 6m | 10 | +0.3% | +1.3% | -20.8% | +14.2% | 50% |
| **USO** | 1m | 10 | +4.1% | +0.5% | -15.0% | +52.9% | 50% |
| **USO** | 3m | 10 | +10.2% | +8.1% | -20.7% | +52.2% | 60% |
| **USO** | 6m | 10 | +11.4% | +4.9% | -27.6% | +56.3% | 60% |
| **GLD** | 1m | 10 | -1.2% | -1.9% | -8.3% | +11.7% | 20% |
| **GLD** | 3m | 10 | -1.8% | -1.4% | -12.0% | +6.4% | 40% |
| **GLD** | 6m | 10 | -1.1% | -3.2% | -15.2% | +25.0% | 30% |
| **TLT** | 1m | 10 | -2.4% | -2.7% | -6.0% | +2.5% | 10% |
| **TLT** | 3m | 10 | -5.9% | -4.9% | -17.6% | +4.2% | 30% |
| **TLT** | 6m | 10 | -9.2% | -8.1% | -22.3% | +1.2% | 20% |

**Episodes (последни 5 от 10):**
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-05-19` (36d)
- `2026-07-22 → 2026-08-03` (8d)
- `2026-09-01 → 2026-09-28` (15d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 17 · **Total matching days:** 294 · **History:** 2021-05-17 → 2026-11-06

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 17 | +1.9% | +1.6% | -4.8% | +9.0% | 71% |
| **SPY** | 3m | 17 | +2.8% | +4.2% | -12.6% | +16.2% | 71% |
| **SPY** | 6m | 17 | +6.2% | +8.1% | -14.0% | +21.0% | 76% |
| **USO** | 1m | 17 | +2.4% | -2.2% | -13.0% | +22.9% | 41% |
| **USO** | 3m | 17 | +3.4% | -0.8% | -14.5% | +29.9% | 41% |
| **USO** | 6m | 17 | +14.2% | +2.6% | -12.4% | +87.1% | 71% |
| **GLD** | 1m | 17 | +2.4% | +2.1% | -5.6% | +9.0% | 76% |
| **GLD** | 3m | 17 | +5.5% | +7.2% | -16.8% | +23.6% | 65% |
| **GLD** | 6m | 17 | +10.0% | +9.8% | -14.1% | +43.8% | 71% |
| **TLT** | 1m | 17 | +0.3% | -0.0% | -6.3% | +8.2% | 47% |
| **TLT** | 3m | 17 | -1.5% | -1.1% | -15.3% | +11.9% | 35% |
| **TLT** | 6m | 17 | -4.6% | -1.7% | -21.3% | +7.0% | 35% |

**Episodes (последни 5 от 17):**
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)
- `2026-08-07 → 2026-09-03` (19d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 20 · **Total matching days:** 304 · **History:** 2021-05-17 → 2026-11-06

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 20 | +0.3% | +0.5% | -8.7% | +7.0% | 50% |
| **SPY** | 3m | 20 | +1.8% | +3.2% | -13.7% | +9.1% | 65% |
| **SPY** | 6m | 20 | +2.7% | +4.0% | -16.4% | +16.9% | 65% |
| **USO** | 1m | 20 | -0.2% | -3.7% | -21.8% | +55.8% | 45% |
| **USO** | 3m | 20 | +3.7% | -0.2% | -12.7% | +64.3% | 50% |
| **USO** | 6m | 20 | +8.6% | +2.6% | -16.0% | +75.1% | 55% |
| **GLD** | 1m | 20 | -0.8% | -0.2% | -12.4% | +7.6% | 45% |
| **GLD** | 3m | 20 | +1.5% | +1.5% | -13.7% | +19.0% | 65% |
| **GLD** | 6m | 20 | +7.0% | +4.3% | -15.8% | +55.5% | 65% |
| **TLT** | 1m | 20 | -0.2% | -0.1% | -5.6% | +5.2% | 45% |
| **TLT** | 3m | 20 | -3.4% | -3.9% | -17.3% | +8.7% | 35% |
| **TLT** | 6m | 20 | -6.5% | -5.5% | -21.4% | +4.6% | 25% |

**Episodes (последни 5 от 20):**
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (13d)
- `2026-09-21 → 2026-10-15` (16d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-11-06

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (10 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **US_PMI_COMPOSITE** | S&P Global US Composite PMI | growth | diffusion_indices | 4 | 2.60 | 2.60 | 2026-10-10 00:00:00 | 2026-11-07 00:00:00 | ✓ |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 4 | 2.59 | 2.75 | 2026-10-10 00:00:00 | 2026-11-07 00:00:00 | ✓ |
| **US_PMI_SVCS** | S&P Global US Services PMI | growth | diffusion_indices | 4 | 2.09 | 2.09 | 2026-10-10 00:00:00 | 2026-11-07 00:00:00 | ✓ |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 4 | 2.07 | 2.07 | 2026-10-10 00:00:00 | 2026-11-07 00:00:00 | ✓ |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 3 | 2.43 | 2.43 | 2026-10-17 00:00:00 | 2026-11-07 00:00:00 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | 3 | 2.06 | 2.06 | 2026-10-17 00:00:00 | 2026-11-07 00:00:00 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | 3 | 2.02 | 2.02 | 2026-10-10 00:00:00 | 2026-10-24 00:00:00 | ✓ |
| **COMPUTSA** | Завършени жилища (SAAR) | growth | housing_supply | 2 | 2.95 | 2.95 | 2026-10-10 00:00:00 | 2026-10-17 00:00:00 | ✓ |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 2 | 2.16 | 2.16 | 2026-10-24 00:00:00 | 2026-11-07 00:00:00 | - |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 1 | 2.06 | 2.06 | 2026-10-10 00:00:00 | 2026-10-10 00:00:00 | - |

### EU (8 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 4 | 5.50 | 5.60 | 2026-10-10 00:00:00 | 2026-11-07 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 4 | 2.39 | 2.45 | 2026-10-10 00:00:00 | 2026-11-07 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 4 | 2.22 | 2.25 | 2026-10-10 00:00:00 | 2026-11-07 00:00:00 | ✓ |
| **EA_OAT_BUND_SPREAD** | OAT-Bund spread (FR-DE 10Y, pp) | credit | sovereign_spreads | 3 | 2.48 | 2.48 | 2026-10-17 00:00:00 | 2026-11-07 00:00:00 | ✓ |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | 3 | 2.18 | 2.18 | 2026-10-17 00:00:00 | 2026-11-07 00:00:00 | - |
| **EA_EMPLOYMENT_PERSONS** | Заетост — брой наети (нац. сметки, EA-20, хил. лица) | labor | employment | 2 | 2.01 | 2.01 | 2026-10-24 00:00:00 | 2026-11-07 00:00:00 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation | sentiment | 1 | 2.28 | 2.28 | 2026-11-07 00:00:00 | 2026-11-07 00:00:00 | - |
| **EA_HICP_ENERGY** | HICP енергия, YoY | inflation | headline_measures | 1 | 2.16 | 2.16 | 2026-11-07 00:00:00 | 2026-11-07 00:00:00 | - |

### CN (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 6 | 2.54 | 2.54 | 2026-10-10 00:00:00 | 2026-11-07 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 6 | 2.23 | 2.23 | 2026-10-10 00:00:00 | 2026-11-07 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 6 | 2.19 | 2.19 | 2026-10-10 00:00:00 | 2026-11-07 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-11-07 00:00:00 · **Generated:** 2026-11-07 08:47:27.549745+00:00

**Режим:** `policy_dilemma` (Policy dilemma)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 44.2 | mixed | 37.0% | 1 | 1 |
| **growth** | 49.1 | mixed | 56.0% | 3 | 3 |
| **inflation** | 40.0 | mixed | 44.4% | 4 | 1 |
| **liquidity** | 39.8 | mixed | 31.6% | 0 | 0 |

### Top anomalies (7 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **US_PMI_COMPOSITE** | S&P Global US Composite PMI | growth | diffusion_indices | +2.60 | up | 58.40 | 2026-09-01 | ✓ max |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | +2.43 | up | 6.35 | 2026-09-01 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | +2.16 | up | 4.60 | 2026-09-01 | - |
| **US_PMI_SVCS** | S&P Global US Services PMI | growth | diffusion_indices | +2.09 | up | 58.80 | 2026-09-01 | ✓ max |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.08 | down | 93.73 | 2026-07-01 | ✓ min |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | +2.07 | up | 55.90 | 2026-09-01 | ✓ max |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | +2.06 | up | 5.08 | 2026-09-01 | - |

### Narrative hints от макро лещите
- **US_PMI_COMPOSITE**: Markit композит — global benchmark, complement към ISM. Flash + final estimates.
- **PPIFIS**: Производствени цени → consumer prices с 1-3 месечен lag. Водещ за CPI при трендови промени.
- **MICH_INFL_1Y**: Household очаквания. По-шумни от market-based, но по-ранни. Extreme movements сигнализират de-anchoring risk.
- **US_PMI_SVCS**: Markit services — global comparable. ISM Services има различна methodology.
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **US_PMI_MFG**: Markit mfg — comparable cross-country. ISM е US-only.
- **CPI_GOODS**: Goods inflation реагира бързо на supply shocks. 2022 peak след доставъчните кризи. Сега често е в deflation/близо до 0.

### Cross-lens divergences (6 entries)
- 🔔 **?**
  - `pair_id`: stagflation_test
  - `name_bg`: Labor tightness × Inflation pressure
  - `question_bg`: Дали labor tightness потвърждава inflation pressure (стагфлация)?
  - `state`: a_down_b_up
  - `interpretation`: Policy dilemma — labor loose, но inflation still hot.
  - `slot_a_label`: Labor tightness
  - `slot_b_label`: Inflation pressure
  - `breadth_a`: 0.1
  - `breadth_b`: 1.0
  - `state_raw`: transition
  - `breadth_a_raw`: 0.6
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
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.667
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
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.333
- 🔔 **?**
  - `pair_id`: credit_policy_transmission
  - `name_bg`: Credit spreads × Policy rates
  - `question_bg`: Дали credit следва policy направление — transmission intact?
  - `state`: both_up
  - `interpretation`: Tightening transmits — rates up + credit widens.
  - `slot_a_label`: Credit stress
  - `slot_b_label`: Policy tightening
  - `breadth_a`: 1.0
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.667
- 🔔 **?**
  - `pair_id`: sentiment_vs_hard_data
  - `name_bg`: Consumer sentiment × Hard activity
  - `question_bg`: Дали sentiment потвърждава hard data, или има разминаване?
  - `state`: transition
  - `interpretation`: Monitoring — divergence typical в political transitions.
  - `slot_a_label`: Consumer sentiment
  - `slot_b_label`: Hard activity
  - `breadth_a`: 0.333
  - `breadth_b`: 0.6
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.333
  - `breadth_b_raw`: 1.0
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
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.333

### Executive narrative
> Policy dilemma — labor market е loose, но инфлацията remains hot. Fed е заклещен между двата мандата. Най-отклонена леща: Инфлация и цени — breadth 83% (разширяване), 4 аномалии, 1 нови екстремума. Обаче inflation expectations остават anchored — Fed narrative-ът за момента държи. За наблюдение следващия релиз: US_PMI_COMPOSITE, US_PMI_SVCS, LABOR_SHARE_NBS (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: US_PMI_COMPOSITE z=+2.60 · NEW-5Y-MAX
- 4 нови екстремуми в top-7 (lookback 5г.)
- Активни двойки: Stagflation test=a_down_b_up; Inflation anchoring=a_up_b_down; Credit × Policy=both_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-11-07 00:00:00 · **Generated:** 2026-11-07 09:14:00.344957+00:00

**Режим:** `transition` (Преходно / смесено)  
**Primary driver:** `none`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 38.7 | mixed | 42.9% | 1 | 0 |
| **growth** | 46.2 | mixed | 16.7% | 1 | 0 |
| **inflation** | 38.8 | mixed | 42.9% | 2 | 0 |
| **credit** | 43.8 | mixed | 36.8% | 4 | 3 |
| **external** | 70.6 | expanding | 50.0% | 1 | 0 |

### Top anomalies (8 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | +5.21 | up | 3.39 | 2026-10-01 | - |
| **EA_OAT_BUND_SPREAD** | OAT-Bund spread (FR-DE 10Y, pp) | credit | sovereign_spreads | +2.48 | up | 0.97 | 2026-09-01 | ✓ max |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | +2.45 | up | 4.44 | 2026-09-01 | ✓ max |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation, growth | sentiment | +2.28 | up | 24.80 | 2026-10-01 | - |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | +2.25 | up | 3.47 | 2026-09-01 | ✓ max |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | -2.18 | down | -6826.60 | 2026-08-01 | - |
| **EA_HICP_ENERGY** | HICP енергия, YoY | inflation | headline_measures | +2.16 | up | 20.80 | 2026-10-01 | - |
| **EA_EMPLOYMENT_PERSONS** | Заетост — брой наети (нац. сметки, EA-20, хил. лица) | labor | employment | -2.01 | down | 0.52 | 2026-04-01 | - |

### Narrative hints от макро лещите
- **EA_BUND_2Y**: EA-aggregate 2Y yield. Curve slope (10Y-2Y) проксира policy expectations и recession risk.
- **EA_OAT_BUND_SPREAD**: Core-but-not-DE EA stress proxy. Captures France-specific stress (e.g., 2024 budget crisis).
- **FR_10Y**: France sovereign yield — компонент на OAT-Bund spread. Core-but-not-DE EA stress indicator.
- **EA_SELLING_PRICE_EXP**: Forward-looking inflation сигнал от business side — мениджърите казват дали ще вдигат цени. Изпреварва HICP с 3-6 месеца.
- **DE_10Y**: Germany 10Y, Maastricht-criterion measure. Reference за BTP-Bund / OAT-Bund spread изчисления.
- **EA_TRADE_BALANCE**: Стоковият баланс с третите страни. Срив към дефицит (2022) = енергийната сметка изпреварва износа. Полярност +1.
- **EA_HICP_ENERGY**: Volatile component на headline. Oil shock dependent. Headline-core gap explainer; de-singleton-ва headline_measures.
- **EA_EMPLOYMENT_PERSONS**: Домашна концепция за заетост (брой наети) от тримесечните нац. сметки. Допълва employment RATE (EA_LFS_EMP) с обемен сигнал — същата полярност. De-singleton-ва employment.

### Cross-lens divergences (7 entries)
- 🔔 **?**
  - `pair_id`: stagflation_test
  - `name_bg`: Стагфлационен тест
  - `question_bg`: Заплатите ли движат услугите нагоре?
  - `state`: transition
  - `interpretation`: Смесена картина — изчакай confirm на trend.
  - `slot_a_label`: Натиск от заплати
  - `slot_b_label`: Базова/услуги инфлация
  - `breadth_a`: 0.0
  - `breadth_b`: 0.5
  - `state_raw`: transition
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.5
- 🔔 **?**
  - `pair_id`: ecb_transmission
  - `name_bg`: Трансмисия на ЕЦБ политиката
  - `question_bg`: ЕЦБ hike-овете стигат ли до банковото кредитиране?
  - `state`: transition
  - `interpretation`: Смесена картина — типично около policy turning points.
  - `slot_a_label`: Политика (реална лихва + баланс)
  - `slot_b_label`: Банково кредитиране (свиване)
  - `breadth_a`: 0.5
  - `breadth_b`: 0.5
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 0.5
- 🔔 **?**
  - `pair_id`: fragmentation_risk
  - `name_bg`: Фрагментационен риск
  - `question_bg`: ЕЦБ hike-овете разширяват ли периферните spreads?
  - `state`: transition
  - `interpretation`: Mixed signals — гледай individual country drivers.
  - `slot_a_label`: Политика (реална лихва + баланс)
  - `slot_b_label`: Sovereign spreads (BTP/OAT-Bund)
  - `breadth_a`: 0.5
  - `breadth_b`: 1.0
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 1.0
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
  - `breadth_b`: 0.5
  - `state_raw`: insufficient_data
  - `breadth_a_raw`: None
  - `breadth_b_raw`: 0.5
- 🔔 **?**
  - `pair_id`: sentiment_vs_hard_data
  - `name_bg`: Очаквания срещу твърди данни
  - `question_bg`: Sentiment отразява ли реалната икономика?
  - `state`: both_down
  - `interpretation`: Broad-based weakness: sentiment + activity и двете слизат. Recession watch.
  - `slot_a_label`: Sentiment (ESI, confidence)
  - `slot_b_label`: Hard activity (IP, retail, GDP)
  - `breadth_a`: 0.333
  - `breadth_b`: 0.25
  - `state_raw`: transition
  - `breadth_a_raw`: 0.333
  - `breadth_b_raw`: 0.5
- 🔔 **?**
  - `pair_id`: growth_labor_lead_lag
  - `name_bg`: Растеж срещу труд (lead-lag)
  - `question_bg`: Активността и пазарът на труда движат ли се заедно?
  - `state`: transition
  - `interpretation`: Смесена картина — изчакай alignment на двата блока.
  - `slot_a_label`: Твърда активност (IP, retail, GDP)
  - `slot_b_label`: Пазар на труда (сила)
  - `breadth_a`: 0.25
  - `breadth_b`: 0.5
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 0.5

### Executive narrative
> Сигналите са в преход — няма доминираща конфигурация. Следващите 2-3 релиза ще ориентират посоката. Най-отклонена леща: Инфлация и цени — breadth 75% (смесено), 2 аномалии, 0 нови екстремума. За наблюдение следващия релиз: EA_OAT_BUND_SPREAD, FR_10Y, DE_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.21
- 3 нови екстремуми в top-8 (lookback 5г.)
- Активни двойки: Sentiment × Hard=both_down



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-11-07 00:00:00 · **Generated:** 2026-11-07 09:24:36.435737+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 38.4 | mixed | -% | - | - |
| **inflation** | 41.7 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 45.7 | mixed | -% | - | - |
| **property** | 31.1 | contracting | -% | - | - |

### Top anomalies (3 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | -2.53 | down | 3.00 | 2026-10-20 | ✓ min |
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
  - `state`: both_up
  - `interpretation`: Балансиран растеж — и износ, и вътрешно търсене се разширяват.
  - `slot_a_label`: Външно търсене
  - `slot_b_label`: Вътрешна активност
  - `breadth_a`: 0.667
  - `breadth_b`: 0.667

### Executive narrative
> Претеглен композитен macro score 37.3/100 → режим „ВЛОШАВАЩ СЕ“ (5/5 лещи). 5 лещи, 3 flagged аномалии (3 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-11-06 |
| `as_of` | 2026-11-06 |
| `regime` | GROWTH |
| `alignment_score` | 4.0 |
| `gms_score` | 0.0 |
| `gms_max` | 8 |
| `gms_tier` | LOW |
| `ks_status` | inactive |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-11-03 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **soymeal** | Commodities | 111668 | 96.0 | 96.0 | 1065 | -95136 |
| **sugar** | Commodities | 223895 | 93.2 | 93.2 | 1065 | -33469 |
| **rbob** | Commodities | 86963 | 91.6 | 91.6 | 1065 | -9849 |
| **aud** | FX | 50106 | 82.3 | 82.3 | 1065 | -4027 |
| **copper** | Commodities | 34444 | 78.2 | 78.2 | 1065 | -27021 |
| **soybeans** | Commodities | 132799 | 76.5 | 76.5 | 1065 | -118861 |
| **cotton** | Commodities | 53148 | 71.8 | 71.8 | 1065 | -10689 |
| **dxy** | FX | 3311 | 68.9 | 68.9 | 1065 | 2447 |
| **bitcoin** | Crypto | -2591 | 67.6 | 67.6 | 448 | 4261 |
| **gbpfx** | FX | 26663 | 67.1 | 67.1 | 1065 | 14231 |
| **soyoil** | Commodities | 40377 | 62.1 | 62.1 | 1065 | -59070 |
| **nasdaq** | US Equities | 10073 | 60.9 | 60.9 | 1065 | 29285 |
| **jpy** | FX | -14817 | 58.3 | 58.3 | 1065 | 10226 |
| **vix** | Volatility | -31479 | 58.3 | 58.3 | 1024 | -36973 |
| **coffee** | Commodities | 9605 | 47.1 | 47.1 | 1065 | -4324 |
| **cattle** | Commodities | 51692 | 44.0 | 44.0 | 1065 | 772 |
| **gold** | Commodities | 104297 | 42.2 | 42.2 | 1065 | -10523 |
| **russell** | US Equities | -55080 | 40.4 | 40.4 | 601 | 50237 |
| **brent** | Commodities | 3636 | 39.9 | 39.9 | 248 | 1225 |
| **heatingoil** | Commodities | 7120 | 36.1 | 36.1 | 1065 | -3833 |
| **us30y** | Rates | -166257 | 33.5 | 33.5 | 1065 | 23421 |
| **corn** | Commodities | -22900 | 30.8 | 30.8 | 1065 | -340259 |
| **sp500** | US Equities | -372318 | 28.4 | 28.4 | 1065 | 42769 |
| **eurfx** | FX | -78559 | 21.2 | 21.2 | 1065 | -34298 |
| **usultra10y** | Rates | -258101 | 18.4 | 18.4 | 555 | 60960 |
| **us2y** | Rates | -1450892 | 14.6 | 14.6 | 1065 | -193408 |
| **wti** | Commodities | 85303 | 14.4 | 14.4 | 1065 | -19188 |
| **platinum** | Commodities | -1076 | 14.2 | 14.2 | 1065 | -9193 |
| **silver** | Commodities | 2665 | 14.0 | 14.0 | 1065 | -4943 |
| **cocoa** | Commodities | -14214 | 12.3 | 12.3 | 1065 | 280 |
| **wheat** | Commodities | -88726 | 11.9 | 11.9 | 1065 | -59183 |
| **chf** | FX | -16845 | 10.2 | 10.2 | 1065 | -5495 |
| **us5y** | Rates | -2315516 | 10.2 | 10.2 | 1065 | -187949 |
| **natgas** | Commodities | -224495 | 2.2 | 2.2 | 1065 | -79814 |
| **us10y** | Rates | -2262310 | 2.2 | 2.2 | 1065 | -122525 |
| **cad** | FX | -86302 | 2.1 | 2.1 | 1065 | -6677 |
| **palladium** | Commodities | -15363 | 0.5 | 0.5 | 1065 | -5842 |
| **hogs** | Commodities | -50492 | 0.1 | 0.1 | 1065 | -15220 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MRNA** | Healthcare | 97.8 | 29.0% | 325.0% | 367.7% | 736.2% | 1.80 | -34.2% |
| 2 | **MPC** | Energy | 90.0 | -19.6% | 16.7% | 53.2% | 153.0% | 1.79 | -23.1% |
| 3 | **CRL** | Healthcare | 89.5 | 13.3% | 21.9% | 90.0% | 77.7% | 1.39 | -33.9% |
| 4 | **RVTY** | Healthcare | 88.5 | 2.0% | 33.7% | 53.6% | 64.5% | 1.18 | -30.1% |
| 5 | **OKTA** | Technology | 88.0 | -23.4% | 11.9% | 101.1% | 152.7% | 0.92 | -33.1% |
| 6 | **PSX** | Energy | 87.9 | -12.7% | 14.6% | 45.0% | 113.3% | 1.74 | -17.4% |
| 7 | **VLO** | Energy | 87.0 | -21.9% | 10.0% | 45.0% | 166.4% | 1.75 | -24.6% |
| 8 | **ILMN** | Healthcare | 85.6 | -19.4% | 11.1% | 50.2% | 116.1% | 1.04 | -29.2% |
| 9 | **MRK** | Healthcare | 84.2 | 3.1% | 12.7% | 33.5% | 73.7% | 1.81 | -11.4% |
| 10 | **APA** | Energy | 82.2 | -1.4% | 9.3% | 27.0% | 114.8% | 1.55 | -27.7% |
| 11 | **HUM** | Healthcare | 82.1 | 12.3% | 12.7% | 58.5% | 47.7% | 0.97 | -44.9% |
| 12 | **VTRS** | Healthcare | 81.6 | 14.2% | 23.2% | 17.7% | 68.0% | 1.86 | -19.0% |
| 13 | **BDX** | Healthcare | 81.1 | 15.9% | 18.6% | 43.6% | 35.1% | 1.53 | -23.1% |
| 14 | **CRWD** | Technology | 81.1 | -17.5% | -3.7% | 64.4% | 97.0% | 0.78 | -37.2% |
| 15 | **CPAY** | Financial Services | 80.3 | 13.2% | 13.5% | 32.3% | 53.6% | 1.41 | -20.2% |
| 16 | **TGT** | Consumer Defensive | 79.9 | 2.4% | 5.0% | 28.6% | 75.1% | 1.72 | -13.3% |
| 17 | **ABBV** | Healthcare | 79.7 | 7.6% | 18.2% | 46.5% | 28.6% | 1.10 | -15.7% |
| 18 | **BIIB** | Healthcare | 79.2 | 13.7% | 19.9% | 28.4% | 42.4% | 1.27 | -14.3% |
| 19 | **SWK** | Industrials | 78.3 | 28.8% | 12.9% | 44.4% | 33.6% | 1.31 | -26.1% |
| 20 | **COP** | Energy | 78.0 | 1.6% | 11.5% | 21.4% | 57.8% | 1.35 | -22.3% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **TECN.SW** | Healthcare | 91.3 | 12.3% | 42.2% | 90.5% | 67.2% | 1.53 | -28.4% |
| 2 | **MOH.AT** | Energy | 89.7 | -10.5% | 13.2% | 68.3% | 170.7% | 2.56 | -14.9% |
| 3 | **GMAB.CO** | Healthcare | 87.8 | 46.2% | 82.5% | 106.7% | 35.2% | 1.48 | -32.3% |
| 4 | **ALE.WA** | Consumer Cyclical | 87.7 | 17.6% | 29.4% | 106.5% | 47.4% | 1.76 | -26.5% |
| 5 | **MAERSK-B.CO** | Industrials | 87.1 | -15.0% | 21.3% | 49.7% | 89.1% | 1.13 | -22.9% |
| 6 | **DEMANT.CO** | Healthcare | 87.0 | 17.3% | 36.1% | 58.4% | 47.3% | 1.56 | -26.8% |
| 7 | **BFT.WA** | Industrials | 85.9 | 16.4% | 12.8% | 55.8% | 71.5% | 2.38 | -17.4% |
| 8 | **BME.L** | Consumer Cyclical | 85.5 | 11.0% | 20.8% | 69.5% | 55.1% | 1.27 | -40.1% |
| 9 | **REP.MC** | Energy | 85.4 | 5.5% | 17.4% | 37.7% | 84.0% | 1.84 | -20.4% |
| 10 | **BAYN.DE** | Healthcare | 84.9 | 27.9% | 14.2% | 48.1% | 66.3% | 1.72 | -30.6% |
| 11 | **DSFIR.AS** | Basic Materials | 84.9 | 13.1% | 20.1% | 71.0% | 47.8% | 1.56 | -27.0% |
| 12 | **ORNBV.HE** | Healthcare | 84.5 | 23.3% | 29.6% | 52.3% | 40.1% | 1.68 | -18.0% |
| 13 | **FRO.OL** | Energy | 83.6 | -13.4% | 18.5% | 26.1% | 108.4% | 1.31 | -21.7% |
| 14 | **LOTB.BR** | Consumer Defensive | 83.2 | 13.2% | 14.1% | 35.2% | 65.3% | 2.47 | -11.9% |
| 15 | **ERF.PA** | Healthcare | 82.4 | 16.4% | 27.1% | 51.4% | 33.5% | 1.51 | -20.4% |
| 16 | **KNIN.SW** | Industrials | 82.3 | 5.0% | 19.1% | 35.2% | 54.1% | 1.61 | -13.6% |
| 17 | **EBP.WA** | Financial Services | 82.0 | -0.7% | 8.1% | 39.3% | 73.4% | 1.84 | -10.9% |
| 18 | **EVK.DE** | Basic Materials | 82.0 | 2.9% | 19.8% | 28.2% | 60.0% | 1.74 | -16.2% |
| 19 | **OMV.VI** | Energy | 81.5 | 2.2% | 15.8% | 29.0% | 61.1% | 1.97 | -10.8% |
| 20 | **DB1.DE** | Financial Services | 81.2 | 12.1% | 18.8% | 35.9% | 41.0% | 1.92 | -11.8% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **SNDK** | Information Technology | 2.059 | 1.665 | 1.798 | 1.685 | -0.091 | - | 6.7 | +141.2% |
| 2 | **EIX** | Utilities | 1.621 | 0.342 | 0.749 | 2.890 | -0.907 | - | 6.3 | +18.8% |
| 3 | **MO** | Consumer Staples | 1.540 | 1.195 | 1.807 | 0.790 | -0.133 | - | 15.7 | - |
| 4 | **NEM** | Materials | 1.464 | 0.997 | 1.646 | 0.946 | 0.545 | - | 14.0 | +27.3% |
| 5 | **CF** | Materials | 1.425 | 0.795 | 1.143 | 1.586 | 0.428 | - | 8.4 | +30.9% |
| 6 | **MU** | Information Technology | 1.424 | 1.449 | 1.331 | 0.824 | -0.362 | - | 9.3 | +88.3% |
| 7 | **VLO** | Energy | 1.211 | 1.405 | 0.507 | 1.259 | -0.380 | - | 7.9 | +46.9% |
| 8 | **APA** | Energy | 1.189 | 1.094 | 1.161 | 0.731 | 0.139 | - | 7.3 | +33.3% |
| 9 | **WDC** | Information Technology | 1.107 | 1.106 | 0.945 | 0.762 | -0.618 | - | 9.3 | +129.6% |
| 10 | **EXPE** | Consumer Discretionary | 1.105 | 1.301 | 0.740 | 0.823 | -0.628 | - | 15.2 | +76.8% |
| 11 | **MPC** | Energy | 1.095 | 1.350 | 0.440 | 1.094 | -0.972 | - | 7.4 | +60.5% |
| 12 | **SYF** | Financials | 1.090 | -0.379 | 1.225 | 1.649 | -0.222 | - | 7.7 | +19.8% |
| 13 | **HST** | Real Estate | 1.079 | 2.207 | -0.143 | 0.993 | -0.349 | - | 18.2 | +14.2% |
| 14 | **DVA** | Health Care | 1.052 | 1.000 | 0.165 | 1.588 | -1.308 | - | 14.5 | +96.8% |
| 15 | **SPG** | Real Estate | 1.036 | 0.806 | 1.408 | 0.317 | -1.031 | - | 16.5 | +129.4% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -2.111 | -1.693 | -1.133 | -2.502 | -1.242 |
| 502 | **TSLA** | Consumer Discretionary | -1.876 | -0.746 | -1.235 | -2.601 | -0.298 |
| 501 | **ARES** | Financials | -1.664 | -1.525 | -1.229 | -1.432 | -1.219 |
| 500 | **BA** | Industrials | -1.603 | -0.591 | -2.073 | -1.118 | -1.100 |
| 499 | **BLDR** | Industrials | -1.601 | -2.282 | -1.335 | -0.527 | -1.062 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W45.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W45.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\macro\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-11-02  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
