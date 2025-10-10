"""
Уровень 3. Продвинутый

Задача: реализовать программу,
в которой несколько процессов обрабатывают массив данных (Array) и подсчитывают сумму его элементов.
Каждый процесс обрабатывает свою часть массива. Общий результат сохраняется в объект Value с синхронизацией доступа.
"""

import multiprocessing


def compute_partial_sum(shared_array, start, end, shared_sum, lock):
    local_sum = sum(shared_array[start:end])  # Подсчёт суммы части массива
    print(f'Частичная сумма ({start}-{end}): {local_sum}')  # используются индексы значений
    # print(f'Частичная сумма ({start + 1}-{end}): {local_sum}')  # используются сами значения
    with lock:
        shared_sum.value += local_sum


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8]  # Исходный массив
    shared_array = multiprocessing.Array('i', data)  # Разделяемый массив
    shared_sum = multiprocessing.Value('i', 0)  # Разделяемая сумма
    lock = multiprocessing.Lock()

    num_processes = 4
    chunk_size = len(data) // num_processes
    processes = []

    for i in range(num_processes):
        start = i * chunk_size
        # end = start + chunk_size if i != num_processes - 1 else len(data)
        if i != num_processes - 1:
            end = start + chunk_size
        else:
            end = len(data)

        process = multiprocessing.Process(target=compute_partial_sum, args=(shared_array, start, end, shared_sum, lock))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Общая сумма элементов массива: {shared_sum.value}')


if __name__ == '__main__':
    main()
