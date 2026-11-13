# Сателит — пълен data export за 2026-W46

_Период: 2026-11-09 → 2026-11-15_  
_Генериран: 2026-11-13 14:02 UTC_  
_Тип: comprehensive raw data dump (за downstream analysis с parallel-thinking, deep research, custom workflows)_  
_Различава се от: `2026-W46.md` (structured briefing) и `narrative_2026-W46.md` (prose narrative)._

_Източник: macro-satellite, 12 dashboards, ~100k Parquet rows._


---

## 1. ETF anomalies — пълен universe (всички с |z| >= 1.0σ)

_Седмично изменение vs trailing 13-week distribution на същия symbol. z-score = брой стандартни отклонения от mean._

**24 ETF в universe-а от 37 с |z| >= 1.0σ:**

| Symbol | Week chg | Z-score | Price A | Price B | Date A | Date B | Trailing mean | Trailing std | N base |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|
| **XLI** | +4.16% | +3.80σ | 162.67 | 169.44 | 2026-11-06 | 2026-11-12 | -0.98% | +1.36% | 13 |
| **EFA** | +2.08% | +3.09σ | 101.89 | 104.01 | 2026-11-06 | 2026-11-12 | -0.48% | +0.83% | 13 |
| **SPY** | +2.97% | +3.04σ | 735.29 | 757.12 | 2026-11-06 | 2026-11-12 | -0.38% | +1.10% | 13 |
| **SHY** | -0.60% | -3.02σ | 81.63 | 81.14 | 2026-11-06 | 2026-11-12 | -0.03% | +0.19% | 13 |
| **VEA** | +2.25% | +2.75σ | 67.90 | 69.43 | 2026-11-06 | 2026-11-12 | -0.54% | +1.02% | 13 |
| **DIA** | +2.00% | +2.75σ | 512.22 | 522.47 | 2026-11-06 | 2026-11-12 | -0.40% | +0.87% | 13 |
| **TIP** | -1.41% | -2.42σ | 106.27 | 104.77 | 2026-11-06 | 2026-11-12 | -0.06% | +0.56% | 13 |
| **QQQ** | +4.89% | +2.38σ | 656.10 | 688.17 | 2026-11-06 | 2026-11-12 | -0.72% | +2.36% | 13 |
| **IEF** | -1.80% | -2.36σ | 91.86 | 90.21 | 2026-11-06 | 2026-11-12 | -0.11% | +0.72% | 13 |
| **DFEN** | +11.72% | +2.31σ | 45.55 | 50.89 | 2026-11-06 | 2026-11-12 | -4.51% | +7.02% | 13 |
| **VWO** | +2.06% | +2.27σ | 55.29 | 56.43 | 2026-11-06 | 2026-11-12 | -0.68% | +1.21% | 13 |
| **XLK** | +5.48% | +1.88σ | 164.74 | 173.77 | 2026-11-06 | 2026-11-12 | -0.95% | +3.42% | 13 |
| **EEM** | +3.05% | +1.85σ | 59.33 | 61.14 | 2026-11-06 | 2026-11-12 | -0.75% | +2.05% | 13 |
| **TLT** | -2.69% | -1.83σ | 81.92 | 79.72 | 2026-11-06 | 2026-11-12 | -0.07% | +1.43% | 13 |
| **XLY** | +2.45% | +1.80σ | 117.58 | 120.46 | 2026-11-06 | 2026-11-12 | -0.14% | +1.44% | 13 |
| **IWM** | +1.74% | +1.68σ | 273.67 | 278.44 | 2026-11-06 | 2026-11-12 | -0.73% | +1.47% | 13 |
| **LQD** | -1.42% | -1.66σ | 104.53 | 103.05 | 2026-11-06 | 2026-11-12 | -0.14% | +0.76% | 13 |
| **GLD** | -4.73% | -1.48σ | 372.52 | 354.89 | 2026-11-06 | 2026-11-12 | -0.48% | +2.88% | 13 |
| **UUP** | +1.00% | +1.27σ | 29.13 | 29.42 | 2026-11-06 | 2026-11-12 | +0.29% | +0.56% | 13 |
| **XLF** | +1.84% | +1.21σ | 57.16 | 58.21 | 2026-11-06 | 2026-11-12 | -0.05% | +1.55% | 13 |
| **XLC** | +2.64% | +1.18σ | 104.79 | 107.56 | 2026-11-06 | 2026-11-12 | -0.43% | +2.60% | 13 |
| **SOXX** | +13.52% | +1.13σ | 136.53 | 154.99 | 2026-11-06 | 2026-11-12 | -7.04% | +18.22% | 13 |
| **IBIT** | -5.88% | -1.08σ | 42.88 | 40.36 | 2026-11-06 | 2026-11-12 | +1.39% | +6.76% | 13 |
| **GDX** | -6.58% | -1.02σ | 87.60 | 81.84 | 2026-11-06 | 2026-11-12 | -0.00% | +6.44% | 13 |


