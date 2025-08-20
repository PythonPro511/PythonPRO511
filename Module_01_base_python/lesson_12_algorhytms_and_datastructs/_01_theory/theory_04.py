def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    sorted_list = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_list.append(left_half[i])
            i += 1
        else:
            sorted_list.append(right_half[j])
            j += 1
    sorted_list.extend(left_half[i:])
    sorted_list.extend(right_half[j:])

    return sorted_list


if __name__ == '__main__':
    numbers = [38, 27, 43, 3, 9, 82, 10]
    sorted_numbers = merge_sort(numbers)
    print(f"Отсортированный список: {sorted_numbers}")
    """
    Пошаговый разбор:
    У нас есть список: [38, 27, 43, 3, 9, 82, 10].
    Разделяем его: [38, 27, 43] и [3, 9, 82, 10].
    Ещё раз делим: [38], [27, 43] и [3, 9], [82, 10].
    Сортируем маленькие части:
    [27, 43] → [27, 43]
    
    [3, 9] → [3, 9]
    
    Сливаем обратно:
    [27, 43] + [38] → [27, 38, 43]
    
    [3, 9] + [10, 82] → [3, 9, 10, 82]
    
    Объединяем всё вместе:
    [27, 38, 43] + [3, 9, 10, 82] → [3, 9, 10, 27, 38, 43, 82].
    """