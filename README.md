# Log Analyzer

A small Python 3 learning project that reads a web access log and writes a JSON report of threshold-based detections.

## What it detects

The rules and cutoffs are set in `config.py`.

| Detection | Rule |
| --- | --- |
| Brute force | 10 or more HTTP 401 responses in any 60-second window |
| Unauthorized access | HTTP 403 whose path is exactly `/login`, `/admin`, or `/dashboard` |
| Traffic anomaly | More than 50 requests from one IP in the file |

`BRUTE_FORCE_THRESHOLD` is 10 and `TIME_WINDOW_SECONDS` is 60. `ANOMALY_REQUEST_THRESHOLD` is 50, and the comparison is strict (`count > 50`), so a finding requires 51 or more requests.

## Project structure

```
Log_Analyzer/
├── analyzer.py          # Reads the sample log, runs the checks, prints and saves the report
├── parser.py            # Parses combined-style access log lines
├── detector.py          # Brute-force, unauthorized-access, and volume checks
├── config.py            # Thresholds and sensitive endpoints
├── report.py            # Writes output/report.json and creates the directory if needed
├── sample_logs/
│   └── access.log       # Synthetic log read by analyzer.py
├── output/
│   └── .gitkeep         # Keeps the output directory in git
├── .gitignore
└── README.md
```

## How to run

Python 3 standard library only. Nothing to install.

```bash
git clone https://github.com/tabooy747/Log_Analyzer.git
cd Log_Analyzer
python3 analyzer.py
```

On systems where the Python 3 command is `python`, run `python analyzer.py`.

The script reads `sample_logs/access.log`, prints the findings, and writes the same data to `output/report.json`. `report.py` creates `output/` when that directory is missing.

The sample log is synthetic. Client addresses use the documentation ranges in RFC 5737: `192.0.2.0/24`, `198.51.100.0/24`, and `203.0.113.0/24`. It includes:

- 10 failed logins (`401`) from `203.0.113.10` within nine seconds
- one `403` each for `/admin`, `/dashboard`, and `/login`
- 51 requests from `198.51.100.20`
- three lines that stay under the rules: one isolated `401`, a `200` on `/admin`, and a `403` on `/reports`

The log path is hardcoded in `analyzer.py`. Change `sample_logs/access.log` there to read another file in the same shape. Each data line looks like this (English month abbreviation, no timezone):

```
203.0.113.10 - - [16/Nov/2026:10:00:00] "POST /login HTTP/1.1" 401 512
```

## Sample output

`output/report.json` from the included log:

```json
{
    "brute_force": [
        {
            "type": "Brute Force",
            "ip": "203.0.113.10",
            "attempts": 10,
            "time_window": "2026-11-16 10:00:00"
        }
    ],
    "unauthorized_access": [
        {
            "type": "Unauthorized Access",
            "ip": "192.0.2.15",
            "endpoint": "/admin",
            "time": "2026-11-16 10:02:00"
        },
        {
            "type": "Unauthorized Access",
            "ip": "192.0.2.15",
            "endpoint": "/dashboard",
            "time": "2026-11-16 10:02:01"
        },
        {
            "type": "Unauthorized Access",
            "ip": "192.0.2.25",
            "endpoint": "/login",
            "time": "2026-11-16 10:02:02"
        }
    ],
    "anomalies": [
        {
            "type": "Traffic Anomaly",
            "ip": "198.51.100.20",
            "requests": 51
        }
    ]
}
```

## Limitations

This is a learning project for offline log files.

- Brute force counts every `401` in the 60-second window and labels the finding with the IP of the first `401` in that window. A burst larger than 10 can produce several findings, because each starting line looks forward one window.
- Unauthorized access keeps a row only when the status is `403` and the path is exactly `/login`, `/admin`, or `/dashboard`.
- A traffic anomaly is the total number of requests from one IP across the whole file. The count has no time window of its own.
- The parser accepts one timestamp shape, `dd/Mon/YYYY:HH:MM:SS`, with an English month abbreviation and no timezone.
- Useful next steps are a command-line log path, grouping brute-force findings by source IP, and collapsing overlapping windows into a single finding.
