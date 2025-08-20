person = {'name': 'Иван', 'age': 30, 'city': 'Москва'}

for key in person:
    print(f'Ключ: {key}')

# for key in person.keys():
#     print(f'Ключ: {key}')
print()

for value in person.values():
    print(f'Значение: {value}')
print()

for key, value in person.items():
    print(f'Ключ: {key}. Значение: {value}')
