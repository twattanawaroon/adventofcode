import sys

def get_color(s):
    return s.strip()[:-4].strip()

adj = dict()
for line in sys.stdin:
    s, t = line.strip()[:-1].split('contain')
    treqs = t.split(',')
    sc = get_color(s)
    for treq in treqs:
        tn, ttc = treq.strip().split(' ', 1)
        tc = get_color(ttc)
        if sc not in adj:
            adj[sc] = set()
        if tn != 'no':
            adj[sc].add((tc, int(tn)))

def dfs(adj, p):
    ans = 1
    if p in adj:
        for r, cr in adj[p]:
            ans += cr*dfs(adj, r)
    return ans

print(dfs(adj, 'shiny gold')-1)