---

## 2. Cross-asset divergence patterns — пълно evaluation

_2 активни canonical patterns от `config/divergence_rules.yaml` (пенсионираните с `enabled: false` не се оценяват — П3а), evaluated за края на седмицата._

### Стагфлационна дивергенция (модел vs наратив) (`stagflation_hint`) — не активен
_S&P 500 нормално нагоре, но реалните потоци казват: енергия+ , отбрана-, инфлационни хеджове-, долар+. Класически 7-15 май 2026 pattern._  
**Window:** 8d ending 2026-11-15 · **Conditions matched:** 2/5

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| USO | up ≥ 3.0% | -1.58% | ❌ | 148.41 | 146.07 | 2026-11-06 | 2026-11-12 |
| DFEN | down ≥ 3.0% | +11.72% | ❌ | 45.55 | 50.89 | 2026-11-06 | 2026-11-12 |
| GLD | down ≥ 1.0% | -4.73% | ✅ | 372.52 | 354.89 | 2026-11-06 | 2026-11-12 |
| URA | down ≥ 3.0% | +0.06% | ❌ | 32.34 | 32.36 | 2026-11-06 | 2026-11-12 |
| UUP | up ≥ 0.5% | +1.00% | ✅ | 29.13 | 29.42 | 2026-11-06 | 2026-11-12 |

### Risk-on ротация (small caps лидиращи) (`risk_on_rotation`) — 🔔 ТРИГГЕРИРАН
_IWM (small caps) > SPY, XLF + XLY нагоре, dollar надолу, gold надолу. Reflationar narrative._  
**Window:** 7d ending 2026-11-15 · **Conditions matched:** 4/4

| Symbol | Target | Actual | Match | Price A | Price B | Date A | Date B |
|---|---|---:|:---:|---:|---:|---|---|
| IWM | up ≥ 1.5% | +1.74% | ✅ | 273.67 | 278.44 | 2026-11-06 | 2026-11-12 |
| XLF | up ≥ 1.0% | +1.84% | ✅ | 57.16 | 58.21 | 2026-11-06 | 2026-11-12 |
| XLY | up ≥ 1.0% | +2.45% | ✅ | 117.58 | 120.46 | 2026-11-06 | 2026-11-12 |
| GLD | down ≥ 0.5% | -4.73% | ✅ | 372.52 | 354.89 | 2026-11-06 | 2026-11-12 |



---

## 3. Исторически паралели — top 10 най-similar weeks

_Cosine similarity vs 10-ETF macro signature vector (SPY, IWM, TLT, GLD, USO, UUP, HYG, XLE, XLK, XLF). Forward returns 1m/3m/6m за SPY, USO, GLD, TLT, XLE, IWM._

### Паралел #1: 2025-W20 (week ending 2025-05-18)
**Cosine similarity:** 0.8623 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.56% | +8.29% | +13.08% |
| **USO** | +20.85% | +6.90% | +4.82% |
| **GLD** | +6.02% | +4.48% | +27.77% |
| **TLT** | +0.23% | +0.12% | +2.98% |
| **XLE** | +3.72% | +0.09% | +7.65% |
| **IWM** | -0.62% | +8.23% | +13.17% |

### Паралел #2: 2022-W42 (week ending 2022-10-23)
**Cosine similarity:** 0.7816 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +6.84% | +5.77% | +10.13% |
| **USO** | -0.84% | +1.39% | -3.34% |
| **GLD** | +5.14% | +16.31% | +19.53% |
| **TLT** | +8.92% | +13.99% | +12.05% |
| **XLE** | +7.24% | +4.08% | -2.24% |
| **IWM** | +6.95% | +7.15% | +2.81% |

### Паралел #3: 2024-W17 (week ending 2024-04-28)
**Cosine similarity:** 0.7621 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.24% | +7.12% | +13.93% |
| **USO** | -3.40% | -5.32% | -7.66% |
| **GLD** | +0.72% | +1.85% | +16.94% |
| **TLT** | +2.07% | +5.38% | +4.42% |
| **XLE** | -3.58% | -3.71% | -6.24% |
| **IWM** | +3.43% | +13.04% | +10.35% |

