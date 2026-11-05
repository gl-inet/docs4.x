import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import report_review_stats as reporter


class ReviewStatsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.event = {"action": "synchronize", "pull_request": {"number": 42, "draft": False, "head": {"sha": "abc123", "repo": {"full_name": "gl-inet/docs4.x"}}, "base": {"ref": "master", "repo": {"full_name": "gl-inet/docs4.x"}}}}
        self.needs = {"review": {"result": "success"}, "publish": {"result": "success"}}
        self.review = {"summary": "PRIVATE SUMMARY", "findings": [{"path": "docs/en/private.md", "line": 2, "severity": "high", "category": "link", "problem": "PRIVATE PROBLEM", "suggestion": "PRIVATE SUGGESTION", "replacement_line": "PRIVATE REPLACEMENT"}, {"path": "docs/en/private.md", "line": 5, "severity": "low", "category": "grammar", "problem": "PRIVATE PROBLEM", "suggestion": "", "replacement_line": ""}]}
        self.env = {"GITHUB_REPOSITORY": "gl-inet/docs4.x", "GITHUB_RUN_ID": "123", "GITHUB_RUN_ATTEMPT": "2", "GITHUB_EVENT_NAME": "pull_request", "GITHUB_EVENT_PATH": str(self.root / "event.json"), "STATS_REVIEW_DIR": str(self.root / "review"), "STATS_OUTPUT_PATH": str(self.root / "stats/review-run.json")}
        directory = self.root / "review/.codex-run"
        directory.mkdir(parents=True)
        (directory / "added-lines.json").write_text(json.dumps({"docs/en/private.md": [2]}))
        self.save_review()

    def save_review(self):
        (self.root / "review/codex-output.json").write_text(json.dumps(self.review))

    def build(self):
        (self.root / "event.json").write_text(json.dumps(self.event))
        self.env["STATS_NEEDS"] = json.dumps(self.needs)
        return reporter.build_event(self.env)

    def test_counts_and_privacy(self):
        event = self.build()
        self.assertEqual(event["run_key"], "gl-inet/docs4.x:123:2")
        self.assertEqual(event["result"], {"status": "success", "findings_total": 2, "findings_by_severity": {"high": 1, "low": 1}, "findings_by_category": {"link": 1, "grammar": 1}, "inline_findings": 1, "summary_findings": 1, "suggestions": 1})
        text = json.dumps(event)
        self.assertNotIn("PRIVATE", text)
        self.assertNotIn("private.md", text)
        self.assertNotIn("execution", event)

    def test_statuses(self):
        for review, publish, expected in [("success", "success", "success"), ("success", "failure", "publish_failed"), ("failure", "success", "review_failed"), ("failure", "failure", "review_failed"), ("cancelled", "skipped", "cancelled"), ("success", "cancelled", "cancelled"), ("success", "skipped", "publish_failed")]:
            with self.subTest(review=review, publish=publish):
                self.needs["review"]["result"] = review
                self.needs["publish"]["result"] = publish
                event = self.build()
                self.assertEqual(event["result"]["status"], expected)
                self.assertEqual(event["result"]["findings_total"], 2 if review == "success" else 0)

    def test_empty_review_is_success(self):
        self.review["findings"] = []
        self.save_review()
        self.assertEqual(self.build()["result"]["status"], "success")

    def test_missing_or_invalid_output(self):
        path = self.root / "review/codex-output.json"
        for content in [None, "bad json", '{"findings":[]}', json.dumps({"summary": "", "findings": [{"severity": "high"}]})]:
            if content is None:
                path.unlink(missing_ok=True)
            else:
                path.write_text(content)
            result = self.build()["result"]
            self.assertEqual(result["status"], "invalid_output")
            self.assertEqual(result["findings_total"], 0)
        self.needs["review"]["result"] = "failure"
        self.assertEqual(self.build()["result"]["status"], "review_failed")

    def test_missing_line_map_matches_publisher(self):
        (self.root / "review/.codex-run/added-lines.json").unlink()
        result = self.build()["result"]
        self.assertEqual(result["inline_findings"], 0)
        self.assertEqual(result["summary_findings"], 2)

    def test_context_rejected(self):
        original = copy.deepcopy(self.event)
        for change in [lambda: self.event["pull_request"]["head"]["repo"].update(full_name="attacker/fork"), lambda: self.event["pull_request"].update(draft=True), lambda: self.event["pull_request"]["base"].update(ref="develop")]:
            self.event = copy.deepcopy(original)
            change()
            with self.assertRaises(ValueError):
                self.build()
        self.event = original
        self.needs["review"]["result"] = "skipped"
        with self.assertRaises(ValueError):
            self.build()

    def test_main_and_stale_output(self):
        self.build()
        self.assertEqual(reporter.main(self.env), 0)
        path = Path(self.env["STATS_OUTPUT_PATH"])
        self.assertTrue(path.is_file())
        self.env["GITHUB_RUN_ID"] = "0"
        self.assertEqual(reporter.main(self.env), 1)
        self.assertFalse(path.exists())


if __name__ == "__main__":
    unittest.main()
