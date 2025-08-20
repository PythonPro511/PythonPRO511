fruits = ["apple", "banana", "cherry"]
fruits_new = ["pineapple", "blueberry", "plum"]
for fruit in fruits:
    print(fruit)
print()

if len(fruits) == len(fruits_new):
    for i in range(len(fruits)):
        print(f'Индекс:     {i}. Элемент:     {fruits[i]}')
        print(f'Индекс new: {i}. Элемент new: {fruits_new[i]}')
print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
row_index = 0
for val1, val2, val3 in matrix:
    print(f"Ряд c индексом: {row_index}. Значения ряда: {val1}, {val2}, {val3}")
