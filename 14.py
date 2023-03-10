# ТИП 1:
# Значение выражения 5**36 + 5**24 - 25
# записали в системе счисления с основанием 5.
# Сколько цифр 4 содержится в этой записи?

'''x = 9**8 + 3**8 - 2
k = 0
while x > 0:
    if x % 3 == 2:
        k += 1
    x //= 3
print(k)'''


# ТИП 2
# Операнды арифметического выражения записаны в системе счисления с основанием 16:
# 8x84x(16(CC)) + 78x34((16(CC))
# В записи чисел переменной X обозначена неизвестная цифра из алфавита шестнадцатеричной системы счисления.
# Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 23.
# Для найденного значения x вычислите частное от деления значения арифметического выражения на 23
# укажите его в ответе в десятичной системе счисления. Основание системы счисления в ответе указывать не нужно.

'''for x in '0123456789ABCDEF':
    a = int('8' + x + '84' + x, 16) + int('78' + x + '34', 16)
    if a % 23 == 0:
        print(a // 23)
        break'''

# ТИП 2.1
# Операнды арифметического выражения записаны в системе счисления с основаниями 16 и 14:
# 3D4x(16(CC)) + 4xC4(14(CC))

'''for x in '0123456789ABCD':
    t = int('3D4' + x + '', 16) + int('4' + x + 'C4', 14)
    if t % 154 == 0:
        print(t // 154)
        break'''




'''
x = 5 ** 36 + 5 ** 24 - 25
s = ''
while x != 0:
    s += str(x % 5)
    x //= 5
s = s[::-1]
print(s.count("4"))
'''  # прямое сложение


'''result = []
for x in '0123456789ABC':
    for y in '0123456789ABC':
        t = int('8' + x + '78' + y, 13) + int('79' + x + y + '7', 18)
        if t % 9 == 0:
            result.append(t)
if result:
    print(min(result) // 9)
'''  # операции с двумя переменными 2y66x9 + x0y112

'''
for x in '0123456789AB':
    t = int('2AB' + x + '', 12) + int('' + x + '8E', 17)
    if t % 27 == 0:
        print(t // 27)
        break
'''  # операции с одной переменной 2ABx12 + x8E17

'''
for x in '0123456789A':
    t = int('982' + x + '8', 11) + int('194' + x + '7', 11)
    if t % 58 == 0:
        print(t // 58)
        exit
'''  # операции в одной СС 982x811 + 194x711

'''
for A in range(1, 1000):
    for x in '0123456789AB':
        M = int('49' + x + '26', 12)
        N = int('49' + x + '70', 12)
        if (M + A) % N == 0:
            print(A)
            break'''