# VRM_WEEK — Текуща Седмица
> **⚠️ ЕДИНСТВЕНИЯТ АВТОРИТЕТЕН ФАЙЛ ЗА ТЕКУЩИ ЧИСЛА**
> Актуализира се след Ф2 checkpoint всяка седмица (събота).
> Скиловете четат ОТТУК за текущи метрики.
> `VRM_STATE.md` е за KS протокол, история и pending решения — не за текущи числа.

**Последна актуализация:** 2026-04-25
**Седмица:** 2026-04-25 → 2026-05-01
**Одобрено от Цветослав:** ДА (Ф2 checkpoint 2026-04-25 — обновена диагноза)

---

## 🔢 VRM ЯДРО

```
РЕЖИМ:            REFLATION
РЕЖИМ_БГ:         РЕФЛАЦИЯ
СИГНАЛ:           ЗАЩИТИ (KS активен)
ALIGNMENT:        6.0
ALIGNMENT_MAX:    8
ALIGNMENT_LABEL:  УМЕРЕН-ЧИСТ
GMS_SCORE:        3
GMS_MAX:          8
GMS_LABEL:        MEDIUM
```

**Класификация на сигнала:** 6/8 = УМЕРЕН-ЧИСТ (не оспорван формално, но двойствен по същество — REFLATION модел / STAGFLATION макро underlay)
*(KS остава активен — режимната алокация е игнорирана, важат KS тегла. GMS падна 7→3 — GLD/TLT_3M обърна негатив, но при активен KS GMS е override.)*

---

## 🔴 KILL SWITCH

```
KS_АКТИВЕН:                  ДА
KS_ОТ:                       2026-03-28
KS_ВАРИАНТ:                  A
KS_ПОРТФЕЙЛ:                 TLT 60% / GLD 30% / IEF 10%
KS_EU_ПОРТФЕЙЛ:              IDTL 60% / IGLN 30% / IBTM 10%
KS_СЕДМИЦИ_АКТИВЕН:          4.0
KS_ДЕАКТИВИРАНЕ_НЕ_ПРЕДИ:    2026-05-09
KS_ЦЕНОВО_УСЛОВИЕ:           ✅ SPY 4W = +12.09% (над прага -3.0%)
KS_ВРЕМЕВО_УСЛОВИЕ:          ❌ 4.0 / 6 седмици минимум
KS_TLT_TIP_SPREAD:           -0.68% (Вариант A потвърден — праг за B: < -1.0%; буфер 0.32 пп)
KS_RE_ENTRY_NOTE:            При деактивиране: SPY 4W > +5% → условен 1-стъпков ре-вход (100% REFLATION)
```

---

## 📊 GAP АНАЛИЗ — 4W Реални Данни

```
SPY_4W:     +12.09%
QQQ_4W:     +16.94%
XLE_4W:     -9.20%
GLD_4W:     +4.52%
TLT_4W:     +1.25%
TIP_4W:     +1.93%
IWM_4W:     +13.21%
EEM_SPY_3M: +0.040
TLT_TIP_SPREAD: -0.68%
VIX:        18.71
MOVE:       66.97
HY_SPREAD:  2.85%
YIELD_CURVE_10Y2Y: +0.521%
```

