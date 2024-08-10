# Дополнительное практическое задание по модулю: "Наследование классов"

from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=True):
        self.__color = color
        self.__sides = sides
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        self.filled = filled

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        in_range = lambda x: True if x in range(0, 256) else False
        return in_range(r) and in_range(g) and in_range(b)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid_sides(self, *sides):
        for side in sides:
            if not (isinstance(side, int) and side > 0):
                return False
        return len(sides) == self.sides_count

    def get_sides(self):
        return list(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__get_radius()

    def __get_radius(self):
        return self.__len__() / (2 * pi)

    def get_square(self):
        return pi * self.__get_radius() ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.__get_height()

    def __get_height(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return 2 * (p * (p - a) * (p - b) * (p - c)) ** .5 / max(self.get_sides())

    def get_square(self):
        return max(self.get_sides()) * self.__get_height() / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = (*sides,) * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
