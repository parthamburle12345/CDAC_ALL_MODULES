import re

# 1. Compile a single regular expression using named capture groups
LOG_PATTERN = re.compile(
    r'^(?P<ip>\S+)\s+-\s+-\s+\[(?P<time>[^\]]+)\]\s+"(?P<method>[A-Z]+)\s+(?P<resource>\S+)\s+[A-Z0-9/.]+"\s+(?P<status>\d+)\s+(?P<bytes>\d+)$'
)

def analyze_server_logs(logs_text):
    valid_external_requests = []
    
    # 2. Parse input logs_text line-by-line
    for line in logs_text.strip().splitlines():
        line_clean = line.strip()
        if not line_clean:
            continue
            
        match = LOG_PATTERN.match(line_clean)
        if not match:
            print(f"Warning: Could not parse line: '{line_clean}'. Skipping.")
            continue
            
        data = match.groupdict()
        ip = data["ip"]
        
        # 3. Local IP Address Filtering: ignore IPs starting with "192.168." or "10."
        if ip.startswith("192.168.") or ip.startswith("10."):
            continue
            
        # 4. Compile dictionary with integer status and bytes
        valid_external_requests.append({
            "ip": ip,
            "time": data["time"],
            "method": data["method"],
            "resource": data["resource"],
            "status": int(data["status"]),
            "bytes": int(data["bytes"])
        })
        
    # 5. Return list of dictionaries
    return valid_external_requests


# Example Walkthrough
log_data = """192.168.1.5 - - [28/Aug/2026:10:00:00] "GET /index.html HTTP/1.1" 200 1024
8.8.8.8 - - [28/Aug/2026:10:10:00] "GET /api/v1/users HTTP/1.1" 200 4096
Corrupted log entry here
10.0.0.12 - - [28/Aug/2026:10:15:00] "POST /submit_data HTTP/1.1" 403 512
172.16.0.4 - - [28/Aug/2026:10:20:00] "POST /login HTTP/1.1" 401 256"""

parsed_logs = analyze_server_logs(log_data)
print("\nReturned List:")
print(parsed_logs)