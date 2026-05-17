"""Markdown → HTML за briefing hero блок.

Заместител на грозния `<pre>` + html.escape подход. Парсва narrative_*.md +
{label}.md и извлича конкретни секции като чист HTML.
"""
from __future__ import annotations

import re
from pathlib import Path

from markdown_it import MarkdownIt

_md = MarkdownIt("commonmark", {"html": False, "linkify": True, "breaks": False})
_md.enable("table")


def render_markdown(md_text: str) -> str:
    """Чист markdown → HTML conversion (CommonMark + GFM tables)."""
    return _md.render(md_text)


def extract_section(md_text: str, heading_pattern: str) -> str | None:
    """Извлича цялата ## секция чието заглавие matches heading_pattern (regex).

    Връща markdown текста от заглавието до следващото ## или края на файла. None
    ако не съвпадне нищо.
    """
    pat = re.compile(rf"^##\s+{heading_pattern}\s*$", re.MULTILINE)
    m = pat.search(md_text)
    if not m:
        return None
    start = m.start()
    # Find next ## (но не ###) после този match
    rest = md_text[m.end():]
    next_m = re.search(r"^##\s+", rest, re.MULTILINE)
    if next_m:
        return md_text[start:m.end() + next_m.start()].rstrip()
    return md_text[start:].rstrip()


def render_briefing_hero(narrative_path: Path | None,
                          structured_path: Path | None) -> str:
    """Чете двата briefing файла и връща HTML за hero блока.

    Layout:
    - TL;DR (от structured `## TL;DR`)
    - Теза + конкретни условия (от narrative `## 🎯 Тезата на седмицата`)

    Ако някой файл липсва — gracefully изпуска секцията.
    """
    parts: list[str] = []

    if structured_path and structured_path.exists():
        text = structured_path.read_text(encoding="utf-8")
        tldr_md = extract_section(text, r"TL;DR")
        if tldr_md:
            parts.append('<div class="briefing-tldr">')
            parts.append(render_markdown(tldr_md))
            parts.append('</div>')

    if narrative_path and narrative_path.exists():
        text = narrative_path.read_text(encoding="utf-8")
        thesis_md = extract_section(text, r"🎯\s*Тезата на седмицата")
        if thesis_md:
            parts.append('<div class="briefing-thesis">')
            parts.append(render_markdown(thesis_md))
            parts.append('</div>')

    if not parts:
        return ('<p class="hint">Briefing файловете все още не са генерирани за '
                'тази седмица. Стартирай <code>python -m macro_satellite briefing</code> '
                'и <code>python -m macro_satellite narrative</code>.</p>')

    return "\n".join(parts)


def render_briefing_full_link_block(narrative_path: Path | None,
                                     structured_path: Path | None,
                                     week_label: str) -> str:
    """Малък блок с линкове към пълните briefing файлове."""
    links: list[str] = []
    base = "https://github.com/tsvetoslavtsachev/macro-satellite/blob/main/briefings"
    if narrative_path and narrative_path.exists():
        links.append(
            f'<a class="link-external" href="{base}/narrative_{week_label}.md">'
            f'📋 Целият narrative briefing</a>'
        )
    if structured_path and structured_path.exists():
        links.append(
            f'<a class="link-external" href="{base}/{week_label}.md">'
            f'📊 Структуриран briefing (всички числа)</a>'
        )
    if not links:
        return ""
    return '<div class="briefing-links">' + " · ".join(links) + "</div>"
