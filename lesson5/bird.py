"""
Напишите класс Bird, представляющий птицу, имеющий следующие методы:

- fly(self): метод, который выводит сообщение "Flying".

Напишите класс Penguin, наследующийся от класса Bird, представляющий пингвина, имеющий следующие методы:

- fly(self): метод, который выводит сообщение "I am a penguin and cannot fly".

Напишите класс Eagle, наследующийся от класса Bird, представляющий орла, имеющий следующие методы:

- hunt(self): метод, который выводит сообщение "Hunting".
"""


class Bird:
    """ класс Bird, представляющий птицу """
    def fly(self):
        """ метод, который выводит сообщение 'Flying'"""
        print("Flying")


class Penguin(Bird):
    """ класс Penguin, наследующийся от класса Bird, представляющий пингвина """
    def fly(self):
        """метод, который выводит сообщение 'I am a penguin and cannot fly'"""
        print("I am a penguin and cannot fly")


class Eagle(Bird):
    """ класс Eagle, наследующийся от класса Bird, представляющий орла """
    def hunt(self):
        """ метод, который выводит сообщение 'Hunting'"""
        print('Hunting')


# код для проверки 
bird = Bird()
bird.fly()  # Flying

penguin = Penguin()
penguin.fly()  # I am a penguin and cannot fly

eagle = Eagle()
eagle.fly()  # Flying
eagle.hunt()  # Hunting
