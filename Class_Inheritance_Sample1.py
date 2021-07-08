
class Animal:
        def __init__(self, name, age, weight):
            self.name = name
            self.age = age
            self.weight = weight

        def move(self):
            print('i can move')

        def make_noise(self):
            print('this is my voice')


class Reptile(Animal):
    def __init__(self, name, age, weight, home):
        super().__init__(name, age, weight)
        self.home = home

turtle = Reptile('lucky', 300, 400, 'land')
print(turtle.home)
