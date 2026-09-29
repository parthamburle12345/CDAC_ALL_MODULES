import re

def demo_search_and_match():
    """
    Demonstrates the difference between re.match() and re.search().
    - re.match() checks for a match ONLY at the beginning of the string.
    - re.search() checks for a match ANYWHERE in the string.
    Also demonstrates how to retrieve information from a Match object.
    """
    print("--- Demo: re.search() vs re.match() ---")
    text = "Java programming is fun and Python is powerful."
    pattern = "Python"

    # re.match() searches only at the beginning
    match_result = re.match(pattern, text)
    if match_result:
        print(f"re.match() found: '{match_result.group()}' at span {match_result.span()}")
    else:
        print("re.match() did not find the pattern at the beginning.")

    # Try matching "fun" (which is in the middle of the text) with re.match()
    match_result2 = re.match("fun", text)
    print(f"re.match('fun', text): {match_result2} (None because 'fun' is not at the start)")

    # re.search() searches the entire string and returns the first occurrence
    search_result = re.search("fun", text)
    if search_result:
        print(f"re.search() found 'fun': '{search_result.group()}' at span {search_result.span()} (start: {search_result.start()}, end: {search_result.end()})")
    
    search_result2 = re.search(pattern, text)
    if search_result2:
        print(f"re.search() found 'Python': '{search_result2.group()}' at span {search_result2.span()}")
    print()


def demo_fullmatch():
    """
    Demonstrates re.fullmatch().
    - re.fullmatch() checks if the ENTIRE string matches the pattern.
    Useful for strict validation (e.g., email, zip code, phone number).
    """
    print("--- Demo: re.fullmatch() ---")
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    
    email1 = "user@example.com"
    email2 = "user@example.com extra text"  # Contains extra text at the end

    # Check email1
    match1 = re.fullmatch(email_pattern, email1)
    print(f"Is '{email1}' a full match? {match1 is not None}")  # True

    # Check email2 (will fail since there is extra text not matching the email pattern)
    match2 = re.fullmatch(email_pattern, email2)
    print(f"Is '{email2}' a full match? {match2 is not None}")  # False
    
    # re.search() will succeed because it finds the substring matching the pattern
    search_match = re.search(email_pattern, email2)
    print(f"re.search() on '{email2}': Found '{search_match.group()}'")
    print()


def demo_findall_and_finditer():
    """
    Demonstrates re.findall() and re.finditer().
    - re.findall() returns a list of all non-overlapping matches as strings.
    - re.finditer() returns an iterator yielding Match objects for all matches.
      This is useful to retrieve the position (span) and groups for each match.
    """
    print("--- Demo: re.findall() vs re.finditer() ---")
    text = "The product costs $12, the tax is $2, and shipping is $5."
    pattern = r"\$\d+"  # Matches a literal dollar sign followed by one or more digits

    # re.findall() returns a list of matching substrings
    prices = re.findall(pattern, text)
    print(f"re.findall() returned: {prices}")

    # re.finditer() returns match objects, allowing us to find locations/spans
    print("re.finditer() matches:")
    for match in re.finditer(pattern, text):
        print(f"  Found '{match.group()}' at span {match.span()} (position {match.start()} to {match.end()})")
    print()


def demo_split():
    """
    Demonstrates re.split().
    - re.split() splits a string by the occurrences of the pattern.
    Useful for splitting by multiple characters/delimiters (e.g. space, comma, semicolon, colon).
    """
    print("--- Demo: re.split() ---")
    # A string with multiple separators: commas, semicolons, spaces, and colons
    text = "apple, banana; cherry;;;;;  orange:grape"
    pattern = r"[,\s;:]+"  # Split by comma, whitespace, semicolon, or colon (one or more)

    words = re.split(pattern, text)
    print(f"Original text: '{text}'")
    print(f"re.split() result: {words}")
    print()


