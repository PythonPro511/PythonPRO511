def combine_employee_data(names, positions, salaries):
    combined = zip(names, positions, salaries)
    return list(map(lambda x: f"{x[0]} - {x[1]}: {x[2]}", combined))


if __name__ == '__main__':
    emp_names = ['Hannah', 'Boris', 'Victoria']
    emp_positions = ['Manager', 'Developer', 'QA-Engineer']
    emp_salaries = [80000, 120000, 90000]
    print(combine_employee_data(emp_names, emp_positions, emp_salaries))
