from src.figure import Figure

class Triangle(Figure):

    def __init__(self, side_a=None, side_b=None, side_c=None):
        if side_a == None or side_b == None or side_c == None:
            raise ValueError
        else:
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
            self.name = 'Треугольник'

    # площадь треугольника по формуле Герона
    @property
    def area(self):
        p = (self.side_a + self.side_b + self.side_c)/ 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5

    # периметр треугольника
    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
