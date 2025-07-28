# 1.Simple Arithmetic Calculator
# Take two numbers from the user and perform addition, subtraction, multiplication, 
# division, and modulus. Print each result with a proper message.

a,b = map(int, input("Enter two numbers: ").split())

print("------Simple Arithmetic Calculator------")
print("Addition: ", a+b)
print("Substraction: ", a-b)
print("Multiplication: ", a*b)
print("Division: ", a/b)
print("Modulo: ", a+b)
print("Floar Division: ", a//b)
print("Exponential: ", a**b)
print("-----------------------------------------")
