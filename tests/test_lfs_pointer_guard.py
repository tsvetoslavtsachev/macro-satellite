"""Fail-loud guard срещу Git-LFS показалци на fetch границата.

Контекст: ако upstream `output/api/macro_state.json` стане LFS-tracked, raw.
githubusercontent.com връща ~130B ПОКАЗАЛЕЦ вместо JSON. Без guard parser-ът гърми
с криптично `Expecting value`, заровено в report.failures (зелено CI) → каналът тихо
спира да се обновява. Guard-ът хваща сигнатурата на самата граница: ясна, именувана
грешка. (Cardinal rule: по-добре силен fail, отколкото тих запис на празно.)

Offline — без мрежа (monkeypatch на fetch_bytes).
"""
from __future__ import annotations

import pytest

from macro_satellite.collectors.base import FetchError
from macro_satellite.config import DashboardConfig, GithubSource
from macro_satellite.sources import github_raw

_POINTER = (
    b"version https://git-lfs.github.com/spec/v1\n"
    b"oid sha256:16a1bd5a9e28d14ac0cad2d807f9ffd26f6872fb3d6af085a0be8c7384f58933\n"
    b"size 33122\n"
)
_REAL_JSON = b'{\n  "region": "US",\n  "as_of_date": "2026-06-27"\n}'


def test_guard_rejects_lfs_pointer():
    with pytest.raises(ValueError, match="Git-LFS pointer"):
        github_raw._assert_real_content(_POINTER, "https://example/macro_state.json")


def test_guard_rejects_leading_whitespace_pointer():
    # lstrip → показалец, предшестван от newline/space, пак се хваща
    with pytest.raises(ValueError, match="Git-LFS pointer"):
        github_raw._assert_real_content(b"\n  " + _POINTER, "https://example/x.json")


def test_guard_rejects_empty():
    with pytest.raises(ValueError, match="empty"):
        github_raw._assert_real_content(b"   \n\t ", "https://example/x.json")


def test_guard_passes_real_json_unchanged():
    assert github_raw._assert_real_content(_REAL_JSON, "https://example/x.json") is _REAL_JSON


def test_fetch_latest_raises_on_pointer(monkeypatch):
    monkeypatch.setattr(github_raw, "fetch_bytes", lambda url, **kw: _POINTER)
    src = GithubSource(owner="tsvetoslavtsachev", repo="us-macro-dashboard",
                       file="output/api/macro_state.json")
    with pytest.raises(ValueError, match="Git-LFS pointer"):
        github_raw.fetch_latest(src)


def test_collect_one_pointer_is_loud_not_silent(monkeypatch):
    """End-to-end: показалец → FetchError (report.failures), НЕ тих запис на празно."""
    from macro_satellite import runner

    monkeypatch.setattr(github_raw, "fetch_bytes", lambda url, **kw: _POINTER)
    d = DashboardConfig(
        name="us_macro_state", table="us_macro_state",
        github=GithubSource(owner="tsvetoslavtsachev", repo="us-macro-dashboard",
                            file="output/api/macro_state.json"),
        parser="macro_satellite.collectors.macro_state:parse_us", key_cols=[],
    )
    with pytest.raises(FetchError):
        runner._collect_one(d)
