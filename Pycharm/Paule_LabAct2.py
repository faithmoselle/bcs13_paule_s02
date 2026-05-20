word = input("Enter a phrase: ")
letter = input("Enter a letter within the word for counting: ")
count = 0
i = 0
while i < len(word):
    if word[i] == letter.lower() or word[i] == letter.upper():
        count = count + 1
    i = i + 1
print(letter, " was repeated ", str(count), " times.")
