# Q1) Calculator Application:
# • Create a Python script that defines functions for basic arithmetic operations 
# (addition, subtraction, multiplication, division). Allow users to input two 
# numbers and choose an operation to perform.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Simple Calculator")

choice = 0
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

while(1):
    print("----------------------------------")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter choice (1/2/3/4/5): ")
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Exited from program!!")
        break
    else:
        print("Invalid input")
    print("----------------------------------")

