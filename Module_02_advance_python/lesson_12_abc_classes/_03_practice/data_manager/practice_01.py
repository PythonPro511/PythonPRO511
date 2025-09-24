from abc import ABC, abstractmethod


class DataManager(ABC):

    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self):
        pass


class FileDataManager(DataManager):

    def __init__(self, filename='data.txt', encoding='utf-8'):
        self.filename = filename
        self.encoding = encoding

    def save(self, data):
        with open(self.filename, 'w', encoding=self.encoding) as file:
            file.write(data)

    def load(self):
        with open(self.filename, 'r', encoding=self.encoding) as file:
            return file.read()


class DatabaseDataManager(DataManager):
    def __init__(self):
        self.data = None

    def save(self, data):
        self.data = data

    def load(self):
        return self.data


if __name__ == '__main__':
    file_manager = FileDataManager(filename=r'data/data.txt')
    file_manager.save('Пример записи данных')
    print(file_manager.load())

    db_manager = DatabaseDataManager()
    db_manager.save('Пример данных в БД')
    print(db_manager.load())
