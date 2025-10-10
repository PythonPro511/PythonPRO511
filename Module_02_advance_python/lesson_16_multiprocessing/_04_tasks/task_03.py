"""
Задача: реализовать многопроцессорную функцию monitor_file_uploads(),
которая запускает загрузку нескольких файлов с разными задержками.
Функция должна каждые 2 секунды выводить список файлов,
которые уже загружены, пока не завершится загрузка всех файлов.

"""

import multiprocessing
import time


def upload_file(file_name, delay, queue):
    print(f'Начата загрузка файла {file_name} это займет {delay} секунд...')
    time.sleep(delay)
    queue.put(file_name)
    print(f'Файл {file_name} успешно загружен.')


def monitor_file_uploads(files):
    processes = []
    results = multiprocessing.Queue()
    downloaded = []  # хранилище для скачанных файлов

    for file, delay in files:
        process = multiprocessing.Process(target=upload_file, args=(file, delay, results))
        processes.append(process)
        process.start()

    while any(process.is_alive() for process in processes):
        downloaded_file = [results.get() for _ in range(results.qsize())]
        if downloaded_file:  # если в процессе проверки что-то скачалось
            downloaded.extend(downloaded_file)  # добавляем это что-то в хранилище
        print(f'Загружено файлов: {len(downloaded)} ({', '.join(downloaded)})')
        time.sleep(2)

    # костыль чтобы не потерять последний скачанный файл
    downloaded_file = [results.get() for _ in range(results.qsize())]
    downloaded.extend(downloaded_file)
    print(f'Все файлы успешно загружены: {', '.join(downloaded)}')


if __name__ == '__main__':
    files = [
        ("file1.txt", 6),
        ("file2.txt", 4),
        ("file3.txt", 8)
    ]

    monitor_file_uploads(files)
