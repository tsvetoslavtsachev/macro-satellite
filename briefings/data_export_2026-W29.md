# Сателит — пълен data export за 2026-W29

_Период: 2026-07-13 → 2026-07-19_  
_Генериран: 2026-07-17 08:11 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W29.md` (structured briefing) и `narrative_2026-W29.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**11 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **SOXX** | -8.75% | -1.93σ | 581.34 | 530.50 | 2026-07-10 | 2026-07-16 | +3.38% | +6.27% | 13 |
| **XLK** | -4.45% | -1.59σ | 185.78 | 177.52 | 2026-07-10 | 2026-07-16 | +2.14% | +4.14% | 13 |
| **XLI** | -0.97% | -1.42σ | 181.92 | 180.15 | 2026-07-10 | 2026-07-16 | +0.46% | +1.01% | 13 |
| **URA** | -8.98% | -1.41σ | 42.97 | 39.11 | 2026-07-10 | 2026-07-16 | -1.14% | +5.58% | 13 |
| **USO** | +9.75% | +1.38σ | 108.70 | 119.30 | 2026-07-10 | 2026-07-16 | -0.77% | +7.65% | 13 |
| **QQQ** | -2.70% | -1.34σ | 725.51 | 705.94 | 2026-07-10 | 2026-07-16 | +1.38% | +3.03% | 13 |
| **XLP** | +2.01% | +1.25σ | 84.12 | 85.81 | 2026-07-10 | 2026-07-16 | +0.17% | +1.47% | 13 |
| **EEM** | -4.05% | -1.24σ | 66.90 | 64.19 | 2026-07-10 | 2026-07-16 | +0.85% | +3.94% | 13 |
| **DBC** | +3.42% | +1.24σ | 27.52 | 28.46 | 2026-07-10 | 2026-07-16 | -0.23% | +2.94% | 13 |
| **VNQ** | +2.83% | +1.14σ | 97.32 | 100.07 | 2026-07-10 | 2026-07-16 | +0.37% | +2.15% | 13 |
| **DFEN** | -10.14% | -1.07σ | 76.07 | 68.36 | 2026-07-10 | 2026-07-16 | +0.92% | +10.33% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-07-19 · **Conditions matched:** 4/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | +9.75% | ✅ | 108.70 | 119.30 | 2026-07-10 | 2026-07-16 |
| DFEN | down ≥ 3.0% | -10.14% | ✅ | 76.07 | 68.36 | 2026-07-10 | 2026-07-16 |
| GLD | down ≥ 1.0% | -3.20% | ✅ | 377.01 | 364.96 | 2026-07-10 | 2026-07-16 |
| URA | down ≥ 3.0% | -8.98% | ✅ | 42.97 | 39.11 | 2026-07-10 | 2026-07-16 |
| UUP | up ≥ 0.5% | -0.18% | ❌ | 28.39 | 28.34 | 2026-07-10 | 2026-07-16 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — не активен
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-07-19 · **Conditions matched:** 2/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | -0.14% | ❌ | 295.99 | 295.59 | 2026-07-10 | 2026-07-16 |
| XLF | up ≥ 1.0% | +1.87% | ✅ | 55.71 | 56.75 | 2026-07-10 | 2026-07-16 |
| XLY | up ≥ 1.0% | +0.09% | ❌ | 117.24 | 117.34 | 2026-07-10 | 2026-07-16 |
| GLD | down ≥ 0.5% | -3.20% | ✅ | 377.01 | 364.96 | 2026-07-10 | 2026-07-16 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2026-W05 (week ending 2026-02-01)
**Cosine similarity:** 0.9225 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.68% | +4.14% | +8.49% |
| **USO** | +13.43% | +79.58% | +50.03% |
| **GLD** | +5.21% | -4.89% | -17.98% |
| **TLT** | +2.64% | -1.74% | -3.35% |
| **XLE** | +10.71% | +15.28% | +11.69% |
| **IWM** | -0.16% | +7.56% | +13.84% |

### Паралел #2: 2023-W37 (week ending 2023-09-17)
**Cosine similarity:** 0.8504 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.66% | +5.86% | +14.99% |
| **USO** | -3.06% | -17.39% | -6.10% |
| **GLD** | -0.03% | +4.86% | +11.98% |
| **TLT** | -8.29% | +6.66% | -0.02% |
| **XLE** | -0.96% | -8.38% | -0.49% |
| **IWM** | -4.72% | +7.31% | +10.24% |

### Паралел #3: 2021-W37 (week ending 2021-09-19)
**Cosine similarity:** 0.8469 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.09% | +4.18% | +0.71% |
| **USO** | +14.11% | +0.91% | +48.33% |
| **GLD** | +1.03% | +2.46% | +9.48% |
| **TLT** | -3.67% | +1.11% | -10.55% |
| **XLE** | +17.64% | +10.24% | +49.80% |
| **IWM** | +1.52% | -3.30% | -6.84% |

### Паралел #4: 2026-W10 (week ending 2026-03-08)
**Cosine similarity:** 0.8415 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -1.96% | +9.69% | +11.65% |
| **USO** | +26.95% | +22.29% | +9.68% |
| **GLD** | -8.81% | -16.32% | -22.92% |
| **TLT** | -2.06% | -3.84% | -4.80% |
| **XLE** | +6.35% | +1.94% | +0.80% |
| **IWM** | +0.81% | +12.26% | +17.82% |

### Паралел #5: 2024-W07 (week ending 2024-02-18)
**Cosine similarity:** 0.8265 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +3.24% | +5.99% | +10.97% |
| **USO** | +6.84% | +4.85% | +3.96% |
| **GLD** | +7.22% | +20.03% | +24.50% |
| **TLT** | +0.17% | -1.48% | +5.05% |
| **XLE** | +7.72% | +10.97% | +5.73% |
| **IWM** | +0.22% | +3.18% | +5.42% |

### Паралел #6: 2025-W25 (week ending 2025-06-22)
**Cosine similarity:** 0.8255 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +5.82% | +11.68% | +14.52% |
| **USO** | -9.35% | -11.55% | -18.15% |
| **GLD** | +1.92% | +9.37% | +28.66% |
| **TLT** | +0.03% | +2.93% | +1.23% |
| **XLE** | -3.94% | -0.52% | -0.81% |
| **IWM** | +6.72% | +16.14% | +19.87% |