### Паралел #4: 2023-W20 (week ending 2023-05-21)
**Cosine similarity:** 0.7562 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +4.43% | +4.27% | +7.68% |
| **USO** | +0.03% | +13.91% | +10.72% |
| **GLD** | -2.12% | -4.53% | +0.02% |
| **TLT** | +2.19% | -7.25% | -10.94% |
| **XLE** | -1.61% | +11.51% | +6.34% |
| **IWM** | +5.12% | +4.85% | +1.24% |

### Паралел #5: 2025-W49 (week ending 2025-12-07)
**Cosine similarity:** 0.7302 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.89% | -1.94% | +7.56% |
| **USO** | -4.74% | +51.24% | +84.96% |
| **GLD** | +6.92% | +22.53% | +2.54% |
| **TLT** | -1.01% | +0.33% | -3.53% |
| **XLE** | -0.61% | +23.19% | +25.59% |
| **IWM** | +2.12% | +0.05% | +12.31% |

### Паралел #6: 2022-W04 (week ending 2022-01-30)
**Cosine similarity:** 0.7279 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -2.71% | -6.78% | -6.78% |
| **USO** | +15.89% | +24.51% | +25.95% |
| **GLD** | +8.69% | +5.87% | -1.80% |
| **TLT** | -1.28% | -16.54% | -17.96% |
| **XLE** | +8.62% | +14.51% | +19.49% |
| **IWM** | +2.17% | -5.28% | -4.10% |

### Паралел #7: 2024-W45 (week ending 2024-11-10)
**Cosine similarity:** 0.6984 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +0.77% | +0.43% | -5.66% |
| **USO** | -2.37% | +3.73% | -8.92% |
| **GLD** | +0.25% | +6.43% | +23.75% |
| **TLT** | +0.64% | -3.48% | -5.88% |
| **XLE** | -3.73% | -5.54% | -12.07% |
| **IWM** | -0.60% | -5.09% | -15.67% |

### Паралел #8: 2023-W04 (week ending 2023-01-29)
**Cosine similarity:** 0.6955 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | -2.32% | +2.53% | +12.63% |
| **USO** | -3.29% | -2.88% | +3.73% |
| **GLD** | -5.27% | +3.11% | +1.47% |
| **TLT** | -4.69% | -0.23% | -6.47% |
| **XLE** | -8.26% | -6.69% | -5.90% |
| **IWM** | -0.74% | -7.59% | +3.61% |

### Паралел #9: 2025-W17 (week ending 2025-04-27)
**Cosine similarity:** 0.6911 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +7.36% | +15.70% | +22.99% |
| **USO** | -2.54% | +8.43% | +6.01% |
| **GLD** | -0.08% | +0.88% | +23.89% |
| **TLT** | -3.55% | -2.77% | +2.90% |
| **XLE** | +0.38% | +5.72% | +6.89% |
| **IWM** | +7.00% | +15.59% | +28.49% |

### Паралел #10: 2023-W26 (week ending 2023-07-02)
**Cosine similarity:** 0.6828 · **Common symbols:** 10/10

| Symbol | +1m | +3m | +6m |
|---|---:|---:|---:|
| **SPY** | +2.98% | -3.56% | +7.23% |
| **USO** | +14.81% | +27.24% | +4.88% |
| **GLD** | +1.23% | -3.83% | +7.24% |
| **TLT** | -4.66% | -13.84% | -3.94% |
| **XLE** | +7.27% | +11.36% | +3.29% |
| **IWM** | +5.62% | -5.62% | +7.18% |



---

## 4. Backtest на canonical queries

_8 предефинирани hypothesis-а. За всеки: брой episodes в 5y history + forward returns статистика (mean/median/win_rate)._

### `stagflation_signature` — Стагфлационна signature (USO силен, DFEN слаб, GLD слаб)
_Седмици когато USO е +5%+ за 4w, DFEN -3%- за 4w, GLD -1%- за 4w. Reproducира 7-15 май 2026 incident._  
**Episodes:** 16 · **Total matching days:** 96 · **History:** 2021-05-17 → 2026-11-12

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 16 | +2.0% | +2.2% | -3.1% | +7.4% | 69% |
| **SPY** | 3m | 16 | +2.4% | +2.5% | -7.3% | +12.0% | 69% |
| **SPY** | 6m | 16 | +6.6% | +8.6% | -6.8% | +21.8% | 69% |
| **USO** | 1m | 16 | -0.5% | -1.2% | -14.3% | +12.7% | 44% |
| **USO** | 3m | 16 | -1.0% | -5.1% | -18.9% | +30.5% | 44% |
| **USO** | 6m | 16 | +12.4% | +2.1% | -9.7% | +109.4% | 56% |
| **GLD** | 1m | 16 | +2.1% | +0.8% | -7.1% | +9.0% | 69% |
| **GLD** | 3m | 16 | +3.7% | +3.4% | -12.6% | +24.5% | 62% |
| **GLD** | 6m | 16 | +3.8% | +3.4% | -12.5% | +25.3% | 56% |
| **TLT** | 1m | 16 | -1.5% | -1.1% | -6.7% | +3.6% | 31% |
| **TLT** | 3m | 16 | -0.8% | -0.5% | -16.5% | +11.1% | 44% |
| **TLT** | 6m | 16 | -4.2% | -3.9% | -18.0% | +7.5% | 25% |

