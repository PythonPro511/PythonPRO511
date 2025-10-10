from multiprocessing import Process, shared_memory
import array


def worker(shm_name, array_type, array_size):
    # Подключаемся к разделяемой памяти
    existing_shm = shared_memory.SharedMemory(name=shm_name)
    # Создаём массив на основе этой памяти
    shared_array = array.array(array_type, existing_shm.buf)
    # Изменяем данные в массиве
    shared_array[0] += 10
    print(f'Обновленный массив в процессе: {shared_array}')
    existing_shm.close()


if __name__ == '__main__':
    # Создаём массив данных
    data = array.array('i', [5, 10, 15])  # 'i' — тип данных для целых чисел
    # Создаём разделяемую память
    shm = shared_memory.SharedMemory(create=True, size=data.buffer_info()[1] * data.itemsize)
    # Копируем данные в разделяемую память
    my_shared_array = array.array('i', shm.buf[:data.buffer_info()[1] * data.itemsize])
    my_shared_array[:] = data[:]
    print(f'Исходный массив: {my_shared_array}')

    # создаем и запускаем процесс
    process = Process(target=worker, args=(shm.name, 'i', len(data)))
    process.start()
    process.join()

    # проверяем обновление
    print(f'Массив после изменений: {my_shared_array}')

    # Закрываем и удаляем разделяемую память.
    shm.close()
    shm.unlink()
