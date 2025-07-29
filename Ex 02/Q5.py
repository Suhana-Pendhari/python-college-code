# Q5) Prime Number Finder:
# Write a program that finds and prints all prime numbers up to a specified 
# limit (n). Use a for loop and include a break statement to optimize the process.

print("-----Prime Number Finder-----")
n = int(input("Enter the limit (n) to find prime numbers up to: "))
        
if (n < 2):
    print("There are no prime numbers less than 2.")
else:
    print(f"Prime numbers up to {n}:")
            
    for num in range(2, n + 1):
        for divisor in range(2, int(num ** 0.5) + 1):
            if (num % divisor == 0):
                break
        else:
            print(num, end=' ')
    print()

print("-----------------------------")
