from math import sqrt
"""
Тип ошибки 4: Переопределение импортированной функции — TypeError: ‘str’ object is not callable

Пример ошибки:
"""
# sqrt = "Не функция"
# print(sqrt(16))

"""
Решение:

Не используйте имена встроенных или импортированных функций для переменных.
"""
my_sqrt = "Не функция"
print(sqrt(16))
print(my_sqrt)