"""Small standard-library GitHub client; credentials never follow redirects."""
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("GitHub API redirects are not allowed")


class GitHub:
    def __init__(self, repository: str, token: str) -> None:
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
            raise ValueError("Invalid repository")
        self.repository = repository
        self.token = token
        self.opener = urllib.request.build_opener(NoRedirect())

    def request(self, method: str, url: str, payload: dict | None = None):
        if not url.startswith("https://"):
            if url.startswith("/") or ":" in url or "\\" in url:
                raise ValueError("Invalid GitHub API path")
            url = f"https://api.github.com/repos/{self.repository}/{url}"
        parsed = urllib.parse.urlsplit(url)
        if (parsed.scheme != "https" or parsed.netloc != "api.github.com"
                or parsed.fragment or "\\" in url
                or any(p in (".", "..") for p in urllib.parse.unquote(parsed.path).split("/"))):
            raise ValueError("Untrusted GitHub API URL")
        request = urllib.request.Request(
            url, method=method,
            data=json.dumps(payload).encode() if payload is not None else None,
            headers={"Authorization": f"Bearer {self.token}",
                     "Accept": "application/vnd.github+json",
                     "X-GitHub-Api-Version": "2022-11-28",
                     "User-Agent": "docs4.x-workflows"},
        )
        with self.opener.open(request, timeout=60) as response:
            body = response.read()
            return json.loads(body) if body else None

    def paged(self, url: str) -> list[dict]:
        items = []
        for page in range(1, 101):
            batch = self.request("GET", f"{url}?per_page=100&page={page}")
            if not isinstance(batch, list):
                raise ValueError("Expected a GitHub list")
            items.extend(batch)
            if len(batch) < 100:
                return items
        raise ValueError("GitHub pagination limit exceeded")

    def graphql(self, query: str, variables: dict):
        return self.request("POST", "https://api.github.com/graphql", {"query": query, "variables": variables})
