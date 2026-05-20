# Write a Python program that accepts a
# sequence of comma-separated numbers from the user and
# generates a list and a tuple of those numbers.

#Sample data: 3, 5, 7, 23

num = [input("Input some comma seperated Numbers: ")]
num_list = (num)
num_tuple = tuple(num_list)
print ("List: " ,num)
print ("Tuple: " ,num_list)