import sys
import math

def gcd(vp, vq):
    if vp < vq:
        wp, wq = vq, vp
    else:
        wp, wq = vp, vq
    while wq > 0:
        wr = wp % wq
        wp = wq
        wq = wr
    return wp

def find_typ(p, q):
    px, py = p
    qx, qy = q
    dx = qx - px
    dy = qy - py
    r = gcd(abs(dx), abs(dy))
    if r == 0:
        return (0, 0)
    return (dx//r, dy//r)

def dist(p, q):
    px, py = p
    qx, qy = q
    dx = qx - px
    dy = qy - py
    return dx**2 + dy**2

a = []
i = 0
for line in sys.stdin:
    x = line.strip()
    for j in range(len(x)):
        if x[j] == '#':
            a.append((i, j))
    i += 1
best = 0
besti = None
for i in range(len(a)):
    p = a[i]
    s = set()
    for j in range(len(a)):
        q = a[j]
        typ = find_typ(p, q)
        if typ != (0, 0):
            s.add(typ)
    if best < len(s):
        best = len(s)
        besti = i
print(a[besti])
m = dict()
for j in range(len(a)):
    if j == besti:
        continue
    typ = find_typ(a[besti], a[j])
    if typ not in m:
        m[typ] = []
    m[typ].append(a[j])
k = list(m)
k.sort(key=lambda x:-math.atan2(x[1],x[0]))
for t in k:
    m[t].sort(key=lambda x: dist(a[besti], x))
v = []
still = True
while still:
    still = False
    for t in k:
        if len(m[t]) > 0:
            v.append(m[t].pop(0))
            still = True
f = v[199]
print(f[1]*100+f[0])
