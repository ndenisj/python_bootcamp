import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", password="", database="pythondbclass")
mycursor = mydb.cursor()

mycursor.execute('CREATE TABLE student (NAME varchar (200), AGE int (11), CLASS varchar (50))') # Create a table
mycursor.execute('SHOW TABLES') # Show all tables
for tb in mycursor:
    print(tb)