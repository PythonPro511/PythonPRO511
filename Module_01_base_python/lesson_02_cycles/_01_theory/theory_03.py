for number in range(1, 11):
    if number == 5:
        break
    print(number)
else:
    print('цикл завершен без прерываний')
print()

for number in range(1, 11):
    if number == 5 or number == 7:
        continue
    print(number)
print()
