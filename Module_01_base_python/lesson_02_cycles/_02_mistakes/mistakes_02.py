try:
    result = 1 / 0
except Exception:
    print("Что-то пошло не так.")

try:
    result = 1 / 0
except ZeroDivisionError:
    print("На ноль делить нельзя.")

try:
    result = 1 / 0
except Exception as Ex:
    print(type(Ex).__name__)
    print("Что-то пошло не так.")