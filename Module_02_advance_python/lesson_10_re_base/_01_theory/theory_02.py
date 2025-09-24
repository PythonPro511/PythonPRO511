import re

text = "Мой телеграм - @username. Но лучше свяжитесь со мной по email: user@example.com или support@domain.org."

# pattern = re.compile(r'[A-Za-z0-9_]+@yandex\.ru')
pattern = re.compile(r'[\w.-]+@[\w.-]+\.[a-zа-яё]+')
matches = re.findall(pattern, text)
print(matches)

