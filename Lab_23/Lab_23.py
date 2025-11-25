import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

# Test the function
email_id = input("Enter email ID: ")
if validate_email(email_id):
    print("Valid email ID.")
else:
    print("Invalid email ID.")
