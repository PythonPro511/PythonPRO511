import re

text = "Сегодня я узнал много нового о #Python и #регулярных выражениях. #Программирование — это круто!"

pattern = re.compile(r'#\w+')
hashtags = re.findall(pattern, text)
print(f'Найденные хэштеги: {', '.join(hashtags)}')
