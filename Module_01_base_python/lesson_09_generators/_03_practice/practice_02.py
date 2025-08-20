def even_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number


if __name__ == '__main__':
    try:
        user_start = int(input("Введите начало диапазона: "))
        user_end = int(input("Введите конец диапазона: "))
    except ValueError:
        print('Границы диапазона должны быть целым числом!')
    else:
        print(f'Четные числа в диапазоне от {user_start} до {user_end} (включительно):')
        for even in even_numbers(user_start, user_end):
            print(even)

# # Генератор списка
# def even_numbers_with_lc(start, end):
#     return [number for number in range(start, end + 1) if number % 2 == 0]
#
#
# # Основная программа
# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
#
# print(f"Чётные числа от {start} до {end}:")
# print(even_numbers_with_lc(start, end))
