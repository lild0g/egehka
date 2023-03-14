'''for x in range(25):
    for y in range(25):
        for z in range(25):
            s = '>' + '1' * 25 + '2' * 17 + '3' * 10
            while '1' in s or '2' in s or '3' in s:
                s = s.replace('>1', '22>3', 1)
                s = s.replace('>2', '2>', 1)
                s = s.replace('>3', '11>2', 1)
            if s.count('1') == 25 and s.count('2') ==  17 and s.count('3') == 10:
                print(x, y, z, )'''


s = '>' + '1' * 11 + '2' * 12 + '3' * 30
while '>1' in s or '>2' in s or '>3' in s:
    s = s.replace('>1', '22>', 1)
    s = s.replace('>2', '2>', 1)
    s = s.replace('>3', '1>', 1)
print(s.count('1') + s.count('2')*2 + s.count('3')*3)


