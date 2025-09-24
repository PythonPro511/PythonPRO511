"""
Тип ошибки 1:  Удаление элемента из списка во время итерации — RuntimeError

Ошибка возникает, когда при выполнении сортировки или поиска попытаться изменить список,
по которому в данный момент выполняется итерация.

Пример ошибки:
"""

# numbers = [10, 20, 30, 40]
# for num in numbers:
#     if num % 20 == 0:
#         numbers.append(40)  # RuntimeError: list changed size during iteration
# print(numbers)

"""
Решение:
Используйте копию списка для итерации
Создайте копию списка и выполняйте изменения в исходном списке.
"""

numbers = [10, 20, 30, 40]
for num in numbers[:]:
    if num % 20 == 0:
        numbers.append(40)
print(numbers)

numbers = [10, 20, 30, 40]
for num in list(numbers):
    if num % 20 == 0:
        numbers.append(40)
print(numbers)

numbers = [10, 20, 30, 40]
for num in numbers.copy():
    if num % 20 == 0:
        numbers.append(40)
print(numbers)
