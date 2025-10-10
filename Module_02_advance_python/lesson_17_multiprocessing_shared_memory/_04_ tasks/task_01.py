"""
Уровень 1. Базовый
Задача: реализовать программу, в которой два процесса увеличивают общий счётчик.
Счётчик реализуется с помощью объекта Value.
Каждый процесс должен увеличивать значение счётчика 10 раз, синхронизируя доступ к переменной.
"""

import multiprocessing


def increment_counter(shared_counter: multiprocessing.Value, lock):
    for _ in range(10):
        with lock:
            shared_counter.value += 1


def main():
    shared_counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    process1 = multiprocessing.Process(target=increment_counter, args=(shared_counter, lock))
    process2 = multiprocessing.Process(target=increment_counter, args=(shared_counter, lock))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print(f'Итоговое значение счетчика: {shared_counter.value}')



if __name__ == '__main__':
    main()
