#'Нули ничто, отрицание недопустимо'
my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5]
a = 0
while 1 > 0 :
    if int(my_list[int(a)]) >= 0 :
        print(my_list[int(a)])
        if int(a) < len(my_list):
            a = int(int(a) + 1)
        else:
            break
    else:
        break
