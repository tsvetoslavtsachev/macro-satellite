# -*- coding: utf-8 -*-
"""Retro cleanup of etf_prices (mandate #32 FINAL, 2026-07-14) -- one-off, deterministic.

Ц. каза „чисти": финалът на мандат #32. Двете исторически замърсявания, замразени в
сателитния parquet от преди фикса (mandate #32-B), се лекуват НАЗАД с ЕДИН детерминистичен
скрипт (никаква ръчна операция, никакви числа от ръка -- само архивни стойности през кода):

OPERATION 1 -- PHANTOM DELETE. Изтрива баровете на непазарни дни (наследство от пенсионирания
``etf_dashboard`` колектор, който стемпваше ``updatedAt.date()`` без сесийна проверка).
Летвата е новият ``utils.market_calendar``. АСЕРТ срещу описа от диагнозата (Фаза Б):
точно 213 реда на точно 3-те дати -- 2026-04-11 (събота, 40) · 2026-05-25 (Memorial Day, 85)
· 2026-06-19 (Juneteenth, 88). ВСЯКО разминаване (освен „вече чисто" = 0 фантома, за
идемпотентния втори пуск) -> СТОП без нито един запис.

OPERATION 2 -- RAW-CLOSE RE-ANCHOR. За ВСЕКИ оцелял ред, за който price-archive има суров
close за (символ, дата) -- цената се презаписва с архивния RAW close (сплит-коригиран, НЕ
дивидент-коригиран). Това реанкерира и старите yfinance редове (bootstrap-нати с adj_close),
и data-core джоба (value_tr), към единната RAW конвенция на mandate #32-B. Редове без архивно
покритие (сателитните-only символи DFEN/EFA/VEA/IBIT/ASHR + дати извън архива) остават
непипнати и се броят в доклада. Архивът е READ-ONLY: четем през ``datacore.archive.read``
(дедуп по последен ``recorded_on`` -- семантиката по подразбиране на read), преизползвайки
``base_first._raw_close_map`` -- същият код-път като живия колектор, нула дублирана логика.

ИДЕМПОТЕНТНОСТ: втори пуск намира 0 фантома и 0 ценови разлики -> 0 записа (git-чисто).
ДЕТЕРМИНИЗЪМ: партициите се пренаписват само ако са пипнати, със сорт [date, symbol] и
zstd -- byte-конвенцията на ``parquet_writer.upsert``. Само ``price`` се променя; source /
ingested_at / всички други колони остават байт-за-байт (одитната следа се пази).

ПУСК (локално, от корена на репото):
    .venv/Scripts/python.exe -m macro_satellite.backfill.retro_cleanup_m32 [--dry-run]

Локална топология: collectors + data-core checkout-ите и price-archive се резолвват като в
живия колектор (PYTHONPATH / DATACORE_ROOT), с documented fallback към C:\\Projects layout-а.
"""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# ── Описът от диагнозата (Фаза Б, 2026-07-14) -- КОТВАТА на operation 1 ──────────────
# Пълен скан на etf_prices през market_calendar намери ТОЧНО тези фантомни барове.
# Скриптът отказва да изтрие каквото и да е друго: намереното множество трябва да е
# РАВНО на този опис (първи пуск) или ПРАЗНО (втори пуск / вече чисто).
EXPECTED_PHANTOMS: dict[date, int] = {
    date(2026, 4, 11): 40,    # събота -- etf_dashboard_git
    date(2026, 5, 25): 85,    # Memorial Day -- etf_dashboard_live
    date(2026, 6, 19): 88,    # Juneteenth -- etf_dashboard_live
}
EXPECTED_TOTAL = 213

TABLE = "etf_prices"
SORT_KEYS = ["date", "symbol"]           # byte-конвенцията на parquet_writer.upsert

# Локален layout fallback (същите чекаути, които живият колектор ползва през PYTHONPATH).
_LOCAL_COLLECTORS = Path(r"C:\Projects\collectors")
_LOCAL_DATACORE = Path(r"C:\Projects\data-core")
_LOCAL_ARCHIVE = Path(r"C:\Projects\price-archive")


def _wire_archive_imports() -> None:
    """collectors.price.consumer + datacore да са importable (CI: PYTHONPATH; локално: fallback)."""
    for mod, local in (("collectors", _LOCAL_COLLECTORS), ("datacore", _LOCAL_DATACORE)):
        try:
            __import__(mod)
        except ImportError:
            if local.exists():
                sys.path.insert(0, str(local))
            __import__(mod)   # втори опит; истинска липса -> честен ImportError (ремонтът СПИРА)


def _resolve_archive_root() -> str:
    """DATACORE_ROOT env -> локалния price-archive checkout. Ремонт БЕЗ архив няма (hard stop)."""
    import os
    root = os.environ.get("DATACORE_ROOT")
    if root and Path(root).exists():
        return root
    if _LOCAL_ARCHIVE.exists():
        return str(_LOCAL_ARCHIVE)
    raise SystemExit("STOP: price-archive не е достъпен (нито DATACORE_ROOT, нито "
                     f"{_LOCAL_ARCHIVE}) -- ре-анкер без архив е забранен.")


def _partition_files() -> list[Path]:
    from macro_satellite.paths import parquet_table_dir
    return sorted(parquet_table_dir(TABLE).glob("year=*/month=*/data.parquet"))