**Episodes (последни 5 от 16):**
- `2026-03-18 → 2026-04-10` (17d)
- `2026-04-29 → 2026-05-19` (10d)
- `2026-07-17 → 2026-08-03` (5d)
- `2026-09-10 → 2026-10-01` (14d)
- `2026-10-16 → 2026-10-27` (8d)

### `spy_near_high_with_oil_high` — SPY близо до ATH + петролни цени високи
_SPY в рамките на 3% от 52w high, USO в горните 20% от 52w range._  
**Episodes:** 2 · **Total matching days:** 122 · **History:** 2021-05-17 → 2026-11-12

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 2 | +6.3% | +6.3% | +3.5% | +9.1% | 100% |
| **SPY** | 3m | 2 | +6.9% | +6.9% | +3.5% | +10.3% | 100% |
| **SPY** | 6m | 2 | +7.8% | +7.8% | +0.7% | +15.0% | 100% |
| **USO** | 1m | 2 | +5.6% | +5.6% | +4.0% | +7.2% | 100% |
| **USO** | 3m | 2 | +8.7% | +8.7% | -9.9% | +27.4% | 50% |
| **USO** | 6m | 2 | +18.5% | +18.5% | +15.5% | +21.6% | 100% |
| **GLD** | 1m | 2 | +3.5% | +3.5% | -0.2% | +7.2% | 50% |
| **GLD** | 3m | 2 | -5.6% | -5.6% | -13.8% | +2.6% | 50% |
| **GLD** | 6m | 2 | -9.1% | -9.1% | -13.5% | -4.6% | 0% |
| **TLT** | 1m | 2 | -1.4% | -1.4% | -1.8% | -1.0% | 0% |
| **TLT** | 3m | 2 | -4.9% | -4.9% | -6.8% | -2.9% | 0% |
| **TLT** | 6m | 2 | -8.2% | -8.2% | -11.2% | -5.2% | 0% |

**Episodes (последни 5 от 2):**
- `2026-04-08 → 2026-06-15` (47d)
- `2026-07-14 → 2026-11-12` (75d)

### `tlt_yields_high` — Дългосрочни yields високи (TLT депресиран)
_TLT < 90 (proxy за 10Y > ~4.5%)._  
**Episodes:** 8 · **Total matching days:** 484 · **History:** 2021-05-17 → 2026-11-12

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
- `2025-11-03 → 2026-11-12` (252d)

### `late_cycle_warning` — Late-cycle warning: SPY ATH + GLD rising + HYG weak
_SPY близо до ATH (-3% или по-добре), GLD +5%+ за 13w, HYG -2%- за 13w._  
**Episodes:** 1 · **Total matching days:** 1 · **History:** 2021-05-17 → 2026-11-12

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 1 | -1.5% | -1.5% | -1.5% | -1.5% | 0% |
| **SPY** | 3m | 1 | -1.8% | -1.8% | -1.8% | -1.8% | 0% |
| **SPY** | 6m | 1 | -1.8% | -1.8% | -1.8% | -1.8% | 0% |
| **USO** | 1m | 1 | +14.3% | +14.3% | +14.3% | +14.3% | 100% |
| **USO** | 3m | 1 | -1.5% | -1.5% | -1.5% | -1.5% | 0% |
| **USO** | 6m | 1 | -1.5% | -1.5% | -1.5% | -1.5% | 0% |
| **GLD** | 1m | 1 | -6.8% | -6.8% | -6.8% | -6.8% | 0% |
| **GLD** | 3m | 1 | -9.8% | -9.8% | -9.8% | -9.8% | 0% |
| **GLD** | 6m | 1 | -9.8% | -9.8% | -9.8% | -9.8% | 0% |
| **TLT** | 1m | 1 | +2.5% | +2.5% | +2.5% | +2.5% | 100% |
| **TLT** | 3m | 1 | +0.5% | +0.5% | +0.5% | +0.5% | 100% |
| **TLT** | 6m | 1 | +0.5% | +0.5% | +0.5% | +0.5% | 100% |

**Episodes (последни 5 от 1):**
- `2026-09-25 → 2026-09-25` (1d)

