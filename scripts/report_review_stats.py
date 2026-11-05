#!/usr/bin/env python3
"""Generate counts-only Docs PR review telemetry. No network or credentials.

Only a successful review job's valid output contributes findings. Counts describe
produced findings (not necessarily posted comments); publish failures stay visible.
"""
from __future__ import annotations

from collections import Counter
from collections.abc import Mapping
import json
import os
from pathlib import Path

SEVERITIES = {"high", "medium", "low"}
CATEGORIES = {"accuracy", "copy-paste", "link", "image", "grammar", "spelling", "terminology", "ui-label", "structure", "translation", "other"}
MAX_INPUT = 8 * 1024 * 1024


def read_json(path: Path):
    if path.stat().st_size > MAX_INPUT:
        raise ValueError("input too large")
    return json.loads(path.read_text(encoding="utf-8"))


def finding_counts(directory: Path) -> dict:
    review = read_json(directory / "codex-output.json")
    if not isinstance(review, dict) or set(review) != {"summary", "findings"} or not isinstance(review["summary"], str) or not isinstance(review["findings"], list):
        raise ValueError("invalid review")
    findings = review["findings"]
    lines_path = directory / ".codex-run" / "added-lines.json"
    lines = read_json(lines_path) if lines_path.is_file() else {}
    if not isinstance(lines, dict) or any(not isinstance(k, str) or not isinstance(v, list) or any(type(n) is not int for n in v) for k, v in lines.items()):
        raise ValueError("invalid line map")
    keys = {"path", "line", "severity", "category", "problem", "suggestion", "replacement_line"}
    for f in findings:
        if not isinstance(f, dict) or set(f) != keys or any(not isinstance(f[k], str) for k in keys - {"line"}) or type(f["line"]) is not int or f["severity"] not in SEVERITIES or f["category"] not in CATEGORIES:
            raise ValueError("invalid finding")
    inline = sum(f["line"] in lines.get(f["path"], ()) for f in findings)
    return {
        "findings_total": len(findings),
        "findings_by_severity": dict(Counter(f["severity"] for f in findings)),
        "findings_by_category": dict(Counter(f["category"] for f in findings)),
        "inline_findings": inline,
        "summary_findings": len(findings) - inline,
        "suggestions": sum(bool(f["replacement_line"]) for f in findings),
    }


def build_event(env: Mapping[str, str]) -> dict:
    repository = env["GITHUB_REPOSITORY"]
    run_id, attempt = int(env["GITHUB_RUN_ID"]), int(env["GITHUB_RUN_ATTEMPT"])
    event = read_json(Path(env["GITHUB_EVENT_PATH"]))
    pr = event["pull_request"]
    if run_id <= 0 or attempt <= 0 or env["GITHUB_EVENT_NAME"] != "pull_request" or pr["head"]["repo"]["full_name"] != repository or pr["base"]["repo"]["full_name"] != repository or pr["base"]["ref"] != "master" or pr["draft"]:
        raise ValueError("unsupported context")
    needs = json.loads(env["STATS_NEEDS"])
    review_result, publish_result = needs["review"]["result"], needs["publish"]["result"]
    if review_result == "skipped":
        raise ValueError("skipped reviews are not reported")
    counts = {"findings_total": 0, "findings_by_severity": {}, "findings_by_category": {}, "inline_findings": 0, "summary_findings": 0, "suggestions": 0}
    status = "success"
    if review_result == "cancelled" or publish_result == "cancelled":
        status = "cancelled"
    elif review_result != "success":
        status = "review_failed"
    if review_result == "success":
        try:
            counts = finding_counts(Path(env.get("STATS_REVIEW_DIR", "review")))
        except (ValueError, OSError, KeyError, TypeError):
            if status != "cancelled":
                status = "invalid_output"
        if status == "success" and publish_result != "success":
            status = "publish_failed"
    return {
        "source": "docs-review", "event_type": "run_completed", "schema_version": 1,
        "run_key": f"{repository}:{run_id}:{attempt}",
        "context": {
            "docs_product": "router", "docs_version": "4", "repository": repository,
            "run_id": run_id, "run_attempt": attempt,
            "run_url": f"https://github.com/{repository}/actions/runs/{run_id}/attempts/{attempt}",
            "trigger": "pull_request", "pr_number": pr["number"],
            "pr_url": f"https://github.com/{repository}/pull/{pr['number']}",
            "pr_action": event["action"], "head_sha": pr["head"]["sha"],
        },
        "result": {"status": status, **counts},
    }


def main(env: Mapping[str, str] | None = None) -> int:
    env = os.environ if env is None else env
    output = Path(env.get("STATS_OUTPUT_PATH", "stats/review-run.json"))
    try:
        output.unlink(missing_ok=True)
        event = build_event(env)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(event, ensure_ascii=False) + "\n", encoding="utf-8")
    except Exception:
        print("::error::Review stats artifact generation failed.")
        return 1
    print(f"Review stats artifact generated: {event['result']['status']}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
