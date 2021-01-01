import sys

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

jn = dict()
deg = dict()
for tid in m:
    deg[tid] = 0
    edges = get_edges(m[tid])
    for e in edges:
        if e not in jn:
            jn[e] = []
        jn[e].append(tid)

count = 0
for e in jn:
    if len(jn[e]) == 2:
        p1, p2 = jn[e]
        deg[p1] += 1
        deg[p2] += 1

ans = 1
for tid in m:
    if deg[tid] == 2:
        ans *= tid
print(ans)