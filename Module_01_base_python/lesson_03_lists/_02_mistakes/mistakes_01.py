# my_list = [10, 20, 30]
# print(my_list[3])  # IndexError: list index out of range
my_list = [10, 20, 30]
if len(my_list) > 3:
    print(my_list[3])
else:
    print("Индекс вне диапазона")