### `oil_supply_shock` — Oil supply shock (USO 4w > +15%)
_Рядко event — USO +15% за 4 седмици._  
**Episodes:** 10 · **Total matching days:** 101 · **History:** 2021-05-17 → 2026-11-12

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 10 | -0.1% | +0.6% | -7.2% | +7.8% | 60% |
| **SPY** | 3m | 10 | +1.8% | +1.4% | -8.3% | +11.6% | 50% |
| **SPY** | 6m | 10 | +0.9% | +2.7% | -20.8% | +14.2% | 60% |
| **USO** | 1m | 10 | +4.1% | +0.5% | -15.0% | +52.9% | 50% |
| **USO** | 3m | 10 | +10.0% | +7.3% | -20.7% | +52.2% | 60% |
| **USO** | 6m | 10 | +11.1% | +4.0% | -27.6% | +56.3% | 60% |
| **GLD** | 1m | 10 | -1.2% | -1.9% | -8.3% | +11.7% | 20% |
| **GLD** | 3m | 10 | -2.2% | -1.4% | -12.0% | +6.4% | 40% |
| **GLD** | 6m | 10 | -2.1% | -5.5% | -15.2% | +25.0% | 30% |
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
**Episodes:** 17 · **Total matching days:** 294 · **History:** 2021-05-17 → 2026-11-12

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 17 | +1.9% | +1.6% | -4.8% | +9.0% | 71% |
| **SPY** | 3m | 17 | +2.8% | +4.2% | -12.6% | +16.2% | 71% |
| **SPY** | 6m | 17 | +6.4% | +8.1% | -14.0% | +21.0% | 76% |
| **USO** | 1m | 17 | +2.4% | -2.2% | -13.0% | +22.9% | 41% |
| **USO** | 3m | 17 | +3.4% | -0.8% | -14.5% | +29.9% | 41% |
| **USO** | 6m | 17 | +14.1% | +2.6% | -12.4% | +87.1% | 71% |
| **GLD** | 1m | 17 | +2.4% | +2.1% | -5.6% | +9.0% | 76% |
| **GLD** | 3m | 17 | +5.5% | +7.2% | -16.8% | +23.6% | 65% |
| **GLD** | 6m | 17 | +9.8% | +9.8% | -14.1% | +43.8% | 71% |
| **TLT** | 1m | 17 | +0.3% | -0.0% | -6.3% | +8.2% | 47% |
| **TLT** | 3m | 17 | -1.5% | -1.1% | -15.3% | +11.9% | 35% |
| **TLT** | 6m | 17 | -4.8% | -3.7% | -21.3% | +7.0% | 35% |

**Episodes (последни 5 от 17):**
- `2025-06-12 → 2025-06-16` (3d)
- `2025-09-03 → 2025-10-24` (38d)
- `2025-11-26 → 2026-03-06` (49d)
- `2026-04-20 → 2026-04-24` (4d)
- `2026-08-07 → 2026-09-03` (19d)

### `dollar_squeeze` — Dollar squeeze (UUP 4w > +2%)
_Доларова сила — често крос-asset stress signal._  
**Episodes:** 20 · **Total matching days:** 304 · **History:** 2021-05-17 → 2026-11-12

| Symbol | Horizon | n | Mean | Median | Min | Max | Win rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **SPY** | 1m | 20 | +0.3% | +0.5% | -8.7% | +7.0% | 50% |
| **SPY** | 3m | 20 | +1.9% | +3.2% | -13.7% | +9.1% | 65% |
| **SPY** | 6m | 20 | +3.0% | +4.7% | -16.4% | +16.9% | 70% |
| **USO** | 1m | 20 | -0.2% | -3.7% | -21.8% | +55.8% | 45% |
| **USO** | 3m | 20 | +3.6% | -1.0% | -12.7% | +64.3% | 45% |
| **USO** | 6m | 20 | +8.4% | +1.8% | -16.0% | +75.1% | 50% |
| **GLD** | 1m | 20 | -0.8% | -0.2% | -12.4% | +7.6% | 45% |
| **GLD** | 3m | 20 | +1.2% | +1.5% | -13.7% | +19.0% | 65% |
| **GLD** | 6m | 20 | +6.5% | +4.3% | -15.8% | +55.5% | 65% |
| **TLT** | 1m | 20 | -0.2% | -0.1% | -5.6% | +5.2% | 45% |
| **TLT** | 3m | 20 | -3.6% | -3.9% | -17.3% | +8.7% | 30% |
| **TLT** | 6m | 20 | -6.8% | -6.8% | -21.4% | +4.6% | 20% |

