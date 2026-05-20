def polynomial(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                print(f"({i}, {j}, {k})")


n = int(input("Enter n: "))
polynomial(n)
