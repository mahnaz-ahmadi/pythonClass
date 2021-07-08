
class Lady:
        def __init__(self, name, age, education):
            self.name = name
            self.__age = age
            self.education = education


lady = Lady('Maryam', 30, 'mc')
print(lady.age)
