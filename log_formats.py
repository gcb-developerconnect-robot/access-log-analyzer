"""Known access log formats for the analyzer."""
import re

# Apache/Nginx Common Log Format (CLF). Client IPs may be IPv4 or IPv6.
COMMON = re.compile(
    r'^(?P<ip>[0-9A-Fa-f:.]+) \S+ \S+ \[(?P<time>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<path>\S+) (?P<proto>[^"]+)" '
    r'(?P<status>\d{3}) (?P<size>\d+|-)'
)

# Combined Log Format: CLF plus referrer and user agent.
COMBINED = re.compile(
    COMMON.pattern + r' "(?P<referrer>[^"]*)" "(?P<agent>[^"]*)"'
)

FORMATS = {
    'common': COMMON,
    'combined': COMBINED,
}


def get_format(name: str) -> re.Pattern:
  """Returns the compiled regex for a named log format."""
  try:
    return FORMATS[name]
  except KeyError:
    raise ValueError(f'unknown log format {name!r}; want one of {sorted(FORMATS)}') from None
