# Номер 224 Поляков

'''def f(n):
    if n == 1: return 1
    if n > 1 and n % 2 == 0: return n * n + f(n - 1)
    if n > 1 and n % 2 != 0: return f(n - 1) + 2 * f(n - 2)


print(f(23))'''

# Номер 226 Поляков
import sys

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

from sys import *
setrecursionlimit(10000)


def f(n):
    if n >= 2025: return n
    if n < 2025: return n + f(n + 2)


print(f(2022) - f(2023))

