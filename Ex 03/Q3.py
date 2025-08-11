# Q3) Create a Python program that converts temperatures between Celsius and Fahrenheit using functions. 
# The program should provide a menu for the user to choose the type of conversion and then display the result.
# Requirements:
# 1. Function 1: celsius_to_fahrenheit(celsius):
# o	Takes a temperature in Celsius as input.
# o	Returns the equivalent temperature in Fahrenheit.
# o	Formula: Fahrenheit = (Celsius * 9/5) + 32
# 2. Function 2: fahrenheit_to_celsius(fahrenheit):
# o	Takes a temperature in Fahrenheit as input.
# o	Returns the equivalent temperature in Celsius.
# o	Formula: Celsius = (Fahrenheit - 32) * 5/9
# 3. Main Program Flow:
# o	Display a menu with options:
# 1.Convert Celsius to Fahrenheit
# 2.Convert Fahrenheit to Celsius
# 3.Exit
# o	Prompt the user to choose an option.
# o	Based on the user's choice, call the appropriate function and display the result.
# o	Allow the user to perform multiple conversions until they choose to exit.


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("\nTemperature Conversion Menu")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

