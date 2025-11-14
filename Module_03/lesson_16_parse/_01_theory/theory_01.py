import requests
from bs4 import BeautifulSoup

# Прописываем ссылку на ресурс, который будем парсить
url = "https://habr.com/ru/articles/"
url_page = "https://habr.com/ru/articles/965432/"
response = requests.get(url=url_page)
html = response.text
# 'html.parser' — стандартный парсер для обработки HTML-документов
soup = BeautifulSoup(html, 'html.parser')

# Находит первый тег с заголовками первого уровня <h1>
title = soup.find('h1')
# Все теги параграфов <p>
all_paragraphs = soup.find_all('p')

# Находит элемент div с классом "tm-article-body"
article_content = soup.find('div', class_="tm-article-body")
# Находит ссылку с указанным href (hyperreference, значением гиперссылки)
author_link = soup.find("a", {'href': "ru/users/username/"})

# print(title)
# print(all_paragraphs)
# print(article_content)
# print(author_link)
