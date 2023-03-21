'''for x in range(25):
    for y in range(25):
        for z in range(25):
            s = '>' + '1' * 25 + '2' * 17 + '3' * 10
            while '1' in s or '2' in s or '3' in s:
                s = s.replace('>1', '22>3', 1)
                s = s.replace('>2', '2>', 1)
                s = s.replace('>3', '11>2', 1)
            if s.count('1') == 25 and s.count('2') ==  17 and s.count('3') == 10:
                print(x, y, z, )'''


# s = '>' + '1' * 11 + '2' * 12 + '3' * 30
# while '>1' in s or '>2' in s or '>3' in s:
#     s = s.replace('>1', '22>', 1)
#     s = s.replace('>2', '2>', 1)
#     s = s.replace('>3', '1>', 1)
# print(s.count('1') + s.count('2')*2 + s.count('3')*3)

# s1 = sum(list(map(int, s))) - считает сумму цифр в строке

'''def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % 1 == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)   '''
# Статград
'''for x in range(20):
    for y in range(20):
        for z in range(20):
            s = '0' + '1' * x + '2' * y + '3' * z + '0'
            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            if s.count('1') == 56 and s.count('2') == 44 and s.count('3') == 19:
                print(x + y + z + 2)'''


for x in range(50):
    s = '0' + '1' * x + '2' * x + '0'
    while '00' not in s:
        s = s.replace('011', '20', 1)
        s = s.replace('022', '10', 1)
        s = s.replace('01', '220', 1)
        s = s.replace('02', '110', 1)
        if s.count('1') == 40 and s.count('2') > 50:
            print(s.count('2'))









