import sys
import codelib as cl

def dist(ax, ay, bx, by):
    return abs(ax-bx)+abs(ay-by)
ansf = 0

r = []
MY = 2000000
for line in sys.stdin:
    s = line.strip().split()
    ax = int(s[2][2:-1])
    ay = int(s[3][2:-1])
    bx = int(s[8][2:-1])
    by = int(s[9][2:])
    d = dist(ax, ay, bx, by)-abs(ay-MY)
    if d >= 0:
        r.append((ax-d, 1))
        r.append((ax+d+1, -1))
r.sort()
pos = -100000000
val = 0
for item, d in r:
    if val > 0:
        ansf += item-pos
    val += d
    pos = item

print(ansf)
#need to handle beacon offbyone