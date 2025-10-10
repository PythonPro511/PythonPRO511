"""
Тип ошибки 3: Некорректный размер памяти
Ошибка возникает при недостаточном объёме памяти.
Пример ошибки:
"""

from multiprocessing import shared_memory
import array
import sys

shm = shared_memory.SharedMemory(create=True, size=10)  # Нужно 20 байт

"""
Решение:

рассчитываем размер через nbytes.
"""

if __name__ == '__main__':
    data = array.array('i', [1, 2, 3])  # Массив целых чисел
    size = sys.getsizeof(data)  # размер объекта в байтах
    print(size)
