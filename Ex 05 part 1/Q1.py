# Q1) Write a Python program that reads a text file (data.txt) line by line
# and prints each line to the console.

with open('data.txt', 'r') as file:
    for line in file:
        print(line, end='')
