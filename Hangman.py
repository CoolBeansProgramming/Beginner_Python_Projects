# Hangman

def easy():
    easy_file = open("easy_words.txt", 'r')
    easy = easy_file.readlines()

    newList = []
    for line in easy:
        if line[-1] == '\n':
            newList.append(line[:-1])
        else:
            newList.append(line)
    print(newList)

def medium():
    easy_file = open("easy_words.txt", 'r')
    easy = easy_file.readlines()

    newList = []
    for line in easy:
        if line[-1] == '\n':
            newList.append(line[:-1])
        else:
            newList.append(line)
        print(newList)

def hard():
    easy_file = open("easy_words.txt", 'r')
    easy = easy_file.readlines()

    newList = []
    for line in easy:
        if line[-1] == '\n':
            newList.append(line[:-1])
        else:
            newList.append(line)
        print(newList)

print("Welcome to hangman!")
level =input("Choose your level: easy, medium, hard. ")

if level == 'easy':
    easy()
elif level == 'medium':
    medium()
elif level == 'hard':
    hard()

