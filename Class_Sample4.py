
class Cat:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def hello(self):
        print("hello my name is {} and {} years old".format(self.name, self.age))


jack = Cat("jack", 4, "white")
jack.hello()

jo = Cat("jo", 6, "black")
jo.hello()
