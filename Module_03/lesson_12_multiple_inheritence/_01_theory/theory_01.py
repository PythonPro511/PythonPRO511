class BaseModel:
    def __init__(self, m_id):
        self.__m_id = m_id

    @property
    def m_id(self):
        return self.__m_id

    def save(self):
        print(f'Объект с id={self.m_id} сохранен в БД')


class UserModel(BaseModel):
    def __init__(self, m_id, name):
        super().__init__(m_id)
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f'Пользователь: {self.name}, ID: {self.m_id}')


if __name__ == '__main__':
    user = UserModel(1, "Alice")
    user.save()  # Метод из родительского класса
    user.display_info()  # Метод из дочернего класса
