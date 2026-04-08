import re
from datetime import datetime

LOG_PATTERN = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<time>.*?)\] "(?P<method>\w+) (?P<endpoint>.*?) HTTP.*" (?P<status>\d+)'
)

def parse_time(time_str):
    return datetime.strptime(time_str, "%d/%b/%Y:%H:%M:%S")

def parse_log(file_path):
    logs = []

    with open(file_path, "r") as f:
        for line in f:
            match = LOG_PATTERN.search(line)
            if match:
                data = match.groupdict()
                data["time"] = parse_time(data["time"])
                logs.append(data)

    return logs