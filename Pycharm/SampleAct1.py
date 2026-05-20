# Perform Arithmetic Operators:
# + - * % // **

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
total = int(num1)+int(num2)
print("The total is " + str(total))
diff = int(num1)-int(num2)
print("The difference is " + str(diff))
prod = int(num1)*int(num2)
print("The product is " + str(prod))
quot = float(num1)/float(num2)
print("The quotient is " + str(quot))
rem = float(num1)%float(num2)
print("The remainder is " + str(rem))
smalldiv = float(num1)//float(num2)
print("The result is " + str(smalldiv))
expo = float(num1)**float(num2)
print("The result is " + str(expo))
