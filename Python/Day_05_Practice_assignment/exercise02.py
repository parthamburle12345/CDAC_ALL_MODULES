import re

# Compiled regex with start (^) and end ($) boundaries
ACADEMIC_EMAIL_PATTERN = re.compile(r"^[a-z0-9._]+@[a-z0-9.-]+(?:\.edu|\.res\.in)$")

def validate_academic_email(email):
    if not isinstance(email, str):
        return False
    return bool(ACADEMIC_EMAIL_PATTERN.match(email))


# Example Walkthrough
print(validate_academic_email("arham.khan@cdac.res.in"))  # Output: True
print(validate_academic_email("lisa_stud12@mit.edu"))      # Output: True
print(validate_academic_email("vinod@gmail.com"))          # Output: False (invalid suffix)
print(validate_academic_email("ALICE@college.edu"))        # Output: False (contains uppercase letters)
print(validate_academic_email("bob@mit.edu.com"))          # Output: False (does not end in .edu or .res.in)

