"""
Агрегация
"""
class Body:

    def __init__(self, body_type):
        self.body_type = body_type

    def display_body_type(self):
        print(f'Материал корпуса: {self.body_type}')

    def check_body(self):
        return f'Мы проверили корпус из {self.body_type}'

    def __str__(self):
        return f'Материал корпуса: {self.body_type}'


class Engine:

    def __init__(self, engine_type):
        self.engine_type = engine_type

    def display_engine_type(self):
        print(f'Тип двигателя: {self.engine_type}')

    def start_engine(self):
        return f'Мы запустили двигатель: {self.engine_type}'

    def __str__(self):
        return f'Тип двигателя: {self.engine_type}'


class Wheels:

    def __init__(self, wheels_type):
        self.wheels_type = wheels_type

    def display_wheels_type(self):
        print(f'Шасси самолета: {self.wheels_type}')

    def go_to_start(self):
        return f'Самолет на {self.wheels_type} колеса, выехал на взлетную полосу'

    def __str__(self):
        return f'Шасси самолета: {self.wheels_type}'


class Plane:

    def __init__(self, body: Body, engine: Engine, wheels: Wheels):
        self.body = body
        self.engine = engine
        self.wheels = wheels

    def display_plane(self):
        print(self.body)
        print(self.engine)
        print(self.wheels)

    def go_to_fly(self):
        print(self.body.check_body())
        print(self.engine.start_engine())
        print(self.wheels.go_to_start())


if __name__ == '__main__':
    plane_body = Body('Пластик')
    plane_engine = Engine('Электро')
    plane_wheels = Wheels('Резиновые')

    plane = Plane(plane_body, plane_engine, plane_wheels)
    plane.display_plane()
    print()
    plane.go_to_fly()
