#Домашнее задание по теме "Декораторы"
def is_prime(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        for i in range(a):
            if i > 1:
                x = []
                x.append(a % i)
        if any(x) is True:
            print("Простое")
            return a
        else:
            print("Составное")
            return a
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
