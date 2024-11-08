import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Paroli12"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE eldarco")

print("Done")