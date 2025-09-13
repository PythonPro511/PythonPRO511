from collections import defaultdict

# Примеры использования defaultdict:
# С list - полезно для группировки данных:

dd1 = defaultdict(list)
dd1['a'].append(1)
dd1['a'].append(2)
dd1['b'].append(2)
dd1['c'].append(3)
print(dd1)
print()

# С int - часто используется для подсчёта элементов:
dd2 = defaultdict(int)
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
for fruit in data:
    dd2[fruit] += 1
print(dd2)
print()


# С пользовательской функцией - можем использовать свою функцию для задания значений по умолчанию:
def default_value():
    return 'значение по умолчанию'


dd3 = defaultdict(default_value)
print(dd3['missing_key'])
print(dd3)
print()

# Группировка данных - использование defaultdict для группировки элементов по ключу:
data = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
grouped = defaultdict(list)
for k, v in data:
    grouped[k].append(v)
print(grouped)
