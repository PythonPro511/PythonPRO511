"""
Задание 1. Синхронизированный счётчик

Ситуация: мы разрабатываем многопроцессорное приложение, в котором каждый из процессоров обращается к общему счётчику.

Задача — реализовать приложение, использующее счётчик с применением shared_memory и Lock.
Каждый процесс должен увеличить счётчик 5 раз.

Шаги реализации:

1) Создадим разделяемую память (shared_memory) для хранения значения счётчика.
2) Используем объект Lock для синхронизации доступа к счётчику.
3) Реализуем функцию worker, которая будет увеличивать значение счётчика в цикле.
4) Запустим несколько процессов, каждый из которых выполняет функцию worker.
"""

from multiprocessing import Process, shared_memory, Lock
import array


def worker(shm_name, lock):
    shm = shared_memory.SharedMemory(name=shm_name)
    counter = array.array('q', shm.buf)  # 'q' означает целые числа (int64)
    for _ in range(5):
        with lock:
            counter[0] += 1  # Увеличиваем счётчик

    shm.close()


if __name__ == '__main__':
    shm_ = shared_memory.SharedMemory(create=True,
                                      size=array.array('q', [0]).itemsize)  # Создаём разделяемую память для int64
    counter_ = array.array('q', shm_.buf)
    counter_[0] = 0

    lock_ = Lock()
    processes = [Process(target=worker, args=(shm_.name, lock_)) for _ in range(3)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    final_value = array.array('q', shm_.buf)[0]
    print(f'Итоговое значение: {final_value}')

    shm_.close()
    shm_.unlink()
