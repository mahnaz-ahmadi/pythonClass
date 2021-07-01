import sqlite3

connection = sqlite3.connect("testDb.sqlite")

cursor = connection.cursor()

first_name = input("input your first name : ")
last_name = input("input your last name : ")

query = f'insert into person values("{first_name}", "{last_name}")'

cursor.execute(query)

connection.commit()
connection.close()

connection = sqlite3.connect("testDb.sqlite")

cursor = connection.cursor()

query = f'select * from person'
result = cursor.execute(query)

for item in result:
   print(item[0], item[1])

connection.commit()
connection.close()
