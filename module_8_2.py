#Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции"
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except(TypeError):
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчета суммы - {i}')
    return result, incorrect_data

def calculate_average(numbers):
    try:
        a = personal_sum(numbers)
        result2 = a[0] / (len(numbers) - a[1])
    except(ZeroDivisionError):
        result2 = 0
    except(TypeError):
        result2 = None
        print('В numbers записан некорректный тип данных')
    return result2
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
