"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""
from datetime import datetime


class Car:
    """ класс Car, представляющий машину"""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        if year <= datetime.now().year:
            self.year = year
        else:
            raise Exception('Эта машина еще не была выпущена')



# код для проверки
car = Car('Toyota', 'Corolla', 2022)

car = Car('Toyota', 'Corolla', 3000)
# raises Exception('Эта машина еще не была выпущена')