**Episodes (последни 5 от 20):**
- `2025-07-29 → 2025-08-01` (4d)
- `2025-10-09 → 2025-11-03` (8d)
- `2026-02-25 → 2026-03-30` (13d)
- `2026-06-05 → 2026-07-01` (13d)
- `2026-09-21 → 2026-10-15` (16d)

### `energy_outperformance` — Енергията води (XLE/SPY ratio в нагоре trend)
_XLE/SPY ratio в горните 15% от 52w range — енергията outperform-ва._  
**Episodes:** 0 · **Total matching days:** 0 · **History:** 2021-05-17 → 2026-11-12

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
| **CN_LPR_1Y** | 1-годишен Loan Prime Rate (PBoC) | credit | rates | 6 | 2.54 | 2.54 | 2026-10-12 00:00:00 | 2026-11-09 00:00:00 | ✓ |
| **CN_YOUTH_UNEMPLOYMENT** | Младежка безработица (16-24 г., %) | labor | unemployment | 6 | 2.23 | 2.23 | 2026-10-12 00:00:00 | 2026-11-09 00:00:00 | ✓ |
| **CN_CGB_10Y** | 10Y China Government Bond yield | credit | rates | 6 | 2.19 | 2.19 | 2026-10-12 00:00:00 | 2026-11-09 00:00:00 | - |



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

**Дата:** 2026-11-09 00:00:00 · **Generated:** 2026-11-09 14:32:20.704180+00:00

**Режим:** `deteriorating` (ВЛОШАВАЩ СЕ)  
**Primary driver:** `None`

### Lens scores
| Lens | Score | Direction | Breadth % | N anomalies | N new extremes |
|---|---:|---|---:|---:|---:|
| **growth** | 38.4 | mixed | -% | - | - |
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
  - `state`: both_up
  - `interpretation`: Балансиран растеж — и износ, и вътрешно търсене се разширяват.
  - `slot_a_label`: Външно търсене
  - `slot_b_label`: Вътрешна активност
  - `breadth_a`: 0.833
  - `breadth_b`: 0.667

### Executive narrative
> Претеглен композитен macro score 36.8/100 → режим „ВЛОШАВАЩ СЕ“ (5/5 лещи). 5 лещи, 3 flagged аномалии (3 застояли изключени), 3 cross-lens двойки.



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

### US (period: 2026-11-06 → 2026-11-11)

**stable_winner (1m):** +7 entered, -10 exited
  - **Entered:** CASY, EQIX, FCX, GL, HAS, IBKR, SPG
  - **Exited:** APA, FITB, GOOG, GOOGL, HST, IVZ, KEY, MNST, NEM, PFG

**stable_winner (3m):** +6 entered, -4 exited
  - **Entered:** ADM, AEP, AES, AIZ, IRM, KO _(включително 1 за първи път в историята: KO)_
  - **Exited:** CIEN, IVZ, NEM, NTRS

**quality_dip (1m):** +12 entered, -7 exited
  - **Entered:** AES, APA, FITB, GOOG, GOOGL, HST, IVZ, KEY, KO, MNST, NEM, PFG _(включително 1 за първи път в историята: KO)_
  - **Exited:** CASY, EQIX, FCX, GL, HAS, IBKR, SPG

**quality_dip (3m):** +4 entered, -4 exited
  - **Entered:** CIEN, IVZ, NEM, NTRS
  - **Exited:** ADM, AEP, AIZ, IRM

**faded_bounce (1m):** +7 entered, -6 exited
  - **Entered:** AXON, CCI, CLX, ERIE, PAYX, SHW, TSCO
  - **Exited:** APTV, COIN, HRL, MOS, NVR, PEG

**faded_bounce (3m):** +3 entered, -6 exited
  - **Entered:** AJG, LULU, SHW
  - **Exited:** BKNG, BX, EXE, KKR, LEN, OKE

### EU (period: 2026-11-06 → 2026-11-12)

**stable_winner (1m):** +5 entered, -12 exited
  - **Entered:** ASML.AS, BOL.ST, CPG.L, HM-B.ST, INDU-C.ST
  - **Exited:** BAMI.MI, BCP.LS, DANSKE.CO, FRES.L, HOC.L, HUBN.SW, IHG.L, RWE.DE, SGRO.L, SUBC.OL, VOD.L, VOE.VI

**stable_winner (3m):** +4 entered, -10 exited
  - **Entered:** CPG.L, FORTUM.HE, MBK.WA, SDZ.SW _(включително 2 за първи път в историята: FORTUM.HE, SDZ.SW)_
  - **Exited:** AIXA.DE, BEZ.L, DLG.MI, FR.PA, JYSK.CO, MT.AS, RWE.DE, SUBC.OL, UNI.MC, VWS.CO

