class Car:
    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f'{self.brand} едет!')

    def stop(self):
        print(f'{self.brand} остановился!')

    def repaint(self, new_color):
        self.color = new_color
        print(f'Автомобиль: {self.brand} теперь в цвете: {self.color}.')


# Создаём объекты с разными марками и цветами
if __name__ == '__main__':
    my_car = Car('Toyota', 'red')
    friend_car = Car('Ford', 'blue')

    my_car.drive()
    my_car.stop()
    print()
    friend_car.drive()
    friend_car.stop()

    my_car.repaint('black')
    print(my_car.color)
