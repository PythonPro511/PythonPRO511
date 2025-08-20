"""
Тип ошибки 5: Чтение файла, открытого в режиме записи — UnsupportedOperation
Ошибка возникает при попытке прочитать файл, открытый в режиме записи («w»).
Пример ошибки:
"""

# with open("example.txt", "w", encoding='utf-8') as file:
#     print(file.read())  # UnsupportedOperation

"""
Решение:
Перед записью преобразуйте данные в строку с помощью str().
Исправленный код:
"""

with open("example.txt", "r+", encoding='utf-8') as file:
    print(file.read())
    file.write('\nИ тогда (конечно, если бы')
