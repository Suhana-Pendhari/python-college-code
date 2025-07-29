# Q4) Number Guessing Game:
# Develop a number guessing game where the computer picks a random number 
# between 1 and 100, and the user has to guess it. Use a while loop to allow 
# multiple guesses until the correct number is guessed.

import random

n = random.randint(1, 100)
guess = None
attempts = 0

print("I'm thinking of a number between 1 and 100. Can you guess it?")

while guess != n:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < 1 or guess > 100:
        print("Please guess a number between 1 and 100.")
        continue

    if guess < n:
        print("Too low! Try again.")
    elif guess > n:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
