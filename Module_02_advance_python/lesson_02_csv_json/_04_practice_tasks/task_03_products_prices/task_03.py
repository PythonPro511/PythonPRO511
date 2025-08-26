"""
Задача: дано два файла.
В первом products.csv содержатся данные о количестве продуктов,
во втором файле prices.json — стоимости этих продуктов.
Нужно создать новый JSON-файл, в котором будут указаны продукты, их количество и общая стоимость.
"""
import csv
import json


def get_data_products(file_path):
    products = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = list(csv.reader(file, delimiter=','))
        for row in reader[1:]:
            print(row)
            product, quantity = row[0], int(row[1])
            if product in products:
                products[product]['quantity'] += quantity
            else:
                products[product] = {'quantity': quantity}
    return products


def get_prices_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        prices = json.load(file)
    return prices


def make_total_data(file_path, products, prices):
    for product, total_cost in prices.items():
        products[product]['total_cost'] = total_cost
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(products, file, ensure_ascii=False, indent=4)
    return True


if __name__ == '__main__':
    my_products = get_data_products('products.csv')
    my_prices = get_prices_json_data('prices.json')
    make_total_data('total_data.json', my_products, my_prices)
