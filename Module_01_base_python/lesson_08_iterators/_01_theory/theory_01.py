# numbers = [1, 2, 3]
# iterator = iter(numbers)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# numbers = [1, 2, 3]
# for number in numbers:
#     print(number)
#

numbers = [1, 2, 3]
iterator = iter(numbers)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
