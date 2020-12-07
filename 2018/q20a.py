import sys
from collections import deque
doffsets = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}

def makeadj(adj, ap, aq):
    if ap not in adj:
        adj[ap] = set()
    if aq not in adj:
        adj[aq] = set()
    adj[ap].add(aq)
    adj[aq].add(ap)

def makepath(adj, apx, apy, apd):
    dx, dy = doffsets[apd]
    makeadj(adj, (apx, apy), (apx+dx, apy+dy))

def read(s, state):
    if state[0] >= len(s)-1:
        return ')'
    else:
        c = s[state[0]]
        state[0] += 1
        return c

def node(s, state):
    locs = set([(0, 0)])
    adj = set()
    while True:
        c = read(s, state)
        if c == ')':
            return locs, adj, False
        elif c == '|':
            return locs, adj, True
        elif c == '(':
            offsets = set()
            adks = set()
            more = True
            while more:
                glocs, adk, more = node(s, state)
                offsets |= glocs
                adks |= adk
            newlocs = set()
            for lx, ly in locs:
                for ox, oy, od in adks:
                    adj.add((lx+ox, ly+oy, od))
            for lx, ly in locs:
                for ox, oy in offsets:
                    newlocs.add((lx+ox, ly+oy))
            locs = newlocs
        else:
            ox, oy = doffsets[c]
            newlocs = set()
            for lx, ly in locs:
                adj.add((lx, ly, c))
                newlocs.add((lx+ox, ly+oy))
            locs = newlocs

def bfs(adj):
    q = deque()
    dist = dict()
    q.append((0, 0))
    dist[(0, 0)] = 0
    ap = None
    while len(q) > 0:
        ap = q.popleft()
        for aq in adj[ap]:
            if aq not in dist:
                dist[aq] = dist[ap]+1
                q.append(aq)
    return dist[ap]

for line in sys.stdin:
    s = line.strip()
    state = [1]
    locs, adk, more = node(s, state)
    adj = dict()
    for apx, apy, apd in adk:
        makepath(adj, apx, apy, apd)
    print(bfs(adj))
