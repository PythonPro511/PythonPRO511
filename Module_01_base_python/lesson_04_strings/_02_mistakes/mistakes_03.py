# age = 25
# message = "I am " + age + " years old."  # Ошибка, так как age не строка

age = 25
message = "I am " + str(age) + " years old."
print(message)