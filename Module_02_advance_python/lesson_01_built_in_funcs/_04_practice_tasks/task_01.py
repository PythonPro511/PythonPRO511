"""
Задача: написать программу, которая печатает попарное произведение чисел в заданном списке.
"""

from functools import reduce

nums_list = [1, 5, 7, 3, 8, 6]
temp_result = lambda a, b: a * b
total_result = reduce(temp_result, nums_list)

print(total_result)
