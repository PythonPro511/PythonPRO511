from multiprocessing import Array, Process


# shared_array = Array('i', 5)  # Массив целых чисел длиной 5
# Первый аргумент — тип элементов массива (аналогично Value).
# Второй аргумент — итерируемый объект (список) или размер массива.

def square_elements(shared_array):
    for i in range(len(shared_array)):
        shared_array[i] = shared_array[i] ** 2


if __name__ == '__main__':
    my_shared_array = Array('i', [1, 2, 3, 4])
    process = Process(target=square_elements, args=(my_shared_array,))
    process.start()
    process.join()
    print(f'Итоговый массив: {list(my_shared_array)}')
