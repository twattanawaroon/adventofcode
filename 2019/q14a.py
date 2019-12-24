import sys

def dfs(e):
    visited.add(e)
    if e in adj:
        for elem in adj[e]:
            if elem not in visited:
                dfs(elem)
    if e != 'ORE':
        rmake, q = recipe[e]
        rdup = (need[e]+rmake-1)//rmake
        for qn, qe in q:
            need[qe] += qn*rdup

def parse(s):
    sn, se = s.strip().split()
    return (int(sn), se)

recipe = dict()
adj = dict()
need = dict()
visited = set()
need['ORE'] = 0

for line in sys.stdin:
    p, q = line.strip().split('=>')
    pl = p.split(',')
    px = list(map(parse, pl))
    qn, qe = parse(q)
    recipe[qe] = (qn, px)
    need[qe] = 0
    for pn, pe in px:
        if pe not in adj:
            adj[pe] = []
        adj[pe].append(qe)
need['FUEL'] = 1
dfs('ORE')
print(need['ORE'])