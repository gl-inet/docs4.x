"""Offline tests; no network requests or real credentials."""
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import ssl
import unittest
from unittest import mock
import urllib.error

SPEC = importlib.util.spec_from_file_location(
    "codex_diagnostic", Path(__file__).resolve().parents[1] / "codex_diagnostic.py")
diag = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(diag)

KEY = "CANARY_PRIVATE_KEY"
URL = "https://canary-private.example/v1/responses"
BODY = "CANARY_PRIVATE_RESPONSE"


def completed():
    return {"status": "completed", "output": [{"type": "message", "content": [
        {"type": "output_text", "text": json.dumps(diag.EXPECTED)}]}]}


def response(data):
    value = io.BytesIO(json.dumps(data).encode())
    value.status = 200
    return value


class DiagnosticTests(unittest.TestCase):
    def test_request_and_schemas(self):
        for schema in (None, diag.MINIMAL_SCHEMA, {"type": "object"}):
            with self.subTest(schema=schema):
                opener = mock.Mock()
                opener.open.return_value = response(completed())
                self.assertEqual(diag.probe(opener, URL, KEY, "test-model", schema), (200, "completed"))
                request = opener.open.call_args.args[0]
                payload = json.loads(request.data)
                self.assertEqual(request.full_url, URL)
                self.assertEqual(request.get_header("Authorization"), "Bearer " + KEY)
                self.assertEqual(payload["model"], "test-model")
                self.assertEqual(payload["input"], diag.PROMPT)
                self.assertEqual(payload["max_output_tokens"], 512)
                self.assertFalse(payload["stream"])
                self.assertFalse(payload["store"])
                if schema is None:
                    self.assertNotIn("text", payload)
                else:
                    self.assertEqual(payload["text"]["format"]["schema"], schema)
                    self.assertTrue(payload["text"]["format"]["strict"])

    def test_response_classifications(self):
        cases = [
            (completed(), "completed"),
            ({"status": "incomplete"}, "incomplete_response"),
            ({"status": "failed"}, "unexpected_status"),
            ({"error": {"code": "invalid_json_schema", "message": BODY}}, "schema_rejected"),
            ({"error": {"code": "model_not_found"}}, "model_rejected"),
            ({"error": {"message": BODY}}, "unknown_error"),
            ({"status": "completed", "output": []}, "missing_output_text"),
            ({"status": "completed", "output": [{"type": "message", "content": [
                {"type": "refusal", "refusal": BODY}]}]}, "refusal"),
            ({"status": "completed", "output": [{"type": "message", "content": [
                {"type": "output_text", "text": BODY}]}]}, "invalid_output_json"),
        ]
        for data, label in cases:
            self.assertEqual(diag.result_label(data), label)

    def test_errors_do_not_escape(self):
        cases = [
            (TimeoutError(URL + KEY), (None, "timeout")),
            (urllib.error.URLError(ssl.SSLError(KEY)), (None, "tls_error")),
            (urllib.error.URLError(URL), (None, "connection_error")),
            (urllib.error.HTTPError(URL, 400, KEY, {}, io.BytesIO(json.dumps(
                {"error": {"code": "invalid_json_schema", "message": BODY}}).encode())),
             (400, "schema_rejected")),
            (urllib.error.HTTPError(URL, 404, KEY, {}, io.BytesIO(b'{}')), (404, "unknown_error")),
            (urllib.error.HTTPError(URL, 302, KEY, {"Location": URL}, io.BytesIO(b'{}')),
             (302, "redirect_blocked")),
        ]
        for error, expected in cases:
            opener = mock.Mock()
            opener.open.side_effect = error
            self.assertEqual(diag.probe(opener, URL, KEY, "test"), expected)

    def test_redirect_handler(self):
        self.assertIsNone(diag.NoRedirect().redirect_request(None, None, 302, KEY, {}, URL))

    def test_bounded_response(self):
        with self.assertRaises(ValueError):
            diag.decode_body(io.BytesIO(b'x' * (diag.MAX_BYTES + 1)))
        with self.assertRaises(ValueError):
            diag.decode_body(io.BytesIO(b'not json'))

    @mock.patch.dict(os.environ, {"OPENAI_API_KEY": KEY,
                                "CODEX_RESPONSES_API_ENDPOINT": URL,
                                "DIAGNOSTIC_MODEL": ""})
    def test_candidates_and_no_secret_output(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        with mock.patch.object(diag, "probe", return_value=(200, "completed")) as probe, \
                contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            self.assertEqual(diag.main(), 0)
        self.assertEqual([call.args[3] for call in probe.call_args_list],
                         ["gpt-6.2-sol", "gpt-6.1-sol", "gpt-6.2-sol", "gpt-6.2-sol"])
        for canary in (KEY, URL, BODY):
            self.assertNotIn(canary, stdout.getvalue() + stderr.getvalue())

    @mock.patch.dict(os.environ, {"OPENAI_API_KEY": KEY,
                                "CODEX_RESPONSES_API_ENDPOINT": URL,
                                "DIAGNOSTIC_MODEL": ""})
    def test_baseline_failure_skips_schemas(self):
        with mock.patch.object(diag, "probe", return_value=(502, "upstream_error")) as probe, \
                contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(diag.main(), 1)
        self.assertEqual(probe.call_count, 2)

    @mock.patch.dict(os.environ, {"OPENAI_API_KEY": KEY,
                                "CODEX_RESPONSES_API_ENDPOINT": URL,
                                "DIAGNOSTIC_MODEL": ""})
    def test_no_traceback_on_unexpected_error(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        with mock.patch.object(diag, "probe", side_effect=RuntimeError(KEY + URL + BODY)), \
                contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            self.assertEqual(diag.main(), 1)
        self.assertEqual(stdout.getvalue(), "diagnostic: internal_error_details_suppressed\n")
        self.assertEqual(stderr.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
