import asyncio


async def simulate_download(file_name, delay):
    print(f"Начало загрузки файла: {file_name}")
    await asyncio.sleep(delay)
    print(f"Загрузка файла завершена: {file_name}. Время загрузки: {delay}")


async def simulate_downloads(file_list):
    tasks = []
    for file in file_list:
        # print(*file, sep=', ')
        filename, delay = file
        task = asyncio.create_task(simulate_download(filename, delay))
        tasks.append(task)

    for task in tasks:
        await task


if __name__ == "__main__":
    files = [
        ("file1.txt", 4),
        ("file2.txt", 1),
        ("file3.txt", 2.5)
    ]
    asyncio.run(simulate_downloads(files))
