person1 = {}
person1['name'] = 'Иван'
person1['age'] = 30
print(person1)

person2 = {'name': 'Мария', 'age': 22}
print(person2)

person3 = dict(name='Алексей', age='45')
print(person3)

print(person3['name'])
print(person3['age'])

person3['name'] = 'Игорь'
print(person3)

person4 = dict([('name', 'Alice'), ('email', 'alice@example.com'), ('age', 26), ('phone', '123-456-7890')])
