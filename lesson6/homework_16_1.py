from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass


class PrintMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}, '{self.description}', {self.price}, {self.quantity})"


class Product(BaseProduct, PrintMixin):
    """
    Класс для описания товара в магазине
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """ Конструктор для Product"""
        self.name = name
        self.description = description
        self.__price = price
        if quantity:
            self.quantity = quantity
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        super().__init__()

    @classmethod
    def new_product(cls, product):
        """ Класс-метод для создания объекта класса Product """
        return cls(**product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __add__(self, other):
        if type(self) is type(other):
            return self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError

    def __len__(self):
        return self.quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    """Класс для описания смартфона"""
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для описания трава газонная"""
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """
    Класс для категорий товара
    """
    name: str
    description: str
    products: list

    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        """ Конструктор для категории товара"""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        """ Метод-геттер выводит список товаров в виде строк """
        products_str = ''
        for product in self.__products:
            products_str += str(product) + '\n'
        return products_str

    @products.setter
    def products(self, new_product):
        """ Метод-сеттер добавляет новый продукт в список продуктов"""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
        else:
            raise TypeError

    def cost_of_all_goods(self):
        """
        Метод вычисляет стоимость всех продуктов в self.__products
        """
        total_cost = 0
        for product in self.__products:
            total_cost += product.quantity * product.price
        return total_cost

    def __add__(self, other):
        if isinstance(self, Smartphone) and isinstance(other, Smartphone) or isinstance(self, LawnGrass) and isinstance(other, LawnGrass):
            return self.cost_of_all_goods() + other.cost_of_all_goods()
        else:
            raise TypeError

    def __str__(self):
        total = 0
        for product in self.__products:
            total += len(product)
        return f"{self.name}, количество продуктов: {total} шт."

    def middle_price(self):
        try:
            return sum([p.price for p in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0

# 1

data = [
    {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        "products": [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5
            },
            {
                "name": "Iphone 15",
                "description": "512GB, Gray space",
                "price": 210000.0,
                "quantity": 8
            },
            {
                "name": "Xiaomi Redmi Note 11",
                "description": "1024GB, Синий",
                "price": 31000.0,
                "quantity": 14
            }
        ]
    },
    {
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        "products": [
            {
                "name": "55 QLED 4K",
                "description": "Фоновая подсветка",
                "price": 123000.0,
                "quantity": 7
            }
        ]
    }
]
categories = []
for category in data:
    products = []
    for product in category['products']:
        products.append(Product.new_product(product))  # добавленный метод
    category['products'] = products
    categories.append(Category(**category))

product_item = Product('Test', 'Test', 1000, 10)
product_item_2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5, 'Xiaomi', 10000, 'red')
product_item_3 = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')

try:
    broken_product = Product('Test', 'Test', 1000, 0)
except ValueError as e:
    print( str(e) == "Товар с нулевым количеством не может быть добавлен")

# Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)
# Product('Iphone 15', '512GB, Gray space', 210000.0, 8)
# Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
# Product('55 QLED 4K', 'Фоновая подсветка', 123000.0, 7)
# Product('Test', 'Test', 1000, 10)
# Smartphone('Test2', 'Test2', 2000, 10)
# LawnGrass('Test3', 'Test3', 3000, 10)
# True

# 2
print( categories[0].middle_price() == 140333.33333333334)

#3
null_category = Category('Test', 'Test', [])

print( null_category.middle_price() == 0)