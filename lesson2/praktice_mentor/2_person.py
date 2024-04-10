from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f'{self.name}, ему {self.age}')

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

person = Person('Иван', 19)
person.display()

person1 = Person.fromBirthYear('Николай',  2000)
person1.display()
