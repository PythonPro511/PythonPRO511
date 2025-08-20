from functools import reduce


def calculate_total(cart, base_summ):
    item_totals = map(lambda x: x[0] * x[1], cart)
    return reduce(lambda x, y: x + y, item_totals, base_summ)


if __name__ == '__main__':
    my_cart = [
        (10.99, 2),
        (5.49, 4),
        (3.99, 3)
    ]
    print(calculate_total(my_cart, 0))
    print(calculate_total(my_cart, 100))
