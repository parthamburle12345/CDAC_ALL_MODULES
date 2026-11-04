"""
CDAC Code Reviewer — Teammate Python Client SDK
Import and use directly inside any Python backend:
    from code_reviewer_client import review_code
"""

import requests

API_URL = "http://localhost:8000/api/review"

def review_code(code_string: str, language: str = "python", api_url: str = API_URL):
    """
    Sends source code to the CDAC Code Reviewer API.
    Returns PRD-compliant JSON with issues and refactoredCode.
    """
    payload = {
        "code": code_string,
        "language": language
    }
    resp = requests.post(api_url, json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()

if __name__ == "__main__":
    sample_code = """
def calculate_sum(items=[]):
    items.append(1)
    return items
"""
    print("Testing local API...")
    try:
        res = review_code(sample_code, "python")
        print("Summary       :", res.get("summary"))
        print("Severity Score:", res.get("severityScore"))
        print("Issues Found  :", len(res.get("issues", [])))
        print("Refactored Code:\n", res.get("refactoredCode"))
    except Exception as e:
        print(f"API Error (ensure server is running): {e}")