"""
Напишите класс Animal, представляющий животное, имеющий следующие методы:

- __init__(self, name): конструктор, принимающий имя животного;
- speak(self): метод, который выводит звук, издаваемый животным.

Напишите класс Dog, наследующийся от класса Animal, представляющий собаку, имеющий следующие методы:

- speak(self): метод, который выводит звук, издаваемый собакой.

Напишите класс Cat, наследующийся от класса Animal, представляющий кошку, имеющий следующие методы:

- speak(self): метод, который выводит звук, издаваемый кошкой.
"""


class Animal:
    """класс Animal, представляющий животное"""
    def __init__(self, name):
        """конструктор, принимающий имя животного"""
        self.name = name

    @staticmethod
    def speak():
       """метод, который выводит звук, издаваемый животным"""
       print("?")


class Dog(Animal):
    """класс Dog, наследующийся от класса Animal, представляющий собаку"""
    @staticmethod
    def speak():
        """метод, который выводит звук, издаваемый собакой"""
        print("Woof!")


class Cat (Animal):
    """класс Cat, наследующийся от класса Animal, представляющий кошку"""
    @staticmethod
    def speak():
        """метод, который выводит звук, издаваемый кошкой"""
        print("Meow!")


# код для проверки 
animal = Animal("Animal")
animal.speak()  # ?

dog = Dog("Dog")
dog.speak()  # Woof!

cat = Cat("Cat")
cat.speak()  # Meow!
