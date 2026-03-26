class person:
    def __init__(self,name_input,country_input):
        self.name=name_input
        self.country=country_input

p1=person('nitesh','india')
p2=person('steve','australia')
l1=[p1,p2]
print(l1)
print(p1)

class Atm:

    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        userinput = input("""
Hi how can i help you!!
1. press 1 to create pin
2. press 2 to change pin
3. press 3 to check balance
4. press 4 to withdraw
5. Anything else to exit
""")

        if userinput == "1":
            self.create_pin()

        elif userinput == "2":
            self.change_pin()

        elif userinput == "3":
            self.check_balance()

        elif userinput == "4":
            pass

        else:
            exit()

    def create_pin(self):
        user_pin = input("enter your pin: ")
        self.pin = user_pin

        user_balance = int(input("enter balance: "))
        self.balance = user_balance

        print("pin created successfully")
        self.menu()

    def change_pin(self):
        old_pin = input("enter the old pin: ")

        if old_pin == self.pin:
            new_pin = input("enter new pin: ")
            self.pin = new_pin
            print("pin change successfully")
        else:
            print("wrong pin")

        self.menu()

    def check_balance(self):
        user_pin = input("enter your pin: ")

        if user_pin == self.pin:
            print(f"your balance is {self.balance}")
        else:
            print("chal nikal yaha se")

        self.menu()



