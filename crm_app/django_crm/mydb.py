import mysql.connector

database = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "Hello#123"
)

# cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE TABOT")

print("all done")