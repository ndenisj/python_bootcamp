import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", password="", database="pythondbclass")
mycursor = mydb.cursor()

deleteQuery = "DELETE FROM student WHERE NAME='Obaji'"
mycursor.execute(deleteQuery)

mydb.commit()