
class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


e = Employee()
e.a = 45          # instance variable
e.name = "harry"

print(e.name)
e.show()
