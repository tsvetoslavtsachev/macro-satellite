"""Tests за visualization.md_renderer — markdown → HTML за briefing hero."""
from __future__ import annotations

from macro_satellite.visualization.md_renderer import (
    extract_section,
    render_briefing_hero,
    render_markdown,
)


SAMPLE_NARRATIVE = """# Сателитен Разказ — Седмица 2026-W20

_Период: 2026-05-11 → 2026-05-17_

## 🎯 Тезата на седмицата

**Стагфлационна дивергенция**

Триггерирана е канонична **Стагфлационна дивергенция** — съвпадат **5/5** условия:

- USO +11.0%
- DFEN -8.9%

---

## 📊 Какво се случи

Друг текст.
"""

SAMPLE_STRUCTURED = """# Сателитен Обзор — Седмица 2026-W20

## TL;DR
- 🔔 Триггерирани patterns: Стагфлационна дивергенция
- 📈 Топ движение: TIP -0.7% (-2.55σ)

---

## ETF движения
по-надолу
"""


def test_render_markdown_basic():
    html = render_markdown("**bold** text")
    assert "<strong>bold</strong>" in html


def test_render_markdown_table():
    html = render_markdown("| A | B |\n|---|---|\n| 1 | 2 |\n")
    assert "<table>" in html
    assert "<th>A</th>" in html


def test_extract_section_tldr():
    md = extract_section(SAMPLE_STRUCTURED, r"TL;DR")
    assert md is not None
    assert "Триггерирани patterns" in md
    assert "Топ движение" in md
    # Не трябва да включва следваща ## секция
    assert "ETF движения" not in md


def test_extract_section_emoji_heading():
    md = extract_section(SAMPLE_NARRATIVE, r"🎯\s*Тезата на седмицата")
    assert md is not None
    assert "5/5" in md
    # Не трябва да хваща следваща ##
    assert "Какво се случи" not in md


def test_extract_section_not_found():
    md = extract_section(SAMPLE_STRUCTURED, r"NonExistent")
    assert md is None


def test_render_briefing_hero_falls_back_when_files_missing(tmp_path):
    missing_narrative = tmp_path / "narrative_missing.md"
    missing_structured = tmp_path / "missing.md"
    html = render_briefing_hero(missing_narrative, missing_structured)
    assert "не са генерирани" in html or "still" in html.lower() or "macro_satellite" in html


def test_render_briefing_hero_renders_both_files(tmp_path):
    n_path = tmp_path / "narrative_W20.md"
    s_path = tmp_path / "W20.md"
    n_path.write_text(SAMPLE_NARRATIVE, encoding="utf-8")
    s_path.write_text(SAMPLE_STRUCTURED, encoding="utf-8")
    html = render_briefing_hero(n_path, s_path)
    # TL;DR present
    assert "Триггерирани patterns" in html or "TL;DR" in html
    # Thesis present
    assert "Стагфлационна дивергенция" in html
    # No <pre> tag — markdown трябва да е истински HTML
    assert "<pre>" not in html
    # Tables, lists, bold trябва да са истински tags
    assert "<ul>" in html or "<li>" in html
