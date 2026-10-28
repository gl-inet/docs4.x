"""Minimal GitHub REST and GraphQL client for the workflow scripts (standard library only)."""

from __future__ import annotations

import json
import urllib.request


class GitHub:
    def __init__(self, repository: str, token: str) -> None:
        self.repository = repository
        self.token = token

    def request(self, method: str, url: str, payload: dict | None = None):
        if not url.startswith("https://"):
            url = f"https://api.github.com/repos/{self.repository}/{url}"
        request = urllib.request.Request(
            url,
            method=method,
            data=json.dumps(payload).encode() if payload is not None else None,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "docs4.x-workflows",
            },
        )
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read()
            return json.loads(body) if body else None

    def paged(self, url: str) -> list[dict]:
        items, page = [], 1
        while True:
            batch = self.request("GET", f"{url}?per_page=100&page={page}")
            items.extend(batch)
            if len(batch) < 100:
                return items
            page += 1

    def graphql(self, query: str, variables: dict):
        return self.request("POST", "https://api.github.com/graphql", {"query": query, "variables": variables})
