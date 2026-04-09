# 🔐 Log Analysis & Threat Detection Tool (In Progress)

A Python-based cybersecurity tool designed to analyze server logs and detect suspicious activity, including brute-force login attempts, unauthorized access, and anomalous traffic patterns.

---

## 📌 Overview

This project simulates core functionality of a Security Information and Event Management (SIEM) system by processing log data and identifying potential security threats. It is being developed to demonstrate practical skills in cybersecurity analysis, threat detection, and Python programming.

---

## 🚨 Features

* **Brute-Force Detection**

  * Identifies repeated failed login attempts within a defined time window

* **Unauthorized Access Detection**

  * Flags access attempts to sensitive endpoints (e.g., `/admin`, `/login`) with forbidden responses

* **Traffic Anomaly Detection**

  * Detects abnormal request volumes from individual IP addresses

* **Structured Reporting**

  * Outputs findings in JSON format for further analysis or integration

---

## 🧠 Detection Techniques

* Time-window-based analysis for login attempts
* Endpoint sensitivity monitoring
* IP behavior profiling
* Threshold-based anomaly detection

---

## 🏗️ Project Structure

```
log-analyzer/
│── analyzer.py          # Main execution script
│── parser.py            # Log parsing and timestamp extraction
│── detector.py          # Threat detection logic
│── config.py            # Configurable thresholds and settings
│── report.py            # JSON report generation
│── utils.py             # Helper functions (future use)
│── sample_logs/         # Sample log files for testing
│── output/              # Generated reports
│── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/log-analyzer.git
cd log-analyzer
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the analyzer:

```bash
python analyzer.py
```

Output will be displayed in the console and saved to:

```
output/report.json
```

---

## 📄 Example Output

```json
{
    "brute_force": [
        {
            "type": "Brute Force",
            "ip": "192.168.1.1",
            "attempts": 15,
            "time_window": "2026-04-07 10:00:00"
        }
    ],
    "unauthorized_access": [],
    "anomalies": [
        {
            "type": "Traffic Anomaly",
            "ip": "192.168.1.2",
            "requests": 120
        }
    ]
}
```

---

## 🛠️ Technologies Used

* Python 3
* Regular Expressions (`re`)
* JSON for reporting
* Datetime for time-based analysis

---

## 🎯 Project Goals

* Simulate real-world log analysis workflows used in SOC environments
* Build a foundation for a lightweight SIEM system
* Demonstrate threat detection and data analysis skills

---

## 🚀 Future Enhancements

* Real-time log monitoring (live tailing)
* Web-based dashboard (Flask or React)
* IP geolocation and threat intelligence integration
* Machine learning-based anomaly detection
* Alerting system (email, webhook, etc.)

---

## 📌 Resume Description

**Log Analysis & Threat Detection Tool (In Progress)**

* Developing a Python-based tool to analyze logs and detect suspicious activity
* Implemented brute-force detection using time-windowed failed login analysis
* Identifies unauthorized access attempts and abnormal traffic patterns
* Designed modular architecture for scalability and future SIEM integration

---

## ⚠️ Disclaimer

This tool is intended for educational and defensive cybersecurity purposes only. Use responsibly and only on systems you own or have permission to analyze.

---

## 👤 Author

Douglas Marsh
Cybersecurity Enthusiast | Aspiring Security Analyst
