import sys

mons = ['                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   ']

def get_left(tile, n):
    return ''.join([tile[i][0]   for i in range(n)])

def get_right(tile, n):
    return ''.join([tile[i][n-1] for i in range(n)])

def get_top(tile, n):
    return ''.join([tile[0][i]   for i in range(n)])

def get_bottom(tile, n):
    return ''.join([tile[n-1][i] for i in range(n)])

def smaller(s):
    t = s[::-1]
    return s if s < t else t

def get_edges(tile):
    n = len(tile)
    ans = []
    ans.append(smaller(get_left(tile, n)))
    ans.append(smaller(get_right(tile, n)))
    ans.append(smaller(get_top(tile, n)))
    ans.append(smaller(get_bottom(tile, n)))
    return ans

def identity(tile):
    return tile

def flip(tile):
    n = len(tile)
    x = []
    for i in range(n):
        x.append(tile[i][::-1])
    return x

def rotate(tile):
    n = len(tile)
    x = []
    for i in range(n):
        x.append(''.join([tile[j][i] for j in range(n-1, -1, -1)]))
    return x

def get_transform(num):
    if num == 0:
        return identity
    elif num == 4:
        return flip
    else:
        return rotate

def orient(m, tid, check):
    for i in range(8):
        m[tid] = get_transform(i)(m[tid])
        if check(m[tid]):
            return True
    return False

def find(m, used, tids, check):
    for tid in tids:
        if tid not in used and orient(m, tid, check):
            return tid
    return None

def has_mon(g, mons, mm, nn, i, j):
    for ii in range(mm):
        for jj in range(nn):
            if mons[ii][jj] == '#' and g[i+ii][j+jj] == '.':
                return False
    return True

def mark_mon(g, mons, mm, nn, i, j):
    for ii in range(mm):
        for jj in range(nn):
            if mons[ii][jj] == '#':
                g[i+ii][j+jj] = 'O'

def mark_mons(g, mons):
    n = len(g)
    mm = len(mons)
    nn = len(mons[0])
    for i in range(n-mm+1):
        for j in range(n-nn+1):
            if has_mon(g, mons, mm, nn, i, j):
                mark_mon(g, mons, mm, nn, i, j)

m = dict()
for line in sys.stdin:
    s = line.strip()
    if len(s) == 0:
        m[tid] = x
    elif s[-1] == ':':
        tid = int(s[:-1].split()[1])
        x = []
    else:
        x.append(s)
        n = len(s)

jn = dict()
adj = dict()
for tid in m:
    adj[tid] = []
    edges = get_edges(m[tid])
    for e in edges:
        if e not in jn:
            jn[e] = []
        jn[e].append(tid)

count = 0
for e in jn:
    if len(jn[e]) == 2:
        p1, p2 = jn[e]
        adj[p1].append(p2)
        adj[p2].append(p1)

used = set()
corner = None
for tid in m:
    if len(adj[tid]) == 2:
        corner = tid
        break
orient(m, corner, lambda x: len(jn[smaller(get_top(x, n))]) == 1 and len(jn[smaller(get_left(x, n))]) == 1)
used.add(corner)

grid = []
r = int(len(m)**0.5)
for i in range(r):
    row = []
    if i == 0:
        row.append(corner)
    else:
        c = grid[-1][0]
        d = find(m, used, adj[c], lambda x: get_top(x, n) == get_bottom(m[c], n))
        row.append(d)
        used.add(d)
    for j in range(1, r):
        c = row[-1]
        d = find(m, used, adj[c], lambda x: get_left(x, n) == get_right(m[c], n))
        row.append(d)
        used.add(d)
    grid.append(row)

final = []
for row in grid:
    for i in range(1, n-1):
        final.append(''.join([m[item][i][1:-1] for item in row]))

for i in range(8):
    final = get_transform(i)(final)
    for i in range(len(final)):
        final[i] = [c for c in final[i]]
    mark_mons(final, mons)
    for i in range(len(final)):
        final[i] = ''.join(final[i])

print(sum([row.count('#') for row in final]))