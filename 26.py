'''a = [int(x) for x in open('26_5228.txt')][1:]
a = sorted(a, reverse = True)
b = int(a[0])
k = 1
for i in range(1, len(a)):
    if b - a[i] >= 8:
        b = a[i]
        k += 1
print(k, b)'''
c = 0
f = open('26_2686 (1).txt')
k = int(f.readline())
a = sorted([list(map(int, x.split())) for x in f])
for i in range(k - 1):
    if a[i][0] == a[i + 1][0] and a[i][1] + 1 == a[i + 1][1]:
        c += 1
        if c >= 5:
            print(a[i][0], a[i][1] + 1)
    else:
        c = 0





