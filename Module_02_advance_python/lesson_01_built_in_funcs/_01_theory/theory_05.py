nums_list = [1, 2, 3]
letters_list = ['a', 'b', 'c', 'd']

# [(1, 'a'), (2, 'b'), (3, 'c'))
print(list(zip(nums_list, letters_list)))

for num, letter in zip(nums_list, letters_list):
    print(f'Число: {num} Буква: {letter}')
