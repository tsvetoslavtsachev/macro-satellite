```
════════════════════════════════════════════════════════════════════════
  MACHINE BASE RATE [US] — gap-журнал (Тухла 2a/3б)
════════════════════════════════════════════════════════════════════════
  Прозорец: 2021-06-20 → 2026-06-07 (260 седмици с изчислим gap от 264 генерирани)
  σ_gap=0.6328  τ_open=0.6328  τ_close=0.3164
  σ_economy=0.0205  σ_markets=0.3738
  ЕПИЗОДИ: 19 (censored: 1) — броим епизоди, не записи

  Епизоди (open → close, config, peak gap):
    ep001_2021-W44         2021-11-07 → 2021-11-21 gap_pos  peak=+0.735 (2w)
    ep002_2021-W47         2021-11-28 → 2021-12-26 gap_neg  peak=-0.956 (4w)
    ep003_2022-W01         2022-01-09 → 2022-02-27 gap_neg  peak=-0.910 (7w)
    ep004_2022-W19         2022-05-15 → 2022-06-05 gap_neg  peak=-0.652 (3w)
    ep005_2022-W29         2022-07-24 → 2022-09-25 gap_pos  peak=+1.296 (9w)
    ep006_2023-W04         2023-01-29 → 2023-03-19 gap_pos  peak=+1.458 (7w)
    ep007_2023-W20         2023-05-21 → 2023-08-20 gap_pos  peak=+1.522 (13w)
    ep008_2023-W35         2023-09-03 → 2023-09-10 gap_pos  peak=+0.982 (1w)
    ep009_2023-W40         2023-10-08 → 2023-10-15 gap_pos  peak=+1.050 (1w)
    ep010_2023-W44         2023-11-05 → 2024-02-04 gap_pos  peak=+1.287 (13w)
    ep011_2024-W06         2024-02-11 → 2024-03-17 gap_pos  peak=+1.063 (5w)
    ep012_2024-W28         2024-07-14 → 2024-08-04 gap_pos  peak=+1.026 (3w)
    ep013_2024-W37         2024-09-15 → 2025-02-16 gap_pos  peak=+1.290 (22w)
    ep014_2025-W09         2025-03-02 → 2025-04-27 gap_neg  peak=-0.698 (8w)
    ep015_2025-W19         2025-05-11 → 2025-08-03 gap_pos  peak=+1.070 (12w)
    ep016_2025-W33         2025-08-17 → 2025-11-16 gap_pos  peak=+1.172 (13w)
    ep017_2025-W49         2025-12-07 → 2026-01-25 gap_pos  peak=+1.061 (7w)
    ep018_2026-W06         2026-02-08 → 2026-04-05 gap_neg  peak=-0.803 (8w)
    ep019_2026-W16         2026-04-19 → ОТВОРЕН    gap_pos  peak=+0.998 (8w)

────────────────────────────────────────────────────────────────────────
  BASE RATE — ПЪЛЕН 2021→
────────────────────────────────────────────────────────────────────────
  config_key = gap_neg
    Y= 4w: n_eps=5 resolved=5 unresolved=0  market_leads=2 (40%) · economy_leads=1 (20%) · widen=2 (40%)
    Y= 8w: n_eps=5 resolved=5 unresolved=0  economy_leads=2 (40%) · meet=2 (40%) · widen=1 (20%)
    Y=13w: n_eps=5 resolved=5 unresolved=0  economy_leads=2 (40%) · widen=3 (60%)
  config_key = gap_pos
    Y= 4w: n_eps=14 resolved=14 unresolved=0  market_leads=4 (29%) · economy_leads=3 (21%) · meet=1 (7%) · widen=6 (43%)
    Y= 8w: n_eps=14 resolved=13 unresolved=1  market_leads=6 (46%) · economy_leads=2 (15%) · meet=2 (15%) · widen=3 (23%)
    Y=13w: n_eps=14 resolved=13 unresolved=1  market_leads=4 (31%) · economy_leads=4 (31%) · meet=3 (23%) · widen=2 (15%)

────────────────────────────────────────────────────────────────────────
  BASE RATE — POST-REFLATION 2022→
────────────────────────────────────────────────────────────────────────
  config_key = gap_neg
    Y= 4w: n_eps=4 resolved=4 unresolved=0  market_leads=1 (25%) · economy_leads=1 (25%) · widen=2 (50%)
    Y= 8w: n_eps=4 resolved=4 unresolved=0  economy_leads=2 (50%) · meet=2 (50%)
    Y=13w: n_eps=4 resolved=4 unresolved=0  economy_leads=1 (25%) · widen=3 (75%)
  config_key = gap_pos
    Y= 4w: n_eps=13 resolved=13 unresolved=0  market_leads=4 (31%) · economy_leads=3 (23%) · meet=1 (8%) · widen=5 (38%)
    Y= 8w: n_eps=13 resolved=12 unresolved=1  market_leads=5 (42%) · economy_leads=2 (17%) · meet=2 (17%) · widen=3 (25%)
    Y=13w: n_eps=13 resolved=12 unresolved=1  market_leads=4 (33%) · economy_leads=4 (33%) · meet=3 (25%) · widen=1 (8%)

────────────────────────────────────────────────────────────────────────
  RECONCILIATION (caveat #1 quantified): recon − table икон-axis на overlap
────────────────────────────────────────────────────────────────────────
    2026-05-15 2026-W20: table=+0.2150 recon=-0.1620 Δ=-0.3770
    2026-05-16 2026-W20: table=+0.2150 recon=-0.1620 Δ=-0.3770
    2026-05-23 2026-W21: table=+0.1330 recon=-0.1605 Δ=-0.2935
    2026-05-30 2026-W22: table=+0.1730 recon=-0.1580 Δ=-0.3310

────────────────────────────────────────────────────────────────────────
  VELOCITY ASYMMETRY (caveat #3): средно |ΔE| vs |ΔM| per хоризонт
────────────────────────────────────────────────────────────────────────
    Y= 4w: mean|ΔE|=0.031  mean|ΔM|=0.431  M/E=13.9×  → market_leads ларгели механичен
    Y= 8w: mean|ΔE|=0.065  mean|ΔM|=0.577  M/E=8.9×  → market_leads ларгели механичен
    Y=13w: mean|ΔE|=0.070  mean|ΔM|=0.862  M/E=12.3×  → market_leads ларгели механичен

────────────────────────────────────────────────────────────────────────
  ⚠ REVISION/VINTAGE BIAS: backfill чете РЕВИЗИРАН fred_cache + trim по дата-на-наблюдение (вкл. непубликувани-към-X данни) → machine base rate е BEST-CASE (perfect-hindsight), НЕ real-time постижим. Human forward track record (2b) ще е по-реалистичен. Никога не го представяй като real-time edge.

  ⚠ МЕТОДОЛОГИЧНА КОНСИСТЕНТНОСТ: днешната методология (робастен z спрямо 10-г. прозорец + полярност на ниво серия + U-форма за инфлация; orient +1 навсякъде) приложена назад. U-формата прави inflation orient режим-инвариантен (близост до целта = здраве), затова двойният доклад (full vs post-2022) е по-малко чувствителен към 2021 reflation, отколкото при стария stagflation-scoped orient. Виж LENS_SCORING_METHODOLOGY.md.

  ⚠ VELOCITY ASYMMETRY (за честно четене): икономика-оста е структурно БАВНА (месечни макро данни) → движи се много по-малко от пазари-оста за същия хоризонт (виж диагностиката долу). Затова market_leads е ДО ГОЛЯМА СТЕПЕН МЕХАНИЧЕН — бавният икон-крак физически не може да затвори голям gap за седмици. Vol-нормализацията изравнява amplitude-per-σ, НЕ structural velocity. → НЕ чети 'market_leads %' като tradeable edge; информативни са widen-ставките + pos/neg асиметрията. economy_leads (по-рядко) е по-значимо когато се случи.

  Записано: C:\Projects\dashboards\macro-satellite\journal\economy_reconstructed.parquet
            C:\Projects\dashboards\macro-satellite\journal\machine_episodes.parquet
            C:\Projects\dashboards\macro-satellite\journal\gap_series.parquet
════════════════════════════════════════════════════════════════════════
```
