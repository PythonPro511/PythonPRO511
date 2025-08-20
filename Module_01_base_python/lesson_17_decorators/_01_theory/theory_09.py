class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        if type(new_radius) in [int, float]:
            self.__radius = new_radius
        else:
            print('Ошибка типа данных!')


if __name__ == '__main__':
    circle = Circle(5)
    print(circle.radius)
    circle.radius = "10"
    print(circle.radius)
    circle.radius = 15
    print(circle.radius)

