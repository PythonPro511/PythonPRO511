"""
Задание 2. Параллельное обновление матрицы

Ситуация: мы продолжаем разрабатывать многопроцессорное приложение,
которое анализирует данные, представленные в виде матрицы.
Каждый из процессов умножает отдельную строку матрицы на 2.

Задача — разработать приложение, создающее матрицу n*m.
Каждый процесс приложения должен обрабатывать строки заданным путём.
Применить синхронизацию так, чтобы строки обрабатывались независимо.

Шаги реализации:

1) Создадим разделяемую память для хранения матрицы.
2) Разделим матрицу на строки, каждая из которых будет обрабатываться отдельным процессом.
3) Используем объект Lock для защиты операций записи в разделяемую память.
4) Реализуем функцию process_row, которая умножает элементы строки на 2.
5) Запустим процессы для обработки всех строк.

"""

from multiprocessing import Process, shared_memory, Lock
import array


def process_row(shm_name, row, cols, lock):
    shm = shared_memory.SharedMemory(name=shm_name)
    matrix = array.array('i', shm.buf)  # 'i' означает целые числа (int)
    start = row * cols  # начало строки
    end = start + cols  # конец строки

    with lock:
        for i in range(start, end):
            matrix[i] *= 2

    shm.close()


if __name__ == '__main__':
    rows_, cols_ = 3, 3
    data = [[i * cols_ + j for j in range(cols_)] for i in range(rows_)]
    # [
    # [0, 1, 2],
    # [3, 4, 5],
    # [6, 7, 8]
    # ]

    flat_data = [item for sublist in data for item in sublist]
    # [0, 1, 2, 3, 4, 5, 6, 7, 8]

    arr = array.array('i', flat_data)
    shm_ = shared_memory.SharedMemory(create=True, size=arr.buffer_info()[1] * arr.itemsize)
    shm_.buf[:] = arr.tobytes()

    lock = Lock()
    processes = [
        Process(target=process_row, args=(shm_.name, i, cols_, lock)) for i in range(rows_)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    result_matrix = array.array('i', shm_.buf)
    result_matrix = [result_matrix[i * cols_:(i + 1) * cols_] for i in range(rows_)]

    print(f'Итоговая матрица: ')
    for row in result_matrix:
        print(row)

    shm_.close()
    shm_.unlink()
