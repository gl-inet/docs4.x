#!/usr/bin/env python3
"""Generate a data-only translation stats artifact; no network or credentials.

STATS_NEEDS contains GitHub's toJSON(needs) for the four existing jobs.
The production collector downloads this JSON and validates it before ingestion.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
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


def main(env: Mapping[str, str] | None = None) -> int:
    env = os.environ if env is None else env
    output = Path(env.get("STATS_OUTPUT_PATH", "stats/translation-run.json"))
    try:
        # Remove stale output before generation so an invalid rerun cannot upload it.
        output.unlink(missing_ok=True)
        event = build_event(env)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(event, ensure_ascii=False) + "\n", encoding="utf-8")
    except Exception:
        # Do not echo input values, exception messages, or credentials into logs.
        print("::error::Translation stats artifact generation failed.")
        return 1
    print(f"Translation stats artifact generated: {event['result']['status']}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
