#create class
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def display(self):
        print(f"Point:({self.x},{self.y})")

    def move(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy
        print(f"After move:({self.x},{self.y})")

    def distance_from_origin(self):
        distance=(self.x**2+self.y**2)**0.5
        print(f"Distance from origin:{distance:.2f}")

#object creation
values=Point(4,6)

#call methods
values.display()
values.move(3,2)
values.distance_from_origin()