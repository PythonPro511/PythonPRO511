from collections import defaultdict


def group_products_by_category(items: list[tuple[str, str]]) -> defaultdict[str, list]:
    # Создаём defaultdict с типом list для автоматической инициализации
    grouped = defaultdict(list)

    for category, product in items:
        grouped[category].append(product)

    return grouped


if __name__ == '__main__':
    prod_items = [
        ("Фрукты", "Яблоко"),
        ("Овощи", "Морковь"),
        ("Фрукты", "Банан"),
        ("Молочные продукты", "Молоко"),
        ("Овощи", "Картофель")
    ]
    result = group_products_by_category(prod_items)
    print(result)

