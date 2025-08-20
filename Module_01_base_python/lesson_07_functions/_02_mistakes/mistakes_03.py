"""
Тип ошибки 3: Использование несуществующего модуля — ModuleNotFoundError: No module named ‘non_existent_module’

Пример ошибки:
"""
# import non_existent_module

"""
Решение:

Проверьте название модуля и установите его, если он отсутствует (в данном случае python-dotenv).
"""
from dotenv import load_dotenv
