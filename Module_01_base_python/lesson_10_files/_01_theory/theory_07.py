def save_contacts_in_file(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as file:
        for name, phone in data.items():
            file.write(f'{name}: {phone}\n')


def read_contacts_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())


if __name__ == '__main__':
    contacts = {"Иван": "123-456", "Мария": "789-012"}
    save_contacts_in_file(filepath=r'files\contacts.txt', data=contacts)
    try:
        read_contacts_from_file(filepath=r'files\contacts_read.txt')
    except FileNotFoundError:
        print(f'Файл не найден, создаю файл с контактами')
        save_contacts_in_file(filepath=r'files\contacts_read.txt', data=contacts)
