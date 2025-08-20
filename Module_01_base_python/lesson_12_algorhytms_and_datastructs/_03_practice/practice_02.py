stack = []

while True:
    command = input("Введите команду: 1 - add, 2 - complete, 3 - show, 4 - exit: ").strip()
    if command == "1":
        task = input('Введите задачу: ')
        stack.append(task)
        print(f'Задача "{task}" добавлена.')

    elif command == '2':
        if stack:
            completed = stack.pop()
            print(f'Задача "{completed}" завершена.')
        else:
            print(f'Стэк пуст. Все задачи выполнены.')

    elif command == '3':
        if stack:
            reversed_stack = stack[:]
            reversed_stack.reverse()
            print(f'Текущие задачи в порядке выполнения: {', '.join(reversed_stack)}')
        else:
            print(f'Стэк пуст. Нет активных задач.')

    elif command == '4':
        print('Работа завершена.')
        break
    else:
        print(f'Ошибка ввода.')