fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     if fruit == "banana":
#         fruits.remove(fruit)

for i in range(len(fruits)):
    if fruits[i] == 'banana':
        fruits.pop(i)


# fruits = ["apple", "banana", "cherry"]
# new_fruits = fruits
# print(fruits)
# print(new_fruits)
#
# new_fruits.remove('banana')
# print(fruits)
# print(new_fruits)
# print(fruits == new_fruits)
# print(fruits is new_fruits)
# print()
#
# fruits = ["apple", "banana", "cherry"]
# new_fruits_slice = fruits[:]
# print(fruits == new_fruits_slice)
# print(fruits is new_fruits_slice)
#
# new_fruits_list = list(fruits)
# print(fruits == new_fruits_list)
# print(fruits is new_fruits_list)
#
# new_fruits_copy = fruits.copy()
# print(fruits == new_fruits_copy)
# print(fruits is new_fruits_copy)


# fruits = ["apple", "banana", "cherry"]
#
# for fruit in fruits[:]:
#     if fruit == "banana":
#         fruits.remove(fruit)
# print(fruits)