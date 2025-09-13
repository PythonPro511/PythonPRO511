from collections import Counter

# когда использовать Counter
# Подсчёт элементов:
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
counter = Counter(data)
print(counter)
print()

# Доступ к значениям:
print(counter['banana'])
print(counter['grape'])
print()

# Метод most_common() - возвращает список самых частых элементов в порядке убывания их частоты:
print(counter.most_common(2))
print()

# Метод update() - позволяет обновить счётчик, добавляя новые элементы или увеличивая количество уже существующих.
counter.update(['apple', 'banana', 'grape'])
print(counter)
print()

# Арифметические операции:
# объекты Counter поддерживают сложение, вычитание, пересечение и объединение.
# Сложение:
c1 = Counter(a=2, b=3)
c2 = Counter(a=1, b=2)
print(c1 + c2)

# Вычитание:
print(c1 - c2)

# Пересечение
print(c1 & c2)

# Объединение
print(c1 | c2)
