# Q1) Write a Python program that takes two integers as input from the user and performs 
# division of the first integer by the second. If the second integer is zero, the 
# program should raise a ZeroDivisionError. The program should also handle this exception 
# and display an appropriate error message without crashing.

try:
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
    