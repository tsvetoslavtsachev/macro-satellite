# Сателит — пълен data export за 2026-W36

_Период: 2026-08-31 → 2026-09-06_  
_Генериран: 2026-09-04 10:47 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W36.md` (structured briefing) и `narrative_2026-W36.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**11 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **HYG** | -0.79% | -1.82σ | 79.74 | 79.11 | 2026-08-28 | 2026-09-02 | -0.05% | +0.40% | 13 |
| **XLF** | -0.76% | -1.49σ | 58.10 | 57.66 | 2026-08-28 | 2026-09-02 | +0.93% | +1.13% | 13 |
| **XLI** | -2.46% | -1.46σ | 177.14 | 172.78 | 2026-08-28 | 2026-09-02 | +0.19% | +1.82% | 13 |
| **SHY** | -0.31% | -1.23σ | 81.89 | 81.64 | 2026-08-28 | 2026-09-02 | -0.04% | +0.22% | 13 |
| **LQD** | -0.94% | -1.16σ | 106.35 | 105.35 | 2026-08-28 | 2026-09-02 | -0.21% | +0.63% | 13 |
| **USO** | +8.83% | +1.15σ | 129.70 | 141.15 | 2026-08-28 | 2026-09-02 | +0.31% | +7.42% | 13 |
| **DFEN** | -11.77% | -1.14σ | 67.73 | 59.76 | 2026-08-28 | 2026-09-02 | -0.27% | +10.09% | 13 |
| **DIA** | -0.83% | -1.11σ | 535.06 | 530.62 | 2026-08-28 | 2026-09-02 | +0.36% | +1.08% | 13 |
| **DBC** | +3.70% | +1.06σ | 30.79 | 31.93 | 2026-08-28 | 2026-09-02 | +0.38% | +3.13% | 13 |
| **IEF** | -0.72% | -1.05σ | 92.85 | 92.18 | 2026-08-28 | 2026-09-02 | -0.15% | +0.55% | 13 |
| **XLRE** | -1.69% | -1.03σ | 44.48 | 43.73 | 2026-08-28 | 2026-09-02 | +0.10% | +1.74% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-09-06 · **Conditions matched:** 3/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | +8.83% | ✅ | 129.70 | 141.15 | 2026-08-28 | 2026-09-02 |
| DFEN | down ≥ 3.0% | -11.77% | ✅ | 67.73 | 59.76 | 2026-08-28 | 2026-09-02 |
| GLD | down ≥ 1.0% | -1.49% | ✅ | 408.89 | 402.78 | 2026-08-28 | 2026-09-02 |
| URA | down ≥ 3.0% | -2.74% | ❌ | 45.57 | 44.32 | 2026-08-28 | 2026-09-02 |
| UUP | up ≥ 0.5% | -0.04% | ❌ | 28.18 | 28.17 | 2026-08-28 | 2026-09-02 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-09-06 · **Conditions matched:** 1/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | -0.59% | ❌ | 295.75 | 294.01 | 2026-08-28 | 2026-09-02 |
| XLF | up ≥ 1.0% | -0.76% | ❌ | 58.10 | 57.66 | 2026-08-28 | 2026-09-02 |
| XLY | up ≥ 1.0% | -2.00% | ❌ | 117.21 | 114.86 | 2026-08-28 | 2026-09-02 |
| GLD | down ≥ 0.5% | -1.49% | ✅ | 408.89 | 402.78 | 2026-08-28 | 2026-09-02 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2026-W05 (week ending 2026-02-01)
**Cosine similarity:** 0.9534 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.68% | +4.14% | +7.96% |
| **USO** | +13.43% | +79.58% | +62.44% |
| **GLD** | +5.21% | -4.89% | -16.50% |
| **TLT** | +2.64% | -1.74% | -5.60% |
| **XLE** | +10.71% | +15.28% | +16.65% |
| **IWM** | -0.16% | +7.56% | +12.15% |

### Паралел #2: 2026-W20 (week ending 2026-05-17)
**Cosine similarity:** 0.9525 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.51% | +5.03% | +3.52% |
| **USO** | -22.10% | -14.59% | -4.78% |
| **GLD** | -4.71% | -3.79% | -3.48% |
| **TLT** | +3.02% | -1.94% | -2.04% |
| **XLE** | -6.86% | +4.16% | +9.52% |
| **IWM** | +5.22% | +9.90% | +5.91% |

### Паралел #3: 2026-W11 (week ending 2026-03-15)
**Cosine similarity:** 0.9305 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.86% | +12.00% | +15.53% |
| **USO** | +3.30% | +4.62% | +17.73% |
| **GLD** | -3.42% | -16.12% | -12.60% |
| **TLT** | +0.77% | -0.89% | -5.30% |
| **XLE** | -3.03% | -0.26% | +12.82% |
| **IWM** | +8.97% | +18.80% | +19.23% |

