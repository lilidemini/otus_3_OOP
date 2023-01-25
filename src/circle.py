from src.figure import Figure

class Circle(Figure):
    def __init__(self, radius=None):
        if radius == None or type(radius) not in (int, float):
            raise ValueError
        else:
            self.radius = radius
            self.pi = 3.14
            self.name = 'Круг'

    # площадь круга
    @property
    def area(self):
        return self.pi * (self.radius ** 2)

    # периметр круга
    @property
    def perimeter(self):
        return 2 * self.pi * self.radius
