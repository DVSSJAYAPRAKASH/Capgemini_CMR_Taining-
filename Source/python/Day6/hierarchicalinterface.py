class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14* (self.radius**2)
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
class Rectangle(Shape):
    def __init__(self,lenght,breadth):
        self.length=lenght
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
def main():
    circle=Circle(4)
    print(f"Area of a Circle: {circle.area()}")
    square=Square(5)
    print(f"Area of a Square: {square.area()}")
    rectangle=Rectangle(10,8)
    print(f"Area of Rectangle: {rectangle.area()}")
main()