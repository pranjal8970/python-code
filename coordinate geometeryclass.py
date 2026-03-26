class line:
      def __init__(self,A,B,C):
            self.A=A
            self.B=B
            self.C=C
      def __str__(self):
              return f"{self.A}x+{self.B}y+{ self.C}"

      def check_online(self,point):
            if(self.A*point.x_cod+self.B*point.y_cod+self.C==0):
                return "lies on line"
            else:
                 return "not lies on line"
               
         


class Point:

    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return f"<{self.x_cod},{self.y_cod}>"
    def euclidean_distance(self,other):

        return ((self.x_cod-other.x_cod)**2+(self.y_cod-other.y_cod)**2)**0.5

    def distance_from_origin(self):
        return ((self.x_cod-0)**2+(self.y_cod-0)**2)**0.5
p1 = Point(0, 0)
p2 = Point(1,1)
print(p1.euclidean_distance(p2))
print(p2.distance_from_origin())

print(p1)
l1=line(2,3,4)
print(l1)
print(l1.check_online(p2))