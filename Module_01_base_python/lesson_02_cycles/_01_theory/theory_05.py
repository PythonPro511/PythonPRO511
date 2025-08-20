# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# except Exception as Ex:
#     print(type(Ex).__name__)
#     print('На ноль делить нельзя!')


# try:
#     number = int(input("Введите целое число: "))
# except ValueError:
#     print('Вы ввели не целое число!')
# except Exception as Ex:
#     print(type(Ex).__name__)
# else:
#     print(f'Ваше число: {number}')


file = None

filename = input('Введите имя файла: ')
try:
    file = open(filename)
except FileNotFoundError:
    print(f"Файл: {filename} не найден")
else:
    data = file.read()
    print(data)
finally:
    if file is not None:
        file.close()
    print('Программа завершена!')
