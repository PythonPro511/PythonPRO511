import multiprocessing
from multiprocessing import Value


# shared_value = Value('i', 0)
# print(shared_value.value)
# shared_value.value = 42
# print(shared_value.value)

def increment(shared_value):
    for _ in range(10):
        shared_value.value += 1


if __name__ == '__main__':
    my_shared_value = multiprocessing.Value('i', 0)
    process = multiprocessing.Process(target=increment, args=(my_shared_value,))
    process.start()
    process.join()

    print(f'Итоговое значение: {my_shared_value.value}')
