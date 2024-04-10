class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def display(self):
        return f"длина {self.width}, ширина {self.height}, периметр {self.perimeter()} и площадь {self.area()}"


restangle = Rectangle(3, 5)
print(restangle.display())