### Паралел #4: 2026-W18 (week ending 2026-05-03)
**Cosine similarity:** 0.9262 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.40% | +3.66% | +6.18% |
| **USO** | -3.87% | -9.54% | -1.16% |
| **GLD** | -2.65% | -12.20% | -4.82% |
| **TLT** | +0.05% | -3.92% | -4.28% |
| **XLE** | -1.51% | +1.19% | +10.62% |
| **IWM** | +4.43% | +4.27% | +5.27% |

### Паралел #5: 2023-W06 (week ending 2023-02-12)
**Cosine similarity:** 0.9262 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -4.00% | +0.87% | +9.22% |
| **USO** | -9.93% | -11.16% | +6.27% |
| **GLD** | +2.00% | +7.76% | +2.45% |
| **TLT** | +0.68% | +0.85% | -7.76% |
| **XLE** | -9.38% | -12.96% | -0.34% |
| **IWM** | -7.25% | -9.24% | +0.36% |

### Паралел #6: 2026-W10 (week ending 2026-03-08)
**Cosine similarity:** 0.9215 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.96% | +9.69% | +13.80% |
| **USO** | +26.95% | +22.29% | +29.77% |
| **GLD** | -8.81% | -16.32% | -14.94% |
| **TLT** | -2.06% | -3.84% | -7.36% |
| **XLE** | +6.35% | +1.94% | +15.08% |
| **IWM** | +0.81% | +12.26% | +17.19% |

### Паралел #7: 2022-W09 (week ending 2022-03-06)
**Cosine similarity:** 0.9144 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.36% | -5.00% | -9.24% |
| **USO** | -5.86% | +12.60% | -10.11% |
| **GLD** | -2.42% | -6.04% | -13.29% |
| **TLT** | -8.38% | -17.26% | -21.41% |
| **XLE** | +0.96% | +18.98% | +6.29% |
| **IWM** | +2.18% | -5.84% | -9.35% |

### Паралел #8: 2024-W40 (week ending 2024-10-06)
**Cosine similarity:** 0.9055 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.65% | +3.31% | -11.82% |
| **USO** | -2.12% | +2.06% | -11.04% |
| **GLD** | +3.43% | -0.62% | +14.17% |
| **TLT** | -2.94% | -8.64% | -2.83% |
| **XLE** | -3.23% | -6.13% | -15.48% |
| **IWM** | +2.32% | +2.41% | -17.32% |

### Паралел #9: 2026-W17 (week ending 2026-04-26)
**Cosine similarity:** 0.9053 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.13% | +3.50% | +7.17% |
| **USO** | +3.47% | +3.24% | +6.61% |
| **GLD** | -4.44% | -14.16% | -7.03% |
| **TLT** | -1.86% | -3.99% | -5.49% |
| **XLE** | +1.72% | +4.84% | +14.47% |
| **IWM** | +5.01% | +5.25% | +6.28% |

### Паралел #10: 2025-W01 (week ending 2025-01-05)
**Cosine similarity:** 0.8962 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.66% | -14.64% | +5.64% |
| **USO** | -0.53% | -12.83% | -3.50% |
| **GLD** | +7.81% | +14.88% | +26.14% |
| **TLT** | +1.31% | +6.37% | -0.37% |
| **XLE** | +2.94% | -9.96% | -0.50% |
| **IWM** | +1.11% | -19.27% | -0.60% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 14 · **Total matching days:** 74 · **History:** 2021-05-17 → 2026-09-02

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 14 | +2.2% | +2.4% | -3.1% | +7.4% | 71% |
| **SPY** | 3m | 14 | +2.8% | +2.7% | -7.3% | +12.0% | 79% |
| **SPY** | 6m | 14 | +7.7% | +9.8% | -6.8% | +21.8% | 79% |
| **USO** | 1m | 14 | +0.5% | +0.3% | -14.3% | +12.7% | 50% |
| **USO** | 3m | 14 | -1.1% | -2.0% | -18.9% | +24.5% | 50% |
| **USO** | 6m | 14 | +13.1% | +2.1% | -8.7% | +109.4% | 57% |
| **GLD** | 1m | 14 | +3.1% | +2.0% | -0.9% | +9.0% | 79% |
| **GLD** | 3m | 14 | +5.9% | +7.3% | -12.6% | +24.5% | 71% |
| **GLD** | 6m | 14 | +7.2% | +9.8% | -12.5% | +25.3% | 71% |
| **TLT** | 1m | 14 | -1.5% | -1.1% | -6.7% | +3.6% | 36% |
| **TLT** | 3m | 14 | -0.6% | -0.1% | -16.5% | +11.1% | 50% |
| **TLT** | 6m | 14 | -4.3% | -3.7% | -18.0% | +7.5% | 29% |

