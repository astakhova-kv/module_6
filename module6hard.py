from math import pi


class Figure:
    sides_count = 0

    def __init__(self, __color, *sides):
        if len(sides) != self.sides_count and len(sides) != 1:
            self.__sides = [1] * self.sides_count
        elif len(sides) == 1:
            self.__sides = [*sides] * self.sides_count
        else:
            self.__sides = list(sides)
        self.filled = False
        self.__color = __color

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        count = 0
        for i in range(len(new_sides)):
            if new_sides[i] == int(new_sides[i]) and new_sides[i] > 0:
                count += 1
        if count == self.sides_count:
            return True

    def __len__(self):
        perim = sum(self.__sides)
        return perim

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, __sides):
        Figure.__init__(self, __color, __sides)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        s = pi * self.__radius ** 2
        return round(s, 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, __sides):
        Figure.__init__(self, __color, __sides)
        self.__sides = super().get_sides()

    def get_square(self):
        p = sum(self.get_sides()) / 2
        a, b, c = self.get_sides()
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return round(s, 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, __sides):
        Figure.__init__(self, __color, __sides)
        self.__sides = [__sides] * 12

    def get_volume(self):
        v = self.get_sides()[0] ** 3
        return v


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
treug = Triangle((200, 200, 100), 10)
treug.set_sides(15, 12, 17)
print(treug.get_sides())
print(treug.get_square())
