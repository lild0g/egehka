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