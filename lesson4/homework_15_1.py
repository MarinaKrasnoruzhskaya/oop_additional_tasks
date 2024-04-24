import warnings

warnings.filterwarnings('ignore')


class Product:
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
        self.quantity = quantity

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
        products.append(Product.new_product(product))
    category['products'] = products
    categories.append(Category(**category))

# 1
product_item = Product('Test', 'Test', 1000, 10)
product_item_2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5,  'Xiaomi', 10000, 'red')
product_item_3 = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')


try:
    product_item + product_item_2
except TypeError:
    print('Ошибка сложения. Нельзя складывать не экземпляры одного класса')

print(product_item + product_item == 20000)

# Ошибка сложения. Нельзя складывать не экземпляры одного класса
# True

# 2

try:
    categories[0].products = 1
except TypeError:
    print('Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)')

categories[0].products = product_item
print(product_item.name in categories[0].products)

# Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)
# True

# 3
# print(product_item_2.name)
# print(product_item_2.quantity)
# print(product_item_2.description)
# print(product_item_2.price)
# print(product_item_2.efficiency)
# print(product_item_2.model)
# print(product_item_2.model)
# print(product_item_2.memory)
# print(product_item_2.color)

# 4
# print(product_item_3.country)
# print(product_item_3.germination_period)
# print(product_item_3.color)
# print(product_item_3.name)
# print(product_item_3.description)
# print(product_item_3.price)
# print(product_item_3.quantity)
