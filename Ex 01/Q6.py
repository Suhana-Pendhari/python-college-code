# 6.Swapping Without Temporary Variable
# Take two numbers and swap their values using arithmetic operators only 
# (no temp variable). Display the values before and after swapping.

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("----Before Swapping----")
print("a =", a)
print("b =", b)

a = a + b
b = a - b
a = a - b

print("----After Swapping----")
print("a =", a)
print("b =", b)
