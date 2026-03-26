class customer:
     def __init__(self,name,gender,address):
          self.name=name
          self.gender=gender
          self.address=address

     def print_address(self):
        print( self.address.get_city(),self.address.pin,self.address.state)
        
     
class address:
     def __init__(self,city,pin,state):
          self.__city=city
          self.pin=pin
          self.state=state

     def get_city(self):
          return self.__city


add1=address('varansi',221202,'utterpradesh')
cust=customer('pranjla','male',add1)
cust.print_address()