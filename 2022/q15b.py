import sys
import codelib as cl

def dist(ax, ay, bx, by):
    return abs(ax-bx)+abs(ay-by)
ansf = 0

MINV = 0
MAXV = 4000000
def overlap(ax, bx):
    if bx < MINV or ax > MAXV+1:
        return 0
    return min(bx, MAXV+1)-max(ax, MINV)

z = []
for line in sys.stdin:
    s = line.strip().split()
    ax = int(s[2][2:-1])
    ay = int(s[3][2:-1])
    bx = int(s[8][2:-1])
    by = int(s[9][2:])
    z.append((ax, ay, bx, by))

for py in range(MINV, MAXV+1):
    r = []
    for ax, ay, bx, by in z:
        d = dist(ax, ay, bx, by)-abs(ay-py)
        if d >= 0:
            r.append((ax-d, 1))
            r.append((ax+d+1, -1))
    r.sort()
    
    ans = 0
    pos = -100000000
    val = 0
    for item, d in r:
        if val > 0:
            ans += overlap(pos, item)
        else:
            px = pos
        val += d
        pos = item
    if ans < MAXV+1:
        ansf = px*MAXV+py
        break

print(ansf)
