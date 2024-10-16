import random
#Матрица воплоти:
def get_matrix(n, m, Value):
    matrix = []
    #matrix.insert([1:1] 0)
    for i in range(n):
        matrix += []
        #matrix += a
        for j in range(m):
            matrix.insert(i, (Value))
            #matrix.append(i, (Value))
            #mayrix[1].insert(1, 'Value')
    return matrix


result1 = get_matrix(2,2,10)
print(result1)
result2 = get_matrix(3,5,42)
print(result2)
result3 = get_matrix(4,2,13)
print(result3)
