# Номер 4987 Поляков
'''for c1 in '123456789':
    for c2 in '123456789':
        a = int(f'1{c1}34567{c2}9')
        if a % 17 == 0:
            print(a, a // 17)'''

# Номер 4988 Поляков
'''from fnmatch import *
for x in range(0, 10**8+1, 169):
    if fnmatch(str(x), '1?23*4?5'):
        print(x, x // 169)'''

# простой алгоритм для нахождения делителей числа
'''a = int(input())
b = []
for i in range(1, a + 1):
    if a % i == 0:
        b.append(i)
print(b)'''

# усовершенствованный алгоритм для нахождения делителей числа
'''def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


print(div(36))'''

# Номер 2926 Поляков
'''def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for i in range(209834, 209857 + 1):
    if len(div(i)) == 4:
        print(div(i))'''

# Номер 2858 Поляков
'''def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for i in range(135790, 163228 + 1):
    if sum(div(i)) >= 460000:
        print(len(div(i)), sum(div(i)))'''

# Номер 2905 Поляков
'''def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for j in range(123456789, 223456789 + 1, 2):
    if len(div(j)) == 3:
        print(j, j**0.5)'''

# Номер 2562 Поляков
'''def f(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for x in range(174457, 174505 + 1):
    if len(f(x)) == 2:
        print(f(x))'''

# Номер 2572 Поляков
'''def f(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            if i % 2 == 0:
                d.add(i)
            if (x // i) % 2 == 0:
                d.add(x // i)
    return sorted(d)


for x in range(190201, 190260 + 1):
    if len(f(x)) == 4:
        print(f(x)[-1], f(x)[-2])'''

# Номер 2574 Поляков
'''def f(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)

for x in range(...):
    if len(f(x)) == 3:
        print(f(x))'''

# Номер 2575 Поляков
'''def f(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)

for x in range(int(244143 ** 0.25), int(1367821 ** 0.25) + 1):
    if len(f(x)) == 2:
        print(x ** 2, x ** 3)'''

# Номер 2897 Поляков Простые числа
'''def f(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)

k = 0

for x in range(2358827, 2358891 + 1):
    if len(f(x)) == 2:
        k += 1
        print(k,x)'''

# Номер 3440 Поляков
'''def f(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d) 
summ = 0

for x in range(33333, 55555):
    summ = int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2]) + int(str(x)[3]) + int(str(x)[4])
    if len(f(x)) == 2 and summ > 35:
        print(x, summ)'''

# функция, которая опеделяет пстые числа
'''def p(x):
    
    
    return (x > 1) and all(x % 1 for i in range(2, int(x ** 0.5) +1))'''

# Номер 5957 Поляков

'''def f(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for x in range(1, 10**9+1):
    if len(f(x)) == 117 and (str(x)[:2] == str(x)[-2:]):
        print(f(x)[-2:])'''


# 5
'''from fnmatch import *

for x in range(0, 10 ** 9 + 1, 23):
    if fnmatch(str(x), '12345?7?8'):
        print(x, x // 23)'''


# 4
'''for i in range(1000000, 2000000 + 1):
    c = 0
    for x in range(int(i ** 0.5), 899, -1):
        if i % x == 0:
            if (abs(i / x - x) <= 100):
                c += 1
        if c > 2:
            print(i)
            break'''


# 2

'''for num in range(95632, 95650 + 1):
    delitel = []
    for d in range(1, int(num ** 0.5) + 1):
        if num % d == 0:
            if d % 2 != 0:
                delitel.append(d)
            if num // d != d and num // d % 2 != 0:
                delitel.append(num // d)
    if len(delitel) == 6:
        delitel.sort()
        print(delitel[0],
              delitel[1],
              delitel[2],
              delitel[3],
              delitel[4],
              delitel[5])'''''


# 3
'''import math

for i in range(123456789, 223456789):
    if int(math.sqrt(i)) ** 2 == i:
        a = []
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                a.append(j)
                b = i // j
                if j != b:
                    a.append(b)
        if len(a) == 3:
            a.sort()
            print(i, max(a))'''

# 1
'''def p(x):
    return (x > 1) and all(x % i for i in range(2, int(x ** 0.5) + 1))


k = 0
for i in range(245690, 245756 + 1):
    if p(i):
        k += 1
        print(k, i)'''