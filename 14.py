x = 5**36 + 5**24 - 25
k = 0
while x > 0:
    if x % 5 == 4:
        k += 1
    x //= 5
print(k)