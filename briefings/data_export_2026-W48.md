# Сателит — пълен data export за 2026-W48

_Период: 2026-11-23 → 2026-11-29_  
_Генериран: 2026-11-27 16:17 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W48.md` (structured briefing) и `narrative_2026-W48.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**23 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **XLB** | +5.94% | +2.58σ | 48.34 | 51.21 | 2026-11-20 | 2026-11-25 | -0.75% | +2.59% | 13 |
| **IWM** | +4.78% | +2.52σ | 256.61 | 268.87 | 2026-11-20 | 2026-11-25 | -1.16% | +2.36% | 13 |
| **VNQ** | +3.35% | +2.18σ | 92.56 | 95.66 | 2026-11-20 | 2026-11-25 | -0.46% | +1.75% | 13 |
| **XLI** | +4.21% | +2.14σ | 156.37 | 162.95 | 2026-11-20 | 2026-11-25 | -1.06% | +2.45% | 13 |
| **XLY** | +4.47% | +2.12σ | 112.46 | 117.49 | 2026-11-20 | 2026-11-25 | -0.34% | +2.27% | 13 |
| **DIA** | +4.20% | +2.09σ | 481.08 | 501.27 | 2026-11-20 | 2026-11-25 | -0.74% | +2.37% | 13 |
| **XLRE** | +3.30% | +1.98σ | 42.46 | 43.86 | 2026-11-20 | 2026-11-25 | -0.44% | +1.89% | 13 |
| **VWO** | +4.27% | +1.92σ | 50.62 | 52.78 | 2026-11-20 | 2026-11-25 | -1.31% | +2.91% | 13 |
| **DFEN** | +11.26% | +1.86σ | 39.70 | 44.17 | 2026-11-20 | 2026-11-25 | -4.13% | +8.29% | 13 |
| **EFA** | +3.16% | +1.79σ | 96.14 | 99.18 | 2026-11-20 | 2026-11-25 | -0.88% | +2.26% | 13 |
| **SPY** | +3.90% | +1.79σ | 689.81 | 716.70 | 2026-11-20 | 2026-11-25 | -0.76% | +2.60% | 13 |
| **URA** | +3.43% | +1.78σ | 26.79 | 27.71 | 2026-11-20 | 2026-11-25 | -3.99% | +4.17% | 13 |
| **EEM** | +4.75% | +1.77σ | 53.84 | 56.40 | 2026-11-20 | 2026-11-25 | -1.61% | +3.59% | 13 |
| **XLC** | +5.35% | +1.77σ | 100.03 | 105.38 | 2026-11-20 | 2026-11-25 | -0.76% | +3.46% | 13 |
| **VEA** | +3.22% | +1.76σ | 63.62 | 65.67 | 2026-11-20 | 2026-11-25 | -1.07% | +2.43% | 13 |
| **GDX** | +8.03% | +1.70σ | 68.40 | 73.89 | 2026-11-20 | 2026-11-25 | -2.88% | +6.42% | 13 |
| **XLF** | +3.56% | +1.55σ | 54.57 | 56.51 | 2026-11-20 | 2026-11-25 | -0.37% | +2.53% | 13 |
| **QQQ** | +4.19% | +1.44σ | 608.45 | 633.93 | 2026-11-20 | 2026-11-25 | -1.15% | +3.70% | 13 |
| **XLK** | +4.55% | +1.27σ | 149.01 | 155.79 | 2026-11-20 | 2026-11-25 | -1.46% | +4.72% | 13 |
| **XLV** | +3.63% | +1.24σ | 177.24 | 183.68 | 2026-11-20 | 2026-11-25 | +0.15% | +2.81% | 13 |
| **HYG** | +0.25% | +1.10σ | 76.33 | 76.52 | 2026-11-20 | 2026-11-25 | -0.32% | +0.52% | 13 |
| **GLD** | +1.42% | +1.07σ | 322.87 | 327.45 | 2026-11-20 | 2026-11-25 | -2.01% | +3.19% | 13 |
| **UUP** | -0.07% | -1.02σ | 29.62 | 29.60 | 2026-11-20 | 2026-11-25 | +0.46% | +0.52% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-11-29 · **Conditions matched:** 0/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | +0.19% | ❌ | 139.63 | 139.89 | 2026-11-20 | 2026-11-25 |
| DFEN | down ≥ 3.0% | +11.26% | ❌ | 39.70 | 44.17 | 2026-11-20 | 2026-11-25 |
| GLD | down ≥ 1.0% | +1.42% | ❌ | 322.87 | 327.45 | 2026-11-20 | 2026-11-25 |
| URA | down ≥ 3.0% | +3.43% | ❌ | 26.79 | 27.71 | 2026-11-20 | 2026-11-25 |
| UUP | up ≥ 0.5% | -0.07% | ❌ | 29.62 | 29.60 | 2026-11-20 | 2026-11-25 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — 🔔 ТРИГГЕРИРАН
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-11-29 · **Conditions matched:** 3/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | +4.78% | ✅ | 256.61 | 268.87 | 2026-11-20 | 2026-11-25 |
| XLF | up ≥ 1.0% | +3.56% | ✅ | 54.57 | 56.51 | 2026-11-20 | 2026-11-25 |
| XLY | up ≥ 1.0% | +4.47% | ✅ | 112.46 | 117.49 | 2026-11-20 | 2026-11-25 |
| GLD | down ≥ 0.5% | +1.42% | ❌ | 322.87 | 327.45 | 2026-11-20 | 2026-11-25 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2025-W48 (week ending 2025-11-30)
**Cosine similarity:** 0.9403 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.53% | +0.38% | +10.70% |
| **USO** | -1.87% | +15.31% | +81.64% |
| **GLD** | +2.84% | +24.72% | +7.54% |
| **TLT** | -2.61% | +0.68% | -4.93% |
| **XLE** | -0.59% | +23.65% | +24.47% |
| **IWM** | -0.29% | +5.09% | +16.76% |

