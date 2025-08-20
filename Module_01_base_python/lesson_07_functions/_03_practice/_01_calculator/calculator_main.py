from _01_calculator_utils.utils import calculator

while True:
    print(f'\nПростой калькулятор: ')
    try:
        user_num1 = float(input('Введите первое число: '))
        user_num2 = float(input('Введите второе число: '))
        user_operation = input("Введите операцию: '+', '*', '-', '/': ").strip()

        result = calculator(user_num1, user_num2, user_operation)
        print(f'Результат: {result}')
    except ValueError:
        print(f'Ошибка: введите корректные числа!')

    user_input = input('Хотите продолжить? (yes/no): ').strip().lower()
    if user_input not in ["yes", 'y', 'да']:
        break
