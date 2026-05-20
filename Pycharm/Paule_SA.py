#Programmed by: Faith Paule
#Date: April 22, 2023

'''Write a PYTHON program to find the most frequent item of an array.
 Sample array :  arr1=[1, 'D', 'D', 'D', 2, 3, 'D', 3, 'D', 2, 7, 9, 3];
Sample Output : D (5 TIMES)'''

word = [1, 'D', 'D', 'D', 2, 3, 'D', 3, 'D', 2, 7, 9, 3]
word_list = word
word_tuple = tuple(word_list)
count = 0
frequency = 0
for i in word_tuple:
    if word_tuple.count(i) > count:
        count = word_tuple.count(i)
        frequency = i
print("\n===========================================================")
print("1st Activity")
print("\tSample Array: ", word_tuple)
print("\t", frequency, count, " times")



print("===========================================================")
print("2nd Activity")
phrase = input("\tEnter a phrase: ")
count2 = {}
for char in phrase:
    if char in count2:
        count2[char] += 1
    else:
        count2[char] = 1
print(count2)

leastchar = []
for i in count2:
    if count2[i] == 1:
        leastchar.append(i)

print("\tNot repeated character: ", leastchar)



print("===========================================================")
print("3rd Activity")
'''3.	A happy number is defined by the following process :
"Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers (or sad numbers)".
Write a PYTHON program to find and print the first 5 happy numbers. 
'''
start = int(input("\tEnter the starting number: "))
last = int(input("\tEnter the finishing number: "))
print("\tHappy Numbers: ")

for i in range(start, last + 1):
    sum = 0
    num = i
    while sum != 1 and sum != 4:
        sum = 0
        while num > 0:
            square = num % 10
            sum = sum + (square * square)
            num = num // 10
        num = sum
    if sum == 1:
        print("\t",i, end=" ")