**Ключови наблюдения от Ф2 (25.04.2026) — обновени с COT корекция от Цветослав:**
- SPY/QQQ ралито продължава (+12.09% / +16.94%) — НЕ short squeeze. COT показва институционално купуване от началото на април; хедж фондовете УВЕЛИЧАВАТ shorts (smart money long, fast money short divergence).
- РЕЖИМЕН CAVEAT: Моделът чете REFLATION (бизнес климат + retail sales силни); макро реалността показва STAGFLATION (CPI 3.3% YoY, gasoline +21.2%, oil shock, Initial claims 207K, заплати +z2.24). Двата наратива съществуват едновременно.
- XLE -9.20% ❌ продължава да отслабва — demand destruction страх + HF stagflation хедж дори при oil +17% седмично от Iran/Hormuz война.
- GLD +4.52% (от +7.68% преди седмица, -3.16pp) — силен USD пробива; институционалното злато се изтегли. Първи седмичен спад от 5 седмици.
- VIX 18.71 (от пик 35 в средата на март) | MOVE 66.97 (от пик 116 в април) → стрес индикаторите ДРАСТИЧНО надолу, пазарите абсорбират геополитиката.
- HY Spread 2.85% близо до историческите минимуми → кредитът е напълно risk-on, не сигнализира риск.
- TLT-TIP spread обърна от +0.30% на -0.68% (буфер до Вариант B праг -1.0%: 0.32 пп) — реалните доходности по-малко атрактивни от номиналните; следи внимателно.
- EARNINGS SEASON (пропуснат фактор от моя първоначален анализ): Компаниите засега НЕ говорят за рецесия; намаленията на печалбите НЕ са драстични. Tech earnings предстоят (последна седмица април / първа седмица май) → потенциален catalyst за нов leg up.
- FOMC 28-29 април: очакван hold, hawkish тон; oil shock измества рейт кът към късен 2026.

---

## 📈 ETF КАРТА

*Попълва се ръчно от ETF Dashboard всяка събота.*

```
ETF_TOP1_TICKER:  EWY
ETF_TOP1_NAME:    iShares MSCI South Korea
ETF_TOP1_SCORE:   100.0
ETF_TOP1_1M:      +19.1%

ETF_TOP2_TICKER:  SOXX
ETF_TOP2_NAME:    iShares Semiconductor
ETF_TOP2_SCORE:   98.8
ETF_TOP2_1M:      +24.7%

ETF_TOP3_TICKER:  DFEN
ETF_TOP3_NAME:    Direxion Daily Aerospace 3x
ETF_TOP3_SCORE:   97.6
ETF_TOP3_1M:      +8.8%

ETF_BOT1_TICKER:  INDA
ETF_BOT1_NAME:    iShares MSCI India
ETF_BOT1_SCORE:   3.5
ETF_BOT1_1M:      +8.3%

ETF_BOT2_TICKER:  FXY
ETF_BOT2_NAME:    CurrencyShares Japanese Yen
ETF_BOT2_SCORE:   2.4
ETF_BOT2_1M:      +0.4%

ETF_BOT3_TICKER:  VIXY
ETF_BOT3_NAME:    ProShares VIX Short-Term
ETF_BOT3_SCORE:   1.2
ETF_BOT3_1M:      -18.6%

ETF_MAX_DRAWDOWN_LEADER:  SHY (iShares 1-3Y Treasury, -1.0%)
ETF_SHARPE_LEADER:        EWY (5.73)
ETF_LOW_VOL:              EMB (6.75% vol)
ETF_SECTOR_BIAS:          Thematic (avgRS=82.7)
```

---

## 🔗 INTERMARKET КОРЕЛАЦИИ

*Попълва се ръчно от ETF Dashboard (30-day rolling vs SPY).*

```
CORR_SPY_TLT:  +0.48  (c30) / +0.28 (c90)
CORR_SPY_GLD:  +0.49  (c30) / +0.25 (c90)
CORR_SPY_USO:  -0.67  (c30) / -0.45 (c90)
CORR_SPY_UUP:  -0.67  (c30) / -0.34 (c90)
CORR_SPY_EEM:  +0.90  (c30) / +0.79 (c90)
CORR_SPY_HYG:  +0.86  (c30) / +0.80 (c90)
```

---

## 🏦 COT ПОЗИЦИОНИРАНЕ

*Данни от: cot_snapshot.json (dashboard repo weekly-refresh). Report date: 2026-04-14.*

```
COT_REPORT_DATE:     2026-04-14
COT_SUMMARY:         4 LONG / 7 SHORT / 0 NEUTRAL
COT_MOST_SHORT:      NASDAQ (5.1-ти персентил)
COT_MOST_LONG:       CORN (89.1-ви персентил)
```

