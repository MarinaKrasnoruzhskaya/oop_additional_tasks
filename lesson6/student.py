"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число
- Оценки - список из целых чисел, может быть пустым

Опишите класс Student и метод avg_rate так, чтобы считалась средняя оценка, а при пустом списке оценок возвращался 0

"""


class Student:

    def __init__(self, name, course, estimates=None):
        self.name = name
        self.course = course
        self.estimates = estimates if estimates else []

    def avg_rate(self):
        try:
            print(round(sum([estimate for estimate in self.estimates]) / len(self.estimates), 2))
        except ZeroDivisionError:
            print(0.0)


# код для проверки
student = Student('Ivan', 'Python', [5, 4, 5, 5])
student.avg_rate() # 4.75

student = Student('Ivan', 'Python', [])
student.avg_rate() # 0.0
