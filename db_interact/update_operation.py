import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", password="", database="pythondbclass")
mycursor = mydb.cursor()

updateQuery = "UPDATE student SET CLASS='SS1 Flutter' WHERE NAME='Okorie'"
mycursor.execute(updateQuery)

mydb.commit()