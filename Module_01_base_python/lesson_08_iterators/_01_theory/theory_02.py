# # Решение без итераторов:
# with open('students.txt', 'r', encoding='utf-8') as file:
#     data = file.readlines()
#     print("Первые 10 строк")
#     print(data[:10])
#
# data_list = []
# for d in data[:]:
#     clean_data = d.strip()
#     data_list.append(clean_data)
#
# print(data_list[:10])
# print()

# Решение с итераторами в функции:
def display_num_of_strings(strings_num=0):
    with open('students.txt', 'r', encoding='utf-8') as file:
        iterator = iter(file)
        print(f"Первые {strings_num} строк: ")
        for _ in range(strings_num):
            try:
                print(next(iterator).strip())
            except StopIteration:
                print("Файл закончился.")
                break


if __name__ == '__main__':
    user_strings = int(input("Введите число строк для вывода: "))
    display_num_of_strings(user_strings)
