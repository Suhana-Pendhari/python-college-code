# Q2) Factorial Calculation:
# • Write a function to compute the factorial of a number. Prompt the 
# user to enter a number and display its factorial.

def factorial(n):
    if(n == 1 or n == 0):
        return n
    return n * factorial(n-1)

n = int(input("Enter number for factorial: "))
print("Factorial is: ", factorial(n))
