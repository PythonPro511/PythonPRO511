import re

text = 'Пользователь написал: "Привет" и ушёл.'
pattern = r'"......"'
matches = re.findall(pattern, text)
print(matches)


text = 'Пользователь написал: "Привет" и ушёл. А потом добавил: "Пока!".'
pattern = re.compile(r'"(.*?)"')
matches = re.findall(pattern, text)
print(matches)
