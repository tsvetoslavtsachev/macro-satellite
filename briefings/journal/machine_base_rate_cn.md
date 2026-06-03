```
════════════════════════════════════════════════════════════════════════
  MACHINE BASE RATE [CN] — gap-журнал (Тухла 2a/3б)
════════════════════════════════════════════════════════════════════════
  Прозорец: 2021-06-20 → 2026-06-07 (260 седмици с изчислим gap от 264 генерирани)
  σ_gap=0.4837  τ_open=0.4837  τ_close=0.2418
  σ_economy=0.0429  σ_markets=0.3525
  ЕПИЗОДИ: 26 (censored: 1) — броим епизоди, не записи

  Епизоди (open → close, config, peak gap):
    ep001_2021-W24         2021-06-20 → 2021-06-27 gap_neg  peak=-0.748 (1w)
    ep002_2021-W26         2021-07-04 → 2021-08-15 gap_neg  peak=-0.527 (6w)
    ep003_2021-W39         2021-10-03 → 2021-11-07 gap_pos  peak=+1.255 (5w)
    ep004_2021-W45         2021-11-14 → 2021-11-28 gap_pos  peak=+0.809 (2w)
    ep005_2021-W48         2021-12-05 → 2021-12-12 gap_neg  peak=-0.553 (1w)
    ep006_2021-W49         2021-12-12 → 2021-12-19 gap_pos  peak=+0.523 (1w)
    ep007_2022-W05         2022-02-06 → 2022-02-13 gap_pos  peak=+0.539 (1w)
    ep008_2022-W08         2022-02-27 → 2022-03-06 gap_pos  peak=+0.533 (1w)
    ep009_2022-W11         2022-03-20 → 2022-09-18 gap_pos  peak=+1.009 (26w)
    ep010_2022-W39         2022-10-02 → 2022-10-30 gap_pos  peak=+0.961 (4w)
    ep011_2022-W44         2022-11-06 → 2022-11-27 gap_pos  peak=+0.784 (3w)
    ep012_2022-W48         2022-12-04 → 2023-02-05 gap_pos  peak=+0.739 (9w)
    ep013_2023-W08         2023-02-26 → 2023-03-12 gap_pos  peak=+0.770 (2w)
    ep014_2023-W12         2023-03-26 → 2023-04-02 gap_neg  peak=-0.607 (1w)
    ep015_2023-W27         2023-07-09 → 2023-11-12 gap_pos  peak=+1.315 (18w)
    ep016_2024-W03         2024-01-21 → 2024-02-04 gap_pos  peak=+1.209 (2w)
    ep017_2024-W06         2024-02-11 → 2024-06-16 gap_pos  peak=+1.354 (18w)
    ep018_2024-W39         2024-09-29 → 2025-01-05 gap_pos  peak=+1.576 (14w)
    ep019_2025-W03         2025-01-19 → 2025-03-02 gap_pos  peak=+1.107 (6w)
    ep020_2025-W10         2025-03-09 → 2025-03-16 gap_pos  peak=+0.587 (1w)
    ep021_2025-W20         2025-05-18 → 2025-06-01 gap_pos  peak=+0.502 (2w)
    ep022_2025-W29         2025-07-20 → 2025-08-03 gap_pos  peak=+0.925 (2w)
    ep023_2025-W33         2025-08-17 → 2025-10-12 gap_pos  peak=+1.481 (8w)
    ep024_2025-W49         2025-12-07 → 2026-02-08 gap_pos  peak=+0.919 (9w)
    ep025_2026-W11         2026-03-15 → 2026-04-05 gap_pos  peak=+0.663 (3w)
    ep026_2026-W18         2026-05-03 → ОТВОРЕН    gap_pos  peak=+0.669 (6w)

────────────────────────────────────────────────────────────────────────
  BASE RATE — ПЪЛЕН 2021→
────────────────────────────────────────────────────────────────────────
  config_key = gap_neg
    Y= 4w: n_eps=4 resolved=4 unresolved=0  market_leads=1 (25%) · economy_leads=3 (75%)
    Y= 8w: n_eps=4 resolved=4 unresolved=0  market_leads=2 (50%) · economy_leads=2 (50%)
    Y=13w: n_eps=4 resolved=4 unresolved=0  economy_leads=2 (50%) · meet=1 (25%) · widen=1 (25%)
  config_key = gap_pos
    Y= 4w: n_eps=22 resolved=22 unresolved=0  market_leads=13 (59%) · economy_leads=3 (14%) · meet=2 (9%) · widen=4 (18%)
    Y= 8w: n_eps=22 resolved=21 unresolved=1  market_leads=11 (52%) · economy_leads=5 (24%) · meet=2 (10%) · widen=3 (14%)
    Y=13w: n_eps=22 resolved=20 unresolved=2  market_leads=8 (40%) · economy_leads=3 (15%) · meet=3 (15%) · widen=6 (30%)

────────────────────────────────────────────────────────────────────────
  BASE RATE — POST-REFLATION 2022→
────────────────────────────────────────────────────────────────────────
  config_key = gap_neg
    Y= 4w: n_eps=1 resolved=1 unresolved=0  economy_leads=1 (100%)
    Y= 8w: n_eps=1 resolved=1 unresolved=0  economy_leads=1 (100%)
    Y=13w: n_eps=1 resolved=1 unresolved=0  economy_leads=1 (100%)
  config_key = gap_pos
    Y= 4w: n_eps=19 resolved=19 unresolved=0  market_leads=10 (53%) · economy_leads=3 (16%) · meet=2 (11%) · widen=4 (21%)
    Y= 8w: n_eps=19 resolved=18 unresolved=1  market_leads=10 (56%) · economy_leads=4 (22%) · meet=2 (11%) · widen=2 (11%)
    Y=13w: n_eps=19 resolved=17 unresolved=2  market_leads=6 (35%) · economy_leads=2 (12%) · meet=3 (18%) · widen=6 (35%)

────────────────────────────────────────────────────────────────────────
  RECONCILIATION (caveat #1 quantified): recon − table икон-axis на overlap
────────────────────────────────────────────────────────────────────────
    2026-06-02 2026-W23: table=-0.4708 recon=-0.4708 Δ=+0.0000

────────────────────────────────────────────────────────────────────────
  VELOCITY ASYMMETRY (caveat #3): средно |ΔE| vs |ΔM| per хоризонт
────────────────────────────────────────────────────────────────────────
    Y= 4w: mean|ΔE|=0.057  mean|ΔM|=0.356  M/E=6.2×  → market_leads ларгели механичен
    Y= 8w: mean|ΔE|=0.087  mean|ΔM|=0.420  M/E=4.8×  → market_leads ларгели механичен
    Y=13w: mean|ΔE|=0.121  mean|ΔM|=0.554  M/E=4.6×  → market_leads ларгели механичен

────────────────────────────────────────────────────────────────────────
  ⚠ REVISION/VINTAGE BIAS: backfill чете РЕВИЗИРАН fred_cache + trim по дата-на-наблюдение (вкл. непубликувани-към-X данни) → machine base rate е BEST-CASE (perfect-hindsight), НЕ real-time постижим. Human forward track record (2b) ще е по-реалистичен. Никога не го представяй като real-time edge.

  ⚠ МЕТОДОЛОГИЧНА КОНСИСТЕНТНОСТ: днешната build_macro_state методология + днешните gap_weights ориентации (вкл. stagflation-scoped inflation=-1) приложени назад. За консистентна метрика е feature; но 2021 reflation носи обърнат inflation orient → виж двойния доклад (full vs post-2022).

  ⚠ VELOCITY ASYMMETRY (за честно четене): икономика-оста е структурно БАВНА (месечни макро данни) → движи се много по-малко от пазари-оста за същия хоризонт (виж диагностиката долу). Затова market_leads е ДО ГОЛЯМА СТЕПЕН МЕХАНИЧЕН — бавният икон-крак физически не може да затвори голям gap за седмици. Vol-нормализацията изравнява amplitude-per-σ, НЕ structural velocity. → НЕ чети 'market_leads %' като tradeable edge; информативни са widen-ставките + pos/neg асиметрията. economy_leads (по-рядко) е по-значимо когато се случи.

  Записано: C:\Projects\dashboards\macro-satellite\journal\economy_reconstructed_cn.parquet
            C:\Projects\dashboards\macro-satellite\journal\machine_episodes_cn.parquet
            C:\Projects\dashboards\macro-satellite\journal\gap_series_cn.parquet
════════════════════════════════════════════════════════════════════════
```
