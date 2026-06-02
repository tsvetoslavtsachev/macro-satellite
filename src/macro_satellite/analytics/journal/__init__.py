"""Журнал на присъдите — Phase 6, Тухла 2 (синтез-слой).

Тухла 2a (тази итерация) = МАШИННАТА половина:
  economy_reconstruct → episodes → attribution → store → backfill → machine base rate.

Присъда = залог за КОЙ КРАК ще затвори даден gap-епизод до хоризонт Y. В 2a няма
човешки залог още; машината класифицира историческите gap-епизоди в 4 изхода
(vol-нормализиран attribution): market_leads · economy_leads · meet · widen.

⚠ Два caveat-а важат за всеки machine base rate оттук (виж `backfill.CAVEATS`):
  1. REVISION/VINTAGE BIAS — backfill чете ревизиран fred_cache → best-case, НЕ real-time.
  2. МЕТОДОЛОГИЧНА КОНСИСТЕНТНОСТ — днешната методология приложена назад (counterfactual).

НЕ е в 2a: човешки orchestrator вход, resolution loop, VRM, калибрационно четене (= 2b).
"""
