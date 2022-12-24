for i in range(1,100):
    n = str(bin(i))[2:]
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    if int(n, 2) > 43:
        print(i,n)
        break