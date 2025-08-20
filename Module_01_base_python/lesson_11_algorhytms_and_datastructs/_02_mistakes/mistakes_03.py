"""
Тип ошибки 3: Линейный поиск без обработки отсутствия элемента

Ошибка возникает, если линейный поиск не найдёт элемент,
а код не обработает этот случай, программа может работать некорректно.
"""
numbers = [10, 20, 30]
target = 40
for num in numbers:
    if num == target:
        print("Элемент найден")

"""
Решение:

Добавьте флаг или возвращаемое значение для обработки случая, когда элемент не найден.
"""


def linear_search(lst, target):
    for num in lst:
        if num == target:
            return "Элемент найден"
    return "Элемент не найден"


numbers = [10, 20, 30]
print(linear_search(numbers, 40))  # Элемент не найден

numbers = [10, 20, 30]
target = 40
for num in numbers:
    if num == target:
        print("Элемент найден")
        break
else:
    print("Элемент не найден")
