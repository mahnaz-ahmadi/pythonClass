
class Cat:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def hello(self):
        print("hello my name is {} and {} years old".format(self.name, self.age))

    def change_name(self, new_name):
       self.name = new_name


cat1 = Cat("jack", 4, "white")
cat1.hello()

cat1.change_name("jo")
cat1.hello()
