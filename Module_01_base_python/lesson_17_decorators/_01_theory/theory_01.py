def apply_function(func, value):
    return func(value)


def square(x):
    return x * x


result = apply_function(square, 5)
print(result)
