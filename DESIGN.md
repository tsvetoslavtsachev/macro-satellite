# Handoff — Аналитичен Сателит (нов проект)

> **Цел на този документ:** Самостоятелен контекст за нов чат, в който започва архитектура и proof-of-concept на голям нов проект — система за събиране, съхранение и анализ на динамика от всички dashboards на Цветослав Цачев (ELANA Trading).

---

## Контекст и философия

**Кой:** Цветослав Цачев, инвестиционен анализатор в ELANA Trading. Прави седмични видеа за широка аудитория и за платени Members.

**Текущ проблем:**
Цветослав има 10+ dashboards, всеки от които дава **snapshot към момента** (текущо състояние). Когато седне в петък/събота да подготви видеото, той вижда само "къде сме сега". Не вижда:
- Какво се промени за тази седмица в сравнение с предишната
- Кое е необичайно в сравнение с предишните 12 седмици
- Каква е траекторията на ключови сектори за 1-3-6 месеца
- Как се променя моделното класифициране във времето

**Цветослав го описа така:** *"От погледа в храстите отиваме в космоса. Трябва ни невероятна оптика на нашия сателит."*

**Импулсът за проекта** дойде в седмицата 11-15 май 2026, когато беше открит огромен пазарен ход (петрол +10%, defense -8%, gold -3%, uranium -11%, dollar +1.3%, yields на 4.60%), който НЕ се вижда в S&P 500 графиката (S&P направи нов исторически връх). Тази промяна беше открита само защото локалното копие на ETF dashboard не беше синхронизирано — Цветослав видя 7 май, после git pull, после 15 май. Сравнението показа драматична картина.

**Цел:** Това да не е случайност. Да го виждаме редовно. Автоматично.

---

## Какво представлява "Сателитът"

Система от 5 слоя, която:

1. **Събира** данни всеки ден от всички dashboards
2. **Съхранява** historical snapshots с time-series индексация
3. **Открива** значими промени между snapshots (delta engine)
4. **Отговаря** на въпроси за динамика през времето (query interface)
5. **Разказва** обобщена картина за седмица/месец (narrative briefing)

---

## Източници на данни (всички dashboards)

