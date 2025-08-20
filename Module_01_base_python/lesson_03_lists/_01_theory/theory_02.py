# numbers = [10, 20, 30, 40, 50]
# #           0   1   2   3   4
# #          -1  -2  -3  -4  -5
# number_idx_0 = numbers[0]
# print(number_idx_0)
# print(numbers[3])
# print(numbers[-4])
# print(numbers[-2])
# print()
#
# slice_of_numbers = numbers[1:4]
# print(slice_of_numbers)
# print(numbers[:3])
# print(numbers[2:])
# print(numbers[::2])
# print(numbers[1::2])


numbers = [10, 20, 30, 40, 50]
print(len(numbers))
print(numbers[1:len(numbers) - 1])

for i in range(len(numbers)):
    print(numbers[i])
print()

matrix = [
    [1, 2, 3],  # 0
    [4, 5, 6],  # 1
    [7, 8, 9]  # 2
]

first_row = matrix[1]
element = matrix[1][1]
print(first_row)
print(element)
