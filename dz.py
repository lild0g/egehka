# функция делимость
'''def f(x, a):
    return (a % 3 == 0) and ((220 % x == 0) <= ((a % x != 0) <= (550 % x != 0)))


for a in range(1, 1001):
    if all(f(x, a) == 1 for x in range(1, 10000)):
        print(a)'''

# функция график
'''def f(x, y, a):
    return (x+y<=22) and (y<=x-6) and (y>=a)

for a in range(1, 1000):
    if all(f(x, y, a) == 1 for x in range(1, 1000) for y in range(1, 1000)):
        print(a)'''

# фунция коньюнкция
'''def f(x, a):
    return (x & 41 == 0) <= ((x & 119 != 0) <= (x & a != 0))

for a in range(1, 1000):
    if all(f(x, a) == 1 for x in range(1, 1000)):
        print(a)'''