| Dashboard | Локация | Формат | Какво има |
|---|---|---|---|
| **VRM State** | `C:\Users\tsach\Downloads\VRM2\VRM_STATE.md` | Markdown | Режим, KS статус, alignment score, GMS |
| **VRM Week** | `C:\Users\tsach\Downloads\VRM2\VRM_WEEK.md` | Markdown | Седмични числа |
| **US Macro** | `C:\Projects\dashboards\us-macro-dashboard\output\briefing_context_YYYY-MM-DD.md` | Markdown | Themes, breadth, cross-lens, anomalies (\|z\|>2) |
| **EU Macro** | `C:\Projects\dashboards\eu-macro-dashboard\output\briefing_context_YYYY-MM-DD.md` | Markdown | EA macro themes, anomalies |
| **ETF Dashboard** | `C:\Projects\dashboards\ETF-Dashboard\data\etfs.json` | JSON | ~50 ETF — price, returns (1M/3M/6M/12M/YTD), volatility, sharpe, RS score, flows |
| **SP500 Rotation Radar** | `C:\Projects\dashboards\SP500-rotationradar\docs\data.json` | JSON | Stable winners, quality dips, faded bounces, по 1M и 3M; trajectory история за всяка акция |
| **STOXX600 Rotation Radar** | `C:\Projects\dashboards\STOXX600-rotationradar\` | JSON | EU rotation radar |
| **SP500 Momentum Rank** | `C:\Projects\dashboards\SP500-momentumrank\` | (трябва да се провери) | ~500 US акции по momentum |
| **STOXX600 Momentum Rank** | `C:\Projects\dashboards\stoxx600-momentumrank\` | (трябва да се провери) | ~600 EU акции |
| **COT/CTA Dashboard** | `C:\Projects\dashboards\cot-cta-positioning-dashboard\` | JSON | Asset managers vs hedge funds positions, percentiles |
| **Stock Selection** | `C:\Projects\dashboards\stock-selection-dashboard\` | (трябва да се провери) | Trend/Quality/Value/Risk factor scores |
| **COT Monitor** | `C:\Projects\dashboards\cot-monitor\` | (трябва да се провери) | COT alerts |

**Всички dashboards имат git хранилища** — github.com/tsvetoslavtsachev/...

---

## КРИТИЧНИ принципи на архитектурата

### 1. Запазвай **цените**, не само returns

**Защо:** Returns са lagged windows. Когато сравняваш `return1m` на два snapshot-а от различни дати, получаваш разлика в base-effected стойности, не истинския interval ход.

**Конкретен пример (грешка, която беше направена на 15 май 2026):**
- USO `return1m` на 7 май = +6.3% (база 7 април)
- USO `return1m` на 15 май = +27.7% (база 15 април — локално дъно)
- Разликата +21.4 pp изглежда като "взрив за 8 дни"
- Реално: цена 7 май = 134.97, цена 15 май = 148.23 → **истинският 8-дневен ход е +9.8%**

**Правило:** Сателитът съхранява цените. Изчислява интервални промени `(price_B / price_A) - 1`, не разлики в lagged returns.

### 2. Time-series, не snapshot

Всяка серия се съхранява като time-indexed дата → стойност. Така може:
- *"Покажи ми USO price за последните 3 месеца"*
- *"Кога за последно XLE беше под 50?"*
- *"Каква е корелацията на USO с UUP за последните 6 месеца?"*

### 3. Daily granularity, weekly aggregation

- Daily snapshots — за прецизни интервални анализи
- Weekly aggregates — за по-стабилни тренд анализи (по-малко шум)
- Monthly aggregates — за structural shifts

### 4. Откриване на аномалии, не само записване

Сателитът не е архив. Той активно открива:
- Промени \|z\|>2 в стандартизирани стойности
- Rotation events (актив влиза/излиза от quadrant)
- Regime changes (модел сочи различно)
- Корелационни прекъсвания

---

## Архитектура — 5 слоя

### Слой 1 — Daily Collector

**Какво прави:**
- Всяка вечер (22:30-23:00 София) изпълнява `git pull` на всички dashboard repos
- Чете output файловете
- Записва дневен snapshot в storage

**Имплементация:**
- Bash / Python скрипт
- Стартиран от Windows Task Scheduler или GitHub Action
- Логва успех/грешка в `logs/collector_YYYY-MM-DD.log`

**Output:**
```
storage/
├── raw/
│   ├── YYYY-MM-DD/
│   │   ├── etfs.json
│   │   ├── sp500_rotation.json
│   │   ├── vrm_state.md
│   │   ├── us_macro_briefing.md
│   │   └── ...
```

### Слой 2 — Storage

**Структура:**
- **Raw archive** — оригиналните snapshot файлове по дата
- **Time-series database** — Parquet/SQLite за structured data
  - Една таблица за ETF prices/returns (long format: date, symbol, price, return1m, ..., rs_score, ...)
  - Една таблица за rotation rankings (date, symbol, current_rank, abs_strength, mom_12_1, delta_1m, delta_3m, quadrant_1m, quadrant_3m)
  - Една таблица за VRM state (date, regime, alignment, gms, ks_status, ...)
  - Една таблица за macro themes (date, theme, breadth_up, anomalies_count, ...)
- **Markdown archive** — за briefings и narrative state

**Технологии:**
- Parquet (compact, columnar) или SQLite (queryable, simple)
- DuckDB за query interface
- pandas за анализ

### Слой 3 — Delta Engine

**Какво прави:**
Сравнява snapshots и открива:

- **Price/return moves** — `(price_B / price_A) - 1` за интервал
- **Rotation events** — акция, която влезе/излезе от stable_winners за интервал
- **Regime shifts** — VRM режим се промени, alignment score падна с >1 точка
- **Anomaly emergence** — нова серия с \|z\|>2 в US/EU macro
- **Correlation breakdowns** — двойки серии, които се движат различно от историческото
- **Cross-asset divergences** — петрол нагоре + defense надолу + индекс нагоре (текущ пример)

**Output:**
```
deltas/
├── daily/
│   └── YYYY-MM-DD_vs_prev.json    # промени от вчера
├── weekly/
│   └── YYYY-WW.json                # седмични промени
├── monthly/
│   └── YYYY-MM.json                # месечни промени
```

### Слой 4 — Query Interface

**Какво прави:**
Естествено-езикови въпроси върху time-series:

- *"Какво се промени тази седмица?"*
- *"Кои ETF преобърнаха посока за 8 дни?"*
- *"Кога за последно sticky CPI беше под 2.5%?"*
- *"Покажи ми динамиката на defense vs oil за 3 месеца"*
- *"Кои сектори се появиха като stable winners за първи път през последния месец?"*

**Имплементация:**
- DuckDB SQL queries върху Parquet файлове
- Wrapper на Python който прави SQL от естествен език
- Или директно chat → SQL → данни → формат

### Слой 5 — Narrative Briefing

**Какво прави:**
Седмично/месечно генерира markdown документ, който събира всички delta открития в narrative форма. Готов вход за `weekly-story-teller` скила.

**Шаблон:**
```markdown
# Сателитен брифинг — седмица YYYY-WW

## Какво се промени за тази седмица
- Топ rotation events
- Aномалии в US/EU macro
- VRM regime shifts (ако има)
- Cross-asset divergences

## Какво е необичайно за последните 12 седмици
- Серии в нови екстреми
- Регресии към средното
- Откъсвания от исторически паралели

## Исторически паралели
- Кога преди това е имало подобна комбинация
- Какво е последвало

