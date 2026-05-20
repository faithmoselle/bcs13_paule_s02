import mysql.connector


def login(username, password):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="loginform"
    )

    cursor = connection.cursor()

    query = "SELECT * FROM logindatabase WHERE username = %s AND password = %s"
    values = (username, password)
    cursor.execute(query, values)

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if user:
        return True
    else:
        return False


username = input("Username: ")
password = input("Password: ")

if login(username, password):
    print("Successful login!")
else:
    print("INVALID USERNAME/PASSWORD.")