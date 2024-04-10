class House:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        if self._price:
            return self._price
        else:
            return f"AttributeError: 'House' object has no attribute '_price'."

    @ price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Пожалуйста, введите корректное значение")

    @price.deleter
    def price(self):
        self._price = None


house = House(50000.0)
print(house.price)

house.price = 45000.0
print(house.price)

house.price = -50
print(house.price)

del house.price
print(house.price)