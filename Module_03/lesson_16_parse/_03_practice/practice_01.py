"""
Задача 1: Парсинг сайта «Академии ТОП»
Ситуация:
Вы получили задачу разработать скрипт для сбора текстовой информации с главной страницы
https://spb.top-academy.ru.
Ваши коллеги посоветовали вам воспользоваться библиотекой BeautifulSoup для эффективной загрузки результатов.

Используйте следующий код для тестирования инструмента:
if __name__ == "__main__":
    url = "https://spb.top-academy.ru"
    paragraphs = get_paragraphs(url)

    if paragraphs:
        print(paragraphs[:100])
    else:
        print("Не удалось получить параграфы со страницы")

Задача:

Создайте новую функцию для GET-запроса к указанному сайту.
Укажите заголовки, URL, пропишите тайм-ауты и добавьте обработку ошибок с raise_for_status.

Задача 2: Дорабатываем функцию get_paragraphs

Ситуация:
Вы продолжаете разрабатывать функцию для получения текстовой информации со страницы. Добавьте метод для парсинга информации с помощью BeautifulSoup.

Задача:
Доработайте функцию, добавив создание объекта soup и выгрузку параграфов.
"""
import requests
from bs4 import BeautifulSoup


def get_paragraphs(url):
    """Получение параграфов с указанной страницы"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        result = []
        for p in soup.find_all('p'):
            text = p.get_text().strip()
            if text:
                result.append(text)
        return result
    except requests.exceptions.RequestException as e:
        print(f'Ошибка при запросе: {e}')
        return None
    except AttributeError:
        print(f'Не удалось получить нужные элементы на странице.')
        return None
    except Exception as e:
        print(f'Неизвестная ошибка: {e}')
        return None


# if __name__ == "__main__":
#     url = "https://spb.top-academy.ru"
#     paragraphs = get_paragraphs(url)
#
#     if paragraphs:
#         print(paragraphs[:100])
#     else:
#         print("Не удалось получить параграфы со страницы")


if __name__ == "__main__":
    parser = SimpleParagraphParser()
    url = "https://spb.top-academy.ru"
    paragraphs = parser.get_paragraphs(url)
    if paragraphs:
        print("Первые 5 параграфов:")
    for i, p in enumerate(paragraphs[:5], 1):
        print(f"{i}. {p[:100]}..." if len(p) > 100 else f"{i}. {p}")
    else:
        print("Не удалось получить параграфы со страницы")
