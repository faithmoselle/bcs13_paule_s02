n = input("Enter n: ")
n = int(n)

for i in range(0, 2 ^ n):
    i = bin(i)[2:]  # starting from 0b
    print(i)
