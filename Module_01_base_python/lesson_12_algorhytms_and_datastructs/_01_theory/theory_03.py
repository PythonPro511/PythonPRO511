def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return f'Элемент найден на позиции: {mid}'
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "Элемент не найден"


if __name__ == '__main__':
    numbers = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(numbers, 7))
    print(binary_search(numbers, 11))
    print(binary_search(numbers, 3))
    print(binary_search(numbers, 4))
