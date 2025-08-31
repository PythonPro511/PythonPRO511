def greet(name):
    """
    Эта функция принимает строку, которая содержит имя персоны
    и возвращает строку - приветствие.

    :param name (str): имя персоны
    :return str: приветствие
    """
    greeting = f'Hello {name}'
    return greeting


def greet1(name):
    """
    Эта функция принимает строку, которая содержит имя персоны
    и возвращает строку - приветствие.

    Parameters:
        name (str): имя персоны

    Returns:
        str: приветствие
    """
    greeting = f'Hello {name}'
    return greeting


if __name__ == '__main__':
    greet("Петр")
    greet1("Иван")
    print(greet.__doc__)
    print(greet1.__doc__)
