from abc import ABC, abstractmethod

class Figure(ABC):

    # площадь фигуры
    @abstractmethod
    def area(self):
        pass

    # периметр фигуры
    @abstractmethod
    def perimeter(self):
        pass

    # сумма площади двух фигур
    def add_area(self, figure):
        if hasattr(figure, 'area') == True:
            return self.area + figure.area
        else: raise ValueError

    # название фигуры
    def get_name(self):
        return getattr(self, 'name')
