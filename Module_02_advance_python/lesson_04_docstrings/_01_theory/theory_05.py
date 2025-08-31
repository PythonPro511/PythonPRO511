def process_number(value: int) -> int:
    if not isinstance(value, int):
        raise TypeError(f'Ожидаемое значение типа int, получено {type(value).__name__}')
    return value ** 2


if __name__ == '__main__':
    print(process_number(5))
    print(process_number("5"))
