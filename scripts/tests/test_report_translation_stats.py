"""Run: python3 -m unittest discover -s scripts/tests -p 'test_report_translation_stats.py'."""

import contextlib
import io
import json
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
                self.assertIn("::warning::", self.run_report(env, opener))
                opener.open.assert_not_called()

    def test_redirects_are_not_followed(self):
        handler = stats.NoRedirect()
        self.assertIsNone(handler.redirect_request(None, None, 302, "", {}, "https://elsewhere.example"))


if __name__ == "__main__":
    unittest.main()
