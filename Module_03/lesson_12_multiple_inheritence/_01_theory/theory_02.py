"""
Пример использования наследования в ORM

Представим, что мы разрабатываем ORM для работы с базой данных.
У нас есть несколько таблиц: Users, Products, Orders.
Они имеют общие поля, такие как id и created_at, а также общий метод save().
Мы можем создать базовый класс BaseModel, который будет содержать эту общую логику,
а затем наследовать от него конкретные модели.
"""

from datetime import datetime


class BaseModel:
    def __init__(self, m_id):
        self.m_id = m_id
        self.created_at = datetime.now()

    def save(self):
        print(f'Объект с id={self.m_id} сохранен в БД')


class UserModel(BaseModel):
    def __init__(self, m_id, name):
        super().__init__(m_id)
        self.name = name


class ProductModel(BaseModel):
    def __init__(self, m_id, title, price):
        super().__init__(m_id)
        self.title = title
        self.price = price


if __name__ == '__main__':
    # Использование
    user = UserModel(1, "Alice")
    product = ProductModel(101, "Laptop", 999.99)

    user.save()  # Объект с id=1 сохранён в базу данных.
    product.save()  # Объект с id=101 сохранён в базу данных.