### Паралел #2: 2025-W17 (week ending 2025-04-27)
**Cosine similarity:** 0.9204 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +7.36% | +15.70% | +22.99% |
| **USO** | -2.54% | +8.43% | +6.01% |
| **GLD** | -0.08% | +0.88% | +23.89% |
| **TLT** | -3.55% | -2.77% | +2.90% |
| **XLE** | +0.38% | +5.72% | +6.89% |
| **IWM** | +7.00% | +15.59% | +28.49% |

### Паралел #3: 2024-W33 (week ending 2024-08-18)
**Cosine similarity:** 0.9186 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.58% | +5.67% | +9.99% |
| **USO** | -6.03% | -8.61% | -0.66% |
| **GLD** | +2.31% | +1.98% | +14.79% |
| **TLT** | +3.49% | -7.55% | -8.51% |
| **XLE** | -3.02% | +4.71% | -0.44% |
| **IWM** | +3.20% | +7.47% | +6.29% |

### Паралел #4: 2022-W25 (week ending 2022-06-26)
**Cosine similarity:** 0.9013 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.21% | -5.67% | -1.84% |
| **USO** | -7.52% | -19.63% | -14.70% |
| **GLD** | -5.91% | -10.04% | -1.66% |
| **TLT** | +4.37% | -6.09% | -9.24% |
| **XLE** | +2.10% | -1.55% | +21.61% |
| **IWM** | +2.42% | -4.44% | -0.40% |

### Паралел #5: 2022-W36 (week ending 2022-09-11)
**Cosine similarity:** 0.8938 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -12.02% | -3.28% | -5.09% |
| **USO** | +0.91% | -11.60% | -5.57% |
| **GLD** | -2.92% | +4.53% | +8.79% |
| **TLT** | -7.80% | -1.83% | -2.51% |
| **XLE** | -1.39% | +2.58% | +2.52% |
| **IWM** | -10.50% | -4.69% | -5.99% |

### Паралел #6: 2023-W44 (week ending 2023-11-05)
**Cosine similarity:** 0.8906 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.04% | +13.72% | +17.62% |
| **USO** | -9.71% | -9.81% | +0.37% |
| **GLD** | +1.28% | +2.07% | +15.24% |
| **TLT** | +7.97% | +9.63% | +2.52% |
| **XLE** | -4.07% | -3.65% | +6.80% |
| **IWM** | +5.67% | +11.42% | +15.71% |

### Паралел #7: 2023-W22 (week ending 2023-06-04)
**Cosine similarity:** 0.8871 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.71% | +5.44% | +7.29% |
| **USO** | -1.18% | +19.91% | +7.93% |
| **GLD** | -1.43% | -0.52% | +6.05% |
| **TLT** | +0.09% | -7.00% | -8.82% |
| **XLE** | +1.83% | +13.57% | +6.41% |
| **IWM** | +3.09% | +4.85% | +1.59% |

### Паралел #8: 2024-W12 (week ending 2024-03-24)
**Cosine similarity:** 0.8800 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -2.99% | +4.47% | +9.03% |
| **USO** | +4.30% | +2.57% | -4.90% |
| **GLD** | +7.33% | +7.20% | +20.89% |
| **TLT** | -5.27% | -0.02% | +5.21% |
| **XLE** | +4.03% | -2.87% | -3.94% |
| **IWM** | -3.17% | -2.30% | +8.05% |

### Паралел #9: 2022-W45 (week ending 2022-11-13)
**Cosine similarity:** 0.8771 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.87% | +2.39% | +3.28% |
| **USO** | -11.45% | -6.06% | -16.55% |
| **GLD** | +2.40% | +5.35% | +13.52% |
| **TLT** | +10.02% | +5.62% | +6.52% |
| **XLE** | -7.16% | -3.14% | -15.69% |
| **IWM** | -2.95% | +1.82% | -7.59% |

### Паралел #10: 2021-W29 (week ending 2021-07-25)
**Cosine similarity:** 0.8714 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.83% | +3.00% | -0.45% |
| **USO** | -4.25% | +17.30% | +22.86% |
| **GLD** | +0.05% | -0.47% | +1.50% |
| **TLT** | +0.53% | -2.94% | -3.28% |
| **XLE** | -0.25% | +19.44% | +28.71% |
| **IWM** | +1.02% | +3.58% | -10.28% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 16 · **Total matching days:** 96 · **History:** 2021-05-17 → 2026-11-25

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.0% | +2.2% | -3.1% | +7.4% | 69% |
| **SPY** | 3m | 16 | +1.7% | +2.5% | -7.3% | +12.0% | 69% |
| **SPY** | 6m | 16 | +5.6% | +8.6% | -6.8% | +21.8% | 62% |
| **USO** | 1m | 16 | -0.6% | -1.2% | -14.3% | +12.7% | 44% |
| **USO** | 3m | 16 | -1.5% | -5.1% | -18.9% | +30.5% | 44% |
| **USO** | 6m | 16 | +11.6% | +2.1% | -13.5% | +109.4% | 56% |
| **GLD** | 1m | 16 | +2.1% | +0.8% | -7.0% | +9.0% | 69% |
| **GLD** | 3m | 16 | +2.8% | +3.4% | -17.4% | +24.5% | 62% |
| **GLD** | 6m | 16 | +2.4% | +3.4% | -17.4% | +25.3% | 56% |
| **TLT** | 1m | 16 | -1.5% | -1.1% | -6.7% | +3.6% | 31% |
| **TLT** | 3m | 16 | -0.4% | +0.5% | -16.5% | +11.1% | 56% |
| **TLT** | 6m | 16 | -3.6% | -2.5% | -18.0% | +7.5% | 38% |

