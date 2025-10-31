class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = value

    def __str__(self):
        return f"User: {self.name}\nage: {self.age}"


if __name__ == '__main__':
    user = User(name='Иван', age=35)
    print(user.name)
    print(user.age)
    user.age = 36
    print(user.age)
    try:
        user.age = -1
    except ValueError as ve:
        print(ve)
    print(user)
