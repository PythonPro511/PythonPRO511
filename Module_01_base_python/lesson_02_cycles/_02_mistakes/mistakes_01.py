# # Цикл while без условия выхода
# while True:
#     print("Бесконечный цикл")

count = 0
while count < 5:
    print("Конечный цикл")
    count += 1  # Условие выхода из цикла

while True:
    user_input = input("Введите стоп!")
    if user_input == 'стоп':
        break
    print("Крутим цикл")