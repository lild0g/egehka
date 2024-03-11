# функция делимость
'''def f(x,a):
    return (a % 3 == 0) and ((220 % x == 0) <= ((a % x != 0) <= (550 % x != 0)))

for a in range(1, 1001):
    if all(f(x, a) == 1 for x in range(1, 10000)):
        print(a)'''

# функция график
'''def f(x, y, a):
    return ((x - 2y) < 3a) or (2y > x) or (3x > 50) #выражение в ()

for a in range(1, 1000):
    if all(f(x, y, a) == 1 for x in range(1, 1000) for y in range(1, 1000)):
        print(a)'''

# фунция коньюнкция
'''def f(x, a):
    return (x & 107 == 0) <= ((x & 55 != 0) <= (x & a != 0))

for a in range(1, 1000):
    if all(f(x, a) == 1 for x in range(1, 1000)):
        print(a)'''

# 2 типа задач:
# наибольшее что-то( множество, сумма, произведение...
# наименьшее что-то( множеств, сумма, произведение...
# сумма, произведение ... меньше всего в самом меньшем множестве, и наоборот

# Amin
# 1) задаём пустое множество А
# 2) добавляем в А значения х, которые обращают функцию в ноль

# Amax
# 1) задаём большое множество А
# 2) исключить из А значения х, которые обращают функцию в ноль

# Задача
# Задаём множества, которые даны в условии
# Написать функцию логического выражения
# Перебор значений х
# Вывод А

# ЗАДАЧА №4881
'''p = {1, 12}
q = {12, 13, 14, 15, 16}
a = set()


def f(x):
    return (x not in a) <= ((x not in p) and (x not in q))


for x in range(1, 1000):
    if f(x) == 0:
        a.add(x)
print(a)'''

# ЗАДАЧА №4872

'''p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
a = {i for i in range(1, 1000)}


def f(x):
    return (((x in a) <= (x in p)) and ((x in q) <= (x not in a)))


for x in range(1, 1000):
    if f(x) == 0:
        a.remove(x)
print(len(a))'''

# ОТРЕЗКИ

'''def f(x, a1, a2):
    return (a1 <= x <= a2) <= (430 <= x <= 490) or (440 <= x <= 530)

m = 0
for a1 in range(400, 600):
    for a2 in range(a1 + 1, 600):
        if all(f(x, a1, a2) == 1 for x in range(400, 600)):
            m = max(m, a2 - a1)

print(m//10)'''


'''def f(x, a1, a2):
    return (a1 <= x <= a2) <= (150 <= x <= 390) or (440 <= x <= 570)

m = 0
for a1 in range(100, 600):
    for a2 in range(a1 + 1, 600):
        if all(f(x, a1, a2) == 1 for x in range(100, 600)):
            m = max(m, a2 - a1)

print(m//10)'''


'''def f(x,a1,a2):
    return (((150 <= x <= 390) <= (a1 <= x < a2)) and ((440 <= x <= 570) <= ( a1 <= x <= a2)))

m = 10**5
for a1 in range(100, 600):
    for a2 in range(a1 + 1, 600):
        if all(f(x, a1, a2) == 1 for x in range(100, 600)):
            m = min(m, a2 - a1)
print(m//10)'''


'''def f(x,a1,a2):
    return (not(a1 <= x <= a2) <= (not(250 <= x <= 500))) <= ((a1 <= x <= a2) <= (320 <= x <= 470))

m = 0
for a1 in range(200, 600):
    for a2 in range(a1 + 1, 600):
        if all(f(x, a1, a2) == 1 for x in range(200, 600)):
            m = max(m, a2 - a1)
print(m//10)'''


'''def f(x, y, a):
    return (x + 2 * y < a) or (y > x) or (x > 60) #выражение в ()

for a in range(1, 1000):
    if all(f(x, y, a) == 1 for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break'''

# 22 Поляков
'''def f(x, A):
    return ((x & 25) != 0) <= (((x & 17) == 0) <= ((x & A) != 0))

for A in range(0, 1000):
    if all(f(x, A) == 1 for x in range(0, 1000)):
        print(A)
        break'''

# 370 Поляков
'''def f(x,a):
    return (x % a != 0) <= ((x % 6 == 0) <= (x % 4 != 0))

for a in range(1, 1000):
    if all(f(x, a) == 1 for x in range(1, 1000)):
        print(a)'''


# 7267 Поляков
'''def f(x, y, a):
    return (4 * x + y > 115) or (x > 3 * y) or (x + 4 * y < a)


for a in range(0, 500):
    if any(f(x, y, a) == 0 for x in range(0, 1000) for y in range(0, 1000)):
        print(a)'''


# 6222 Поляков
'''def f(x, y, a):
    return (((x+y) - 73) <= 0) or ((37 - (x-y)) <= 0) or ((y - a) > 0)


for a in range(0, 1000):
    if all(f(x, y, a) == 1 for x in range(0, 1000) for y in range(0, 1000)):
        print(a)'''


# 5921 Поляков
'''def f(x, y, a):
    return (x + a >= 160) or ((x % 7 == 0) <= (x - 17 <= 0))


for a in range(0, 1000):
    if all(f(x, y, a) == 1 for x in range(0, 1000) for y in range(0, 1000)):
        print(a)'''


# 5920 Поляков
'''def f(x, y, z, a):
    return ((z % 115 == 0) or (y % 78 == 0) or (x % 51 == 0)) <= (x * y * z % a == 0)


for a in range(1, 500):
    if all(f(x, y, z, a) == 1 for x in range(1, 500) for y in range(1, 500) for z in range(1, 500)):
        print(a)'''


'''def f(a, x):
    return ((37 + a + x + 45) == 180) == ((a + 90 == 180) and not (a + 23 < 120))


for a in range(1, 181):
    if all(f(a, x) == 1 for x in range(1, 1000)):
        print(a)'''


'''def f(x, y, z, a):
    return (x | 50 == x) or (y & 34 != 0) or (z | 24 != 24) or (x * y * z > (a // 8))


for a in range(1, 100):
    if all(f(x, y, z, a) == 1 for x in range(1, 100) for y in range(1, 100) for z in range(1, 100)):
        print(a)'''
