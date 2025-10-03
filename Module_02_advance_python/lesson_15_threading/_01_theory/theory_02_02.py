"""race condition (гонка данных) пример 1"""
import threading
from time import sleep

counter = 0


# def increase(by, lock):
#     global counter
#
#     lock.acquire()
#     local_counter = counter
#     local_counter += by
#
#     sleep(0.5)
#
#     counter = local_counter
#     print(f'Значение counter: {counter}')
#     lock.release()

def increase(by, lock):
    global counter

    with lock:
        local_counter = counter
        local_counter += by

        sleep(0.5)

        counter = local_counter


if __name__ == '__main__':
    my_lock = threading.Lock()
    thread1 = threading.Thread(target=increase, args=(10, my_lock))
    thread2 = threading.Thread(target=increase, args=(20, my_lock))
    thread3 = threading.Thread(target=increase, args=(30, my_lock))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print(f'Значение counter в итоге: {counter}')
