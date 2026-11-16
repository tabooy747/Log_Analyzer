import json
import os

def generate_report(results, output_file="output/report.json"):
    output_dir = os.path.dirname(output_file)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    return results