'''s = open('zadanie24_1 (1)').redline()
s = s.replace('8', ' ').replace('C', ' ')
s = s.split()
print(len(max(s, key = len)))'''

s = open('zadanie24_2.txt').readline()
k = 1
m = 0
for i in range(len(s)):
    if s[i] != s[i-1] != ' ':
       k += 1
    else:
        m = max(k,m)
        k = 1
m = max(k,m)
print(m)



