import asyncio


async def my_coroutine(sleep_time):  # в данном случае параметр sleep_time нужен для наглядности
    print(f"Start {sleep_time}")
    await asyncio.sleep(sleep_time)
    print(f"End {sleep_time}")


async def main(sleep_time):
    task1 = asyncio.create_task(my_coroutine(sleep_time + 2))
    task2 = asyncio.create_task(my_coroutine(sleep_time))

    await task1
    await task2


if __name__ == '__main__':
    asyncio.run(main(1))
