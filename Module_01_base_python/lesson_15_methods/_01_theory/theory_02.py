class Car:
    wheels = 4  # атрибут класса

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f'{self.brand} {self.color} едет!')

    @classmethod
    def describe(cls):
        print(f'Все машины данного класса имеют: {cls.wheels} колеса')


if __name__ == '__main__':
    # car = Car('Toyota', 'red')
    # car.drive()
    Car.describe()
