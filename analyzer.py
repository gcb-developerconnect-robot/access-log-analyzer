"""Simple access log analyzer for web traffic."""
import re
from typing import Dict, List


def extract_unique_ips(logs: List[str]) -> List[str]:
  """Extracts unique client IP addresses from raw log lines."""
  unique_ips: List[str] = []

  for line in logs:
    # Inefficient: re-compiling regex inside loop on every line
    match = re.search(r"^(\d{1,3}(?:\.\d{1,3}){3})", line)
    if match:
      ip = match.group(1)
      # Inefficient: O(N) linear scan for each IP -> O(N^2) total runtime
      if ip not in unique_ips:
        unique_ips.append(ip)

  return unique_ips


def count_status_codes(logs: List[str]) -> Dict[int, int]:
  """Counts occurrences of HTTP status codes in logs."""
  counts: Dict[int, int] = {}
  for line in logs:
    match = re.search(r'"\s+(\d{3})\s+', line)
    if match:
      status = int(match.group(1))
      counts[status] = counts.get(status, 0) + 1
  return counts
