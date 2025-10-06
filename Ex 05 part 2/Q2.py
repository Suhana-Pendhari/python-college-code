# Q2) Write a Python program that reads user input for a numeric value and performs 
# mathematical operations on it. The program should handle cases where the user 
# inputs an invalid value (such as a non-numeric value) that cannot be converted 
# into the required numeric type. If an invalid input is provided, the program 
# should raise and handle a ValueError exception gracefully.

try:
    num = float(input("Enter a number: "))
    print("Square:", num * num)
except ValueError:
    print("Error: Invalid input, please enter a numeric value")
