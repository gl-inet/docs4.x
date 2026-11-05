"""Run: python3 -m unittest discover -s scripts/tests."""

import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

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

    def test_cancellation(self):
        for job in stats.JOBS:
            data = needs()
            data[job]["result"] = "cancelled"
            self.assertEqual(stats.run_status(data), "cancelled")

    def test_attempt_identity(self):
        env = environment()
        event = stats.build_event(env)
        self.assertEqual(event["run_key"], "gl-inet/docs4.x:123:2")
        self.assertEqual(event["context"]["run_url"],
                         "https://github.com/gl-inet/docs4.x/actions/runs/123/attempts/2")
        self.assertEqual(set(event), {"source", "event_type", "schema_version", "run_key", "context", "result"})
        env["GITHUB_RUN_ATTEMPT"] = "3"
        self.assertNotEqual(event["run_key"], stats.build_event(env)["run_key"])


class ArtifactTests(unittest.TestCase):
    def test_writes_without_url_or_token(self):
        with tempfile.TemporaryDirectory() as directory:
            env = environment()
            path = Path(directory) / "stats" / "translation-run.json"
            env["STATS_OUTPUT_PATH"] = str(path)
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(stats.main(env), 0)
            self.assertEqual(json.loads(path.read_text()), stats.build_event(env))

    def test_invalid_input_removes_stale_artifact(self):
        for field, value in (("GITHUB_RUN_ID", "invalid"), ("GITHUB_RUN_ATTEMPT", "0"),
                             ("STATS_NEEDS", "invalid-secret")):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as directory:
                env = environment()
                path = Path(directory) / "translation-run.json"
                path.write_text("stale")
                env.update({field: value, "STATS_OUTPUT_PATH": str(path)})
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    self.assertEqual(stats.main(env), 1)
                self.assertFalse(path.exists())
                self.assertNotIn("invalid-secret", output.getvalue())


if __name__ == "__main__":
    unittest.main()