## Open questions за разказа
- Какво трябва да се провери ръчно
- Кои хипотези не могат да се валидират автоматично
```

**Свързване с `weekly-story-teller`:**
Когато сателитът е готов, активацията на скила става:
```
"weekly story от сателита за [дата]"
```
И скилът чете автоматично подготвения брифинг, без потребителят да предоставя sources.

---

## Фази на изграждане

### Фаза 1 — Architecture + Proof-of-Concept (1 чат)

**Deliverable:**
- Design doc (структура, схеми, технологии)
- Работещ daily collector за 2-3 dashboards (ETF, SP500 Rotation, VRM)
- Storage схема (Parquet или SQLite)
- Минимален delta engine — *"какво се промени между ден A и ден B"*
- Тест на real data за периода 7-15 май 2026 (където знаем че имаше голяма промяна)

**Acceptance test:**
Сателитът трябва да открие автоматично:
- USO +9.8% за 8 дни (не +21pp lagged return)
- XLE +6.2%
- DFEN -8%, URA -11%
- GLD -3.3%, TLT -2.3%
- UUP +1.3%

### Фаза 2 — Пълен Collector + Delta Engine (1 чат)

- Добавяне на всички dashboards
- Weekly + monthly aggregates
- Rotation event detection
- Anomaly emergence tracking
- Cross-asset divergence detection
- Алармен механизъм (notify когато се случи рядко събитие)

### Фаза 3 — Query Interface + Narrative Briefing (1 чат)

- DuckDB query layer
- Natural language → SQL
- Markdown narrative briefing generator
- Свързване с `weekly-story-teller` скила

### Фаза 4 — Backtest Interface (1 чат)

- *"Кога в историята е имало подобна комбинация (10Y 4.60 + петрол 100 + S&P на връх)?"*
- *"Какво е последвало в следващите 1/3/6 месеца?"*
- Backtest на хипотези от minute видеата

### Фаза 5 — Visualization (по желание, 1 чат)

- HTML dashboard за сателита
- Time-series графики
- Cross-asset heatmaps
- Делта alerts табло

---

## Open Questions за първия чат

### Технологически избори

1. **Storage:** Parquet или SQLite? (Препоръка: започни с Parquet — по-бързо, по-малки файлове, лесно с pandas/DuckDB)
2. **Scheduler:** Windows Task Scheduler или GitHub Action? (Препоръка: Windows Task Scheduler за начало, по-късно мигриране към GHA ако има стойност)
3. **Език:** Python (стандартен за data work) или нещо друго? (Препоръка: Python с pandas, DuckDB, pyarrow)
4. **Дължина на history:** колко назад да започне backfill-ът? (Препоръка: погледни git history на dashboards — има ли последни 3-6 месеца snapshots в git log?)

### Скоп на Фаза 1

5. **Кои 2-3 dashboards в Фаза 1?** Препоръка: ETF Dashboard + SP500 Rotation Radar + VRM_STATE (трите най-сготови JSON-и).
6. **Какви интервали в Делта Engine?** Препоръка: 1-ден, 7-дни, 30-дни.
7. **Какви аномалии?** Препоръка: \|интервален ход\| > исторически median + 1σ.

### Свързване

8. **Къде живее сателитът — отделен repo или в Cowork plugin?** Препоръка: отделен repo `C:\Projects\dashboards\macro-satellite\` за модулярност.
9. **Кога влиза в production?** Препоръка: Фаза 1 готова за 1-2 седмици, тогава тест на ръчни седмични видеа за месец, после Фаза 2.

---

## Първа стъпка в новия чат

1. Прочети този handoff
2. Прочети `C:\Projects\dashboards\projects-overview\` (ако има подобен документ) — за да разбереш текущите dashboards
3. Направи git log на 2-3 от dashboards-ите — да видиш каква history е достъпна
4. Питай Цветослав:
   - Готов ли е за Фаза 1 архитектура сега, или предпочита първо да обсъдим scope?
   - Има ли technical constraints (Python version, OS, наличие на disk space)?
   - Колко агресивно искаме автоматизация на старта vs ръчни git pull-ове?
5. Започни с design doc — `C:\Projects\dashboards\macro-satellite\DESIGN.md`

---

## Свързани файлове

- **Handoff за разказа тази седмица:** `C:\Users\tsach\Downloads\VRM2\Handoffs\handoff_razkaz_2026-05-17.md`
- **Скил weekly-story-teller:** `C:\Users\tsach\.claude\skills\weekly-story-teller\SKILL.md`
- **VRM_STATE:** `C:\Users\tsach\Downloads\VRM2\VRM_STATE.md`
- **Текущи dashboards root:** `C:\Projects\dashboards\`

---

## Дългосрочна визия

Сателитът е **дългосрочна инвестиция**. Целта не е да автоматизира всичко за един месец, а да изгради инфраструктура, която след 6 месеца:

- Дава автоматичен седмичен брифинг с динамика
- Открива rare events (като 8-дневния обрат от 7-15 май)
- Дава исторически контекст за всеки текущ ход
- Захранва weekly-story-teller с готов вход
- Захранва Members анализите с по-дълбоки конкретики
- Дава база за backtest на хипотези

**Това, което Цветослав каза:** *"От погледа в храстите отиваме в космоса. Трябва ни невероятна оптика на нашия сателит."*

Не бързаме. Правим го правилно от началото.
