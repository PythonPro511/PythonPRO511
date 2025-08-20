from functools import wraps

def authorize(func):
    @wraps(func)
    def wrapper(user):
        if user == 'admin':
            return func()
        else:
            print('Доступ запрещен')
            return False

    return wrapper


@authorize  # в вызов функции надо передать уровень доступа пользователя
def secret():
    print('Секретная информация')


secret('admin')
secret('user')
print(secret.__name__)
