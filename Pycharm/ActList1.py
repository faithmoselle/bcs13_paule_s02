'''Laboratory Activity No. 3
Filename: ActListl.py
Create a 5-input based that accept numbers and find sum, average and the smallest number of List in Python.
Note: use sum() function in adding the list and use len() in finding the average of the list.
Submit a pdf file(LabAct3_Surname) that contains the explanation of the code , include sample output screenshot and python file '''

my_list= []

for i in range (5):
    num = int(input("Input Numbers: "))
    my_list.append(num)

total = sum(my_list)
average = total/len(my_list)
smallest = min(my_list)

print ("The sum of the list is :" , total)
print ("The average of the list is :", average)
print ("The smallest number in the list is :", smallest)

