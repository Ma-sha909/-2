#Домашнее задание по теме "Создание функций на лету"
first = 'Мама мыла раму'
second = 'Рамена мало было'
a = list(map(lambda x, y: x == y, first, second))
print(a)

import pprint
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        for i in data_set:
            i = str(i)
            with open(file_name, "a", encoding='utf-8') as file:
                print(file.write('i'))

            #file = open(file_name, "a", encoding='utf8')
            #pprint.pprint(file.write('i\n'))
        #file.close()
    return write_everything
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice
class MysticBall:
    def __init__(self, *words):
        self.words = list(words)
    def __call__(self):
        a = choice(self.words)
        return a
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
