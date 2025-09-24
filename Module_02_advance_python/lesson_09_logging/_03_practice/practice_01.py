import logging

# Создание логгера
logger = logging.getLogger('order_logger')
logger.setLevel(logging.ERROR)

# Создание обработчика для записи в файл
file_handler = logging.FileHandler('orders_errors.log', encoding='utf-8')
file_handler.setLevel(logging.ERROR)

# Настройка формата логов
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

if __name__ == '__main__':
    try:
        raise ValueError("Некорректные данные заказа!")
    except ValueError as e:
        logger.error(f'Ошибка обработки заказа: {e}')
