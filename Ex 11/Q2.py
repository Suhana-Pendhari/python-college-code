# Q2) Phone Number Extraction: Given a text document containing various lines of text, 
# write a Python script to extract all valid phone numbers using regular expressions. 
# Phone numbers should adhere to a specific format (e.g., (123) 456-7890 or 123-456-7890).

import re

# Simple function to extract phone numbers
find_phones = lambda text: re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)

print("-" * 40)

# Sample text
text = """
Call John at (123) 456-7890 or Jane at 987-654-3210.
Office: 555-123-4567, Emergency: (888) 999-0000.
Fake: 12345, 123-456.
"""
print("Text Document: ", text)

print("-" * 40)

# Extract and display
print("Phone Numbers Found:")
phones = find_phones(text)
for phone in phones:
    print(f"📞 {phone}")

print("-" * 40)