**Episodes (последни 5 от 14):**
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-08-03` (5d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 79 · **History:** 2021-05-17 → 2026-09-02

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +6.3% | +6.3% | +3.5% | +9.1% | 100% |
| **SPY** | 3m | 2 | +6.0% | +6.0% | +1.8% | +10.3% | 100% |
| **SPY** | 6m | 2 | +7.5% | +7.5% | +1.8% | +13.2% | 100% |
| **USO** | 1m | 2 | +5.6% | +5.6% | +4.0% | +7.2% | 100% |
| **USO** | 3m | 2 | +3.8% | +3.8% | -9.9% | +17.5% | 50% |
| **USO** | 6m | 2 | +15.4% | +15.4% | +13.3% | +17.5% | 100% |
| **GLD** | 1m | 2 | +3.5% | +3.5% | -0.2% | +7.2% | 50% |
| **GLD** | 3m | 2 | -2.8% | -2.8% | -13.8% | +8.2% | 50% |
| **GLD** | 6m | 2 | +0.5% | +0.5% | -7.3% | +8.2% | 50% |
| **TLT** | 1m | 2 | -1.4% | -1.4% | -1.8% | -1.0% | 0% |
| **TLT** | 3m | 2 | -2.7% | -2.7% | -2.9% | -2.5% | 0% |
| **TLT** | 6m | 2 | -4.1% | -4.1% | -5.7% | -2.5% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-09-02` (32d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 434 · **History:** 2021-05-17 → 2026-09-02

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
- `2025-11-03 → 2026-09-02` (202d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-09-02

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 10 · **Total matching days:** 88 · **History:** 2021-05-17 → 2026-09-02

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 10 | -0.1% | +0.7% | -7.2% | +7.8% | 60% |
| **SPY** | 3m | 10 | +1.8% | +1.4% | -8.3% | +11.6% | 60% |
| **SPY** | 6m | 10 | +1.1% | +3.3% | -20.8% | +14.2% | 70% |
| **USO** | 1m | 10 | +3.4% | -0.6% | -15.0% | +52.9% | 50% |
| **USO** | 3m | 10 | +8.3% | +3.6% | -20.7% | +52.2% | 60% |
| **USO** | 6m | 10 | +10.3% | +2.3% | -27.6% | +56.3% | 60% |
| **GLD** | 1m | 10 | -0.7% | -0.9% | -8.3% | +11.7% | 30% |
| **GLD** | 3m | 10 | -0.4% | +0.9% | -12.0% | +6.4% | 60% |
| **GLD** | 6m | 10 | +0.4% | +0.4% | -15.2% | +25.0% | 50% |
| **TLT** | 1m | 10 | -1.9% | -2.1% | -6.0% | +2.5% | 20% |
| **TLT** | 3m | 10 | -5.7% | -4.9% | -17.6% | +4.2% | 30% |
| **TLT** | 6m | 10 | -9.2% | -8.1% | -22.3% | +1.2% | 20% |

**Episodes (последни 5 от 10):**
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-05-19` (36d)
- `2026-07-22 → 2026-08-03` (8d)
- `2026-09-01 → 2026-09-02` (2d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 17 · **Total matching days:** 293 · **History:** 2021-05-17 → 2026-09-02

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 17 | +1.9% | +1.6% | -4.8% | +9.0% | 71% |
| **SPY** | 3m | 17 | +3.0% | +4.2% | -12.6% | +16.2% | 71% |
| **SPY** | 6m | 17 | +6.4% | +8.0% | -14.0% | +21.0% | 76% |
| **USO** | 1m | 17 | +2.4% | -2.2% | -13.0% | +22.9% | 41% |
| **USO** | 3m | 17 | +3.1% | -0.8% | -14.5% | +29.9% | 41% |
| **USO** | 6m | 17 | +12.9% | +2.6% | -12.4% | +87.1% | 71% |
| **GLD** | 1m | 17 | +2.4% | +1.4% | -5.6% | +9.0% | 76% |
| **GLD** | 3m | 17 | +6.0% | +7.2% | -16.8% | +23.6% | 71% |
| **GLD** | 6m | 17 | +10.8% | +9.8% | -8.9% | +43.8% | 76% |
| **TLT** | 1m | 17 | +0.3% | -0.0% | -6.3% | +8.2% | 47% |
| **TLT** | 3m | 17 | -1.5% | -1.1% | -15.3% | +11.9% | 35% |
| **TLT** | 6m | 17 | -4.5% | -1.7% | -21.3% | +7.0% | 35% |

**Episodes (последни 5 от 17):**
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)
- `2026-08-07 → 2026-09-01` (18d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 19 · **Total matching days:** 288 · **History:** 2021-05-17 → 2026-09-02

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 19 | +0.4% | +1.0% | -8.7% | +7.0% | 53% |
| **SPY** | 3m | 19 | +2.1% | +3.6% | -13.7% | +9.1% | 68% |
| **SPY** | 6m | 19 | +3.3% | +6.8% | -16.4% | +16.9% | 74% |
| **USO** | 1m | 19 | -0.6% | -5.6% | -21.8% | +55.8% | 42% |
| **USO** | 3m | 19 | +3.9% | -0.6% | -12.7% | +64.3% | 47% |
| **USO** | 6m | 19 | +8.8% | +5.0% | -16.0% | +75.1% | 53% |
| **GLD** | 1m | 19 | -0.6% | -0.1% | -12.4% | +7.6% | 47% |
| **GLD** | 3m | 19 | +1.8% | +1.7% | -13.7% | +19.0% | 68% |
| **GLD** | 6m | 19 | +8.1% | +6.0% | -15.8% | +55.5% | 74% |
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
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-09-02

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (11 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | 5 | 2.65 | 2.70 | 2026-08-01 00:00:00 | 2026-08-29 00:00:00 | ✓ |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 5 | 2.63 | 2.71 | 2026-08-01 00:00:00 | 2026-08-29 00:00:00 | ✓ |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | 5 | 2.18 | 2.22 | 2026-08-01 00:00:00 | 2026-08-29 00:00:00 | - |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 4 | 2.29 | 2.30 | 2026-08-01 00:00:00 | 2026-08-29 00:00:00 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 4 | 2.16 | 2.16 | 2026-08-01 00:00:00 | 2026-08-22 00:00:00 | - |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | 4 | 2.09 | 2.09 | 2026-08-01 00:00:00 | 2026-08-22 00:00:00 | - |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 3 | 2.28 | 2.28 | 2026-08-01 00:00:00 | 2026-08-15 00:00:00 | ✓ |
| **TRIMMED_MEAN_CPI** | Trimmed-Mean CPI (Cleveland Fed, 16%) | inflation | sticky_measures | 2 | 2.28 | 2.28 | 2026-08-01 00:00:00 | 2026-08-08 00:00:00 | ✓ |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 2 | 2.15 | 2.15 | 2026-08-01 00:00:00 | 2026-08-08 00:00:00 | - |
| **COMPUTSA** | Завършени жилища (SAAR) | growth | housing_supply | 2 | 2.06 | 2.06 | 2026-08-22 00:00:00 | 2026-08-29 00:00:00 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | 1 | 2.02 | 2.02 | 2026-08-01 00:00:00 | 2026-08-01 00:00:00 | ✓ |

### EU (4 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.27 | 5.27 | 2026-08-01 00:00:00 | 2026-08-29 00:00:00 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.16 | 2.17 | 2026-08-01 00:00:00 | 2026-08-29 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.16 | 2.17 | 2026-08-01 00:00:00 | 2026-08-29 00:00:00 | ✓ |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | 2 | 2.38 | 2.38 | 2026-08-01 00:00:00 | 2026-08-08 00:00:00 | - |

### CN (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 8 | 2.55 | 2.55 | 2026-08-03 00:00:00 | 2026-08-31 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 8 | 2.23 | 2.23 | 2026-08-03 00:00:00 | 2026-08-31 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 1 | 2.19 | 2.19 | 2026-08-22 00:00:00 | 2026-08-22 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-08-29 00:00:00 · **Generated:** 2026-08-29 09:03:30.320639+00:00

**Режим:** `transition` (Преходно / смесено)  
**Primary driver:** `none`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 36.5 | contracting | 22.2% | 3 | 2 |
| **growth** | 45.2 | mixed | 44.0% | 1 | 0 |
| **inflation** | 41.5 | mixed | 38.9% | 1 | 1 |
| **liquidity** | 53.2 | mixed | 42.1% | 0 | 0 |

### Top anomalies (5 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.71 | down | 93.55 | 2026-04-01 | ✓ min |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | -2.70 | down | 61.40 | 2026-07-01 | ✓ min |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | -2.25 | down | 2.30 | 2026-06-01 | - |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | -2.22 | down | 58.90 | 2026-07-01 | - |
| **COMPUTSA** | Завършени жилища (SAAR) | growth, housing | housing_supply | -2.06 | down | -16.76 | 2026-07-01 | - |

### Narrative hints от макро лещите
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **CIVPART**: Структурни сдвигове (демография, ранно пенсиониране). Пост-COVID не се възстанови напълно.
- **HPIPONM226S**: Monthly FHFA версия. Само purchase transactions (без refi appraisals). По-чист от refi-bias.
- **EMRATIO**: Не зависи от definition на 'active labor force'. По-стабилен индикатор на дълбоката заетост.
- **COMPUTSA**: Завършва construction pipeline (12-18m след starts). Превишение спрямо sales = inventory build.

### Cross-lens divergences (6 entries)
- 🔔 **?**
  - `pair_id`: stagflation_test
  - `name_bg`: Labor tightness × Inflation pressure
  - `question_bg`: Дали labor tightness потвърждава inflation pressure (стагфлация)?
  - `state`: transition
  - `interpretation`: Transition — signals not aligned; watch next releases.
  - `slot_a_label`: Labor tightness
  - `slot_b_label`: Inflation pressure
  - `breadth_a`: 0.5
  - `breadth_b`: 0.167
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 0.833
- 🔔 **?**
  - `pair_id`: growth_labor_lead_lag
  - `name_bg`: Hard activity × Labor claims
  - `question_bg`: Дали hard activity и labor market следват едно тенденция?
  - `state`: a_down_b_up
  - `interpretation`: Activity cools, labor stable — late-cycle decoupling.
  - `slot_a_label`: Hard activity
  - `slot_b_label`: Labor market (claims inverted)
  - `breadth_a`: 0.2
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.8
  - `breadth_b_raw`: 0.667
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
  - `breadth_b`: 0.667
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.0
  - `breadth_b_raw`: 0.667
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
> Сигналите са в преход — няма доминираща конфигурация. Следващите 2-3 релиза ще ориентират посоката. Най-отклонена леща: Монетарна политика и кредит — breadth 39% (смесено), 0 аномалии, 0 нови екстремума. За наблюдение следващия релиз: LABOR_SHARE_NBS, CIVPART (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: LABOR_SHARE_NBS z=-2.71 · NEW-5Y-MIN
- 2 нови екстремуми в top-5 (lookback 5г.)
- Активни двойки: Growth × Labor=a_down_b_up; Inflation anchoring=both_down; Credit × Policy=a_down_b_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-08-29 00:00:00 · **Generated:** 2026-08-29 09:22:49.432481+00:00

**Режим:** `policy_dilemma` (Policy dilemma)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 42.8 | mixed | 42.9% | 0 | 0 |
| **growth** | 40.8 | mixed | 25.0% | 0 | 0 |
| **inflation** | 50.9 | mixed | 57.1% | 0 | 0 |
| **credit** | 45.0 | mixed | 36.8% | 3 | 2 |
| **external** | 14.8 | contracting | 16.7% | 0 | 0 |

### Top anomalies (3 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | +5.27 | up | 2.83 | 2026-07-01 | - |
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
  - `breadth_a`: 0.5
  - `breadth_b`: 0.0
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 0.0
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
> Policy dilemma — labor market е loose, но инфлацията remains hot. ЕЦБ е заклещена между инфлацията и растежа. Най-отклонена леща: Финансови условия, кредит и спредове — breadth 88% (разширяване), 3 аномалии, 2 нови екстремума. За наблюдение следващия релиз: FR_10Y, DE_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.27
- 2 нови екстремуми в top-3 (lookback 5г.)
- Активни двойки: Stagflation test=a_down_b_up



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-08-31 00:00:00 · **Generated:** 2026-08-31 12:00:11.096012+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 41.9 | mixed | -% | - | - |
| **inflation** | 44.9 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 47.8 | mixed | -% | - | - |
| **property** | 28.6 | contracting | -% | - | - |

### Top anomalies (2 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | -2.55 | down | 3.00 | 2026-08-20 | ✓ min |
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
> Претеглен композитен macro score 38.8/100 → режим „ВЛОШАВАЩ СЕ“ (5/5 лещи). 5 лещи, 2 flagged аномалии (4 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-08-28 |
| `as_of` | 2026-08-28 |
| `regime` | REFLATION |
| `alignment_score` | 5.0 |
| `gms_score` | 4.0 |
| `gms_max` | 8 |
| `gms_tier` | MEDIUM |
| `ks_status` | inactive |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-08-28 → 2026-09-02)

**stable_winner (1m):** +13 entered, -14 exited
  - **Entered:** AEP, BEN, BK, EME, EQIX, ETR, FCX, GEV, GS, HST, NEE, PWR, WMT _(включително 1 за първи път в историята: EQIX)_
  - **Exited:** BKR, EIX, EXPE, FDX, INCY, JBHT, JNJ, MAR, MRK, PLD, USB, VTR, VTRS, WELL

**stable_winner (3m):** +3 entered, -6 exited
  - **Entered:** EQIX, IRM, PWR
  - **Exited:** CAT, MNST, RL, SPG, VTR, WDC

**quality_dip (1m):** +14 entered, -13 exited
  - **Entered:** EIX, EXPE, FDX, HLT, INCY, JBHT, JNJ, MAR, MRK, PLD, USB, VTR, VTRS, WELL _(включително 4 за първи път в историята: FDX, HLT, JBHT, MAR)_
  - **Exited:** AEP, BEN, BK, EME, EQIX, ETR, FCX, GEV, GS, HST, NEE, PWR, WMT

**quality_dip (3m):** +7 entered, -4 exited
  - **Entered:** CAT, HLT, MNST, RL, SPG, VTR, WDC _(включително 2 за първи път в историята: CAT, HLT)_
  - **Exited:** BKR, EQIX, IRM, PWR

**faded_bounce (1m):** +7 entered, -11 exited
  - **Entered:** BR, BX, CCI, HRL, INVH, KKR, STZ _(включително 1 за първи път в историята: CCI)_
  - **Exited:** ABT, AJG, AON, AVB, AWK, EOG, GIS, MAA, MRSH, RSG, SO

**faded_bounce (3m):** +3 entered, -7 exited
  - **Entered:** AMT, CARR, EQT _(включително 2 за първи път в историята: AMT, EQT)_
  - **Exited:** ARE, AVB, BSX, CI, GIS, PEG, TDG

### EU (period: 2026-08-28 → 2026-09-02)

**stable_winner (1m):** +9 entered, -10 exited
  - **Entered:** BPE.MI, HOC.L, NDA.DE, SDR.L, SPSN.SW, SWED-A.ST, TSCO.L, UNI.MC, URW.PA
  - **Exited:** ABN.AS, ALLN.SW, ANTO.L, ASML.AS, BARN.SW, BCP.LS, EMG.L, GAW.L, HSBA.L, STAN.L

**stable_winner (3m):** +4 entered, -8 exited
  - **Entered:** BIRG.IR, DANSKE.CO, ENR.DE, SPM.MI
  - **Exited:** BCP.LS, EBS.VI, FTK.DE, GLE.PA, ING.WA, INGA.AS, SAN.MC, SPSN.SW

**quality_dip (1m):** +10 entered, -10 exited
  - **Entered:** ABN.AS, ALLN.SW, ANTO.L, ASML.AS, BARN.SW, BCP.LS, GAW.L, HSBA.L, MBK.WA, STAN.L _(включително 1 за първи път в историята: MBK.WA)_
  - **Exited:** BPE.MI, HOC.L, NDA.DE, SBRY.L, SDR.L, SPSN.SW, SWED-A.ST, TSCO.L, UNI.MC, URW.PA

**quality_dip (3m):** +9 entered, -6 exited
  - **Entered:** BCP.LS, EBS.VI, FTK.DE, GLE.PA, ING.WA, INGA.AS, MBK.WA, SAN.MC, SPSN.SW
  - **Exited:** BIRG.IR, DANSKE.CO, EMG.L, ENR.DE, SBRY.L, SPM.MI

**faded_bounce (1m):** +9 entered, -5 exited
  - **Entered:** ADYEN.AS, BKW.SW, CAP.PA, CS.PA, LIFCO-B.ST, NEM.DE, RNO.PA, SGO.PA, VTY.L _(включително 1 за първи път в историята: VTY.L)_
  - **Exited:** BC.MI, BTRW.L, RACE.MI, RED.MC, VPK.AS

**faded_bounce (3m):** +1 entered, -6 exited
  - **Entered:** VTY.L _(включително 1 за първи път в историята: VTY.L)_
  - **Exited:** BC.MI, BEIJ-B.ST, DGE.L, LISP.SW, SY1.DE, ZURN.SW



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-08-25 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **cotton** | Commodities | 95841 | 97.8 | 97.8 | 1055 | 43431 |
| **corn** | Commodities | 376513 | 97.4 | 97.4 | 1055 | 208114 |
| **soybeans** | Commodities | 198254 | 94.5 | 94.5 | 1055 | 43253 |
| **copper** | Commodities | 76446 | 94.3 | 94.3 | 1055 | 9956 |
| **soymeal** | Commodities | 97036 | 94.0 | 94.0 | 1055 | 8381 |
| **sugar** | Commodities | 207082 | 91.9 | 91.9 | 1055 | 319495 |
| **soyoil** | Commodities | 88442 | 91.7 | 91.7 | 1055 | -21413 |
| **rbob** | Commodities | 79858 | 88.4 | 88.4 | 1055 | 5891 |
| **aud** | FX | 54061 | 85.9 | 85.9 | 1055 | 26443 |
| **gbpfx** | FX | 47909 | 84.7 | 84.7 | 1055 | 6812 |
| **dxy** | FX | 9189 | 83.1 | 83.1 | 1055 | 10790 |
| **gold** | Commodities | 151315 | 66.7 | 66.7 | 1055 | 30987 |
| **coffee** | Commodities | 26693 | 65.9 | 65.9 | 1055 | 1557 |
| **vix** | Volatility | -30143 | 60.1 | 60.1 | 1014 | -17854 |
| **heatingoil** | Commodities | 17342 | 57.2 | 57.2 | 1055 | 5968 |
| **brent** | Commodities | 7238 | 54.2 | 54.2 | 238 | -9557 |
| **wheat** | Commodities | -14171 | 52.1 | 52.1 | 1055 | -7291 |
| **platinum** | Commodities | 10475 | 48.1 | 48.1 | 1055 | 4098 |
| **cattle** | Commodities | 57441 | 47.9 | 47.9 | 1055 | -9082 |
| **sp500** | US Equities | -315204 | 44.7 | 44.7 | 1055 | -17728 |
| **eurfx** | FX | -38359 | 34.9 | 34.9 | 1055 | 26839 |
| **silver** | Commodities | 13235 | 33.3 | 33.3 | 1055 | 4848 |
| **natgas** | Commodities | -71496 | 31.0 | 31.0 | 1055 | 34109 |
| **bitcoin** | Crypto | -8089 | 30.1 | 30.1 | 438 | -1216 |
| **chf** | FX | -8825 | 27.2 | 27.2 | 1055 | 822 |
| **wti** | Commodities | 104573 | 22.3 | 22.3 | 1055 | -3734 |
| **us30y** | Rates | -302994 | 18.5 | 18.5 | 1055 | 86528 |
| **us2y** | Rates | -1232753 | 18.1 | 18.1 | 1055 | 331541 |
| **nasdaq** | US Equities | -41232 | 14.7 | 14.7 | 1055 | 17066 |
| **jpy** | FX | -77042 | 12.8 | 12.8 | 1055 | 24948 |
| **cocoa** | Commodities | -14627 | 11.8 | 11.8 | 1055 | -500 |
| **us5y** | Rates | -2111810 | 11.6 | 11.6 | 1055 | -3172 |
| **palladium** | Commodities | -5486 | 11.2 | 11.2 | 1055 | 687 |
| **russell** | US Equities | -97700 | 8.8 | 8.8 | 591 | -23080 |
| **usultra10y** | Rates | -372157 | 7.3 | 7.3 | 545 | 28053 |
| **cad** | FX | -72092 | 5.8 | 5.8 | 1055 | 30403 |
| **us10y** | Rates | -2134339 | 3.1 | 3.1 | 1055 | 21400 |
| **hogs** | Commodities | -31135 | 0.1 | 0.1 | 1055 | -20251 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MRNA** | Healthcare | 96.8 | 164.6% | 207.4% | 160.9% | 135.6% | 1.41 | -34.2% |
| 2 | **VLO** | Energy | 94.8 | 18.6% | 40.6% | 63.7% | 104.3% | 2.34 | -12.1% |
| 3 | **MPC** | Energy | 94.0 | 24.1% | 45.2% | 76.5% | 75.9% | 2.16 | -18.3% |
| 4 | **DELL** | Technology | 93.0 | 5.3% | 17.1% | 236.2% | 291.2% | 1.95 | -32.3% |
| 5 | **PSX** | Energy | 90.6 | 25.0% | 39.4% | 57.4% | 57.5% | 2.05 | -17.3% |
| 6 | **PANW** | Technology | 89.9 | -10.3% | 17.1% | 107.2% | 92.3% | 1.11 | -36.0% |
| 7 | **CRL** | Healthcare | 88.4 | 24.6% | 62.2% | 62.5% | 45.2% | 1.20 | -33.9% |
| 8 | **STT** | Financial Services | 88.3 | 2.6% | 21.0% | 51.9% | 67.8% | 2.01 | -11.8% |
| 9 | **TGT** | Consumer Defensive | 88.3 | 11.1% | 31.9% | 38.4% | 65.4% | 1.86 | -19.6% |
| 10 | **CRWD** | Technology | 87.9 | -3.7% | 8.8% | 99.6% | 104.3% | 1.19 | -37.2% |
| 11 | **CNC** | Healthcare | 87.2 | 5.1% | 13.1% | 49.7% | 116.3% | 1.58 | -32.7% |
| 12 | **FTNT** | Technology | 87.1 | -8.2% | 5.5% | 86.7% | 118.8% | 1.61 | -26.9% |
| 13 | **MRK** | Healthcare | 85.7 | 18.5% | 33.2% | 27.9% | 54.8% | 1.87 | -11.4% |
| 14 | **EXPE** | Consumer Cyclical | 83.9 | -1.1% | 36.9% | 39.7% | 48.0% | 0.68 | -37.4% |
| 15 | **APA** | Energy | 83.6 | 24.9% | 17.4% | 45.7% | 55.4% | 1.33 | -27.7% |
| 16 | **MU** | Technology | 83.5 | 7.1% | -11.4% | 138.7% | 654.6% | 2.54 | -39.1% |
| 17 | **NUE** | Basic Materials | 83.5 | -3.7% | 2.7% | 50.8% | 89.7% | 1.76 | -18.4% |
| 18 | **HPE** | Technology | 83.3 | -1.1% | -5.7% | 142.8% | 135.8% | 1.54 | -26.4% |
| 19 | **BNY** | Financial Services | 83.1 | 3.3% | 15.7% | 38.0% | 52.4% | 1.92 | -10.2% |
| 20 | **SNDK** | Technology | 82.5 | 8.8% | -15.2% | 159.3% | 2695.4% | 2.92 | -56.5% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **RBI.VI** | Financial Services | 92.6 | 4.0% | 29.1% | 67.4% | 121.4% | 2.15 | -18.0% |
| 2 | **AKER.OL** | Industrials | 91.6 | 19.5% | 25.2% | 73.4% | 91.9% | 2.56 | -15.6% |
| 3 | **CCC.L** | Technology | 91.2 | 19.7% | 21.9% | 72.6% | 101.9% | 2.54 | -16.2% |
| 4 | **UNI.MI** | Financial Services | 89.3 | 0.9% | 35.6% | 48.4% | 68.6% | 1.90 | -11.5% |
| 5 | **REP.MC** | Energy | 88.9 | 7.5% | 25.3% | 42.7% | 92.2% | 2.15 | -20.4% |
| 6 | **BMPS.MI** | Financial Services | 88.6 | -1.4% | 28.6% | 63.5% | 67.0% | 1.44 | -25.5% |
| 7 | **BBVA.MC** | Financial Services | 87.9 | 2.0% | 29.3% | 39.7% | 65.8% | 1.70 | -18.7% |
| 8 | **ABN.AS** | Financial Services | 87.6 | 7.5% | 25.2% | 57.0% | 60.9% | 1.94 | -18.0% |
| 9 | **ATS.VI** | Technology | 87.4 | 6.5% | 3.8% | 197.6% | 623.4% | 2.51 | -50.1% |
| 10 | **BAYN.DE** | Healthcare | 86.9 | 3.7% | 37.5% | 31.1% | 72.2% | 1.35 | -30.6% |
| 11 | **PKN.WA** | Energy | 86.4 | 4.4% | 13.2% | 43.9% | 102.3% | 2.19 | -12.3% |
| 12 | **TKA.DE** | Basic Materials | 86.2 | 16.2% | 20.8% | 44.5% | 80.3% | 1.30 | -41.4% |
| 13 | **UNI.MC** | Financial Services | 85.8 | 5.6% | 26.1% | 44.8% | 54.7% | 1.89 | -17.8% |
| 14 | **BG.VI** | Financial Services | 85.1 | -0.5% | 16.6% | 45.6% | 68.0% | 1.88 | -16.3% |
| 15 | **BPE.MI** | Financial Services | 84.6 | -2.2% | 21.7% | 30.0% | 76.5% | 1.86 | -18.1% |
| 16 | **BFT.WA** | Industrials | 84.6 | -2.2% | 16.4% | 43.2% | 68.3% | 1.76 | -17.4% |
| 17 | **ELE.MC** | Utilities | 84.4 | -0.4% | 19.1% | 29.8% | 72.5% | 2.58 | -7.6% |
| 18 | **FRO.OL** | Energy | 84.0 | 12.1% | 31.7% | 19.2% | 83.0% | 1.66 | -20.5% |
| 19 | **BMED.MI** | Financial Services | 83.7 | 1.4% | 23.3% | 40.2% | 50.6% | 1.70 | -18.7% |
| 20 | **NESTE.HE** | Energy | 83.6 | 8.4% | 8.1% | 44.6% | 90.1% | 1.69 | -20.4% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **EIX** | Utilities | 2.397 | 1.944 | 1.030 | 3.219 | -1.051 | - | 5.8 | +19.7% |
| 2 | **SNDK** | Information Technology | 1.664 | 1.837 | 1.765 | 0.618 | -0.021 | - | 21.1 | +91.6% |
| 3 | **CF** | Materials | 1.558 | 0.903 | 1.295 | 1.720 | 0.463 | - | 10.2 | +29.9% |
| 4 | **NEM** | Materials | 1.352 | 0.657 | 1.718 | 0.939 | 0.514 | - | 16.4 | +25.9% |
| 5 | **MO** | Consumer Staples | 1.347 | 0.067 | 2.010 | 1.131 | -0.350 | - | 14.6 | - |
| 6 | **TPR** | Consumer Discretionary | 1.322 | 1.818 | 1.146 | 0.458 | -1.026 | - | 16.9 | +197.1% |
| 7 | **HST** | Real Estate | 1.313 | 1.580 | 0.479 | 1.402 | -0.288 | - | 14.8 | +15.6% |
| 8 | **APA** | Energy | 1.253 | 1.065 | 1.262 | 0.831 | -0.352 | - | 9.3 | +26.7% |
| 9 | **DVA** | Health Care | 1.213 | 1.322 | 0.194 | 1.700 | -1.476 | - | 15.4 | +88.5% |
| 10 | **SYF** | Financials | 1.144 | -0.138 | 1.185 | 1.725 | -0.405 | - | 8.2 | +20.8% |
| 11 | **SPG** | Real Estate | 1.143 | 0.890 | 1.372 | 0.583 | -1.369 | - | 14.9 | +120.5% |
| 12 | **BMY** | Health Care | 1.070 | 0.906 | 0.862 | 0.959 | 0.584 | - | 15.0 | +46.6% |
| 13 | **EXPE** | Consumer Discretionary | 1.070 | 1.666 | 0.796 | 0.345 | -0.668 | - | 19.1 | +89.5% |
| 14 | **MAS** | Industrials | 1.059 | -0.316 | 1.438 | 1.384 | -0.770 | - | 16.5 | +5862.5% |
| 15 | **MU** | Information Technology | 0.992 | 1.605 | 0.899 | 0.085 | -0.559 | - | 21.6 | +66.6% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -1.847 | -1.316 | -0.912 | -2.484 | -1.081 |
| 502 | **COIN** | Financials | -1.692 | -2.633 | -1.713 | 0.000 | -1.696 |
| 501 | **CSGP** | Real Estate | -1.688 | -3.429 | -0.461 | -0.679 | 0.693 |
| 500 | **BA** | Industrials | -1.605 | -0.649 | -1.149 | -2.204 | -1.227 |
| 499 | **TSLA** | Consumer Discretionary | -1.579 | -0.049 | -1.354 | -2.447 | -0.389 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W36.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W36.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-08-31  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
