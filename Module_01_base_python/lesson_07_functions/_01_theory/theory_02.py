# Функция с параметром
def greet_person(name):
    print(f'Привет, {name}')


# Позиционные и именованные аргументы
def introduce_person(name, age):
    print(f'Меня зовут {name}, мне {age} лет')


# Необязательные аргументы
def greet_user(name='гость'):
    print(f'Привет, {name}')


def proceed_data(data=None):
    if data:
        if type(data) is list:
            print('Это список')
        elif type(data) is dict:
            print('Это словарь')
    else:
        print('Нет данных')


if __name__ == '__main__':
    # # Функция с параметром
    # user_name = input("Введите ваше имя: ").strip().capitalize()
    # greet_person(user_name)

    # Позиционные и именованные аргументы
    # user_name = input("Введите ваше имя: ").strip().capitalize()
    # user_age = int(input("Введите ваш полный возраст: "))
    # introduce_person(name=user_name, age=user_age)
    # introduce_person(age=user_age, name=user_name)

    # Необязательные аргументы
    greet_user()
    greet_user('Дмитрий')
    print()

    proceed_data()
    proceed_data(['item1'])
    proceed_data({'k': 'v'})

