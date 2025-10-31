class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_age(self, value):
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = value

    def __str__(self):
        return f"User: {self.get_name()}\nage: {self.get_age()}"


if __name__ == '__main__':
    user = User(name='Иван', age=35)
    print(user.get_name())
    print(user.get_age())
    user.set_age(36)
    print(user.get_age())
    try:
        user.set_age(-1)
    except ValueError as ve:
        print(ve)
