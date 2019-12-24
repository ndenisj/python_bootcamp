import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", password="")

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE pythondbclass") # SQL Query to create a new Database
mycursor.execute('SHOW DATABASES') # Display the list of all database in the server
for db in mycursor:
    print(db)