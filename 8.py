#Борис составляет 6-буквенные коды из букв Б, О, Р, И, С.
#Буквы Б и Р нужно обязательно использовать ровно по одному разу, букву С можно использовать один раз или не использовать совсем,
#буквы О и И можно использовать произвольное количество раз или не использовать совсем.
#Сколько различных кодов может составить Борис?

'''from itertools import product
a = product('ABCDEFX', repeat=4)
k = 0
for i in a:
    s = ''.join(i)
    if s.count('X') == 1:
        k += 1
print(k)'''

# Номер 6926 Поляков
'''from itertools import *
k = 0
for i in product('чистыйразум', repeat = 5):
    s = ''.join(i)
    if s.count('й') <= 1:
        k += 1
print(k)'''

# Номер 6272
'''from itertools import *
k = 0
for j in range(2, 5):
    for i in permutations('ABCD', j)
        s = ''.join(i)
print(k)'''

# номер 5758
'''from itertools import *
x = []
for i in product('антиуопя', repeat = 16):
    a = ''.join(i)
    if 'антиутопия' in a:
        if'''

'''from itertools import *
c = 0
a = []
for i in range(1,6):
    for j in combinations_with_replacement('ЯУОИА', i):
        s1 = ''.join(j)
        a.append(s1)
b = []
for k in range(1, 6):
    for c in combinations_with_replacement('НПТ', k):
        s2 = ''.join(c)
        b.append(s2)
for i in range(len(a)):
    for j in range(len(a)):
        if len(str(a[i])) + len(str(b[j])) == 6:
            c += 1
            print(c)'''

'''from itertools import *
a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
k = 0
for a in product('0123456789ABCDE', repeat = 5):
    x = ''.join(a)
    if (int(x[0], 15) % 2 == 0 and int(x[1], 15) % 3 == 0 and int(x[2], 15) % 2 == 0 and int(x[3], 15) % 3 == 0 and int(x[4], 15) % 2 == 0) or int(x[0], 15) % 3 == 0 and int(x[1], 15) % 2 == 0 and int(x[2], 15) % 3 == 0 and int(x[3], 15) % 2 == 0 and int(x[4], 15) % 3 == 0:
        k += 1

print(k)'''

# Анализ списка заданной длины Поляков

# № 6918
from itertools import *
k = 0
for a in product('ШТСМКИЕВА', repeat = 5):
    sogl = ['Т', 'М', 'Ш', 'В', 'С', 'К']
    glas = ['И', 'А', 'Е']
    x = ''.join(a)
    k += 1
    if (x[0] and x[4] in glas) and (x[1] and x[3] in glas) and x[2] in sogl:
        print(k)


