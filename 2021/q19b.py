import sys
import codelib as cl

verts = [
    (lambda q: (q[0],q[1],q[2])),
    (lambda q: (q[0],-q[1],-q[2])),
    (lambda q: (-q[0],q[1],-q[2])),
    (lambda q: (-q[0],-q[1],q[2])),
    (lambda q: (q[0],q[2],-q[1])),
    (lambda q: (q[0],-q[2],q[1])),
    (lambda q: (-q[0],q[2],q[1])),
    (lambda q: (-q[0],-q[2],-q[1])),
    (lambda q: (q[1],q[0],-q[2])),
    (lambda q: (q[1],-q[0],q[2])),
    (lambda q: (-q[1],q[0],q[2])),
    (lambda q: (-q[1],-q[0],-q[2])),
    (lambda q: (q[1],q[2],q[0])),
    (lambda q: (q[1],-q[2],-q[0])),
    (lambda q: (-q[1],q[2],-q[0])),
    (lambda q: (-q[1],-q[2],q[0])),
    (lambda q: (q[2],q[0],q[1])),
    (lambda q: (q[2],-q[0],-q[1])),
    (lambda q: (-q[2],q[0],-q[1])),
    (lambda q: (-q[2],-q[0],q[1])),
    (lambda q: (q[2],q[1],-q[0])),
    (lambda q: (q[2],-q[1],q[0])),
    (lambda q: (-q[2],q[1],q[0])),
    (lambda q: (-q[2],-q[1],-q[0])),
]

def compat(a1, a2):
    for ax, ay, az in a1:
        for bx, by, bz in a2:
            count = 0
            cx, cy, cz = ax-bx, ay-by, az-bz
            for gx, gy, gz in a2:
                if (gx+cx, gy+cy, gz+cz) in a1:
                    count += 1
            if count >= 12:
                return cx, cy, cz
    return None

def dfs(s1, a, visited):
    visited.add(s1)
    mx = []
    for s2 in a:
        if s2 in visited:
            continue
        a1 = a[s1]
        for rot in verts:
            a2 = [rot(k) for k in a[s2]]
            cc = compat(a1, a2)
            if cc is not None:
                dfs(s2, a, visited)
                mx.append((s2, rot, cc))
    for s2, rot, cc in mx:
        a2 = [rot(k) for k in a[s2]]
        cx, cy, cz = cc
        for bcn, cor in b[s2]:
            ncor = rot(cor)
            bx, by, bz = ncor
            b[s1].add((bcn, (bx+cx, by+cy, bz+cz)))

a = dict()
b = dict()
for line in sys.stdin:
    s = line.strip()
    if len(s) > 0 and s[4] == 's':
        reading = int(s.split()[2].strip())
    elif len(s) > 0:
        p = tuple(map(int,s.split(',')))
        cl.dict_add_to_list(a, reading, p)

for item in a:
    a[item] = set(a[item])
    b[item] = set([(item, (0, 0, 0))])

v = set()
dfs(0, a, v)

ans = 0
for ac, ao in b[0]:
    ax, ay, az = ao
    for bc, bo in b[0]:
        bx, by, bz = bo
        ans = max(ans, abs(ax-bx)+abs(ay-by)+abs(az-bz))
print(ans)