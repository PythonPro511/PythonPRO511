class Student:
    def __init__(self, name, age):
        self.name = name  # Атрибут name (имя)
        self.age = age  # Атрибут age (возраст)

    def __str__(self):
        return f'Студент: {self.name}, возраст: {self.age}'

    def __repr__(self):
        return f'Student("{self.name}", {self.age})'


if __name__ == '__main__':
    student = Student('Peter', 16)
    print(student)
    print(repr(student))
    print(student.__repr__())
