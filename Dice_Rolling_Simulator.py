# Dice Rolling Simulator

import random
print("Welcome to Dice Rolling Simulator")

loop = True
while loop:
    rand = random.randint(1,6)
    print("You rolled a", rand)
    ans = input("Would you like to roll again (y=yes, n=no)? ")
    if ans == 'n':
        break
