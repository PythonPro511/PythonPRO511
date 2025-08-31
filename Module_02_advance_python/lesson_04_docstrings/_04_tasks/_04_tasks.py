class Rectangle:
    """
    Represents a rectangle with width and height.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Methods:
        area() -> float:
            Calculates and returns the area of the rectangle.

        perimeter() -> float:
            Calculates and returns the perimeter of the rectangle.
    """

    def __init__(self, width: float, height: float):
        """
        Initializes the rectangle with the given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        if not (isinstance(width, float) or isinstance(height, float)):
            raise TypeError(
                f"""Ожидаемый тип данных: float
                Получено: width > {type(width).__name__}, height > {type(height).__name__}"""
            )
        self.width = width
        self.height = height

    def calculate_area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle (width * height).
        """
        return self.width * self.height

    def calculate_perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle (2 * (width + height)).
        """
        return 2 * (self.width + self.height)


if __name__ == '__main__':
    rectangle = Rectangle(6.0, 5.0)
    print(rectangle.calculate_area())
    print(rectangle.calculate_perimeter())
    print(Rectangle.__doc__)
    print(rectangle.calculate_perimeter.__doc__)
    print(rectangle.calculate_perimeter.__doc__)

    # rectangle = Rectangle(5, 3)