def _load(path: Path, schema: pa.Schema) -> pd.DataFrame:
    return pq.read_table(path, schema=schema).to_pandas()


def main(argv: list[str] | None = None) -> int:
    try:  # Windows конзолна кирилица
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="M32 retro cleanup на etf_prices (phantom delete + raw re-anchor)")
    ap.add_argument("--dry-run", action="store_true", help="само доклад, нула записи")
    args = ap.parse_args(argv)

    from macro_satellite.storage.schema import get_schema
    from macro_satellite.utils.market_calendar import is_us_trading_day

    schema = get_schema(TABLE)
    files = _partition_files()
    if not files:
        raise SystemExit(f"STOP: няма партиции за {TABLE}")

    # ── PASS 0: пълен скан -- фантомният опис трябва да съвпадне ТОЧНО (или да е празен) ──
    parts: dict[Path, pd.DataFrame] = {p: _load(p, schema) for p in files}
    found: dict[date, int] = {}
    for df in parts.values():
        for d, n in df.loc[~df["date"].map(is_us_trading_day), "date"].value_counts().items():
            found[d] = found.get(d, 0) + int(n)

    already_clean = not found
    if not already_clean and found != EXPECTED_PHANTOMS:
        print("STOP: фантомният скан НЕ съвпада с описа от диагнозата -- нито един запис не е направен.")
        print(f"  очаквано: { {str(k): v for k, v in EXPECTED_PHANTOMS.items()} } (общо {EXPECTED_TOTAL})")
        print(f"  намерено: { {str(k): v for k, v in sorted(found.items())} } (общо {sum(found.values())})")
        return 2
    assert already_clean or sum(found.values()) == EXPECTED_TOTAL

    # ── Архивният RAW close (READ-ONLY; дедуп по последен recorded_on -- archive.read) ──
    _wire_archive_imports()
    from collectors.price import consumer

    from macro_satellite.backfill.base_first import _raw_close_map
    root = _resolve_archive_root()
    all_symbols = sorted({s for df in parts.values() for s in df["symbol"].dropna().unique()})
    raw = _raw_close_map(consumer, all_symbols, root)
    if not raw:
        raise SystemExit("STOP: архивното четене върна 0 серии -- ре-анкерът е невъзможен, нула записи.")

    # ── PASS 1: partition по partition -- изтриване + ре-анкер, запис само ако е пипнат ──
    deleted_by_date: dict[date, int] = {}
    changed_by_src: dict[str, int] = {}
    covered_unchanged = 0
    uncovered = 0
    touched_files: list[Path] = []

    for path, df in parts.items():
        dirty = False

        # 1) phantom delete
        mask_phantom = ~df["date"].map(is_us_trading_day)
        if mask_phantom.any():
            for d, n in df.loc[mask_phantom, "date"].value_counts().items():
                deleted_by_date[d] = deleted_by_date.get(d, 0) + int(n)
            df = df.loc[~mask_phantom].copy()
            dirty = True

        # 2) raw-close re-anchor
        new_price = [
            raw.get(s, {}).get(d) for s, d in zip(df["symbol"], df["date"], strict=True)
        ]
        for i, (old, new) in enumerate(zip(df["price"], new_price, strict=True)):
            if new is None:
                uncovered += 1
            elif pd.isna(old) or float(old) != float(new):
                src = str(df["source"].iloc[i]).split("@")[0]
                changed_by_src[src] = changed_by_src.get(src, 0) + 1
            else:
                covered_unchanged += 1
        col = df["price"].copy()
        upd = pd.Series(new_price, index=df.index, dtype="float64")
        repl = upd.notna() & (col.isna() | (col != upd))
        if repl.any():
            col.loc[repl] = upd.loc[repl]
            df = df.assign(price=col)
            dirty = True

        if dirty and not args.dry_run:
            out = df.sort_values(by=SORT_KEYS).reset_index(drop=True)
            tbl = pa.Table.from_pandas(out, schema=schema, preserve_index=False)
            pq.write_table(tbl, path, compression="zstd")
        if dirty:
            touched_files.append(path)

    # ── Счетоводството ──
    n_deleted = sum(deleted_by_date.values())
    n_changed = sum(changed_by_src.values())
    print("── M32 RETRO CLEANUP · счетоводна таблица ──────────────────────────")
    print(f"  режим:                        {'DRY-RUN (нула записи)' if args.dry_run else 'LIVE'}")
    print(f"  1· изтрити фантомни редове:   {n_deleted}"
          + (f"  {[f'{d}: {n}' for d, n in sorted(deleted_by_date.items())]}" if deleted_by_date else "  (вече чисто)"))
    print(f"  2· пресорсвани към RAW close: {n_changed}")
    for src, n in sorted(changed_by_src.items()):
        print(f"       - {src}: {n}")
    print(f"     покрити, вече RAW (0 промяна): {covered_unchanged}")
    print(f"     БЕЗ архивно покритие (остават): {uncovered}")
    print(f"  пипнати партиции:             {len(touched_files)}")
    print("────────────────────────────────────────────────────────────────────")
    if already_clean and n_changed == 0:
        print("ИДЕМПОТЕНТЕН ПУСК: нищо за правене -- 0 записа.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
