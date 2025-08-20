class Animal:
    def __init__(self, name, paws):
        self.name = name
        self.paws = paws

    def speak(self):
        return f'Я животное: {self.name} я издаю какой-то звук'

    def walk(self):
        return f'Я животное: {self.name} я хожу на {self.paws} лапах'


class Dog(Animal):
    def __init__(self, name, paws, age):
        super().__init__(name, paws)
        self.age = age

    def speak(self):
        animal_sound = super().speak()
        return f'{animal_sound}\nЯ собака: {self.name} я издаю звук: Гав-гав!'


class Cat(Animal):
    def speak(self):
        return f'Я кот: {self.name} я издаю звук: Мяу-мяу!'


if __name__ == '__main__':
    dog = Dog("Шарик", 4, 5)
    print(dog.name)
    print(dog.paws)
    print(dog.age)
    print(dog.speak())
    print(dog.walk())
    print()

    cat = Cat("Мурзик", 3)
    print(cat.name)
    print(cat.paws)
    print(cat.speak())
    print(cat.walk())
    print()
