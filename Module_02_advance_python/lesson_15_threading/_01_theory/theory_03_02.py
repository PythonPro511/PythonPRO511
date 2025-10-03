import threading

# Общая переменная, которую будем изменять
counter = 0

# Создаём Lock для синхронизации
lock = threading.Lock()

def increment():
    global counter
    for i in range(100000):
        with lock:
            counter += 1


if __name__ == '__main__':
    threads = []
    for _ in range(5):
        threads.append(threading.Thread(target=increment))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Counter value: {counter}')

    # Counter value: 432157
