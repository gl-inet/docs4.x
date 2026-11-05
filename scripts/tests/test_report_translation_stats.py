"""Run: python3 -m unittest discover -s scripts/tests -p 'test_report_translation_stats.py'."""

import contextlib
import errno
import io
import json
import socket
import ssl
import sys
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import report_translation_stats as stats


def needs(prepare="success", translate="success", validate="success", publish="success",
          has_delta="true", has_changes="true"):
    return {
        "prepare": {"result": prepare, "outputs": {"has_delta": has_delta}},
        "translate": {"result": translate, "outputs": {"has_changes": has_changes}},
        "validate": {"result": validate},
        "publish": {"result": publish},
    }


def environment():
    return {
        "AI_AGENT_STATS_URL": "https://stats.example/",
        "AI_AGENT_STATS_TOKEN": "test-secret",
        "GITHUB_REPOSITORY": "gl-inet/docs4.x",
        "GITHUB_RUN_ID": "123",
        "GITHUB_RUN_ATTEMPT": "2",
        "GITHUB_EVENT_NAME": "schedule",
        "STATS_NEEDS": json.dumps(needs()),
    }


class StatusTests(unittest.TestCase):
    def test_statuses(self):
        for data, expected in [
            (needs(), "success"),
            (needs(translate="skipped", validate="skipped", publish="skipped", has_delta="false"), "no_delta"),
            (needs(validate="skipped", has_changes="false"), "no_changes"),
            (needs(prepare="failure", translate="skipped", validate="skipped", publish="skipped"), "failed"),
            (needs(translate="failure", validate="skipped", publish="skipped"), "failed"),
            (needs(validate="failure", publish="failure"), "validation_failed"),
            (needs(publish="failure"), "failed"),
            (needs(validate="skipped"), "failed"),
            (needs(has_delta=""), "failed"),
            (needs(has_changes=""), "failed"),
            (needs(validate="skipped", publish="failure", has_changes="false"), "failed"),
            (needs(has_delta="false"), "failed"),
            ({}, "failed"),
        ]:
            with self.subTest(data=data):
                self.assertEqual(stats.run_status(data), expected)

    def test_cancellation_takes_precedence(self):
        for job in stats.JOBS:
            data = needs()
            data[job]["result"] = "cancelled"
            self.assertEqual(stats.run_status(data), "cancelled")

    def test_event_is_minimal_and_attempt_scoped(self):
        env = environment()
        event = stats.build_event(env)
        self.assertEqual(event["run_key"], "gl-inet/docs4.x:123:2")
        self.assertEqual(event["context"], {
            "docs_product": "router", "docs_version": "4", "repository": "gl-inet/docs4.x",
            "run_id": 123, "run_attempt": 2,
            "run_url": "https://github.com/gl-inet/docs4.x/actions/runs/123/attempts/2",
            "trigger": "schedule",
        })
        self.assertEqual(set(event), {"source", "event_type", "schema_version", "run_key", "context", "result"})
        self.assertNotIn("test-secret", json.dumps(event))
        env["GITHUB_RUN_ATTEMPT"] = "3"
        self.assertNotEqual(stats.build_event(env)["run_key"], event["run_key"])


