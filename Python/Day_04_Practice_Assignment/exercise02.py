class InvalidPhoneNumberError(Exception):
    pass

def register_contact(phonebook, name, phone_input):
    if not isinstance(name, str) or not name.strip() or not all(c.isalpha() or c.isspace() for c in name):
        raise ValueError("Contact name must be a non-empty alphabetic string.")
    
    try:
        phone_str = str(phone_input)
        if not phone_str.isdigit():
            raise ValueError("Phone number must contain digits only.")
        int(phone_str)
    except ValueError:
        raise InvalidPhoneNumberError("Phone number must contain digits only.")
    
    phonebook[name] = phone_str
    return phonebook

contacts = {}

# 1. Valid Input
contacts = register_contact(contacts, "Alice", "0987654321")
print("Contacts after valid input:", contacts)
# Result: {"Alice": "0987654321"}

# 2. Invalid Phone Number (Raises InvalidPhoneNumberError)
try:
    contacts = register_contact(contacts, "Bob", "123-456-789")
except InvalidPhoneNumberError as e:
    print("Caught:", e)  # Output: Phone number must contain digits only.

# 3. Invalid Name (Raises ValueError)
try:
    contacts = register_contact(contacts, "Bob123", "9876543210")
except ValueError as e:
    print("Caught:", e)  # Output: Contact name must be a non-empty alphabetic string.

