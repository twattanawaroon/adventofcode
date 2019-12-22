import sys
from collections import deque

def bfs(ws, wt, adj, adj_up, adj_dn):
    q = deque()
    q.append(ws)
    dist = dict()
    dist[ws] = 0
    while len(q) > 0:
        p = q.popleft()
        if p == wt:
            return dist[p]
        vp, dp = p
        for vq in adj[vp]:
            if (vq, dp) not in dist:
                dist[(vq, dp)] = dist[p]+1
                q.append((vq, dp))
        if vp in adj_up and (adj_up[vp], dp+1) not in dist:
            dist[(adj_up[vp], dp+1)] = dist[p]+1
            q.append((adj_up[vp], dp+1))
        if dp > 0 and vp in adj_dn and (adj_dn[vp], dp-1) not in dist:
            dist[(adj_dn[vp], dp-1)] = dist[p]+1
            q.append((adj_dn[vp], dp-1))
    return None

N = 33
H = 117
W = 123
x = []
adj = dict()
adj_up = dict()
adj_dn = dict()
lbl_out = dict()
lbl_inn = dict()
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

def connectUpDn(p1, p2):
    adj_up[p1] = p2
    adj_dn[p2] = p1

def addLabelOut(label, p):
    lbl_out[label] = p

def addLabelInn(label, p):
    lbl_inn[label] = p

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
        addLabelOut(getLabelUp(0, j), (0, j))
for j in range(N, W-N):
    if getCell(H-N, j) == '.':
        addLabelInn(getLabelUp(H-N, j), (H-N, j))
# DOWN
for j in range(N, W-N):
    if getCell(N-1, j) == '.':
        addLabelInn(getLabelDown(N-1, j), (N-1, j))
for j in range(W):
    if getCell(H-1, j) == '.':
        addLabelOut(getLabelDown(H-1, j), (H-1, j))
# LEFT
for i in range(H):
    if getCell(i, 0) == '.':
        addLabelOut(getLabelLeft(i, 0), (i, 0))
for i in range(N, H-N):
    if getCell(i, W-N) == '.':
        addLabelInn(getLabelLeft(i, W-N), (i, W-N))
# RIGHT
for i in range(N, H-N):
    if getCell(i, N-1) == '.':
        addLabelInn(getLabelRight(i, N-1), (i, N-1))
for i in range(H):
    if getCell(i, W-1) == '.':
        addLabelOut(getLabelRight(i, W-1), (i, W-1))

for label in lbl_out:
    if label in lbl_inn:
        connectUpDn(lbl_inn[label], lbl_out[label])

node_s = lbl_out['AA']
node_t = lbl_out['ZZ']
print(bfs((node_s, 0), (node_t,0), adj, adj_up, adj_dn))