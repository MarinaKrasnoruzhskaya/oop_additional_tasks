class Rectangle:
    def __init__(self, wingth, height):
        self.wingth = wingth
        self.height = height

    def perimeter(self):
        return 2 * (self.wingth + self.height)

    def area(self):
        return self.wingth * self.height

    def display(self):
        return (f"Длина прямоугольника - {self.height} \n"
                f"Ширина прямоугольника - {self.wingth}\n"
                f"Площадь - {self.area()}\n"
                f"Периметр - {self.perimeter()}")

rectangle = Rectangle(3, 4)
print(rectangle.display())