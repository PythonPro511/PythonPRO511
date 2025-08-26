"""
Задача: прочитать CSV-файл с данными о студентах и вывести средний балл по каждому предмету.
"""
import csv


def display_average_marks(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        results_matrix = list(csv.reader(file))
        disciplines = results_matrix[0]
        results = results_matrix[1:]
        sum_math = 0
        sum_physics = 0
        sum_chemistry = 0
        for result in results:
            sum_math += int(result[1])
            sum_physics += int(result[2])
            sum_chemistry += int(result[3])
        avg_math = sum_math / 3
        avg_physics = sum_physics / 3
        avg_chemistry = sum_physics / 3
        print(f'{disciplines[1]} - {avg_math}')
        print(f'{disciplines[2]} - {avg_physics}')
        print(f'{disciplines[3]} - {avg_chemistry}')


if __name__ == '__main__':
    display_average_marks('students.csv')
