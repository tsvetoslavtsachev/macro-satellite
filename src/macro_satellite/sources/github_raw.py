"""raw.githubusercontent.com fetch helpers."""
from __future__ import annotations

from ..config import GithubSource, github_raw_url
from ..utils.http import fetch_bytes, fetch_many


def fetch_latest(src: GithubSource) -> bytes:
    return fetch_bytes(github_raw_url(src))


def fetch_at_sha(src: GithubSource, sha: str) -> bytes:
    return fetch_bytes(github_raw_url(src, sha=sha))


def fetch_alt_paths(owner: str, repo: str, ref: str, paths: list[str]) -> dict[str, bytes]:
    """Един SHA, много файлове. Полезно за COT manifest + markets/*.json."""
    urls = [f"https://raw.githubusercontent.com/{owner}/{repo}/{ref}/{p}" for p in paths]
    by_url = fetch_many(urls)
    out: dict[str, bytes] = {}
    for path, url in zip(paths, urls):
        if url in by_url:
            out[path] = by_url[url]
    return out
