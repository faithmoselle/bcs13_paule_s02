#Programmed by Faith Paule
'''Laboratory Activity #4
Create a 5-user input list that accept either string or number then select an item randomly from a list and remove the selected item randomly in the list. Submit a pdf file(LabAct4_Surname) that contains the explanation of the code and include 3 sample output screenshot and python file.
'''
import random

#List of items
list = []
for i in range(5): #Accept 5 user input
    userinput = input("Enter a string or a number: ")
    list.append(userinput)

#Select random item
print("List of user input: ", list)
random = random.choice(list)
#Remove item from the list
remove_item = list.remove(random)
#Prints the item removed
print("Item that has been removed from the list: ", random)
#Prints the items left from the list
print("Modified List: ", list)