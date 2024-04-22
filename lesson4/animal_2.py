"""
Допишите код под условия в цикле так, чтобы вывод был корректным
"""


class Animal:

    def __init__(self, name):
        self.name = name

    def walk(self):
        pass


class Dog(Animal):

    @staticmethod
    def bark():
        print('Bark!')


class Cat(Animal):

    @staticmethod
    def meow():
        print('Meow!')



animals = [Dog('Dog1'), Dog('Dog2'), Cat('Cat1'), Dog('Dog3')]

for animal in animals:
    # Должно выводиться Bark или Meow в зависимости от того какой класс
    if isinstance(animal, Dog):
        animal.bark()
    if isinstance(animal, Cat):
        animal.meow()
