import requests
from bs4 import BeautifulSoup

# Прописываем ссылку на ресурс, который будем парсить
url = "https://habr.com/ru/articles/"
url_page = "https://habr.com/ru/articles/965432/"
response = requests.get(url=url_page)
html = response.text
# 'html.parser' — стандартный парсер для обработки HTML-документов
soup = BeautifulSoup(html, 'html.parser')

title = soup.find('h1', class_='tm-title').text.strip()
print(title)
content = soup.find("div", class_="tm-article-body").text.strip()
print(content)

print(f"Заголовок: {title}\n\nТекст: {content[:200]}...")