**S&P 500 (TFF):**
```
SP500_CTA_DIRECTION:   НЕТНО SHORT
SP500_CTA_PERCENTILE:  18.6  (траектория: 4.5 → 92.9 на 2026-03-31 → 91.0 на 2026-04-07 → 18.6 на 2026-04-14. Покритието беше DURING пада; от 31 март CTA добавят нови shorts)
SP500_CTA_NET:         -420,356 контракта (-21.46% от OI)
SP500_AM_DIRECTION:    НЕТНО LONG
SP500_AM_PERCENTILE:   89.7
SP500_AM_NET:          +1,003,143 контракта
SP500_OI:              1,959,076
```

**NASDAQ (TFF):**
```
NASDAQ_CTA_DIRECTION:  НЕТНО SHORT
NASDAQ_CTA_PERCENTILE: 4.5  (MAX SHORT 3-годишен — непокрит, потенциален squeeze setup)
NASDAQ_CTA_NET:        -58,892 контракта (-21.30% от OI)
NASDAQ_AM_DIRECTION:   НЕТНО LONG
NASDAQ_AM_PERCENTILE:  63.5
```

**US10Y (TFF):**
```
US10Y_CTA_DIRECTION:   НЕТНО SHORT
US10Y_CTA_PERCENTILE:  25.0
US10Y_CTA_NET:         -2,009,971 контракта (-38.75% от OI)
US10Y_AM_DIRECTION:    НЕТНО LONG
US10Y_AM_PERCENTILE:   91.0  (екстремно дълго, институционална ставка на rate cuts / рецесия — пикнал 92.3 на 2026-04-07)
```

**Валути:**
```
EURFX_CTA:   НЕТНО LONG, 80.8 пс (crowded long EUR)
GBPFX_CTA:   НЕТНО LONG, 24.4 пс
DXY_CTA:     НЕТНО SHORT, 41.7 пс
```

**Стоки (Disagg):**
```
GOLD_CTA:    НЕТНО LONG, 19.9 пс (не е претрупан)
WTI_CTA:     НЕТНО SHORT, 30.1 пс | Commercials +147,152 (bullish setup)
CORN_CTA:    НЕТНО LONG, 89.1 пс (претрупан) | Commercials -447,998
```

**Крипто:**
```
BITCOIN_CTA: НЕТНО SHORT, 68.6 пс
BITCOIN_AM:  НЕТНО LONG, 2.6 пс (институционалните изоставиха крипто)
```

```
COT_COMMENT: |
  Ралито +9.3% на SPY НЕ е CTA short squeeze. Реалното CTA покритие беше по-рано:
  4.5 → 92.9 пс. между 24 фев и 31 март (DURING пада — класическо покритие).
  След 31 март CTA добавят НОВИ shorts и падат 92.9 → 18.6 пс (фейдват ралито):
  -175,873 нови short контракта за седмицата 2026-04-14.
  Реалният драйвер на ралито е Asset Manager re-entry: SP500 AM 40→89 пс, NASDAQ
  AM 13→63 пс за 3 седмици (механично Q1-end rebalancing на пенсионни/insurance mandates).
  Двете страни на институционалните се разминават: AM купуват equity по mandate +
  купуват 10Y duration при 91 пс (рецесия/rate cuts хедж); CTA са скептични.
  NASDAQ CTA остават 4.5 пс — непокрит crowded short, setup за потенциален squeeze
  при продължаване на цените през earnings (TXN сря, ASML чет).
  Crowded trade-ове за watch: CORN long 89pc, EUR long 81pc, BITCOIN AM изоставен 2.6pc.
```

---

## 📊 MOMENTUM — S&P 500 TOP 5

*Данни от: momentumrank_sp500_all_2026-04-17.xlsx*

```
SP500_DATE:  2026-04-17

SP500_TOP1:  SNDK|Sandisk|Technology|96.1|+2939%|+143%|+43%
SP500_TOP2:  CIEN|Ciena Corp.|Technology|96.0|+701%|+99%|+38%
SP500_TOP3:  LITE|Lumentum|Technology|96.0|+1466%|+151%|+37%
SP500_TOP4:  GLW|Corning Inc.|Technology|95.9|+321%|+97%|+34%
SP500_TOP5:  WDC|Western Digital|Technology|95.9|+955%|+73%|+35%
```

