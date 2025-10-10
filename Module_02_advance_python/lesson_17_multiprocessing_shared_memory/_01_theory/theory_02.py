from multiprocessing import Process, Queue, shared_memory
import array
import time


# Функция для вычисления квадрата числа и записи результата в разделяемую память
def compute_square(shm_name, index, queue):
    # Подключаемся к разделяемой памяти
    shm = shared_memory.SharedMemory(name=shm_name)
    # Создаём массив на основе разделяемой памяти
    shared_array = array.array('i', shm.buf)

    # вычисляем квадрат числа по индексу
    num = shared_array[index]
    result = num ** 2
    shared_array[index] = result

    # отправляем результат в очередь для дополнительной проверки
    queue.put((index, result))

    # Закрываем доступ к разделяемой памяти
    shm.close()

    # имитация задержки
    shm.close()


if __name__ == '__main__':
    # Исходные данные: список целых чисел
    data = array.array('i', [1, 2, 3])  # Массив целых чисел

    # создаем разделяемую память
    shm = shared_memory.SharedMemory(create=True, size=data.buffer_info()[1] * data.itemsize)

    # копируем данные в разделяемую память
    shared_array = array.array('i', shm.buf)
    shared_array[:] = data[:]

    # создаем очередь для обмена результатами
    queue = Queue()

    # создаем и запускаем процессы
    processes = []
    for i in range(len(data)):
        process = Process(target=compute_square, args=(shm.name, i, queue))
        processes.append(process)
        process.start()

    # ожидаем завершения всех процессов
    for process in processes:
        process.join()

    # Чтение результатов из очереди
    print(f'\nРезультаты полученные из очереди')
    while not queue.empty():
        index, result = queue.get()
        print(f'Индекс {index}, квадрат = {result}')

    # чтение итогового массива из разделяемой памяти
    print(f'\nитоговый массив в разделяемой памяти:')
    shared_array = array.array('i', shm.buf)  # Обновляем ссылку на массив
    print(shared_array.tolist())

    # Освобождаем ресурсы разделяемой памяти
    shm.close()
    shm.unlink()

    print("Все процессы завершены.")