**quality_dip (1m):** +13 entered, -7 exited
  - **Entered:** BAMI.MI, BCP.LS, DANSKE.CO, FORTUM.HE, HOC.L, HUBN.SW, IHG.L, RWE.DE, SDZ.SW, SGRO.L, UNI.MI, VOD.L, VOE.VI _(включително 2 за първи път в историята: FORTUM.HE, SDZ.SW)_
  - **Exited:** ASML.AS, BOL.ST, CPG.L, HM-B.ST, INDU-C.ST, UMI.BR, WRT1V.HE

**quality_dip (3m):** +10 entered, -5 exited
  - **Entered:** AIXA.DE, BEZ.L, DLG.MI, FR.PA, JYSK.CO, MT.AS, RWE.DE, UNI.MC, UNI.MI, VWS.CO _(включително 1 за първи път в историята: MT.AS)_
  - **Exited:** CPG.L, FRES.L, MBK.WA, UMI.BR, WRT1V.HE

**faded_bounce (1m):** +12 entered, -13 exited
  - **Entered:** BKW.SW, EQT.ST, EXPN.L, GIVN.SW, LATO-B.ST, LSEG.L, PRX.AS, RHM.DE, SQN.SW, TE.PA, TRYG.CO, TW.L _(включително 1 за първи път в историята: PRX.AS)_
  - **Exited:** AV.L, CAP.PA, CVC.AS, HER.MI, HOLM-B.ST, INW.MI, PNN.L, RACE.MI, SCA-B.ST, SGO.PA, SWEC-B.ST, TEP.PA, VTY.L

**faded_bounce (3m):** +7 entered, -9 exited
  - **Entered:** BKW.SW, CAP.PA, COLO-B.CO, EXPN.L, LSEG.L, SQN.SW, WISE.L _(включително 1 за първи път в историята: COLO-B.CO)_
  - **Exited:** AV.L, BWY.L, EQT.ST, PGHN.SW, PNDORA.CO, SGO.PA, TEP.PA, TOM.OL, TW.L



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
| 1 | **MRNA** | Healthcare | 97.7 | 15.0% | 290.7% | 393.2% | 773.4% | 1.74 | -34.2% |
| 2 | **OKTA** | Technology | 90.3 | -19.6% | 17.6% | 133.1% | 164.2% | 1.05 | -33.1% |
| 3 | **RVTY** | Healthcare | 90.0 | 2.1% | 34.7% | 66.6% | 68.2% | 1.24 | -30.1% |
| 4 | **CRL** | Healthcare | 89.7 | 14.6% | 21.8% | 110.4% | 77.0% | 1.40 | -33.9% |
| 5 | **MPC** | Energy | 89.7 | -15.5% | 13.3% | 62.8% | 147.0% | 1.84 | -23.1% |
| 6 | **PSX** | Energy | 88.0 | -11.6% | 11.8% | 52.5% | 117.4% | 1.82 | -17.4% |
| 7 | **HUM** | Healthcare | 86.2 | 6.4% | 16.2% | 47.1% | 78.2% | 1.27 | -44.9% |
| 8 | **VLO** | Energy | 86.2 | -20.3% | 6.1% | 50.3% | 160.2% | 1.74 | -24.6% |
| 9 | **VTRS** | Healthcare | 85.9 | 22.1% | 32.3% | 23.1% | 75.6% | 2.23 | -19.0% |
| 10 | **ILMN** | Healthcare | 85.2 | -21.5% | 10.5% | 46.9% | 122.8% | 1.05 | -29.2% |
| 11 | **APA** | Energy | 84.3 | -2.1% | 17.4% | 28.0% | 101.8% | 1.41 | -27.7% |
| 12 | **AMD** | Technology | 83.8 | -8.7% | 14.5% | 24.1% | 148.2% | 1.06 | -37.7% |
| 13 | **CRWD** | Technology | 82.6 | -12.3% | 1.6% | 62.9% | 87.4% | 0.80 | -37.2% |
| 14 | **MRK** | Healthcare | 82.1 | 3.7% | 9.2% | 31.4% | 68.5% | 1.72 | -11.4% |
| 15 | **BDX** | Healthcare | 81.7 | 14.5% | 18.6% | 50.7% | 34.5% | 1.46 | -23.1% |
| 16 | **TGT** | Consumer Defensive | 81.7 | 7.8% | 5.4% | 35.9% | 74.3% | 1.86 | -13.3% |
| 17 | **SWK** | Industrials | 80.8 | 27.5% | 14.1% | 51.8% | 39.2% | 1.39 | -26.1% |
| 18 | **ABBV** | Healthcare | 79.3 | 8.2% | 18.3% | 43.4% | 28.4% | 1.11 | -15.7% |
| 19 | **HAS** | Consumer Cyclical | 79.2 | 29.3% | 29.2% | 34.0% | 26.7% | 1.40 | -27.3% |
| 20 | **BBY** | Consumer Cyclical | 79.1 | 19.6% | 24.5% | 93.9% | 18.6% | 0.78 | -32.0% |

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
| 1 | **SNDK** | Information Technology | 1.958 | 1.682 | 1.693 | 1.574 | -0.130 | - | 7.5 | +141.2% |
| 2 | **EIX** | Utilities | 1.729 | 0.409 | 0.892 | 2.973 | -0.864 | - | 6.4 | +18.8% |
| 3 | **MO** | Consumer Staples | 1.487 | 1.114 | 1.834 | 0.737 | -0.056 | - | 16.1 | - |
| 4 | **CF** | Materials | 1.464 | 0.992 | 1.206 | 1.473 | 0.450 | - | 8.8 | +30.9% |
| 5 | **NEM** | Materials | 1.363 | 0.647 | 1.682 | 0.996 | 0.562 | - | 13.1 | +27.3% |
| 6 | **HST** | Real Estate | 1.319 | 1.943 | 0.335 | 1.255 | -0.316 | - | 18.9 | +14.2% |
| 7 | **MU** | Information Technology | 1.292 | 1.395 | 1.173 | 0.736 | -0.384 | - | 10.7 | +88.3% |
| 8 | **APA** | Energy | 1.147 | 1.065 | 1.151 | 0.683 | 0.172 | - | 7.7 | +33.3% |
| 9 | **SYF** | Financials | 1.126 | -0.402 | 1.174 | 1.862 | -0.194 | - | 7.5 | +19.8% |
| 10 | **DVA** | Health Care | 1.120 | 1.032 | 0.198 | 1.691 | -1.326 | - | 13.2 | +96.8% |
| 11 | **VLO** | Energy | 1.102 | 1.453 | 0.335 | 1.135 | -0.397 | - | 8.5 | +46.9% |
| 12 | **DECK** | Consumer Discretionary | 1.046 | 0.379 | 0.786 | 1.421 | 0.318 | - | 11.2 | +44.3% |
| 13 | **SPG** | Real Estate | 1.019 | 0.815 | 1.360 | 0.352 | -1.443 | - | 16.9 | +125.2% |
| 14 | **CPAY** | Financials | 1.019 | 1.740 | 0.995 | -0.040 | -0.671 | - | 25.1 | +32.2% |
| 15 | **MPC** | Energy | 1.000 | 1.296 | 0.315 | 1.039 | -0.995 | - | 8.2 | +60.5% |

