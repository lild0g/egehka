a = [int(x) for x in open('26_5228.txt')][1:]
a = sorted(a, reverse = True)
b = int(a[0])
k = 1
for i in range(1, len(a)):
    if b - a[i] >= 8:
        b = a[i]
        k += 1
print(k, b)

