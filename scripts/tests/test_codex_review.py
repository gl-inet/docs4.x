import argparse
import copy
import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import codex_review as review


def finding():
    return dict(path="docs/page.md", line=2, severity="medium", category="grammar",
                problem="Wrong word.", suggestion="Fix the word.", replacement_line="new")


class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        self.git("init")
        self.git("config", "user.email", "test@example.com")
        self.git("config", "user.name", "Test")
        (self.repo / "docs").mkdir()
        (self.repo / "docs/page.md").write_text("keep\nold\nend\n")
        self.git("add", ".")
        self.git("commit", "-m", "base")
        self.base = self.git("rev-parse", "HEAD").strip()
        (self.repo / "docs/page.md").write_text("keep\nnew\nend\nadded\n")
        # A PR script must never be imported or executed.
        (self.repo / "github_api.py").write_text("raise RuntimeError('untrusted')\n")
        self.git("add", ".")
        self.git("commit", "-m", "head")
        self.head = self.git("rev-parse", "HEAD").strip()
        self.output = self.root / "review.json"
        self.output.write_text(json.dumps({"summary": "Reviewed.", "findings": [finding()]}))
        self.args = argparse.Namespace(repo=self.repo, base=self.base, head=self.head,
                                       review=self.output, pr=12, result="success", dry_run=False)

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.repo), *args], check=True,
                              capture_output=True, text=True).stdout

    def test_prepare_real_diff(self):
        event = self.root / "event.json"
        event.write_text(json.dumps({"pull_request": {"number": 12, "title": "Docs",
                                                      "body": "untrusted", "user": {"login": "author"}}}))
        out = self.root / "input"
        args = argparse.Namespace(repo=self.repo, base=self.base, head=self.head, event=event, out=out)
        self.assertEqual(review.cmd_prepare(args), 0)
        self.assertEqual(json.loads((out / "added-lines.json").read_text()), {"docs/page.md": [2, 4]})
        self.assertIn("+new", (out / "pr.diff").read_text())
        self.assertEqual(json.loads((out / "pr.json").read_text())["head_commit"], self.head)
        self.assertNotIn("github_api.py", (out / "changed-files.txt").read_text())

    def test_isolated_cli_from_untrusted_checkout(self):
        scripts = self.repo / "scripts"
        scripts.mkdir()
        for name in ("github_api.py", "codex_review.py", "__init__.py"):
            (scripts / name).write_text("raise RuntimeError('untrusted scripts')\n")
        event = self.root / "event.json"
        event.write_text(json.dumps({"pull_request": {"number": 12, "title": "Docs",
                                                      "body": "untrusted", "user": {"login": "author"}}}))
        out = self.root / "input"
        command = [sys.executable, "-I", str(Path(review.__file__).resolve())]
        common = ["--repo", str(self.repo), "--base", self.base, "--head", self.head]
        prepared = subprocess.run(
            [*command, "prepare", *common, "--event", str(event), "--out", str(out)],
            cwd=self.repo, capture_output=True, text=True, encoding="utf-8",
        )
        self.assertEqual(prepared.returncode, 0, prepared.stdout + prepared.stderr)
        self.assertEqual(json.loads((out / "added-lines.json").read_text()), {"docs/page.md": [2, 4]})
        self.assertIn("+new", (out / "pr.diff").read_text())
        published = subprocess.run(
            [*command, "publish", *common, "--review", str(self.output), "--pr", "12", "--dry-run"],
            cwd=self.repo, capture_output=True, text=True, encoding="utf-8",
        )
        self.assertEqual(published.returncode, 0, published.stdout + published.stderr)
        self.assertIn("Reviewed.", published.stdout)
        self.assertIn('"line": 2', published.stdout)
        self.assertIn("```suggestion", published.stdout)

    def test_diff_parser_context_and_deleted_lines(self):
        diff = "diff --git a/docs/p.md b/docs/p.md\n+++ b/docs/p.md\n@@ -1,3 +1,3 @@\n same\n-old\n+new\n end\n"
        self.assertEqual(review.added_lines(diff), {"docs/p.md": [2]})

    def test_reject_invalid_output(self):
        valid = {"summary": "OK", "findings": [finding()]}
        variants = []
        for key, value in [("path", "docs/../secret"), ("path", "/tmp/x"),
                           ("path", "docs/a\\b"), ("line", True), ("line", 0),
                           ("line", 1.5), ("problem", "x" * 2001), ("severity", []),
                           ("category", "invalid"), ("replacement_line", "a\nb")]:
            obj = copy.deepcopy(valid)
            obj["findings"][0][key] = value
            variants.append(obj)
        variants += [{"summary": "OK", "findings": [finding()] * 31},
                     {"summary": "OK", "findings": [], "extra": 1}, []]
        for obj in variants:
            with self.subTest(obj=str(obj)[:80]), self.assertRaises(ValueError):
                review.validate_review(obj)

    def test_duplicate_json_and_size(self):
        self.output.write_text('{"summary":"a","summary":"b"}')
        with self.assertRaises(ValueError):
            review.load_json(self.output)
        self.output.write_text(" " * 250001)
        with self.assertRaises(ValueError):
            review.load_json(self.output)

    def test_dry_run_needs_no_credentials_or_network(self):
        self.args.dry_run = True
        with patch.object(review, "GitHub") as client, contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(review.cmd_publish(self.args), 0)
        client.assert_not_called()
        self.assertIn('"line": 2', output.getvalue())

    def client(self):
        client = MagicMock()
        client.repository = "owner/repo"
        client.request.return_value = {"head": {"sha": self.head, "repo": {"full_name": "owner/repo"}},
                                       "state": "open", "draft": False, "base": {"ref": "master"}}
        client.paged.return_value = []
        return client

    def test_publish_recomputes_lines_and_checks_head(self):
        outside = finding()
        outside["line"] = 3
        self.output.write_text(json.dumps({"summary": "OK", "findings": [finding(), outside]}))
        client = self.client()
        with patch.object(review, "GitHub", return_value=client), patch.dict(
                review.os.environ, GITHUB_TOKEN="test", GITHUB_REPOSITORY="owner/repo"):
            review.cmd_publish(self.args)
        posts = [c.args for c in client.request.call_args_list if c.args[0] == "POST"]
        self.assertEqual(len(posts), 2)
        self.assertEqual([c["line"] for c in posts[0][2]["comments"]], [2])
        self.assertEqual(posts[0][2]["commit_id"], self.head)
        self.assertIn("docs/page.md:3", posts[1][2]["body"])
        self.assertEqual(sum(c.args[0] == "GET" for c in client.request.call_args_list), 3)

    def test_unchanged_path_never_constructs_client(self):
        item = finding()
        item["path"] = "docs/unrelated.md"
        self.output.write_text(json.dumps({"summary": "OK", "findings": [item]}))
        with patch.object(review, "GitHub") as client:
            with self.assertRaisesRegex(ValueError, "outside the documentation diff"):
                review.cmd_publish(self.args)
        client.assert_not_called()

    def test_stale_head_never_writes(self):
        client = self.client()
        client.request.return_value["head"]["sha"] = self.base
        with patch.object(review, "GitHub", return_value=client), patch.dict(
                review.os.environ, GITHUB_TOKEN="test", GITHUB_REPOSITORY="owner/repo"):
            with self.assertRaises(ValueError):
                review.cmd_publish(self.args)
        self.assertTrue(all(c.args[0] == "GET" for c in client.request.call_args_list))

    def test_head_change_during_publish_prevents_writes(self):
        client = self.client()
        current = copy.deepcopy(client.request.return_value)
        stale = copy.deepcopy(current)
        stale["head"]["sha"] = self.base
        client.request.side_effect = [current, stale]
        with patch.object(review, "GitHub", return_value=client), patch.dict(
                review.os.environ, GITHUB_TOKEN="test", GITHUB_REPOSITORY="owner/repo"):
            with self.assertRaises(ValueError):
                review.cmd_publish(self.args)
        self.assertTrue(all(c.args[0] == "GET" for c in client.request.call_args_list))

    def test_bad_json_and_wrong_checkout_never_construct_client(self):
        with patch.object(review, "GitHub") as client:
            self.output.write_text("not JSON")
            with self.assertRaises(ValueError):
                review.cmd_publish(self.args)
            self.args.head = self.base
            with self.assertRaises(ValueError):
                review.cmd_publish(self.args)
        client.assert_not_called()

    def test_failure_summary_does_not_load_review(self):
        self.args.result, self.args.dry_run = "failure", True
        self.output.unlink()
        with contextlib.redirect_stdout(io.StringIO()) as output:
            review.cmd_publish(self.args)
        self.assertIn("did not finish", output.getvalue())


if __name__ == "__main__":
    unittest.main()
