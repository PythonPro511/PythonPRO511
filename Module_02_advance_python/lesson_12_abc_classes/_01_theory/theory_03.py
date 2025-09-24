from abc import ABC, abstractmethod


class Person(ABC):

    @property
    @abstractmethod
    def name(self):
        pass


class Student(Person):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print('Тип данных неверен, ожидаемый тип данных >> строка')


if __name__ == '__main__':
    student = Student('Иван')
    print(student.name)
    student.name = 'Петр'
    print(student.name)
    student.name = 1
