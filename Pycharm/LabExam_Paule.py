#Programmed by: Faith Paule
#March 14, 2024
#2nd Semester - S-ITCS227LA

'''Laboratory Exam
Create Python program that generates Fibonacci number sequence and find their square in the given sequence based on the user input.
Condition:  • Fibonacci sequence should be in list format • User Input should be only positive input. If the user puts a negative value, it should be an output that accept only positive input.
Submit a two-sample output screenshot and the python code(LabExam Surname) only.
Rubrics: Meet the condition = 10 pts each condition Execute the code properly = 20 pts

'''
def fibonacci_series(n): #It takes a positive integer n as input.
    """Generates the Fibonacci sequence of n numbers."""
    fib_sequence = [0, 1]  # Initialize the sequence with the first two numbers

    for i in range(2, n): #It creates a list fib_sequence and initializes it with the first two Fibonacci numbers (0 and 1). It returns the fib_sequence list.
        next_num = fib_sequence[i - 1] + fib_sequence[i - 2]  # Calculate the next number
        fib_sequence.append(next_num)  # Add it to the sequence

    return fib_sequence

# Get user input
while True: #It keeps prompting the user until a positive integer is entered.
    try:
        num = int(input("Enter the number of Fibonacci numbers: "))
        if num > 0:
            break
        else:
            print("Invalid input. Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Generate the Fibonacci sequence
fib_sequence = fibonacci_series(num) #fibonacci_series function is called to generate the sequence. The sequence is printed as a list.

# Print the sequence and squares
print("Fibonacci sequence of", num, "numbers:")
print("fib_sequence:", fib_sequence)

for i in range(1, num + 1): #iterates through the sequence, calculates the square of each number, and prints them in a list format.
    square = fib_sequence[i - 1] ** 2
    print("Fibonacci number({0}): {1}, Square: {2}".format(i, fib_sequence[i - 1], square))