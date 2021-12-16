import sys

def add_adj(adj, a, b):
    if a not in adj:
        adj[a] = []
    adj[a].append(b)

def low(q):
    return 'a' <= q[0] <= 'z'

def dfs(adj, p, v, doubled):
    if p == 'end':
        return 1
    ans = 0
    for q in adj[p]:
        if q == 'start':
            continue
        if low(q) and q not in v:
            v.add(q)
            ans += dfs(adj, q, v, doubled)
            v.remove(q)
        elif low(q) and not doubled:
            ans += dfs(adj, q, v, True)
        elif not low(q):
            ans += dfs(adj, q, v, doubled)
    return ans

score = 0
adj = dict()
for line in sys.stdin:
    x1, y1 = line.strip().split('-')
    add_adj(adj, x1, y1)
    add_adj(adj, y1, x1)

score = dfs(adj, 'start', set(['start']), False)

print(score)
