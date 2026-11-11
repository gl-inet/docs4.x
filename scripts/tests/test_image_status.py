"""Offline regression tests for image HTTP checks, aligned with docs-kvm."""
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, patch
import urllib.error

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pr_check as pc

URL = "https://example.invalid/image.png"


def response(status=200):
    result = Mock(status=status)
    result.__enter__ = Mock(return_value=result)
    result.__exit__ = Mock(return_value=False)
    return result


def http_error(status):
    return urllib.error.HTTPError(URL, status, "", {}, None)


class ImageStatusTests(unittest.TestCase):
    def test_successful_head_does_not_request_get(self):
        with patch.object(pc.urllib.request, "urlopen", return_value=response()) as request:
            self.assertEqual(pc.url_status(URL), 200)
            self.assertEqual([call.args[0].method for call in request.call_args_list], ["HEAD"])

    def test_head_failures_are_confirmed_by_get(self):
        for status in (403, 404, 405, 410):
            with self.subTest(status=status), patch.object(
                pc.urllib.request, "urlopen", side_effect=[http_error(status), response()]
            ) as request:
                self.assertEqual(pc.url_status(URL), 200)
                self.assertEqual([call.args[0].method for call in request.call_args_list], ["HEAD", "GET"])

    def test_get_confirms_missing_image(self):
        for status in (404, 410):
            with self.subTest(status=status), patch.object(
                pc.urllib.request, "urlopen", side_effect=[http_error(status), http_error(status)]
            ) as request:
                self.assertEqual(pc.url_status(URL), status)
                self.assertEqual(request.call_count, 2)

    def test_get_unavailable_does_not_reuse_head_missing_status(self):
        failures = [(http_error(503), 503), (urllib.error.URLError("offline"), "offline")]
        for error, expected in failures:
            with self.subTest(expected=expected), patch.object(
                pc.urllib.request, "urlopen", side_effect=[http_error(404), error]
            ) as request:
                self.assertEqual(pc.url_status(URL), expected)
                self.assertEqual(request.call_count, 2)


if __name__ == "__main__":
    unittest.main()
