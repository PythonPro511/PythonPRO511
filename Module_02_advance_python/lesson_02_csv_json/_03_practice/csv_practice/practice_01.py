import csv
import json


def analyse_sales(file_path):
    sales_list = []
    total_revenue = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # print(row)
            quantity = int(row['quantity'])
            price = int(row['price'])
            total_revenue += quantity * price
            sales_list.append(row)
    return total_revenue, sales_list


def make_json_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    result, info = analyse_sales('files/sales.csv')
    print(result)
    print(info)
    make_json_file('files/sales.json', info)
