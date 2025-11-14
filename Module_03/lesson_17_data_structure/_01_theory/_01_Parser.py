import requests
from bs4 import BeautifulSoup


def parse_currency_rates(currencies):
    url = "https://www.cbr.ru/currency_base/daily/"

    try:
        # 1. Отправляем HTTP-запрос к странице
        response = requests.get(url)

        # 2. Создаем объект BeautifulSoup для анализа HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 3. Находим таблицу с курсами валют
        table = soup.find('table', class_='data')

        # 4. Извлекаем все строки таблицы, кроме заголовка
        rows = table.find_all('tr')[1:]

        # 5. Создаем словарь для хранения результатов
        rates = {}

        # 6. Обрабатываем каждую строку таблицы
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 5:
                currency = cols[1].text.strip()
                # 7. Фильтруем только нужные валюты
                if currency in currencies:
                    # 8. Преобразуем значение курса в число
                    value = float(cols[4].text.replace(',', '.'))
                    rates[currency] = {"value": value}
        return rates
    except Exception as ex:
        print(f'Ошибка при работе возникло исключение: {type(ex).__name__} >> {ex}')
        return None


# if __name__ == '__main__':
#     user_currencies = input("Введите валюты через пробел: ").upper().split()
#     our_rates = parse_currency_rates(user_currencies)
#     print(our_rates)
