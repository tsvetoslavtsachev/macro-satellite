"""HTTP client за GitHub raw + API. Sync + async с retry.

Auth: ако env var GITHUB_TOKEN е set → Authorization Bearer. Иначе anonymous.
"""
from __future__ import annotations

import asyncio
import os
from typing import Any

import httpx

DEFAULT_TIMEOUT = 30.0
MAX_RETRIES = 3
RETRY_BACKOFF = 1.5


def _headers() -> dict[str, str]:
    h = {"User-Agent": "macro-satellite/0.1.0", "Accept": "application/json"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("DASHBOARDS_READ_PAT")
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def fetch_bytes(url: str, timeout: float = DEFAULT_TIMEOUT) -> bytes:
    last_err: Exception | None = None
    for attempt in range(MAX_RETRIES):
        try:
            r = httpx.get(url, headers=_headers(), timeout=timeout,
                          follow_redirects=True)
            if r.status_code == 404:
                raise FileNotFoundError(f"404 from {url}")
            r.raise_for_status()
            return r.content
        except (httpx.TimeoutException, httpx.HTTPError) as e:
            last_err = e
            if attempt < MAX_RETRIES - 1:
                import time
                time.sleep(RETRY_BACKOFF ** attempt)
                continue
            raise
    raise RuntimeError(f"Unreachable, last_err={last_err}")


def fetch_json(url: str, timeout: float = DEFAULT_TIMEOUT) -> Any:
    import json
    return json.loads(fetch_bytes(url, timeout=timeout))


def fetch_json_api(url: str, timeout: float = DEFAULT_TIMEOUT) -> Any:
    """Като fetch_json, но с GitHub API headers (Accept: vnd.github+json)."""
    h = _headers()
    h["Accept"] = "application/vnd.github+json"
    h["X-GitHub-Api-Version"] = "2022-11-28"
    last_err: Exception | None = None
    for attempt in range(MAX_RETRIES):
        try:
            r = httpx.get(url, headers=h, timeout=timeout, follow_redirects=True)
            r.raise_for_status()
            return r.json()
        except (httpx.TimeoutException, httpx.HTTPError) as e:
            last_err = e
            if attempt < MAX_RETRIES - 1:
                import time
                time.sleep(RETRY_BACKOFF ** attempt)
                continue
            raise
    raise RuntimeError(f"Unreachable, last_err={last_err}")


async def _afetch_one(client: httpx.AsyncClient, url: str,
                      sem: asyncio.Semaphore) -> tuple[str, bytes]:
    async with sem:
        for attempt in range(MAX_RETRIES):
            try:
                r = await client.get(url, headers=_headers(),
                                     timeout=DEFAULT_TIMEOUT,
                                     follow_redirects=True)
                if r.status_code == 404:
                    raise FileNotFoundError(f"404 from {url}")
                r.raise_for_status()
                return url, r.content
            except (httpx.TimeoutException, httpx.HTTPError):
                if attempt < MAX_RETRIES - 1:
                    await asyncio.sleep(RETRY_BACKOFF ** attempt)
                    continue
                raise
    raise RuntimeError("unreachable")


async def afetch_many(urls: list[str], concurrency: int = 10) -> dict[str, bytes]:
    sem = asyncio.Semaphore(concurrency)
    async with httpx.AsyncClient() as client:
        tasks = [_afetch_one(client, u, sem) for u in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    out: dict[str, bytes] = {}
    for r in results:
        if isinstance(r, BaseException):
            continue
        url, content = r
        out[url] = content
    return out


def fetch_many(urls: list[str], concurrency: int = 10) -> dict[str, bytes]:
    return asyncio.run(afetch_many(urls, concurrency=concurrency))
