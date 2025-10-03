"""race condition (гонка данных) пример 1"""
import threading
from time import sleep

counter = 0


def increase(by):
    global counter

    local_counter = counter
    local_counter += by

    sleep(0.5)

    counter = local_counter
    print(f'Значение counter: {counter}')


if __name__ == '__main__':
    thread1 = threading.Thread(target=increase, args=(10,))
    thread2 = threading.Thread(target=increase, args=(20,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'Значение counter в итоге: {counter}')
