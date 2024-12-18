#Задание "Они все так похожи":
class Figure:
    sides_count = 0
    a = False
    def __init__(self, color, *sides):
        self.__color = color #список цветов в формате RGB
        if int(len(sides)) == self.sides_count:
            #print(len(sides))
            self.__sides = list(sides)
        else:
            self.__sides = list([1] * self.sides_count) #список сторон целые числа
        filled = 0  # закрашенный, bool

    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b):
        if r in range(250+1) and g in range(250+1) and b in range(250+1):
            return True
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            a = (r, g, b)
            self.__color = a
        else:
            return
    def __is_valid_sides(self, *sid):
        tru_fals = []
        if len(sid) == len(self.__sides):
            for k in sid:
                if isinstance(k, int) is True and k > 0:
                    tru_fals.append(True)
                else:
                    tru_fals.append(False)
            return all(tru_fals)
        else:
            return False
    def get_sides(self):
        return self.__sides
    def __len__(self):
        return int(sum(self.get_sides()))
    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = []
            for n in new_sides:
                self.__sides.append(int(n))
            return self.__sides
        else:
            return

class Circle(Figure):
    sides_count = 1
    __radius = sides_count / 2 * 3.14
    def get_square(self):
        return 3.14 * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        P = sum(self.get_sides() / 2 )
        return P * (P - self.get_sides()[0]) * (P - self.get_sides()[1]) * (P - self.get_sides()[2])

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self._Figure__sides = list([sides] * self.sides_count)
    def get_volume(self):
        a = self.get_sides()[0] ** 3
        return a

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print('1', circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print('2', cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print('3', cube1.get_sides())
circle1.set_sides(15) # Изменится
print('4', circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print('5', len(circle1))
# Проверка объёма (куба):
print('6', cube1.get_volume())
"""Выходные данные (консоль):
[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216"""