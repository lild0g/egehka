# 19 задание с одной кучей
'''def f(s, c, m):
    if s >= 129:
        return c % 2 == m % 2
    if c == m:
        return 0
    h = [f(s + 1, c + 1, m + 1), f(s * 2, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1, 128 + 1):
    for m in range(1, 4 + 1):
        if f(s, 0, m) == 1:
            print(s, m)'''


# 19 задание с двумя кучами

'''def f(s1, s2, c, m):
    if (s1 + s2) >= 77:
        return c % 2 == m % 2
    if c == m:
        return 0
    h = [f(s1 + 1, s2, c + 1, m), f(s1 * 2, s2, c + 1, m), f(s1, s2 + 1, c + 1, m), f(s1, s2 * 2, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else any(h)  # при любом ходе Пети all()
    # при неудачном ходе Пети any()


for s2 in range(1, 69 + 1):
    for m in range(1, 4 + 1):
        if f(7, s2, 0, m) == 1:
            print(s2, m)'''



