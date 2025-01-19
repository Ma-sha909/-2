#Домашнее задание по теме "Генераторы"
def all_variants(text):
    a = len(text)
    i = 0
    while i in range(a):
        for k in range(i,a):
            yield text[i:k+1]
        i += 1

a = all_variants("abc")
for i in a:
    print(i)