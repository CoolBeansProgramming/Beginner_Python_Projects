# Hangman

import random

def game():
    newList = []
    for line in f:
        if line[-1] == '\n':
            newList.append(line[:-1])
        else:
            newList.append(line)
    print(random.randint(1,len(newList)))
    print(len(newList))
    g =input("Make your first guess: ")

print("Welcome to hangman!")
level =input("Choose your level: easy, medium, hard. ")

if level == 'easy':
    file = open("easy_words.txt", 'r')
    f = file.readlines()
    game()

elif level == 'medium':
    file = open("medium_words.txt", 'r')
    f = file.readlines()
    game()

elif level == 'hard':
    file = open("hard_words.txt", 'r')
    f = file.readlines()
    game()

else:
    print("Please select easy, medium, or hard. ")

