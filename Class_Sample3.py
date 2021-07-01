
class Cat:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def hello(self):
        print("miou miou")


jack = Cat("jack", 4, "white")

jo = Cat("jo", 6, "black")

print(jack.name)

print(jo.name)
