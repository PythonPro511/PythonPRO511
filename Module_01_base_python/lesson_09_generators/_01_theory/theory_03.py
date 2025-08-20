# Создание списка квадратов чисел от 0 до 4
squares = [x ** 2 for x in range(5)]
print(squares)
print()

# Создание словаря, где ключи — это числа, а значения — их квадраты
squares_dict = {x: x ** 2 for x in range(5)}
print(squares_dict)
print()

# Создание множества квадратов чисел
squares_set = {x ** 2 for x in range(5)}
print(squares_set)
print()

# Список только чётных чисел от 0 до 9
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
print()

# Словарь только для нечётных чисел
odd_squares_dict = {x: x ** 2 for x in range(10) if x % 2 != 0}
print(odd_squares_dict)
