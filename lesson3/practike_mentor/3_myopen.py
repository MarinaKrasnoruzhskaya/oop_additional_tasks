from time import perf_counter, sleep


class MyOpen:

    def __init__(self, file_name, mode='r'):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.fp = open(self.file_name, self.mode)
        self.start = perf_counter()
        print("Файл успешно открыт")
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Файл был открыт {perf_counter() - self.start} секунд и теперь успешно закрыт.")
        return self.fp.close()

with MyOpen('countries.txt', 'r') as fp:
    content = fp.read()
    print('Чтение данных 2 секунды...')
    sleep(2)

print('Продолжение кода...')