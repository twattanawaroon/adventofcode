import sys, math
import codelib as cl
from aocd import submit

adj = [dict()]
par = dict()
siz = dict()
nowdir = 0

def mkdir(nowdir, newdir):
    if newdir not in adj[nowdir]:
        nid = len(adj)
        adj.append(dict())
        adj[nowdir][newdir] = nid
        par[nid] = nowdir

for line in sys.stdin:
    s = line.strip().split()
    if s[0] == '$':
        if s[1] == 'cd':
            if s[2] == '/':
                nowdir = 0
            elif s[2] == '..':
                nowdir = par[nowdir]
            else:
                newdir = s[2]
                mkdir(nowdir, newdir)
                nowdir = adj[nowdir][newdir]
    else:
        a, b = s
        newdir = b
        mkdir(nowdir, newdir)
        if a != 'dir':
            siz[adj[nowdir][newdir]] = int(a)

def dfs(p):
    if p in siz:
        return 0
    siz[p] = 0
    for name in adj[p]:
        nid = adj[p][name]
        dfs(nid)
        siz[p] += siz[nid]
dfs(0)
need = siz[0]-40000000

def dfz(p):
    ans = siz[p] if siz[p] >= need else math.inf
    for name in adj[p]:
        nid = adj[p][name]
        ans = min(ans, dfz(nid))
    return ans
ansf = dfz(0)
submit(ansf, part="b", day=7, year=2022)