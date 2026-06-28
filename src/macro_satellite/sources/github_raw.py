"""raw.githubusercontent.com fetch helpers."""
from __future__ import annotations

from ..config import GithubSource, github_raw_url
from ..utils.http import fetch_bytes, fetch_many

# Git-LFS pointer magic. Ако upstream файлът е LFS-tracked, raw.githubusercontent.com
# връща ПОКАЗАЛЕЦА (~130 байта текст), не съдържанието — и parser-ът после щеше да
# гръмне с криптично `Expecting value`, заровено в report.failures (зелено CI). Тук
# хващаме сигнатурата на самата граница: ясна, именувана грешка вместо тиха зараза.
# Prefix-проверката е zero-false-positive — никой валиден JSON/MD не започва така.
_LFS_POINTER_MAGIC = b"version https://git-lfs.github.com/spec/v1"


def _assert_real_content(content: bytes, url: str) -> bytes:
    """Fail-loud guard: сваленото да е реално съдържание, не LFS показалец/празнота.

    Cardinal rule в дух: по-добре силен fail, отколкото тих запис на празно в
    каноничния път. НЕ налагаме произволен размерен под (легитимно малък JSON не
    бива да гасне канал) — пазим точните известни „bad" сигнатури:
      • Git-LFS показалец (upstream файлът е LFS-tracked → raw връща pointer);
      • празен/whitespace-only 200 отговор.
    """
    if content.lstrip()[:len(_LFS_POINTER_MAGIC)] == _LFS_POINTER_MAGIC:
        raise ValueError(
            f"fetched a Git-LFS pointer ({len(content)}B), not real content, from "
            f"{url} — upstream file is LFS-tracked and raw.githubusercontent.com "
            f"served the pointer. Resolve via the GitHub blob/contents API (media "
            f"type) or repoint the source at a non-LFS file."
        )
    if not content.strip():
        raise ValueError(f"fetched empty/whitespace-only content from {url}")
    return content


def fetch_latest(src: GithubSource) -> bytes:
    url = github_raw_url(src)
    return _assert_real_content(fetch_bytes(url), url)


def fetch_at_sha(src: GithubSource, sha: str) -> bytes:
    url = github_raw_url(src, sha=sha)
    return _assert_real_content(fetch_bytes(url), url)


def fetch_alt_paths(owner: str, repo: str, ref: str, paths: list[str]) -> dict[str, bytes]:
    """Един SHA, много файлове. Полезно за COT manifest + markets/*.json."""
    urls = [f"https://raw.githubusercontent.com/{owner}/{repo}/{ref}/{p}" for p in paths]
    by_url = fetch_many(urls)
    out: dict[str, bytes] = {}
    for path, url in zip(paths, urls):
        if url in by_url:
            out[path] = by_url[url]
    return out
