class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l
x = int(input())
aSquare =  Square(x)
print(aSquare.area)