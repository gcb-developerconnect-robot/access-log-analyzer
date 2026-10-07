"""Known access log formats for the analyzer."""
import re

# Apache/Nginx Common Log Format (CLF).
COMMON = re.compile(
    r'^(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<path>\S+) (?P<proto>[^"]+)" '
    r'(?P<status>\d{3}) (?P<size>\d+|-)'
)
