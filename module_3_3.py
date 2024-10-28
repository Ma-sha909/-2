"Распаковка"

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

#1.Функция с параметрами по умолчанию:

print_params()
print_params(3)
print_params(b = "длинная строка")
print_params(b = 25)
print_params(c = [1, 2, 3])

#2.Распаковка параметров:

values_list = [1, 'text', True]
values_dict = {'a':3, 'b':'строки', 'c':True}

print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:

values_list_2 = [54.32, 'строка']
print_params(*values_list_2, 42)