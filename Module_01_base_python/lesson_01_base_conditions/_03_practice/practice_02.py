card_number = input("Введите номер вашей скидочной карты: ")
discount_input = input("Введите размер вашей скидки в процентах: ")

discount = float(discount_input)
# if discount < 0 or discount > 100:
#     print("Размер скидки должен быть между 0% и 100%")
# else:
#     print(f'Карта №{card_number} активирована. Ваша скидка: {discount}%')

if not 0 < discount < 100:
    print("Размер скидки должен быть между 0% и 100%")
else:
    print(f'Карта №{card_number} активирована. Ваша скидка: {discount}%')
