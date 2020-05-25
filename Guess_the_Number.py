# Guess the number

import random

print("Hello and welcome to my number guessing game!")
number = input("Please choose a number between 1 and 100.")

loop = True
while loop:
    rand = random.randint(1, 100)

    if number < rand:
        print("You guessed too low!")
    elif number > rand:
        print("You guessed too high!")
    break

print("You guessed correctly! My number was", rand)
