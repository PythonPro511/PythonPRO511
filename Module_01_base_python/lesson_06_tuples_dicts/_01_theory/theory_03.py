contact_info = {'name': 'Alice', 'email': 'alice@example.com', 'age': 26, 'phone': '123-456-7890'}

if "email" in contact_info:  # по умолчанию проверка осуществляется по ключам (их наличие)
    print("Email найден!")

contact_info['city'] = 'Москва'

contact_info.update({"age": 27})

print(list(contact_info.keys()))
print(list(contact_info.values()))
print(list(contact_info.items()))
