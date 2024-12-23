from pprint import pprint
#Задача "Учёт товаров":
class Product:
    def __init__(self, name, weight, category):
        self.name = str(name) #название продукта
        self.weight = float(weight) #общий вес товара
        self.category = str(category) #категория товара
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'product.txt'
    def get_products(self):
        file = open(self._Shop__file_name, 'r')
        pprint(file.read())
        file.close()
    def add(self, *products):
        file = open(self._Shop__file_name, 'r')
        a = file.read()
        for k in products:
            if k.name in a:
                print(f'Продукт {k.name} уже есть в магазине')
            else:
                file.close()
                file2 = open(self._Shop__file_name, 'a')
                file2.write(f'{k}\n')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
