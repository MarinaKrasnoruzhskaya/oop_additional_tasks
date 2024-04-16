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
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product):
        return cls(**product)

    @property
    def price(self):
        return  self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __add__(self, other):
        return self.quantity * self.price + other.quantity * other.price

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
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.products)

    @property
    def products(self):
        products_str = ''
        for product in self.__products:
            products_str += str(product) + '\n'
        return products_str

    def number_products_in_category(self):
        """
        вычисляет количество продуктов категории
        """
        total = 0
        for product in self.__products:
            total += product.quantity
        return total

    def cost_of_all_goods(self):
        """
        вычисляет стоимость всех продуктов в self.__products
        """
        total_cost = 0
        for product in self.__products:
            total_cost += product.quantity * product.price
        return total_cost

    def __add__(self, other):
        return self.cost_of_all_goods() + other.cost_of_all_goods()

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.number_products_in_category()} шт."


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

# Test, 1000 руб. Остаток: 10 шт.
# True
# Test2, 500 руб. Остаток: 20 шт.

print(categories[0] + categories[1])
