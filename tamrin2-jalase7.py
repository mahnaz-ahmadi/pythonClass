import sqlite3

class Person:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def create(self):
        connection = sqlite3.connect("testDb.sqlite")

        cursor = connection.cursor()

        query = f'CREATE TABLE IF NOT EXISTS Person (first_name TEXT,last_name TEXT,email TEXT,age INTEGER)'

        cursor.execute(query)

        connection.commit()
        connection.close()



    def save(self):
        self.create()

        print("hello my name is {} and {} years old. my email address is {} ".format(self.first_name + " "  + self.last_name, self.age, self.email))

        connection = sqlite3.connect("testDb.sqlite")

        cursor = connection.cursor()

        query = f'insert into person values("{self.first_name}", "{self.last_name}", "{self.email}", "{self.age}")'

        cursor.execute(query)

        connection.commit()
        connection.close()

        print("data saved in db")

        connection = sqlite3.connect("testDb.sqlite")

        cursor = connection.cursor()

        query = f'select * from person'
        result = cursor.execute(query)

        for item in result:
           print(item[0], item[1], item[2], item[3])

        connection.commit()
        connection.close()


new_person = Person("baran", "ahmadi", "baran.ahmadi@gmail.com", 4)
new_person.save();
