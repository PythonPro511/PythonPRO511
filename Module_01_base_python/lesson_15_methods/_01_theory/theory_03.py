class Car:
    wheels = 4  # атрибут класса
    cars = []

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        Car.cars.append(self)

    def drive(self):
        print(f'{self.brand} {self.color} едет!')
        Car.general_info()

    @classmethod
    def describe(cls):
        print(f'Все машины данного класса имеют: {cls.wheels} колеса')

    @classmethod
    def display_all_cars(cls):
        for car in cls.cars:
            print(car.brand, car.color)

    @staticmethod
    def general_info():
        print(f'Машины это транспортные средства.')


if __name__ == '__main__':
    # Car.describe()
    Car.general_info()
    car1 = Car('Toyota', 'red')
    # car1.drive()
    car2 = Car('Honda', 'blue')
    Car.display_all_cars()
