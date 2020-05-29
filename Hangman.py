# Hangman

print("Welcome to hangman!")
# print("Choose your level: easy, medium, hard.")

easy_file = open("easy_words.txt", 'r')
easy = easy_file.readlines()

newList = []
for line in easy:
    if line[-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append(line)
print(newList)