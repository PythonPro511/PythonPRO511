person1 = {'name': 'Иван', 'age': 30}
# .get(key) — возвращает значение для указанного ключа,
# если ключ существует в словаре.
# Если ключа нет, возвращает None, или заданное значение:
age = person1.get('age', 'возраст не указан')
print(age)
city = person1.get('city', 'город не указан')
print(city)
print(person1)

# .setdefault(key) — возвращает значение для указанного ключа,
# если ключ существует в словаре.
# Если ключа нет, создается пара ключ-значение (если значение передано),
# если нет, то значением будет None:
city = person1.setdefault('city', 'Москва')
print(person1)
print()

# .keys() — возвращает объект, содержащий ключи словаря:
person1_keys = person1.keys()
print(person1_keys)
print(type(person1_keys))
print(list(person1_keys)[1])
print()

# .values() — возвращает объект, содержащий значения словаря:
person1_values = person1.values()
print(person1_values)
print(type(person1_values))
print(list(person1_values)[1])
print()

# .items() — возвращает объект с парами (ключ, значение):
person1_items = person1.items()
print(person1_items)
print(type(person1_items))
print(list(person1_items)[1])
print()

# .update(other) — обновляет словарь, добавляя пары (ключ, значение) из другого словаря.
# Существующие ключи обновляются, новые ключи добавляются:

person1 = {'name': 'Иван', 'age': 30, 'city': 'Москва'}
person1.update({'city': 'Санкт-Петербург', 'профессия': 'инженер'})
print(person1)

current_city = person1.pop('city')
print(current_city)
print(person1)
