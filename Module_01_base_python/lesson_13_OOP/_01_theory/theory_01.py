class Car:

    def __init__(self, brand, color):
        self.brand = brand
    #   my_car.brand
        self.color = color
        print(f'Объект класса Car: {self.brand}, {self.color} создан')


# Создаём объекты с разными марками и цветами
if __name__ == '__main__':
    my_car = Car('Toyota', 'red')
    friend_car = Car('Ford', 'blue')

    print(my_car.brand)
    print(my_car.color)
    print()
    print(friend_car.brand)
    print(friend_car.color)
