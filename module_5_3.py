#Задача "Нужно больше этажей":
class House:
    def __init__(self,name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'
    def __eq__(self, other):
        if isinstance(other, House) is True and isinstance(other.number_of_floors, int) is True:
            return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        if isinstance(other, House) is True and isinstance(other.number_of_floors, int) is True:
            return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        if isinstance(other, House) is True and isinstance(other.number_of_floors, int) is True:
            return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        if isinstance(other, House) is True and isinstance(other.number_of_floors, int) is True:
            return self.number_of_floors > other.number_of_floor
    def __ge__(self, other):
        if isinstance(other, House) is True and isinstance(other.number_of_floors, int) is True:
            return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        if isinstance(other, House) is True and isinstance(other.number_of_floors, int) is True:
            return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        if isinstance(value, int) is True:
            self.number_of_floors += value
            return f'Название: {self.name}, количество этажей: {self.number_of_floors}'
    def __radd__(self, value):
        if isinstance(value, int) is True:
            self.number_of_floors += value
            return f'Название: {self.name}, количество этажей: {self.number_of_floors}'
    def __iadd__(self, value):
        if isinstance(value, int) is True:
            self.number_of_floors += value
            return f'Название: {self.name}, количество этажей: {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print("1", h1)
print("2", h2)
print("3", h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print("4", h1)
print("5", h1 == h2)
h1 += 10 # __iadd__
print("6", h1)
h2 = 10 + h2 # __radd__
print("7", h2)
print("8", h1 > h2) # __gt__
print("8", h1 >= h2) # __ge__
print("8", h1 < h2) # __lt__
print("8", h1 <= h2) # __le__
print("8", h1 != h2) # __ne__