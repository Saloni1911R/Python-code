import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def validate_phone(phone):
    pattern = r'^\d{10}$'   # only 10 digits
    return re.match(pattern, phone)

# Main program
data = input("Enter Email or Phone number: ")

if validate_email(data):
    print("Valid Email ID.")
elif validate_phone(data):
    print("Valid Phone Number.")
else:
    print("Invalid input.")