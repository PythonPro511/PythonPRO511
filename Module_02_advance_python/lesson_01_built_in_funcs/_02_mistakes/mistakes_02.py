"""
Тип ошибки 2: Неверное количество аргументов в функции, переданной в reduce

Получим ошибку, если аргументом в reduce передать функцию, принимающую меньше двух аргументов.
"""
from functools import reduce

# nums_list = [2, 5, 3, 5]
# print(reduce(lambda a: a ** 2), nums_list)

"""
Аналогично и для случая функции, принимающей больше двух аргументов:
"""
nums_list = [2, 5, 3, 5]
multiply = lambda a, b: a * b
print(reduce(multiply, nums_list))
