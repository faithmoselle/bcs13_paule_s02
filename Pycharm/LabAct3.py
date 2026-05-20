#Calculate the sum of the digits in an integer

num = int(input("Enter a number: "))
total = 0
while num>0:
    total += num%10
    num//=10

print("The sum of the digits: ", total)

