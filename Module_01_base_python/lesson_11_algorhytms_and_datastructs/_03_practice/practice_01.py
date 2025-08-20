def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


if __name__ == '__main__':
    grades_input = input('Введите оценки учеников через пробел: ')
    grades_list = [int(grade) for grade in grades_input.split()]
    print(f'Исходные оценки: {grades_list}')
    sorted_grades = insertion_sort(grades_list)
    print(f'Отсортированные оценки: {sorted_grades}')
    # [7, 4, 6, 5, 4, 8, 9, 2, 3] - 4
    # [4, 7, 6, 5, 4, 8, 9, 2, 3] - 7
    # [4, 6, 7, 5, 4, 8, 9, 2, 3] - 6
    # [4, 5, 6, 7, 4, 8, 9, 2, 3] - 5
