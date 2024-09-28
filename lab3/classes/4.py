import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return distance

t = int(input())
z = int(input())
t1 = int(input())
z2 = int(input())
p1 = Point(t, z)
p2 = Point(t1, z2)

p1.show() 
p2.show()  

p1.move(23, 52) 
p1.show()  

distance = p1.dist(p2)
print(distance)
