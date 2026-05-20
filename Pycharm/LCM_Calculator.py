"""
LCM Calculator Program - MATH200

Authors:
- Claire Cecilio
- Brian Garilao
- Greg Lagarto
- Faith Paule

Created by GROUP 01 - BCS23 on December 18, 2023.

The LCM Program - MATH200 is a Python script designed to
calculate the Least Common Multiple (LCM) of a set of integers.

"""


def gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The GCD of the two input integers.
    """
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    """
    Calculate the least common multiple (LCM) of two numbers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The LCM of the two input integers.
    """
    return abs(a * b) // gcd(a, b)


def multiple_lcm(*args):
    """
    Calculate the least common multiple (LCM) of multiple numbers.

    Args:
        *args (int): Variable number of integers.

    Returns:
        int: The LCM of the input integers.
    """
    if len(args) < 2:
        raise ValueError("MINIMUM of 2 numbers required for LCM Calculation.")

    result = args[0]
    for num in args[1:]:
        result = lcm(result, num)

    return result


def get_user_input():
    """
    Get user input for a list of numbers.

    Returns:
        list: A list of integers entered by the user.
    """
    try:
        input_str = input("Enter numbers separated by spaces. Type 'X' to terminate: ")
        if input_str.lower() == 'x':
            return None
        else:
            numbers = [int(x) for x in input_str.split()]
            return numbers
    except ValueError:
        print("\nInvalid input. Please enter valid integers.\n")
        return get_user_input()


def format_with_spaces(number):
    """
    Format an integer with commas for better readability.

    Args:
        number (int): The integer to be formatted.

    Returns:
        str: The formatted string.
    """
    return "{:,}".format(number)


def main():
    """
    Main program to interactively calculate the LCM of user-provided numbers.
    """
    print("WELCOME TO THE LCM CALCULATOR PROGRAM!")

    while True:
        try:
            user_input = input("\nDo you want to calculate LCM? (Y/N): ").lower()
            if user_input != 'y':
                print("Program terminated.")
                break

            numbers = get_user_input()
            if numbers is None:
                print("Program terminated.")
                break

            result = multiple_lcm(*numbers)
            formatted_numbers = [format_with_spaces(num) for num in numbers]
            formatted_result = format_with_spaces(result)

            print(f"\nThe LCM of {', '.join(formatted_numbers)} is: {formatted_result}")

        except ValueError as ve:
            print(f"Error: {ve}")

    print("Thank you for using the LCM Calculator!")
    print("PROGRAM ENDING...\n")


if __name__ == "__main__":
    main()
