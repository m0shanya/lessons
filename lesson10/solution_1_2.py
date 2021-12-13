"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса;
методы: нахождение периметра и площади окружности),
Triangle (атрибуты: три точки, методы: нахождение площади и периметра),
Square (атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
"""

from math import pi


class Point:
    def __init__(self, point_x, point_y):
        self.point_x = point_x
        self.point_y = point_y


class Figure:
    def __init__(self, perimetr=None, square=None):
        self.perimetr = perimetr
        self.square = square


class Circle(Figure):
    def __init__(self, coord_c, radius):
        super().__init__()
        self.coord_xc = coord_c
        self.radius = radius

    def circle_per(self):
        self.perimetr = 2 * pi * self.radius
        return self.perimetr

    def circle_square(self):
        self.square = pi * (self.radius) ** 2
        return self.square


class Square(Figure):
    def __init__(self, point_1, point_2):
        super().__init__()
        self.point_1 = point_1
        self.point_2 = point_2
        # side_arr = [j - i for i, j in zip(point_1, point_2)]
        # self.side = abs(side_arr[0] - side_arr[1])
        self.lenght = self.side()

    def side(self):
        x0 = self.point_1.point_x
        y0 = self.point_1.point_y
        x1 = self.point_2.point_x
        y1 = self.point_2.point_y

        self.lenght = abs((x0 - x1) + (y0 - y1))
        return self.lenght

    def square_per(self):
        perimetr = 4 * self.lenght
        return perimetr

    def square_square(self):
        square = self.lenght ** 2
        return square


class Triangle(Figure):
    def __init__(self, p_1, p_2, p_3):
        super().__init__()
        self.p_1 = p_1
        self.p_2 = p_2
        self.p_3 = p_3
        self.lenght_1 = self.side()
        self.lenght_2 = self.side()
        self.lenght_3 = self.side()

    def side(self):
        x0 = self.p_1.point_x
        y0 = self.p_1.point_y
        x1 = self.p_2.point_x
        y1 = self.p_2.point_y
        x2 = self.p_3.point_x
        y2 = self.p_3.point_y

        self.lenght_1 = abs((x0 - x1) + (y0 - y1))
        self.lenght_2 = abs((x1 - x2) + (y1 - y2))
        self.lenght_3 = abs((x2 - x0) + (y2 - y0))
        return self.lenght_1, self.lenght_2, self.lenght_3

    def triangle_per(self):
        perimetr = self.lenght_1 + self.lenght_2 + self.lenght_3
        return perimetr


"""
    def square_square(self, perimetr):
        # формула Герона( полупериметр, три стороны и квадратный корень)
        self.pol_per = perimetr / 2
        self.square = self.lenght ** 2
        return self.square
"""

if __name__ == '__main__':

    center = Point(2, 0)
    radius = 8
    c = Circle(center, radius)

    point_1 = Point(1, 1)
    point_2 = Point(5, 2)
    point_3 = Point(5, 5)
    t = Triangle(point_1, point_2, point_3)

    pt_1 = Point(0, 0)
    pt_2 = Point(4, 0)
    s = Square(pt_1, pt_2)

    my_list = [c, t, s]
    for figures in my_list:
        if figures == my_list[0]:
            # print(f"Perimetr of circle: {figures.circle_per}")
            print(f"Square of circle: {figures.circle_square}")
        elif figures == my_list[2]:
            print(f"Square of square: {figures.square_square}")
            # print(f"Perimetr of square: {figures.square_per}")
        elif figures == my_list[1]:
            print(f"Perimetr of triangle: {figures.triangle_per}")
