import asyncio
from datetime import datetime


async def task1():
    await asyncio.sleep(3)
    print("Результат задачи 1")
    return "Результат задачи 1"


async def task2():
    await asyncio.sleep(1)
    print("Результат задачи 2")
    return "Результат задачи 1"


async def main():
    print(datetime.now())
    results = await asyncio.gather(task1(), task2())
    print(results)
    print(datetime.now())

if __name__ == '__main__':
    asyncio.run(main())
