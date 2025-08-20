# Инициализация списка срочных ключевых слов, которые могут указывать на необходимость немедленного ответа
urgent_keywords = ["асап", "сейчас", "немедленно"]

# Ввод текста обращения клиента
client_message = input("Введите текст обращения клиента: ")

# Анализ текста на наличие срочных ключевых слов
urgent = False
for keyword in urgent_keywords:
    if keyword in client_message.lower():
        urgent = True
        break

# Вывод срочного сообщения
if urgent:
    client_message = "СРОЧНО: " + client_message.upper()
print("Обработанное обращение:", client_message)