#Домашнее задание по уроку "Пространство имен"

def test_function(name):
    def iner_function(name):
        print('Я в области видимости функции test_function')
    iner_function(name)
    return

a = test_function(14)
b = iner_function(name)
print(a)
print(b)