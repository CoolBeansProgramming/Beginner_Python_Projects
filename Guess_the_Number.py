# Guess the number

import random

print("Hello and welcome to my number guessing game!")
number = int(input("Please choose a number between 1 and 100: "))

rand = random.randint(1, 100)

loop = True
while loop:

    if number < rand:
        print("You guessed too low!")
    elif number > rand:
        print("You guessed too high!")
    elif number == rand:
        print("You guessed correctly! My number was", rand)
    break



