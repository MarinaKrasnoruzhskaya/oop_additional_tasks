"""
Напишите класс User, имеющий следующие свойства и методы:

- __init__(self, name, password): конструктор, принимающий имя пользователя и пароль
- name: свойство, которое возвращает имя пользователя
- password: свойство, которое позволяет установить или изменить пароль пользователя
- is_admin: свойство, которое возвращает, является ли пользователь администратором или нет
- _is_admin: свойство-помощник, которое определяет, является ли пользователь администратором или нет
- login(self, password): метод, который проверяет, соответствует ли введенный пароль паролю пользователя
- logout(self): метод, который выходит из аккаунта пользователя (устанавливает значение свойства _is_logged_in в False при условии, что пользователь залогинен)

Для свойств name и password используйте декораторы @property и @password.setter.
"""


class User:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        self._is_admin = False
        self._is_logged_in = True

    @property
    def name(self):
        return f'{self.__name}'

    @property
    def password(self):
        return f'{self.__password}'

    @password.setter
    def password(self, pass_new):
        self.__password = pass_new

    @property
    def is_admin(self):
        return self._is_admin

    @name.setter
    def name(self, value):
        self.__name = value


    def login(self, password):
        return self.__password == password

    def logout(self):
        if self._is_logged_in:
            self._is_logged_in = False


# код для проверки
user1 = User("Alice", "qwerty")
print(user1.name)  # Alice
print(user1.password)  # qwerty
print(user1.is_admin)  # False

user1.password = "newpassword"
print(user1.password)  # newpassword

user1._is_admin = True
print(user1.is_admin)  # True

user1.login("newpassword")  # True
user1.logout()
