# from datetime import date


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def pers_name(self):
        return self.__name

    @property
    def pers_age(self):
        return self.__age

    @pers_name.setter
    def pers_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self.__name = new_name

    @pers_age.setter
    def pers_age(self, new_age):
        if new_age in range(1, 120):
            self.__age = new_age

    # @classmethod
    # def fromBirthYear(cls, name, year):
    #     return cls(name, date.today().year - year)


person = Person('Иван', 19)
print(person.pers_name)
print(person.pers_age)

# person1 = Person.fromBirthYear('Николай',  2000)
# print(person.pers_name)
# print(person.pers_age)

person.pers_name = 'Николай'
print(person.pers_name)

person.pers_age = 25
print(person.pers_age)
