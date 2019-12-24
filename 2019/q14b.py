import sys

def makeFuel(fuel):
    need = dict()
    visited = set()
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
                if qe not in need:
                    need[qe] = 0
                need[qe] += qn*rdup

    need['ORE'] = 0
    need['FUEL'] = fuel
    dfs('ORE')
    return need['ORE']

def parse(s):
    sn, se = s.strip().split()
    return (int(sn), se)

recipe = dict()
adj = dict()

for line in sys.stdin:
    p, q = line.strip().split('=>')
    pl = p.split(',')
    px = list(map(parse, pl))
    qn, qe = parse(q)
    recipe[qe] = (qn, px)
    for pn, pe in px:
        if pe not in adj:
            adj[pe] = []
        adj[pe].append(qe)

ans = 0
l = 0
r = 10**20
while l <= r:
    m = (l+r)//2
    if makeFuel(m) <= 10**12:
        ans = m
        l = m+1
    else:
        r = m-1
print(ans)