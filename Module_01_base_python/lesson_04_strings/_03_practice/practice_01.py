keywords = ['срочно', 'важно', 'немедленно', 'директор']
message = input("Введите ваше сообщение: ")

urgent = False

for keyword in keywords:
    if keyword in message.lower():
        urgent = True
        break

if urgent:  # if urgent is True:
    message = 'ВНИМАНИЕ: ' + message.upper()
print(f'Обработанное сообщение: {message}')
