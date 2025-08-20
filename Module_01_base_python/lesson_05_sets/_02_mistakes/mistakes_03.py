# Тип ошибки 3: Изменение множества во время итерации — RuntimeError: Set changed size during iteration
#
# Ошибка может возникнуть, есть изменить множества во время его перебора.

# my_set = {1, 2, 3}
# for item in my_set:
#     my_set.add(4)  # Ошибка: множество изменено


# Решение:
# Создайте копию множества для безопасной итерации.

my_set = {1, 2, 3}
i = 4
for item in my_set.copy():  # Итерация по копии
    my_set.add(i)

print(my_set)

my_set = {1, 2, 3}
for item in set(my_set):  # Итерация по копии
    my_set.add(4)

print(my_set)