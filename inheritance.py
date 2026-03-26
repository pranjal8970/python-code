class user:
    def __init__(self):
        self.name='netish'
    def login(self):
        print('login')

    
    
class student(user):
    def __init__(self):
        self.rollno=100
    def enroll(self):
        print('enroll into the cour')

u=user()
s=student()
print(s)