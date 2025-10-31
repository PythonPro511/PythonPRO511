"""
Задача 1:
Улучшение класса ORM: замена атрибутов на приватные и добавление геттеров
Ситуация:
Ваши коллеги разработали модель ORM, однако не добавили инкапсуляцию, что делает текущую версию программы уязвимой.
Вы получили код:

class User:
    def __init__(self, id, name, email):
        self.id = id  # Публичный атрибут
        self.name = name  # Публичный атрибут
        self.email = email  # Публичный атрибут

    def save(self):
        # Логика сохранения в базу данных
        print(f"Сохранение пользователя: {self.name}, email: {self.email}")


# Использование
user = User(1, "Иван Иванов", "ivan@example.com")
user.name = ""  # Некорректное значение
user.email = "invalid-email"  # Некорректный email
user.save()  # Сохранение некорректных данных

Задача:
Доработайте класс модели в ORM, чтобы все атрибуты были приватными (_ или __).
Добавьте геттеры для получения доступа к данным.
Используйте свойства (@property).
"""


class User:
    def __init__(self, u_id, name, email):
        self.__u_id = u_id  # Приватный атрибут
        self.__name = name  # Приватный атрибут
        self.__email = email  # Приватный атрибут

    @property
    def u_id(self):
        return self.__u_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 3:
            raise ValueError("Имя не может быть короче 3х букв")
        if not new_name.replace(" ", "").isalpha():
            raise ValueError("Введены недопустимые символы")
        User.report_changes(self.__name, new_name)
        self.__name = new_name

    # task 2 setters
    @email.setter
    def email(self, new_email):
        if '@' not in new_email:
            raise ValueError('Некорректный email')
        User.report_changes(self.__email, new_email)
        self.__email = new_email

    def save(self):
        # Логика сохранения в базу данных
        print(f"Сохранение пользователя: {self.name}, email: {self.email}")

    @staticmethod
    def report_changes(old_value, new_value):
        print(f'Данные изменены: {old_value} >> {new_value}')


if __name__ == '__main__':
    # Использование
    user = User(1, "Иван Иванов", "ivan@example.com")
    user.name = "Петр Петров"  # Корректное значение
    user.email = "petr@example.com"  # Корректный email
    # user.name = ""  # Ошибка: Имя не может быть пустым
    # user.email = "invalid-email"  # Ошибка: Некорректный email
    user.save()  # Сохранение корректных данных
