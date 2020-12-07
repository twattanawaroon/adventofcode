import sys
import random

def parse(strin):
    p1, r1 = strin.split('r=')
    p2 = (p1.split('<')[1]).split('>')[0]
    xx, yy, zz = map(int, p2.split(','))
    return xx, yy, zz, int(r1)

def inrangeof(x2, y2, z2):
    count = 0
    for i in range(len(a)):
        x1, y1, z1, r1 = a[i]
        if abs(x1-x2)+abs(y1-y2)+abs(z1-z2) <= r1:
            count += 1
    return count

def test(xx, yy, zz):
    global bestw, bestm
    w = inrangeof(xx, yy, zz)
    m = abs(xx)+abs(yy)+abs(zz)
    if bestw is None or bestw < w:
        bestw = w
        bestm = m
    elif bestw == w:
        if bestm > m:
            bestm = m

a = [parse(line.strip()) for line in sys.stdin]

global bestw, bestm
bestw = None
bestm = None
for i in range(len(a)):
    x, y, z, r = a[i]
    test(x-r, y, z)
    test(x+r, y, z)
    test(x, y-r, z)
    test(x, y+r, z)
    test(x, y, z-r)
    test(x, y, z+r)
    for j in range(20):
        p = random.randint(0, r)
        q = random.randint(0, r-p)
        v = r-p-q
        test(x-p, y-q, z-v)
        test(x-p, y-q, z+v)
        test(x-p, y+q, z-v)
        test(x-p, y+q, z+v)
        test(x+p, y-q, z-v)
        test(x+p, y-q, z+v)
        test(x+p, y+q, z-v)
        test(x+p, y+q, z+v)

print(bestw)
print(bestm)