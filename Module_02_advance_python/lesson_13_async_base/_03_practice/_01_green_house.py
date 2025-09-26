import asyncio
import random


async def temperature_sensor():
    """Симуляция работы датчика температуры"""
    for _ in range(5):
        gather_time = random.uniform(1, 3)
        await asyncio.sleep(gather_time)
        temperature = random.uniform(-10, 35)
        print(f'[Температура] Данные: {temperature:.2f}°C >> t сбора {gather_time:.2f} секунд')


async def humidity_sensor():
    """Симуляция работы датчика влажности"""
    for _ in range(5):
        gather_time = random.uniform(1, 3)
        await asyncio.sleep(gather_time)
        humidity = random.uniform(30, 90)
        print(f'[Влажность] Данные: {humidity:.2f}% >> t сбора {gather_time:.2f} секунд')


async def main():
    temperature_task = asyncio.create_task(temperature_sensor())
    humidity_task = asyncio.create_task(humidity_sensor())

    # Ожидаем завершения всех задач
    await temperature_task
    await humidity_task


if __name__ == '__main__':
    asyncio.run(main())
