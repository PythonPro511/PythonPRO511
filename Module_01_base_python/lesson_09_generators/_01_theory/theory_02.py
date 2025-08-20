# def count_up_to(limit):
#     count = 1
#     while count <= limit:
#         yield count
#         count += 1
#
#
# for number in count_up_to(5):
#     print(number)

import sys

numbers_list = [x ** 2 for x in range(1000)]  # Список квадратов чисел
numbers_gen = (x ** 2 for x in range(1000))  # Генератор квадратов чисел

print(f'Размер списка: {sys.getsizeof(numbers_list), "байт"}')
print(f'Размер генератора: {sys.getsizeof(numbers_gen), "байт"}')
