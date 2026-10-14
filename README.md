# Access Log Analyzer

A lightweight Python library and CLI utility for parsing web server access logs, extracting unique client IP addresses, and aggregating HTTP status codes.

## Usage

```python
from analyzer import count_status_codes, extract_unique_ips

logs = [
    '192.168.1.1 - - [19/Aug/2026:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024',
    '10.0.0.2 - - [19/Aug/2026:10:00:01 +0000] "POST /api/v1/login HTTP/1.1" 401 128',
    '192.168.1.1 - - [19/Aug/2026:10:00:02 +0000] "GET /dashboard HTTP/1.1" 200 4096',
]

unique_ips = extract_unique_ips(logs)
status_counts = count_status_codes(logs)

print("Unique IPs:", unique_ips)
print("Status Counts:", status_counts)
```

## Running Tests

```bash
pytest test_analyzer.py
```

## Supported Log Formats

See `log_formats.py`:

- `COMMON`: Apache/Nginx Common Log Format.
- `COMBINED`: Common Log Format plus referrer and user agent.

A sample log lives in `samples/access.log`.

## Roadmap

- JSON log output (abandoned in favor of a separate tool).
