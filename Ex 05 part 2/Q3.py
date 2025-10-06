# Q3) Write a Python program that takes user input and converts it into an integer. 
# If the user enters a value that is not a valid number (such as a string containing 
# alphabetic characters or symbols), handle the resulting exception gracefully
# and display an error message indicating that the input format is invalid.

try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Error: Invalid input format")
