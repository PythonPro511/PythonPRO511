user_name = input("Введите ваше имя: ")
balance_input = input("Введите ваш начальный баланс: ")

balance = float(balance_input)
if balance < 0:
    print("Начальный баланс не может быть отрицательным!")
else:
    print(f'Добро пожаловать, {user_name}! Ваш начальный баланс: {balance} руб.')