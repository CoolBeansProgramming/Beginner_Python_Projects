# Hangman

import random

def game(f):
    newList = []
    for line in f:
        if line[-1] == '\n':
            newList.append(line[:-1])
        else:
            newList.append(line)
    word = random.choice(newList)
    print(word)
    guess = input("Make your first guess: ")
    if guess in word:
        print("Good guess! The letter", guess, "is in the word.")
    else:
        print("The letter", guess, "is not in the word.")

print("Welcome to hangman!")
level =input("Choose your level: easy, medium, hard. ")


if level == 'easy':
    file = open("easy_words.txt", 'r')
    f = file.readlines()
    game(f)

elif level == 'medium':
    file = open("medium_words.txt", 'r')
    f = file.readlines()
    game(f)

elif level == 'hard':
    file = open("hard_words.txt", 'r')
    f = file.readlines()
    game(f)

else:
    print("Please select easy, medium, or hard. ")

