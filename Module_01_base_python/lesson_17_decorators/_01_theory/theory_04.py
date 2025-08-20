def decorator1(func):
    def wrapper():
        print("Декоратор 1")
        func()

    return wrapper


def decorator2(func):
    def wrapper():
        print("Декоратор 2")
        func()

    return wrapper


@decorator1
@decorator2
def say_hello():
    print('Hello world!')


if __name__ == '__main__':
    say_hello()
