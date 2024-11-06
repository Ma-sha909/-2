#Задание "Раз, два, три, четыре, пять .... Это не всё?":
elements = []
def calculate_structure_sum(data_structure):
    global elements
    a_int_ = 0
    b_str_ = 0
    c = []
    i = data_structure
    if type(i) is list or type(i) is set or type(i) is tuple:
        for k in i:
            calculate_structure_sum(k)
    else:
        if isinstance(i, dict) is True:
            calculate_structure_sum(list(i.items()))
        else:
            elements.append(i)
    for n in elements:
        if isinstance(n, int) is True:
            a_int_ += n
        if isinstance(n, str) is True:
            for m in n:
                if isinstance(m, int) is True:
                    a_int_ += n
                else:
                    c.append(n)
            b_str_ = len(c)
    return int(a_int_) + int(b_str_)

result = calculate_structure_sum([[1,2,3], {'a':4,'b':5}, (6, {'cube':7, 'drum':8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])])
print(result)
