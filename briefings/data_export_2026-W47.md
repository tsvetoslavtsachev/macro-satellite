# Сателит — пълен data export за 2026-W47

_Период: 2026-11-16 → 2026-11-22_  
_Генериран: 2026-11-20 14:59 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W47.md` (structured briefing) и `narrative_2026-W47.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**21 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **DIA** | -4.09% | -3.54σ | 523.15 | 501.73 | 2026-11-13 | 2026-11-18 | -0.19% | +1.10% | 13 |
| **EFA** | -3.75% | -3.13σ | 104.17 | 100.26 | 2026-11-13 | 2026-11-18 | -0.32% | +1.10% | 13 |
| **VWO** | -4.65% | -2.97σ | 56.38 | 53.76 | 2026-11-13 | 2026-11-18 | -0.48% | +1.40% | 13 |
| **VEA** | -3.97% | -2.93σ | 69.44 | 66.68 | 2026-11-13 | 2026-11-18 | -0.44% | +1.21% | 13 |
| **XLF** | -3.85% | -2.32σ | 58.68 | 56.42 | 2026-11-13 | 2026-11-18 | +0.08% | +1.70% | 13 |
| **SPY** | -3.20% | -2.22σ | 754.37 | 730.20 | 2026-11-13 | 2026-11-18 | -0.21% | +1.35% | 13 |
| **XLV** | -4.07% | -2.14σ | 188.85 | 181.17 | 2026-11-13 | 2026-11-18 | +0.96% | +2.35% | 13 |
| **EEM** | -4.99% | -1.99σ | 60.92 | 57.88 | 2026-11-13 | 2026-11-18 | -0.66% | +2.17% | 13 |
| **XLB** | -3.39% | -1.85σ | 52.23 | 50.46 | 2026-11-13 | 2026-11-18 | -0.03% | +1.81% | 13 |
| **URA** | -7.60% | -1.80σ | 31.84 | 29.42 | 2026-11-13 | 2026-11-18 | -2.57% | +2.79% | 13 |
| **DBC** | -4.16% | -1.56σ | 30.79 | 29.51 | 2026-11-13 | 2026-11-18 | +0.24% | +2.82% | 13 |
| **XLE** | -5.65% | -1.41σ | 64.96 | 61.29 | 2026-11-13 | 2026-11-18 | +0.47% | +4.33% | 13 |
| **IBIT** | -9.19% | -1.40σ | 38.94 | 35.36 | 2026-11-13 | 2026-11-18 | +0.93% | +7.24% | 13 |
| **IWM** | -2.67% | -1.31σ | 277.54 | 270.12 | 2026-11-13 | 2026-11-18 | -0.71% | +1.50% | 13 |
| **USO** | -6.51% | -1.28σ | 145.58 | 136.11 | 2026-11-13 | 2026-11-18 | +1.26% | +6.05% | 13 |
| **SLV** | -7.77% | -1.25σ | 44.13 | 40.70 | 2026-11-13 | 2026-11-18 | -2.04% | +4.60% | 13 |
| **SHY** | +0.21% | +1.23σ | 81.17 | 81.34 | 2026-11-13 | 2026-11-18 | -0.08% | +0.23% | 13 |
| **GDX** | -8.35% | -1.17σ | 81.64 | 74.82 | 2026-11-13 | 2026-11-18 | -0.53% | +6.69% | 13 |
| **IEF** | +0.70% | +1.09σ | 90.04 | 90.67 | 2026-11-13 | 2026-11-18 | -0.25% | +0.87% | 13 |
| **GLD** | -4.01% | -1.03σ | 355.45 | 341.19 | 2026-11-13 | 2026-11-18 | -0.89% | +3.05% | 13 |
| **XLRE** | -1.69% | -1.02σ | 44.37 | 43.62 | 2026-11-13 | 2026-11-18 | -0.14% | +1.52% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-11-22 · **Conditions matched:** 3/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | -6.51% | ❌ | 145.58 | 136.11 | 2026-11-13 | 2026-11-18 |
| DFEN | down ≥ 3.0% | -8.73% | ✅ | 50.27 | 45.88 | 2026-11-13 | 2026-11-18 |
| GLD | down ≥ 1.0% | -4.01% | ✅ | 355.45 | 341.19 | 2026-11-13 | 2026-11-18 |
| URA | down ≥ 3.0% | -7.60% | ✅ | 31.84 | 29.42 | 2026-11-13 | 2026-11-18 |
| UUP | up ≥ 0.5% | +0.41% | ❌ | 29.50 | 29.62 | 2026-11-13 | 2026-11-18 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-11-22 · **Conditions matched:** 1/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | -2.67% | ❌ | 277.54 | 270.12 | 2026-11-13 | 2026-11-18 |
| XLF | up ≥ 1.0% | -3.85% | ❌ | 58.68 | 56.42 | 2026-11-13 | 2026-11-18 |
| XLY | up ≥ 1.0% | -0.65% | ❌ | 119.98 | 119.20 | 2026-11-13 | 2026-11-18 |
| GLD | down ≥ 0.5% | -4.01% | ✅ | 355.45 | 341.19 | 2026-11-13 | 2026-11-18 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2023-W25 (week ending 2023-06-25)
**Cosine similarity:** 0.9568 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.13% | -0.64% | +9.33% |
| **USO** | +14.00% | +29.17% | +10.04% |
| **GLD** | +2.36% | +0.24% | +6.77% |
| **TLT** | -2.09% | -11.52% | -4.69% |
| **XLE** | +11.31% | +15.45% | +9.85% |
| **IWM** | +7.95% | -2.16% | +11.58% |

