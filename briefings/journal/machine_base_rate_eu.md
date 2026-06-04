```
════════════════════════════════════════════════════════════════════════
  MACHINE BASE RATE [EU] — gap-журнал (Тухла 2a/3б)
════════════════════════════════════════════════════════════════════════
  Прозорец: 2021-06-20 → 2026-06-07 (260 седмици с изчислим gap от 264 генерирани)
  σ_gap=0.7588  τ_open=0.7588  τ_close=0.3794
  σ_economy=0.0221  σ_markets=0.4030
  ЕПИЗОДИ: 22 (censored: 1) — броим епизоди, не записи

  Епизоди (open → close, config, peak gap):
    ep001_2021-W24         2021-06-20 → 2021-06-27 gap_neg  peak=-1.273 (1w)
    ep002_2021-W26         2021-07-04 → 2021-09-19 gap_neg  peak=-1.249 (11w)
    ep003_2021-W41         2021-10-17 → 2021-11-07 gap_neg  peak=-0.978 (3w)
    ep004_2021-W47         2021-11-28 → 2022-01-09 gap_neg  peak=-1.139 (6w)
    ep005_2022-W08         2022-02-27 → 2022-04-17 gap_neg  peak=-1.143 (7w)
    ep006_2022-W21         2022-05-29 → 2022-06-26 gap_pos  peak=+1.036 (4w)
    ep007_2022-W36         2022-09-11 → 2023-03-19 gap_pos  peak=+1.406 (27w)
    ep008_2023-W13         2023-04-02 → 2023-04-23 gap_pos  peak=+1.061 (3w)
    ep009_2023-W20         2023-05-21 → 2023-08-27 gap_pos  peak=+1.395 (14w)
    ep010_2023-W45         2023-11-12 → 2023-12-17 gap_pos  peak=+1.149 (5w)
    ep011_2024-W06         2024-02-11 → 2024-05-05 gap_pos  peak=+1.214 (12w)
    ep012_2024-W24         2024-06-16 → 2024-06-30 gap_neg  peak=-0.759 (2w)
    ep013_2024-W31         2024-08-04 → 2024-08-25 gap_neg  peak=-0.815 (3w)
    ep014_2024-W38         2024-09-22 → 2025-03-02 gap_pos  peak=+1.133 (23w)
    ep015_2025-W10         2025-03-09 → 2025-03-30 gap_pos  peak=+1.054 (3w)
    ep016_2025-W15         2025-04-13 → 2025-06-15 gap_pos  peak=+1.022 (9w)
    ep017_2025-W26         2025-06-29 → 2025-07-27 gap_pos  peak=+0.839 (4w)
    ep018_2025-W31         2025-08-03 → 2025-08-10 gap_neg  peak=-0.811 (1w)
    ep019_2025-W34         2025-08-24 → 2025-09-28 gap_neg  peak=-0.974 (5w)
    ep020_2025-W50         2025-12-14 → 2025-12-21 gap_pos  peak=+0.776 (1w)
    ep021_2026-W05         2026-02-01 → 2026-04-12 gap_neg  peak=-0.880 (10w)
    ep022_2026-W18         2026-05-03 → ОТВОРЕН    gap_pos  peak=+1.055 (6w)

────────────────────────────────────────────────────────────────────────
  BASE RATE — ПЪЛЕН 2021→
────────────────────────────────────────────────────────────────────────
  config_key = gap_neg
    Y= 4w: n_eps=10 resolved=10 unresolved=0  market_leads=5 (50%) · economy_leads=4 (40%) · meet=1 (10%)
    Y= 8w: n_eps=10 resolved=10 unresolved=0  market_leads=3 (30%) · economy_leads=4 (40%) · meet=1 (10%) · widen=2 (20%)
    Y=13w: n_eps=10 resolved=10 unresolved=0  market_leads=3 (30%) · economy_leads=2 (20%) · meet=3 (30%) · widen=2 (20%)
  config_key = gap_pos
    Y= 4w: n_eps=12 resolved=12 unresolved=0  market_leads=3 (25%) · meet=2 (17%) · widen=7 (58%)
    Y= 8w: n_eps=12 resolved=11 unresolved=1  market_leads=3 (27%) · economy_leads=2 (18%) · widen=6 (55%)
    Y=13w: n_eps=12 resolved=11 unresolved=1  market_leads=3 (27%) · economy_leads=2 (18%) · meet=1 (9%) · widen=5 (45%)

────────────────────────────────────────────────────────────────────────
  BASE RATE — POST-REFLATION 2022→
────────────────────────────────────────────────────────────────────────
  config_key = gap_neg
    Y= 4w: n_eps=6 resolved=6 unresolved=0  market_leads=4 (67%) · economy_leads=2 (33%)
    Y= 8w: n_eps=6 resolved=6 unresolved=0  market_leads=2 (33%) · economy_leads=2 (33%) · meet=1 (17%) · widen=1 (17%)
    Y=13w: n_eps=6 resolved=6 unresolved=0  market_leads=2 (33%) · economy_leads=2 (33%) · meet=1 (17%) · widen=1 (17%)
  config_key = gap_pos
    Y= 4w: n_eps=12 resolved=12 unresolved=0  market_leads=3 (25%) · meet=2 (17%) · widen=7 (58%)
    Y= 8w: n_eps=12 resolved=11 unresolved=1  market_leads=3 (27%) · economy_leads=2 (18%) · widen=6 (55%)
    Y=13w: n_eps=12 resolved=11 unresolved=1  market_leads=3 (27%) · economy_leads=2 (18%) · meet=1 (9%) · widen=5 (45%)

────────────────────────────────────────────────────────────────────────
  RECONCILIATION (caveat #1 quantified): recon − table икон-axis на overlap
────────────────────────────────────────────────────────────────────────
    2026-05-16 2026-W20: table=-0.4720 recon=-0.1130 Δ=+0.3590
    2026-05-23 2026-W21: table=-0.3470 recon=-0.1135 Δ=+0.2335
    2026-05-30 2026-W22: table=-0.2360 recon=-0.1145 Δ=+0.1215

────────────────────────────────────────────────────────────────────────
  VELOCITY ASYMMETRY (caveat #3): средно |ΔE| vs |ΔM| per хоризонт
────────────────────────────────────────────────────────────────────────
    Y= 4w: mean|ΔE|=0.040  mean|ΔM|=0.483  M/E=12.1×  → market_leads ларгели механичен
    Y= 8w: mean|ΔE|=0.051  mean|ΔM|=0.634  M/E=12.4×  → market_leads ларгели механичен
    Y=13w: mean|ΔE|=0.056  mean|ΔM|=0.742  M/E=13.3×  → market_leads ларгели механичен

────────────────────────────────────────────────────────────────────────
  ⚠ REVISION/VINTAGE BIAS: backfill чете РЕВИЗИРАН fred_cache + trim по дата-на-наблюдение (вкл. непубликувани-към-X данни) → machine base rate е BEST-CASE (perfect-hindsight), НЕ real-time постижим. Human forward track record (2b) ще е по-реалистичен. Никога не го представяй като real-time edge.

  ⚠ МЕТОДОЛОГИЧНА КОНСИСТЕНТНОСТ: днешната методология (робастен z спрямо 10-г. прозорец + полярност на ниво серия + U-форма за инфлация; orient +1 навсякъде) приложена назад. U-формата прави inflation orient режим-инвариантен (близост до целта = здраве), затова двойният доклад (full vs post-2022) е по-малко чувствителен към 2021 reflation, отколкото при стария stagflation-scoped orient. Виж LENS_SCORING_METHODOLOGY.md.

  ⚠ VELOCITY ASYMMETRY (за честно четене): икономика-оста е структурно БАВНА (месечни макро данни) → движи се много по-малко от пазари-оста за същия хоризонт (виж диагностиката долу). Затова market_leads е ДО ГОЛЯМА СТЕПЕН МЕХАНИЧЕН — бавният икон-крак физически не може да затвори голям gap за седмици. Vol-нормализацията изравнява amplitude-per-σ, НЕ structural velocity. → НЕ чети 'market_leads %' като tradeable edge; информативни са widen-ставките + pos/neg асиметрията. economy_leads (по-рядко) е по-значимо когато се случи.

  Записано: C:\Projects\dashboards\macro-satellite\journal\economy_reconstructed_eu.parquet
            C:\Projects\dashboards\macro-satellite\journal\machine_episodes_eu.parquet
            C:\Projects\dashboards\macro-satellite\journal\gap_series_eu.parquet
════════════════════════════════════════════════════════════════════════
```
