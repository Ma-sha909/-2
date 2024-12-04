#Задача "Съедобное, несъедобное":
from tkinter.font import names
class Animal:
    def __init__(self, name):
        self.alive = True #живой
        self.fed = False #накормленный
        self.name = name  #имя
    def eat(self, food):
        if type(food) is Flower or type(food) is Fruit:
            if food.adible is True:
                self.fed = True
                print(f'{self.name} съел {food.name}')
            else:
                self.alive = False
                print(f'{self.name} не стал есть {food.name}')

class Plant:
    adible = False
    def __init__(self, name):
        self.name = name   #имя
        pass
class Mammal(Animal):
    pass
class Predator(Animal):
    pass
class Flower(Plant):
    pass
class Fruit(Plant):
    adible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)