"""
Ошибка 2: Отсутствие обработки изменений структуры сайта
Проблема:
Сайты часто меняют структуру HTML, что ломает существующие парсеры.
"""
import requests
from bs4 import BeautifulSoup

# Старый парсер
response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find('span', class_='product-price').text
# После изменений на сайте класс стал 'new-price-class'
"""
Решение:
1) Использовать более устойчивые селекторы (например, data-атрибуты).
2) Реализовать систему оповещений о сбоях:
"""


def send_alert():
    print(f'ТРЕВОГА! ЧТО-ТО ПОШЛО НЕ ТАК!')
    pass


try:
    price = soup.find('span', {'data-testid': 'price'}).text
except AttributeError:
    send_alert()
