from datetime import datetime
from functools import wraps


def log_action(func):
    @wraps(func)
    def wrapper(username, *args, **kwargs):
        with open("action.log", 'a', encoding='utf-8') as log_file:
            log_file.write(f'{datetime.now()} - Пользователь: {username}, действие: {func.__name__}\n')
        return func(username, *args, **kwargs)

    return wrapper


@log_action
def login(username):
    print(f'{username} вошел в систему.')


@log_action
def update_profile(username, profile_data):
    print(f'{username} обновил профиль с данными: {profile_data}.')


if __name__ == '__main__':
    login("Alice")
    update_profile("Alice", {"age": 25, "city": "Moscow"})
    login("Peter")
    update_profile("Peter", {"age": 33, "city": "Minsk"})
