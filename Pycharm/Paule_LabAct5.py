println = []
print(" ")
start = int(input("Enter the starting year: "))
last = int(input("Enter the last year: "))
print("Leap Years from 2000 to the Present Year, 2023: ")
for year in range(start, last):
    if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
        println.append(str(year))
print(', '.join(println))
