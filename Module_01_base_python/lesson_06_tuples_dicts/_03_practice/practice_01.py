employees = {}

employees[(1, "Alice")] = {'position': "Manager", "skills": {'leader', 'communication'}}
employees[(2, "Bob")] = {'position': "Developer", "skills": {'python', 'databases'}}
# print(employees)
# {
# (1, 'Alice'): {'position': 'Manager', 'skills': {'leader', 'communication'}},
# (2, 'Bob'): {'position': 'Developer', 'skills': {'databases', 'python'}}
# }

for key, value in employees.items():
    print(f'Сотрудник {key[0]}: {key[1]}')
    print(f'Должность: {value['position']}')
    print(f'Навыки: {', '.join(value['skills'])}')
    print()

for (emp_id, name), info in employees.items():
    print(f'Сотрудник {emp_id}: {name}')
    print(f'Должность: {info['position']}')
    print(f'Навыки: {', '.join(info['skills'])}')
    print()
