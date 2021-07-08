
class A:
    def __init__(self, name):
        self.name = name


class B(A):
    def __init__(self, name):
        super().__init__(name)

class C(B):
    def __init__(self, name):
        super().__init__(name)


child = C("mahnaz")
print(child.name)
