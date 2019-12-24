import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", password="", database="pythondbclass")
mycursor = mydb.cursor()

selectQuery = "SELECT * FROM student"
# selectQuery = "SELECT * FROM student WHERE NAME = 'Okorie'"
mycursor.execute(selectQuery)

myresult = mycursor.fetchall()
for result in myresult:
    print(result)