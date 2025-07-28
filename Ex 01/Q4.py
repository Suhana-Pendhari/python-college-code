# 4.Identity Operator Check
# Assign two variables with the same number. Use is and is not operators to check
# if they refer to the same object.

a,b = map(int, input("Enter two numbers: ").split())

if(a is b):
    print("Equal")

if(a is not b):
    print("Not Equal")
