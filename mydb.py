
import mysql.connector
database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password'
)
# cursor object
cursor_object = database.cursor()

cursor_object.execute("CREATE DATABASE elderco")
print("All Done")
