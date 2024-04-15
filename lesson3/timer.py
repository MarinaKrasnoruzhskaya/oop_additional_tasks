"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
from time import sleep, perf_counter


class Timer:
    def __enter__(self):
        self.start = perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time = perf_counter() - self.start
        print("Execution time:", self.elapsed_time)


with Timer() as timer:
    # блок кода
    sleep(2)
    # код для проверки 

    # print("Execution time:", timer.elapsed_time) # выдаёт ошибку
