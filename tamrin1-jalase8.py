class Vehicle:
    def __init__(self, name, type, speed, fuel, weight, capacity):
        self.name = name
        self.type = type
        self.speed = speed
        self.fuel = fuel
        self.weight = weight
        self.capacity = capacity

    def move(self):
        print("i move in {}".format(self.type))

    def info(self):
        print("my name is {} and my operation zone is {}"
              .format(self.name, self.type))


class Car(Vehicle):
    def __init__(self, name, type, speed, fuel, weight, capacity,
        engine_power, cylinders_count):
        super().__init__(name, type, speed, fuel, weight, capacity)
        self.engine_power = engine_power
        self.cylinders_count = cylinders_count

    def start(self):
        print("car engine started!")

class Motorcycle(Vehicle):
    def __init__(self, name, type, speed, fuel, weight, capacity,
        jump_height):
        super().__init__(name, type, speed, fuel, weight, capacity)
        self.jump_height = jump_height

    def jump(self):
        print("maximum height of my jump is {}".format(self.jump_height))


class Airplane(Vehicle):
    def __init__(self, name, type, speed, fuel, weight, capacity,
        flight_height):
        super().__init__(name, type, speed, fuel, weight, capacity)
        self.flight_height = flight_height

    def fly(self):
        print("maximum height of my flight is {}".format(self.flight_height))

print("------------------------------------------")

car = Car('car', 'land', 240, 60, 400, 4, 1800, 4)
car.info()
car.start()
car.move()

print("------------------------------------------")

motorcycle = Motorcycle('motorcycle', 'land', 100, 20, 120, 2, 5)
motorcycle.info()
motorcycle.move()
motorcycle.jump()

print("------------------------------------------")

airplane = Airplane('airplane', 'sky', 1200, 3500, 4000, 300, 1500)
airplane.info()
airplane.move()
airplane.fly();

print("------------------------------------------")
