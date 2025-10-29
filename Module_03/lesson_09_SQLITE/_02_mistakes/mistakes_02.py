"""
Тип ошибки 2: Неверное использование метода fetchall()

Использование метода fetchall() для извлечения всех данных сразу может привести к перегрузке памяти,
особенно если в нашей базе хранится много записей.
Это может спровоцировать ошибку недостатка памяти или замедлить работу программы.
"""

import sqlite3

conn = sqlite3.connect(r"databases\example.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM large_table")
rows = cursor.fetchall()  # Много данных


"""
Решение:
Используйте методы fetchone() или fetchmany(n), извлекайте данные по частям:
"""

rows = cursor.fetchmany(1000)  # Читаем данные по 1000 строк

while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(row)