### Паралел #2: 2022-W16 (week ending 2022-04-24)
**Cosine similarity:** 0.9520 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -7.55% | -7.26% | -12.15% |
| **USO** | +7.46% | -2.33% | -7.52% |
| **GLD** | -3.42% | -10.88% | -14.50% |
| **TLT** | -0.94% | -1.20% | -22.35% |
| **XLE** | +10.56% | -6.63% | +14.08% |
| **IWM** | -8.88% | -6.84% | -10.37% |

### Паралел #3: 2025-W14 (week ending 2025-04-06)
**Cosine similarity:** 0.9130 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +10.59% | +23.76% | +32.44% |
| **USO** | -4.89% | +10.70% | +5.58% |
| **GLD** | +12.78% | +9.80% | +27.86% |
| **TLT** | -5.73% | -6.33% | -3.74% |
| **XLE** | +2.23% | +10.50% | +12.89% |
| **IWM** | +8.60% | +23.12% | +35.68% |

### Паралел #4: 2022-W49 (week ending 2022-12-11)
**Cosine similarity:** 0.9126 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -0.69% | -1.87% | +9.31% |
| **USO** | +4.85% | +6.83% | +0.13% |
| **GLD** | +4.60% | +4.08% | +8.97% |
| **TLT** | -2.20% | -0.70% | -4.15% |
| **XLE** | +6.28% | -0.06% | -1.63% |
| **IWM** | +1.06% | -1.37% | +3.59% |

### Паралел #5: 2022-W38 (week ending 2022-09-25)
**Cosine similarity:** 0.9000 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.61% | +4.07% | +7.56% |
| **USO** | +8.10% | +6.12% | -6.67% |
| **GLD** | +0.65% | +9.31% | +20.02% |
| **TLT** | -10.04% | -3.35% | +1.09% |
| **XLE** | +24.05% | +23.52% | +10.51% |
| **IWM** | +6.49% | +4.23% | +2.68% |

### Паралел #6: 2024-W36 (week ending 2024-09-08)
**Cosine similarity:** 0.8975 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +6.07% | +12.48% | +6.58% |
| **USO** | +9.95% | +1.90% | +4.58% |
| **GLD** | +5.09% | +5.34% | +16.37% |
| **TLT** | -4.59% | -5.19% | -9.49% |
| **XLE** | +5.88% | +5.82% | +1.65% |
| **IWM** | +4.66% | +14.93% | -0.94% |

### Паралел #7: 2022-W24 (week ending 2022-06-19)
**Cosine similarity:** 0.8718 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +7.22% | +5.38% | +4.76% |
| **USO** | -6.35% | -16.13% | -22.13% |
| **GLD** | -6.85% | -9.01% | -2.62% |
| **TLT** | +1.99% | -4.47% | -4.43% |
| **XLE** | -1.59% | +6.74% | +14.79% |
| **IWM** | +8.18% | +8.36% | +5.56% |

### Паралел #8: 2022-W35 (week ending 2022-09-04)
**Cosine similarity:** 0.8572 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -3.64% | +3.74% | +3.05% |
| **USO** | -1.61% | -2.23% | -2.20% |
| **GLD** | +0.90% | +5.02% | +8.31% |
| **TLT** | -6.06% | -2.84% | -7.56% |
| **XLE** | -0.75% | +12.94% | +9.13% |
| **IWM** | -2.27% | +4.42% | +6.34% |

### Паралел #9: 2022-W19 (week ending 2022-05-15)
**Cosine similarity:** 0.8529 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -6.93% | +6.32% | -0.80% |
| **USO** | +8.82% | -7.75% | -8.49% |
| **GLD** | -0.13% | -0.55% | -2.51% |
| **TLT** | -6.18% | -0.37% | -15.60% |
| **XLE** | +4.28% | -2.86% | +15.29% |
| **IWM** | -4.88% | +12.52% | +4.96% |

