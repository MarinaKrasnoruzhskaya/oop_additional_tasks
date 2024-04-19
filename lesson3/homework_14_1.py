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
        return self.quantity * self.price + other.quantity * other.price

    def __len__(self):
        return self.quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."


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
    def products(self, new_product: Product):
        """ Метод-сеттер добавляет новый продукт в список продуктов"""
        self.__products.append(new_product)

    def cost_of_all_goods(self):
        """
        Метод вычисляет стоимость всех продуктов в self.__products
        """
        total_cost = 0
        for product in self.__products:
            total_cost += product.quantity * product.price
        return total_cost

    def __add__(self, other):
        return self.cost_of_all_goods() + other.cost_of_all_goods()

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

product_item = Product('Test', 'Test', 1000, 10)
print(product_item)
print(str(product_item) == 'Test, 1000 руб. Остаток: 10 шт.')
product_item_2 = Product('Test2', 'Test2', 500, 20)
print(product_item_2)

product_item = Product('Test', 'Test', 1000, 10)

print(str(categories[0]) == 'Смартфоны, количество продуктов: 27 шт.')

print( str(product_item) == 'Test, 1000 руб. Остаток: 10 шт.')


product_item_2 = Product('Test2', 'Test2', 500, 20)

print( product_item + product_item_2 == 20000)