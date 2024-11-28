#Email Validator
import re

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(email_regex, email):
        return True
    return False

user_email = input("Enter an email address to validate: ")

if is_valid_email(user_email):
    print(f"'{user_email}' is a valid email address.")
else:
    print(f"'{user_email}' is not a valid email address.")
