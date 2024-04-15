'''
from turtle import *
color('black', 'red')
speed(100)
m = 100
begin_fill()
left(90)
for i in range(4):
    forward(10 * m)
    right(90)
end_fill()
canvas = getcanvas()
cnt = 0
for y in range(-100 * m, 100 * m, m):
    for x in range(-100 * m, 100 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            cnt += 1
print(cnt)
done()
exit()
'''

'''
count = 0
for x in range(1, 9):
    for y in range(1, 9):
        if -x / 3 ** 0.5 + 9 > y > x / 3 ** 0.5:
            count += 1
print(count)
'''  # треугольник

'''
count = 0
for x in range(1, 8):
    for y in range(1, 8):
        if (y < x / 3 ** 0.5) or (y > -x / 3 ** 0.5 + 12):
            count += 1
print(count)
'''  # треугольник с двумя условиями

from turtle import *
left(90) # поворачивваем голову черепахи на 90 градусов
k = 20
speed(100)
for i in range(2):
    forward(13 * k)
    right(90)
    forward(18 * k)
    right(90)
up()
forward(5 * k)
right(90)
forward(9 * k)
left(90)
down()
for i in range(2):
    forward(11 * k)
    right(90)
    forward(7 * k)
    right(90)
up() # надо поднять хвост в конце всегно алгоритма

for x in range(-1 * k, 25 * k, k):
    for y in range(-1 * k, 25 * k, k):
        goto(x, y)
        dot(3, 'red')
done()



