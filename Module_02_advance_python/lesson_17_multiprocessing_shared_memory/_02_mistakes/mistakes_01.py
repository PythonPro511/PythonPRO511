"""
Тип ошибки 1: Утечка разделяемой памяти
Ошибка возникает в случае, если разделяемая память была не закрыта и не удалена.
Пример ошибки:
"""
from multiprocessing import shared_memory

shm = shared_memory.SharedMemory(create=True, size=100)
# ...
# Забыли вызвать shm.close() и shm.unlink()

"""
Решение:
вызываем close() и unlink().
"""
shm.close()
shm.unlink()
