def count_unique(numbers: list[int]) -> dict[int, int]:
    """
    Возвращает словарь в котором в качестве ключей выступают элементы списка,
    а в качестве значений их количество

    Параметры:
        numbers (list[int]): список целых чисел

    Возвращает:
        counter (dict): словарь в котором ключи это элементы списка, а значения их количество
    """

    counter = dict()
    for item in numbers:
        if item not in counter:
            counter[item] = 0
        counter[item] += 1
    return counter


if __name__ == '__main__':
    print(count_unique([1, 1, 3, 4, 5, 6, 8, 8]))
