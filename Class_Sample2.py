
class Cat:
    name = ""
    age = 0
    color = ""

    def hello(self):
        print("miou miou")


jack = Cat()
jack.name = "jack"
jack.age = 4
jack.color = "white"

jo = Cat()
jo.name = "jo"
jo.age = 4
jo.color = "black"

print(jack.name)
jack.hello()

print(jo.name)
jo.hello()
