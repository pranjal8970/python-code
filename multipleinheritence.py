class Employee:
    company = "itc"
    abs="pranjal"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class coder:
    language = "python"

    def printlanguage(self):
        print(f"Out of all languages, here is your language {self.language}")


class Programmer(Employee, coder):
    company = "itcinfotech"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


print(Employee.company, Programmer.company,Programmer.abs8)
