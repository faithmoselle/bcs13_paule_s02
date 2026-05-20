# Perform Arithmetic Operators:
# Quarter(25), Dime(10), Nickels(5), Penny(1)

sec = int(input("Enter Seconds: "))

years = sec//31536000
sec = sec%31536000
weeks = sec//604800
sec = sec%604800
days = sec//86400
sec = sec%86400
hours = sec//3600
sec = sec%3600
mins = sec//60
sec = sec%60
seconds = sec//1
sec = sec%1
print(" ")
print("Years: ", years)
print("Weeks: ", weeks)
print("Days: ", days)
print("Hours: ", hours)
print("Minutes: ", mins)
print("Seconds: ", seconds)
