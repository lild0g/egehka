'''a = [int(x) for x in open('26_5228.txt')][1:]
a = sorted(a, reverse = True)
b = int(a[0])
k = 1
for i in range(1, len(a)):
    if b - a[i] >= 8:
        b = a[i]
        k += 1
print(k, b)'''

'''ans = [0, 0]
f = open('26.txt')
k = int(f.readline())
a = sorted([list(map(int, x.split())) for x in f])
for i in range(k - 1):
    if a[i][0] == a[i + 1][0] and a[i][1] + 3 == a[i + 1][1]:
        r = a[i][0]
        p = a[i][1] + 1
        if r > ans[0]:
            ans[0] = r
            ans[1] = p

print(ans)'''

'''ans = []
a = [int(x) for x in open('26.txt')]
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] % 2 == 0 and a[j] % 2 == 0:
            sr = (a[i] + a[j]) // 2
            if sr in a:
                ans.append(sr)
print(len(ans), max(ans))'''

# КЕГЭ №12933
'''f = open('26_12933.txt')
n, k = [int(x) for x in f.readline().split()] # прочитали и разредали, получили 2 строчки состоящие из цифр
a = []
for i in range(1, n + 1): # n - кол-во иттераций; перебором захватываем всё
    ts, to = [int(x) for x in f.readline().split()] # ts - время шлифовки, to - время окрашивания
    a.append((ts, i, 's')) # делаем картежи s - шлифовка, o - окрашивание
    a.append((to, i, 'o'))
a.sort() # время по возврастанию
lenta = [0] * (n + 1) # метод для выведения по номеру места, создание ленты
ks = 0 # кол-во отшлифованных деталей
spo = set() # создаём множество окрашнных деталей
start, end = 1, n # start - первое место на ленте, end - последнее место на ленте
for t, id, op in a: # t - время , id - айди, op - операция
    if id not in spo: # проверили есть ли деталь
        spo.add(id) # добавляет окрашенные детали
        if op == 's': # если деталь для шлифовки
            lenta[start] = id # ставим этот элемент в начало ленты
            start += 1
            ks += 1
        else: # если деталь для окрашивания
            lenta[end] = id # ставим этот элемент в конец ленты
            end -= 1 # -= потому что идём с конца
print(ks, lenta[k])'''

# КЕГЭ №13101
'''f = open('26_13101.txt')
n = int(f.readline())
a = []
for i in f:
    st, t, o = [int(x) for x in i.split()] # st - начало время обслуживания, t - время обслуживания, o - окно
    a.append((st, t, o)) # создаём картеж
a.sort()
okno1 = [] # первая очередь
okno2 = [] # вторая очередь
kn = 0 # счёчтик обслуживаемых
k2 = 0
for st, t, o in a:
    okno1 = [x for x in okno1 if x > st]
    okno2 = [x for x in okno2 if x > st]
    if o == 1 or (o == 0 and len(okno1) <= len(okno2)):
        if len(okno1) >= 14:
            kn += 1
            continue
        if len(okno1) == 0:
            okno1 += [st + t]
        else:
            okno1 += [max(okno1) + t]
    else:
        if len(okno2) >= 14:
            kn += 1
            continue
        k2 += 1
        if len(okno2) == 0:
            okno2 += [st + t]
        else:
            okno2 += [max(okno2) + t]
print(k2, kn)'''

# КЕГЭ 12478
'''f = open('26_12478.txt')
n, start, finish = [int(x) for x in f.readline().split()]
a = []
for i in f:
    s, e = [int(x) for x in f.readline().split()]
    a.append([s, e])
a.sort()'''

# КЕГЭ 11605
'''f = open('26_11605.txt')
n = [int(x) for x in f.readline().split()]
a = []
k = []
for i in f:
    s, e = [int(x) for x in f.readline().split()]
    a.append((s, e))
a.sort()
for i in range(len(a) - 1):
    if a[i][1] == 10000:
        k.append(a[i])
print(len(a))'''

# номер 8512 Кабанов
'''f = open('26_8512.txt')
k = int(f.readline())
n = int(f.readline())
a = []
for s in f:
    st, end = [int(x) for x in s.split()]
    a.append([st, end])
a.sort()
b = [0] * k  # номер +1
count = 0  # обслуженные пассажиры
last_s = 0  # текущий последний багаж начало
last_end = 0  # минимальный номер текущей последней ячейки
for i in a:
    s = i[0]
    e = i[1]
    for j in range(k):
        if b[j] <= s:
            b[j] = e + 1
            count += 1
            if s > last_s:
                last_s = s
                last_end = j + 1
            break
print(count, last_end)'''

# номер 6406 Поляков
'''f = open('26-119.txt')
n, l, m = [int(x) for x in f.readline().split()]
a = []
for s in f:
    st, t, typ = [x for x in s.split()]
    end = int(st) + int(t)
    a.append([int(st), end, typ])
a.sort()
k_A = 0
k_B = 0
park = [0] * (l + m)  # места для автомобилей  0...l - 1 места; места для микроавтобусов l...l + m - 1
for i in a:
    st, t, typ = i[0], i[1], i[2]
    if typ == 'A':
        for j in range(l + m):
            if park[j] <= st:
                park[j] = t
                k_A += 1
                break
    if typ == 'B':
        for j in range(l, l + m):
            if park[j] <= st:
                park[j] = t
                k_B += 1
                break
print(k_B, n - k_A - k_B)'''
