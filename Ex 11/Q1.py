# Q1) Email Validation: Write a Python function that takes an email address as input and uses 
# regular expressions to validate if the email address is correctly formatted according to 
# standard rules (e.g., username@domain.com).

import re

def validate_email(email):
    """
    Simple email validation function
    """
    # Basic email pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

def main():
    print("=== Email Validator ===")
    print("Enter email addresses to validate (type 'quit' to exit)\n")
    
    while True:
        email = input("Enter email address: ").strip()
        
        if email.lower() == 'quit':
            print("Goodbye!")
            break
            
        if validate_email(email):
            print(f"✓ '{email}' is a VALID email address\n")
        else:
            print(f"✗ '{email}' is an INVALID email address\n")

if __name__ == "__main__":
    main()
