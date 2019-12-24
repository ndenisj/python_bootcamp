import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", password="")

if mydb:
    print("Connection Successful")
else:
    print("Error Connecting TO DB")
