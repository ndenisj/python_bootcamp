import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", password="", database="pythondbclass")
mycursor = mydb.cursor()

insertQuery = "INSERT INTO student (NAME, AGE, CLASS) VALUES (%s, %s, %s)"
# name = input("Enter your name? ")
# age = input("Enter your name? ")
# class_ = input("Enter your name? ")
students = [("Adebayo", 25, "JSS2 Python"), ("Obaji", 20, "JSS1 Django"), ("Okorie", 18, "JSS1 Flutter"),]

mycursor.executemany(insertQuery, students)

mydb.commit() # save the data in the table