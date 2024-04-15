# Номер 224 Поляков

'''def f(n):
    if n <= 1: return 1
    if n > 1 and n % 2 == 0: return n * n + f(n - 1)
    if n > 1 and n % 2 != 0: return f(n - 1) + 2 * f(n - 2)

print(f(23))'''

'''def F(n):
    if n <= 2:return n + 1
    if n > 2:return F(n - 1) * F(n - 2)
print(F(4))'''

#F(n) = n + 1 при n ≤ 2;
#F(n) = F(n − 1) × F(n − 2) при n > 2.

# Номер 226 Поляков

'''def f(n):
    if n == 1: return 1
    if n >= 2: return f(n - 1) - 2 * g(n - 1)


def g(n):
    if n == 1: return 1
    if n >= 2: return f(n - 1) + 2 * g(n - 1)


print(g(21))'''

# Демоверсия ЕГЭ 2023 / 5537 Поляков

'''from sys import *  # вызывает функцию sys
setrecursionlimit(10000)  # увеличивает колличество вызовов рекурсии



def f(n):
    if n == 1: return 1
    if n > 1: return n * f(n - 1)


print(f(2023) / f(2020))'''

# Досрок

'''from sys import *
setrecursionlimit(10000)


def f(n):
    if n >= 2025: return n
    if n < 2025: return n + f(n + 2)


print(f(2022) - f(2023))'''

'''from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1: return 1
    if n > 1: return n * f(n - 1)


for n in range(2, 3000):
    f(n)


print(f(2023)//f(2020))'''

# Номер 2265

'''def f(n):
    if n <= 3: return n
    if 3 < n <= 32: return n // 4 + f(n - 3)
    if n > 32: return 2 * f(n - 5)


print(f(100))'''

# Номер 2278
'''k = 0
def f(n):
    if n > 25: return 2 * n * n * n + 1
    if n <= 25: return f(n + 2) + 2 * f(n + 3)


for n in range(1, 1001):
    if f(n) % 11 == 0:
        k += 1
print(k)'''

# Номер 3110

'''def f(n):
    if n == 1: return 2
    if n > 1: return f(n - 1) + 5 * n ** 2


print(f(39))'''

# Номер 3691

'''def f(n):
    if n <= 1: return 1
    if n > 1 and n % 2 == 0: return 3 + f((n / 2) - 1)
    if n > 1 and n % 2 != 0: return n + f(n + 2)
n = 2
while n < 1000:
    try:
        r = f(n)
        if r == 19:
            print(n)
            break
    except:
        pass
    n += 1'''

from sys import *  # вызывает функцию sys
setrecursionlimit(10000)

def F(n):
    if n <= 7: return 1
    if n > 7: return n + 2 + F(n - 1)
print(F(2024) - F(2020))