# номер 48448 РЕШУ ЕГЭ
f = open('27-B.txt')
n = int(f.readline())
k = [0] * 3
for x in range(n):
    x = int(f.readline())
    ost = x % 3
    k[ost] += 1
