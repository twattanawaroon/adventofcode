import sys
import networkx as nx

ings = set()
algs = set()
c = []
for line in sys.stdin:
    s = line.strip()[:-1]
    s1, s2 = s.split('(contains ')
    x = set(s1.strip().split())
    y = set(s2.strip().split(', '))
    c.append((x, y))

for x, y in c:
    ings |= x
    algs |= y

m = dict()
for alg in algs:
    m[alg] = ings.copy()

for x, y in c:
    for alg in y:
        m[alg] &= x

for alg in algs:
    print(alg, m[alg])

alglist = list(algs)
alglist.sort()

g = nx.Graph(m)
matching = nx.algorithms.bipartite.matching.maximum_matching(g, top_nodes=algs)
print(','.join([matching[alg] for alg in alglist]))