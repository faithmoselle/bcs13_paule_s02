#Programmed by: Faith Paule
#March 11, 2024
#Second Semester A.Y. 2023-2024

#Palindrome explanation
print("Palindrome is a word, sentence, verse, or even number that reads the same backward or forward.")
#function which return reverse of a string
def isPalindrome(input):
    return input == input[::-1]

# Driver code
user_input = input("Enter a string or number: ") #request for user input
palindrome_result = isPalindrome(user_input) #palindrome_result is the variable that calls the function and perform the assignement

#if-else statement used for conditional statement
if palindrome_result:
    print("\tResult: PALINDROME")
else:
    print("\tResult:NOT PALINDROME")