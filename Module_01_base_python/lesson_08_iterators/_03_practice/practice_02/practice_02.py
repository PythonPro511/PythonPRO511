# Список шагов рецепта
recipe_steps = [
    "Нагрейте сковороду",
    "Добавьте масло",
    "Положите нарезанные овощи",
    "Обжарьте до готовности",
    "Посыпьте специями и подавайте"
]

recipe_iterator = iter(recipe_steps)

while True:
    try:
        step = next(recipe_iterator)
        print(f'Шаг: {step}')
    except StopIteration:
        print("Рецепт завершен")
        break
