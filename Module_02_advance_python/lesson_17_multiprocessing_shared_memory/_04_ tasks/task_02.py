"""
Уровень 2. Средний

Задача: реализовать программу, в которой массив чисел (Array) заполняется несколькими процессами.
Каждый процесс добавляет квадрат своего индекса в общий массив.
Использовать синхронизацию для защиты массива от одновременного изменения.
"""

import multiprocessing


def fill_array(shared_array, index, lock):
    with lock:
        shared_array[index] = index ** 2
        print(f'Процесс {index}: записано {index ** 2}')


def main():
    size = 5
    shared_array = multiprocessing.Array('i', size)  # разделяемый массив
    lock = multiprocessing.Lock()

    processes = []
    for i in range(size):
        process = multiprocessing.Process(target=fill_array, args=(shared_array, i, lock))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Итоговый массив: {list(shared_array)}')


if __name__ == '__main__':
    main()
