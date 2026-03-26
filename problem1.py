class twoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"the vector is{self.i}+{self.j}")


class threeDvector(twoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
        print(f"the vector is{self.i}+{self.j}+{self.k}")


        
o=twoDvector(1,2)
o.show()
b=threeDvector(1,2,3)
b.show()