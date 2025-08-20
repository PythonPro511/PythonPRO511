nums_list = [1, 2, 3]
new_list = list()
for num in nums_list:
    new_list.append(num ** 2)

print(new_list)
print()

nums_list = [1, 2, 3]
result = map(lambda x: x ** 2, nums_list)
print(result)
print(list(result))

for value in map(lambda x: x ** 2, nums_list):
    print(value)
print()


def calculate_square(x):
    return x ** 2


result = map(calculate_square, nums_list)
print(list(result))

upper_lambda = lambda letter: letter.upper()
result = map(upper_lambda, 'привет')
print(list(result))

