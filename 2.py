# ((x → y) ≡ (y → z)) ∧ (y ∨ w)


print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x or not(z)) and (x == (not(w))) and (x <= y)) == 1:
                    print(x, y, z, w)
