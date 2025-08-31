class Calculator:
    """
    Класс для выполнения арифметических операций

    Methods:
        add(a, b): возвращает сумму значений a и b
    """

    @staticmethod
    def add(a, b):
        """
        Суммирует два числа

        Arguments:
            a (int): первое число
            b (int): второе число
        """
        s = a + b
        return s


if __name__ == '__main__':
    print(Calculator.__doc__)
    print(Calculator.add.__doc__)
