class RestaurantOrder:
    total_order = 0
    tables = {}

    def __init__(self, table_number, order_details):
        self.table_number = table_number
        self.order_details = order_details
        RestaurantOrder.total_order += 1
        RestaurantOrder.tables.setdefault(table_number, []).append(order_details)

    @staticmethod
    def is_table_available(table_number):
        return len(RestaurantOrder.tables.get(table_number, [])) == 0

    @classmethod
    def get_total_orders(cls):
        return f'Всего заказов: {cls.total_order}'

    def add_order(self, order_details):
        RestaurantOrder.tables.setdefault(self.table_number, []).append(order_details)
        RestaurantOrder.total_order += 1
