from collections import deque

# добавление элементов
d = deque()
d.append(10)
d.appendleft(5)
print(d)
print()

# удаление элементов
d1 = deque([1, 2, 3])
last_item = d1.pop()
print(last_item)
first_item = d1.popleft()
print(first_item)
print(d1)
print()

# индексация
d2 = deque([1, 2, 3, 4])
print(d2[0], d2[1], d2[-1])
print()

# ограничение длины очереди
d3 = deque(maxlen=3)
d3.append(1)
d3.append(2)
d3.append(3)
print(d3)
d3.append(4)
print(d3)
d3.appendleft(5)
print(d3)

# перестановка элементов
d4 = deque([1, 2, 3, 4])
d4.rotate(1)
print(d4)
d4.rotate(-2)
print(d4)
