"""
Тип ошибки 2: Отсутствие синхронизации

Ошибка возникает в состоянии гонки при одновременном доступе к памяти.

Пример ошибки:
"""

from multiprocessing import Lock
import array

# def worker():
#     array[0] += 1  # Без блокировки


"""
Решение:

используем Lock для синхронизации.
"""


def worker(lock):
    with lock:
        array[0] += 1


if __name__ == '__main__':
    lock = Lock()
