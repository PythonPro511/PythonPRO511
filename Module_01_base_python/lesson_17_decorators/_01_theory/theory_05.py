from datetime import datetime

def log(func):
    def wrapper(*args, **kwargs):
        print(f'{datetime.now()} - Вызов функции {func.__name__} c аргументами: {args} / {kwargs}\n')
        return func(*args, **kwargs)

    return wrapper


@log
def add(a, b):
    return a + b


@log
def add_no_params():
    return 3 + 4


@log
def add_args_kwargs(*args, **kwargs):
    args_sum = 0
    kwargs_sum = 0
    if args:
        args_sum = sum(args)
    if kwargs:
        kwargs_sum = sum(kwargs.values())

    return args_sum, kwargs_sum


if __name__ == '__main__':
    result1 = add(3, 5)
    print(result1)
    result2 = add_no_params()
    print(result2)
    result3 = add_args_kwargs(1, 2, 3, a=4, b=5, c=6)
    print(result3)
