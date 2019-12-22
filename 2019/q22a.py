import sys

def cut(b, off):
    if off < 0:
        off += 10007
    return b[off:] + b[:off]

def shuf(b, off):
    c = [None] * 10007
    for i in range(10007):
        c[(i*off)%10007] = b[i]
    return c

a = list(range(10007))
for line in sys.stdin:
    x = line.strip().split()
    if x[0] == 'cut':
        a = cut(a, int(x[1]))
    elif x[1] == 'into':
        a = a[::-1]
    elif x[1] == 'with':
        a = shuf(a, int(x[3]))
print(a.index(2019))