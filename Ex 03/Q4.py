# Q4) Palindrome Checker:
# Define a function that checks whether a given string is a palindrome 
# (reads the same backward as forward). Test the function with user-inputted strings.

def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

word = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(word):
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')
