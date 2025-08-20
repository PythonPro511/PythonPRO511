my_set_t = {1, 2, (3, 4)}
# my_set_l = {1, 2, [3, 4]}


math_students = {"Alice", "Bob", "Charlie"}
physics_students = {"Bob", "Dave", "Eve"}

# Студенты, записавшиеся на оба курса
both_courses = math_students.intersection(physics_students)
# both_courses = math_students & physics_students
print(f"Оба курса: {both_courses}")

# Только на математику
only_math = math_students.difference(physics_students)
# only_math = math_students - physics_students
print(f"Только математика: {only_math}")

# Записались хотя бы на один курс
any_course = math_students.union(physics_students)
# any_course = math_students | physics_students
print(f'Хотя бы 1 курс: {any_course}')
