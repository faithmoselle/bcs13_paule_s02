for i in range(1, 101):
    if i % 3 == 0:
        print(i, ") BSCS")
    elif i % 5 == 0:
        print(i, ") DLSUD")
    elif i % 3 == 0 and i % 5 == 0:
        print(i, ") DLSUDBSCS")
    else:
        print(i, ")")
