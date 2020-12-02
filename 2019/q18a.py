import sys
import heapq
from collections import deque

KEYS = 26

def cleared(kmap, p):
    i = ord(p)-ord('A')
    return kmap[i]

def bfs(ps, kmap, adj, loc):
    vs = loc[ps]
    q = deque()
    q.append(vs)
    dist = dict()
    ans = dict()
    dist[vs] = 0
    while len(q) > 0:
        p = q.popleft()
        pi, pj = p
        if 'a' <= getCell(pi, pj) <= 'z':
            ans[getCell(pi, pj)] = dist[p]
        for pt in adj[p]:
            pti, ptj = pt
            if 'A' <= getCell(pti, ptj) <= 'Z' and not cleared(kmap, getCell(pti, ptj)):
                continue
            if pt not in dist:
                dist[pt] = dist[p]+1
                q.append(pt)
    return ans

def getRest(kmap):
    return [chr(ord('a')+i) for i in range(KEYS) if not kmap[i]]

def mergeMap(kmap, p):
    i = ord(p)-ord('a')
    klis = list(kmap)
    klis[i] = True
    return tuple(klis)

def sssp(sv, adj, loc):
    snode = (sv, (False,)*KEYS)
    q = [(0, snode)]
    dist = dict()
    dist[snode] = 0
    while len(q) > 0:
        pd, pnode = heapq.heappop(q)
        pv, pkmap = pnode
        if dist[pnode] != pd:
            continue
        #print(pnode)
        if all(pkmap):
            return dist[pnode]
        dmap = bfs(pv, pkmap, adj, loc)
        rest = getRest(pkmap)
        for qv in rest:
            if qv not in dmap:
                continue
            qnode = (qv, mergeMap(pkmap, qv))
            if qnode not in dist:
                dist[qnode] = dist[pnode]+dmap[qv]
                heapq.heappush(q, (dist[qnode], qnode))
            elif dist[qnode] > dist[pnode]+dmap[qv]:
                dist[qnode] = dist[pnode]+dmap[qv]
                heapq.heappush(q, (dist[qnode], qnode))
    return None

x = []
adj = dict()
loc = dict()
dirs_one = ((1,0),(0,1))

def connect(p1, p2):
    if p1 not in adj:
        adj[p1] = []
    adj[p1].append(p2)
    if p2 not in adj:
        adj[p2] = []
    adj[p2].append(p1)

def addLabel(label, p):
    if label not in lbl:
        lbl[label] = []
    lbl[label].append(p)

def getCell(i, j):
    if 0 <= i < H and 0 <= j < W:
        return x[i][j]
    return '#'

for line in sys.stdin:
    x.append(line)
H = len(x)
W = len(x[0])
for i in range(H):
    for j in range(W):
        if 'a' <= getCell(i, j) <= 'z' or getCell(i, j) == '@':
            loc[getCell(i, j)] = (i, j)
        if getCell(i, j) != '#':
            for dx, dy in dirs_one:
                px = i+dx
                py = j+dy
                if getCell(px, py) != '#':
                    connect((i,j), (px, py))

print(sssp('@', adj, loc))