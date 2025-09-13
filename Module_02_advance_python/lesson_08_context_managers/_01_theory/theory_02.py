class FileWriter:

    def __init__(self, file_path, encoding=None):
        self.file_path = file_path
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, 'w', encoding=self.encoding)
        return self

    def write(self, text):
        self.file.write(text)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Ошибка: {exc_val}")
        self.file.close()
        return True


if __name__ == '__main__':
    with FileWriter(r'example_files\example02ex.txt', encoding='utf-8') as writer:
        writer.write('Hello World!\n')
        writer.write('Привет Мир!')
        raise Exception('Ошибка при записи!')
