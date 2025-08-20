from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2


if __name__ == '__main__':
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    print(circle.get_area())
    print(rectangle.get_area())
    print(rectangle.get_perimeter())
