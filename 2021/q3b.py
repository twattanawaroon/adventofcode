import sys

def ff(y, crit):
    if len(y) == 1:
        num, onum = y[0]
        return int(onum, 2)
    f = []
    for num, onum in y:
        f.append(num[0])
    a0 = f.count('0')
    a1 = f.count('1')
    if crit:
        maj = '0' if a0 > a1 else '1'
    else:
        maj = '1' if a0 > a1 else '0'
    yy = []
    for num, onum in y:
        if num[0] == maj:
            yy.append((num[1:], onum))
    return ff(yy, crit)

x = []
for line in sys.stdin:
    n = line.strip()
    x.append((n, n))
a0 = ff(x, True)
a1 = ff(x, False)

print(a0*a1)