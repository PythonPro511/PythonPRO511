# Тип ошибки 4: Цикл по изменяемому словарю
#
# RuntimeError: dictionary changed size during iteration
#
# Ошибка:
#
# Изменение словаря во время его перебора может привести к ошибке.

# my_dict = {"a": 1, "b": 2, "c": 3}
# for key in my_dict:
#     my_dict.pop(key)  # Ошибка: словарь изменён во время итерации

my_dict = {"a": 1, "b": 2, "c": 3}
for key in list(my_dict.keys()):
    my_dict.pop(key)  # Ошибка: словарь изменён во время итерации
print(my_dict)