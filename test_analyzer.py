"""Unit tests for access log analyzer."""
import unittest
from analyzer import extract_unique_ips, count_status_codes


class TestAccessLogAnalyzer(unittest.TestCase):

  def setUp(self):
    self.sample_logs = [
        '192.168.1.1 - - [19/Aug/2026:10:00:00 +0000] "GET /index.html HTTP/1.1"'
        ' 200 1024',
        '10.0.0.2 - - [19/Aug/2026:10:00:01 +0000] "POST /api/v1/login HTTP/1.1"'
        ' 401 128',
        '192.168.1.1 - - [19/Aug/2026:10:00:02 +0000] "GET /dashboard HTTP/1.1"'
        ' 200 4096',
        '172.16.0.5 - - [19/Aug/2026:10:00:03 +0000] "GET /healthz HTTP/1.1"'
        ' 500 64',
        '10.0.0.2 - - [19/Aug/2026:10:00:04 +0000] "GET /profile HTTP/1.1" 200'
        ' 2048',
    ]

  def test_extract_unique_ips(self):
    unique_ips = extract_unique_ips(self.sample_logs)
    self.assertEqual(unique_ips, ['192.168.1.1', '10.0.0.2', '172.16.0.5'])

  def test_count_status_codes(self):
    counts = count_status_codes(self.sample_logs)
    self.assertEqual(counts, {200: 3, 401: 1, 500: 1})


if __name__ == '__main__':
  unittest.main()
