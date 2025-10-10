import multiprocessing


def say_hello():
    print("Привет от процесса.")


if __name__ == '__main__':
    # Создаём процесс
    process = multiprocessing.Process(target=say_hello)
    process.start()  # Запускаем процесс
    process.join()  # Ожидаем завершения процесса
