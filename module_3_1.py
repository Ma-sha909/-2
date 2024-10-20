print('Первый вариант:')
calls = 0
def count_calls():
    print(calls)

def string_info(string):
    c = [len(string), string.upper(), string.lower()]
    global calls
    calls += 1
    print(c)

def is_contauns(string, list_to_search):

    list_to_search = [n.lower() for n in list_to_search]
    if string.lower() in list_to_search:
        b = True
    else:
        b = False
    global calls
    calls += 1
    print(b)

string_info('Capybara')
string_info('Armageddon')
is_contauns('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contauns('cycle', ['recycling', 'cyclic'])
count_calls()

print("Второй вариант:")

calls2 = 0
def count_calls2():
    global calls2
    calls2 += 1

def string_info2(string):
    c = [len(string), string.upper(), string.lower()]
    count_calls2()
    print(c)

def is_contauns2(string, list_to_search):
    list_to_search = [n.lower() for n in list_to_search]
    if string.lower() in list_to_search:
        b = True
    else:
        b = False
    count_calls2()
    print(b)

string_info2('Capybara')
string_info2('Armageddon')
is_contauns2('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contauns2('cycle', ['recycling', 'cyclic'])
print(calls2)