*Формат: TICKER|Компания|Сектор|Score|12M%|3M%|1M%*

**Наблюдение:** Топ 5 са изцяло Technology — AI инфраструктура (оптика, storage, fiber).

---

## 📊 MOMENTUM — STOXX 600 TOP 5

*Данни от: stoxx600_momentumrank_all_2026-04-17.xlsx (уникални)*

```
STOXX_DATE:  2026-04-17

STOXX_TOP1:  ACS.MC|ACS Group|Industrials|Spain|92.8|+150%|+34%|+18%
STOXX_TOP2:  NOKIA.HE|Nokia|Technology|Finland|92.4|+106%|+57%|+22%
STOXX_TOP3:  ENI.MI|Eni|Energy|Italy|92.2|+117%|+45%|+9%
STOXX_TOP4:  AIXA.DE|AIXTRON|Technology|Germany|91.7|+265%|+76%|+9%
STOXX_TOP5:  MEL.MC|Meliá Hotels|Consumer Cyclical|Spain|90.8|+81%|+40%|+28%
```

*Формат: TICKER|Компания|Сектор|Страна|Score|12M%|3M%|1M%*

---

## ✍️ СЕДМИЧЕН ИЗВОД

```
ИЗВОД: |
  Ралито +12.09% на SPY за 4 седмици НЕ е short squeeze. COT данните показват
  институционално купуване от началото на април; хедж фондовете УВЕЛИЧАВАТ shorts
  (smart money long, fast money short divergence). Това е реално институционално bid,
  не техническо покритие. Хипотезата от 18.04 за "изчерпано squeeze гориво" отпада.
  Earnings season е краткосрочен tailwind: компаниите засега НЕ говорят за рецесия;
  намаленията на печалбите НЕ са драстични. Tech earnings (последна седмица април /
  първа седмица май) могат да бъдат catalyst за нов leg up.
  Режимна двойственост: VRM показва REFLATION (модел чете силни бизнес климат + retail
  sales); макро реалността показва STAGFLATION (CPI 3.3% YoY, gasoline +21.2%, oil
  shock, Initial claims 207K, заплати +z2.24, M2 +z2.77). Това НЕ е оспорван режим
  по дефиниция — alignment е 6/8. Това е ОГРАНИЧЕНИЕ на лещата: моделът хваща
  силните страни на growth-а, пропуска инфлационния натиск.
  Stress indicators отслабват драстично: VIX от пик 35 → 18.7; MOVE от пик 116 → 67.
  Пазарите абсорбират геополитиката; HY spreads на исторически минимуми. XLE -9.20%
  при oil +17% = HF stagflation хедж + demand destruction страх; GLD -3.16pp за
  седмицата = силен USD пробива.
  Kill Switch активен (Епизод 8, 4.0/6 седмици) до минимум 9 май. Парадокс: KS защита
  докато пазарът върви нагоре +12% — приема се като цена на дисциплината. Re-entry
  план готов: при деакт. на 9 май, ако SPY 4W > +5% → 1-стъпков 100% REFLATION.
  Ключов risk event: FOMC 28-29 април (hawkish тон + oil shock = stagflation pricing).
```

---

## 📋 ИНСТРУКЦИИ ЗА СКИЛОВЕТЕ

### Как да четете този файл

Полетата в `code блокове` са структурирани key:value.
Стойностите в `[квадратни скоби]` = незапълнени placeholders → питай Цветослав или попълни от дашборда.
Стойностите без скоби = реални, одобрени данни.

### Кой попълва какво

| Поле | Кой попълва | Кога |
|------|-------------|------|
| VRM Ядро (режим, alignment, GMS) | Оркестраторът след Ф2 | Събота сутринта |
| Kill Switch | Оркестраторът след Ф1 | Събота сутринта |
| GAP Анализ 4W | Оркестраторът след Ф1 | Събота сутринта |
| ETF Карта + Intermarket | Ръчно от Цветослав | Събота (ETF Dashboard) |
| COT | Ръчно от Цветослав | Петък след 22:00 |
| Momentum | Оркестраторът или Цветослав | Excel файловете са налични |
| Седмичен Извод | Ръчно от Цветослав | Събота при запис на видео |

