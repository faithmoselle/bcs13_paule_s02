'''Laboratory Activity No.5
Part 1: Sum of the items in a Dictionary Given Dictionary: my_dict = {'a': 25, 'b': 5, 'c': 100, 'd': 11, 'e': 12,'f':40} Find the Sum all the items in a dictionary.
Part 2: Product of the items in a Dictionary Given the values in part 1, find the product of the all items
Submit a pdf file(LabAct5 Surname) that contains the Explanation of the code and include the screenshot of code output and python files.

'''
my_dict = {'a': 25, 'b': 5, 'c': 100, 'd': 11, 'e': 12, 'f': 40}
values =my_dict.values()
print("Items in the dictionary: ", values)
#Part 1
def Sum(dict): #Method in getting the total of the values in the dictionary
    addend = dict.values() #Gets the values from the dictionary
    total = sum(addend)  # 193
    print("\nPart 1\nSum of all values in the dictionary: ", total) #Print the total of the values in the dictionary

Sum(my_dict)

#Part 2
def Product(dictionary): #Method in getting the product of the elements in the dictinary
    elements = dictionary.values() #Gets the values from the dictionary
    multiplier = 1
    for i in elements: #Scan through all the values in the dictionary
        multiplier = multiplier * i
    print("\nPart 2\nProduct of all values in the dictionary: ", multiplier)

Product(my_dict)