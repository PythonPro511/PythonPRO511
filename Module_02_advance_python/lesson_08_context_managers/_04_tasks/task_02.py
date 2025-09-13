"""
Задача: написать класс ConfigManager,
который будет использоваться как менеджер контекста для временного изменения конфигурации приложения.
Класс должен содержать атрибут конфигурации (строку), а при инициализации получать новое значение для него.
Во время выполнения блока with конфигурация должна меняться на новую, а при выходе из него принимать начальное значение.
"""

class ConfigManager:

    def __init__(self, new_config_value=None):
        self.config_value = 'config'
        self.new_config_value = new_config_value
        self.old_config_value = None

    def __enter__(self):
        if self.new_config_value:
            self.old_config_value = self.config_value
            self.config_value = self.new_config_value
            print(f'Настройка изменена: {self.old_config_value} >> {self.config_value}')
        else:
            print(f'Запуск с базовой настройкой: {self.config_value}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.old_config_value:
            self.config_value = self.old_config_value
            print(f'Настройка восстановлена: {self.config_value}')
        else:
            print(f'Настройка восстановлена: {self.config_value}')


if __name__ == '__main__':
    with ConfigManager('new_config') as manager_n:
        print('Работаем по логике приложения.')

    with ConfigManager() as manager_d:
        print('Работаем по логике приложения.')
