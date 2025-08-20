# my_list = list(range(8 + 1))
# print(my_list)
#
# new_list = []
#
# for element in my_list:
#     if element % 2 == 0:
#         new_list.append(element)
#
# print(new_list)


my_list = list(range(8 + 1))
is_even = lambda x: x % 2 == 0
print(is_even(10))

result = filter(is_even, my_list)
print(result)
print(list(result))