def demo_sub_and_subn():
    """
    Demonstrates re.sub() and re.subn().
    - re.sub() replaces all occurrences of a pattern with a replacement string.
    - re.subn() is similar but returns a tuple: (new_string, number_of_substitutions).
    """
    print("--- Demo: re.sub() vs re.subn() ---")
    text = "Contact us at info@example.com or support@example.org for help."
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # Masking email addresses with re.sub()
    masked_text = re.sub(pattern, "[MASKED EMAIL]", text)
    print(f"re.sub() output:   {masked_text}")

    # Masking email addresses with re.subn() to also get the count of replacements
    masked_text_n, count = re.subn(pattern, "[MASKED EMAIL]", text)
    print(f"re.subn() output:  {masked_text_n}")
    print(f"Number of replacements made: {count}")
    print()


def demo_compilation_and_flags():
    """
    Demonstrates re.compile() and using flags like re.IGNORECASE.
    - re.compile() compiles a regular expression pattern into a regular expression object.
      This is efficient if you reuse the pattern multiple times in your code.
    - re.IGNORECASE (or re.I) makes the match case-insensitive.
    """
    print("--- Demo: re.compile() and Flags ---")
    # Pre-compile the regex pattern with the IGNORECASE flag
    pattern_obj = re.compile(r"python", re.IGNORECASE)

    texts = [
        "Python is awesome.",
        "I love PYTHON.",
        "pyThOn is everywhere."
    ]

    print("Matching pre-compiled case-insensitive pattern:")
    for text in texts:
        match = pattern_obj.search(text)
        if match:
            print(f"  Matched '{match.group()}' in '{text}'")
    print()


def demo_groups_capturing():
    """
    Demonstrates captured groups and named groups.
    - Parentheses () are used to group sub-patterns and capture them.
    - Named groups use the syntax (?P<name>pattern) to assign a name to a group.
    - Retrieve groups using match.group(1), match.groups(), match.group('name'), or match.groupdict().
    """
    print("--- Demo: Captured and Named Groups ---")
    
    # 1. Positional/Numbered Groups
    date_text = "Today's date is 2026-08-31."
    # date_pattern = r"\d{4}-\d{2}-\d{2}"  # no group here
    date_pattern = r"(\d{4})-(\d{2})-(\d{2})"  # Groups for year, month, day
    # date_pattern = r"(?P<year>\d{4})-(?P<mon>\d{2})-(?P<day>\d{2})"  # Named groups for year, month, day

    match = re.search(date_pattern, date_text)
    if match:
        print("Positional Groups:")
        print(f"  Full Match (group 0): {match.group(0)}")  # group(0) is always the entire match
        print(f"  Year (group 1):       {match.group(1)}")
        print(f"  Month (group 2):      {match.group(2)}")
        print(f"  Day (group 3):        {match.group(3)}")
        print(f"  All groups as tuple: {match.groups()}")

    # 2. Named Groups
    log_line = "ERROR [2026-08-31 13:24:05] Database connection failed."
    # Define named groups using (?P<group_name>pattern)
    log_pattern = r"(?P<level>[A-Z]+)\s+\[(?P<timestamp>[^\]]+)\]\s+(?P<message>.*)"

    log_match = re.search(log_pattern, log_line)
    if log_match:
        print("\nNamed Groups:")
        print(f"  Log Level: {log_match.group('level')}")
        print(f"  Timestamp: {log_match.group('timestamp')}")
        print(f"  Message:   {log_match.group('message')}")
        print(f"  All named groups as dict: {log_match.groupdict()}")
    print()


def main():
    print("================ Regular Expression Demos ================")
    # Uncomment any of the functions below to run the demo.
    
    demo_search_and_match()
    # demo_fullmatch()
    # demo_findall_and_finditer() 
    # demo_split()
    # demo_sub_and_subn()
    # demo_compilation_and_flags()
    # demo_groups_capturing()
    print("==========================================================")

if __name__ == "__main__":
    main()
