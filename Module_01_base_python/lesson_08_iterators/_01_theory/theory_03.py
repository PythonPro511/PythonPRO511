text = "Python"
iterator = iter(text)
print(next(iterator))
print(next(iterator))

numbers_set = {10, 20, 30}

iterator = iter(numbers_set)

for number in iterator:
    print(number)