### Паралел #7: 2022-W51 (week ending 2022-12-25)
**Cosine similarity:** 0.8188 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.52% | +3.35% | +13.14% |
| **USO** | +1.30% | -12.06% | -9.95% |
| **GLD** | +7.78% | +9.80% | +6.54% |
| **TLT** | +4.95% | +4.59% | +1.15% |
| **XLE** | +3.66% | -10.53% | -11.14% |
| **IWM** | +7.19% | -1.49% | +3.54% |

### Паралел #8: 2025-W01 (week ending 2025-01-05)
**Cosine similarity:** 0.8125 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.66% | -14.64% | +5.64% |
| **USO** | -0.53% | -12.83% | -3.50% |
| **GLD** | +7.81% | +14.88% | +26.14% |
| **TLT** | +1.31% | +6.37% | -0.37% |
| **XLE** | +2.94% | -9.96% | -0.50% |
| **IWM** | +1.11% | -19.27% | -0.60% |

### Паралел #9: 2024-W25 (week ending 2024-06-23)
**Cosine similarity:** 0.8058 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +1.70% | +4.36% | +8.57% |
| **USO** | -2.58% | -7.29% | -7.06% |
| **GLD** | +3.63% | +12.77% | +12.72% |
| **TLT** | -1.53% | +5.24% | -6.01% |
| **XLE** | +0.65% | -1.10% | -6.25% |
| **IWM** | +11.12% | +10.59% | +10.77% |

### Паралел #10: 2026-W11 (week ending 2026-03-15)
**Cosine similarity:** 0.7980 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.86% | +12.00% | +13.35% |
| **USO** | +3.30% | +4.62% | -0.49% |
| **GLD** | -3.42% | -16.12% | -20.81% |
| **TLT** | +0.77% | -0.89% | -2.69% |
| **XLE** | -3.03% | -0.26% | -1.18% |
| **IWM** | +8.97% | +18.80% | +19.87% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 13 · **Total matching days:** 69 · **History:** 2021-05-17 → 2026-07-16

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 13 | +2.0% | +1.7% | -3.1% | +7.4% | 69% |
| **SPY** | 3m | 13 | +3.0% | +4.3% | -7.3% | +12.0% | 77% |
| **SPY** | 6m | 13 | +7.7% | +11.0% | -6.8% | +21.8% | 77% |
| **USO** | 1m | 13 | +0.4% | -0.8% | -14.3% | +12.7% | 46% |
| **USO** | 3m | 13 | -2.7% | -4.1% | -20.8% | +24.5% | 46% |
| **USO** | 6m | 13 | +10.5% | -1.9% | -20.8% | +109.4% | 46% |
| **GLD** | 1m | 13 | +2.6% | +0.9% | -0.9% | +8.9% | 77% |
| **GLD** | 3m | 13 | +5.5% | +5.9% | -12.6% | +24.5% | 69% |
| **GLD** | 6m | 13 | +5.6% | +10.3% | -17.9% | +25.3% | 69% |
| **TLT** | 1m | 13 | -1.3% | -1.1% | -6.7% | +3.6% | 38% |
| **TLT** | 3m | 13 | -0.3% | +0.3% | -16.5% | +11.1% | 54% |
| **TLT** | 6m | 13 | -4.0% | -2.4% | -18.0% | +7.5% | 31% |

