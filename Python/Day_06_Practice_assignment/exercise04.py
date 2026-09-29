import re

class Patient:
    # 1. Class-level variable to track total patients created
    _patient_counter = 0

    # 2. Static method to validate date of birth format (YYYY-MM-DD)
    @staticmethod
    def validate_dob_format(dob_str):
        if not isinstance(dob_str, str):
            return False
        # Matches exactly 4 digits, hyphen, 2 digits, hyphen, 2 digits
        return bool(re.fullmatch(r"^\d{4}-\d{2}-\d{2}$", dob_str))

    # 3. Constructor
    def __init__(self, name, dob):
        if not Patient.validate_dob_format(dob):
            raise ValueError(f"Invalid date of birth format: '{dob}'. Expected YYYY-MM-DD.")
        
        Patient._patient_counter += 1
        self.patient_id = f"PAT-{1000 + Patient._patient_counter}"
        self.name = name
        self.dob = dob

    # 4. Class method to retrieve patient counter
    @classmethod
    def get_total_patients(cls):
        return cls._patient_counter


# Example Walkthrough
if __name__ == "__main__":
    # 1. Valid Registration
    p1 = Patient("Arham Khan", "1999-05-15")
    print(p1.patient_id)  # Output: PAT-1001

    # 2. Invalid DOB registration (throws ValueError)
    try:
        p2 = Patient("Lisa", "12/08/1998")
    except ValueError as e:
        print(e)  # Output: Invalid date of birth format: '12/08/1998'. Expected YYYY-MM-DD.

    print(Patient.get_total_patients())  # Output: 1
