"""
Тип ошибки 2: Бесконечный цикл в сортировке

Ошибка происходит, когда в алгоритме пузырьковой сортировки забыть уменьшать количество итераций,
что приведёт к бесконечному циклу.
"""

# def bubble_sort(lst):
#     n = len(lst)
#     while True:  # Ошибка: Условие выхода из цикла отсутствует
#         for i in range(n - 1):
#             if lst[i] > lst[i + 1]:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#     return lst
#
#
# numbers = [64, 34, 25, 12, 22, 11, 90]
# print(bubble_sort(numbers))

"""
Решение:

Добавьте правильное условие выхода из цикла.
"""

def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


numbers = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numbers))
