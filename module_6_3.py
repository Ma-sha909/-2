"""
Задача "Ошибка эволюции":
"""
import random
class Animal:
    live = True
    sound = None #звук(изначально отсутствует)
    _DEGREE_OF_DANGER = 0 #степень опасности существа
    def __init__(self, speed):
        self._cords = [0, 0, 0] #- координаты в пространстве.
        self.speed = speed #- скорость передвижения существа(определяется при создании объекта)
    def move(self, dx, dy, dz):
        if dz < 0:
            print("It's too deep, i can't dive :(")
            exit()
        else:
            self._cords = [dx * self.speed, dy * self.speed, dz * self.speed]
    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")
    def speak(self):
        print(self.sound)
class Bird(Animal):
    beak = True #-наличие клюва
    def lay_eggs(self):
        print(f'Here are(is) {random.choice(range(1, 4))} eggs for you')
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        a = dz < self._cords[2]
        if a is True:
            new_speed = self.speed // 2
            self._cords[2] = self._cords[2] - abs(dz) * new_speed
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
class Duckbill(Bird, PoisonousAnimal, AquaticAnimal): #- класс описывающий утконоса
    sound = "Click-click-click" #- звук, который издаёт утконос

#Пример работы программы:
db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()