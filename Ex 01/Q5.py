# 5.Membership Operator Use
# Input a character and check if it is present in the string 
# "Python Programming" using in and not in operators.

s = "Python Programming"
print(s)
c = input("Enter a character: ")

if(c in s):
    print("Character is present")

if(c not in s):
    print("Character is absent")
