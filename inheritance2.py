class Parent:
    def __init__(self):
        self.a = 10

class Child(Parent):
    def __init__(self):
        self.b = 20

p = Parent()
c = Child()

print(c.a)   # ❌ ERROR
# error hai baad main puchanea
 