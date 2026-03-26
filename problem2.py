class amimals:
    pass
class pets(amimals):
    pass
class dog(pets):
    @staticmethod
    def bark():
        print("bow bow")

d=dog()
d.bark()