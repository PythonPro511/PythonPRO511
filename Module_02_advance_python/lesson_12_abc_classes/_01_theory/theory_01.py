from abc import ABC, abstractmethod


class Shape(ABC):
    pass


class Circle(Shape):
    pass


class Square(Shape):
    pass


if __name__ == '__main__':
    circle = Circle()
    square = Square()