### Bottom 5 (worst composite score)
| Rank | Ticker | Sector | Composite | Trend | Quality | Value | Risk |
|---:|---|---|---:|---:|---:|---:|---:|
| 503 | **AXON** | Industrials | -2.158 | -1.622 | -1.371 | -2.443 | -1.219 |
| 502 | **TSLA** | Consumer Discretionary | -1.851 | -0.572 | -1.333 | -2.624 | -0.356 |
| 501 | **ARES** | Financials | -1.732 | -1.577 | -1.377 | -1.421 | -1.191 |
| 500 | **KKR** | Financials | -1.569 | -1.923 | -0.778 | -1.376 | -0.753 |
| 499 | **BA** | Industrials | -1.548 | -0.518 | -2.128 | -1.048 | -1.072 |



---

## Mета — навигация и употреба

**Този файл е comprehensive raw data dump за downstream AI агенти (parallel-thinking, deep research, custom workflows).** Не е narrative, не е bullet sheet. Структуриран за machine + human парсване.

### Свързани сателитни артефакти

- **Structured briefing:** `briefings/2026-W46.md` — TLDR + 8 sections, ~10KB
- **Narrative briefing:** `briefings/narrative_2026-W46.md` — БГ prose за weekly-story-teller, ~5KB
- **Backtest reports:** `briefings/backtests/backtest_*.md` — пълни forward returns per canonical query
- **Interactive dashboard:** https://tsvetoslavtsachev.github.io/macro-satellite/
- **Raw archives:** `storage/raw/YYYY-MM-DD/` — оригиналните JSON-и от dashboards

### Регенериране

```
cd C:\Projects\macro\macro-satellite
python -m macro_satellite export-week                      # current week
python -m macro_satellite export-week --week 2026-11-09  # anchor date
```

Регенерира се автоматично при weekly-briefing.yml workflow всеки петък 09:00 София.
