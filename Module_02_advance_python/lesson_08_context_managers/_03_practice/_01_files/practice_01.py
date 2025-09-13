class FileManager:

    def __init__(self, file_path, param='rt', encoding=None):
        self.file_path = file_path
        self.param = param
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, self.param, encoding=self.encoding)
        return self

    def read(self):
        return self.file.read()

    def write(self, text):
        self.file.write(text)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Произошла ошибка {exc_type.__name__}: {exc_val}")
            return False
        self.file.close()
        return True


if __name__ == '__main__':
    with FileManager(r'examples\example.txt', 'a', encoding='utf-8') as file:
        file.write('Hello World!\n')

    with FileManager(r'examples\example.txt', encoding='utf-8') as file:
        data = file.read()

    print(data)
