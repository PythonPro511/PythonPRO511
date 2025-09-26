import asyncio


async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)
    print("End")


if __name__ == '__main__':
    asyncio.run(my_coroutine())