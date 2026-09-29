import re

# Single compiled RegEx pattern to parse all three phone number formats
PHONE_PATTERN = re.compile(
    r"(?:\((\d{3})\)\s*(\d{3})-(\d{4}))|"       # (AAA) PPP-LLLL
    r"(?:(\d{3})-(\d{3})-(\d{4}))|"             # AAA-PPP-LLLL
    r"(?:(?<!\d)(\d{3})(\d{3})(\d{4})(?!\d))"   # AAAPPPLLLL (10 digits)
)

def scrape_directory_phones(directory_text):
    phone_records = []
    for match in PHONE_PATTERN.finditer(directory_text):
        # Extract the 3 active capture groups for whichever format matched
        groups = [g for g in match.groups() if g is not None]
        if len(groups) == 3:
            area_code, prefix, line_number = groups
            phone_records.append({
                "area_code": area_code,
                "prefix": prefix,
                "line_number": line_number,
                "formatted": f"({area_code}) {prefix}-{line_number}"
            })
    return phone_records


# Example Walkthrough
directory = "Contact HR at 123-456-7890 or the helpdesk at (987) 654-3210. Direct line is 5558881234."
results = scrape_directory_phones(directory)
print(results)