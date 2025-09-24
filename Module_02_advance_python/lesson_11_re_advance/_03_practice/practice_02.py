import re

text = "Это тестовый текст, в котором есть повторяющиеся слова слова."

pattern = re.compile(r'\b(\w+)\s+\1\b')
duplicates = re.findall(pattern, text)
print(f'Повторяющиеся слова: {duplicates}')