### Кой чете откъде

| Скил / Изход | Чете VRM_WEEK.md | Чете VRM_STATE.md |
|--------------|------------------|-------------------|
| vrm-signal-t0 | ✅ Числа (режим, KS, дати) | ❌ Не |
| vrm-snapshot-t2 | ✅ Числа + KS детайли | ❌ Само при съмнение за KS протокол |
| pazaren-puls | ✅ KS статус + alignment | ✅ KS протокол контекст |
| vrm-orchestrator | ✅ Записва тук след Ф2 | ✅ Чете за history |
| Пазарен Радар (презентация) | ✅ Всичко | ❌ Не |

---

## 🔄 ИСТОРИЯ НА ОБНОВЯВАНИЯТА

| Дата | Кой | Какво |
|------|-----|-------|
| 2026-04-17 | Claude (Cowork) | Файлът е създаден. Попълнени: VRM Ядро (4.0/8 УМЕРЕН), KS статус, Momentum данни от Excel. Оставени placeholder: ETF, Intermarket, COT, Извод. |
| 2026-04-17 | Claude (Cowork) | Попълнени ETF Карта (Top: EWY/USO/SOXX; Bot: INDA/FXY/VIXY) и Intermarket корелации от etfs.json (дата 2026-04-16). Оставен placeholder: COT, Извод. |
| 2026-04-20 | Claude (Cowork) | COT секция попълнена със свежи данни (report date 2026-04-14, dashboard repo). Ключова промяна: SP500 CTA 91→19 пс. short. ИЗВОД обновен с интегриран анализ: рали + позициониране + макро стагфлация (briefing_2026-04-20.html). Подготовка за Пазарен Радар 2026-04-21 (пилотно начало-на-седмица видео). |
| 2026-04-21 | Claude (Cowork) | ETF секция синхронизирана с etf_snapshot.json (2026-04-20). Ключови промени: TOP2 смяна USO→SOXX, TOP3 смяна SOXX→DFEN; USO 1М +3.4%→+0.37%; EWY 1М +19.1%→+19.1%; SOXX 1М +20%→+24.7%; Sharpe лидер 5.59→5.73. Корелации актуализирани (SPY/GLD +0.42→+0.49). Пазарен Радар HTML обновен. |
| 2026-04-24 | Claude (Cowork) | **КОРЕКЦИЯ на COT интерпретацията** — предишната версия погрешно твърдеше, че ралито +9.3% е CTA short squeeze (91→19 пс покритие). Реалната картина: покритието беше 4.5→92.9 DURING пада (24 фев–31 март); след това CTA добавят нови shorts и падат 92.9→18.6 (фейдват ралито). Реален драйвер на ралито: Asset Manager re-entry (SP500 AM 40→89, NASDAQ AM 13→63 пс). Обновени: SP500_CTA_PERCENTILE 19.2→18.6, NASDAQ_CTA_PERCENTILE 5.1→4.5, US10Y_CTA_PERCENTILE 25.6→25.0, US10Y_AM_PERCENTILE 91.7→91.0. COT_COMMENT и ИЗВОД пренаписани. Одобрено от Цветослав. |
| 2026-04-25 | Claude (Cowork) | **Ф2 checkpoint седмица 25.04** — обновени числа: SPY 4W +9.32→+12.09, QQQ +11.27→+16.94, XLE -7.08→-9.20, GLD +7.68→+4.52, TLT-TIP +0.30→-0.68, GMS 7→3. KS остава активен (4.0/6 седмици, мин. 9 май). Цветослав корекции (одобрени): (1) Ралито НЕ е squeeze — институционално купуване от април + HF увеличават shorts; (2) Двойственост REFLATION модел / STAGFLATION макро — модел пропуска инфлационния натиск; (3) Earnings season tailwind — компаниите не говорят рецесия, tech отчети предстоят; (4) Вариант A потвърден. Ключови наблюдения и ИЗВОД пренаписани. |
