from collections import Counter
import re


def count_words(text: str) -> Counter:
    text = text.lower()
    words = re.split(r'[-:;.,!? \n]+', text)
    words.pop()
    return Counter(words)


if __name__ == '__main__':
    my_text = "Hello world! Hello Python. Python is great, world is big."
    result = count_words(my_text)
    print(result)
    # [0-9A-Za-zА-Яа-яЁё]+