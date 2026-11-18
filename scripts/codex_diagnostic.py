#!/usr/bin/env python3
"""Manually probe a trusted Responses endpoint without logging sensitive data.

This tests direct synthetic requests, not the Codex CLI/proxy/tool-call path.
Only fixed labels and HTTP status numbers leave the process. No retries,
redirects, environment proxies, raw errors, response artifacts, or PR content.
"""

import json
import os
from pathlib import Path
import re
import socket
import ssl
import urllib.error
import urllib.parse
import urllib.request

PROMPT = 'Return only JSON: {"summary":"ok","findings":[]}'
EXPECTED = {"summary": "ok", "findings": []}
MINIMAL_SCHEMA = {
    "type": "object", "additionalProperties": False,
    "required": ["summary", "findings"],
    "properties": {
        "summary": {"type": "string"},
        "findings": {"type": "array", "items": {"type": "string"}},
    },
}
MAX_BYTES = 64 * 1024


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def error_label(data):
    """Classify only known machine-readable fields; never echo provider text."""
    error = data.get("error") if isinstance(data, dict) else None
    if not isinstance(error, dict):
        return "unknown_error"
    code = error.get("code")
    param = error.get("param")
    if code in ("model_not_found", "unsupported_model", "invalid_model"):
        return "model_rejected"
    if code in ("invalid_json_schema", "invalid_schema", "unsupported_schema"):
        return "schema_rejected"
    if param in ("text.format", "text.format.schema", "response_format", "response_format.schema"):
        return "schema_parameter_rejected"
    if code in ("invalid_api_key", "authentication_error"):
        return "authentication_rejected"
    if code in ("insufficient_quota", "rate_limit_exceeded"):
        return "quota_or_rate_limit"
    if error.get("type") == "upstream_error":
        return "upstream_error"
    return "unknown_error"


def decode_body(response):
    body = response.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise ValueError("oversized")
    return json.loads(body)


def result_label(data):
    if not isinstance(data, dict):
        return "unexpected_envelope"
    if data.get("error"):
        return error_label(data)
    if data.get("status") == "incomplete":
        return "incomplete_response"
    if data.get("status") != "completed":
        return "unexpected_status"
    output = data.get("output")
    if not isinstance(output, list):
        return "unexpected_envelope"
    texts = []
    for item in output:
        if not isinstance(item, dict):
            return "unexpected_envelope"
        if item.get("type") != "message":
            continue
        content = item.get("content")
        if not isinstance(content, list):
            return "unexpected_envelope"
        for part in content:
            if not isinstance(part, dict):
                return "unexpected_envelope"
            if part.get("type") == "refusal":
                return "refusal"
            if part.get("type") == "output_text" and isinstance(part.get("text"), str):
                texts.append(part["text"])
    if not texts:
        return "missing_output_text"
    try:
        value = json.loads("".join(texts))
    except ValueError:
        return "invalid_output_json"
    return "completed" if value == EXPECTED else "unexpected_synthetic_output"


def probe(opener, endpoint, key, model, schema=None):
    payload = {
        "model": model, "input": PROMPT, "stream": False,
        "store": False, "max_output_tokens": 512,
    }
    if schema is not None:
        payload["text"] = {"format": {
            "type": "json_schema", "name": "gateway_diagnostic",
            "strict": True, "schema": schema,
        }}
    request = urllib.request.Request(
        endpoint, data=json.dumps(payload).encode("utf-8"), method="POST",
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
    )
    try:
        with opener.open(request, timeout=40) as response:
            status = response.status
            return status, result_label(decode_body(response))
    except urllib.error.HTTPError as error:
        try:
            label = error_label(decode_body(error))
        except (ValueError, UnicodeError):
            label = "unreadable_error_body"
        finally:
            error.close()
        if 300 <= error.code < 400:
            label = "redirect_blocked"
        return error.code, label
    except (TimeoutError, socket.timeout):
        return None, "timeout"
    except urllib.error.URLError as error:
        if isinstance(error.reason, (TimeoutError, socket.timeout)):
            return None, "timeout"
        if isinstance(error.reason, ssl.SSLError):
            return None, "tls_error"
        return None, "connection_error"
    except (ValueError, UnicodeError):
        return None, "unreadable_response"


def main():
    try:
        endpoint = os.environ.get("CODEX_RESPONSES_API_ENDPOINT", "")
        key = os.environ.get("OPENAI_API_KEY", "")
        override = os.environ.get("DIAGNOSTIC_MODEL", "").strip()
        url = urllib.parse.urlsplit(endpoint)
        if (url.scheme != "https" or not url.hostname or url.username or url.password
                or url.fragment or any(ord(c) < 33 for c in endpoint)
                or not key or any(ord(c) < 32 for c in key)):
            print("configuration: invalid_or_missing_credentials_or_endpoint")
            return 1
        models = [override] if override else ["gpt-6.2-sol", "gpt-6.1-sol"]
        if any(not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}", model) for model in models):
            print("configuration: invalid_model_input")
            return 1
        schema = json.loads((Path(__file__).resolve().parents[1]
                             / ".github/codex/pr-review.schema.json").read_text(encoding="utf-8"))
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
        selected = None
        for index, model in enumerate(models, 1):
            status, label = probe(opener, endpoint, key, model)
            # Candidate numbers map to the fixed order above or the manual input.
            print(f"model_candidate_{index}/baseline: http={status or 'none'} result={label}")
            if label == "completed" and selected is None:
                selected = model
        if selected is None:
            print("conclusion: no_completed_baseline; schema_compatibility_untested")
            return 1
        success = True
        for name, candidate_schema in (("minimal_schema", MINIMAL_SCHEMA), ("review_schema", schema)):
            status, label = probe(opener, endpoint, key, selected, candidate_schema)
            print(f"{name}: http={status or 'none'} result={label}")
            success = success and label == "completed"
        print("conclusion: direct_probes_completed_not_cli_verified" if success
              else "conclusion: inspect_schema_probe_classifications")
        return 0 if success else 1
    except Exception:
        # Do not allow exception messages/tracebacks to reveal a URL, key or body.
        print("diagnostic: internal_error_details_suppressed")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
