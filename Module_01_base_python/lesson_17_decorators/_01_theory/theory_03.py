def decorator(func):
    def wrapper(name):
        print('До вызова функции')
        func(name)
        print('После вызова функции')
        print()
    return wrapper


@decorator
def greet(name):
    print(f'Привет, {name}!')


if __name__ == '__main__':
    greet('Иван')
    greet('Петр')
