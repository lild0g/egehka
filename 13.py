# ДЕМО ЕГЭ 2024
from ipaddress import *

k = 0
net = ip_network('146.212.200.55/255.255.240.0', 0) # сначала ip адресс, потом маска
'''for ip in net:
    if bin(int(ip)).count('0') % 2 == 0:
        k += 1'''
print(net)


'''
from ipaddress import *

k = 0
for i in range(32):
    net = ip_network('71.192.0.12/' + str(i), 0)
    sub = str(net).split('/')
    print(net, sub)
    if sub[0] == '71.192.0.0':
        k += 1
print(k)
'''

from ipaddress import *
k = 0
net = ip_network('105.224.200.224/255.255.255.224', 0)
for ip in net:
    ip = list(map(int, str(ip).split('.')))
    ip2 = [bin(x)[2:] for x in ip]
    ip2 = ''.join(ip2)
    if ip2.count('1') % 4 == 0:
        k += 1
print(k)


