import logging
from datetime import datetime
import time


class UserSessions:
    def __init__(self, username):
        self.username = username
        self.login_time = None
        self.logout_time = None

    def login(self):
        self.login_time = datetime.now()
        logger.info(f'Пользователь: {self.username} вошел в систему.')

    def logout(self):
        if not self.login_time:
            logger.error(f'Ошибка: пользователь {self.username} не был авторизован.')
            return
        self.logout_time = datetime.now()
        session_duration = self.logout_time - self.login_time
        logger.info(f'Пользователь {self.username} вышел из системы. Продолжительность сессии: {session_duration}')

    def change_settings(self, new_username):
        if not self.login_time:
            logger.error(f'Ошибка: пользователь {self.username} не авторизован для изменения настроек.')
            return
        logger.info(f'Пользователь: {self.username} изменил настройки имени новое имя >> {new_username}')
        self.username = new_username


# Создание логгера
logger = logging.getLogger('user_actions')
logger.setLevel(logging.INFO)

# Создание обработчика для записи в файл
file_handler = logging.FileHandler('user_actions_log.log', encoding='utf-8')
file_handler.setLevel(logging.INFO)

# Настройка формата логов
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

if __name__ == '__main__':
    user1 = UserSessions('Alex')
    user1.login()
    user1.change_settings('SuperAlex')
    time.sleep(5)
    user1.logout()
    print()

    user2 = UserSessions("Eva")
    user2.change_settings("NewEva")
