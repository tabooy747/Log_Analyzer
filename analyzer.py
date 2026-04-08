from parser import parse_log
from detector import (
    detect_brute_force,
    detect_unauthorized_access,
    detect_anomalies
)
from report import generate_report

def main():
    logs = parse_log("sample_logs/access.log")

    results = {
        "brute_force": detect_brute_force(logs),
        "unauthorized_access": detect_unauthorized_access(logs),
        "anomalies": detect_anomalies(logs)
    }

    report = generate_report(results)

    print("\n=== Threat Detection Report ===")
    for key, value in report.items():
        print(f"\n{key.upper()}:")
        for item in value:
            print(item)

if __name__ == "__main__":
    main()