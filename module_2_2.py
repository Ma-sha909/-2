first= int(input("введите первое число"))
second= int(input("введите второе число"))
third= int(input("введите третье число"))
#Если все числа равны между собой, то вывести 3
if first==second==third:
    print(3)
#Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
elif first==second or first==third or third==second:
    print(2)
#сли равных чисел среди 3-х вообще нет, то вывести 0
else:
    print(0)