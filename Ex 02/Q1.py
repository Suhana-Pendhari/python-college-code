# Q1) Leap Year Checker:
# Develop a script that determines whether a given year entered 
# by the user is a leap year or not using conditional statements.

print("----Leap Year Checker----")
a = int(input("Enter year: "))

if(a%4 == 0):
    print("Its leap year")
else:
    print("It is not a leap year")
print("--------------------------")