### Паралел #10: 2025-W47 (week ending 2025-11-23)
**Cosine similarity:** 0.8457 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.39% | +4.61% | +13.14% |
| **USO** | +1.44% | +16.67% | +103.35% |
| **GLD** | +10.52% | +25.21% | +10.57% |
| **TLT** | -2.23% | -0.10% | -5.39% |
| **XLE** | -0.47% | +22.75% | +33.06% |
| **IWM** | +6.99% | +12.31% | +21.02% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 16 · **Total matching days:** 96 · **History:** 2021-05-17 → 2026-11-18

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.0% | +2.2% | -3.1% | +7.4% | 69% |
| **SPY** | 3m | 16 | +1.9% | +2.5% | -7.3% | +12.0% | 69% |
| **SPY** | 6m | 16 | +5.9% | +8.6% | -6.8% | +21.8% | 62% |
| **USO** | 1m | 16 | -0.6% | -1.2% | -14.3% | +12.7% | 44% |
| **USO** | 3m | 16 | -1.8% | -5.1% | -18.9% | +30.5% | 44% |
| **USO** | 6m | 16 | +11.2% | +2.1% | -15.9% | +109.4% | 56% |
| **GLD** | 1m | 16 | +2.1% | +0.8% | -7.0% | +9.0% | 69% |
| **GLD** | 3m | 16 | +3.3% | +3.4% | -13.9% | +24.5% | 62% |
| **GLD** | 6m | 16 | +3.1% | +3.4% | -13.9% | +25.3% | 56% |
| **TLT** | 1m | 16 | -1.5% | -1.1% | -6.7% | +3.6% | 31% |
| **TLT** | 3m | 16 | -0.7% | -0.1% | -16.5% | +11.1% | 50% |
| **TLT** | 6m | 16 | -4.1% | -3.7% | -18.0% | +7.5% | 31% |

