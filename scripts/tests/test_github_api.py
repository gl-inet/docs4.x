"""Offline regression coverage for the GitHub client shared with docs-kvm."""
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import MagicMock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from github_api import GitHub, NoRedirect


class GitHubTests(unittest.TestCase):
    def test_host_protection(self):
        client = GitHub("owner/repo", "secret")
        client.opener = MagicMock()
        for url in ("https://evil.example/x", "https://api.github.com.evil/x",
                    "https://api.github.com@evil/x", "https://api.github.com:443/x",
                    "http://api.github.com/x", "//evil/x", "https://api.github.com/x#fragment",
                    "https://api.github.com/../x", "https://api.github.com/%2e%2e/x",
                    "https://api.github.com/\\evil"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                client.request("GET", url)
        client.opener.open.assert_not_called()

    def test_redirects_never_forward_token(self):
        for code in (301, 302, 303, 307, 308):
            with self.subTest(code=code), self.assertRaises(ValueError):
                NoRedirect().redirect_request(None, None, code, "redirect", {}, "https://evil.example")

    def test_request_and_graphql(self):
        client = GitHub("owner/repo", "secret")
        client.opener = MagicMock()
        client.opener.open.return_value.__enter__.return_value = io.BytesIO(b'{"ok":true}')
        self.assertEqual(client.request("POST", "issues/12/comments", {"body": "ok"}), {"ok": True})
        req = client.opener.open.call_args.args[0]
        self.assertEqual(req.full_url, "https://api.github.com/repos/owner/repo/issues/12/comments")
        self.assertEqual(req.get_header("Authorization"), "Bearer secret")
        self.assertEqual(req.get_header("User-agent"), "docs4.x-workflows")
        self.assertEqual(json.loads(req.data), {"body": "ok"})
        client.opener.open.return_value.__enter__.return_value = io.BytesIO(b'{}')
        client.graphql("query { viewer { login } }", {})
        self.assertEqual(client.opener.open.call_args.args[0].full_url, "https://api.github.com/graphql")

    def test_pagination_and_repository(self):
        for repository in ("bad", "../owner/repo", "owner/repo?x", "owner/repo/extra"):
            with self.assertRaises(ValueError):
                GitHub(repository, "secret")
        client = GitHub("owner/repo", "secret")
        client.request = MagicMock(side_effect=[[{}] * 100, [{"id": 101}]])
        self.assertEqual(len(client.paged("issues/12/comments")), 101)
        self.assertEqual(client.request.call_args.args[1], "issues/12/comments?per_page=100&page=2")

    def test_pagination_requires_list(self):
        client = GitHub("owner/repo", "secret")
        for batch in ({"message": "unexpected"}, None):
            client.request = MagicMock(return_value=batch)
            with self.subTest(batch=batch), self.assertRaisesRegex(ValueError, "Expected a GitHub list"):
                client.paged("issues/12/comments")
            self.assertEqual(client.request.call_count, 1)

    def test_pagination_is_bounded(self):
        client = GitHub("owner/repo", "secret")
        client.request = MagicMock(return_value=[{}] * 100)
        with self.assertRaisesRegex(ValueError, "pagination limit exceeded"):
            client.paged("issues/12/comments")
        self.assertEqual(client.request.call_count, 100)
        self.assertEqual(client.request.call_args.args[1], "issues/12/comments?per_page=100&page=100")


if __name__ == "__main__":
    unittest.main()
