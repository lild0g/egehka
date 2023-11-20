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
from itertools import *
x = []
for i in product('антитопия', repeat = 16):
    a = ''.join(i)
    if 'антиутопия' in a:
        if
