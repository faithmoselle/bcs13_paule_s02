#Programmed by Faith Paule
'''Part 1'''
odd = [1, 3, 5, 7]
# Prints the unmodified odd
print(odd) #[1, 3, 5, 7]
# Prints the index 2 of the list
print(odd[2]) #5
# odd[4] prints index 4 - nonexistent
print(odd[4])
# len - returns the number of items in the container
print(len(odd)) #4
number = odd[1]
# Prints 'number' or index 1 on the list
print(number) #3
# Modified index 1 of odd
odd[1]=2
# Prints the modified elements of the dictionary, odd
print(odd) #[1, 2, 5, 7]
# Prints dictionary odd's index 1 before the modification
print(number) #3
'''Part 2'''
'''
elements = {'C': 'carbon', 'H': 'hydrogen', 'O': 'oxygen', 'N': 'nitrogen'}
print(type(elements))
print(elements.keys())
print(elements.values())
print(elements['C'])
atom = 'N'
print(elements[atom])
print(elements[N])
print(elements['nitrogen'])
print(elements[1])
print(len(elements))
elements['B'] = 'Boron'
print(elements.items())'''

