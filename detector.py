from collections import defaultdict
from datetime import timedelta
from config import *

def detect_brute_force(logs):
    alerts = []
    logs_sorted = sorted(logs, key=lambda x: x["time"])

    for i in range(len(logs_sorted)):
        window = []
        base_time = logs_sorted[i]["time"]

        for j in range(i, len(logs_sorted)):
            if logs_sorted[j]["time"] - base_time <= timedelta(seconds=TIME_WINDOW_SECONDS):
                if logs_sorted[j]["status"] == "401":
                    window.append(logs_sorted[j])
            else:
                break

        if len(window) >= BRUTE_FORCE_THRESHOLD:
            alerts.append({
                "type": "Brute Force",
                "ip": window[0]["ip"],
                "attempts": len(window),
                "time_window": str(base_time)
            })

    return alerts


def detect_unauthorized_access(logs):
    alerts = []

    for log in logs:
        if log["endpoint"] in SENSITIVE_ENDPOINTS and log["status"] == "403":
            alerts.append({
                "type": "Unauthorized Access",
                "ip": log["ip"],
                "endpoint": log["endpoint"],
                "time": str(log["time"])
            })

    return alerts


def detect_anomalies(logs):
    ip_counts = defaultdict(int)

    for log in logs:
        ip_counts[log["ip"]] += 1

    return [
        {
            "type": "Traffic Anomaly",
            "ip": ip,
            "requests": count
        }
        for ip, count in ip_counts.items()
        if count > ANOMALY_REQUEST_THRESHOLD
    ]