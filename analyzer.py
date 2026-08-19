"""Simple access log analyzer for web traffic."""
import re
from typing import Dict, List, Set

# Pre-compile regexes at module level once
IP_PATTERN = re.compile(r"^(\d{1,3}(?:\.\d{1,3}){3})")
STATUS_PATTERN = re.compile(r'"\s+(\d{3})\s+')


def extract_unique_ips(logs: List[str]) -> List[str]:
  """Extracts unique client IP addresses from raw log lines in O(N) time."""
  seen_ips: Set[str] = set()
  unique_ips: List[str] = []

  for line in logs:
    match = IP_PATTERN.search(line)
    if match:
      ip = match.group(1)
      # O(1) lookup using hash set
      if ip not in seen_ips:
        seen_ips.add(ip)
        unique_ips.append(ip)

  return unique_ips


def count_status_codes(logs: List[str]) -> Dict[int, int]:
  """Counts occurrences of HTTP status codes in logs."""
  counts: Dict[int, int] = {}
  for line in logs:
    match = STATUS_PATTERN.search(line)
    if match:
      status = int(match.group(1))
      counts[status] = counts.get(status, 0) + 1
  return counts
