def iterate_orders(orders: iter):
    while True:
        try:
            order = next(orders)
            print(f'Обрабатывается заказ: {order}')
        except StopIteration:
            print(f'Все заказы обработаны.')
            break


def get_orders_data(filepath):
    orders_list = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            orders_list.append(line.rstrip())
    return orders_list


def display_orders(filepath, orders_num=0):
    with open(filepath, 'r', encoding='utf-8') as file:
        iterator = iter(file)
        print(f"Первые {orders_num} заказов: ")
        for _ in range(orders_num):
            try:
                print(next(iterator).strip())
            except StopIteration:
                print("Файл закончился.")
                break


if __name__ == '__main__':
    # Список заказов
    my_orders = ["Кофе", "Чай", "Пирожное", "Сэндвич"]
    my_orders_iterator = iter(my_orders)
    iterate_orders(my_orders_iterator)
    print()

    my_file_orders = get_orders_data('orders.txt')
    my_file_iterator = iter(my_file_orders)
    iterate_orders(my_file_iterator)
    print()

    display_orders('orders.txt', 5)
