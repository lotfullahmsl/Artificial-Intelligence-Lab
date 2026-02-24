from abc import ABC, abstractmethod
import math


class Shape(ABC):
    
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def calculate_area(self):
        pass
    
    def display_info(self):
        print(f"{self.name} - Area: {self.calculate_area():.2f}")


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width


class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2


class Cylinder(Shape):
    def __init__(self, radius, height):
        super().__init__("Cylinder")
        self.radius = radius
        self.height = height
    
    def calculate_area(self):
        # Surface area: 2πr(r + h)
        return 2 * math.pi * self.radius * (self.radius + self.height)


# Test the classes
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    square = Square(4)
    circle = Circle(3)
    cylinder = Cylinder(3, 7)
    
    
    rect.display_info()
    square.display_info()
    circle.display_info()
    cylinder.display_info()
