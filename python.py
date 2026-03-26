class Employee:
    company = "itc"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class Programmer:
    company = "itcinfotech"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class ShowLanguage:
    def showlanguage(self):
        print(f"The name is {self.name} and he is a good language programmer")


print(Employee.company, Programmer.company)

