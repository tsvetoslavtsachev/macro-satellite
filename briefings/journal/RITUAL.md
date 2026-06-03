# Gap-журнал — седмичен ритуал (Тухла 2b)

> Как се пълни човешката половина на gap-журнала. Дисциплината идва от РИТУАЛА, не от cron —
> затова е човешки + локален + седмичен, закачен за съботния VRM рутин (vrm-orchestrator Ф2).

## Защо ЛОКАЛЕН (не CI cron)

- `journal-backfill` ползва cross-repo bridge към `us-macro-dashboard` (fred_cache) → нужни са
  двата репо-та локално. (Автоматизирани в CI са само `daily-collect` + `weekly-briefing`.)
- `journal-judge` иска ЧОВЕШКИ залог → не може да се cron-ва.

## Седмичният цикъл (събота, след VRM Ф2)

```
1. journal-backfill   # refresh gap_series + епизоди с новата седмица
                      # (резолюциите узряват САМО ако серията расте)
2. journal-prep       # worksheet JOURNAL_WEEK.md: отворени епизоди + VRM снимка + дължими резолюции
3. ПРИСЪДА или ABSTAIN # попълваш ПРИСЪДА блок(ове) за отворен епизод, ИЛИ съзнателно пропускаш
4. journal-judge      # валидира (C3 raise при липсващ критерий) + append + разрешава дължимите
5. journal-calibrate  # machine base rate vs human track (реални числа чак при n≥3 на кош)
```

Команди (PYTHONUTF8=1 + .venv): `python -m macro_satellite <стъпка> --region US`

## Дисциплина (за честен track record)

- **ABSTAIN е позволен, но СЪЗНАТЕЛЕН.** Не си длъжен да залагаш всяка седмица — но пропускът да
  е избор, не cherry-picking. Track record-ът е честен само ако не подбираш седмиците (C3 анти-селекция).
- **Критерий — конкретен и machine-adjacent.** Без `falsification_criterion` → `journal-judge` ГРЪМВА.
  Дай праг (напр. „опровергано ако на 8w gap още > +0.4 И пазар-ос не е паднала ≥0.3").
- **Хоризонт — при несигурност, заложи и трите (4/8/13w).** Timing-ът се разрешава емпирично; всеки
  хоризонт е отделен запис, но калибрацията брои ЕПИЗОДИ, не записи.
- **Залогът е на ИНФОРМАТИВНАТА ос.** Не market_leads % (ларгели механичен — velocity asymmetry), а
  close-vs-widen · редкия economy_leads · timing. Там добавяш стойност над прайора.

## Записи

- `journal/human_judgments.jsonl` + `human_resolutions.jsonl` — **append-only, git-tracked** (одит трейл).
  Commit-вай ги (data-commit, както daily-collect). Никога не редактирай минал запис тихо.
- `journal/JOURNAL_WEEK.md` — **транзиентен worksheet** (gitignore-нат; регенерира се всеки prep).

## Пътят към Тухла 3а

Натрупваш присъди forward → при **n≥3 епизода на кош** калибрацията дава реални human-vs-prior числа →
тогава Тухла 3а (йерархичен shrinkage + регим-aware inflation orient) става смислена. Дотогава 3а чака.

## Първа присъда (референция)

2026-06-03 — ep030 (gap_pos, gap +0.56): close/market_leads @4/8/13w, high confidence
(AI ротация надолу, катализатор Иран сделка + нефт; falsifier: инфлация→заплати = widen). Commit `e371a43`.
