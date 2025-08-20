count = 1

while count <= 10:
    print(count)
    count += 1
print()

user_thirsty = input("Вы утолили жажду? ")
while user_thirsty == "нет":
    print('Вы выпили чашку чая.')
    user_thirsty = input("Вы утолили жажду? ")