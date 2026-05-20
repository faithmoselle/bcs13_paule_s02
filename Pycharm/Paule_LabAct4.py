# Computation to validate if numbers are armstrong/not
# 3**3 + 7**3 + 1**3 = 371
num = int(input("Enter a 3 digit number: "))
output = 0
temp = num
while temp > 0:
    digit = temp % 10
    output = output + digit ** 3
    temp //= 10

if num == output:
    print(num, "is an Armstrong Number.")
else:
    print(num, "is not an Armstrong Number.")
