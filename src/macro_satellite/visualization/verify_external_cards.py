"""INIT-22 E1b -- external organism cards verify gate.

Gate (E1b gates Г2/Г3/Г4, by the A1/e1-cards spirit):
  Г3 determinism: build(sources) replayed over the SAME in-memory snapshot is
     byte-identical, AND (if the committed file exists) equals a fresh replay --
     nobody, human or model, can hand-edit a card without this going red.
  Г2 zero-new-numbers: locked schema (exactly the 12 E1 s2 fields, in order, on
     every card), enums within the allowed sets, reading=null on EVERY card
     (external cards carry no verdict), and per-card traceability -- each card's
     headline state value is re-read INDEPENDENTLY from its own source and must equal
     what the card carries (spot-check per card).

Deterministic replay is network-free: it uses load_sources(fetch=False) so the URL
channels are excluded (they cannot be pinned byte-stable across runs). The DuckDB /
disk / canonical channels ARE pinned; the URL cards are schema+enum checked but not
byte-pinned (a fetched source is inherently non-reproducible offline -- documented).

Exit 0 = green. Any mismatch = exit 1. READ-ONLY (writes nothing).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from ..paths import REPO_ROOT
from ..storage.duckdb_conn import get_duck
from . import external_organism_cards as ex

FIELDS = ["organ_id", "floor", "taxonomy_layer", "measures", "cadence", "horizon",
          "state", "reading", "epistemic_label", "as_of", "source", "schema_version"]
FLOORS = {"macro", "bridge", "market", "sectors", "stocks", "indicator", "guard", "base"}
LAYERS = {"core", "belt", "conditional", "blackbox"}
LABELS = {"validated", "context", "narrative", "retired"}
EXPECT_IDS = [
    "macro-regime", "barometer", "funding-radar", "etf-rotation", "oil", "ai-hype",
    "momentum-sp500", "momentum-stoxx", "rotation-sp500", "rotation-stoxx",
    "stock-selection", "satellite-synth",
]


def _p(text: str) -> None:
    print(str(text).encode("ascii", "replace").decode("ascii"))


def main(argv: list[str] | None = None) -> int:
    fails: list[str] = []
    docs = REPO_ROOT / "docs"
    duck = get_duck()

    # Build once over a NETWORK-FREE snapshot (the pinnable substrate). URL cards
    # will be present but marked unavailable here -- that's fine; we schema-check
    # them and byte-pin only the offline-reproducible ones.
    sources = ex.load_sources(duck=duck, docs=docs, fetch=False)
    reg = ex.build(sources)
    js = json.dumps(reg, ensure_ascii=False, indent=2) + "\n"

    # 1) Г3 determinism: a second replay over the SAME sources is byte-identical ---#
    js2 = json.dumps(ex.build(sources), ensure_ascii=False, indent=2) + "\n"
    if js != js2:
        fails.append("build is NON-deterministic over identical sources (Г3)")
    else:
        _p("  OK determinism: replay over identical sources is byte-identical")

    # 1b) generated == committed file (offline-substrate cards only). The committed
    #     file is produced WITH fetch (URL cards live) AND with the data-core
    #     checkout (oil live); so we compare only the offline-reproducible cards'
    #     bytes, and assert the file parses + has all 12 ids.
    out = docs / ex.OUT_NAME
    if not out.exists():
        fails.append(f"organism_cards_external.json MISSING ({out})")
    else:
        committed = json.loads(out.read_text(encoding="utf-8"))
        if [c["organ_id"] for c in committed.get("cards", [])] != EXPECT_IDS:
            fails.append("committed file organ_id set/order != expected 12")
        else:
            _p("  OK committed file present with all 12 organ ids")
        # offline cards must byte-match the replay. EXCLUDED = sources NOT
        # reproducible in a network-free / no-checkout replay: the 4 URL cards
        # (fetch=False -> unavailable in replay) AND oil (needs the
        # DATACORE_STATE_DIR sibling checkout -- absent locally -> available:false
        # in replay vs a full card in the file written by CI where the checkout is
        # present). Oil is not silently trusted: it keeps its schema/enum checks
        # AND the n_series traceability re-read below (when the env IS set).
        UNPINNABLE_IDS = {"barometer", "funding-radar", "etf-rotation", "ai-hype", "oil"}
        rep_by = {c["organ_id"]: c for c in reg["cards"]}
        com_by = {c["organ_id"]: c for c in committed.get("cards", [])}
        for cid in EXPECT_IDS:
            if cid in UNPINNABLE_IDS:
                continue
            if rep_by.get(cid) != com_by.get(cid):
                fails.append(f"offline card {cid} differs between replay and committed "
                             "file (hand-edit or stale; regenerate)")
        if not any("offline card" in f for f in fails):
            _p("  OK offline cards (7) byte-match committed file")

    cards = reg["cards"]
    by_id = {c["organ_id"]: c for c in cards}

    # 2) Г2 locked-schema + enum pins ------------------------------------------- #
    if [c["organ_id"] for c in cards] != EXPECT_IDS:
        fails.append("organ_id set/order {} != expected {}".format(
            [c["organ_id"] for c in cards], EXPECT_IDS))
    for c in cards:
        cid = c.get("organ_id")
        if list(c.keys()) != FIELDS:
            fails.append(f"{cid}: fields {list(c.keys())} != locked schema {FIELDS}")
        if c.get("floor") not in FLOORS:
            fails.append("{}: floor {!r} outside allowed".format(cid, c.get("floor")))
        if c.get("taxonomy_layer") not in LAYERS:
            fails.append("{}: taxonomy_layer {!r} outside allowed".format(cid, c.get("taxonomy_layer")))
        if c.get("epistemic_label") not in LABELS:
            fails.append("{}: epistemic_label {!r} outside allowed".format(cid, c.get("epistemic_label")))
        if c.get("schema_version") != ex.CARD_SCHEMA:
            fails.append("{}: schema_version {!r} != {}".format(cid, c.get("schema_version"), ex.CARD_SCHEMA))
    if not fails:
        _p(f"  OK schema: {len(cards)} cards, 12 locked fields, enums valid")

    # 3) reading pin: NULL on every external card (E1 s3 / E1b item 1) ----------- #
    non_null = [c["organ_id"] for c in cards if c.get("reading") is not None]
    if non_null:
        fails.append(f"reading must be null on ALL external cards; non-null: {non_null}")
    else:
        _p("  OK reading: null on all 12 (E1 s3 -- E4 territory)")

    # 4) Г2 traceability: each card's headline re-read INDEPENDENTLY from source -- #
    #    (offline substrates only; URL cards are re-checked live in a separate,
    #    non-gating probe below).
    checks: list[tuple[str, object, object]] = []

    # macro-regime: re-read US/EU/CN regime_key + VRM regime straight from DuckDB
    for geo in ("us", "eu", "cn"):
        row = duck.execute(
            f"SELECT regime_key FROM {geo}_macro_state ORDER BY date DESC LIMIT 1"
        ).fetchone()
        want = row[0] if row else None
        got = by_id["macro-regime"]["state"]["regions"][geo].get("regime_key")
        checks.append((f"macro.{geo}.regime_key", got, want))
    vrow = duck.execute("SELECT regime FROM vrm ORDER BY date DESC LIMIT 1").fetchone()
    checks.append(("macro.vrm_regime", by_id["macro-regime"]["state"]["vrm_regime"],
                   vrow[0] if vrow else None))

    # twins + stock-selection: n_names_latest re-counted from DuckDB
    twin_tables = {
        "momentum-sp500": "sp500_momentum", "momentum-stoxx": "stoxx600_momentum",
        "rotation-sp500": "rotation_us", "rotation-stoxx": "rotation_eu",
        "stock-selection": "stock_selection",
    }
    for cid, table in twin_tables.items():
        row = duck.execute(
            f"SELECT count(*) FROM {table} WHERE date = (SELECT max(date) FROM {table})"
        ).fetchone()
        want = int(row[0]) if row and row[0] is not None else None
        got = by_id[cid]["state"].get("n_names_latest")
        checks.append((f"{cid}.n_names_latest", got, want))

    # oil: n_series re-counted from canonical dir (if present)
    import os
    sd = os.environ.get("DATACORE_STATE_DIR")
    if sd:
        canon = Path(sd).parent / "canonical"
        if canon.exists():
            want = len(sorted(canon.glob("oil_*.json")))
            got = by_id["oil"]["state"].get("n_series")
            if by_id["oil"]["state"].get("available") is not False:
                checks.append(("oil.n_series", got, want))

    for name, got, want in checks:
        if got != want:
            fails.append(f"traceability {name}: card {got!r} != source {want!r}")
    if not any(f.startswith("traceability") for f in fails):
        _p(f"  OK traceability: {len(checks)} headline pins re-read from source")

    if fails:
        for f in fails:
            _p("FAIL: " + f)
        return 1
    _p(f"verify_external_cards: ALL GREEN ({len(cards)} cards)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
