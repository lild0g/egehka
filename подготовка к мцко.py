# 1011,01(2) + 24,6(8)

'''print(hex(int(int('1011', 2) + 0.25 + int('24', 8) + 6 * 8.125)))
print(hex(32))''' # ответ: 20


# №2

'''def f(a, b, c):
    return a or not b and c


for a in range(2):
    for b in range(2):
        for c in range(2):
            print(a, b, c, int(f(a, b, c)))''' # ответ:


# №3 - руками, ответ: 27


# №4,  ответ:

'''for i in range(1, 1000):
    n = str(bin(i))[2:]  
    if n % 2 == 0:
        n += '10'
    else:
        n += '11'
    if n.count('1') % 2 == 0:
        n += n[-1]
    else:
        n += n[-2]
    r = int(n, 2) 
    if r > 44:
        print(r)
        break'''


# №5, ответ:

# №6 - руками, ответ: 1024

# №7 - круги Эйлера, ответ: 140

# №8, ответ:

'''p = 5
q = 7
e = 11
for d in range(40):
    f = (p - 1) * (q - 1)
    if (d * e) % f == 1:
        print(d)'''

# №9 - руками, ответ: 57

# №10

'''print((~18 | (132 >= 2)) & (86 <= 1))'''

# №11 - ответ: 231
'''def f(c, e):
    if c > e or c == 32: return 0
    if c == e: return 1
    if c < e: return f(c + 3, e) + f(c + 4, e) + f(c * 3, e)


print(f(4, 16) * f(16, 46))'''

# №12 - ответ: 15

'''k = 0
for i in range(0, 100, 2):
    s = i
    n = 120
    while s > 0:
        s = s // 6
        n = n - 6
    if n == 108:
        k += 1
print(k)'''

# №13 - ответ 77 -1944
'''ans = []
a = [int(x) for x in open('13.txt')]
for i in range(len(a)):
    if a[i] % 8 == 0 and a[i + 1] % 8 == 0:
       ans.append(a[i] + a[i + 1])
print(len(ans), min(ans))'''
