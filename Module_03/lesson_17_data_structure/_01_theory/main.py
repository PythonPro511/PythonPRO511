from _01_Parser import parse_currency_rates
from _02_Database import init_db, save_rates_to_db

if __name__ == '__main__':
    user_currencies = ['BYN', 'USD', 'EUR']
    my_currencies = [
        ('BYN', 'Белорусский рубль'),
        ('USD', 'Доллар США'),
        ('EUR', 'Евро')
    ]
    init_db('currencies', my_currencies)
    rates = parse_currency_rates(user_currencies)
    if save_rates_to_db('currencies', rates):
        print(f'Данные успешно сохранены в БД')
    else:
        print("Ошибка при сохранении данных")
