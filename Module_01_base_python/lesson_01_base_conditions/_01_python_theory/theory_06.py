# user_num = int(input("Введите целое число: "))
#
# if user_num > 0:
#     print(f'Число: {user_num} - положительное.')
# elif user_num == 0:
#     print(f'Число: {user_num} равно 0.')
# else:
#     print(f'Число: {user_num} - отрицательное.')


condition1 = True
condition2 = True
if condition1:
    print("Условие 1 истинно!")
    print("Поэтому мы видим эти строки!")
    if condition2:
        print("Условия 1 и 2 истинны!")
        print("Поэтому мы видим и эти вложенные строки!")


if condition1 and condition2:
    print("Условия 1 и 2 истинны!")
    print("Поэтому мы видим и эти новые строки!")
