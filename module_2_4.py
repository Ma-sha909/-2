#"Все не так уж просто"
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = [ ]
not_primes = [ ]
for i in numbers:
    print("число i", i)
    for n in range(2, i):
        print("число n", n)
        is_primes = (i % n)
        0 == True
        print("остаток от деления", is_primes)
        if is_primes == True:
            primes.append(i)
            break
        if is_primes == False:
            not_primes.append(i)
     
print(primes)
print(set(not_primes))
