from functools import wraps


def authorize_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get('role') == 'admin':
            print(f'Пользователь: {user['name']} получил доступ:')
            return func(user, *args, **kwargs)
        else:
            print(f'Доступ запрещен для пользователя {user['name']}.')
            return False

    return wrapper


@authorize_admin
def view_secret_data(user):
    print(f'Секретные данные доступны для {user['name']}')


if __name__ == '__main__':
    admin_user = {'name': 'Alice', 'role': 'admin'}
    regular_user = {'name': 'Bob', 'role': 'user'}
    view_secret_data(admin_user)
    print()

    view_secret_data(regular_user)
