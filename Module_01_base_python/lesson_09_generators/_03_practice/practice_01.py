def multiples(limit, divider):
    for number in range(1, limit + 1):
        if number % divider == 0:
            yield number


if __name__ == '__main__':
    try:
        user_limit = int(input("Введите верхний предел: "))
        user_divider = int(input("Введите делитель: "))
    except ValueError:
        print('Верхний предел/Делитель должны быть целым числом!')
    else:
        print(f'Числа от 1 до {user_limit}, кратные {user_divider}:')
        for multiple in multiples(user_limit, user_divider):
            print(multiple)


# def multiples_with_lc(limit, divisor):
#     return [number for number in range(1, limit + 1) if number % divisor == 0]
#
#
# if __name__ == '__main__':
#     limit = int(input("Введите верхний предел: "))
#     divisor = int(input("Введите делитель: "))
#
#     print(f"Числа от 1 до {limit}, кратные {divisor}:")
#     print(multiples_with_lc(limit, divisor))
