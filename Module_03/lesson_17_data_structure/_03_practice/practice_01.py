"""
Задача 1: Парсинг курсов валют с сайта ЦБ РФ
Ситуация:
Написать Python-скрипт для парсинга актуальных курсов валют с официального сайта Центрального Банка России.
URL для парсинга: https://www.cbr.ru/currency_base/daily/
Задача:
Написать скрипт с обработкой ошибок и протестировать функцию. Представить результат в виде словаря:
{
    'USD': {'value': 92.45, 'unit': 1},
    'EUR': {'value': 99.12, 'unit': 1},
    'CNY': {'value': 12.87, 'unit': 10}
}
Шаги реализации:

1) Отправляем запрос с тайм-аутом.
2) Создаем объект BeautifulSoup.
3) Находим таблицу с курсами.
4) Инициализируем словарь для хранения результатов.
5) Перебираем строки таблицы.
6) Фильтруем нужные валюты.
"""

import requests
from bs4 import BeautifulSoup


def parce_currency_rates(currencies):
    url = "https://www.cbr.ru/currency_base/daily/"
    try:
        # 1. Отправляем запрос с тайм-аутом
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Проверяем успешность запроса

        # 2. Создаем объект BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # 3. Находим таблицу с курсами
        table = soup.find('table', {'class': 'data'})

        # 4. Инициализируем словарь для результатов
        rates = {}

        # 5. Перебираем строки таблицы
        for row in table.find_all('tr')[1:]:  # Пропускаем заголовок
            cols = row.find_all('td')

            # Проверяем, что строка содержит достаточно данных
            if len(cols) >= 5:
                currency_code = cols[1].text.strip()

                # 6. Фильтруем нужные валюты
                if currency_code in currencies:
                    unit = int(cols[2].text.strip())
                    value = float(cols[4].text.replace(',', '.'))

                    # 7. Сохраняем данные
                    rates[currency_code] = {
                        'value': value,
                        'unit': unit
                    }
        return rates

    except requests.exceptions.RequestException as e:
        print(f'Ошибка при запросе: {e}')
        return None


if __name__ == '__main__':
    currency_codes = ['USD', "EUR", "BYN", "CNY"]
    result = parce_currency_rates(currency_codes)
    if result:
        print(f'Актуальные курсы валют:')
        for currency, data in result.items():
            print(f'{currency}: {data['value']} руб. за {data['unit']} ед.')
    else:
        print(f'Ну удалось получить данные')
