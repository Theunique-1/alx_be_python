import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area() method")
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.lenth * self.width

class Circle(Shape):
    def init(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2