**Episodes (последни 5 от 16):**
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-08-03` (5d)
- `2026-09-10 → 2026-10-01` (14d)
- `2026-10-16 → 2026-10-27` (8d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 122 · **History:** 2021-05-17 → 2026-11-25

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +6.3% | +6.3% | +3.5% | +9.1% | 100% |
| **SPY** | 3m | 2 | +6.9% | +6.9% | +3.5% | +10.3% | 100% |
| **SPY** | 6m | 2 | +5.1% | +5.1% | -4.7% | +15.0% | 50% |
| **USO** | 1m | 2 | +5.6% | +5.6% | +4.0% | +7.2% | 100% |
| **USO** | 3m | 2 | +8.7% | +8.7% | -9.9% | +27.4% | 50% |
| **USO** | 6m | 2 | +16.0% | +16.0% | +15.5% | +16.4% | 100% |
| **GLD** | 1m | 2 | +3.5% | +3.5% | -0.2% | +7.2% | 50% |
| **GLD** | 3m | 2 | -5.6% | -5.6% | -13.8% | +2.6% | 50% |
| **GLD** | 6m | 2 | -12.8% | -12.8% | -13.5% | -12.0% | 0% |
| **TLT** | 1m | 2 | -1.4% | -1.4% | -1.8% | -1.0% | 0% |
| **TLT** | 3m | 2 | -4.9% | -4.9% | -6.8% | -2.9% | 0% |
| **TLT** | 6m | 2 | -6.7% | -6.7% | -11.2% | -2.2% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-11-12` (75d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 493 · **History:** 2021-05-17 → 2026-11-25

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
- `2025-11-03 → 2026-11-25` (261d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 1 · **Total matching days:** 1 · **History:** 2021-05-17 → 2026-11-25

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | -1.5% | -1.5% | -1.5% | -1.5% | 0% |
| **SPY** | 3m | 1 | -7.1% | -7.1% | -7.1% | -7.1% | 0% |
| **SPY** | 6m | 1 | -7.1% | -7.1% | -7.1% | -7.1% | 0% |
| **USO** | 1m | 1 | +14.3% | +14.3% | +14.3% | +14.3% | 100% |
| **USO** | 3m | 1 | -5.7% | -5.7% | -5.7% | -5.7% | 0% |
| **USO** | 6m | 1 | -5.7% | -5.7% | -5.7% | -5.7% | 0% |
| **GLD** | 1m | 1 | -6.8% | -6.8% | -6.8% | -6.8% | 0% |
| **GLD** | 3m | 1 | -16.8% | -16.8% | -16.8% | -16.8% | 0% |
| **GLD** | 6m | 1 | -16.8% | -16.8% | -16.8% | -16.8% | 0% |
| **TLT** | 1m | 1 | +2.5% | +2.5% | +2.5% | +2.5% | 100% |
| **TLT** | 3m | 1 | +3.7% | +3.7% | +3.7% | +3.7% | 100% |
| **TLT** | 6m | 1 | +3.7% | +3.7% | +3.7% | +3.7% | 100% |

**Episodes (последни 5 от 1):**
- `2026-09-25 → 2026-09-25` (1d)

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 10 · **Total matching days:** 101 · **History:** 2021-05-17 → 2026-11-25

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 10 | -0.1% | +0.6% | -7.2% | +7.8% | 60% |
| **SPY** | 3m | 10 | +1.3% | -0.9% | -8.3% | +11.6% | 50% |
| **SPY** | 6m | 10 | -0.2% | +0.0% | -20.8% | +14.2% | 50% |
| **USO** | 1m | 10 | +4.1% | +0.5% | -15.0% | +52.9% | 50% |
| **USO** | 3m | 10 | +9.6% | +5.5% | -20.7% | +52.2% | 50% |
| **USO** | 6m | 10 | +10.2% | +2.2% | -27.6% | +56.3% | 50% |
| **GLD** | 1m | 10 | -1.2% | -1.9% | -8.3% | +11.7% | 20% |
| **GLD** | 3m | 10 | -2.9% | -1.4% | -17.5% | +6.4% | 40% |
| **GLD** | 6m | 10 | -3.5% | -5.9% | -17.5% | +25.0% | 30% |
| **TLT** | 1m | 10 | -2.4% | -2.7% | -6.0% | +2.5% | 10% |
| **TLT** | 3m | 10 | -5.9% | -4.9% | -17.6% | +4.2% | 30% |
| **TLT** | 6m | 10 | -9.1% | -8.1% | -22.3% | +1.2% | 20% |

**Episodes (последни 5 от 10):**
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-05-19` (36d)
- `2026-07-22 → 2026-08-03` (8d)
- `2026-09-01 → 2026-09-28` (15d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 17 · **Total matching days:** 294 · **History:** 2021-05-17 → 2026-11-25

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 17 | +1.9% | +1.6% | -4.8% | +9.0% | 71% |
| **SPY** | 3m | 17 | +2.8% | +4.2% | -12.6% | +16.2% | 71% |
| **SPY** | 6m | 17 | +6.1% | +8.1% | -14.0% | +21.0% | 76% |
| **USO** | 1m | 17 | +2.4% | -2.2% | -13.0% | +22.9% | 41% |
| **USO** | 3m | 17 | +3.4% | -0.8% | -14.5% | +29.9% | 41% |
| **USO** | 6m | 17 | +13.8% | +2.6% | -12.4% | +87.1% | 71% |
| **GLD** | 1m | 17 | +2.4% | +2.1% | -5.6% | +9.0% | 76% |
| **GLD** | 3m | 17 | +5.5% | +7.2% | -16.8% | +23.6% | 65% |
| **GLD** | 6m | 17 | +9.4% | +9.8% | -17.8% | +43.8% | 71% |
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
**Episodes:** 21 · **Total matching days:** 310 · **History:** 2021-05-17 → 2026-11-25

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 21 | +0.1% | -0.0% | -8.7% | +7.0% | 48% |
| **SPY** | 3m | 21 | +1.3% | +2.7% | -13.7% | +9.1% | 62% |
| **SPY** | 6m | 21 | +2.1% | +1.3% | -16.4% | +16.9% | 62% |
| **USO** | 1m | 21 | -0.4% | -3.9% | -21.8% | +55.8% | 43% |
| **USO** | 3m | 21 | +3.1% | -1.3% | -12.7% | +64.3% | 43% |
| **USO** | 6m | 21 | +7.4% | -3.9% | -16.0% | +75.1% | 48% |
| **GLD** | 1m | 21 | -1.1% | -0.2% | -12.4% | +7.6% | 43% |
| **GLD** | 3m | 21 | +0.5% | +1.3% | -17.8% | +19.0% | 62% |
| **GLD** | 6m | 21 | +5.2% | +2.7% | -17.8% | +55.5% | 62% |
| **TLT** | 1m | 21 | -0.1% | -0.1% | -5.6% | +5.2% | 48% |
| **TLT** | 3m | 21 | -3.1% | -3.4% | -17.3% | +8.7% | 38% |
| **TLT** | 6m | 21 | -6.0% | -3.6% | -21.4% | +4.6% | 29% |

**Episodes (последни 5 от 21):**
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (13d)
- `2026-09-21 → 2026-10-15` (16d)
- `2026-11-13 → 2026-11-23` (6d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-11-25

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (8 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **US_PMI_COMPOSITE** | S&P Global US Composite PMI | growth | diffusion_indices | 5 | 2.60 | 2.60 | 2026-11-07 00:00:00 | 2026-11-23 00:00:00 | ✓ |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 5 | 2.52 | 2.54 | 2026-11-07 00:00:00 | 2026-11-23 00:00:00 | - |
| **US_PMI_SVCS** | S&P Global US Services PMI | growth | diffusion_indices | 5 | 2.09 | 2.09 | 2026-11-07 00:00:00 | 2026-11-23 00:00:00 | ✓ |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 5 | 2.08 | 2.08 | 2026-11-07 00:00:00 | 2026-11-23 00:00:00 | ✓ |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 5 | 2.07 | 2.07 | 2026-11-07 00:00:00 | 2026-11-23 00:00:00 | ✓ |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 2 | 2.16 | 2.16 | 2026-11-07 00:00:00 | 2026-11-14 00:00:00 | - |
| **HY_OAS** | High Yield спред (HY OAS) | liquidity | credit_spreads | 1 | 2.38 | 2.38 | 2026-11-23 00:00:00 | 2026-11-23 00:00:00 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | 1 | 2.06 | 2.06 | 2026-11-07 00:00:00 | 2026-11-07 00:00:00 | - |

### EU (8 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.21 | 5.21 | 2026-11-07 00:00:00 | 2026-11-23 00:00:00 | - |
| **EA_OAT_BUND_SPREAD** | OAT-Bund spread (FR-DE 10Y, pp) | credit | sovereign_spreads | 5 | 4.63 | 5.17 | 2026-11-07 00:00:00 | 2026-11-23 00:00:00 | ✓ |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.65 | 2.70 | 2026-11-07 00:00:00 | 2026-11-23 00:00:00 | ✓ |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | 5 | 2.29 | 2.32 | 2026-11-07 00:00:00 | 2026-11-23 00:00:00 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation | sentiment | 5 | 2.28 | 2.28 | 2026-11-07 00:00:00 | 2026-11-23 00:00:00 | - |
| **EA_HICP_ENERGY** | HICP енергия, YoY | inflation | headline_measures | 5 | 2.18 | 2.19 | 2026-11-07 00:00:00 | 2026-11-23 00:00:00 | - |
| **EA_EMPLOYMENT_PERSONS** | Заетост — брой наети (нац. сметки, EA-20, хил. лица) | labor | employment | 5 | 2.12 | 2.14 | 2026-11-07 00:00:00 | 2026-11-23 00:00:00 | ✓ |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.09 | 2.25 | 2026-11-07 00:00:00 | 2026-11-23 00:00:00 | ✓ |

### CN (5 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 8 | 2.23 | 2.23 | 2026-11-07 00:00:00 | 2026-11-26 00:00:00 | ✓ |
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 6 | 2.53 | 2.53 | 2026-11-07 00:00:00 | 2026-11-26 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 6 | 2.19 | 2.19 | 2026-11-07 00:00:00 | 2026-11-22 00:00:00 | - |
| **CN_GDP_DEFLATOR_Q** | БВП дефлатор (тримесечен, YoY %) | inflation | deflator_quarterly | 1 | 2.15 | 2.15 | 2026-11-26 00:00:00 | 2026-11-26 00:00:00 | - |
| **CN_RE_INVEST_YOY** | Инвестиции в имоти — натрупани от началото на годината (YoY %) | property | investment | 1 | 2.07 | 2.07 | 2026-11-26 00:00:00 | 2026-11-26 00:00:00 | ✓ |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-11-23 00:00:00 · **Generated:** 2026-11-23 21:10:43.832413+00:00

**Режим:** `policy_dilemma` (Policy dilemma)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 42.9 | mixed | 37.0% | 1 | 1 |
| **growth** | 48.4 | mixed | 48.0% | 3 | 3 |
| **inflation** | 39.0 | mixed | 33.3% | 2 | 1 |
| **liquidity** | 38.9 | mixed | 31.6% | 1 | 0 |

### Top anomalies (6 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **US_PMI_COMPOSITE** | S&P Global US Composite PMI | growth | diffusion_indices | +2.60 | up | 58.40 | 2026-09-01 | ✓ max |
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | +2.54 | up | 6.52 | 2026-10-01 | - |
| **HY_OAS** | High Yield спред (HY OAS) | liquidity | credit_spreads | +2.38 | up | 3.76 | 2026-11-20 | - |
| **US_PMI_SVCS** | S&P Global US Services PMI | growth | diffusion_indices | +2.09 | up | 58.80 | 2026-09-01 | ✓ max |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.08 | down | 93.73 | 2026-07-01 | ✓ min |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | +2.07 | up | 55.90 | 2026-09-01 | ✓ max |

### Narrative hints от макро лещите
- **US_PMI_COMPOSITE**: Markit композит — global benchmark, complement към ISM. Flash + final estimates.
- **PPIFIS**: Производствени цени → consumer prices с 1-3 месечен lag. Водещ за CPI при трендови промени.
- **HY_OAS**: Risk premium на junk bonds. Spikes предхождат equity volatility и рецесионен стрес. < 300 bps = risk-on; > 800 bps = distress.
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
  - `breadth_b`: 0.0
  - `state_raw`: a_up_b_down
  - `breadth_a_raw`: 0.8
  - `breadth_b_raw`: 0.0
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
  - `state`: both_up
  - `interpretation`: Tightening transmits — rates up + credit widens.
  - `slot_a_label`: Credit stress
  - `slot_b_label`: Policy tightening
  - `breadth_a`: 1.0
  - `breadth_b`: 0.833
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
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
  - `breadth_b_raw`: 0.8
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
> Policy dilemma — labor market е loose, но инфлацията remains hot. Fed е заклещен между двата мандата. Най-отклонена леща: Инфлация и цени — breadth 88% (разширяване), 2 аномалии, 1 нови екстремума. Expectations също нагоре — de-anchoring в ход, рискът ескалира. За наблюдение следващия релиз: US_PMI_COMPOSITE, US_PMI_SVCS, LABOR_SHARE_NBS (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: US_PMI_COMPOSITE z=+2.60 · NEW-5Y-MAX
- 4 нови екстремуми в top-6 (lookback 5г.)
- Активни двойки: Stagflation test=a_down_b_up; Inflation anchoring=both_up; Credit × Policy=both_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-11-23 00:00:00 · **Generated:** 2026-11-23 21:10:31.025797+00:00

**Режим:** `policy_dilemma` (Policy dilemma)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 38.3 | mixed | 42.9% | 1 | 1 |
| **growth** | 44.7 | mixed | 25.0% | 1 | 0 |
| **inflation** | 38.3 | mixed | 42.9% | 2 | 0 |
| **credit** | 38.3 | mixed | 36.8% | 4 | 2 |
| **external** | 64.1 | expanding | 62.5% | 1 | 0 |

### Top anomalies (8 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | +5.21 | up | 3.39 | 2026-10-01 | - |
| **EA_OAT_BUND_SPREAD** | OAT-Bund spread (FR-DE 10Y, pp) | credit | sovereign_spreads | +5.17 | up | 1.47 | 2026-10-01 | ✓ max |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | +2.70 | up | 4.89 | 2026-10-01 | ✓ max |
| **EA_TRADE_BALANCE** | Търговски баланс (стоки, извън-ЕА, M€, SCA) | external | external_balance | -2.32 | down | -8677.60 | 2026-09-01 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation, growth | sentiment | +2.28 | up | 24.80 | 2026-10-01 | - |
| **EA_HICP_ENERGY** | HICP енергия, YoY | inflation | headline_measures | +2.19 | up | 21.00 | 2026-10-01 | - |
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
  - `breadth_b`: 1.0
  - `state_raw`: insufficient_data
  - `breadth_a_raw`: None
  - `breadth_b_raw`: 1.0
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
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.333
  - `breadth_b_raw`: 0.75
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
  - `breadth_a_raw`: 0.75
  - `breadth_b_raw`: 0.5

### Executive narrative
> Policy dilemma — labor market е loose, но инфлацията remains hot. ЕЦБ е заклещена между инфлацията и растежа. Най-отклонена леща: Инфлация и цени — breadth 100% (разширяване), 2 аномалии, 0 нови екстремума. За наблюдение следващия релиз: EA_OAT_BUND_SPREAD, FR_10Y (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.21
- 3 нови екстремуми в top-8 (lookback 5г.)
- Активни двойки: Stagflation test=a_down_b_up; Sentiment × Hard=both_down; Growth × Labor=both_down



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-11-26 00:00:00 · **Generated:** NaT

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 31.8 | contracting | -% | - | - |
| **inflation** | 46.6 | mixed | -% | - | - |
| **labor** | 51.6 | mixed | -% | - | - |
| **credit** | 48.3 | mixed | -% | - | - |
| **property** | 17.5 | contracting | -% | - | - |

### Top anomalies (4 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | -2.53 | down | 3.00 | 2026-11-20 | ✓ min |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | +2.23 | up | 15.79 | 2025-12-31 | ✓ max |
| **CN_GDP_DEFLATOR_Q** | БВП дефлатор (тримесечен, YoY %) | inflation | deflator_quarterly | +2.15 | up | 1.50 | 2026-09-30 | - |
| **CN_RE_INVEST_YOY** | Инвестиции в имоти — натрупани от началото на годината (YoY %) | property | investment | -2.07 | down | -21.60 | 2026-10-01 | ✓ min |

### Narrative hints от макро лещите
- **CN_LPR_1Y**: Замества benchmark lending rate от 2019. Главен policy signal.
- **CN_YOUTH_UNEMPLOYMENT**: Рекорд 21.3% юни 2023. НБС спря публикуването за 6 месеца. Структурен проблем — образователна система произвежда повече дипломирани, отколкото пазарът може да абсорбира.
- **CN_GDP_DEFLATOR_Q**: Имплицитен дефлатор = номинален YoY − реален YoY (от НБС тримесечни данни). Отрицателен 12 поредни тримесечия (2Q2023–1Q2026) → debt-deflation. Ключов falsifier сигнал за recessionary режима.
- **CN_RE_INVEST_YOY**: НБС (чрез chinadata.live). ВНИМАНИЕ: това е темп от началото на годината (YTD), не месечен; през годината се изглажда и се нулира всеки януари/февруари. Дълбок и устойчив спад.

### Cross-lens divergences (3 entries)
- 🔔 **?**
  - `pair_id`: credit_real_economy
  - `name_bg`: Кредитна експанзия × Реален сектор
  - `question_bg`: Превръща ли се кредитът в реална инвестиция, или ликвидността засяда (debt-deflation)?
  - `state`: transition
  - `interpretation`: Преход — кредит и реален сектор не са ясно aligned; чакай следващ TSF/FAI print.
  - `slot_a_label`: Кредитна експанзия
  - `slot_b_label`: Имоти и инвестиции
  - `breadth_a`: 0.25
  - `breadth_b`: 0.417
- 🔔 **?**
  - `pair_id`: monetary_inflation_trap
  - `name_bg`: Монетарно разхлабване × Инфлация
  - `question_bg`: Води ли разхлабването на PBoC до инфлация, или политиката бута в дефлация (policy trap)?
  - `state`: a_up_b_down
  - `interpretation`: Policy trap — PBoC разхлабва, но инфлацията пада/е в дефлация. Трансмисията е счупена (Japan-style): по-ниските лихви не вдигат цените при deleveraging.
  - `slot_a_label`: Монетарно разхлабване
  - `slot_b_label`: Инфлация
  - `breadth_a`: 0.667
  - `breadth_b`: 0.0
- 🔔 **?**
  - `pair_id`: external_domestic_balance
  - `name_bg`: Външно търсене × Вътрешна активност
  - `question_bg`: Балансиран ли е растежът, или Китай зависи от износа при слабо вътрешно търсене?
  - `state`: insufficient_data
  - `interpretation`: Insufficient data в една от двете групи.
  - `slot_a_label`: Външно търсене
  - `slot_b_label`: Вътрешна активност
  - `breadth_a`: None
  - `breadth_b`: 0.0

### Executive narrative
> Претеглен композитен macro score 42.4/100 → режим „ВЛОШАВАЩ СЕ“ (6/6 лещи). 6 лещи, 4 flagged аномалии, 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-11-20 |
| `as_of` | 2026-11-20 |
| `regime` | REFLATION |
| `alignment_score` | 2.0 |
| `gms_score` | 0.0 |
| `gms_max` | 8 |
| `gms_tier` | LOW |
| `ks_status` | active |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-11-20 → 2026-11-25)

**stable_winner (1m):** +8 entered, -8 exited
  - **Entered:** EQIX, GEV, IBKR, INTC, NUE, STT, TGT, WSM _(включително 2 за първи път в историята: INTC, WSM)_
  - **Exited:** DAL, GL, HAS, HLT, KEY, PSX, RL, TPR

**stable_winner (3m):** +5 entered, -5 exited
  - **Entered:** AEP, ETR, INTC, PNC, WSM _(включително 2 за първи път в историята: INTC, WSM)_
  - **Exited:** AIZ, GL, HAS, KO, PFG

**quality_dip (1m):** +8 entered, -6 exited
  - **Entered:** D, DAL, GL, HLT, KEY, PSX, RL, TPR _(включително 2 за първи път в историята: D, PSX)_
  - **Exited:** EQIX, GEV, IBKR, NUE, STT, TGT

**quality_dip (3m):** +5 entered, -3 exited
  - **Entered:** AIZ, D, GL, KO, PFG _(включително 2 за първи път в историята: D, KO)_
  - **Exited:** AEP, ETR, PNC

**faded_bounce (1m):** +6 entered, -6 exited
  - **Entered:** CPRT, ISRG, KR, PNR, SPGI, VICI _(включително 3 за първи път в историята: KR, PNR, VICI)_
  - **Exited:** CSGP, EXE, LII, PSKY, SHW, TAP

**faded_bounce (3m):** +5 entered, -5 exited
  - **Entered:** AXON, BX, CSGP, KR, VICI _(включително 2 за първи път в историята: KR, VICI)_
  - **Exited:** CMG, COIN, EQT, IP, SHW

### EU (period: 2026-11-20 → 2026-11-26)

**stable_winner (1m):** +7 entered, -7 exited
  - **Entered:** AAL.L, BG.VI, CAST.ST, FRO.OL, INDU-C.ST, MBK.WA, TELIA.ST _(включително 1 за първи път в историята: CAST.ST)_
  - **Exited:** ABI.BR, BCP.LS, BGEO.L, SSAB-B.ST, TIT.MI, VACN.SW, ZEG.L

**stable_winner (3m):** +8 entered, -10 exited
  - **Entered:** BEZ.L, CAST.ST, DANSKE.CO, FORTUM.HE, FRO.OL, GLEN.L, INDU-C.ST, JYSK.CO _(включително 1 за първи път в историята: CAST.ST)_
  - **Exited:** ABN.AS, ASML.AS, BAYN.DE, BCP.LS, ELE.MC, INGA.AS, SSAB-B.ST, TIT.MI, UNI.MI, VOD.L

**quality_dip (1m):** +7 entered, -9 exited
  - **Entered:** ABI.BR, BCP.LS, BGEO.L, SSAB-B.ST, TIT.MI, VACN.SW, ZEG.L _(включително 1 за първи път в историята: SSAB-B.ST)_
  - **Exited:** AAL.L, BG.VI, FRO.OL, HM-B.ST, INDU-C.ST, MBK.WA, MRL.MC, RIO.L, TELIA.ST

**quality_dip (3m):** +10 entered, -10 exited
  - **Entered:** ABN.AS, ASML.AS, BAYN.DE, BCP.LS, ELE.MC, INGA.AS, SSAB-B.ST, TIT.MI, UNI.MI, VOD.L _(включително 3 за първи път в историята: BAYN.DE, ELE.MC, SSAB-B.ST)_
  - **Exited:** BEZ.L, DANSKE.CO, FORTUM.HE, FRO.OL, GLEN.L, HM-B.ST, INDU-C.ST, JYSK.CO, MRL.MC, RIO.L

**faded_bounce (1m):** +12 entered, -11 exited
  - **Entered:** BALD-B.ST, BEIJ-B.ST, BKW.SW, BWY.L, BZU.MI, COLO-B.CO, EQT.ST, III.L, LATO-B.ST, LISP.SW, SWEC-B.ST, UTG.L _(включително 2 за първи път в историята: BZU.MI, COLO-B.CO)_
  - **Exited:** ADYEN.AS, BME.L, DSY.PA, EVD.DE, EZJ.L, MRO.L, NEM.DE, SGO.PA, STJ.L, TOM.OL, VNA.DE

**faded_bounce (3m):** +10 entered, -4 exited
  - **Entered:** BOL.PA, CMBN.SW, EQT.ST, III.L, JMT.LS, PGHN.SW, RHM.DE, RNO.PA, SWEC-B.ST, TRYG.CO _(включително 1 за първи път в историята: RHM.DE)_
  - **Exited:** ADYEN.AS, BWY.L, EZJ.L, MNDI.L



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-11-17 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **soymeal** | Commodities | 86283 | 90.2 | 90.2 | 1067 | -118410 |
| **rbob** | Commodities | 79636 | 87.3 | 87.3 | 1067 | -13955 |
| **sugar** | Commodities | 181463 | 85.0 | 85.0 | 1067 | -87545 |
| **bitcoin** | Crypto | -1211 | 76.7 | 76.7 | 450 | 3731 |
| **copper** | Commodities | 27347 | 72.9 | 72.9 | 1067 | -20662 |
| **aud** | FX | 37980 | 71.9 | 71.9 | 1067 | -14517 |
| **gbpfx** | FX | 28790 | 69.5 | 69.5 | 1067 | 4686 |
| **cotton** | Commodities | 48998 | 68.1 | 68.1 | 1067 | -17468 |
| **sp500** | US Equities | -234978 | 67.2 | 67.2 | 1067 | 136267 |
| **soybeans** | Commodities | 99698 | 61.6 | 61.6 | 1067 | -107238 |
| **jpy** | FX | -23790 | 53.8 | 53.8 | 1067 | -900 |
| **russell** | US Equities | -42353 | 52.4 | 52.4 | 603 | 10682 |
| **dxy** | FX | -1251 | 51.4 | 51.4 | 1067 | -4434 |
| **nasdaq** | US Equities | -10928 | 45.5 | 45.5 | 1067 | -11878 |
| **coffee** | Commodities | 6767 | 43.9 | 43.9 | 1067 | -9580 |
| **gold** | Commodities | 104270 | 42.2 | 42.2 | 1067 | -4415 |
| **brent** | Commodities | 3091 | 38.0 | 38.0 | 250 | 1932 |
| **soyoil** | Commodities | 4024 | 38.0 | 38.0 | 1067 | -65834 |
| **cattle** | Commodities | 43321 | 37.9 | 37.9 | 1067 | -7822 |
| **us30y** | Rates | -145229 | 36.5 | 36.5 | 1067 | 17528 |
| **heatingoil** | Commodities | 4453 | 32.8 | 32.8 | 1067 | -8868 |
| **vix** | Volatility | -72916 | 32.3 | 32.3 | 1026 | -52026 |
| **corn** | Commodities | -71080 | 24.7 | 24.7 | 1067 | -217337 |
| **eurfx** | FX | -76587 | 21.5 | 21.5 | 1067 | -7747 |
| **us2y** | Rates | -1288895 | 18.0 | 18.0 | 1067 | -3347 |
| **platinum** | Commodities | -675 | 14.4 | 14.4 | 1067 | -7290 |
| **wheat** | Commodities | -83763 | 13.6 | 13.6 | 1067 | -32629 |
| **us5y** | Rates | -2224698 | 10.8 | 10.8 | 1067 | -107154 |
| **silver** | Commodities | 17 | 10.2 | 10.2 | 1067 | -3729 |
| **usultra10y** | Rates | -343870 | 9.5 | 9.5 | 557 | -25393 |
| **chf** | FX | -19763 | 8.2 | 8.2 | 1067 | -6156 |
| **wti** | Commodities | 60819 | 8.2 | 8.2 | 1067 | -41087 |
| **cocoa** | Commodities | -20268 | 7.8 | 7.8 | 1067 | -9414 |
| **cad** | FX | -72118 | 6.1 | 6.1 | 1067 | 18995 |
| **natgas** | Commodities | -211476 | 3.1 | 3.1 | 1067 | -54628 |
| **palladium** | Commodities | -14816 | 0.9 | 0.9 | 1067 | -2673 |
| **us10y** | Rates | -2482443 | 0.3 | 0.3 | 1067 | -375219 |
| **hogs** | Commodities | -52250 | 0.1 | 0.1 | 1067 | -11117 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **MRNA** | Healthcare | 97.0 | 6.2% | 54.7% | 364.2% | 761.2% | 1.66 | -34.2% |
| 2 | **OKTA** | Technology | 90.5 | -10.8% | 16.7% | 113.0% | 185.6% | 1.29 | -33.1% |
| 3 | **CRL** | Healthcare | 88.0 | -7.5% | 12.0% | 83.1% | 110.5% | 1.30 | -33.9% |
| 4 | **VTRS** | Healthcare | 83.6 | 6.6% | 18.1% | 24.8% | 81.3% | 2.01 | -19.0% |
| 5 | **RVTY** | Healthcare | 83.5 | -6.8% | 16.3% | 49.0% | 61.1% | 0.90 | -30.1% |
| 6 | **TGT** | Consumer Defensive | 82.2 | 17.2% | 4.5% | 35.8% | 79.9% | 2.25 | -13.3% |
| 7 | **BDX** | Healthcare | 81.3 | 13.4% | 18.3% | 51.0% | 33.2% | 1.40 | -23.1% |
| 8 | **APA** | Energy | 81.0 | -10.4% | 7.9% | 26.0% | 114.0% | 1.35 | -27.7% |
| 9 | **SWK** | Industrials | 80.7 | 10.0% | 11.0% | 40.5% | 54.2% | 1.27 | -26.1% |
| 10 | **PSX** | Energy | 80.5 | -11.6% | -1.1% | 35.0% | 105.8% | 1.66 | -20.2% |
| 11 | **BBY** | Consumer Cyclical | 80.3 | 4.1% | 24.1% | 40.5% | 37.2% | 0.79 | -32.0% |
| 12 | **HAS** | Consumer Cyclical | 80.2 | -6.0% | 18.1% | 30.8% | 52.5% | 0.98 | -27.3% |
| 13 | **MPC** | Energy | 80.1 | -20.4% | -4.5% | 38.5% | 131.9% | 1.50 | -28.4% |
| 14 | **BIIB** | Healthcare | 79.2 | 3.5% | 18.0% | 33.1% | 42.9% | 1.01 | -14.3% |
| 15 | **HUM** | Healthcare | 79.1 | -1.8% | 3.8% | 32.3% | 83.0% | 1.10 | -44.3% |
| 16 | **PANW** | Technology | 78.8 | -11.3% | -7.0% | 38.2% | 118.5% | 1.19 | -36.0% |
| 17 | **TRV** | Financial Services | 78.7 | 2.5% | 10.5% | 39.3% | 38.6% | 1.47 | -9.9% |
| 18 | **VLO** | Energy | 78.2 | -16.3% | -6.5% | 32.9% | 125.4% | 1.50 | -29.5% |
| 19 | **GILD** | Healthcare | 78.1 | 11.1% | 19.4% | 31.3% | 30.1% | 1.18 | -21.6% |
| 20 | **AMGN** | Healthcare | 77.5 | 5.4% | 8.0% | 41.1% | 36.7% | 1.09 | -16.6% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **GMAB.CO** | Healthcare | 94.7 | 0.1% | 82.4% | 150.6% | 97.7% | 1.46 | -32.3% |
| 2 | **ALE.WA** | Consumer Cyclical | 94.3 | 12.0% | 45.2% | 91.7% | 89.5% | 2.37 | -26.5% |
| 3 | **BME.L** | Consumer Cyclical | 90.9 | 26.8% | 45.8% | 103.2% | 59.9% | 1.52 | -19.8% |
| 4 | **BFT.WA** | Industrials | 90.3 | 11.8% | 24.0% | 54.8% | 91.0% | 2.56 | -17.4% |
| 5 | **ORNBV.HE** | Healthcare | 88.2 | 6.2% | 30.2% | 52.8% | 63.5% | 1.72 | -16.8% |
| 6 | **TECN.SW** | Healthcare | 87.8 | -2.2% | 22.2% | 51.5% | 84.2% | 1.40 | -28.4% |
| 7 | **LPP.WA** | Consumer Cyclical | 86.5 | 4.3% | 35.2% | 31.9% | 71.5% | 1.56 | -24.2% |
| 8 | **FRO.OL** | Energy | 86.2 | -8.9% | 14.9% | 46.1% | 106.5% | 1.40 | -26.2% |
| 9 | **SOON.SW** | Healthcare | 84.1 | 2.7% | 25.2% | 46.2% | 47.6% | 1.48 | -27.1% |
| 10 | **DSFIR.AS** | Basic Materials | 82.8 | 1.4% | 12.0% | 57.2% | 56.7% | 1.39 | -27.0% |
| 11 | **BPT.L** | Financial Services | 81.8 | 1.7% | 25.0% | 51.4% | 40.0% | 0.79 | -28.4% |
| 12 | **ERF.PA** | Healthcare | 81.5 | 0.0% | 18.9% | 39.6% | 48.0% | 1.32 | -20.4% |
| 13 | **LOTB.BR** | Consumer Defensive | 81.5 | 5.2% | 10.2% | 28.1% | 77.0% | 2.50 | -11.9% |
| 14 | **DEMANT.CO** | Healthcare | 81.0 | -9.6% | 13.7% | 31.4% | 70.2% | 1.17 | -25.4% |
| 15 | **MOH.AT** | Energy | 80.7 | -17.8% | -8.3% | 57.1% | 156.4% | 2.11 | -20.0% |
| 16 | **SIGN.SW** | Basic Materials | 80.2 | 6.9% | 14.8% | 33.7% | 55.1% | 1.23 | -18.1% |
| 17 | **OCTV-SDB.ST** | Technology | 80.0 | 2.4% | 18.4% | 37.2% | -% | 1.38 | -20.5% |
| 18 | **SDZ.SW** | Healthcare | 79.7 | 1.6% | 19.5% | 29.0% | 45.4% | 1.23 | -17.6% |
| 19 | **BAYN.DE** | Healthcare | 79.4 | 12.8% | 5.9% | 49.6% | 50.8% | 1.25 | -30.6% |
| 20 | **MBK.WA** | Financial Services | 78.6 | 8.7% | 19.2% | 28.3% | 44.3% | 1.21 | -14.8% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **SNDK** | Information Technology | 2.098 | 1.686 | 1.664 | 1.956 | -0.147 | - | 4.7 | +141.2% |
| 2 | **EIX** | Utilities | 1.644 | 0.271 | 0.896 | 2.890 | -0.883 | - | 6.7 | +18.8% |
| 3 | **MO** | Consumer Staples | 1.572 | 1.207 | 1.846 | 0.851 | -0.021 | - | 15.7 | - |
| 4 | **CF** | Materials | 1.535 | 1.212 | 1.283 | 1.380 | 0.517 | - | 8.3 | +30.9% |
| 5 | **HST** | Real Estate | 1.448 | 2.238 | 0.326 | 1.345 | -0.283 | - | 18.4 | +14.2% |
| 6 | **MU** | Information Technology | 1.373 | 1.552 | 1.156 | 0.825 | -0.410 | - | 8.1 | +88.3% |
| 7 | **NEM** | Materials | 1.368 | 0.444 | 1.795 | 1.055 | 0.463 | - | 11.8 | +27.3% |
| 8 | **APA** | Energy | 1.155 | 1.088 | 1.157 | 0.680 | 0.197 | - | 7.4 | +33.3% |
| 9 | **DVA** | Health Care | 1.140 | 1.032 | 0.191 | 1.762 | -1.344 | - | 12.3 | +96.8% |
| 10 | **HAS** | Consumer Discretionary | 1.087 | 1.747 | 0.937 | 0.186 | 0.087 | - | 16.5 | +139.8% |
| 11 | **SYF** | Financials | 1.072 | -0.467 | 1.172 | 1.790 | -0.155 | - | 7.2 | +19.8% |
| 12 | **VLO** | Energy | 1.047 | 1.163 | 0.328 | 1.266 | -0.494 | - | 7.3 | +46.9% |
| 13 | **SPG** | Real Estate | 1.044 | 0.889 | 1.360 | 0.347 | -1.421 | - | 16.9 | +125.2% |
| 14 | **WDC** | Information Technology | 1.020 | 1.129 | 0.876 | 0.616 | -0.670 | - | 9.6 | +129.6% |
| 15 | **MPC** | Energy | 1.019 | 1.205 | 0.317 | 1.171 | -1.060 | - | 6.9 | +60.5% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -2.170 | -1.452 | -1.366 | -2.637 | -1.312 |
| 502 | **BA** | Industrials | -1.696 | -0.852 | -2.146 | -1.104 | -1.084 |
| 501 | **TSLA** | Consumer Discretionary | -1.688 | -0.199 | -1.308 | -2.577 | -0.439 |
| 500 | **ARES** | Financials | -1.681 | -1.439 | -1.379 | -1.415 | -1.206 |
| 499 | **BLDR** | Industrials | -1.570 | -2.365 | -1.297 | -0.431 | -1.042 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W48.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W48.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\macro\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-11-23  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
