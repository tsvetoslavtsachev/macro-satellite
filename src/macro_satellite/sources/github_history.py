"""GitHub API за commit history на конкретен файл.

GET /repos/{owner}/{repo}/commits?path=...&since=...&until=...&per_page=100
Anonymous: 60 req/hour. Authenticated (GITHUB_TOKEN): 5000 req/hour.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime

from ..config import GithubSource
from ..utils.dates import date_to_iso, parse_iso_datetime
from ..utils.http import fetch_json_api


@dataclass(frozen=True)
class CommitRef:
    sha: str
    committed_at: datetime  # UTC

    @property
    def date_utc(self) -> date:
        return self.committed_at.date()

    @property
    def short_sha(self) -> str:
        return self.sha[:8]


def list_file_commits(src: GithubSource,
                      since: date | None = None,
                      until: date | None = None,
                      max_pages: int = 10) -> list[CommitRef]:
    """Връща commits на конкретен файл, най-новите първи."""
    base = f"https://api.github.com/repos/{src.owner}/{src.repo}/commits"
    params = [f"path={src.file}", "per_page=100", f"sha={src.branch}"]
    if since:
        params.append(f"since={date_to_iso(since)}T00:00:00Z")
    if until:
        params.append(f"until={date_to_iso(until)}T23:59:59Z")
    out: list[CommitRef] = []
    for page in range(1, max_pages + 1):
        url = f"{base}?{'&'.join(params)}&page={page}"
        items = fetch_json_api(url)
        if not items:
            break
        for it in items:
            out.append(CommitRef(
                sha=it["sha"],
                committed_at=parse_iso_datetime(it["commit"]["committer"]["date"]),
            ))
        if len(items) < 100:
            break
    return out


def latest_commit_per_date(commits: list[CommitRef]) -> dict[date, CommitRef]:
    """За всяка дата → последния commit (по timestamp)."""
    by_date: dict[date, CommitRef] = {}
    # commits идват от най-нови първи; reverse за right-most-wins fallback
    for c in sorted(commits, key=lambda x: x.committed_at):
        by_date[c.date_utc] = c  # later overrides earlier
    return by_date
