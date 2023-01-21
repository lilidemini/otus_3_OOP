class Materials:
    WOOD = 15.0
    STEEL = 50.0
    PAPER = 1.0

class Cube:

    def __init__(self, h, w, d, material):
        self.h = h
        self.w = w
        self.d = d
        self.material = material

# СПОСОБЫ СОЗДАНИЯ ЦЕНЫ
    # СПОСОБ 1. price как атрибут класса в функции __init__():
        self.price_attribute = self.w * self.d * self.h * self.material
    # но, тогда значение price не будет изменяться в экземпляре cube
    # при изменении атрибутов w, d, h, material в экземпляре cube

    # СПОСОБ 2. price как метод класса:
    def price_method(self):
        return self.w * self.d * self.h * self.material
    # не соответствует концепции ООП, так как price - существительное
    # и должно вызываться как атрибут cube.price
    # а не как метод cube.price()

    # СПОСОБ 3. price как метод класса с property:
    # соответствует концепции ООП
    # декоратор property для вычисляемых атрибутов
    # теперь метод price вызывается как атрибут, а не метод
    @ property
    def price(self):
        return self.w * self.d * self.h * self.material

cube = Cube(h=1, w=2, d=5, material=Materials.WOOD)
print(cube.price_method()) # 150.0

# изменить значение у атрибута ширина w
cube.w = 10.0

# вызовем атрибут price из способа 1 с измененным значением ширины w
print(cube.price_attribute) # 150.0

# вызовем метод price из способа 2 с измененным значением ширины w
print(cube.price_method()) # 750.0

# вызовем метод price как атрибут из способа 3 с измененным значением ширины w
print(cube.price) # 750.0
