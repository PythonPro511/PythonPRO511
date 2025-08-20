"""
Задача: вам предоставлены данные о нескольких товарах в онлайн-магазине.
Из этих данных для товаров, чья стоимость меньше 110, нужно применить скидку 20%.
В качестве ответа вывести отредактированный список стоимостей, отсортированный по возрастанию.
"""

goods = [140, 130, 190, 140, 120, 50, 100, 140, 10, 100, 110]
goods_lower = list(filter(lambda x: x < 110, goods))
goods_upper = list(filter(lambda x: x >= 110, goods))

discounted_goods = list(map(lambda x: x * (1 - 20 / 100), goods_lower))

sorted_goods = sorted(discounted_goods + goods_upper)
print(sorted_goods)