class ReporterTests(unittest.TestCase):
    def run_report(self, env, opener):
        output = io.StringIO()
        with patch.object(stats.urllib.request, "build_opener", return_value=opener), contextlib.redirect_stdout(output):
            self.assertEqual(stats.main(env), 0)
        self.assertNotIn("test-secret", output.getvalue())
        return output.getvalue()

    def test_disabled_and_missing_token_do_not_send(self):
        for field in ("AI_AGENT_STATS_URL", "AI_AGENT_STATS_TOKEN"):
            env = environment()
            env.pop(field)
            opener = MagicMock()
            self.run_report(env, opener)
            opener.open.assert_not_called()

    def test_new_and_duplicate_accepted(self):
        for status in (200, 201):
            opener = MagicMock()
            opener.open.return_value.__enter__.return_value.status = status
            self.assertIn("accepted: success", self.run_report(environment(), opener))
            opener.open.assert_called_once()
            args, kwargs = opener.open.call_args
            request = args[0]
            self.assertEqual(request.full_url, "https://stats.example/api/v1/docs-translation/runs")
            self.assertEqual(request.get_method(), "POST")
            self.assertEqual(request.get_header("X-stats-token"), "test-secret")
            self.assertEqual(json.loads(request.data)["result"], {"status": "success"})
            self.assertEqual(kwargs["timeout"], 5)

    def test_errors_do_not_fail_or_expose_exception_messages(self):
        for error in (
            TimeoutError("test-secret"), urllib.error.URLError("test-secret"),
            urllib.error.HTTPError("https://stats.example", 401, "test-secret", {}, None),
        ):
            opener = MagicMock()
            opener.open.side_effect = error
            self.assertIn("::warning::", self.run_report(environment(), opener))
            opener.open.assert_called_once()

    def test_transport_error_categories_are_safe_and_best_effort(self):
        # Include URL, token, response-body and workflow-command markers in
        # errors to prove none of their text reaches the Actions log.
        sensitive = "https://stats.example/private test-secret response-body\n::error::injected"
        cases = [
            (socket.gaierror(socket.EAI_AGAIN, sensitive), "dns_error"),
            (ssl.SSLCertVerificationError(1, sensitive), "tls_certificate_error"),
            (ssl.SSLError(1, sensitive), "tls_error"),
            (TimeoutError(sensitive), "timeout"),
            (OSError(errno.ETIMEDOUT, sensitive), "timeout"),
            (ConnectionRefusedError(errno.ECONNREFUSED, sensitive), "connection_refused"),
            (ConnectionResetError(errno.ECONNRESET, sensitive), "connection_reset"),
            (OSError(errno.ENETUNREACH, sensitive), "network_unreachable"),
            (OSError(errno.EHOSTUNREACH, sensitive), "network_unreachable"),
            (ConnectionAbortedError(errno.ECONNABORTED, sensitive), "connection_error"),
            (OSError(errno.EIO, sensitive), "transport_error"),
            (RuntimeError(sensitive), "unexpected_error"),
        ]
        for reason, category in cases:
            for error in (reason, urllib.error.URLError(reason)):
                with self.subTest(reason=type(reason).__name__, wrapped=error is not reason):
                    opener = MagicMock()
                    opener.open.side_effect = error
                    output = self.run_report(environment(), opener)
                    self.assertIn(f"category={category}", output)
                    self.assertIn("before retrying", output)
                    self.assertEqual(output.count("\n"), 1)
                    for marker in ("https://", "stats.example", "response-body", "::error::injected"):
                        self.assertNotIn(marker, output)
                    opener.open.assert_called_once()
                    self.assertEqual(opener.open.call_args.kwargs["timeout"], 5)

    def test_string_url_reason_is_not_logged_or_interpreted(self):
        opener = MagicMock()
        opener.open.side_effect = urllib.error.URLError("test-secret timed out https://stats.example")
        output = self.run_report(environment(), opener)
        self.assertIn("category=transport_error", output)
        self.assertNotIn("timed out", output)
        self.assertNotIn("https://", output)

    def test_http_errors_keep_status_without_exposing_details(self):
        for status in (302, 401, 500):
            with self.subTest(status=status):
                error = urllib.error.HTTPError(
                    "https://stats.example/private", status, "test-secret", {}, io.BytesIO(b"response-body")
                )
                opener = MagicMock()
                opener.open.side_effect = error
                output = self.run_report(environment(), opener)
                self.assertIn(f"not accepted (HTTP {status})", output)
                self.assertNotIn("https://", output)
                self.assertNotIn("response-body", output)
                self.assertTrue(error.closed)

    def test_bad_inputs_do_not_send(self):
        for field, value in (
            ("AI_AGENT_STATS_URL", "http://stats.example"),
            ("AI_AGENT_STATS_URL", "https://user:password@stats.example"),
            ("AI_AGENT_STATS_URL", "https://stats.example?token=test-secret"),
            ("STATS_NEEDS", "invalid-json-test-secret"),
            ("GITHUB_RUN_ID", "not-a-number"),
            ("GITHUB_RUN_ATTEMPT", "0"),
        ):
            with self.subTest(field=field, value=value):
                env = environment()
                env[field] = value
                opener = MagicMock()
                self.assertIn("category=invalid_input", self.run_report(env, opener))
                opener.open.assert_not_called()

    def test_redirects_are_not_followed(self):
        handler = stats.NoRedirect()
        self.assertIsNone(handler.redirect_request(None, None, 302, "", {}, "https://elsewhere.example"))


if __name__ == "__main__":
    unittest.main()
