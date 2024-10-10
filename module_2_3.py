#'Нули ничто, отрицание недопустимо'
my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5]
a = 0
while a < len(my_list) :
    if int(my_list [int(a)]) >= 0 :
        print(my_list[int(a)])
        a = int(int(a) + 1)
        continue
    else:
        break
