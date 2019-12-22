import sys
from collections import deque

def bfs(vs, vt, adj):
    q = deque()
    q.append(vs)
    dist = dict()
    dist[vs] = 0
    while len(q) > 0:
        p = q.popleft()
        if p == vt:
            return dist[p]
        for p2 in adj[p]:
            if p2 not in dist:
                dist[p2] = dist[p]+1
                q.append(p2)
    return None

N = 33
H = 117
W = 123
x = []
adj = dict()
lbl = dict()
dirs = ((1,0),(0,1))

def getCell(xx, yy):
    return x[xx+2][yy+2]

def getLabelUp(xx, yy):
    return x[xx+0][yy+2] + x[xx+1][yy+2]

def getLabelDown(xx, yy):
    return x[xx+3][yy+2] + x[xx+4][yy+2]

def getLabelLeft(xx, yy):
    return x[xx+2][yy+0] + x[xx+2][yy+1]

def getLabelRight(xx, yy):
    return x[xx+2][yy+3] + x[xx+2][yy+4]

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

for line in sys.stdin:
    x.append(line)
for i in range(H):
    for j in range(W):
        if getCell(i, j) == '.':
            for dx, dy in dirs:
                px = i+dx
                py = j+dy
                if getCell(px, py) == '.':
                    connect((i,j), (px, py))
# UP
for j in range(W):
    if getCell(0, j) == '.':
        addLabel(getLabelUp(0, j), (0, j))
for j in range(N, W-N):
    if getCell(H-N, j) == '.':
        addLabel(getLabelUp(H-N, j), (H-N, j))
# DOWN
for j in range(N, W-N):
    if getCell(N-1, j) == '.':
        addLabel(getLabelDown(N-1, j), (N-1, j))
for j in range(W):
    if getCell(H-1, j) == '.':
        addLabel(getLabelDown(H-1, j), (H-1, j))
# LEFT
for i in range(H):
    if getCell(i, 0) == '.':
        addLabel(getLabelLeft(i, 0), (i, 0))
for i in range(N, H-N):
    if getCell(i, W-N) == '.':
        addLabel(getLabelLeft(i, W-N), (i, W-N))
# RIGHT
for i in range(N, H-N):
    if getCell(i, N-1) == '.':
        addLabel(getLabelRight(i, N-1), (i, N-1))
for i in range(H):
    if getCell(i, W-1) == '.':
        addLabel(getLabelRight(i, W-1), (i, W-1))

for label in lbl:
    if len(lbl[label]) == 2:
        connect(lbl[label][0], lbl[label][1])

node_s = lbl['AA'][0]
node_t = lbl['ZZ'][0]
print(bfs(node_s, node_t, adj))