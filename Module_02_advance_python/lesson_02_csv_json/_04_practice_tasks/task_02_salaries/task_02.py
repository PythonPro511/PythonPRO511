"""
Задача: у вас есть JSON-файл с данными о сотрудниках компании, содержащий их имена, отделы и зарплаты. Нужно написать программу, которая:
выводит общую сумму зарплат для каждого отдела;
сохраняет результаты в новый JSON-файл.
"""
import json


def read_json_data(file_path):
    salaries = dict()
    with open(file_path, 'r', encoding='utf-8') as file:
        employees_data = json.load(file)
        for emp in employees_data:
            department = emp['department']
            salary = emp['salary']
            if department in salaries:
                salaries[department] += salary
            else:
                salaries[department] = salary

    return salaries


def write_json_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return True


if __name__ == '__main__':
    salaries_data = read_json_data('employees.json')
    write_json_file('department_salaries.json', salaries_data)
    for department, salary in salaries_data.items():
        print(f'{department}: {salary}')
