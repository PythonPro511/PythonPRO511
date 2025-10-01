import asyncio
from datetime import datetime


async def task1():
    await asyncio.sleep(3)
    print("Результат задачи 1")
    return "Результат задачи 1"


async def task2():
    await asyncio.sleep(2)
    print("Результат задачи 2")
    return "Результат задачи 1"


async def main():
    print(datetime.now())
    result1 = await task1()
    result2 = await task2()
    print(datetime.now())
    print([result1, result2])


if __name__ == '__main__':
    asyncio.run(main())
