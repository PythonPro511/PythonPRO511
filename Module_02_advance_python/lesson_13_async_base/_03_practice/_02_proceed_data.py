import asyncio
import random


async def download_page(url):
    """Симулирует загрузку страницы."""
    print(f'Начинаю загрузку: {url}')
    download_time = random.uniform(1, 5)
    await asyncio.sleep(download_time)
    print(f'Загрузка завершена: {url}. Время загрузки >> {download_time:.2f}')


async def main(urls):
    # Создаём таски для каждой загрузки
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_page(url))
        tasks.append(task)

    for task in tasks:
        await task


if __name__ == '__main__':
    # Список URL-адресов
    my_urls = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3",
        "https://example.com/page4",
        "https://example.com/page5",
    ]

    # Запускаем Event Loop
    asyncio.run(main(my_urls))
