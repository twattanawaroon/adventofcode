import sys

adj = dict()
visited = set()

def dfs(p, dist):
    visited.add(p)
    if p == 'SAN':
        print(dist-2)
    for q in adj[p]:
        if q not in visited:
            dfs(q, dist+1)

for line in sys.stdin:
    ea, eb = line.strip().split(')')
    if ea not in adj:
        adj[ea] = []
    if eb not in adj:
        adj[eb] = []
    adj[ea].append(eb)
    adj[eb].append(ea)

dfs('YOU', 0)