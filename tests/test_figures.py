from src.square import Square
from src.triangle import Triangle
from src.circle import Circle
from src.rectangle import Rectangle
import pytest

# создание дефолтных экземпляров класса
square = Square(5)
circle = Circle(5)
triangle = Triangle(3, 4, 5)
rectangle = Rectangle(2, 3)

@pytest.mark.parametrize('figure, expected_name', [
    (square, 'Квадрат'), (circle, 'Круг'),
    (rectangle, 'Прямоугольник'), (triangle, 'Треугольник')])
def test_figure_name(figure, expected_name):
    # проверка соответсвия названия фигуры классу
    assert figure.get_name() == expected_name, 'Wrong figure name'

@pytest.mark.parametrize('figure, expected_area', [
    (square, 25), (circle, 78.5),
    (rectangle, 6), (triangle, 6)])
def test_check_area(figure, expected_area):
    # проверка расчета площади фигуры
    assert figure.area == expected_area, 'Unexpected area of figure'

@pytest.mark.parametrize('figure, expected_perimeter', [
    (square, 20), (circle, 31.400000000000002),
    (rectangle, 10), (triangle, 12)])
def test_check_perimeter(figure, expected_perimeter):
    # проверка расчета периметра фигуры
    assert figure.perimeter == expected_perimeter, 'Unexpected perimeter of figure'

@pytest.mark.parametrize('figure, other_figure, expected_result', [
    (square, circle, 103.5), (square, rectangle, 31), (square, triangle, 31),
    (circle, square, 103.5), (circle, rectangle, 84.5), (circle, triangle, 84.5),
    (rectangle, circle, 84.5), (rectangle, square, 31), (rectangle, triangle, 12),
    (triangle, circle, 84.5), (triangle, rectangle, 12.0), (triangle, square, 31)])
def test_sum_areas_figure_and_other_figure(figure, other_figure, expected_result):
    # проверка расчета суммы площадей двух фигур
    assert figure.add_area(other_figure) == expected_result, 'Unexpected sum of areas of figures'

@pytest.mark.parametrize('figure', [square, circle, rectangle, triangle])
def test_type_perimeter_and_area(figure):
    # проверка, что периметр фигур целое или вещественное число
    assert isinstance(figure.perimeter, (int, float)), 'Wrong type of perimeter returned, expected integer or float'
    # проверка, что площадь фигур целое или вещественное число
    assert isinstance(figure.area, (int, float)), 'Wrong type of area returned, expected integer or float'

@pytest.mark.parametrize('side', [None, "str"])
def test_value_error_circle_not_figure(side):
    # проверка получения ValueError при создании не геометрической фигуры Круг
    with pytest.raises(ValueError):
        Circle(side)

@pytest.mark.parametrize('side', [None, "str"])
def test_value_error_square_not_figure(side):
    # проверка получения ValueError при создании не геометрической фигуры Квадрат
    with pytest.raises(ValueError):
        Square(side)

@pytest.mark.parametrize('side', [None, "str", 2])
def test_value_error_rectangle_not_figure(side):
    # проверка получения ValueError при создании не геометрической фигуры Прямоугольник
    with pytest.raises(ValueError):
        Rectangle(side)

@pytest.mark.parametrize('side', [None, "str", 2])
def test_value_error_triangle_not_figure(side):
    # проверка получения ValueError при создании не геометрической фигуры Круг
    with pytest.raises(ValueError):
        Triangle(side)