**Episodes (последни 5 от 16):**
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-08-03` (5d)
- `2026-09-10 → 2026-10-01` (14d)
- `2026-10-16 → 2026-10-27` (8d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 122 · **History:** 2021-05-17 → 2026-11-18

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +6.3% | +6.3% | +3.5% | +9.1% | 100% |
| **SPY** | 3m | 2 | +6.9% | +6.9% | +3.5% | +10.3% | 100% |
| **SPY** | 6m | 2 | +6.0% | +6.0% | -2.9% | +15.0% | 50% |
| **USO** | 1m | 2 | +5.6% | +5.6% | +4.0% | +7.2% | 100% |
| **USO** | 3m | 2 | +8.7% | +8.7% | -9.9% | +27.4% | 50% |
| **USO** | 6m | 2 | +14.4% | +14.4% | +13.3% | +15.5% | 100% |
| **GLD** | 1m | 2 | +3.5% | +3.5% | -0.2% | +7.2% | 50% |
| **GLD** | 3m | 2 | -5.6% | -5.6% | -13.8% | +2.6% | 50% |
| **GLD** | 6m | 2 | -10.9% | -10.9% | -13.5% | -8.3% | 0% |
| **TLT** | 1m | 2 | -1.4% | -1.4% | -1.8% | -1.0% | 0% |
| **TLT** | 3m | 2 | -4.9% | -4.9% | -6.8% | -2.9% | 0% |
| **TLT** | 6m | 2 | -7.9% | -7.9% | -11.2% | -4.6% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-11-12` (75d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 488 · **History:** 2021-05-17 → 2026-11-18

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
- `2025-11-03 → 2026-11-18` (256d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 1 · **Total matching days:** 1 · **History:** 2021-05-17 → 2026-11-18

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | -1.5% | -1.5% | -1.5% | -1.5% | 0% |
| **SPY** | 3m | 1 | -5.3% | -5.3% | -5.3% | -5.3% | 0% |
| **SPY** | 6m | 1 | -5.3% | -5.3% | -5.3% | -5.3% | 0% |
| **USO** | 1m | 1 | +14.3% | +14.3% | +14.3% | +14.3% | 100% |
| **USO** | 3m | 1 | -8.2% | -8.2% | -8.2% | -8.2% | 0% |
| **USO** | 6m | 1 | -8.2% | -8.2% | -8.2% | -8.2% | 0% |
| **GLD** | 1m | 1 | -6.8% | -6.8% | -6.8% | -6.8% | 0% |
| **GLD** | 3m | 1 | -13.3% | -13.3% | -13.3% | -13.3% | 0% |
| **GLD** | 6m | 1 | -13.3% | -13.3% | -13.3% | -13.3% | 0% |
| **TLT** | 1m | 1 | +2.5% | +2.5% | +2.5% | +2.5% | 100% |
| **TLT** | 3m | 1 | +1.1% | +1.1% | +1.1% | +1.1% | 100% |
| **TLT** | 6m | 1 | +1.1% | +1.1% | +1.1% | +1.1% | 100% |

**Episodes (последни 5 от 1):**
- `2026-09-25 → 2026-09-25` (1d)

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 10 · **Total matching days:** 101 · **History:** 2021-05-17 → 2026-11-18

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 10 | -0.1% | +0.6% | -7.2% | +7.8% | 60% |
| **SPY** | 3m | 10 | +1.5% | -0.4% | -8.3% | +11.6% | 50% |
| **SPY** | 6m | 10 | +0.2% | +0.9% | -20.8% | +14.2% | 50% |
| **USO** | 1m | 10 | +4.1% | +0.5% | -15.0% | +52.9% | 50% |
| **USO** | 3m | 10 | +9.3% | +5.5% | -20.7% | +52.2% | 50% |
| **USO** | 6m | 10 | +9.6% | +1.6% | -27.6% | +56.3% | 50% |
| **GLD** | 1m | 10 | -1.2% | -1.9% | -8.3% | +11.7% | 20% |
| **GLD** | 3m | 10 | -2.6% | -1.4% | -14.0% | +6.4% | 40% |
| **GLD** | 6m | 10 | -2.8% | -5.9% | -15.2% | +25.0% | 30% |
| **TLT** | 1m | 10 | -2.4% | -2.7% | -6.0% | +2.5% | 10% |
| **TLT** | 3m | 10 | -6.1% | -4.9% | -17.6% | +4.2% | 20% |
| **TLT** | 6m | 10 | -9.6% | -8.1% | -22.3% | +1.2% | 10% |

**Episodes (последни 5 от 10):**
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-05-19` (36d)
- `2026-07-22 → 2026-08-03` (8d)
- `2026-09-01 → 2026-09-28` (15d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 17 · **Total matching days:** 294 · **History:** 2021-05-17 → 2026-11-18

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 17 | +1.9% | +1.6% | -4.8% | +9.0% | 71% |
| **SPY** | 3m | 17 | +2.8% | +4.2% | -12.6% | +16.2% | 71% |
| **SPY** | 6m | 17 | +6.2% | +8.1% | -14.0% | +21.0% | 76% |
| **USO** | 1m | 17 | +2.4% | -2.2% | -13.0% | +22.9% | 41% |
| **USO** | 3m | 17 | +3.4% | -0.8% | -14.5% | +29.9% | 41% |
| **USO** | 6m | 17 | +13.6% | +2.6% | -12.4% | +87.1% | 71% |
| **GLD** | 1m | 17 | +2.4% | +2.1% | -5.6% | +9.0% | 76% |
| **GLD** | 3m | 17 | +5.5% | +7.2% | -16.8% | +23.6% | 65% |
| **GLD** | 6m | 17 | +9.6% | +9.8% | -14.4% | +43.8% | 71% |
| **TLT** | 1m | 17 | +0.3% | -0.0% | -6.3% | +8.2% | 47% |
| **TLT** | 3m | 17 | -1.5% | -1.1% | -15.3% | +11.9% | 35% |
| **TLT** | 6m | 17 | -4.7% | -3.1% | -21.3% | +7.0% | 35% |

**Episodes (последни 5 от 17):**
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)
- `2026-08-07 → 2026-09-03` (19d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 21 · **Total matching days:** 307 · **History:** 2021-05-17 → 2026-11-18

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 21 | +0.2% | -0.0% | -8.7% | +7.0% | 48% |
| **SPY** | 3m | 21 | +1.5% | +2.7% | -13.7% | +9.1% | 62% |
| **SPY** | 6m | 21 | +2.4% | +1.3% | -16.4% | +16.9% | 62% |
| **USO** | 1m | 21 | -0.5% | -5.6% | -21.8% | +55.8% | 43% |
| **USO** | 3m | 21 | +2.8% | -1.3% | -12.7% | +64.3% | 43% |
| **USO** | 6m | 21 | +7.1% | -5.2% | -16.0% | +75.1% | 48% |
| **GLD** | 1m | 21 | -0.9% | -0.2% | -12.4% | +7.6% | 43% |
| **GLD** | 3m | 21 | +0.8% | +1.3% | -14.4% | +19.0% | 62% |
| **GLD** | 6m | 21 | +5.7% | +2.7% | -15.8% | +55.5% | 62% |
| **TLT** | 1m | 21 | -0.2% | -0.1% | -5.6% | +5.2% | 48% |
| **TLT** | 3m | 21 | -3.3% | -3.4% | -17.3% | +8.7% | 33% |
| **TLT** | 6m | 21 | -6.3% | -5.7% | -21.4% | +4.6% | 24% |

**Episodes (последни 5 от 21):**
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (13d)
- `2026-09-21 → 2026-10-15` (16d)
- `2026-11-13 → 2026-11-18` (3d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-11-18

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (9 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **US_PMI_COMPOSITE** | S&P Global US Composite PMI | growth | diffusion_indices | 4 | 2.60 | 2.60 | 2026-10-17 00:00:00 | 2026-11-14 00:00:00 | ✓ |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 4 | 2.46 | 2.54 | 2026-10-17 00:00:00 | 2026-11-14 00:00:00 | - |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 4 | 2.42 | 2.75 | 2026-10-17 00:00:00 | 2026-11-14 00:00:00 | ✓ |
| **US_PMI_SVCS** | S&P Global US Services PMI | growth | diffusion_indices | 4 | 2.09 | 2.09 | 2026-10-17 00:00:00 | 2026-11-14 00:00:00 | ✓ |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 4 | 2.07 | 2.07 | 2026-10-17 00:00:00 | 2026-11-14 00:00:00 | ✓ |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 3 | 2.16 | 2.16 | 2026-10-24 00:00:00 | 2026-11-14 00:00:00 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | 3 | 2.06 | 2.06 | 2026-10-17 00:00:00 | 2026-11-07 00:00:00 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | 2 | 2.02 | 2.02 | 2026-10-17 00:00:00 | 2026-10-24 00:00:00 | ✓ |
| **COMPUTSA** | Завършени жилища (SAAR) | growth | housing_supply | 1 | 2.95 | 2.95 | 2026-10-17 00:00:00 | 2026-10-17 00:00:00 | ✓ |

### EU (8 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 4 | 5.40 | 5.60 | 2026-10-17 00:00:00 | 2026-11-14 00:00:00 | - |
| **EA_OAT_BUND_SPREAD** | OAT-Bund spread (FR-DE 10Y, pp) | credit | sovereign_spreads | 4 | 3.15 | 5.17 | 2026-10-17 00:00:00 | 2026-11-14 00:00:00 | ✓ |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 4 | 2.51 | 2.70 | 2026-10-17 00:00:00 | 2026-11-14 00:00:00 | ✓ |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | 4 | 2.22 | 2.32 | 2026-10-17 00:00:00 | 2026-11-14 00:00:00 | - |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 4 | 2.20 | 2.25 | 2026-10-17 00:00:00 | 2026-11-14 00:00:00 | ✓ |
| **EA_EMPLOYMENT_PERSONS** | Заетост — брой наети (нац. сметки, EA-20, хил. лица) | labor | employment | 3 | 2.06 | 2.14 | 2026-10-24 00:00:00 | 2026-11-14 00:00:00 | ✓ |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation | sentiment | 2 | 2.28 | 2.28 | 2026-11-07 00:00:00 | 2026-11-14 00:00:00 | - |
| **EA_HICP_ENERGY** | HICP енергия, YoY | inflation | headline_measures | 2 | 2.16 | 2.16 | 2026-11-07 00:00:00 | 2026-11-14 00:00:00 | - |

### CN (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 6 | 2.53 | 2.54 | 2026-10-19 00:00:00 | 2026-11-16 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 6 | 2.23 | 2.23 | 2026-10-19 00:00:00 | 2026-11-16 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 6 | 2.19 | 2.19 | 2026-10-19 00:00:00 | 2026-11-16 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-11-14 00:00:00 · **Generated:** 2026-11-14 08:58:21.848276+00:00

**Режим:** `policy_dilemma` (Policy dilemma)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 43.7 | mixed | 37.0% | 1 | 1 |
| **growth** | 49.6 | mixed | 56.0% | 3 | 3 |
| **inflation** | 37.6 | contracting | 22.2% | 3 | 1 |
| **liquidity** | 42.4 | mixed | 31.6% | 0 | 0 |

### Top anomalies (6 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **US_PMI_COMPOSITE** | S&P Global US Composite PMI | growth | diffusion_indices | +2.60 | up | 58.40 | 2026-09-01 | ✓ max |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | +2.54 | up | 6.52 | 2026-10-01 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | +2.16 | up | 4.60 | 2026-09-01 | - |
| **US_PMI_SVCS** | S&P Global US Services PMI | growth | diffusion_indices | +2.09 | up | 58.80 | 2026-09-01 | ✓ max |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.08 | down | 93.73 | 2026-07-01 | ✓ min |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | +2.07 | up | 55.90 | 2026-09-01 | ✓ max |

### Narrative hints от макро лещите
- **US_PMI_COMPOSITE**: Markit композит — global benchmark, complement към ISM. Flash + final estimates.
- **PPIFIS**: Производствени цени → consumer prices с 1-3 месечен lag. Водещ за CPI при трендови промени.
- **MICH_INFL_1Y**: Household очаквания. По-шумни от market-based, но по-ранни. Extreme movements сигнализират de-anchoring risk.
- **US_PMI_SVCS**: Markit services — global comparable. ISM Services има различна methodology.
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **US_PMI_MFG**: Markit mfg — comparable cross-country. ISM е US-only.

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
  - `breadth_b`: 0.833
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
  - `state`: both_up
  - `interpretation`: De-anchoring in progress — expectations следват realized up.
  - `slot_a_label`: Realized inflation
  - `slot_b_label`: Inflation expectations
  - `breadth_a`: 0.833
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.667
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
  - `state`: both_up
  - `interpretation`: Съгласие — underlying persistent + пазар pricing-ва inflation. Fed зад кривата.
  - `slot_a_label`: Модел (sticky inflation)
  - `slot_b_label`: Пазар (breakevens + survey)
  - `breadth_a`: 1.0
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.667

### Executive narrative
> Policy dilemma — labor market е loose, но инфлацията remains hot. Fed е заклещен между двата мандата. Най-отклонена леща: Инфлация и цени — breadth 88% (разширяване), 3 аномалии, 1 нови екстремума. Expectations също нагоре — de-anchoring в ход, рискът ескалира. За наблюдение следващия релиз: US_PMI_COMPOSITE, US_PMI_SVCS, LABOR_SHARE_NBS (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: US_PMI_COMPOSITE z=+2.60 · NEW-5Y-MAX
- 4 нови екстремуми в top-6 (lookback 5г.)
- Активни двойки: Stagflation test=a_down_b_up; Inflation anchoring=both_up; Credit × Policy=a_down_b_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-11-14 00:00:00 · **Generated:** 2026-11-14 09:24:39.488030+00:00

**Режим:** `slowdown` (Синхронно забавяне (индикирано))  
**Primary driver:** `growth_labor_lead_lag`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 38.3 | mixed | 42.9% | 1 | 1 |
| **growth** | 46.7 | mixed | 25.0% | 1 | 0 |
| **inflation** | 38.8 | mixed | 42.9% | 2 | 0 |
| **credit** | 39.4 | mixed | 36.8% | 4 | 2 |
| **external** | 64.1 | expanding | 62.5% | 1 | 0 |

### Top anomalies (8 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | +5.21 | up | 3.39 | 2026-10-01 | - |
| **EA_OAT_BUND_SPREAD** | OAT-Bund spread (FR-DE 10Y, pp) | credit | sovereign_spreads | +5.17 | up | 1.47 | 2026-10-01 | ✓ max |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | +2.70 | up | 4.89 | 2026-10-01 | ✓ max |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | -2.32 | down | -8677.60 | 2026-09-01 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation, growth | sentiment | +2.28 | up | 24.80 | 2026-10-01 | - |
| **EA_HICP_ENERGY** | HICP енергия, YoY | inflation | headline_measures | +2.16 | up | 20.80 | 2026-10-01 | - |
| **EA_EMPLOYMENT_PERSONS** | Заетост — брой наети (нац. сметки, EA-20, хил. лица) | labor | employment | -2.14 | down | 0.37 | 2026-07-01 | ✓ min |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | +2.06 | up | 3.42 | 2026-10-01 | - |

### Narrative hints от макро лещите
- **EA_BUND_2Y**: EA-aggregate 2Y yield. Curve slope (10Y-2Y) проксира policy expectations и recession risk.
- **EA_OAT_BUND_SPREAD**: Core-but-not-DE EA stress proxy. Captures France-specific stress (e.g., 2024 budget crisis).
- **FR_10Y**: France sovereign yield — компонент на OAT-Bund spread. Core-but-not-DE EA stress indicator.
- **EA_TRADE_BALANCE**: Стоковият баланс с третите страни. Срив към дефицит (2022) = енергийната сметка изпреварва износа. Полярност +1.
- **EA_SELLING_PRICE_EXP**: Forward-looking inflation сигнал от business side — мениджърите казват дали ще вдигат цени. Изпреварва HICP с 3-6 месеца.
- **EA_HICP_ENERGY**: Volatile component на headline. Oil shock dependent. Headline-core gap explainer; de-singleton-ва headline_measures.
- **EA_EMPLOYMENT_PERSONS**: Домашна концепция за заетост (брой наети) от тримесечните нац. сметки. Допълва employment RATE (EA_LFS_EMP) с обемен сигнал — същата полярност. De-singleton-ва employment.
- **DE_10Y**: Germany 10Y, Maastricht-criterion measure. Reference за BTP-Bund / OAT-Bund spread изчисления.

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
  - `state`: both_down
  - `interpretation`: Синхронно забавяне: активността и трудът отслабват заедно. Late-cycle — гледай дали инфлацията позволява отговор на ЕЦБ.
  - `slot_a_label`: Твърда активност (IP, retail, GDP)
  - `slot_b_label`: Пазар на труда (сила)
  - `breadth_a`: 0.25
  - `breadth_b`: 0.25
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 0.5

### Executive narrative
> Синхронно забавяне — hard activity и labor claims сочат в посока на отслабване. Late-cycle риск е активен. Най-отклонена леща: Инфлация и цени — breadth 75% (смесено), 2 аномалии, 0 нови екстремума. За наблюдение следващия релиз: EA_OAT_BUND_SPREAD, FR_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.21
- 3 нови екстремуми в top-8 (lookback 5г.)
- Активни двойки: Sentiment × Hard=both_down; Growth × Labor=both_down



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-11-16 00:00:00 · **Generated:** 2026-11-16 14:20:29.101558+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 37.9 | mixed | -% | - | - |
| **inflation** | 38.8 | mixed | -% | - | - |
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
  - `state`: a_down_b_up
  - `interpretation`: Реален сектор изпреварва кредита — инвестиции растат без нов кредит (вътрешно финансиране / fiscal импулс).
  - `slot_a_label`: Кредитна експанзия
  - `slot_b_label`: Имоти и инвестиции
  - `breadth_a`: 0.333
  - `breadth_b`: 0.7
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
> Претеглен композитен macro score 36.7/100 → режим „ВЛОШАВАЩ СЕ“ (5/5 лещи). 5 лещи, 3 flagged аномалии (3 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-11-13 |
| `as_of` | 2026-11-13 |
| `regime` | REFLATION |
| `alignment_score` | 3.0 |
| `gms_score` | 0.0 |
| `gms_max` | 8 |
| `gms_tier` | LOW |
| `ks_status` | inactive |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-11-13 → 2026-11-18)

**stable_winner (1m):** +6 entered, -7 exited
  - **Entered:** AES, APA, CVS, HAS, LITE, STX
  - **Exited:** ADM, DAL, EQIX, FCX, FITB, PNC, STLD

**stable_winner (3m):** +2 entered, -1 exited
  - **Entered:** IRM, NTRS
  - **Exited:** VLO

**quality_dip (1m):** +7 entered, -6 exited
  - **Entered:** ADM, DAL, EQIX, FCX, FITB, PNC, STLD
  - **Exited:** AES, APA, CVS, HAS, LITE, STX

**quality_dip (3m):** +1 entered, -2 exited
  - **Entered:** VLO
  - **Exited:** IRM, NTRS

**faded_bounce (1m):** +3 entered, -6 exited
  - **Entered:** CSGP, EFX, OTIS
  - **Exited:** AXON, CTAS, DPZ, ISRG, PGR, TDG

**faded_bounce (3m):** +4 entered, -5 exited
  - **Entered:** CSGP, EFX, EXE, PYPL
  - **Exited:** ARES, CTAS, DPZ, MOS, PGR



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
| 1 | **MRNA** | Healthcare | 92.3 | -8.8% | 18.6% | 352.3% | 816.0% | 1.60 | -34.2% |
| 2 | **OKTA** | Technology | 91.2 | -8.1% | 23.6% | 103.7% | 126.3% | 1.02 | -33.1% |
| 3 | **CRL** | Healthcare | 87.8 | 10.7% | 14.5% | 117.9% | 78.8% | 1.35 | -33.9% |
| 4 | **MPC** | Energy | 87.4 | -16.5% | 9.7% | 51.4% | 140.8% | 1.74 | -23.1% |
| 5 | **RVTY** | Healthcare | 86.4 | -2.0% | 23.7% | 54.2% | 62.9% | 1.05 | -30.1% |
| 6 | **VTRS** | Healthcare | 86.1 | 12.0% | 26.8% | 28.4% | 76.4% | 2.07 | -19.0% |
| 7 | **HUM** | Healthcare | 85.5 | 7.1% | 17.5% | 43.4% | 76.9% | 1.26 | -44.4% |
| 8 | **PSX** | Energy | 84.4 | -11.6% | 6.0% | 41.6% | 110.2% | 1.72 | -17.4% |
| 9 | **VLO** | Energy | 84.3 | -16.1% | 5.1% | 39.7% | 143.4% | 1.70 | -24.6% |
| 10 | **CRWD** | Technology | 82.1 | -3.7% | 8.9% | 42.4% | 69.7% | 0.79 | -37.2% |
| 11 | **WST** | Healthcare | 81.0 | 7.9% | 17.4% | 36.3% | 47.0% | 1.35 | -24.7% |
| 12 | **CNC** | Healthcare | 80.8 | 5.7% | 12.1% | 22.6% | 88.7% | 1.39 | -32.7% |
| 13 | **AMD** | Technology | 80.2 | -6.4% | 7.9% | 21.6% | 118.0% | 0.91 | -37.7% |
| 14 | **ILMN** | Healthcare | 80.1 | -22.9% | -1.2% | 43.0% | 117.7% | 0.96 | -32.6% |
| 15 | **SWK** | Industrials | 80.1 | 19.3% | 10.0% | 50.1% | 44.9% | 1.32 | -26.1% |
| 16 | **BDX** | Healthcare | 79.0 | 12.9% | 15.5% | 48.5% | 28.8% | 1.26 | -23.1% |
| 17 | **APA** | Energy | 78.3 | -5.3% | 8.4% | 16.0% | 105.4% | 1.38 | -27.7% |
| 18 | **TGT** | Consumer Defensive | 78.2 | 4.8% | 1.0% | 27.2% | 75.2% | 1.79 | -13.3% |
| 19 | **MCK** | Healthcare | 78.0 | 8.0% | 28.0% | 43.6% | 20.5% | 0.70 | -27.2% |
| 20 | **CPAY** | Financial Services | 77.6 | 12.4% | 11.1% | 31.8% | 44.2% | 1.24 | -20.2% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **TECN.SW** | Healthcare | 91.4 | 9.0% | 32.5% | 91.8% | 78.7% | 1.63 | -28.4% |
| 2 | **MOH.AT** | Energy | 89.6 | -11.9% | 12.3% | 75.0% | 167.3% | 2.48 | -14.9% |
| 3 | **ALE.WA** | Consumer Cyclical | 88.3 | 16.3% | 29.6% | 96.3% | 51.1% | 1.81 | -26.5% |
| 4 | **DEMANT.CO** | Healthcare | 87.7 | 10.4% | 30.1% | 59.0% | 57.0% | 1.57 | -26.8% |
| 5 | **GMAB.CO** | Healthcare | 86.9 | 49.7% | 79.7% | 120.7% | 31.1% | 1.46 | -32.3% |
| 6 | **BFT.WA** | Industrials | 86.8 | 16.1% | 14.2% | 57.1% | 75.1% | 2.44 | -17.4% |
| 7 | **BAYN.DE** | Healthcare | 86.1 | 29.4% | 18.0% | 50.1% | 65.6% | 1.73 | -30.6% |
| 8 | **BME.L** | Consumer Cyclical | 85.9 | 5.7% | 18.6% | 71.3% | 61.9% | 1.25 | -34.3% |
| 9 | **ORNBV.HE** | Healthcare | 85.1 | 29.7% | 32.5% | 53.3% | 39.0% | 1.83 | -18.0% |
| 10 | **MAERSK-B.CO** | Industrials | 83.8 | -20.2% | 14.1% | 40.9% | 90.4% | 0.98 | -22.9% |
| 11 | **FRO.OL** | Energy | 83.6 | -20.4% | 16.6% | 25.8% | 131.3% | 1.35 | -25.0% |
| 12 | **REP.MC** | Energy | 83.2 | -0.5% | 12.4% | 33.4% | 86.8% | 1.72 | -20.4% |
| 13 | **LOTB.BR** | Consumer Defensive | 82.2 | 16.7% | 14.4% | 33.5% | 59.1% | 2.44 | -11.9% |
| 14 | **BAMNB.AS** | Industrials | 82.1 | 12.9% | 11.1% | 48.8% | 58.5% | 1.48 | -16.2% |
| 15 | **DSFIR.AS** | Basic Materials | 81.6 | 6.4% | 15.7% | 62.3% | 41.9% | 1.23 | -27.0% |
| 16 | **LPP.WA** | Consumer Cyclical | 81.0 | 10.2% | 24.2% | 33.5% | 44.6% | 1.25 | -24.2% |
| 17 | **ERF.PA** | Healthcare | 80.9 | 13.1% | 25.3% | 47.2% | 31.4% | 1.35 | -20.4% |
| 18 | **EBP.WA** | Financial Services | 80.6 | 3.6% | 9.2% | 30.5% | 70.0% | 1.92 | -10.9% |
| 19 | **VONN.SW** | Financial Services | 80.1 | 4.6% | 4.9% | 37.3% | 61.0% | 2.68 | -6.9% |
| 20 | **EVK.DE** | Basic Materials | 80.0 | -2.1% | 15.9% | 24.8% | 61.2% | 1.58 | -16.2% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **SNDK** | Information Technology | 2.018 | 1.719 | 1.694 | 1.705 | -0.136 | - | 6.2 | +141.2% |
| 2 | **EIX** | Utilities | 1.602 | 0.172 | 0.895 | 2.860 | -0.881 | - | 6.7 | +18.8% |
| 3 | **MO** | Consumer Staples | 1.503 | 1.111 | 1.823 | 0.812 | -0.072 | - | 16.0 | - |
| 4 | **CF** | Materials | 1.469 | 0.882 | 1.288 | 1.501 | 0.447 | - | 8.0 | +30.9% |
| 5 | **NEM** | Materials | 1.444 | 0.695 | 1.795 | 1.052 | 0.539 | - | 12.1 | +27.3% |
| 6 | **HST** | Real Estate | 1.432 | 2.286 | 0.328 | 1.250 | -0.302 | - | 18.8 | +14.2% |
| 7 | **MU** | Information Technology | 1.362 | 1.588 | 1.179 | 0.752 | -0.406 | - | 9.6 | +88.3% |
| 8 | **DVA** | Health Care | 1.205 | 1.106 | 0.202 | 1.831 | -1.375 | - | 12.2 | +96.8% |
| 9 | **SYF** | Financials | 1.167 | -0.232 | 1.173 | 1.828 | -0.195 | - | 7.3 | +19.8% |
| 10 | **APA** | Energy | 1.147 | 1.095 | 1.159 | 0.665 | 0.135 | - | 7.4 | +33.3% |
| 11 | **VLO** | Energy | 1.115 | 1.333 | 0.336 | 1.271 | -0.422 | - | 7.8 | +46.9% |
| 12 | **TRV** | Financials | 1.027 | 1.501 | 0.323 | 0.924 | 0.596 | - | 10.3 | +27.5% |
| 13 | **TPR** | Consumer Discretionary | 1.027 | 0.751 | 1.308 | 0.499 | -1.320 | - | 16.3 | +433.8% |
| 14 | **WDC** | Information Technology | 1.026 | 1.145 | 0.902 | 0.600 | -0.673 | - | 10.1 | +129.6% |
| 15 | **CPAY** | Financials | 1.023 | 1.827 | 0.999 | -0.095 | -0.645 | - | 25.0 | +32.2% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -2.191 | -1.701 | -1.397 | -2.441 | -1.247 |
| 502 | **TSLA** | Consumer Discretionary | -1.790 | -0.433 | -1.332 | -2.603 | -0.379 |
| 501 | **ARES** | Financials | -1.732 | -1.605 | -1.373 | -1.415 | -1.207 |
| 500 | **KKR** | Financials | -1.603 | -2.009 | -0.773 | -1.400 | -0.748 |
| 499 | **BA** | Industrials | -1.582 | -0.502 | -2.243 | -1.046 | -1.094 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W47.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W47.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\macro\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-11-16  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
