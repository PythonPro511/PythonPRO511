class DBConnection:

    # def __init__(self, user, password, driver, db_name):
    #     self.user = user
    #     self.password = password
    #     self.driver = driver
    #     self.db_name = db_name

    def __enter__(self):
        print(f'Открываем соединение с базой данных')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Закрываем соединение с базой данных")
        if exc_type:
            print(f"Произошла ошибка {exc_type.__name__}: {exc_val}")
            return False
        return True


if __name__ == '__main__':
    with DBConnection():
        print(f'Работаем с БД')
        raise Exception('что-то пошло не так')
