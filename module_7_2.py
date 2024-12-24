from pprint import pprint
#Задача "Записать и запомнить":
def custom_write(file_name, strings):
    name = open(file_name, 'a', encoding = 'utf-8')
    strings_positions = {}
    s = 0
    for i in strings:
        s += 1
        a = name.tell()
        name.write(f'{i}\n')
        strings_positions.update({(s, a):(i)})
    name.close()
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)