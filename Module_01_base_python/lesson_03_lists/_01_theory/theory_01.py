new_list = list()
my_list = [1, 2.5, "Python", True, ['item1', 'item2']]
fruits_list = []
fruits_list.append('apple')
fruits_list.append('banana')
fruits_list.append('cherry')
fruits_list.append('pineapple')

print(new_list)
print(my_list)
print(fruits_list)

other_fruits_list = ['elderberry', 'plum']
fruits_list.extend(other_fruits_list)
print(fruits_list)
print()

try:
    fruits_list.remove('banana')
except ValueError:
    print("Значения нет в списке")
else:
    print('Элемент успешно удален')

# fruit_to_remove = 'banana'
# if fruit_to_remove in fruits_list:
#     fruits_list.remove(fruit_to_remove)
# else:
#     print(f'Элемента {fruit_to_remove} нет в списке')
print(fruits_list)
removed_fruit = fruits_list.pop(1)
print(fruits_list, f'удален {removed_fruit}')
print()
fruits_list[0] = 'blueberry'
print(fruits_list)
print()

sorted_list = sorted(fruits_list)
sorted_list_reverse = sorted(fruits_list, reverse=True)
print(fruits_list)
print(sorted_list)
print(sorted_list_reverse)
print()

fruits_list.sort()
print(fruits_list)
fruits_list.sort(reverse=True)
print(fruits_list)
fruits_list_new = ['blueberry', 'pineapple', 'elderberry', 'plum']
fruits_list_new.reverse()  # реверсирование без сортировки элементов.
print(fruits_list_new)
"0-9A-Za-zА-Яа-я"
