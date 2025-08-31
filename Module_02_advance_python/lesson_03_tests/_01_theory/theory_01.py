def divide(a, b):
    assert b != 0, 'zero division'
    return a / b


if __name__ == '__main__':
    print(divide(5, 2))
    print(divide(5, 0))
