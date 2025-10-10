

import multiprocessing
import time


def say_hello():
    time.sleep(1)
    print("Hello")


def say_world():
    time.sleep(1)
    print("World")


def print_messages_in_parallel():
    process1 = multiprocessing.Process(target=say_hello)
    process2 = multiprocessing.Process(target=say_world)

    process1.start()
    process2.start()

    process1.join()
    process2.join()


if __name__ == '__main__':
    print_messages_in_parallel()