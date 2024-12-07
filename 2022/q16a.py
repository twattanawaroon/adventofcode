import sys
import codelib as cl

adj = dict()
rat = dict()
gvs = []
ansf = 0
for line in sys.stdin:
    sz = line.strip()
    if len(sz) == 0:
        continue
    s1, s2 = sz.split('valve')
    ss = s1.split()
    p = ss[1]
    rat[p] = int(ss[4][5:-1])
    adj[p] = s2[1:].strip().split(', ')
    if rat[p] > 0:
        gvs.append(p)

apsp = dict()
for item in ['AA']+gvs:
    apsp[item] = cl.shortest_path_bfs(cl.dict_lambda(adj), item)

count = 0
visited = dict()
for item in gvs:
    visited[item] = False


def dfs(p, t, score):
    bval = score
    for item in gvs:
        if visited[item]:
            continue
        visited[item] = True
        newt = t+apsp[p][item]+1
        if newt <= 30:
            newscore = score+(30-newt)*rat[item]
            bval = max(bval, dfs(item, newt, newscore))
        visited[item] = False
    return bval


print(dfs('AA', 0, 0))
