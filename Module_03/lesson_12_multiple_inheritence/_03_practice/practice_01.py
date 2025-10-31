"""
Ситуация:
Ваша команда разрабатывает ORM для управления пользователями и администраторами в системе.
У вас уже есть базовый класс User, который описывает обычного пользователя.
Теперь необходимо создать класс Admin, который будет наследовать от User и добавлять дополнительные атрибуты и методы,
характерные для администратора.

Вы получили следующий код:

class User:
    def __init__(self, id, name, email):
        self._id = id       # Приватный атрибут
        self._name = name   # Приватный атрибут
        self._email = email # Приватный атрибут

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    def save(self):
        # Логика сохранения в базу данных
        print(f"Сохранение пользователя: {self.name}, email: {self.email}")


Задача:
Создайте класс Admin, который будет наследовать от класса User.
"""


class User:
    __users = []

    def __init__(self, u_id, name, email):
        self._u_id = u_id  # Приватный атрибут
        self._name = name  # Приватный атрибут
        self._email = email  # Приватный атрибут
        User.add_user({
            'u_id': self._u_id,
            'name': self._name,
            'email': self._email
        })

    @classmethod
    def get_users(cls):
        return cls.__users

    @classmethod
    def add_user(cls, user_data):
        cls.__users.append(user_data)

    @classmethod
    def display_users(cls):
        for user in cls.__users:
            print(user)

    @property
    def id(self):
        return self._u_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    def save(self):
        # Логика сохранения в базу данных
        print(f"Сохранение пользователя: {self.name}, email: {self.email}")


class Admin(User):
    def __init__(self, u_id, name, email, role):
        super().__init__(u_id, name, email)
        self._role = role

    # Task 2 Задача 2: Улучшение класса ORM: добавление сеттеров

    #
    # Ситуация:
    # Вам необходимо добавить геттеры и сеттеры, которые созданный вами класс наследует от родительского класса.
    #
    # Задача:
    # Добавьте к классу User следующие методы:
    #
    # Геттер для атрибута _role.
    #
    # Метод delete_user(user_id), который будет имитировать удаление пользователя с указанным user_id.
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, new_role):
        if self.role not in ['admin', 'superuser']:
            raise ValueError("У вас нет прав для изменения роли")
        self._role = new_role

    def delete_user(self, u_id):
        if self.role in ['admin', 'superuser']:
            for user in User.get_users():
                if user['u_id'] == u_id:
                    print(f'Пользователь {user} удален.')
                    User.get_users().remove(user)
                    break
            else:
                print("Пользователь с таким id не найден")
        else:
            print(f'Нет доступа к данной функции')


if __name__ == '__main__':
    user_01 = User(1, 'User', 'user@mail.ru')
    admin = Admin(2, 'Admin', 'admin@mail.ru', 'admin')
    User.display_users()
    print()
    admin.delete_user(1)
    User.display_users()
