# Q3) Multiplication Table Generator:
# Write a program that generates the multiplication table 
# (up to a specified number) using nested loops (for loops).

n = int(input("Enter number: "))

for i in range(1, n+1):
    print(f"\nMultiplication table for {i}:")
    for j in range(1, 11):
        print(f"{i} X {j}: {i*j}")
