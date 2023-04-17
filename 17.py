# Номер 4612 Поляков

# 1 СПОСОБ

'''a = [int(x) for x in open('17-4.txt')]
k = 0
m = 10001
for i in a:
    if i % 3 == i % 5 and (i % 31 == 0 or i % 47 == 0 or i % 53 == 0):
        k += 1
        m = min(m, i)
    print(k, m)'''

# 2 СПОСОБ

'''a = [int(x) for x in open('17-4.txt')]
k = 0
m = 10001
for i in range(len(a)):
    if (a[i] % 3 == a[i] % 5) and (a[i] % 31 == 0 or a[i] % 47 == 0 or a[i] % 53 == 0):
        k += 1
        m = min(m, i)
    print(k, m)'''

# 3 СПОСОБ

'''a = [int(x) for x in open('17-4.txt')]
ans = []
for i in range(len(a)):
    if (a[i] % 3 == a[i] % 5) and (a[i] % 31 == 0 or a[i] % 47 == 0 or a[i] % 53 == 0):
        ans.append(a[i])
    print(len(ans), min(ans))'''

# Номер 4316 Поляков

'''a = [int(x) for x in open('17-4.txt')]
ans = []
for i in a:
    s = sum(list(map(int, str(i))))
    if (s % 5 == 0) and (i % 3**2 != 0):
        ans.apppend(i)
    print(len(ans), max(ans))'''

# Номер 4311 Поляков

'''a = [int(x) for x in open('17-4.txt')]
k = 0
m = -10001
for i in range(len(a)):
    if a[i] % 13 == 4 and a[i] % 8 == 1:
        k += 1
        m = max(m, i)
    print(k, m)'''