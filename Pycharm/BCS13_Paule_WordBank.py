'''Write a Word Bank program.
The program will ask the use to enter a word
The program will store the word in a List
The program will ask if the user wants to try again. The user will input y/Y if Yes and n/N if No
If yes, refer to step 2
If No, display the total number of words and all the words that the user entered.
'''
ans = "Y"
wordbank = list()
while ans.lower() == "y":
    word = str(input("Enter a word: "))
    wordbank.append(word)
    ans = str(input("Do you wish to try again?Y/N: "))
print(" ")
print(f"Total number of words: {len(wordbank)}")
print("Word in the list: ")
for i in wordbank:
    print(i)