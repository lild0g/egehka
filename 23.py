# Номер 26 Поляков
'''def f(c, e):
    if c > e or c == 12: return 0
    if c == e: return 1
    if c < e: return f(c + 1, e) + f(c + 3, e)


print(f(1, 10) * f(10, 15))'''

'''def f(x, y):
    if x > y or x == 12:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 3, y)
print(f(1, 10) * f(10, 15))'''

# 1. Прибавить 1
# 2. Прибавить 3
# Первая команда увеличивает число на экране на 1, вторая— на 3.
# Программа для исполнителя Увеличитель— это последовательность команд.
# Сколько существует программ, для которых при исходном числе 1 результатом является число 15 и при этом траектория вычислений содержит число 10 и не содержит число 12?