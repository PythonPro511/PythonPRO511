from ClassesEmployee.ClassesEmployee import Employee, Manager, TopManager, Intern

if __name__ == '__main__':
    employees = [
        Employee("Иван", "Иванов", 50000),
        Manager("Мария", "Петрова", 80000, 20000),
        TopManager("Александ", "Дмитриев", 80000, 20000, 1.3),
        Intern("Алексей", "Смирнов", 30000, 0.5)
    ]

    for emp in employees:
        print(f'{emp.get_info()} - Зарплата: {emp.get_salary():.2f}')
