from abc import ABC,abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
def main():
    circle=Circle(2)
    print(f"The area of circle is: {circle.area()}")
    rectangle=Rectangle(2,3)
    print(f"The area of Rectangle is :{rectangle.area()}")
main()

