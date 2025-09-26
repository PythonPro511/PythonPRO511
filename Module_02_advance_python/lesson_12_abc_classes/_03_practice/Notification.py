"""
Уровень 3. Продвинутый

Задача: написать программу, которая создаёт абстрактный класс Notification с абстрактными методами
send, get_details и retry.
А также создать подклассы EmailNotification и SMSNotification, которые реализуют методы send,
get_details и retry для соответствующих типов уведомлений:

send отправляет уведомление,
симулирует успешную или неуспешную отправку (например, через random) и обновляет статус отправки;
get_details возвращает детали уведомления, включая получателя, сообщение и статус отправки;
retry повторно отправляет уведомление, если предыдущая попытка была неудачной.
Добавьте возможность отправки уведомлений через различные каналы и отслеживания статуса отправки.
"""

from abc import ABC, abstractmethod
import random


class Notification(ABC):
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message
        self.status = 'Pending'

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def retry(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print(f'Отправляю почту в адрес: {self.recipient} содержимое: {self.message}')
        if random.choice([True, False]):
            self.status = 'Sent'
            print(f'Почта отправлена успешно в адрес: {self.recipient}')
        else:
            self.status = 'Failed'
            print(f'Не удалось отправить почту в адрес: {self.recipient}')

    def get_details(self):
        return f'Почтовое уведомление: Получатель {self.recipient}, Содержимое: {self.message}, Статус: {self.status}'

    def retry(self):
        if self.status == 'Failed':
            print(f'Повторная отправка почты в адрес: {self.recipient} содержимое: {self.message}')
            self.send()


class SMSNotification(Notification):
    def send(self):
        print(f'Отправляю SMS в адрес: {self.recipient} содержимое: {self.message}')
        if random.choice([True, False]):
            self.status = 'Sent'
            print(f'SMS отправлена успешно в адрес: {self.recipient}')
        else:
            self.status = 'Failed'
            print(f'Не удалось отправить SMS в адрес: {self.recipient}')

    def get_details(self):
        return f'SMS уведомление: Получатель {self.recipient}, Содержимое: {self.message}, Статус: {self.status}'

    def retry(self):
        if self.status == 'Failed':
            print(f'Повторная отправка SMS в адрес: {self.recipient} содержимое: {self.message}')
            self.send()


if __name__ == '__main__':
    email_notification = EmailNotification("john@example.com", "Hello John!")
    sms_notification = SMSNotification("1234567890", "Hello Jane!")

    # Вывод результата
    email_notification.send()
    print(email_notification.get_details())

    sms_notification.send()
    if sms_notification.status == "Failed":
        sms_notification.retry()
    print(sms_notification.get_details())
