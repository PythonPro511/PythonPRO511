class Car:
    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


# Создаём объекты с разными марками и цветами
if __name__ == '__main__':
    my_car = Car('Toyota', 'red')
    friend_car = Car('Ford', 'blue')

    print(Car.wheels)
    print(my_car.wheels)
    print(friend_car.wheels)
    my_car.wheels = 3
    print(Car.wheels)
    print(my_car.wheels)
    print(friend_car.wheels)