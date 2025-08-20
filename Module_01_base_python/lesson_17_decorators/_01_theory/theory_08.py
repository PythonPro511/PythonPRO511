class MyClass:
    count = 0

    @classmethod
    def increment_count(cls):
        # MyClass.count += 1 # при использовании classmethod, мы вместо имени класса подставляем cls (см.ниже)
        cls.count += 1
        print(f'Счетчик теперь: {cls.count}')


if __name__ == '__main__':
    MyClass.increment_count()
    MyClass.increment_count()

