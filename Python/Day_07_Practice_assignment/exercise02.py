import csv
import json
import os

def convert_log_file(input_log_path, output_csv_path, output_json_path):
    records = []

    # 1. Read and parse plain-text log lines
    with open(input_log_path, mode="r", encoding="utf-8") as log_file:
        for line in log_file:
            line = line.strip()
            if not line:
                continue
            parts = [part.strip() for part in line.split("|")]
            if len(parts) == 4:
                records.append({
                    "timestamp": parts[0],
                    "user_id": parts[1],
                    "endpoint": parts[2],
                    "status_code": int(parts[3])
                })

    # 2. Export structured records to CSV with a header row
    fieldnames = ["timestamp", "user_id", "endpoint", "status_code"]
    with open(output_csv_path, mode="w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    # 3. Export structured records to JSON with 2-space indentation
    with open(output_json_path, mode="w", encoding="utf-8") as json_file:
        json.dump(records, json_file, indent=2)

    return records


# Example Walkthrough
if __name__ == "__main__":
    log_path = os.path.join(os.path.dirname(__file__), "server_access.log")
    csv_path = os.path.join(os.path.dirname(__file__), "access_records.csv")
    json_path = os.path.join(os.path.dirname(__file__), "access_records.json")

    # Sample server access log content
    sample_log = """2026-09-01 10:15:30 | USR102 | /api/v1/predict | 200
2026-09-01 10:16:45 | USR105 | /login | 401
2026-09-01 10:17:12 | USR102 | /dashboard | 200
"""
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(sample_log)

    convert_log_file(log_path, csv_path, json_path)

    print("--- CSV Output ---")
    with open(csv_path, "r", encoding="utf-8") as f:
        print(f.read())

    print("--- JSON Output ---")
    with open(json_path, "r", encoding="utf-8") as f:
        print(f.read())
