from src.figure import Figure

class Square(Figure):
    def __init__(self, side_a=None):
        if side_a == None or type(side_a) not in (int, float):
            raise ValueError
        else:
            self.side_a = side_a
            self.name = 'Квадрат'

    # площадь квадрата
    @property
    def area(self):
        return self.side_a ** 2

    # периметр квадрата
    @property
    def perimeter(self):
        return 4 * self.side_a

    def check_side(self):
        if self.side_a == None:
            raise ValueError
