# Задача "Рекурсивное умножение цифр":

def get_multiplied_digits(number):
    str_number = str(number)
    print(str_number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        if first > 0:
            return first
        else:
            first = 1
            return first

result = get_multiplied_digits(40203)
print(result)
