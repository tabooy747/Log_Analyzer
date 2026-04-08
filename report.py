import json

def generate_report(results, output_file="output/report.json"):
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    return results