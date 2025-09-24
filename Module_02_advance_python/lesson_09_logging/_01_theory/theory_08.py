from datetime import datetime

now = datetime.now()
print(now)

formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_date)
print(type(formatted_date))

# %Y — год (четырёхзначный);
# %m — месяц (двухзначный);
# %d — день (двухзначный);
# %H — час (24-часовой формат);
# %M — минуты;
# %S — секунды.

some_text = 'Сегодня 17*09*2025, 19-28'
date_from_text = datetime.strptime(some_text, 'Сегодня %d*%m*%Y, %H-%M')
print(date_from_text)
print(type(date_from_text))

