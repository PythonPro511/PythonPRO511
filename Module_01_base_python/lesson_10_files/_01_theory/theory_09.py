import os

path_ok = r'files\contacts.txt'
path_not_ok = r'files\contacts12345.txt'

print(os.path.exists(path_ok))

if os.path.exists(path_ok):
    print('Файл найден!')
else:
    print('Файл не найден!')

if os.path.exists(path_not_ok):
    print('Файл найден!')
else:
    print('Файл не найден!')