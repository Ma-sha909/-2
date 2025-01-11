#Задача "Вызов разом":
def apply_all_func(int_list, *functions):
    results = {}
    for i in int_list:
        if isinstance(i, int) is True or isinstance(i, float) is True:
            continue
        else:
            int_list.remove(i)
            int_list.append(float(i))
    for i in functions:
        results.update({i.__name__ : i(int_list)})
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


