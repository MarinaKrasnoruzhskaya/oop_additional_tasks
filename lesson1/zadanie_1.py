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
        self.price = price
        self.quantity = quantity

class Category:
    """
    Класс для категорий товара
    """
    name: str
    description: str
    products: list[Product]

    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(self.products)


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
#1
# categories = []
# for category in data:
#     products = []
#     for product in category['products']:
#         print(product)
#         products.append(Product(**product))
#     category['products'] = products
#     categories.append(Category(**category))

#2
# categories = []
# for category in data:
#     products = []
#     for product in category['products']:
#         products.append(Product(**product))
#     category['products'] = products
#     categories.append(Category(**category))
# for product in products:
#     print(product.name)
#     print(product.description)

#3
# categories = []
# for category in data:
#     products = []
#     for product in category['products']:
#
#         products.append(Product(**product))
#     category['products'] = products
#     categories.append(Category(**category))
#
# for product in products:
#     print(product.price)
#     print(product.quantity)

#4
# categories = []
# for category in data:
#     products = []
#     for product in category['products']:
#
#         products.append(Product(**product))
#     category['products'] = products
#     categories.append(Category(**category))
#
# for product in products:
#     print(product.price)
#     print(product.quantity)

#5
# categories = []
# for category in data:
#     products = []
#     for product in category['products']:
#
#         products.append(Product(**product))
#     category['products'] = products
#
#     categories.append(Category(**category))
#
# for category in categories:
#     print(category.name)
#     print(category.description)

#6
categories = []
for category in data:
    products = []
    for product in category['products']:

        products.append(Product(**product))
    category['products'] = products

    categories.append(Category(**category))
print(categories)
for category in categories:
    print(category.category_count)
    print(category.product_count)
