"""
Задание 1. Мониторинг теплицы с использованием asyncio.gather

Ситуация: мы продолжаем разработку «умного дома» из предыдущего занятия.
Напоминаю, что в данный момент мы работаем над системой, контролирующей микроклимат в теплице.
Для контроля условий выращивания растений установлены два датчика: температуры и влажности.
В этот раз наша система должна гарантировать,
что время прихода данных с датчиков (температуры и влажности) не превышает 3 секунд.

Задача:

Реализовать имитацию сбора данных с двух датчиков за заданное время (случайные значения от 1 до 3 секунд,
использовать библиотеку random).
Параллельно получать данные с обоих датчиков, чтобы не терять время в ожидании завершения работы одного из них.
"""

import asyncio
import random
from datetime import datetime


async def read_temperature_sensor(task_num):
    """Имитация считывания данных с датчика температуры."""
    print(f'Считывание данных с датчика температуры {task_num}...')
    await asyncio.sleep(random.uniform(1, 3))
    temp = random.uniform(18, 30)
    print(f'Температура в теплице {task_num}: {temp:.2f}°C')
    return temp


async def read_humidity_sensor(task_num):
    """Имитация считывания данных с датчика влажности."""
    print(f'Считывание данных с датчика влажности {task_num}...')
    await asyncio.sleep(random.uniform(1, 3))
    humidity = random.uniform(40, 70)
    print(f'Влажность в теплице {task_num}: {humidity:.2f}%')
    return humidity


async def monitoring_climate():
    """Мониторинг данных с датчиков температуры и влажности."""
    print(datetime.now())
    temperature_tasks = [read_temperature_sensor(i) for i in range(1, 4)]
    humidity_tasks = [read_humidity_sensor(i) for i in range(1, 4)]

    all_tasks = temperature_tasks + humidity_tasks

    results = await asyncio.gather(*all_tasks, return_exceptions=True)
    print(results)
    temperature1, temperature2, temperature3, humidity1, humidity2, humidity3 = results
    print(f'Средняя температура: {(temperature1 + temperature2 + temperature3) / 3:.2f}°C')
    print(f'Средняя влажность: {(humidity1 + humidity2 + humidity3) / 3:.2f}%')
    print(datetime.now())


if __name__ == '__main__':
    asyncio.run(monitoring_climate())
