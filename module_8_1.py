#Домашнее задание по теме "Try и Except"
def add_everything_up(a, b):
    try:
        c = a + b
    except(TypeError):
        c = f'{a}{b}'
    finally:
        return c
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
