# my_tuple = (1, 2, 3)
# second_item = my_tuple[1]
# print(second_item)
# print()
#
# my_tuple = (1, 2, 3, 4, 5, 6)
# sub_tuple = my_tuple[1:4]
# print(sub_tuple)
# print()
#
# new_tuple = my_tuple + (7, 8, 9)
# print(new_tuple)
# print()
#
# repeated_tuple = (my_tuple * 2)
# print(repeated_tuple)
# print()
#
# print(5 in my_tuple)
# print(10 in my_tuple)
# print()

my_tuple = (1, 2, 3, 4, 5, 6)
print(len(my_tuple))
print()

my_tuple = (1, 2, 2, 3, 3, 3, 4, 5, 6)
print(my_tuple.count(2))
print(my_tuple.count(3))
print(my_tuple.count(1))
print(my_tuple.count(15))
print()

items_tuple = ('item1', 'item2', 'item3', 'item2')
print("Индекс искомого элемента: ", items_tuple.index('item2'))
