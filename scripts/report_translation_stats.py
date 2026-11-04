#!/usr/bin/env python3
"""Best-effort translation run reporting; standard library only, no artifacts.

AI_AGENT_STATS_URL is the service base URL (not an endpoint).
AI_AGENT_STATS_TOKEN is supplied only to the final report step.
STATS_NEEDS contains GitHub's toJSON(needs) for the four existing jobs.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Mapping


JOBS = ("prepare", "translate", "validate", "publish")


def run_status(needs: dict) -> str:
    results = {name: needs.get(name, {}).get("result") for name in JOBS}
    if "cancelled" in results.values():
        return "cancelled"
    if results["prepare"] != "success":
        return "failed"
    has_delta = needs["prepare"].get("outputs", {}).get("has_delta")
    if has_delta == "false" and all(results[name] == "skipped" for name in JOBS[1:]):
        return "no_delta"
    if has_delta != "true" or results["translate"] != "success":
        return "failed"
    if results["validate"] == "failure":
        return "validation_failed"
    if results["publish"] != "success":
        return "failed"
    has_changes = needs["translate"].get("outputs", {}).get("has_changes")
    if has_changes == "true" and results["validate"] == "success":
        return "success"
    if has_changes == "false" and results["validate"] == "skipped":
        return "no_changes"
    return "failed"


def build_event(env: Mapping[str, str]) -> dict:
    repository = env["GITHUB_REPOSITORY"]
    run_id = int(env["GITHUB_RUN_ID"])
    attempt = int(env["GITHUB_RUN_ATTEMPT"])
    if run_id <= 0 or attempt <= 0:
        raise ValueError("run ID and attempt must be positive")
    return {
        "source": "docs-translation",
        "event_type": "run_completed",
        "schema_version": 1,
        "run_key": f"{repository}:{run_id}:{attempt}",
        "context": {
            "docs_product": "router",
            "docs_version": "4",
            "repository": repository,
            "run_id": run_id,
            "run_attempt": attempt,
            "run_url": f"{env.get('GITHUB_SERVER_URL', 'https://github.com').rstrip('/')}/{repository}/actions/runs/{run_id}/attempts/{attempt}",
            "trigger": env["GITHUB_EVENT_NAME"],
        },
        "result": {"status": run_status(json.loads(env["STATS_NEEDS"]))},
    }


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Never forward the stats credential to a redirected endpoint."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def main(env: Mapping[str, str] | None = None) -> int:
    env = os.environ if env is None else env
    base_url = env.get("AI_AGENT_STATS_URL", "").strip().rstrip("/")
    if not base_url:
        print("Translation stats disabled: AI_AGENT_STATS_URL is unset.")
        return 0
    token = env.get("AI_AGENT_STATS_TOKEN", "")
    if not token:
        print("::warning::Translation stats skipped: AI_AGENT_STATS_TOKEN is unset.")
        return 0
    try:
        url = urllib.parse.urlsplit(base_url)
        if url.scheme != "https" or not url.netloc or url.username or url.password or url.query or url.fragment:
            raise ValueError("expected an HTTPS service base URL")
        event = build_event(env)
        request = urllib.request.Request(
            base_url + "/api/v1/docs-translation/runs",
            data=json.dumps(event).encode("utf-8"),
            headers={"Content-Type": "application/json", "X-Stats-Token": token},
            method="POST",
        )
        # One attempt, short timeout; no retries or response-body logging.
        with urllib.request.build_opener(NoRedirect()).open(request, timeout=5) as response:
            if response.status not in (200, 201):
                print(f"::warning::Translation stats not accepted (HTTP {response.status}).")
            else:
                print(f"Translation stats accepted: {event['result']['status']}.")
    except urllib.error.HTTPError as error:
        print(f"::warning::Translation stats not accepted (HTTP {error.code}).")
        error.close()
    except Exception as error:
        # Exception messages can contain URLs or secrets. Log the type only.
        print(f"::warning::Translation stats skipped ({type(error).__name__}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
