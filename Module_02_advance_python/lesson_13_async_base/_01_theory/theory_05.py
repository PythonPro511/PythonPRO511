import asyncio


async def my_coroutine():  # в данном случае параметр sleep_time нужен для наглядности
    print(f"Start ")
    await asyncio.sleep(2)
    print(f"End")
    return "Done"


async def main():
    task = asyncio.create_task(my_coroutine())
    print(f'Task done: {task.done()}')
    await task
    print(f'Task result: {task.result()}')
    print(f'Task done: {task.done()}')


if __name__ == '__main__':
    asyncio.run(main())
