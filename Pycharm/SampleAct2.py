# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Activity #2
# Perform Arithmetic Operators:
# Quarter(25), Dime(10), Nickels(5), Penny(1)

num = int(input("Enter a number: "))

quarter = num//25
num = num % 25
dime = num//10
num = num % 10
nickels = num//5
num = num % 5
penny = num//1
num = num % 1
print("Quarter: ", quarter)
print("Dime: ", dime)
print("Nickels: ", nickels)
print("Penny: ", penny)