import sys

def getm(m, i, j, t):
    return (i,j,t) in m

def matchv(normal_rule, term_rule, rule_order, s):
    n = len(s)
    m = set()
    for dj in range(n):
        for i in range(n-dj):
            j = i+dj
            for t in rule_order:
                z = False
                if t in term_rule and dj == 0:
                    if term_rule[t] == s[i]:
                        z = True
                if t in normal_rule:
                    z = False
                    for rule in normal_rule[t]:
                        if len(rule) == 1:
                            t1 = rule[0]
                            z = z or getm(m,i,j,t1)
                        elif len(rule) == 2:
                            t1, t2 = rule
                            z = z or any([getm(m,i,k,t1) and getm(m,k+1,j,t2) for k in range(i,j)])
                        else:
                            print('fail')
                if z:
                    m.add((i,j,t))
    return (0,n-1,0) in m

def dfs(edge, rule_order, visited, p):
    visited.add(p)
    if p in edge:
        for q in edge[p]:
            if q not in visited:
                dfs(edge, rule_order, visited, q)
    rule_order.append(p)

def process_rule(normal_rule, term_rule, edge, s):
    pa, pb = s.split(':')
    za = int(pa.strip())
    if pb.count('"') > 0:
        # letter rule
        zb = pb.strip()[1]
        term_rule[za] = zb
    else:
        # normal rule
        zbs = pb.strip().split('|')
        normal_rule[za] = []
        if za not in edge:
            edge[za] = set()
        for zc in zbs:
            pcs = tuple(map(int,zc.strip().split()))
            normal_rule[za].append(pcs)
            for pc in pcs:
                edge[za].add(pc)

x = []
normal_rule = dict()
term_rule = dict()
rule_order = []
visited = set()
edge = dict()
edged = False
n1 = set()
n2 = set()
ans = 0
cnt = 0
for line in sys.stdin:
    s = line.strip()
    if len(s) > 0 and s.count(':') > 0:
        if s.startswith('8:'):
            process_rule(normal_rule, term_rule, edge, '8: 42 | 42 8')
        elif s.startswith('11:'):
            process_rule(normal_rule, term_rule, edge, '11: 42 31 | 42 999')
            process_rule(normal_rule, term_rule, edge, '999: 11 31')
        else:
            process_rule(normal_rule, term_rule, edge, s)
    elif len(s) > 0:
        if not edged:
            dfs(edge, rule_order, visited, 0)
            edged = True
        r = matchv(normal_rule, term_rule, rule_order, s)
        cnt += 1
        print(r, cnt)
        if r:
            ans += 1
print(ans)
