class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, model, color, engine_power):
        self.owner = str(owner) #владелец (может меняться)
        self._model = str(model) #модель (неизменна)
        self.__engine_power = int(engine_power) #мощность двигателя(неизменна)
        self.__color = str(color) #цвет (нельзя своими руками)
    def get_model(self):
        print(f'Модель {self._model}')
    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')
    def get_color(self):
        print(f'Цвет: {self.__color}')
    def print_info(self):
        print(f'Модель {self._model}, Мощность двигателя: {self.__engine_power}, Цвет: {self.__color}, Владелец: {self.owner}')
    def set_color(self, new_color):
        if new_color.upper() in (iter.upper() for iter in self.__COLOR_VARIANTS):
            self._Vehicle__color = str(new_color)
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 #в седан может поместиться только 5 пассажиров

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()