from datetime import datetime, timedelta


# Функция для вычисления даты с учётом рабочих дней
def add_weekdays(start_date, num_days):
    current_date = start_date
    while num_days > 0:
        current_date += timedelta(days=1)
        if current_date.weekday() < 5:
            num_days -= 1
    return current_date


if __name__ == '__main__':
    date_now = datetime.now()
    delivery_date = add_weekdays(date_now, 5)
    print(f'Дата доставки: {delivery_date.strftime('%d-%m-%Y >> %H:%M:%S')}')
    print()

    date_monday = datetime(2025, 9, 15, 19, 56, 00)
    delivery_date = add_weekdays(date_monday, 5)
    print(f'Дата доставки: {delivery_date.strftime('%d-%m-%Y >> %H:%M:%S')}')
