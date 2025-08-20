number_of_transactions = 0
amount = 0
total_amount = 0

while True:
    try:
        number_of_transactions = int(input("Введите количество транзакций: "))
        if number_of_transactions >= 0:
            break
        else:
            print("Количество транзакций не может быть отрицательным, попробуйте снова: ")
    except ValueError:
        print('Неверный ввод! Пожалуйста введите число.')

for _ in range(number_of_transactions):
    while True:
        try:
            amount = float(input("Введите сумму транзакции: "))
            if amount >= 0:
                break
            else:
                print("Введите неотрицательное значение суммы")
        except ValueError:
            print('Неверный ввод! Пожалуйста введите числовое значение суммы.')
    description = input("Введите описание транзакции: ")
    print(f"Введена транзакция: Сумма - {amount}\nОписание - '{description}'")
    total_amount += amount

print(f'\nВсе транзакции введены. ИТОГО: {total_amount}')
