# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set)
#
# my_set.remove(2)
# print(my_set)
# my_set.discard(5)
# print(my_set)
#
# my_set.clear()
# print(my_set)

my_set = {1, 2, 3}
copy_set = my_set.copy()
copy_set.add(4)
copy_set.add(4)
copy_set.add(4)
print(my_set)
print(copy_set)

print(len(copy_set))

guests = {"Charlie", "Eve", "Alice", "Frank"}
popped_guest = guests.pop()
print(popped_guest)

