from src.figure import Figure

class Rectangle(Figure):

    def __init__(self, side_a=None, side_b=None):
        if side_a == None or side_b == None or type(side_a) not in (int, float) or type(side_b) not in (int, float):
            raise ValueError
        else:
            self.side_a = side_a
            self.side_b = side_b
            self.name = 'Прямоугольник'

    # площадь прямоугольника
    @property
    def area(self):
        return self.side_a * self.side_b

    # периметр прямоугольника
    @property
    def perimeter(self):
        return 2 * (self.side_a + self.side_b)
