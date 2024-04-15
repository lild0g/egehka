'''s = open('zadanie24_1 (1)').redline()
s = s.replace('8', ' ').replace('C', ' ')
s = s.split()
print(len(max(s, key = len)))'''

'''s = open('zadanie24_2.txt').readline()
k = 1
m = 0
for i in range(len(s)):
    if s[i] != s[i-1] != ' ':
       k += 1
    else:
        m = max(k,m)
        k = 1
m = max(k,m)
print(m)'''

'''s = open('24.txt').readline()
m = 0
k = 1
for i in range(1, len(s)):
    if (s[i] == 'K' and s[i - 1] == 'L') or (s[i] == 'L' and s[i - 1] == 'K'):
        k = 1
    else:
        k += 1
        if k > m:
            m = k
print(m)'''


'''s = open('24_demo.txt').readline()
s = s.replace('X', ' ').replace('Y', ' ')
s = s.split()
print(len(max(s, key = len)))'''#1

'''2s = open('zadanie24_1.txt').readline()
a = 'AB'*12
print(len(a))'''#2

'''import string
al = string.ascii.uppercase
s = open('24.txt').readline()

for i in al:
    print(i, s.count(f'A{i}'))'''#3

'''s = open('24.txt').readline()



'''#4

'''s = open('24 (2).txt').readline()
while 'XZZY' in s:
    s = s.replace('XZZY', 'XZZ ZZY')
print(max(len(c) for c in s.split()))'''#5

'''s = open('24.txt').readline()
s = s.replace('KL', 'K L').replace('LK', 'L K')
print(max(len(c) for  c in s.split()))'''#6

'''s = open('24.txt').readline()

'''#7

'''s = open('24.txt').readline()
s = s.replace('O', 'A').replace('D', 'C').replace('F', 'C')
s = s.replace('CCA', '*').replace('A', ' ').replace('C', ' ')
print(max(len(c) for c in s.split()))''' #8


# досрок с КЕГЭ
s = open('24_15339.txt').readline()
k = 0
for a i