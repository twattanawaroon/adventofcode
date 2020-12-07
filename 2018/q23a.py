import sys

def parse(strin):
    p1, r1 = strin.split('r=')
    p2 = (p1.split('<')[1]).split('>')[0]
    xx, yy, zz = map(int, p2.split(','))
    return xx, yy, zz, int(r1)

a = [parse(line.strip()) for line in sys.stdin]
bestr = None
besti = None
for i in range(len(a)):
    if bestr is None or a[i][3] > bestr:
        bestr = a[i][3]
        besti = i
count = 0
for i in range(len(a)):
    x1, y1, z1, r1 = a[i]
    x2, y2, z2, r2 = a[besti]
    if abs(x1-x2)+abs(y1-y2)+abs(z1-z2) <= r2:
        count += 1

print(count)