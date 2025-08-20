from utils.file_utils import check_file, add_participants, show_participants

if __name__ == '__main__':
    filename = "participants.txt"
    check_file(filename)

    while True:
        command = input('Введите команду:\n1 - add\n2 - show\n0 - exit:\nВаш выбор: ')
        if command == '1':
            name = input('Введите имя участника: ').strip()
            add_participants(filename, name)
            print('Участник добавлен!')
        elif command == '2':
            show_participants(filename)
        elif command == '0':
            print(f'Программа завершает работу.')
            break
        else:
            print('Неизвестная команда попробуйте снова.')