**Episodes (последни 5 от 13):**
- `2024-06-21 → 2024-06-21` (1d)
- `2025-01-13 → 2025-01-13` (1d)
- `2025-11-17 → 2025-11-17` (1d)
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 50 · **History:** 2021-05-17 → 2026-07-16

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +4.5% | +4.5% | -0.1% | +9.1% | 50% |
| **SPY** | 3m | 2 | +5.1% | +5.1% | -0.1% | +10.3% | 50% |
| **SPY** | 6m | 2 | +5.5% | +5.5% | -0.1% | +11.1% | 50% |
| **USO** | 1m | 2 | +3.3% | +3.3% | -0.7% | +7.2% | 50% |
| **USO** | 3m | 2 | -5.3% | -5.3% | -9.9% | -0.7% | 0% |
| **USO** | 6m | 2 | -2.5% | -2.5% | -4.2% | -0.7% | 0% |
| **GLD** | 1m | 2 | -1.1% | -1.1% | -1.9% | -0.2% | 0% |
| **GLD** | 3m | 2 | -7.9% | -7.9% | -13.8% | -1.9% | 0% |
| **GLD** | 6m | 2 | -9.0% | -9.0% | -16.0% | -1.9% | 0% |
| **TLT** | 1m | 2 | -0.4% | -0.4% | -1.0% | +0.2% | 50% |
| **TLT** | 3m | 2 | -1.4% | -1.4% | -2.9% | +0.2% | 50% |
| **TLT** | 6m | 2 | -1.5% | -1.5% | -3.1% | +0.2% | 50% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-07-16` (3d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 400 · **History:** 2021-05-17 → 2026-07-16

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
- `2025-11-03 → 2026-07-16` (168d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-07-16

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 8 · **Total matching days:** 78 · **History:** 2021-05-17 → 2026-07-16

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 8 | -0.5% | -1.3% | -7.2% | +7.8% | 50% |
| **SPY** | 3m | 8 | +1.9% | +2.1% | -8.3% | +11.6% | 50% |
| **SPY** | 6m | 8 | +0.8% | +5.3% | -20.8% | +14.2% | 62% |
| **USO** | 1m | 8 | +4.0% | -1.5% | -15.0% | +52.9% | 38% |
| **USO** | 3m | 8 | +9.4% | +5.5% | -20.7% | +52.2% | 50% |
| **USO** | 6m | 8 | +9.0% | +2.2% | -27.6% | +45.8% | 50% |
| **GLD** | 1m | 8 | -2.5% | -1.9% | -8.3% | +1.9% | 12% |
| **GLD** | 3m | 8 | -1.5% | -1.3% | -12.0% | +6.4% | 50% |
| **GLD** | 6m | 8 | -1.3% | -2.7% | -22.0% | +25.0% | 38% |
| **TLT** | 1m | 8 | -2.1% | -2.7% | -6.0% | +2.5% | 12% |
| **TLT** | 3m | 8 | -6.9% | -6.1% | -17.6% | +4.2% | 25% |
| **TLT** | 6m | 8 | -11.0% | -9.2% | -22.3% | +1.2% | 12% |

**Episodes (последни 5 от 8):**
- `2022-06-07 → 2022-06-09` (3d)
- `2023-04-12 → 2023-04-18` (5d)
- `2023-07-26 → 2023-08-01` (3d)
- `2025-06-13 → 2025-06-20` (5d)
- `2026-03-03 → 2026-05-19` (36d)

### `gold_flight` — Flight to gold (GLD 4w > +5%)
_Сериозен gold rally — често risk-off или real-rates compression сигнал._  
**Episodes:** 16 · **Total matching days:** 275 · **History:** 2021-05-17 → 2026-07-16

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.1% | +1.9% | -4.8% | +9.0% | 75% |
| **SPY** | 3m | 16 | +3.4% | +5.1% | -12.6% | +16.2% | 75% |
| **SPY** | 6m | 16 | +6.8% | +7.6% | -14.0% | +21.0% | 81% |
| **USO** | 1m | 16 | +1.3% | -3.2% | -13.0% | +22.9% | 38% |
| **USO** | 3m | 16 | +1.7% | -2.1% | -14.5% | +29.9% | 31% |
| **USO** | 6m | 16 | +11.4% | +1.8% | -12.4% | +87.1% | 62% |
| **GLD** | 1m | 16 | +2.5% | +1.8% | -5.6% | +9.0% | 75% |
| **GLD** | 3m | 16 | +6.2% | +7.4% | -17.4% | +23.6% | 69% |
| **GLD** | 6m | 16 | +10.9% | +12.1% | -17.4% | +43.8% | 75% |
| **TLT** | 1m | 16 | +0.4% | +0.3% | -6.3% | +8.2% | 50% |
| **TLT** | 3m | 16 | -1.5% | -1.4% | -15.3% | +11.9% | 38% |
| **TLT** | 6m | 16 | -4.5% | -2.5% | -21.3% | +7.0% | 38% |

**Episodes (последни 5 от 16):**
- `2025-03-27 → 2025-05-08` (25d)
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 19 · **Total matching days:** 288 · **History:** 2021-05-17 → 2026-07-16

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 19 | +0.4% | +1.0% | -8.7% | +7.0% | 53% |
| **SPY** | 3m | 19 | +2.0% | +2.7% | -13.7% | +9.1% | 68% |
| **SPY** | 6m | 19 | +3.1% | +6.8% | -16.4% | +16.9% | 74% |
| **USO** | 1m | 19 | -0.6% | -5.6% | -21.8% | +55.8% | 42% |
| **USO** | 3m | 19 | +3.0% | -1.3% | -12.7% | +64.3% | 42% |
| **USO** | 6m | 19 | +7.4% | -5.2% | -16.0% | +75.1% | 47% |
| **GLD** | 1m | 19 | -0.6% | -0.1% | -12.4% | +7.6% | 47% |
| **GLD** | 3m | 19 | +1.3% | +1.3% | -13.7% | +19.0% | 63% |
| **GLD** | 6m | 19 | +7.0% | +6.0% | -22.9% | +55.5% | 68% |
| **TLT** | 1m | 19 | -0.2% | -0.1% | -5.6% | +5.2% | 47% |
| **TLT** | 3m | 19 | -3.5% | -4.4% | -17.3% | +8.7% | 32% |
| **TLT** | 6m | 19 | -6.7% | -6.3% | -21.4% | +4.6% | 21% |

**Episodes (последни 5 от 19):**
- `2025-05-12 → 2025-05-19` (3d)
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (13d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-07-16

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|



---

## 5. Persistent макро аномалии (US + EU + CN)

_Серии, появили се в top_anomalies на macro_state в няколко поредни snapshots. Сегашната history е малка (~2 weeks); pers signal става информативен с time._

### US (12 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | 5 | 2.89 | 2.89 | 2026-06-13 00:00:00 | 2026-07-11 00:00:00 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | 5 | 2.58 | 2.58 | 2026-06-13 00:00:00 | 2026-07-11 00:00:00 | - |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | 5 | 2.37 | 2.43 | 2026-06-13 00:00:00 | 2026-07-11 00:00:00 | - |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor | labor_share | 5 | 2.34 | 2.34 | 2026-06-13 00:00:00 | 2026-07-11 00:00:00 | ✓ |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | 5 | 2.28 | 2.28 | 2026-06-13 00:00:00 | 2026-07-11 00:00:00 | ✓ |
| **JTSQUR** | Quits rate — напускания | labor | flow | 5 | 2.02 | 2.02 | 2026-06-13 00:00:00 | 2026-07-11 00:00:00 | ✓ |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | 3 | 2.63 | 2.76 | 2026-06-13 00:00:00 | 2026-07-11 00:00:00 | ✓ |
| **CSUSHPISA** | Case-Shiller US National HPI (SA) | housing | housing_prices | 3 | 2.20 | 2.26 | 2026-06-13 00:00:00 | 2026-07-11 00:00:00 | - |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | 2 | 2.47 | 2.47 | 2026-07-04 00:00:00 | 2026-07-11 00:00:00 | ✓ |
| **PSAVERT** | Personal Savings Rate | growth | consumer_sentiment | 2 | 2.40 | 2.40 | 2026-06-13 00:00:00 | 2026-06-20 00:00:00 | - |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | 2 | 2.02 | 2.02 | 2026-07-04 00:00:00 | 2026-07-11 00:00:00 | - |
| **MSACSR** | Месеци предлагане — нови жилища | housing | housing_affordability | 1 | 2.02 | 2.02 | 2026-06-27 00:00:00 | 2026-06-27 00:00:00 | ✓ |

### EU (5 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | 5 | 5.33 | 5.37 | 2026-06-13 00:00:00 | 2026-07-11 00:00:00 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation | sentiment | 5 | 2.65 | 2.98 | 2026-06-13 00:00:00 | 2026-07-11 00:00:00 | - |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | 5 | 2.45 | 2.66 | 2026-06-13 00:00:00 | 2026-07-11 00:00:00 | - |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | 5 | 2.25 | 2.27 | 2026-06-13 00:00:00 | 2026-07-11 00:00:00 | ✓ |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | 5 | 2.23 | 2.25 | 2026-06-13 00:00:00 | 2026-07-11 00:00:00 | ✓ |

### CN (3 серии)

| Series ID | Name BG | Lens | Peer group | Occurrences | Mean \|z\| | Max \|z\| | First date | Last date | NEW-EXTREME |
|---|---|---|---|---:|---:|---:|---|---|:---:|
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 7 | 2.56 | 2.56 | 2026-06-15 00:00:00 | 2026-07-13 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 7 | 2.23 | 2.23 | 2026-06-15 00:00:00 | 2026-07-13 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 3 | 2.23 | 2.24 | 2026-06-15 00:00:00 | 2026-07-08 00:00:00 | - |



---

## 6. US Macro State — пълен snapshot

**Дата:** 2026-07-11 00:00:00 · **Generated:** 2026-07-11 08:50:34.045938+00:00

**Режим:** `stagflation_confirmed` (Стагфлация (потвърдена))  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 35.7 | contracting | 29.6% | 4 | 3 |
| **growth** | 41.5 | mixed | 28.0% | 1 | 1 |
| **inflation** | 36.4 | contracting | 27.8% | 4 | 1 |
| **liquidity** | 52.0 | mixed | 42.1% | 0 | 0 |

### Top anomalies (10 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **PPIFIS** | PPI — Final Demand (производствени цени) | inflation | headline_measures | +2.89 | up | 6.42 | 2026-05-01 | - |
| **CPI_GOODS** | CPI — стоки (commodities) | inflation | goods_services | +2.58 | up | 5.29 | 2026-05-01 | - |
| **HPIPONM226S** | FHFA HPI — Monthly Purchase-Only (SA) | housing | housing_prices | -2.56 | down | 2.00 | 2026-04-01 | - |
| **CIVPART** | Коефициент на участие (LFPR) | labor | unemployment | -2.47 | down | 61.50 | 2026-06-01 | ✓ min |
| **MICH_INFL_1Y** | Инфлационни очаквания (Michigan, 1 година) | inflation | expectations | +2.43 | up | 4.80 | 2026-05-01 | - |
| **LABOR_SHARE_NBS** | Labor share — нефермерски бизнес | labor, inflation | labor_share | -2.34 | down | 94.99 | 2026-01-01 | ✓ min |
| **US_PMI_MFG** | S&P Global US Manufacturing PMI | growth | diffusion_indices | +2.28 | up | 55.10 | 2026-05-01 | ✓ max |
| **CSUSHPISA** | Case-Shiller US National HPI (SA) | housing | housing_prices | -2.17 | down | 0.84 | 2026-04-01 | - |
| **EMRATIO** | Заетост/население (prime-age proxy) | labor | unemployment | -2.02 | down | 59.00 | 2026-06-01 | - |
| **JTSQUR** | Quits rate — напускания | labor | flow | -2.02 | down | 1.90 | 2026-05-01 | ✓ min |

### Narrative hints от макро лещите
- **PPIFIS**: Производствени цени → consumer prices с 1-3 месечен lag. Водещ за CPI при трендови промени.
- **CPI_GOODS**: Goods inflation реагира бързо на supply shocks. 2022 peak след доставъчните кризи. Сега често е в deflation/близо до 0.
- **HPIPONM226S**: Monthly FHFA версия. Само purchase transactions (без refi appraisals). По-чист от refi-bias.
- **CIVPART**: Структурни сдвигове (демография, ранно пенсиониране). Пост-COVID не се възстанови напълно.
- **MICH_INFL_1Y**: Household очаквания. По-шумни от market-based, но по-ранни. Extreme movements сигнализират de-anchoring risk.
- **LABOR_SHARE_NBS**: BLS productivity data. Cyclical fluctuations, но структурният trend е низходящ.
- **US_PMI_MFG**: Markit mfg — comparable cross-country. ISM е US-only.
- **CSUSHPISA**: Главен ценови benchmark. Repeat-sales методология; ~2 месеца lag. National композит на 9 census divisions.
- **EMRATIO**: Не зависи от definition на 'active labor force'. По-стабилен индикатор на дълбоката заетост.
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
  - `breadth_a`: 0.75
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 1.0
- 🔔 **?**
  - `pair_id`: growth_labor_lead_lag
  - `name_bg`: Hard activity × Labor claims
  - `question_bg`: Дали hard activity и labor market следват едно тенденция?
  - `state`: both_up
  - `interpretation`: Aligned expansion — activity растяща, claims низки. Healthy.
  - `slot_a_label`: Hard activity
  - `slot_b_label`: Labor market (claims inverted)
  - `breadth_a`: 0.8
  - `breadth_b`: 0.667
  - `state_raw`: both_up
  - `breadth_a_raw`: 0.8
  - `breadth_b_raw`: 0.667
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Realized CPI × Expectations
  - `question_bg`: Дали expectations следват realized inflation, или стоят anchored?
  - `state`: both_up
  - `interpretation`: De-anchoring in progress — expectations следват realized up.
  - `slot_a_label`: Realized inflation
  - `slot_b_label`: Inflation expectations
  - `breadth_a`: 0.667
  - `breadth_b`: 1.0
  - `state_raw`: both_up
  - `breadth_a_raw`: 1.0
  - `breadth_b_raw`: 1.0
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
  - `state`: a_down_b_up
  - `interpretation`: Activity OK, sentiment крачка — strategic pessimism / political bias.
  - `slot_a_label`: Consumer sentiment
  - `slot_b_label`: Hard activity
  - `breadth_a`: 0.0
  - `breadth_b`: 0.8
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.0
  - `breadth_b_raw`: 0.8
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
  - `state_raw`: a_down_b_up
  - `breadth_a_raw`: 0.333
  - `breadth_b_raw`: 1.0

### Executive narrative
> Картината показва стагфлационна конфигурация — трудовият пазар остава tight, а инфлационният натиск е broad-based. Най-отклонена леща: Инфлация и цени — breadth 76% (разширяване), 4 аномалии, 1 нови екстремума. Expectations също нагоре — de-anchoring в ход, рискът ескалира. За наблюдение следващия релиз: CIVPART (нови 5-годишни екстремуми).

### Supporting signals
- Най-силна аномалия: PPIFIS z=+2.89
- 5 нови екстремуми в top-11 (lookback 5г.)
- Активни двойки: Stagflation test=both_up; Growth × Labor=both_up; Inflation anchoring=both_up



---

## 7. EU Macro State — пълен snapshot

**Дата:** 2026-07-11 00:00:00 · **Generated:** 2026-07-11 09:07:34.290730+00:00

**Режим:** `disinflation_cooling` (Дезинфлация и охлаждане)  
**Primary driver:** `stagflation_test`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **labor** | 34.7 | contracting | 42.9% | 1 | 0 |
| **growth** | 38.7 | mixed | 16.7% | 1 | 0 |
| **inflation** | 48.0 | mixed | 85.7% | 1 | 0 |
| **credit** | 44.0 | mixed | 36.8% | 3 | 0 |
| **external** | 13.4 | contracting | 16.7% | 0 | 0 |

### Top anomalies (5 серии)
| Series ID | Name BG | Lens | Peer group | Z | Direction | Value | Last obs | NEW-EXT |
|---|---|---|---|---:|---|---:|---|:---:|
| **EA_BUND_2Y** | Bund 2Y benchmark yield | credit | sovereign_yields | +5.27 | up | 2.72 | 2026-06-01 | - |
| **EA_EMP_EXP_SERVICES** | Очаквания за заетост — услуги (3m напред) | labor | labor_sentiment | -2.66 | down | -3.80 | 2026-06-01 | - |
| **EA_SELLING_PRICE_EXP** | Очаквания за продажни цени (промишленост, 3m напред) | inflation, growth | sentiment | +2.17 | up | 22.30 | 2026-06-01 | - |
| **FR_10Y** | France 10Y government bond yield | credit | sovereign_yields | +2.15 | up | 3.68 | 2026-06-01 | - |
| **DE_10Y** | Germany 10Y Bund yield (Maastricht measure) | credit | sovereign_yields | +2.15 | up | 2.96 | 2026-06-01 | - |

### Narrative hints от макро лещите
- **EA_BUND_2Y**: EA-aggregate 2Y yield. Curve slope (10Y-2Y) проксира policy expectations и recession risk.
- **EA_EMP_EXP_SERVICES**: DG ECFIN survey: forward-looking labor сигнал от услугите (~70% от GDP). Дълга история (от 1996) — за разлика от teibs030 (EA_EMPLOYMENT_EXP, 12m). Същата полярност (higher=better). De-singleton-ва labor_sentiment.
- **EA_SELLING_PRICE_EXP**: Forward-looking inflation сигнал от business side — мениджърите казват дали ще вдигат цени. Изпреварва HICP с 3-6 месеца.
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
  - `breadth_b`: 0.4
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 0.4
- 🔔 **?**
  - `pair_id`: inflation_anchoring
  - `name_bg`: Закотвеност на инфлационните очаквания
  - `question_bg`: Headline отскача — очакванията остават ли закотвени?
  - `state`: insufficient_data
  - `interpretation`: Insufficient data в една от двете групи.
  - `slot_a_label`: Реализирана headline инфлация
  - `slot_b_label`: SPF дългосрочни очаквания
  - `breadth_a`: 0.0
  - `breadth_b`: None
  - `state_raw`: insufficient_data
  - `breadth_a_raw`: 0.0
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
  - `state`: both_up
  - `interpretation`: Healthy expansion: sentiment + hard data confirm-ват растеж.
  - `slot_a_label`: Sentiment (ESI, confidence)
  - `slot_b_label`: Hard activity (IP, retail, GDP)
  - `breadth_a`: 0.778
  - `breadth_b`: 0.75
  - `state_raw`: transition
  - `breadth_a_raw`: 0.778
  - `breadth_b_raw`: 0.5
- 🔔 **?**
  - `pair_id`: growth_labor_lead_lag
  - `name_bg`: Растеж срещу труд (lead-lag)
  - `question_bg`: Активността и пазарът на труда движат ли се заедно?
  - `state`: both_up
  - `interpretation`: Синхронна експанзия: активността расте и трудовият пазар се засилва. Класическа expansion конфигурация.
  - `slot_a_label`: Твърда активност (IP, retail, GDP)
  - `slot_b_label`: Пазар на труда (сила)
  - `breadth_a`: 0.75
  - `breadth_b`: 0.75
  - `state_raw`: transition
  - `breadth_a_raw`: 0.5
  - `breadth_b_raw`: 1.0

### Executive narrative
> Синхронно охлаждане — labor и инфлация отстъпват заедно. Рискът се мести към overshooting, ако claims ускорят. Най-отклонена леща: Инфлация и цени — breadth 0% (свиване), 1 аномалии, 0 нови екстремума. За наблюдение: EA_BUND_2Y (z=+5.27) — най-силното отклонение.

### Supporting signals
- Най-силна аномалия: EA_BUND_2Y z=+5.27
- Активни двойки: Stagflation test=both_down; Sentiment × Hard=both_up; Growth × Labor=both_up



---

## 8. CN Macro State — пълен snapshot

**Дата:** 2026-07-13 00:00:00 · **Generated:** 2026-07-13 08:42:40.266952+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 43.7 | mixed | -% | - | - |
| **inflation** | 48.0 | mixed | -% | - | - |
| **labor** | 18.6 | contracting | -% | - | - |
| **credit** | 52.3 | mixed | -% | - | - |
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
  - `breadth_a`: 0.667
  - `breadth_b`: 0.333

### Executive narrative
> Претеглен композитен macro score 39.9/100 → режим „ВЛОШАВАЩ СЕ“ (5/5 лещи). 5 лещи, 2 flagged аномалии (5 застояли изключени), 3 cross-lens двойки.



---

## 9. VRM — пълен текущ snapshot

### VRM (жив мозък — data-core overlay)
| Field | Value |
|---|---|
| `date` | 2026-07-10 |
| `as_of` | 2026-07-10 |
| `regime` | REFLATION |
| `alignment_score` | 6.0 |
| `gms_score` | 2.0 |
| `gms_max` | 8 |
| `gms_tier` | LOW |
| `ks_status` | unknown |

_4W GAP панелът (spy_4w..iwm_4w), `signal` и KS variant/portfolio етикетите нямат жив източник — ръчната серия (vrm_week) е пенсионирана 07.2026._



---

## 10. Rotation events — US + EU, пълни списъци

### US (period: 2026-07-10 → 2026-07-14)

**stable_winner (1m):** +8 entered, -9 exited
  - **Entered:** APA, CASY, CFG, HWM, LHX, MCK, SPG, USB _(включително 1 за първи път в историята: USB)_
  - **Exited:** EXPE, F, GM, GS, HAL, IDXX, JNJ, LRCX, PLD

**stable_winner (3m):** +1 entered, -5 exited
  - **Entered:** WMT
  - **Exited:** ADM, CVS, EXPE, IVZ, MRK

**quality_dip (1m):** +10 entered, -9 exited
  - **Entered:** EXPE, F, GM, GS, HAL, IDXX, JNJ, MRNA, PLD, TER _(включително 2 за първи път в историята: MRNA, TER)_
  - **Exited:** APA, CASY, CFG, CVS, HWM, LHX, MCK, SPG, USB

**quality_dip (3m):** +6 entered, -2 exited
  - **Entered:** ADM, EXPE, IVZ, MRK, MRNA, TER _(включително 4 за първи път в историята: ADM, MRK, MRNA, TER)_
  - **Exited:** LRCX, WMT

**faded_bounce (1m):** +2 entered, -7 exited
  - **Entered:** AXON, PYPL
  - **Exited:** ARE, ARES, FIS, GIS, POOL, SO, ZBH

**faded_bounce (3m):** +2 entered, -2 exited
  - **Entered:** CAG, HRL
  - **Exited:** BX, SW

### EU (period: 2026-07-10 → 2026-07-14)

**stable_winner (1m):** +10 entered, -8 exited
  - **Entered:** BESI.AS, CA.PA, CBK.DE, DANSKE.CO, EBS.VI, KER.PA, RWE.DE, SAAB-B.ST, SAN.MC, VOE.VI _(включително 1 за първи път в историята: BESI.AS)_
  - **Exited:** AED.BR, BARC.L, HM-B.ST, ISS.CO, LPP.WA, METSO.HE, REP.MC, SWED-A.ST

**stable_winner (3m):** +9 entered, -6 exited
  - **Entered:** ANA.MC, BARC.L, BESI.AS, DLG.MI, EBS.VI, GAW.L, HSBA.L, SAN.MC, STAN.L _(включително 2 за първи път в историята: BESI.AS, HSBA.L)_
  - **Exited:** ABN.AS, BCP.LS, BKT.MC, DANSKE.CO, REP.MC, VWS.CO

**quality_dip (1m):** +9 entered, -9 exited
  - **Entered:** AED.BR, BARC.L, HM-B.ST, ISS.CO, LPP.WA, METSO.HE, ORA.PA, REP.MC, SWED-A.ST _(включително 2 за първи път в историята: ORA.PA, SWED-A.ST)_
  - **Exited:** CA.PA, CBK.DE, DANSKE.CO, EBS.VI, KER.PA, RWE.DE, SAAB-B.ST, SAN.MC, VOE.VI

**quality_dip (3m):** +7 entered, -8 exited
  - **Entered:** ABN.AS, BCP.LS, BKT.MC, DANSKE.CO, ORA.PA, REP.MC, VWS.CO _(включително 1 за първи път в историята: ORA.PA)_
  - **Exited:** ANA.MC, BARC.L, DLG.MI, EBS.VI, GAW.L, HSBA.L, SAN.MC, STAN.L

**faded_bounce (1m):** +10 entered, -8 exited
  - **Entered:** ARCAD.AS, BNR.DE, BOL.PA, DSFIR.AS, HER.MI, ROCK-B.CO, SGE.L, SIKA.SW, VNA.DE, VPK.AS _(включително 1 за първи път в историята: HER.MI)_
  - **Exited:** BEI.DE, CVC.AS, DSY.PA, ICG.L, ITRK.L, LIFCO-B.ST, LUND-B.ST, NTGY.MC

**faded_bounce (3m):** +8 entered, -11 exited
  - **Entered:** BEIJ-B.ST, BOL.PA, CAP.PA, EXPN.L, NEM.DE, RI.PA, SAP.DE, TBCG.L _(включително 4 за първи път в историята: CAP.PA, NEM.DE, SAP.DE, TBCG.L)_
  - **Exited:** AMS.MC, BEI.DE, CMBN.SW, EXO.AS, LUND-B.ST, NTGY.MC, ORSTED.CO, RACE.MI, SREN.SW, TRYG.CO, VZN.SW



---

## 11. COT positioning — текуща картина (cot_monitor)

### COT Monitor (38 markets) (snapshot: 2026-07-07 00:00:00)
_Percentile = пълна история, N седмици (`hist_weeks`) — несравним между пазари._
| Market | Asset class | Net position | Net % | Percentile (пълна история) | Ист. седмици | Weekly change |
|---|---|---:|---:|---:|---:|---:|
| **soyoil** | Commodities | 89228 | 92.6 | 92.6 | 1048 | -42208 |
| **copper** | Commodities | 60397 | 89.8 | 89.8 | 1048 | -10730 |
| **vix** | Volatility | 5112 | 86.5 | 86.5 | 1007 | 40402 |
| **cattle** | Commodities | 113321 | 84.8 | 84.8 | 1048 | 4319 |
| **rbob** | Commodities | 71543 | 82.9 | 82.9 | 1048 | 7209 |
| **brent** | Commodities | 13368 | 77.9 | 77.9 | 231 | 4066 |
| **aud** | FX | 29683 | 66.2 | 66.2 | 1048 | -12609 |
| **coffee** | Commodities | 25511 | 64.7 | 64.7 | 1048 | 22379 |
| **cotton** | Commodities | 39106 | 59.9 | 59.9 | 1048 | -3098 |
| **gbpfx** | FX | 17979 | 56.9 | 56.9 | 1048 | -4333 |
| **soybeans** | Commodities | 68679 | 49.7 | 49.7 | 1048 | -22077 |
| **gold** | Commodities | 114854 | 48.6 | 48.6 | 1048 | 11194 |
| **dxy** | FX | -4454 | 42.3 | 42.3 | 1048 | 9202 |
| **natgas** | Commodities | -60377 | 38.0 | 38.0 | 1048 | 62236 |
| **platinum** | Commodities | 7476 | 37.5 | 37.5 | 1048 | -901 |
| **soymeal** | Commodities | 19025 | 36.3 | 36.3 | 1048 | -33577 |
| **corn** | Commodities | 12659 | 35.2 | 35.2 | 1048 | 17984 |
| **heatingoil** | Commodities | 4803 | 33.8 | 33.8 | 1048 | -4802 |
| **bitcoin** | Crypto | -6717 | 33.2 | 33.2 | 431 | -722 |
| **eurfx** | FX | -45461 | 31.7 | 31.7 | 1048 | -28073 |
| **sp500** | US Equities | -361875 | 31.1 | 31.1 | 1048 | 89711 |
| **chf** | FX | -7218 | 31.0 | 31.0 | 1048 | 3567 |
| **silver** | Commodities | 12131 | 30.5 | 30.5 | 1048 | 2337 |
| **wheat** | Commodities | -62325 | 24.7 | 24.7 | 1048 | 17082 |
| **russell** | US Equities | -72262 | 24.1 | 24.1 | 584 | 2192 |
| **us30y** | Rates | -365483 | 13.0 | 13.0 | 1048 | -83550 |
| **cocoa** | Commodities | -13750 | 12.4 | 12.4 | 1048 | 13536 |
| **wti** | Commodities | 74679 | 11.6 | 11.6 | 1048 | -48528 |
| **sugar** | Commodities | -97713 | 11.3 | 11.3 | 1048 | 32620 |
| **us5y** | Rates | -2174862 | 10.9 | 10.9 | 1048 | 55494 |
| **us2y** | Rates | -1756528 | 10.5 | 10.5 | 1048 | -75586 |
| **palladium** | Commodities | -6382 | 9.5 | 9.5 | 1048 | -1862 |
| **usultra10y** | Rates | -351500 | 7.4 | 7.4 | 538 | -91370 |
| **jpy** | FX | -90083 | 6.4 | 6.4 | 1048 | 9761 |
| **nasdaq** | US Equities | -55013 | 6.1 | 6.1 | 1048 | -20707 |
| **us10y** | Rates | -2004023 | 4.4 | 4.4 | 1048 | -24512 |
| **cad** | FX | -85957 | 1.2 | 1.2 | 1048 | -27334 |
| **hogs** | Commodities | -29002 | 0.2 | 0.2 | 1048 | -15301 |



---

## 12. Momentum leaders (SP500 + STOXX600)

### SP500 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **SNDK** | Technology | 99.4 | -18.4% | 71.0% | 314.9% | 4561.2% | 3.38 | -31.3% |
| 2 | **MU** | Technology | 99.2 | -7.9% | 94.2% | 161.6% | 728.8% | 2.63 | -30.3% |
| 3 | **AMD** | Technology | 98.4 | 3.4% | 107.5% | 154.8% | 249.8% | 1.83 | -27.8% |
| 4 | **DELL** | Technology | 98.3 | 4.3% | 124.3% | 245.1% | 219.6% | 1.78 | -32.3% |
| 5 | **INTC** | Technology | 98.1 | -17.3% | 61.4% | 133.8% | 434.6% | 1.91 | -26.9% |
| 6 | **STX** | Technology | 98.0 | -11.0% | 55.4% | 158.3% | 529.2% | 2.47 | -25.0% |
| 7 | **WDC** | Technology | 97.2 | -8.7% | 40.4% | 142.4% | 743.4% | 2.74 | -31.1% |
| 8 | **AMAT** | Technology | 97.1 | 2.1% | 46.6% | 89.1% | 189.9% | 1.87 | -23.3% |
| 9 | **HPE** | Technology | 97.0 | -1.3% | 94.2% | 116.5% | 137.2% | 1.62 | -26.4% |
| 10 | **MRVL** | Technology | 96.4 | -26.2% | 54.2% | 149.0% | 286.5% | 1.35 | -34.8% |
| 11 | **FLEX** | Technology | 96.0 | -14.0% | 60.6% | 107.2% | 188.1% | 1.40 | -20.6% |
| 12 | **CNC** | Healthcare | 92.8 | 2.2% | 78.8% | 43.6% | 112.8% | 1.44 | -55.5% |
| 13 | **DDOG** | Technology | 92.7 | 15.0% | 139.2% | 108.9% | 65.6% | 0.97 | -48.6% |
| 14 | **KLAC** | Technology | 92.6 | -11.8% | 25.2% | 57.6% | 177.9% | 1.47 | -28.2% |
| 15 | **LRCX** | Technology | 92.6 | -8.5% | 23.2% | 52.5% | 270.0% | 1.99 | -24.7% |
| 16 | **CSCO** | Technology | 91.8 | -7.4% | 35.8% | 52.4% | 81.6% | 1.46 | -13.7% |
| 17 | **PANW** | Technology | 91.3 | 26.6% | 119.1% | 87.4% | 46.6% | 1.39 | -36.0% |
| 18 | **VLO** | Energy | 90.7 | 13.1% | 24.8% | 64.7% | 78.2% | 1.83 | -14.2% |
| 19 | **HUM** | Healthcare | 90.5 | 7.8% | 108.3% | 48.5% | 68.7% | 1.10 | -47.2% |
| 20 | **CRWD** | Technology | 89.9 | 21.1% | 107.5% | 77.1% | 43.4% | 1.08 | -37.2% |

### STOXX600 momentum top 20
| Rank | Symbol | Sector | Mom score | 1m | 3m | 6m | 12m | Sharpe | Drawdown |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **ATS.VI** | Technology | 97.6 | -12.4% | 160.2% | 430.3% | 919.4% | 2.81 | -27.7% |
| 2 | **TPRO.MI** | Technology | 97.2 | -8.3% | 94.9% | 132.1% | 379.6% | 2.36 | -27.0% |
| 3 | **STMMI.MI** | Technology | 96.5 | -10.3% | 78.4% | 155.2% | 154.1% | 1.52 | -33.5% |
| 4 | **IFX.DE** | Technology | 94.7 | -11.1% | 60.6% | 74.8% | 116.1% | 1.32 | -21.2% |
| 5 | **SOI.PA** | Technology | 92.4 | -26.0% | 33.8% | 263.9% | 194.3% | 0.77 | -54.0% |
| 6 | **ASML.AS** | Technology | 92.3 | -4.1% | 26.8% | 44.0% | 151.5% | 2.09 | -15.8% |
| 7 | **NOKIA.HE** | Technology | 91.7 | -20.8% | 19.8% | 85.9% | 205.1% | 1.65 | -30.4% |
| 8 | **GL9.IR** | Consumer Defensive | 91.6 | 8.6% | 38.2% | 61.4% | 75.2% | 2.22 | -8.0% |
| 9 | **VACN.SW** | Industrials | 91.1 | 4.2% | 28.9% | 61.0% | 103.7% | 1.64 | -25.1% |
| 10 | **CCC.L** | Technology | 91.1 | 10.8% | 45.1% | 45.2% | 81.6% | 2.07 | -16.2% |
| 11 | **RBI.VI** | Financial Services | 91.0 | 11.5% | 24.1% | 59.8% | 112.3% | 2.12 | -18.0% |
| 12 | **NESTE.HE** | Energy | 90.4 | 12.2% | 21.7% | 57.3% | 118.4% | 2.07 | -20.4% |
| 13 | **IFCN.SW** | Technology | 90.3 | -2.1% | 50.0% | 61.8% | 68.4% | 1.17 | -25.5% |
| 14 | **AKER.OL** | Industrials | 90.2 | 9.8% | 22.7% | 67.5% | 83.6% | 2.33 | -15.6% |
| 15 | **PRY.MI** | Industrials | 89.2 | -5.3% | 14.3% | 55.6% | 141.0% | 2.06 | -15.0% |
| 16 | **ASM.AS** | Technology | 89.0 | -9.5% | 23.6% | 52.6% | 97.3% | 1.20 | -26.2% |
| 17 | **DHER.DE** | Consumer Cyclical | 88.6 | 3.7% | 108.4% | 53.3% | 59.4% | 0.78 | -48.7% |
| 18 | **BMPS.MI** | Financial Services | 88.2 | 6.5% | 47.0% | 35.4% | 69.4% | 1.68 | -25.5% |
| 19 | **TIT.MI** | Communication Services | 88.2 | 1.2% | 20.1% | 43.7% | 95.0% | 2.29 | -13.0% |
| 20 | **BESI.AS** | Technology | 88.1 | -19.9% | 16.4% | 56.8% | 148.1% | 1.26 | -24.7% |



---

## 13. Stock Selection — top 15 + bottom 5 (composite score)

### Top 15 (composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk | 52w ret | P/E | ROE |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **EIX** | Utilities | 2.119 | 1.840 | 0.910 | 2.749 | -0.589 | - | 8.3 | +18.9% |
| 2 | **NEM** | Materials | 1.849 | 1.448 | 1.799 | 1.457 | 0.585 | - | 12.3 | +25.8% |
| 3 | **MO** | Consumer Staples | 1.626 | 1.163 | 1.939 | 0.998 | -0.342 | - | 14.7 | - |
| 4 | **APA** | Energy | 1.357 | 1.480 | 1.142 | 0.878 | -0.366 | - | 8.0 | +26.2% |
| 5 | **HST** | Real Estate | 1.231 | 1.523 | 0.435 | 1.285 | 0.068 | - | 16.2 | +14.9% |
| 6 | **SPG** | Real Estate | 1.195 | 1.240 | 1.339 | 0.473 | -1.331 | - | 15.4 | +113.6% |
| 7 | **SYF** | Financials | 1.193 | 0.087 | 1.191 | 1.693 | -0.422 | - | 7.7 | +21.8% |
| 8 | **CF** | Materials | 1.091 | 0.021 | 0.995 | 1.707 | 0.539 | - | 10.6 | +27.3% |
| 9 | **BMY** | Health Care | 1.008 | 0.707 | 0.914 | 0.948 | 0.364 | - | 16.4 | +38.7% |
| 10 | **TPR** | Consumer Discretionary | 0.935 | 1.575 | 1.111 | -0.255 | -0.821 | - | 42.8 | +60.9% |
| 11 | **MAS** | Industrials | 0.934 | 0.090 | 1.256 | 0.957 | -1.667 | - | 19.3 | +8457.1% |
| 12 | **DVA** | Health Care | 0.902 | 1.096 | 0.189 | 1.103 | -1.458 | - | 22.3 | +81.0% |
| 13 | **MRK** | Health Care | 0.869 | 1.261 | 0.850 | 0.148 | 0.403 | - | 34.8 | +18.9% |
| 14 | **VRSN** | Information Technology | 0.867 | -0.415 | 2.201 | 0.230 | 1.681 | - | 29.9 | - |
| 15 | **MU** | Information Technology | 0.863 | 1.416 | 0.809 | 0.034 | -0.629 | - | 20.4 | +66.6% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -2.134 | -1.775 | -1.188 | -2.523 | -1.324 |
| 502 | **COIN** | Financials | -1.970 | -2.274 | -1.249 | -1.578 | -1.695 |
| 501 | **CSGP** | Real Estate | -1.770 | -3.151 | -0.727 | -0.819 | 0.488 |
| 500 | **KKR** | Financials | -1.647 | -1.305 | -1.348 | -1.537 | -0.926 |
| 499 | **DASH** | Consumer Discretionary | -1.562 | -1.491 | -0.272 | -2.314 | -0.529 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W29.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W29.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\dashboards\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-07-13  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
