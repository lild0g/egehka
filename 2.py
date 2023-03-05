# ((x → y) ≡ (y → z)) ∧ (y ∨ w)
# ((x → y ) ≡ (z → w)) ∨ (x ∧ w).

print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(not(x <= y) or (y == z) or y):
                    print(x, y, z, w)

print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(not(x <= w) or (y == z) or y):
                    print(x, y, z, w)

'''
# ¬(x → w) ∨ (y ≡ z) ∨ yA
from itertools import *

def f(x, y, z, w):
    return not(x <= y) or (y == z) or y


for a in product([0, 1], repeat=7):
    table = [(a[0], 1, a[1], 0),
             (a[2], 0, 1, a[3]),
             (a[4], a[5], 0, a[6])]
    if len(table)== len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r)))for r in table]==[0, 0, 0]:
                print(p)'''