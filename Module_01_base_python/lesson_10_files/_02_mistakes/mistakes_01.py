"""
Тип ошибки 1: Файл не найден — FileNotFoundError
Ошибка возникает при попытке открыть несуществующий файл.
Пример ошибки:
"""
# file = open("nonexistent.txt", "r")  # FileNotFoundError

"""
Решение:
Перед открытием файла в режиме чтения проверьте его существование.
Исправленный код:
"""

import os

if os.path.exists("nonexistent.txt"):
    with open("nonexistent.txt", "r") as file:
        print(file.read())
else:
    print("Файл не найден.")