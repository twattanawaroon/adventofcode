import sys

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

a = []
i = 0
for line in sys.stdin:
    x = line.strip()
    for j in range(len(x)):
        if x[j] == '#':
            a.append((i, j))
    i += 1
best = 0
bestp = None
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
        bestp = p
print(best)